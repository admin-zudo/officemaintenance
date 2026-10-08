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
    related=['zoho-analytics-agentic-data-foundations-2026', 'deluge-script-examples', 'zoho-crm-implementation-cost'],
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
<p>In 2025 Zoho announced a bigger step: its own large language model (Zia LLM), prebuilt <strong>Zia Agents</strong> and an <strong>Agent Studio</strong> for building custom agents across Zoho apps. Zoho has also supported connecting third-party models such as OpenAI to Zia. Availability of these features varies by product, edition and region, and it is changing quickly, so check what is enabled in your own account before planning around a specific capability.</p>
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
