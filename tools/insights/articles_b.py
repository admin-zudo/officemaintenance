# Article content, part B.

ARTICLES = []

# ------------------------------------------------------------------ Deluge examples
ARTICLES.append(dict(
    slug='deluge-script-examples',
    title='Deluge Script Examples: 10 Real Automations for Zoho CRM, Creator and Books',
    seo_title='Deluge Script Examples: 10 Real Zoho CRM, Creator and Books Automations',
    description='Ten practical Deluge script examples we use in real projects: creating invoices from won deals, blocking duplicates, follow-up tasks, scheduled reminders, API calls, Creator validation and more.',
    lead='Deluge is the scripting language behind Zoho CRM functions, Zoho Creator apps, Zoho Books custom functions and more. These are ten scripts based on the automations we write most often, with notes on how and where to use them.',
    category='Deluge', keyword='deluge script examples',
    published='2026-10-08', modified='2026-10-08',
    cover_alt='A code editor showing a Deluge function that turns a won Zoho CRM deal into a Zoho Books invoice',
    caption='Small Deluge functions remove the manual steps between Zoho apps.',
    related=['zoho-creator-vs-power-apps', 'migrate-hubspot-salesforce-to-zoho-crm', 'zoho-crm-implementation-cost'],
    body='''
<p>Deluge (Data Enriched Language for the Universal Grid Environment) is Zoho&rsquo;s own scripting language. It is deliberately simple: maps, lists, loops and built-in tasks such as <code>zoho.crm.getRecordById</code> or <code>zoho.books.createRecord</code> that talk to other Zoho apps without you handling authentication yourself.</p>
<p>The examples below are simplified versions of scripts we use in client projects. Field API names in your account will differ, so treat them as patterns, not copy-and-paste solutions. Always test in a sandbox or on test records first.</p>

<h2 id="before-you-start">Before you start</h2>
<ul>
  <li><strong>Where Deluge runs:</strong> in Zoho CRM as functions attached to workflow rules, buttons, Blueprint transitions or schedules; in Zoho Creator on form and report events; in Zoho Books as custom functions and workflow actions.</li>
  <li><strong>Field names:</strong> use API names, not display labels. In Zoho CRM you can see them under <em>Setup &gt; Developer Hub &gt; APIs</em>.</li>
  <li><strong>Connections:</strong> calls to other services, including some Zoho apps, use a named connection that stores OAuth credentials. Create it once under <em>Connections</em> and reference it by name.</li>
  <li><strong>Debugging:</strong> use <code>info</code> to print values while testing. Remove noisy output before going live.</li>
</ul>

<h2 id="deal-to-invoice">1. Create a Zoho Books invoice when a CRM deal is won</h2>
<p>Use this as a workflow function on the Deals module, triggered when the stage changes to <em>Closed Won</em>. It assumes each account stores its Zoho Books customer ID in a custom field.</p>
<pre><code>// Argument: dealId (mapped to the Deal ID in the workflow)
deal = zoho.crm.getRecordById("Deals", dealId);
account = zoho.crm.getRecordById("Accounts", deal.get("Account_Name").get("id"));
customerId = account.get("Books_Customer_ID");
if (customerId == null)
{
    info "No Books customer linked to this account";
    return;
}
lineItem = Map();
lineItem.put("name", deal.get("Deal_Name"));
lineItem.put("rate", deal.get("Amount"));
lineItem.put("quantity", 1);
items = List();
items.add(lineItem);
invoice = Map();
invoice.put("customer_id", customerId);
invoice.put("reference_number", deal.get("Deal_Name"));
invoice.put("line_items", items);
response = zoho.books.createRecord("invoices", "YOUR_ORG_ID", invoice, "zbooks");
info response.get("message");</code></pre>
<p><strong>Why it helps:</strong> no one re-types deal values into accounting, and the invoice reference ties back to the deal.</p>

<h2 id="block-duplicates">2. Flag duplicate contacts by email</h2>
<p>Zoho CRM can block exact duplicates on unique fields, but contacts often arrive through imports and integrations with slightly different data. This function runs on contact creation and flags the new record if another contact already has the same email.</p>
<pre><code>// Argument: contactId
contact = zoho.crm.getRecordById("Contacts", contactId);
email = contact.get("Email");
if (email != null &amp;&amp; email != "")
{
    matches = zoho.crm.searchRecords("Contacts", "(Email:equals:" + email + ")");
    if (matches.size() &gt; 1)
    {
        update = Map();
        update.put("Possible_Duplicate", true);
        zoho.crm.updateRecord("Contacts", contactId, update);
    }
}</code></pre>
<p>A saved view filtered on <em>Possible Duplicate</em> then gives an admin a daily clean-up list.</p>

<h2 id="follow-up-task">3. Create a follow-up task when a lead is contacted</h2>
<pre><code>// Argument: leadId. Trigger: Lead Status changes to "Contacted"
lead = zoho.crm.getRecordById("Leads", leadId);
task = Map();
task.put("Subject", "Follow up with " + lead.get("Full_Name"));
task.put("Due_Date", zoho.currentdate.addDay(3).toString("yyyy-MM-dd"));
task.put("What_Id", leadId);
task.put("$se_module", "Leads");
task.put("Owner", lead.get("Owner").get("id"));
zoho.crm.createRecord("Tasks", task);</code></pre>
<p><strong>Why it helps:</strong> follow-ups stop depending on memory, and managers can report on overdue tasks.</p>

<h2 id="stale-deals">4. Email owners about deals past their closing date</h2>
<p>Schedule this function to run every weekday morning.</p>
<pre><code>today = zoho.currentdate.toString("yyyy-MM-dd");
deals = zoho.crm.searchRecords("Deals", "((Closing_Date:less_than:" + today + ")and(Stage:not_equal:Closed Won)and(Stage:not_equal:Closed Lost))");
for each deal in deals
{
    owner = deal.get("Owner");
    sendmail
    [
        from: zoho.adminuserid
        to: owner.get("email")
        subject: "Deal past closing date: " + deal.get("Deal_Name")
        message: "Please update the stage or closing date for " + deal.get("Deal_Name") + "."
    ]
}</code></pre>
<p>Search results are paginated, so for large pipelines loop through pages with the page parameter of <code>searchRecords</code>.</p>

<h2 id="call-api">5. Call an external API and save the result</h2>
<p>This pattern fetches data from another system with <code>invokeurl</code> and writes it back to the record. Here a custom button looks up a company in an external service using a stored connection.</p>
<pre><code>// Argument: accountId
account = zoho.crm.getRecordById("Accounts", accountId);
response = invokeurl
[
    url: "https://api.example.com/companies?domain=" + account.get("Website")
    type: GET
    connection: "example_api"
];
if (response.get("employees") != null)
{
    update = Map();
    update.put("Employees", response.get("employees"));
    zoho.crm.updateRecord("Accounts", accountId, update);
}
return "Company details updated";</code></pre>

<h2 id="creator-validation">6. Validate a Zoho Creator form before it is saved</h2>
<p>Put this in the form&rsquo;s <em>On Validate</em> event. It stops the record from saving and shows a message.</p>
<pre><code>if (input.Quantity &lt;= 0)
{
    alert "Quantity must be at least 1.";
    cancel submit;
}
if (input.Delivery_Date &lt; zoho.currentdate)
{
    alert "Delivery date cannot be in the past.";
    cancel submit;
}</code></pre>

<h2 id="creator-insert">7. Keep an activity log in Zoho Creator</h2>
<p>In the <em>On Success</em> event of an Orders form, add a row to a separate log form. This gives you a simple audit trail that reports and dashboards can use.</p>
<pre><code>insert into Activity_Log
[
    Added_User = zoho.loginuser
    Order = input.ID
    Action = "Order " + input.Status
    Logged_At = zoho.currenttime
];</code></pre>

<h2 id="creator-aggregate">8. Totals and counts across related records</h2>
<p>Creator can fetch and aggregate records directly. This example updates a customer&rsquo;s open order count and total value whenever an order is saved.</p>
<pre><code>openOrders = Orders[Customer == input.Customer &amp;&amp; Status == "Open"];
customer = Customers[ID == input.Customer];
customer.Open_Orders = openOrders.count();
customer.Open_Value = Orders[Customer == input.Customer &amp;&amp; Status == "Open"].sum(Amount);</code></pre>

<h2 id="dates">9. Working with dates</h2>
<p>Date logic comes up in almost every project: SLAs, renewals, reminders. A few useful patterns:</p>
<pre><code>start = toDate("2026-01-15", "yyyy-MM-dd");
renewal = start.addYear(1);
daysLeft = zoho.currentdate.daysBetween(renewal);
if (daysLeft &lt;= 30)
{
    info "Renewal due in " + daysLeft + " days";
}
weekday = zoho.currentdate.getDayOfWeek();  // 1 = Sunday ... 7 = Saturday</code></pre>

<h2 id="error-handling">10. Handle errors instead of failing silently</h2>
<p>Scripts that call other systems will eventually meet a timeout or an unexpected response. Wrap risky calls and record what happened.</p>
<pre><code>try
{
    response = zoho.books.createRecord("invoices", "YOUR_ORG_ID", invoice, "zbooks");
    if (response.get("code") != 0)
    {
        info "Books returned an error: " + response.get("message");
    }
}
catch (e)
{
    sendmail
    [
        from: zoho.adminuserid
        to: "admin@yourcompany.com"
        subject: "Invoice automation failed"
        message: "Deal: " + dealId + "<br>Error: " + e
    ]
}</code></pre>

<h2 id="good-habits">Good habits for maintainable Deluge</h2>
<ul>
  <li><strong>One job per function.</strong> Small functions are easier to test and reuse.</li>
  <li><strong>Comment the why, not the what.</strong> The next developer can read the code; they can&rsquo;t read your reasons.</li>
  <li><strong>Check for nulls</strong> before calling <code>.get()</code> on lookups that may be empty.</li>
  <li><strong>Mind the limits.</strong> Each Zoho product sets limits on function execution time, API calls and emails per day. Batch work in scheduled functions rather than firing one call per record.</li>
  <li><strong>Keep a list of automations</strong>: name, trigger, what it does, who owns it. It is the most useful document in any Zoho account.</li>
</ul>
<p>If you have scripts that work but nobody understands, or automations you would like to build, our <a href="/deluge-development/">Deluge development</a> service covers new functions, reviews and fixes.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('What is Deluge in Zoho?',
         'Deluge is Zoho\'s scripting language. It runs inside Zoho CRM, Zoho Creator, Zoho Books, Zoho Desk and other Zoho apps, and has built-in tasks for reading and writing records across Zoho products, sending email and calling external APIs.'),
        ('Is Deluge hard to learn?',
         'Not for anyone who has written a spreadsheet formula or a little code. The syntax is small: maps, lists, conditions, loops and built-in tasks. The harder part is knowing each Zoho app\'s field API names, limits and events.'),
        ('Where do I write Deluge in Zoho CRM?',
         'Under Setup, in Developer Hub, then Functions. Functions can be attached to workflow rules, custom buttons, Blueprint transitions, related lists or schedules.'),
        ('Can Deluge call non-Zoho APIs?',
         'Yes. The invokeurl task calls any REST API. Store credentials in a named connection so tokens are refreshed automatically and secrets are not written into the script.'),
    ],
))

# ------------------------------------------------------------------ Agentic AI (rewrite)
ARTICLES.append(dict(
    slug='zoho-agentic-ai-hyperautomation',
    title='AI Agents in Zoho CRM: What They Can Do Today and How to Prepare',
    seo_title='AI Agents and Automation in Zoho CRM: A Practical Guide (2026)',
    description='A practical look at AI in Zoho CRM: what Zia and AI agents can realistically handle, where automation still needs rules and human approval, and how to prepare your CRM data and processes.',
    lead='&ldquo;Agentic AI&rdquo; is the phrase of the year, and every software vendor has a version of it. Underneath the marketing there is something genuinely useful for CRM teams, as long as the data and processes underneath are in good shape. Here is a grounded view.',
    category='AI and automation', keyword='zoho crm ai agents',
    published='2026-09-15', modified='2026-10-08',
    cover_alt='A Zoho CRM deal record with an AI assistant panel suggesting a next step that waits for human approval',
    caption='The useful version of AI in a CRM suggests and drafts; a person approves anything that matters.',
    related=['zoho-mcp-claude-chatgpt', 'zoho-analytics-agentic-data-foundations-2026', 'deluge-script-examples'],
    body='''
<p>Traditional CRM automation follows rules you write: <em>when a deal reaches this stage, send this email</em>. AI agents are different. You give them a goal and access to tools, and they decide which steps to take. That makes them flexible, and it also makes them risky if they are pointed at messy data or given too much freedom.</p>
<p>This article explains what that means in Zoho CRM specifically, what we recommend clients automate with AI today, and what they should keep under rules and human approval.</p>

<h2 id="what-is-agentic">What &ldquo;agentic&rdquo; actually means</h2>
<p>An AI agent is a language model connected to tools. Instead of only answering a question, it can look up records, draft an email, update a field or call another system, step by step, until a goal is reached. In a CRM, that might mean:</p>
<ul>
  <li>Reading a new inbound enquiry, finding the matching account and drafting a reply.</li>
  <li>Summarizing a deal&rsquo;s history before a call.</li>
  <li>Spotting deals that have gone quiet and proposing a next action.</li>
  <li>Filling in missing fields from emails and call notes.</li>
</ul>
<p>The difference from a workflow rule is judgment. The difference from a human is that the agent has no context beyond what your CRM data and instructions give it.</p>

<h2 id="zoho-ai-today">AI in the Zoho ecosystem today</h2>
<p>Zoho&rsquo;s AI assistant is <strong>Zia</strong>, which has been part of Zoho CRM for years. Depending on your edition, it provides lead and deal predictions, anomaly detection in sales trends, best-time-to-contact suggestions, email sentiment, data enrichment and a conversational assistant for questions such as &ldquo;show me deals closing this month&rdquo;.</p>
<p>In 2025 Zoho announced a bigger step: its own large language model (Zia LLM), prebuilt <strong>Zia Agents</strong> and an <strong>Agent Studio</strong> for building custom agents across Zoho apps. Zoho has also supported connecting third-party models such as OpenAI to Zia. Availability of these features varies by product, edition and region, and it is changing quickly, so check what is enabled in your own account before planning around a specific capability. Zoho also offers an MCP service that lets outside assistants such as Claude and ChatGPT work with your Zoho data; our <a href="/insights/zoho-mcp-claude-chatgpt/">Zoho MCP guide</a> covers how to set it up safely.</p>
<p>The important point for planning is this: whichever model or agent you use, it acts on your CRM data through the same modules, fields and permissions your team uses. The quality of that foundation decides whether AI helps or creates noise.</p>

<h2 id="good-uses">Where AI helps most right now</h2>
<ol>
  <li><strong>Summaries.</strong> Turning a long deal or ticket history into five lines before a call. Low risk, high time saving.</li>
  <li><strong>Drafting.</strong> First drafts of follow-up emails, proposals and call notes that a person edits and sends.</li>
  <li><strong>Data hygiene.</strong> Suggesting missing fields, standardizing company names and flagging likely duplicates for review.</li>
  <li><strong>Prioritization.</strong> Ranking leads or deals by likelihood to convert, so reps spend time where it counts.</li>
  <li><strong>Internal questions.</strong> Answering &ldquo;which accounts in Texas haven&rsquo;t ordered this quarter?&rdquo; without building a report.</li>
</ol>

<h2 id="keep-rules">What should stay rule-based or human-approved</h2>
<p>Some actions are cheap to get right with a rule and expensive to get wrong with a guess:</p>
<ul>
  <li><strong>Money:</strong> discounts, invoices, refunds and payment terms.</li>
  <li><strong>Commitments:</strong> anything sent to a customer that promises a price, date or scope.</li>
  <li><strong>Deletion and merging</strong> of records.</li>
  <li><strong>Stage changes</strong> that trigger downstream processes, such as provisioning or handover to delivery.</li>
</ul>
<p>For these, use Blueprint transitions, approval processes and Deluge functions with clear conditions, and let AI suggest rather than act. A simple pattern we use is to have the agent write its proposed action into a field or a task, and have a person approve it with one click.</p>

<h2 id="prepare-data">How to prepare your CRM for AI</h2>
<h3>1. Clean the data</h3>
<p>Duplicates, empty fields and inconsistent picklists confuse people and models equally. Deduplicate accounts and contacts, make key fields mandatory at the right stage, and standardize values such as industry and lead source.</p>
<h3>2. Make the process explicit</h3>
<p>If your sales process only exists in people&rsquo;s heads, an agent cannot follow it. Map it in Blueprint with required fields at each step. That alone improves reporting, even before any AI is involved.</p>
<h3>3. Capture context in the CRM</h3>
<p>Connect email and calendars, log calls and keep notes on the record. AI summaries and suggestions are only as good as the history they can read.</p>
<h3>4. Set permissions deliberately</h3>
<p>Agents act with the permissions they are given. Use roles and profiles so that an assistant working for a sales rep sees what that rep should see, and nothing more.</p>
<h3>5. Keep an audit trail</h3>
<p>Log automated changes, for example with a custom field showing the source of an update or a log module written by Deluge. When something goes wrong you need to know whether a person, a rule or an agent made the change.</p>

<h2 id="start-small">Start with one measurable use case</h2>
<p>Pick one repetitive task, such as summarizing deals before weekly pipeline reviews or drafting first replies to web enquiries. Measure the time it takes today, run AI on it for a month with human review, and compare. If it saves time without creating clean-up work, extend it. If not, you have learned cheaply.</p>
<p>Most of the work in a successful AI rollout is the unglamorous part: data quality, clear processes and permissions. That is also where an experienced Zoho developer adds the most value. If you would like help getting your Zoho CRM ready, see our <a href="/zoho-crm-development/">Zoho CRM implementation</a> service.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Does Zoho CRM have AI agents?',
         'Zoho CRM includes Zia, an AI assistant with predictions, anomaly detection, enrichment and a conversational interface, depending on edition. In 2025 Zoho also announced Zia Agents and an Agent Studio for building agents across Zoho apps. Check which features are enabled for your edition and region.'),
        ('Is it safe to let AI update CRM records?',
         'For low-risk fields and suggestions, yes, with logging. For anything involving money, customer commitments, deletion or stage changes that trigger other processes, keep rules and human approval in place and let AI propose rather than act.'),
        ('What should we do before adding AI to Zoho CRM?',
         'Clean and deduplicate data, define the sales process in Blueprint, connect email and calendars so history is captured, set role-based permissions and keep an audit trail of automated changes.'),
    ],
))

# ------------------------------------------------------------------ Zoho MCP
ARTICLES.append(dict(
    slug='zoho-mcp-claude-chatgpt',
    title='Zoho MCP: How to Connect Claude or ChatGPT to Zoho CRM Safely',
    seo_title='Zoho MCP: Connect Claude or ChatGPT to Zoho CRM Safely (2026 Guide)',
    description='What Zoho MCP is, what you need on the Zoho, Claude and ChatGPT side, how to set it up, which authorization mode to choose, and which actions an AI assistant should and should not be allowed to take.',
    lead='Zoho MCP lets an AI assistant such as Claude or ChatGPT read and change records in your Zoho apps from a chat window. Setting it up takes minutes. Deciding what the assistant is allowed to do is the part that deserves your time.',
    category='AI and automation', keyword='zoho mcp',
    published='2026-10-09', modified='2026-10-09',
    cover_alt='Diagram of an AI assistant connected to a Zoho MCP server: read allowed from day one, create with confirmation, delete kept out',
    caption='The assistant can only use the tools you add to the MCP server, so the tool list is your main control.',
    related=['zoho-agentic-ai-hyperautomation', 'deluge-script-examples', 'zoho-analytics-agentic-data-foundations-2026'],
    body='''
<p>Until recently, asking an AI assistant about your CRM meant exporting a spreadsheet and pasting it into a chat. The Model Context Protocol (MCP) removes that step. It is an open standard, introduced by Anthropic in late 2024, that lets an AI assistant call tools in other systems. Zoho now offers its own MCP service, so an assistant can search deals, create tasks or draft invoices in your Zoho account directly.</p>
<p>This guide covers what Zoho MCP is, how to set it up, and the decisions that keep it safe. The product is new and changing quickly, so we link to Zoho&rsquo;s own documentation for anything that is likely to move. The details here were checked in October 2026.</p>

<h2 id="what-is-zoho-mcp">What Zoho MCP is</h2>
<p>Zoho MCP is a service where you create <strong>MCP servers</strong>. A server is a named set of <strong>tools</strong>, and each tool is one action in one app, such as &ldquo;search records&rdquo; in Zoho CRM or &ldquo;create invoice&rdquo; in Zoho Books. You then give the server&rsquo;s address to an AI assistant, which Zoho calls the <strong>MCP client</strong>.</p>
<p>Three points are worth understanding before you start:</p>
<ul>
  <li><strong>Zoho MCP is not an AI.</strong> The intelligence comes from the assistant you connect. Zoho MCP only gives it a controlled way to act.</li>
  <li><strong>The assistant can use only the tools you add.</strong> If the server has no delete tool, the assistant cannot delete anything through it.</li>
  <li><strong>It covers more than CRM.</strong> Zoho lists tools for CRM, Books, Desk, Mail, Calendar, Projects, Creator and other Zoho apps, plus a growing set of third-party services.</li>
</ul>
<p>Zoho CRM also publishes four ready-made CRM servers, for data insights, data operations, module customization, and workflow and process automation. They are a quick way to try the idea, though a server you build yourself gives you tighter control over the tool list.</p>

<h2 id="what-you-need">What you need</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Side</th><th scope="col">Requirement</th><th scope="col">Notes</th></tr></thead>
  <tbody>
    <tr><th scope="row">Zoho</th><td>A Zoho account with the apps you want to connect, and access to the Zoho MCP console</td><td>Zoho states that MCP is free to use for now and that it will give notice before introducing pricing</td></tr>
    <tr><th scope="row">Claude</th><td>A plan that supports custom connectors: Pro, Max, Team or Enterprise</td><td>On Team and Enterprise plans, only an Owner can add the connector; members then connect individually</td></tr>
    <tr><th scope="row">ChatGPT</th><td>Developer mode with MCP apps</td><td>Write actions are in beta on Business, Enterprise and Edu plans; Pro can connect for read and fetch only</td></tr>
    <tr><th scope="row">Other clients</th><td>Any client that supports MCP connections</td><td>Zoho names Cursor, VS Code and Windsurf alongside Claude and ChatGPT</td></tr>
  </tbody>
</table>
</div>
<p>Plan requirements change often. Confirm them on the <a href="https://www.zoho.com/mcp/" target="_blank" rel="noopener">Zoho MCP</a> site and in your AI provider&rsquo;s help centre before you promise this to your team.</p>

<h2 id="setup">How to set it up</h2>
<ol>
  <li><strong>Create a server.</strong> In the Zoho MCP console, choose <em>Create MCP Server</em> and give it a name that says what it is for, such as <code>sales_readonly</code>. You can also start from a pre-configured server.</li>
  <li><strong>Add tools.</strong> Open <em>Tools</em>, choose <em>Add Tools</em>, pick the app and tick only the actions you need. For a first server, search and get tools are enough.</li>
  <li><strong>Check authorization.</strong> Under <em>Connections</em>, confirm how users will authorize. The next section explains the two options.</li>
  <li><strong>Copy the MCP URL.</strong> The <em>Connect</em> section shows the server&rsquo;s URL. Treat it like a password.</li>
  <li><strong>Add it to your assistant.</strong> In Claude, add a custom connector under <em>Customize &gt; Connectors</em>, paste the URL and click <em>Connect</em>. In ChatGPT, create an app under <em>Settings &gt; Apps</em>, paste the URL and choose OAuth.</li>
  <li><strong>Test with a read-only question.</strong> For example: <em>&ldquo;List open deals over 500,000 with no activity in the last 14 days.&rdquo;</em> Check the answer against a CRM report before you trust it.</li>
</ol>
<p>Menu names change as the product develops. Zoho&rsquo;s <a href="https://help.zoho.com/portal/en/kb/mcp/implementation-guide/articles/zoho-mcp-implementation-guide" target="_blank" rel="noopener">implementation guide</a> has the current screens for each client.</p>

<h2 id="authorization">The two authorization modes</h2>
<p>This is the most important setting on the server, because it decides whose access the assistant uses.</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col"></th><th scope="col">Authorize on Demand</th><th scope="col">Authorize via Connections</th></tr></thead>
  <tbody>
    <tr><th scope="row">Who signs in</th><td>Each user, with their own Zoho account</td><td>The Super Admin, once</td></tr>
    <tr><th scope="row">Whose access is used</th><td>The individual user&rsquo;s</td><td>The Super Admin&rsquo;s tokens, shared with trusted members</td></tr>
    <tr><th scope="row">Default for</th><td>Zoho apps</td><td>Third-party services</td></tr>
    <tr><th scope="row">Best for</th><td>Teams, where people should see only what they normally can</td><td>A single shared integration, or third-party tools that need it</td></tr>
  </tbody>
</table>
</div>
<p>For Zoho apps, keep <strong>Authorize on Demand</strong> unless you have a specific reason not to. A sales rep who connects the assistant should not gain a Super Admin&rsquo;s reach through it. If you do need a shared connection, pair it with a server that has very few tools.</p>

<h2 id="what-to-allow">What to let the assistant do</h2>
<p>We sort actions by how hard they are to undo, the same way we do for any automation.</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Action type</th><th scope="col">Examples</th><th scope="col">Our recommendation</th></tr></thead>
  <tbody>
    <tr><th scope="row">Read</th><td>Search records, get a record, get related records</td><td>Allow from day one</td></tr>
    <tr><th scope="row">Create, low risk</th><td>Tasks, notes, call logs, draft emails</td><td>Allow after a week of read-only use, with the assistant asking before each action</td></tr>
    <tr><th scope="row">Update</th><td>Deal stage, owner, amount, contact details</td><td>Allow selectively, always with a confirmation step</td></tr>
    <tr><th scope="row">Money and commitments</th><td>Invoices, quotes, payments, emails sent to customers</td><td>Let the assistant draft; a person approves and sends</td></tr>
    <tr><th scope="row">Delete and configuration</th><td>Deleting records, changing fields, layouts or workflows</td><td>Leave out of the server</td></tr>
  </tbody>
</table>
</div>
<p>Two habits make this easier to manage. Build <strong>separate servers for separate jobs</strong>, for example one read-only server for reporting and another for sales follow-up. And keep each server small. Zoho recommends around 100 tools per server for best results, because an assistant choosing among too many tools is more likely to pick the wrong one.</p>

<h2 id="risks">The risks to plan for</h2>
<ul>
  <li><strong>Hidden instructions in your data.</strong> An assistant reads whatever is in a record, including text a stranger typed into a web form or an email. That text can contain instructions aimed at the assistant. This is called prompt injection, and it is the main reason to keep write and send actions behind a human confirmation.</li>
  <li><strong>The wrong record.</strong> &ldquo;Update the Atlas deal&rdquo; is ambiguous when there are three. Ask the assistant to show the record it found before it changes anything.</li>
  <li><strong>A leaked URL.</strong> The MCP URL gives access to everything on that server. Do not paste it into chats or documents. If it leaks, regenerate the key in the <em>Connect</em> section.</li>
  <li><strong>&ldquo;Always allow&rdquo;.</strong> Assistants ask before using a tool and offer to stop asking. Use that option only for read tools.</li>
  <li><strong>Data leaving Zoho.</strong> Whatever the assistant reads is sent to the AI provider to produce the answer. Check your provider&rsquo;s data-use terms and your own privacy obligations before you connect customer or financial data.</li>
</ul>
<p>Zoho MCP keeps a log of every tool call, which you can filter by tool and by success or failure. Logs are kept for 30 days, so review them weekly while the setup is new.</p>

<h2 id="mcp-vs-automation">MCP, workflows or Deluge: which to use</h2>
<p>MCP does not replace the automation you already have. It suits a different kind of work.</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Use</th><th scope="col">When</th><th scope="col">Example</th></tr></thead>
  <tbody>
    <tr><th scope="row">Workflow rules and Blueprint</th><td>The same thing must happen every time</td><td>Require approval for discounts above a set level</td></tr>
    <tr><th scope="row">Deluge functions</th><td>The logic is fixed but too complex for a rule</td><td>Create a Zoho Books invoice when a deal is won</td></tr>
    <tr><th scope="row">An assistant through MCP</th><td>The request is different each time and a person is present</td><td>&ldquo;Which customers have open tickets and an overdue invoice?&rdquo;</td></tr>
  </tbody>
</table>
</div>
<p>If a task runs on a schedule or must never be skipped, build it as a rule or a function. Our <a href="/insights/deluge-script-examples/">Deluge script examples</a> show the pattern. If it is a question someone asks on a Monday morning, MCP is a good fit. For a wider view of where AI helps in a CRM, see our guide to <a href="/insights/zoho-agentic-ai-hyperautomation/">AI agents in Zoho CRM</a>.</p>

<h2 id="rollout">A four-week rollout plan</h2>
<ol>
  <li><strong>Week 1: read-only, two or three people.</strong> One server with search and get tools. Collect the questions people actually ask.</li>
  <li><strong>Week 2: check accuracy.</strong> Compare the assistant&rsquo;s answers with CRM reports. Wrong answers usually point to data problems such as duplicates or empty fields, which are worth fixing anyway.</li>
  <li><strong>Week 3: add low-risk create tools.</strong> Tasks, notes and drafts, with a confirmation each time.</li>
  <li><strong>Week 4: review logs and decide.</strong> Keep what was used, remove what was not, and write a one-page rule on what the assistant may and may not do.</li>
</ol>
<p>Clean data makes the biggest difference to the result. If your records are inconsistent, start with the data, as described in our <a href="/insights/zoho-analytics-agentic-data-foundations-2026/">data foundations guide</a>.</p>

<h2 id="cost">Cost and limits</h2>
<p>At the time of writing, Zoho says MCP is free to use and that calls made through it count against each app&rsquo;s normal API limits. There is no stated limit on the number of servers. The real costs are the AI subscription for each user and the time spent on setup, permissions and review.</p>
<p>If you want help deciding which tools to expose, or need the underlying <a href="/business-process-automation/">automation</a> and <a href="/zoho-integrations/">integrations</a> tidied up first, that is the kind of work we do.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Is Zoho MCP free?',
         'At the time of writing, Zoho states that Zoho MCP is free to use and that it will notify users in advance if pricing is introduced. Calls made through MCP follow each Zoho app\'s normal API limits. You still pay for your Zoho apps and for the AI assistant you connect.'),
        ('Which AI assistants work with Zoho MCP?',
         'Any client that supports MCP connections. Zoho names Claude, ChatGPT, Cursor, VS Code and Windsurf. Each has its own plan requirements for custom connectors, so check your provider\'s help centre.'),
        ('Can the assistant see records I cannot see?',
         'With Authorize on Demand, each user signs in with their own Zoho account, so the assistant works within that user\'s access. With Authorize via Connections, the Super Admin\'s authorization is shared, so use it carefully and with a small set of tools.'),
        ('Is it safe to let an AI assistant update Zoho CRM?',
         'It can be, with limits. Add only the tools you need, keep delete and configuration tools out of the server, require confirmation before any change, and review the MCP logs regularly. Start with read-only access.'),
        ('Do I need a developer to set up Zoho MCP?',
         'No. Creating a server and connecting an assistant is done through menus. Where help is useful is in deciding which tools to expose, cleaning the data the assistant will read, and building rule-based automation for tasks that must happen the same way every time.'),
        ('What is the difference between Zoho MCP and Zia?',
         'Zia is Zoho\'s own AI, built into Zoho apps. Zoho MCP is a connection layer that lets an outside assistant, such as Claude or ChatGPT, use tools in your Zoho apps. Many teams will use both.'),
    ],
))
