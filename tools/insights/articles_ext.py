# Extra sections, inserted before each article's FAQ heading.

EXT = {}

EXT['zoho-creator-vs-power-apps'] = '''
<h2 id="scenario">A worked scenario: a field service company</h2>
<p>Take a 40-person company that installs and services equipment. Office staff schedule jobs, technicians visit sites, and finance invoices completed work. Today it runs on a shared spreadsheet, phone calls and photos sent over messaging apps.</p>
<p><strong>If the company uses Zoho CRM and Zoho Books,</strong> a Creator app is the natural fit. Jobs are created from CRM accounts, technicians use the Creator mobile app to record work, parts and signatures on site, and a Deluge function sends completed jobs to Zoho Books as invoices. Customers can see their job history through a Creator portal. Everything shares one set of customer records and one login system.</p>
<p><strong>If the company runs on Microsoft 365,</strong> with customers in Dynamics 365 or a SharePoint list and staff working in Teams, Power Apps makes sense. A canvas app handles the technician screens, Power Automate creates follow-up tasks and sends documents, and the data sits in Dataverse or SharePoint. The customer portal would be a Power Pages site, licensed separately.</p>
<p>Both solutions work. The difference is how many products you need to license and maintain, and which team already knows them.</p>
'''

EXT['migrate-hubspot-salesforce-to-zoho-crm'] = '''
<h2 id="common-problems">Common problems and how to avoid them</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Problem</th><th scope="col">Why it happens</th><th scope="col">How to avoid it</th></tr></thead>
  <tbody>
    <tr><th scope="row">Contacts not linked to accounts</th><td>Lookups were matched by name, and names differed slightly</td><td>Match on a legacy ID field, never on names</td></tr>
    <tr><th scope="row">Wrong record owners</th><td>Users did not exist in Zoho CRM at import time</td><td>Create every owner first, including former staff, then deactivate them</td></tr>
    <tr><th scope="row">Picklist values rejected or blank</th><td>Values in the file didn&rsquo;t exactly match the Zoho CRM picklist</td><td>Build picklists first and map old values in the spreadsheet</td></tr>
    <tr><th scope="row">Floods of automated emails</th><td>Workflows were active during the import</td><td>Switch off workflows and assignment rules until validation is complete</td></tr>
    <tr><th scope="row">Dates shifted by a day</th><td>Time zones and date formats differed between systems</td><td>Export in ISO format and check a sample of date-time fields after the test import</td></tr>
    <tr><th scope="row">Team keeps using the old CRM</th><td>The old system was left editable and training was generic</td><td>Make the old CRM read-only and train on real daily tasks</td></tr>
  </tbody>
</table>
</div>

<h2 id="checklist">Migration checklist</h2>
<ul class="checklist">
  <li>Agree what not to migrate (inactive records, unused fields, duplicates)</li>
  <li>Write the object and field mapping sheet</li>
  <li>Choose the Zoho CRM edition based on the features you need</li>
  <li>Create users, roles, profiles, custom fields, modules and picklists</li>
  <li>Add legacy ID fields to every module</li>
  <li>Switch off workflows and assignment rules for the import</li>
  <li>Run a sample import in a sandbox or trial org and fix mapping issues</li>
  <li>Rebuild automation, templates and reports</li>
  <li>Freeze the old CRM, run the final import and validate counts</li>
  <li>Switch automation back on and train each team on their daily tasks</li>
  <li>Keep the old CRM read-only for a few weeks, then cancel it</li>
</ul>
'''

EXT['zoho-crm-implementation-cost'] = '''
<h2 id="week-by-week">What a standard project looks like week by week</h2>
<p>To make the hours concrete, here is how the effort in Example 2 typically spreads out:</p>
<ol>
  <li><strong>Week 1: Discovery and design.</strong> Workshops with sales and management, mapping the current process, agreeing modules, fields, stages and reports. Output: a written design and data mapping sheet.</li>
  <li><strong>Weeks 2 to 3: Configuration.</strong> Modules, layouts, pipelines, Blueprint, roles and permissions, email templates. Weekly demos so the team can react early.</li>
  <li><strong>Weeks 3 to 4: Data migration.</strong> Cleaning, test imports, fixing mapping issues, then the full import with record-count checks.</li>
  <li><strong>Weeks 4 to 5: Integrations and automation.</strong> Accounting integration, workflow rules and any Deluge functions, all tested on real scenarios.</li>
  <li><strong>Week 6: Training and go-live.</strong> Role-based training on the team&rsquo;s own data, documentation handover and go-live.</li>
  <li><strong>The month after:</strong> fixes and adjustments as people use it every day. With us, this first month of support and onboarding is free.</li>
</ol>

<h2 id="proposal">What a good proposal should include</h2>
<p>Whoever you hire, a proposal you can rely on has these elements:</p>
<ul>
  <li>A plain-language summary of the problem you are solving</li>
  <li>The modules, automations, integrations and reports in scope, and what is out of scope</li>
  <li>How data migration will be handled and checked</li>
  <li>The estimated hours or days, and the price</li>
  <li>The timeline with milestones and review points</li>
  <li>Training, documentation and support after launch</li>
  <li>Who owns the account, configuration and code (it should be you)</li>
</ul>
<p>If two proposals have very different prices, compare these sections first. The cheaper one often leaves out migration checks, training or documentation.</p>

<h2 id="ongoing">Ongoing costs after launch</h2>
<p>A CRM is never finished. Budget for:</p>
<ul>
  <li><strong>Licences:</strong> per user per month, growing with your team.</li>
  <li><strong>Small changes:</strong> new fields, reports and automation as your process evolves. For many businesses this is a few hours a month.</li>
  <li><strong>Periodic reviews:</strong> once or twice a year, a review of unused fields, broken automations and data quality keeps the system fast and trusted.</li>
</ul>
'''

EXT['deluge-script-examples'] = '''
<h2 id="testing">How we test and deploy Deluge safely</h2>
<ol>
  <li><strong>Write against test records first.</strong> Create a few records that cover the normal case and the edge cases: empty lookups, zero amounts, missing emails.</li>
  <li><strong>Use the function editor&rsquo;s test run</strong> with a test record ID, and print key values with <code>info</code>.</li>
  <li><strong>Attach the function to its trigger</strong> (workflow, button, schedule) only after it behaves correctly in isolation.</li>
  <li><strong>Check limits.</strong> If a scheduled function processes many records, test it with a realistic volume.</li>
  <li><strong>Document it:</strong> name, trigger, purpose, fields touched and owner, in your automation list.</li>
  <li><strong>Watch the first week</strong> of live runs, especially anything that sends email or creates records in another app.</li>
</ol>
'''

EXT['zoho-agentic-ai-hyperautomation'] = '''
<h2 id="worked-example">A worked example: AI-assisted enquiry handling</h2>
<p>Here is a realistic first project for a business that receives web enquiries through a form that creates leads in Zoho CRM.</p>
<ol>
  <li><strong>Rules first.</strong> A workflow rule assigns the lead by region and product, and checks for an existing account with the same email domain. This part stays rule-based because it must be predictable.</li>
  <li><strong>AI summary.</strong> An assistant summarizes the enquiry in two lines and suggests a category (new project, support question, pricing request), written into fields on the lead.</li>
  <li><strong>AI draft reply.</strong> It drafts a reply using the company&rsquo;s approved templates and the summary, saved as a draft for the assigned rep.</li>
  <li><strong>Human approval.</strong> The rep reviews, edits and sends. Nothing goes to the customer automatically.</li>
  <li><strong>Feedback loop.</strong> Reps mark drafts as &ldquo;used as is&rdquo;, &ldquo;edited&rdquo; or &ldquo;rewritten&rdquo; with a picklist, which gives you a simple quality measure after a month.</li>
</ol>
<p>The result is faster first responses without handing customer communication to a model. If the drafts prove reliable, you can decide later whether some categories can be sent automatically.</p>

<h2 id="measure">How to measure whether it works</h2>
<ul>
  <li><strong>Time saved:</strong> minutes per enquiry, per deal review or per call summary, before and after.</li>
  <li><strong>Quality:</strong> the share of AI drafts used with little or no editing.</li>
  <li><strong>Outcomes:</strong> first-response time, conversion rate and data completeness on key fields.</li>
  <li><strong>Clean-up cost:</strong> time spent correcting AI-made changes. If this rises, tighten the rules.</li>
</ul>

<h2 id="mistakes">Common mistakes</h2>
<ul>
  <li>Turning on AI features across the whole CRM at once, instead of one use case at a time.</li>
  <li>Letting automated changes overwrite fields without recording the source.</li>
  <li>Expecting AI to fix a sales process that was never defined.</li>
  <li>Ignoring data-protection rules about what customer data can be sent to which model and where it is processed.</li>
</ul>
'''

EXT['zoho-analytics-agentic-data-foundations-2026'] = '''
<h2 id="example-dashboard">Example: a sales leader&rsquo;s weekly dashboard</h2>
<p>A dashboard that leadership actually opens every week usually has no more than eight widgets:</p>
<ul>
  <li><strong>Bookings this month versus target,</strong> from CRM deals marked won.</li>
  <li><strong>Invoiced and collected revenue,</strong> from Zoho Books, joined to CRM accounts.</li>
  <li><strong>Pipeline by stage and expected close month,</strong> weighted by probability.</li>
  <li><strong>Deals with no activity in 14 days,</strong> as a table with owners.</li>
  <li><strong>Win rate and average sales cycle</strong> by lead source.</li>
  <li><strong>Top accounts by revenue</strong> with open support tickets from Zoho Desk.</li>
</ul>
<p>Each widget is built on a documented metric, filtered by user so regional managers see their region. That dashboard also becomes the reference for checking Ask Zia&rsquo;s answers.</p>

<h2 id="mistakes">Common mistakes we fix</h2>
<ul>
  <li><strong>Several versions of the same table,</strong> imported at different times by different people. Keep one connected source per system.</li>
  <li><strong>Formula fixes copied into every report.</strong> Move shared logic into query tables.</li>
  <li><strong>Revenue counted twice</strong> because of joins to tables with several rows per deal.</li>
  <li><strong>Dashboards nobody owns.</strong> Give each dashboard an owner who reviews it quarterly.</li>
  <li><strong>Unlimited sharing</strong> of workspaces with raw customer data.</li>
</ul>

<h2 id="governance">Simple routines that keep data trustworthy</h2>
<ul>
  <li>A monthly check that sync jobs are running and record counts match the source systems.</li>
  <li>A quarterly review of unused reports, dashboards and users with access.</li>
  <li>A change log for metric definitions, so everyone knows when and why a number changed.</li>
</ul>
'''

EXT['zoho-partner-software-development'] = '''
<h2 id="compare-providers">Freelancer, agency or partner: a quick comparison</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col"></th><th scope="col">Freelancer</th><th scope="col">Specialist agency or developer team</th><th scope="col">Official Zoho Partner</th></tr></thead>
  <tbody>
    <tr><th scope="row">Best for</th><td>Small, well-defined tasks and scripts</td><td>Custom apps, integrations and full implementations</td><td>Licensing plus implementation, larger rollouts</td></tr>
    <tr><th scope="row">Cost</th><td>Usually lowest</td><td>Moderate</td><td>Varies widely by partner and region</td></tr>
    <tr><th scope="row">Continuity</th><td>Depends on one person</td><td>A team that shares knowledge</td><td>A team with a formal relationship with Zoho</td></tr>
    <tr><th scope="row">Licences</th><td>You buy from Zoho</td><td>You buy from Zoho</td><td>Can be bought through the partner</td></tr>
    <tr><th scope="row">Watch for</th><td>Availability and handover</td><td>Who actually does the work</td><td>Whether the partner level matches your project size</td></tr>
  </tbody>
</table>
</div>

<h2 id="trial">Start with a small paid piece of work</h2>
<p>If you are unsure, start with a small paid task before committing to a full project: a discovery workshop, a design document, or one automation. Within a week or two you will see how the provider communicates, documents and handles feedback. Hourly pricing makes this easy. We charge US$15 per hour for exactly this kind of work.</p>

<h2 id="onboarding">Set your developer up for success</h2>
<ul>
  <li>Give them an admin user, not your own login, so their actions are traceable.</li>
  <li>Name one decision-maker on your side who can answer questions quickly.</li>
  <li>Share examples of real records, documents and reports your team uses today.</li>
  <li>Agree how and how often progress is shown, for example a weekly demo.</li>
  <li>Keep the documentation they produce somewhere your whole team can find it.</li>
</ul>
'''
