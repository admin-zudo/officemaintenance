# Article content, part A. Bodies are plain HTML; <h2 id> drive the table of contents.

ARTICLES = []

# ------------------------------------------------------------------ Creator vs Power Apps
ARTICLES.append(dict(
    slug='zoho-creator-vs-power-apps',
    title='Zoho Creator vs Microsoft Power Apps: An Honest Comparison for Growing Businesses',
    seo_title='Zoho Creator vs Power Apps (2026): Which Low-Code Platform Fits You?',
    description='A practical comparison of Zoho Creator and Microsoft Power Apps: data, logic, portals, mobile, integrations, licensing and the situations where each one is the better choice.',
    lead='Both platforms let you build business apps without a full development team. They are built on different ideas, though, and the wrong choice usually shows up six months later as licensing surprises or workarounds. Here is how they actually differ.',
    category='Comparisons', keyword='zoho creator vs power apps',
    published='2026-10-08', modified='2026-10-08',
    cover_alt='Two low-code app builder windows side by side, one showing a Zoho Creator form and one a Power Apps canvas',
    caption='Same goal, different foundations: Creator bundles database, logic and portals; Power Apps leans on the wider Microsoft stack.',
    related=['zoho-crm-implementation-cost', 'deluge-script-examples', 'zoho-partner-software-development'],
    body='''
<p>Every few weeks a client asks us some version of the same question: <em>&ldquo;We need an internal app. Should we build it on Zoho Creator or Power Apps?&rdquo;</em> The honest answer is that it depends less on the features list and more on where your data and your people already live.</p>
<p>We build on Zoho Creator every day, so read this with that in mind. We have tried to be fair to Power Apps, because for some businesses it is genuinely the better fit, and recommending the wrong platform costs everyone time.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Choose Zoho Creator</strong> if you already use Zoho apps (CRM, Books, Desk, Zoho One), want the database, logic, reports, portals and mobile apps in one product, and want predictable per-user pricing.</li>
  <li><strong>Choose Power Apps</strong> if your company runs on Microsoft 365, your data already sits in SharePoint, Dataverse or SQL Server, your staff live in Teams, and your IT team manages identity and governance through Microsoft Entra ID.</li>
  <li><strong>Be careful</strong> if neither is true. Then the decision comes down to who will maintain the app, which external systems it must talk to, and how many people outside your company need access.</li>
</ul>

<h2 id="how-they-differ">How the two platforms are built</h2>
<p><strong>Zoho Creator</strong> is a self-contained application platform. When you create an app you get a database (forms become tables), a scripting language called Deluge, reports and dashboards, page builders, role-based permissions, customer or partner portals, and native mobile apps, all in one place. You don&rsquo;t need to buy or configure anything else to have a working app.</p>
<p><strong>Power Apps</strong> is one part of the Microsoft Power Platform. The app itself is the user interface. Data usually lives somewhere else (SharePoint lists, Dataverse, SQL Server, Excel or one of hundreds of connectors), workflows usually run in Power Automate, and external portals are a separate product, Power Pages. The logic inside the app is written in Power Fx, an Excel-like formula language.</p>
<p>Neither approach is better in the abstract. Creator gives you fewer moving parts. Power Apps gives you more building blocks, which is powerful when your organization already owns and manages them.</p>

<h2 id="comparison-table">Side-by-side comparison</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">Zoho Creator</th><th scope="col">Power Apps</th></tr></thead>
  <tbody>
    <tr><th scope="row">Data storage</th><td>Built-in database; every form is a table with relationships</td><td>SharePoint, Dataverse, SQL Server or a connector; Dataverse needs premium licensing</td></tr>
    <tr><th scope="row">Logic</th><td>Deluge scripts on form events, schedules, buttons and APIs</td><td>Power Fx formulas in the app; most background workflows in Power Automate</td></tr>
    <tr><th scope="row">App types</th><td>Form- and report-driven apps, custom pages, dashboards</td><td>Canvas apps (pixel-level layout) and model-driven apps (data-first, built on Dataverse)</td></tr>
    <tr><th scope="row">Mobile</th><td>Native iOS and Android apps generated from the same app</td><td>Power Apps mobile player for iOS and Android</td></tr>
    <tr><th scope="row">External users</th><td>Customer or partner portals included in Creator plans</td><td>Power Pages, licensed separately</td></tr>
    <tr><th scope="row">Integrations</th><td>Native links to Zoho apps; REST APIs, webhooks and connections for others</td><td>Large connector catalogue; many business connectors are &ldquo;premium&rdquo;</td></tr>
    <tr><th scope="row">Best ecosystem fit</th><td>Zoho One, Zoho CRM, Zoho Books, Zoho Desk</td><td>Microsoft 365, Teams, SharePoint, Dynamics 365, Azure</td></tr>
  </tbody>
</table>
</div>
<p>Pricing for both platforms changes regularly and depends on edition, region and contract size, so check the official pricing pages for <a href="https://www.zoho.com/creator/pricing.html" target="_blank" rel="noopener">Zoho Creator</a> and <a href="https://www.microsoft.com/en-us/power-platform/products/power-apps/pricing" target="_blank" rel="noopener">Power Apps</a> before you decide. What matters more than the headline price is the next section.</p>

<h2 id="licensing">Licensing: where the surprises hide</h2>
<p>Most of the painful conversations we have about low-code platforms are about licences, not features.</p>
<h3>Power Apps</h3>
<p>Some Microsoft 365 plans let staff use Power Apps with standard connectors such as SharePoint. That is great for simple apps. The moment an app needs Dataverse, a premium connector (SQL Server, many CRMs and ERPs, custom APIs) or external users, every person who uses it typically needs a premium licence, and portals for customers are billed separately. Teams often build a prototype on the free tier and only discover the licence cost when they try to roll it out.</p>
<h3>Zoho Creator</h3>
<p>Creator is licensed per user, and the plans include the database, Deluge, reports and mobile apps. Portal users for customers or partners come with plan-based limits. If you have Zoho One, Creator is already included. The main thing to watch is plan limits: records, storage, scheduled tasks and API calls differ by edition, so size the plan against your expected volume.</p>
<p><strong>Our advice:</strong> before anyone builds a prototype, write down who will use the app (internal staff, field teams, customers), where the data will live, and which other systems it needs to talk to. Price both platforms against that list, not against the demo.</p>

<h2 id="building">What building and maintaining an app feels like</h2>
<p>In Creator, a typical app starts with forms. You define fields and relationships, add Deluge on events such as <em>On Validate</em> and <em>On Success</em>, then build reports, pages and permissions on top. Because the data and logic live together, a developer can trace exactly what happens when a record is saved. Deluge reads like a simplified scripting language, and it has built-in tasks for Zoho apps, for example creating a Zoho Books invoice in one line. If you want to see what that looks like, we wrote a guide with <a href="/insights/deluge-script-examples/">real Deluge script examples</a>.</p>
<p>In Power Apps, canvas apps give designers precise control over layout, which is excellent for task-focused screens. The trade-off is that logic is spread across formulas on individual controls, Power Automate flows and the data source. That is manageable with good discipline, but it is easy for a fast-growing app to become hard to follow.</p>
<p>Either way, the long-term cost of an app is maintenance. Ask who will understand it in two years. Document data models and automations from day one, whichever platform you pick.</p>

<h2 id="integrations">Integrations with the rest of your business</h2>
<p>If your CRM, accounting and helpdesk are Zoho products, Creator has a clear advantage: it can read and write records in Zoho CRM, Books, Desk and others with built-in Deluge tasks and shared authentication. A common pattern we build is a Creator app for operations (jobs, orders, inspections) that pushes approved work into Zoho Books for invoicing and updates the customer in Zoho CRM.</p>
<p>If your stack is Microsoft, Power Apps wins the same argument the other way: SharePoint, Outlook, Teams, Excel and Dynamics 365 connect with almost no effort, and identity is handled through your existing Microsoft accounts.</p>
<p>For anything outside those ecosystems (an e-commerce platform, a payment gateway, a logistics API), both platforms can call REST APIs. In Creator you use <code>invokeurl</code> with a stored connection; in Power Platform you use a custom connector or an HTTP action in Power Automate, which usually needs premium licensing.</p>

<h2 id="when-creator">When Zoho Creator is the better choice</h2>
<ul>
  <li>You already pay for Zoho One or use Zoho CRM and Books, and want an app that shares their data.</li>
  <li>You need a customer or supplier portal and don&rsquo;t want a second product for it.</li>
  <li>Field staff need a mobile app with offline-friendly forms and photo or signature capture.</li>
  <li>You want to replace spreadsheets or an old Access database with something structured, quickly.</li>
  <li>You have no dedicated IT team and want one platform to look after.</li>
</ul>

<h2 id="when-power-apps">When Power Apps is the better choice</h2>
<ul>
  <li>Your company is standardized on Microsoft 365 and your staff spend their day in Teams.</li>
  <li>Your data already lives in SharePoint, Dataverse, SQL Server or Dynamics 365.</li>
  <li>Your IT team manages security, data-loss policies and environments centrally in Microsoft tools.</li>
  <li>You need very precise screen layouts for a single task, such as a kiosk or check-in app.</li>
</ul>

<h2 id="decision-checklist">A five-question decision checklist</h2>
<ol>
  <li><strong>Where does the data live today,</strong> and where should it live after the app is built?</li>
  <li><strong>Who are the users?</strong> Count internal staff, mobile staff and external users separately.</li>
  <li><strong>Which systems must it talk to?</strong> List them, and check whether each connection is native, premium or custom.</li>
  <li><strong>Who will maintain it?</strong> An in-house admin, an IT team or an outside developer?</li>
  <li><strong>What does year two cost?</strong> Licences for the expected number of users, plus support and changes.</li>
</ol>
<p>If you write those answers down, the right platform is usually obvious. If it isn&rsquo;t, a short discovery call with someone who has built on both will save you a rebuild later.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Is Zoho Creator cheaper than Power Apps?',
         'Often, but not always. Creator includes its database, scripting, reports, portals and mobile apps in each plan, while Power Apps can need premium licences for Dataverse, premium connectors and separate Power Pages licensing for external users. Compare both against your real user counts and integrations, using each vendor\'s current pricing page.'),
        ('Can Zoho Creator integrate with Microsoft 365?',
         'Yes. Creator can call Microsoft Graph and other REST APIs through Deluge and stored OAuth connections, and Zoho Flow offers ready-made connectors for many Microsoft services. It takes more setup than staying inside one ecosystem, but it is a common and reliable pattern.'),
        ('Which is easier to learn, Deluge or Power Fx?',
         'Power Fx feels familiar to people who write Excel formulas. Deluge reads more like a simple scripting language and is easier to follow for multi-step business logic, such as creating related records or calling APIs. Most admins can read basic Deluge after a short handover.'),
        ('Can we move an app from Power Apps to Zoho Creator later?',
         'There is no automatic converter. The data can be exported and imported, but screens and logic have to be rebuilt. That is why it is worth choosing carefully at the start.'),
    ],
))

# ------------------------------------------------------------------ Migration
ARTICLES.append(dict(
    slug='migrate-hubspot-salesforce-to-zoho-crm',
    title='Migrating from HubSpot or Salesforce to Zoho CRM: A Step-by-Step Plan',
    seo_title='HubSpot or Salesforce to Zoho CRM Migration: Step-by-Step Plan (2026)',
    description='How to move from HubSpot or Salesforce to Zoho CRM without losing data or momentum: object mapping, import order, rebuilding automation, testing, cut-over and training.',
    lead='A CRM migration fails in predictable ways: broken relationships between records, missing activity history, automations nobody remembered to rebuild, and a sales team that quietly goes back to spreadsheets. This is the plan we follow to avoid all four.',
    category='Zoho CRM', keyword='migrate hubspot to zoho crm',
    published='2026-10-08', modified='2026-10-08',
    cover_alt='Two database panels joined by a field-mapping table, illustrating records moving from an old CRM into Zoho CRM',
    caption='Migration is mostly mapping: objects, fields, owners and the relationships between records.',
    related=['zoho-crm-implementation-cost', 'deluge-script-examples', 'zoho-creator-vs-power-apps'],
    body='''
<p>Teams move to Zoho CRM for different reasons: per-user pricing that scales better, the rest of the Zoho suite (Books, Desk, Campaigns, Analytics) working together, or simply wanting more control over customization. Whatever the reason, the migration itself follows the same shape.</p>
<p>This guide covers moves from both HubSpot and Salesforce, because the steps are almost identical. Where the two differ, we say so.</p>

<h2 id="before-you-start">Before you start: decide what not to migrate</h2>
<p>The cheapest record to migrate is the one you leave behind. Before exporting anything, agree on:</p>
<ul>
  <li><strong>Inactive records.</strong> Contacts with no activity in several years, bounced emails and test records. Archive them in a spreadsheet instead of importing them.</li>
  <li><strong>Unused fields.</strong> Most CRMs collect fields over the years that nobody fills in. Export a field-usage report and drop anything that is empty in most records.</li>
  <li><strong>Duplicate records.</strong> Clean duplicates in the old system or in the export files. Zoho CRM can block duplicates on import, but it cannot decide which version of a contact is correct.</li>
</ul>
<p>This step usually removes a large share of the data and makes everything after it faster.</p>

<h2 id="map-objects">Step 1: Map objects and fields</h2>
<p>Each CRM names things differently. A typical mapping looks like this:</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">HubSpot</th><th scope="col">Salesforce</th><th scope="col">Zoho CRM</th></tr></thead>
  <tbody>
    <tr><td>Companies</td><td>Accounts</td><td>Accounts</td></tr>
    <tr><td>Contacts</td><td>Contacts</td><td>Contacts</td></tr>
    <tr><td>Contacts (lifecycle stage &ldquo;lead&rdquo;)</td><td>Leads</td><td>Leads</td></tr>
    <tr><td>Deals</td><td>Opportunities</td><td>Deals</td></tr>
    <tr><td>Products and line items</td><td>Products and opportunity products</td><td>Products, and Quotes or deal subforms</td></tr>
    <tr><td>Tickets</td><td>Cases</td><td>Cases module, or Zoho Desk</td></tr>
    <tr><td>Notes, calls, meetings, tasks</td><td>Notes, Events, Tasks</td><td>Notes, Calls, Meetings, Tasks</td></tr>
    <tr><td>Custom objects</td><td>Custom objects</td><td>Custom modules</td></tr>
  </tbody>
</table>
</div>
<p>Two decisions matter most here:</p>
<ol>
  <li><strong>Leads versus contacts.</strong> HubSpot keeps everyone as a contact with a lifecycle stage. Zoho CRM, like Salesforce, separates unqualified leads from contacts. Decide which lifecycle stages become Leads and which become Contacts, or the sales team will be confused on day one.</li>
  <li><strong>Picklist values.</strong> Deal stages, lead sources and industries must match exactly, character for character, before import. Build them in Zoho CRM first, then map the old values to them.</li>
</ol>
<p>Put the mapping in a shared spreadsheet: old object, old field, new module, new field, transformation (if any). It becomes the specification for the whole project.</p>

<h2 id="prepare-zoho">Step 2: Prepare Zoho CRM before importing</h2>
<ul>
  <li><strong>Users and roles.</strong> Create every user who owns records, including people who have left (you can deactivate them after import). Ownership is matched by email address.</li>
  <li><strong>Custom fields and modules.</strong> Create them from the mapping sheet.</li>
  <li><strong>A legacy ID field</strong> on every module, for example <em>HubSpot ID</em> or <em>Salesforce ID</em>. This is how related records find each other during import, and it saves hours of debugging later.</li>
  <li><strong>Turn off workflows and assignment rules</strong> during the import, or every imported deal will send an email to its owner.</li>
</ul>

<h2 id="export">Step 3: Export from HubSpot or Salesforce</h2>
<p><strong>HubSpot:</strong> export each object as CSV from its index view, including all properties, and use the associations export to keep links between companies, contacts and deals. Attachments and email bodies need separate handling.</p>
<p><strong>Salesforce:</strong> the Data Export service produces a full set of CSV files, including record IDs and lookup IDs, which makes relationship mapping straightforward. Attachments and files are included as separate files you can map by parent ID.</p>
<p>Zoho CRM also includes a built-in migration option for moving data from other CRMs, including Salesforce and HubSpot exports. It handles standard objects well. For custom objects, complex relationships or data that needs cleaning, a controlled import using the steps below gives you more control.</p>

<h2 id="import-order">Step 4: Import in the right order</h2>
<p>Records that are referenced by others must exist first. The order we use:</p>
<ol>
  <li>Users (already created in step 2)</li>
  <li>Accounts</li>
  <li>Contacts, linked to accounts through the legacy account ID</li>
  <li>Leads</li>
  <li>Products and price books</li>
  <li>Deals, linked to accounts and contacts</li>
  <li>Notes, calls, meetings and tasks, linked to their parent records</li>
  <li>Attachments and files</li>
</ol>
<p>Run the whole sequence first in a sandbox or a trial org with a sample (for example 500 records per module). Fix mapping problems there, not in production.</p>

<h2 id="automation">Step 5: Rebuild automation, don&rsquo;t copy it</h2>
<p>Workflows, sequences, assignment rules, approval processes and email templates do not migrate between CRMs. This is the step most teams underestimate, and also the biggest opportunity: you get to rebuild only what still matters.</p>
<p>List every active automation in the old system with its trigger and outcome. Then rebuild it in Zoho CRM using the simplest tool that works:</p>
<ul>
  <li><strong>Workflow rules</strong> for field updates, emails, tasks and webhooks.</li>
  <li><strong>Blueprint</strong> for stage-by-stage processes with required fields at each step.</li>
  <li><strong>Assignment rules</strong> for lead routing.</li>
  <li><strong>Deluge functions</strong> for anything that needs logic, such as creating related records, deduplicating or calling another system. Our <a href="/insights/deluge-script-examples/">Deluge examples</a> include several common ones.</li>
</ul>

<h2 id="cutover">Step 6: Test, cut over and validate</h2>
<p>A clean cut-over usually happens over a weekend or a quiet day:</p>
<ol>
  <li>Freeze changes in the old CRM.</li>
  <li>Run the final export and import in production.</li>
  <li>Compare record counts per module against the export, and spot-check 20 to 30 records end to end: account, contacts, deals, notes and attachments.</li>
  <li>Re-enable workflows and assignment rules.</li>
  <li>Keep the old CRM read-only for a few weeks in case someone needs to check history.</li>
</ol>

<h2 id="adoption">Step 7: Train people on their real work</h2>
<p>Generic CRM training does not stick. Train each team on the five or six things they do every day, using their own migrated data: finding an account, logging a call, moving a deal, creating a quote. Then schedule a check-in two weeks later to fix the small annoyances that would otherwise push people back to spreadsheets.</p>
<p>We include one month of free support and onboarding after every build for exactly this reason. The first month is when small fixes make the biggest difference.</p>

<h2 id="timeline">How long does it take?</h2>
<p>For a small team with standard objects and clean data, a migration can be done in two to four weeks including setup and training. Larger datasets, custom objects, multiple pipelines or integrations usually take six to ten weeks. Our <a href="/insights/zoho-crm-implementation-cost/">Zoho CRM cost guide</a> breaks down the effort, and our <a href="/pricing/#calculator">pricing calculator</a> gives an indicative estimate for your own project.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Will we lose email history when moving to Zoho CRM?',
         'Logged emails can be migrated as notes or activity records linked to the right contact or deal. Live email sync is set up fresh in Zoho CRM by connecting each user\'s mailbox, which brings recent email back into the CRM from that point.'),
        ('Do HubSpot workflows or Salesforce flows migrate automatically?',
         'No. Automations, sequences, approval processes and templates must be rebuilt in Zoho CRM using workflow rules, Blueprint, assignment rules or Deluge functions. It is a good moment to drop automations that no longer matter.'),
        ('Can we keep using the old CRM during the migration?',
         'Yes, until cut-over. Most of the work happens in a sandbox or trial org while the team keeps working in the old system. Changes are frozen only for the final export and import, usually over a weekend.'),
        ('How do we keep relationships between accounts, contacts and deals?',
         'Add a legacy ID field to every module in Zoho CRM and import the old record IDs into it. Related records then reference those IDs during import, so contacts land on the right accounts and deals keep their contacts.'),
    ],
))

# ------------------------------------------------------------------ Cost
ARTICLES.append(dict(
    slug='zoho-crm-implementation-cost',
    title='How Much Does a Zoho CRM Implementation Cost? A Transparent Breakdown',
    seo_title='Zoho CRM Implementation Cost in 2026: Real Breakdown and Examples',
    description='What a Zoho CRM implementation really costs: licences, setup effort, data migration, integrations, training and support, with three example project sizes priced at an hourly rate.',
    lead='&ldquo;How much will this cost?&rdquo; is the first question every buyer asks and the one most providers avoid answering. Here is how the cost of a Zoho CRM implementation is actually made up, with worked examples using our own hourly rate.',
    category='Zoho CRM', keyword='zoho crm implementation cost',
    published='2026-10-08', modified='2026-10-08',
    cover_alt='A project estimate sheet with line items for setup, migration, integrations and training next to a calculator',
    caption='An implementation estimate is the sum of a few predictable pieces of work.',
    related=['migrate-hubspot-salesforce-to-zoho-crm', 'zoho-creator-vs-power-apps', 'zoho-partner-software-development'],
    body='''
<p>The total cost of a Zoho CRM rollout has two parts that are easy to mix up: what you pay <strong>Zoho</strong> for the software, and what you pay <strong>someone</strong> to set it up around your business. This guide covers both, then walks through three realistic project sizes.</p>
<p>We use our own rate of US$15 per hour for the examples, so the numbers are real for us. Other providers charge different rates, but the hours involved are a useful benchmark wherever you buy.</p>

<h2 id="two-costs">The two costs: licences and implementation</h2>
<h3>1. Zoho CRM licences</h3>
<p>Zoho bills licences per user, per month, and the price depends on the edition (Standard, Professional, Enterprise, Ultimate) and on annual or monthly billing. Zoho CRM is also included in Zoho One, which bundles most Zoho apps for every employee. Prices vary by region and change over time, so always check the <a href="https://www.zoho.com/crm/zohocrm-pricing.html" target="_blank" rel="noopener">official Zoho CRM pricing page</a>.</p>
<p>Edition matters for more than price. Features such as Blueprint, custom functions, sandbox, territory management and API limits differ between editions. Part of a good implementation is choosing the lowest edition that actually covers what you need.</p>
<h3>2. Implementation services</h3>
<p>This is the work of designing and configuring the CRM: modules, fields, layouts, pipelines, automation, data migration, integrations, testing and training. It is almost always priced from an estimate of hours or days, even when you are quoted a fixed price.</p>

<h2 id="what-drives-cost">What drives the implementation cost</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Cost driver</th><th scope="col">Low effort</th><th scope="col">High effort</th></tr></thead>
  <tbody>
    <tr><th scope="row">Sales process</th><td>One pipeline, a handful of stages</td><td>Several pipelines, approvals, Blueprint with required fields at each stage</td></tr>
    <tr><th scope="row">Customization</th><td>Standard modules, a few custom fields</td><td>Custom modules, subforms, page layouts per team, validation rules</td></tr>
    <tr><th scope="row">Data migration</th><td>A few clean spreadsheets</td><td>Another CRM with years of history, attachments and custom objects</td></tr>
    <tr><th scope="row">Integrations</th><td>Email, calendar and other Zoho apps</td><td>Accounting, e-commerce, telephony or in-house systems via API</td></tr>
    <tr><th scope="row">Automation</th><td>Workflow rules and email alerts</td><td>Deluge functions, scheduled jobs, webhooks</td></tr>
    <tr><th scope="row">Reporting</th><td>Standard reports</td><td>Custom dashboards per role, or Zoho Analytics</td></tr>
    <tr><th scope="row">Users and teams</th><td>One team, one country</td><td>Several teams, roles, territories and currencies</td></tr>
  </tbody>
</table>
</div>

<h2 id="examples">Three example projects, priced</h2>
<p>These are typical scopes we see. Your project will differ, which is why we confirm everything in a written proposal after a discovery call.</p>

<h3>Example 1: Starter setup for a small sales team</h3>
<ul>
  <li>Standard modules, one pipeline, 20 to 30 custom fields</li>
  <li>Lead assignment and basic workflow emails</li>
  <li>Import of contacts and open deals from spreadsheets</li>
  <li>Email integration, a few reports and a short training session</li>
</ul>
<p><strong>Typical effort:</strong> 40 to 70 hours, around <strong>US$600 to US$1,050</strong> at US$15 per hour. Usually two to three weeks.</p>

<h3>Example 2: Standard implementation for a growing business</h3>
<ul>
  <li>Two pipelines with Blueprint for the main sales process</li>
  <li>One or two custom modules, page layouts per role</li>
  <li>Migration from another CRM including notes and activities</li>
  <li>Integration with Zoho Books or an accounting system, quotes and products</li>
  <li>Role-based dashboards, documentation and team training</li>
</ul>
<p><strong>Typical effort:</strong> 100 to 180 hours, around <strong>US$1,500 to US$2,700</strong>. Usually four to eight weeks.</p>

<h3>Example 3: Advanced rollout across several teams</h3>
<ul>
  <li>Multiple teams or territories with different processes and permissions</li>
  <li>Deluge functions for deduplication, record creation and scheduled checks</li>
  <li>Three or more integrations (e-commerce, telephony, an in-house system)</li>
  <li>Large migration with attachments and custom objects</li>
  <li>Custom dashboards or Zoho Analytics, plus admin training</li>
</ul>
<p><strong>Typical effort:</strong> 200 to 400 hours, around <strong>US$3,000 to US$6,000</strong>. Usually eight to sixteen weeks.</p>
<p>Want a figure for your own scope? Our <a href="/pricing/#calculator">pricing calculator</a> uses the same approach and updates as you choose options.</p>

<h2 id="hidden-costs">Costs people forget</h2>
<ul>
  <li><strong>Data cleanup.</strong> Messy source data is the most common reason migrations overrun. Budget time for deduplication and standardizing values.</li>
  <li><strong>Change requests.</strong> Once people start using the CRM they will ask for changes. That is healthy; plan a small budget for the first two months.</li>
  <li><strong>Extensions and add-ons.</strong> Some marketplace extensions, telephony services or e-signature tools have their own subscriptions.</li>
  <li><strong>Edition upgrades.</strong> If a must-have feature is only in a higher edition, every user licence goes up. Check this before you build around it.</li>
  <li><strong>Internal time.</strong> Someone on your side needs to answer questions, test and champion the CRM. Plan for a few hours a week from them.</li>
</ul>

<h2 id="hourly-vs-fixed">Hourly or fixed price: which is better?</h2>
<p><strong>Hourly</strong> works well for small changes, fixes and ongoing improvements, where the scope is hard to pin down. You pay for time actually spent, ideally with an agreed cap.</p>
<p><strong>Fixed price</strong> works well for a defined implementation. The provider takes on the risk of estimating correctly, and you know the total before work starts. The trade-off is that the scope has to be written down clearly, and changes outside it are quoted separately.</p>
<p>We offer both: US$15 per hour for open-ended work, and fixed prices for defined projects, based on the estimated days and complexity. See our <a href="/pricing/">pricing page</a> for details.</p>

<h2 id="reduce-cost">Five ways to reduce the cost</h2>
<ol>
  <li>Clean and deduplicate your data before the project starts.</li>
  <li>Start with one team and one pipeline, then expand.</li>
  <li>Use standard modules and fields wherever they fit, and customize only where it changes how people work.</li>
  <li>Choose an internal owner who can make decisions quickly.</li>
  <li>Make sure training and documentation are included, so you don&rsquo;t pay for the same answers twice.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('How much does Zoho CRM implementation cost?',
         'Implementation effort typically ranges from about 40 hours for a small starter setup to 200 to 400 hours for an advanced multi-team rollout. At our rate of US$15 per hour that is roughly US$600 to US$6,000, plus Zoho licence fees, which you pay to Zoho directly.'),
        ('Are Zoho CRM licences included in the implementation price?',
         'No. Licences are billed by Zoho per user per month, depending on the edition. Keeping the subscription in your own name means you own the account and the data.'),
        ('How long does a Zoho CRM implementation take?',
         'A starter setup usually takes two to three weeks, a standard implementation four to eight weeks, and an advanced rollout with several integrations eight to sixteen weeks. The timeline depends mostly on data migration and integrations.'),
        ('What is included after go-live?',
         'With Zudo Works, every build includes one month of free support and onboarding after launch. After that, support continues hourly or on an optional monthly arrangement.'),
    ],
))
