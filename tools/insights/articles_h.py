# Article content, part H (21 October 2026 run).

ARTICLES = []

# ------------------------------------------------------------------ ERPNext vs Zoho ERP
ARTICLES.append(dict(
    slug='erpnext-vs-zoho-erp',
    title='ERPNext vs Zoho ERP for Indian Manufacturers: Open Source You Run, or a Subscription Zoho Runs?',
    seo_title='ERPNext vs Zoho ERP for Manufacturers (India)',
    description='ERPNext and Zoho ERP compared for Indian manufacturers: how each is licensed and hosted, BOMs and job cards, job work and subcontracting, GST through the India Compliance app or built in, and a test plan for your shortlist.',
    lead='Most ERPNext vs Zoho comparisons put ERPNext against Zoho One or Zoho Inventory, which have no manufacturing module. Since January 2026 the fair comparison for an Indian factory is ERPNext against Zoho ERP. Both now have bills of materials, job cards and subcontracting. The real difference is who runs the system and who you call when something breaks.',
    category='Manufacturing', keyword='erpnext vs zoho',
    published='2026-10-21', modified='2026-10-21',
    cover_alt='ERPNext vs Zoho ERP: open source you run, or a subscription Zoho runs. A checklist of six tests to run in both trials: who hosts, updates and supports it, a multi-level BOM run through job cards, stock lying with each job worker, where the ITC-04 data comes from, an e-way bill from the right document, and how custom changes and APIs are built. Beside it an analyst figure with the takeaway to decide who will host and support it first, and how they differ: ERPNext has no per-user licence, Zoho ERP has GST built in and is hosted by Zoho, and both have BOMs, job cards and subcontracting. Facts: ERPNext is GPL-3.0, Zoho ERP Standard has a 5-user minimum, and Zoho ERP is not in Zoho One',
    caption='Both products can make a factory run. The deciding question is who will run the product.',
    related=['zoho-erp-vs-odoo-manufacturing', 'tranzact-vs-zoho-erp', 'zoho-for-manufacturing'],
    body='''
<p>Search for &ldquo;ERPNext vs Zoho&rdquo; and the top results compare ERPNext with Zoho One or Zoho Inventory. Neither of those has a manufacturing module, so the comparison is lopsided before it starts. Zoho ERP, launched in India in January 2026 and sold separately from Zoho One, has bills of materials, manufacturing orders, job cards, quality inspections and subcontracting.</p>
<p>Every feature below was checked on Frappe&rsquo;s and Zoho&rsquo;s own pages on 21 October 2026. Where a vendor&rsquo;s page does not say something, we say so. We do not quote prices: see the official <a href="https://frappe.io/erpnext/pricing" target="_blank" rel="noopener">ERPNext pricing</a> and <a href="https://www.zoho.com/en-in/erp/pricing/" target="_blank" rel="noopener">Zoho ERP pricing</a> pages.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Choose ERPNext</strong> if you want open-source software with no per-user licence, and you have an in-house technical person or a reliable implementation partner to host, configure and maintain it.</li>
  <li><strong>Choose Zoho ERP</strong> if you want a subscription that Zoho hosts and updates, with accounts, GST and production in one product, and you are comfortable paying per user.</li>
  <li><strong>Decide on support first.</strong> With ERPNext you choose who supports you; with Zoho ERP the product comes from one vendor. That choice shapes cost and risk more than any single feature.</li>
</ul>

<h2 id="two-models">Two ways to buy an ERP</h2>
<p><strong>ERPNext</strong> is built by Frappe and released as free, open-source software under the GPL-3.0 licence. You can install it on your own server at no licence cost, or host it on Frappe Cloud, which Frappe says is billed for the resources you use rather than per user and comes with a 14-day trial. Frappe does not implement ERPNext itself; it points customers to its partner network, and its product warranty covers bug fixes, not functional support. Indian GST features come from a separate, installable <strong>India Compliance</strong> app.</p>
<p><strong>Zoho ERP</strong> is a cloud subscription sold and run by Zoho. It has <strong>Standard</strong>, <strong>Premium</strong> and <strong>Custom</strong> plans, billed monthly or yearly, with a 14-day trial and no long-term contract. Pricing is per user, with some lines per employee, and Standard needs at least five users. Each plan also has a yearly transaction allowance per organisation: 100,000 on Standard and 300,000 on Premium, counting sales, purchase and manufacturing orders. Zoho&rsquo;s FAQ is clear that Zoho ERP is not part of Zoho One.</p>

<h2 id="at-a-glance">ERPNext and Zoho ERP at a glance</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">ERPNext</th><th scope="col">Zoho ERP</th></tr></thead>
  <tbody>
    <tr><th scope="row">Licence</th><td>Free, open source (GPL-3.0)</td><td>Per-user subscription; Standard, Premium, Custom</td></tr>
    <tr><th scope="row">Hosting</th><td>Self-hosted, or Frappe Cloud</td><td>Hosted by Zoho</td></tr>
    <tr><th scope="row">Usage limits</th><td>None set by a licence; depends on your server or Frappe Cloud plan</td><td>100,000 transactions a year on Standard, 300,000 on Premium</td></tr>
    <tr><th scope="row">Production</th><td>BOM, Work Order, Job Card, Workstation, Production Plan, capacity planning</td><td>BOM, manufacturing orders, job cards, shop floor, work centers, planning module</td></tr>
    <tr><th scope="row">Subcontracting</th><td>Subcontracting Order, Send to Subcontractor, Subcontracting Receipt</td><td>Subcontract BOMs, subcontract manufacturing orders, purchase orders and material transfers</td></tr>
    <tr><th scope="row">Quality</th><td>Quality Inspection, including against a Job Card</td><td>Quality templates, rules, inspections and an inspection worklist</td></tr>
    <tr><th scope="row">GST</th><td>India Compliance app: GST, e-invoice, e-way bill, TDS and TCS</td><td>Built in: GST filing, e-way bills, TDS</td></tr>
    <tr><th scope="row">Customisation</th><td>No-code forms and workflows, scripts, or changes to the code itself</td><td>Custom modules (up to 25 on Standard and Premium); API through a paid add-on</td></tr>
  </tbody>
</table>
</div>

<h2 id="production">Bills of materials, job cards and planning</h2>
<p>On the shop floor, the two products are closer than most comparisons suggest.</p>
<ul>
  <li><strong>ERPNext</strong> creates a <strong>Job Card</strong> for each operation automatically when a Work Order is submitted, assigned to a Workstation. Operators log time with Start and Complete buttons, record scrap on the Job Card, and can raise a Quality Inspection against it for semi-finished goods. Since version 16, a Pending Qty field lets a Job Card close with the shortfall counted as process loss. Capacity planning is on by default and schedules Job Cards against Workstation hours, and the documentation covers Production Plans and material requirements planning.</li>
  <li><strong>Zoho ERP</strong> has bills of materials that list components and operations, manufacturing orders, job cards, a shop floor view and a manufacturing calendar. Its manufacturing page says the planning module turns production plans into manufacturing orders and can split one operation across several work centers. Batches, lots and serial numbers can be linked to manufacturing and finished goods, and there is a report for delayed job cards.</li>
</ul>
<p>Both will handle a multi-level BOM with routing. Test the one thing your factory does that is unusual, such as alternate materials, rework, or a step done at a customer&rsquo;s site, rather than the standard flow every demo shows.</p>

<h2 id="job-work">Job work and subcontracting</h2>
<p>Job work is where an Indian manufacturer finds out whether an ERP fits. You send material to a job worker, track what is lying with them, receive finished goods and some scrap back, and report all of it to GST on Form ITC-04: half-yearly if turnover is above &#8377;5 crore, yearly if it is not.</p>

<figure style="margin:2rem auto;max-width:660px">
<svg viewBox="0 0 660 270" role="img" aria-labelledby="ej-title ej-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="ej-title">The same job work cycle in ERPNext and Zoho ERP</title>
  <desc id="ej-desc">Material goes from your store to the job worker and comes back as finished goods and scrap. In ERPNext the documents are Subcontracting Order, a Send to Subcontractor stock entry and a Subcontracting Receipt. In Zoho ERP they are a subcontract manufacturing order with purchase orders and material transfers.</desc>
  <style>
    .ej-out{animation:ej-go 5s ease-in-out infinite}
    .ej-back{animation:ej-ret 5s ease-in-out infinite}
    @keyframes ej-go{0%,8%{transform:translateX(0);opacity:0}15%{opacity:1}45%{transform:translateX(330px);opacity:1}52%,100%{transform:translateX(330px);opacity:0}}
    @keyframes ej-ret{0%,50%{transform:translateX(0);opacity:0}57%{opacity:1}90%{transform:translateX(-330px);opacity:1}97%,100%{transform:translateX(-330px);opacity:0}}
    @media (prefers-reduced-motion: reduce){.ej-out,.ej-back{animation:none;opacity:0}}
  </style>
  <rect x="20" y="20" width="200" height="86" rx="12" fill="#ECFDF5" stroke="#0F766E" stroke-width="2"/>
  <text x="120" y="56" font-size="16" font-weight="700" fill="#0F766E" text-anchor="middle">Your store</text>
  <text x="120" y="80" font-size="12.5" fill="#4B5563" text-anchor="middle">Raw material, finished goods</text>
  <rect x="440" y="20" width="200" height="86" rx="12" fill="#fff" stroke="#0F766E" stroke-width="2"/>
  <text x="540" y="56" font-size="16" font-weight="700" fill="#0F766E" text-anchor="middle">Job worker</text>
  <text x="540" y="80" font-size="12.5" fill="#4B5563" text-anchor="middle">Stock lying with them</text>
  <path d="M228 46h204" stroke="#0F766E" stroke-width="2.5" marker-end="url(#ej-a)"/>
  <path d="M432 82H228" stroke="#0F766E" stroke-width="2.5" stroke-dasharray="6 5" marker-end="url(#ej-a)"/>
  <defs><marker id="ej-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#0F766E"/></marker></defs>
  <text x="330" y="38" font-size="12" fill="#4B5563" text-anchor="middle">material out</text>
  <text x="330" y="100" font-size="12" fill="#4B5563" text-anchor="middle">finished goods and scrap back</text>
  <circle class="ej-out" cx="250" cy="46" r="7" fill="#F59E0B"/>
  <circle class="ej-back" cx="410" cy="82" r="7" fill="#F59E0B"/>
  <text x="20" y="150" font-size="14" font-weight="700" fill="#1A1A2E">ERPNext</text>
  <rect x="20" y="160" width="300" height="94" rx="12" fill="#ECFDF5" stroke="#0F766E" stroke-width="1.5"/>
  <text x="36" y="188" font-size="12.5" fill="#1A1A2E">1. Purchase Order (Is Subcontracted)</text>
  <text x="36" y="210" font-size="12.5" fill="#1A1A2E">2. Subcontracting Order</text>
  <text x="36" y="232" font-size="12.5" fill="#1A1A2E">3. Send to Subcontractor, then Receipt</text>
  <text x="340" y="150" font-size="14" font-weight="700" fill="#1A1A2E">Zoho ERP</text>
  <rect x="340" y="160" width="300" height="94" rx="12" fill="#fff" stroke="#0F766E" stroke-width="1.5"/>
  <text x="356" y="188" font-size="12.5" fill="#1A1A2E">1. Subcontract bill of materials</text>
  <text x="356" y="210" font-size="12.5" fill="#1A1A2E">2. Subcontract manufacturing order</text>
  <text x="356" y="232" font-size="12.5" fill="#1A1A2E">3. Purchase order, material transfers</text>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">Both products model job work as a subcontracting flow. What you need to see in a demo is the stock lying with each job worker and the data for ITC-04.</figcaption>
</figure>

<p><strong>ERPNext</strong> documents the flow step by step. You mark a Purchase Order for the service as <em>Is Subcontracted</em>, create a <strong>Subcontracting Order</strong> from it, move material to the supplier&rsquo;s warehouse with a <em>Send to Subcontractor</em> stock entry, and receive finished goods and scrap with a <strong>Subcontracting Receipt</strong>. Raw materials can be backflushed from the BOM or from what was actually transferred, and one Purchase Order can be split across several Subcontracting Orders. On the India side, the India Compliance team announced e-way bills from a stock entry or Subcontracting Receipt in 2024 and listed ITC-04 features as in progress, so check the current release before you rely on it.</p>
<p><strong>Zoho ERP</strong>&rsquo;s help has a Subcontract Manufacturing section covering subcontract bills of materials, subcontract manufacturing orders, purchase orders and material transfers, plus delivery challans in Sales. Its feature pages do not mention ITC-04, and its GST filing help lists GSTR-1, GSTR-3B, GSTR-2A and 2B reconciliation and GSTR-9.</p>
<p>So in each demo, send material to a job worker, bring part of it back with some wastage, and ask to see three things: stock lying with that job worker, the document that travelled with the goods, and the data you would file in ITC-04. Our <a href="/insights/zoho-erp-vs-odoo-manufacturing/">Zoho ERP vs Odoo comparison</a> uses the same test.</p>

<h2 id="gst">GST, e-way bills and statutory work</h2>
<p>With <strong>Zoho ERP</strong>, GST filing, e-way bills and TDS are part of the product, and Zoho maintains them. There is no separate compliance component to install or upgrade.</p>
<p>With <strong>ERPNext</strong>, GST comes from the India Compliance app, which adds GST setup, HSN and SAC codes, GST returns and statutory reports, e-invoices, e-way bills, and TDS and TCS. It is a separate component: whoever hosts your ERPNext needs to keep it updated in step with ERPNext itself. Frappe&rsquo;s own page notes that the features available depend on the app version installed.</p>
<p>If your accountant files from Tally today and is not ready to move, neither product is the whole answer. Our <a href="/insights/zoho-books-vs-tallyprime/">Zoho Books vs TallyPrime guide</a> covers that decision first.</p>

<h2 id="cost">What you actually pay for</h2>
<p>&ldquo;ERPNext is free&rdquo; is true of the licence, not of a working system. With ERPNext, budget for hosting (your own server or Frappe Cloud), implementation by a partner, and a support arrangement, because Frappe Cloud hosting does not include functional support. With Zoho ERP, budget for per-user and per-employee licences, any API add-on, and implementation help.</p>
<p>Compare three years, not one. On the ERPNext side, include upgrades: open-source ERPs move quickly, and someone has to test your customisations against each new version. On the Zoho side, include user growth and whether you will outgrow the transaction allowance of your plan.</p>

<h2 id="customisation">Customisation and integrations</h2>
<p><strong>ERPNext</strong> is the more open of the two. You can change forms, workflows and permissions without code, write scripts in the interface, or change the source itself. That freedom is valuable, and it is also a risk: heavy changes to the core make upgrades harder, so keep custom logic in a separate app where you can.</p>
<p><strong>Zoho ERP</strong> allows up to 25 custom modules on Standard and Premium, unlimited custom reports on Premium, and API access through a paid add-on of 10,000 calls a day per add-on. For processes outside the ERP, such as a dealer portal or a machine checklist on a tablet, a Zoho Creator app is the usual route, connected to the ERP through its API. Zoho ERP also has a documented integration with Zoho CRM for the sales side.</p>

<h2 id="who-fits">Which one fits your factory</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Your situation</th><th scope="col">Usually the better fit</th></tr></thead>
  <tbody>
    <tr><th scope="row">You have an IT person or a partner you trust for the long term</th><td>ERPNext</td></tr>
    <tr><th scope="row">You want the system on your own servers</th><td>ERPNext</td></tr>
    <tr><th scope="row">You need to change how the software itself works</th><td>ERPNext</td></tr>
    <tr><th scope="row">No in-house IT, and you want the vendor to run updates and GST changes</th><td>Zoho ERP</td></tr>
    <tr><th scope="row">You already run Zoho CRM, Books or Creator</th><td>Zoho ERP</td></tr>
    <tr><th scope="row">You want one vendor accountable for the product</th><td>Zoho ERP</td></tr>
  </tbody>
</table>
</div>
<p>If your shortlist also includes Odoo or TranZact, see our comparisons of <a href="/insights/zoho-erp-vs-odoo-manufacturing/">Zoho ERP vs Odoo</a> and <a href="/insights/tranzact-vs-zoho-erp/">TranZact vs Zoho ERP</a>, and our overview of <a href="/insights/zoho-for-manufacturing/">every Zoho route for manufacturers</a>.</p>

<h2 id="test-plan">A test plan for both trials</h2>
<p>Both products offer a 14-day trial. Use it on your own data, not the sample company.</p>
<ul class="checklist">
  <li>Write down who will host, update and support the system for the next three years, and what that costs.</li>
  <li>Build one real multi-level BOM with routing and run a work order through job cards to finished goods.</li>
  <li>Send material to a job worker, receive part of it back with wastage, and find the stock still lying with them.</li>
  <li>Ask where the ITC-04 data comes from, and in what format.</li>
  <li>Raise an e-way bill from the document your stores team would really use.</li>
  <li>List the two integrations you need, such as CRM or a machine data feed, and ask how each is built and maintained.</li>
</ul>
<p>If you choose the Zoho route and need integrations or custom apps around Zoho ERP, our <a href="/zoho-integrations/">Zoho integrations</a> page explains how we work.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Is ERPNext really free?',
         'The software is. ERPNext is open source under the GPL-3.0 licence and can be self-hosted at no licence cost. You still pay for hosting, implementation and support, either to Frappe, through Frappe Cloud and its support plans, or to a partner.'),
        ('Does ERPNext handle Indian GST?',
         'Yes, through the India Compliance app, which adds GST setup, HSN and SAC codes, GST returns and reports, e-invoices, e-way bills, and TDS and TCS. It is installed alongside ERPNext and should be kept updated with it.'),
        ('Does Zoho ERP support job work?',
         'Zoho ERP has a subcontract manufacturing flow with subcontract bills of materials, subcontract manufacturing orders, purchase orders and material transfers. Its pages do not mention Form GST ITC-04, so ask to see where that data would come from in a demo.'),
        ('Is Zoho ERP part of Zoho One?',
         'No. Zoho says Zoho ERP is a separate product with its own Standard, Premium and Custom plans. It is sold through Zoho\'s Indian website and has a 14-day free trial.'),
        ('Can we move from ERPNext to Zoho ERP later, or the other way?',
         'Yes, but treat it as a new implementation. Masters such as items, customers, suppliers and BOMs move across with planning; open transactions, stock with job workers and opening balances need a clean cut-over date agreed with your accountant.'),
    ],
))

# ------------------------------------------------------------------ Zoho One vs Microsoft 365
ARTICLES.append(dict(
    slug='zoho-one-vs-microsoft-365',
    title='Zoho One vs Microsoft 365: Different Suites, and When to Run Both',
    seo_title='Zoho One vs Microsoft 365 (2026 Comparison)',
    description='Zoho One and Microsoft 365 compared fairly: what each suite actually covers, the 2026 plan names and licensing rules, email, files and chat, security, running both side by side, and what manufacturers need on top.',
    lead='Zoho One and Microsoft 365 are often compared as if they were rivals for the same job. They overlap on email, chat, files and meetings, but most of what each one includes the other does not. The useful question is not which suite wins, but which jobs you need each one to do.',
    category='Comparisons', keyword='zoho one vs microsoft 365',
    published='2026-10-21', modified='2026-10-21',
    cover_alt='Zoho One vs Microsoft 365 as three groups: only in Zoho One are CRM, Books and Inventory, Desk, People and Payroll, and Creator and Analytics; in both are email, chat, files and video meetings; only in Microsoft 365 are desktop Word, Excel and PowerPoint, Teams, Intune and Defender on Premium, and Copilot in the apps. An office worker beside the takeaway that many businesses run both, a choose-by-the-job list, and three facts: a 300-user ceiling on Microsoft 365 business plans, two Zoho One plans (Essentials and Standard), and split delivery for Zoho Mail beside Exchange',
    caption='The overlap is smaller than it looks. Most businesses are really deciding where email and documents live.',
    related=['zoho-one-implementation-checklist', 'zoho-creator-vs-power-apps', 'zoho-crm-vs-salesforce'],
    body='''
<p>Most &ldquo;Zoho One vs Microsoft 365&rdquo; articles add up a stack of Microsoft and third-party products, put a single Zoho One price next to it and declare a winner. That skips the part that matters: the two suites are built for different jobs, and many businesses end up running both.</p>
<p>Every plan and feature below was checked on Zoho&rsquo;s and Microsoft&rsquo;s own pages on 21 October 2026. We do not quote prices, because both vary by country and change often; see the official <a href="https://www.zoho.com/one/pricing/" target="_blank" rel="noopener">Zoho One pricing</a> and <a href="https://www.microsoft.com/en-us/microsoft-365/business/microsoft-365-plans-and-pricing" target="_blank" rel="noopener">Microsoft 365 business plans</a> pages. We implement Zoho, so read this with that in mind; we have tried to be fair to Microsoft, because for some teams it is the better fit.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Choose Microsoft 365</strong> if what you need is email, desktop Office apps, Teams and device security, and your CRM, accounting and support tools are already chosen.</li>
  <li><strong>Choose Zoho One</strong> if you need the business applications themselves, such as CRM, accounting, inventory, helpdesk, HR and custom apps, in one subscription with one set of users.</li>
  <li><strong>Run both</strong> if your team lives in Outlook, Word and Excel but you also need those business applications. This is a common, supported setup, not a compromise.</li>
</ul>

<h2 id="what-each-is">What each suite actually is</h2>
<p><strong>Microsoft 365 for business</strong> is a productivity, collaboration and security suite: Outlook and Exchange email, Word, Excel and PowerPoint, Teams, OneDrive and SharePoint, with device management and threat protection on the top plan. Microsoft sells CRM and ERP separately, as Dynamics 365 products.</p>
<p><strong>Zoho One</strong> is a bundle of business applications. Its plan details list CRM, Books, Inventory, Payroll and Expense, Desk, People and Recruit, Projects, Creator, Analytics and Flow, marketing apps, and collaboration apps including Mail, Cliq, WorkDrive and Meeting, all managed from Zoho Directory. Zoho&rsquo;s office apps, Writer, Sheet and Show, are also sold on their own as part of Zoho Workplace.</p>
<p>The overlap is email, chat, file storage and video meetings. Everything else sits on one side only.</p>

<h2 id="plans">The 2026 plans in plain words</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Plan</th><th scope="col">What it is</th><th scope="col">Key rule</th></tr></thead>
  <tbody>
    <tr><th scope="row">Zoho One Essentials</th><td>15+ apps across CRM, collaboration, finance, marketing, customer service and HR</td><td>Per user, annual licensing</td></tr>
    <tr><th scope="row">Zoho One Standard, All Employee</th><td>50+ apps</td><td>Every employee on the payroll must be licensed</td></tr>
    <tr><th scope="row">Zoho One Standard, Flexible User</th><td>50+ apps</td><td>License only the users who need it</td></tr>
    <tr><th scope="row">Microsoft 365 Business Basic</th><td>Web and mobile Office apps, email, Teams, 1 TB OneDrive</td><td>Copilot Chat included; full Copilot is an add-on</td></tr>
    <tr><th scope="row">Microsoft 365 Business Standard with Copilot</th><td>Adds desktop Office apps</td><td>Copilot in the apps</td></tr>
    <tr><th scope="row">Microsoft 365 Business Premium with Copilot</th><td>Adds Intune, Defender for Business and advanced Entra ID</td><td>Copilot in the apps; 1.5 TB email archive</td></tr>
  </tbody>
</table>
</div>
<p>Two rules catch people out. Microsoft&rsquo;s business plans are designed for up to <strong>300 users</strong> across the whole business plan family; larger organisations move to enterprise plans. Zoho One&rsquo;s <strong>All Employee</strong> pricing must cover everyone on the payroll, and Zoho asks you to buy the missing licences or switch to Flexible User pricing if it does not. Microsoft also sells each business plan without Teams.</p>
<p>On billing, Zoho One is monthly or annual with no long-term contract. Microsoft offers a monthly commitment that can be cancelled at any time, or an annual commitment paid monthly or upfront, with early-cancellation terms on the annual options.</p>

<h2 id="overlap">Where they overlap: email, files, chat and meetings</h2>
<p><strong>Email.</strong> Exchange Online gives each business user a 100 GB mailbox. Zoho Mail is included in Zoho One. Zoho&rsquo;s FAQ notes that you can use Zoho Mail either inside Zoho One or as a standalone product, but not both on the same domain.</p>
<p><strong>Documents.</strong> If your team, your customers or your auditors exchange complex Excel models and Word documents all day, desktop Office on Business Standard or Premium is hard to replace. Zoho&rsquo;s office apps handle everyday documents and spreadsheets well; test your own most complex files before you plan to move them.</p>
<p><strong>Chat and meetings.</strong> Teams and Zoho Cliq with Zoho Meeting cover the same ground. The deciding factor is usually where your customers and partners already are.</p>
<p><strong>Files.</strong> Microsoft gives 1 TB of OneDrive per user plus SharePoint team sites. Zoho One includes WorkDrive for team files. Both are fine for most small businesses; the effort is in moving folders and permissions, not in the storage itself.</p>

<h2 id="only-zoho">What only Zoho One covers</h2>
<p>This is the bigger side of the comparison. A sales team needs a CRM; finance needs accounting with local tax; operations needs inventory; support needs a helpdesk; HR needs records, leave and payroll. Zoho One includes all of these, and they share users and customer records. A quote in Zoho CRM can become an invoice in Zoho Books without a connector.</p>
<p>It also includes <strong>Zoho Creator</strong> for custom apps and <strong>Zoho Analytics</strong> for reporting across all of them. Microsoft&rsquo;s nearest equivalent for custom apps, Power Apps, needs its own Premium licence for Dataverse and premium connectors; our <a href="/insights/zoho-creator-vs-power-apps/">Zoho Creator vs Power Apps comparison</a> covers that choice in detail, and our <a href="/insights/zoho-analytics-vs-power-bi/">Zoho Analytics vs Power BI comparison</a> does the same for reporting.</p>

<h2 id="only-microsoft">What only Microsoft 365 covers</h2>
<ul>
  <li><strong>Desktop Office</strong> on Business Standard and Premium, still the standard for heavy spreadsheet and document work.</li>
  <li><strong>Device and threat protection</strong> on Business Premium: Intune for device management, Defender for Business and Defender for Office 365, and advanced Entra ID. Zoho One includes mobile device management for 25 devices by default, which is lighter.</li>
  <li><strong>Copilot</strong> inside the Office apps on the &ldquo;with Copilot&rdquo; plans, and Copilot Chat on Business Basic. Zoho&rsquo;s AI, Zia, works inside its business apps instead.</li>
</ul>

<h2 id="both">Running both side by side</h2>
<p>Many growing companies keep Microsoft 365 for email and documents and add Zoho One, or a few Zoho apps, for the business processes. The pieces that make this work are documented:</p>
<ul>
  <li><strong>Zoho CRM with Microsoft 365:</strong> Zoho describes syncing contacts, tasks and calendar events, adding leads from email, viewing CRM dashboards in a Teams tab, and sharing CRM records in Teams chats.</li>
  <li><strong>Email during a move:</strong> Zoho Mail supports split delivery with Office 365, so some users can be on Zoho Mail while others stay on Exchange under the same domain.</li>
  <li><strong>Licensing:</strong> Flexible User pricing lets you license Zoho One only for the people who use the business apps, while everyone keeps Microsoft 365.</li>
</ul>
<p>The cost of running both is two admin consoles and two sets of users to keep in step. Agree who owns each, and decide early whether Zoho or Microsoft is the identity provider for single sign-on.</p>

<figure style="margin:2rem auto;max-width:640px">
<svg viewBox="0 0 640 270" role="img" aria-labelledby="zm-title zm-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="zm-title">How the two suites overlap</title>
  <desc id="zm-desc">Two overlapping circles. Zoho One alone covers CRM, accounting, inventory, helpdesk, HR and custom apps. Microsoft 365 alone covers desktop Office, device management and Copilot in Office apps. Both cover email, chat, files and meetings.</desc>
  <style>
    .zm-l{animation:zm-in 4s ease-in-out infinite alternate}
    .zm-r{animation:zm-in 4s ease-in-out infinite alternate-reverse}
    @keyframes zm-in{from{opacity:.55}to{opacity:.9}}
    @media (prefers-reduced-motion: reduce){.zm-l,.zm-r{animation:none;opacity:.75}}
  </style>
  <circle class="zm-l" cx="235" cy="135" r="125" fill="#DBEAFE" stroke="#1D4ED8" stroke-width="2"/>
  <circle class="zm-r" cx="405" cy="135" r="125" fill="#E0E7FF" stroke="#3730A3" stroke-width="2"/>
  <text x="180" y="88" font-size="15" font-weight="700" fill="#1D4ED8" text-anchor="middle">Zoho One</text>
  <text x="180" y="112" font-size="12.5" fill="#1A1A2E" text-anchor="middle">CRM, Books</text>
  <text x="180" y="134" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Inventory, Desk</text>
  <text x="180" y="156" font-size="12.5" fill="#1A1A2E" text-anchor="middle">People, Payroll</text>
  <text x="180" y="178" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Creator, Analytics</text>
  <text x="320" y="96" font-size="13" font-weight="700" fill="#1A1A2E" text-anchor="middle">Both</text>
  <text x="320" y="122" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Email</text>
  <text x="320" y="144" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Chat</text>
  <text x="320" y="166" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Files</text>
  <text x="320" y="188" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Meetings</text>
  <text x="452" y="88" font-size="14" font-weight="700" fill="#3730A3" text-anchor="middle">Microsoft 365</text>
  <text x="460" y="112" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Desktop Office</text>
  <text x="460" y="134" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Intune, Defender</text>
  <text x="460" y="156" font-size="12.5" fill="#1A1A2E" text-anchor="middle">Copilot in apps</text>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">Intune and Defender for Business are on Business Premium; desktop Office starts at Business Standard.</figcaption>
</figure>

<h2 id="manufacturers">A note for manufacturers</h2>
<p>Neither suite runs production. Zoho One includes Zoho Inventory, which handles assemblies but has no manufacturing module, and Zoho ERP, which does, is a separate product that is not part of Zoho One. On the Microsoft side, production planning sits in Dynamics 365 products, outside the Microsoft 365 business plans. Our guide to <a href="/insights/zoho-for-manufacturing/">Zoho for manufacturing</a> sets out the Zoho routes, and our <a href="/insights/zoho-one-implementation-checklist/">Zoho One implementation checklist</a> covers what to add on top.</p>

<h2 id="how-to-choose">How to choose</h2>
<ol>
  <li><strong>List the jobs,</strong> not the apps: email, documents, sales, accounts, stock, support, HR.</li>
  <li><strong>Mark which ones you already solve</strong> and are happy with. Do not replace a tool that works just to fill a bundle.</li>
  <li><strong>Check the licensing rule</strong> that applies to you: All Employee or Flexible User on Zoho One, and the 300-user ceiling on Microsoft&rsquo;s business plans.</li>
  <li><strong>Test your hardest files</strong> in Zoho&rsquo;s office apps before planning an email and document move.</li>
  <li><strong>Price three years</strong> of the setup you would really run, including implementation.</li>
</ol>
<p>If you decide to add Zoho alongside Microsoft 365, our <a href="/zoho-integrations/">Zoho integrations</a> page explains how we connect the two.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Can Zoho One replace Microsoft 365?',
         'For many small businesses, yes: Zoho One includes Mail, Cliq, WorkDrive and Meeting alongside its business apps. Teams that depend on desktop Excel and Word, or on Intune and Defender for device security, usually keep Microsoft 365 and add Zoho for the business applications.'),
        ('Can we use Zoho CRM with Outlook and Teams?',
         'Yes. Zoho describes a Microsoft 365 integration for Zoho CRM that syncs contacts, tasks and calendar events, lets users add leads from email, shows CRM dashboards in a Teams tab and shares CRM records in Teams chats.'),
        ('Does Microsoft 365 include a CRM?',
         'The Microsoft 365 business plans focus on email, Office apps, Teams, storage and security. Microsoft sells its CRM and ERP applications separately as Dynamics 365 products.'),
        ('What is the difference between Zoho One Essentials and Standard?',
         'Essentials has 15+ apps across CRM, collaboration, finance, marketing, customer service and HR, billed per user with annual licensing. Standard has 50+ apps and offers All Employee pricing, which must cover everyone on the payroll, or Flexible User pricing for chosen users.'),
        ('Is Zoho ERP included in Zoho One?',
         'No. Zoho lists Zoho ERP among the products not included in Zoho One. It is sold separately, with its own plans.'),
    ],
))

# ------------------------------------------------------------------ Zoho CRM API limits
ARTICLES.append(dict(
    slug='zoho-crm-api-limits',
    title='Zoho CRM API Limits Explained: Credits, Concurrency and How to Stay Under Them',
    seo_title='Zoho CRM API Limits Explained (v8, 2026)',
    description='Zoho CRM API limits for 2026: daily credits by edition, what each call costs, concurrency and sub-concurrency, Bulk Read and COQL caps, alerts and the API dashboard, and how to design integrations that stay under them.',
    lead='Most integration failures with Zoho CRM are not bugs. They are limits: a sync that ran fine with 500 records hits a wall at 50,000, or two jobs start at the same time and one gets a 429 error. Zoho CRM counts API usage in credits over a rolling 24 hours and caps how many calls run at once. Here is how both work, with the current figures.',
    category='Integrations', keyword='zoho crm api limits',
    published='2026-10-21', modified='2026-10-21',
    cover_alt='Zoho CRM API limits: credits cap how much you do in a day, concurrency caps how much at once. One big figure, 50,000 base credits per rolling 24 hours on paid editions plus more per user licence, with 10 to 25 calls running at once per org per app, 10 heavy calls at once such as COQL, convert lead and bulk upserts, and HTTP 429 when either limit or the credits run out. Key point: a 429 with credits left means too many calls at once. Facts: upserting 100 records in one call costs 10 credits, there is no midnight reset, and default usage alerts fire at 80, 90 and 100 percent',
    caption='Credits limit how much you do in a day. Concurrency limits how much you do at once. Most problems are the second kind.',
    related=['zoho-flow-vs-deluge', 'zoho-mcp-claude-chatgpt', 'deluge-script-examples'],
    body='''
<p>If you are planning an integration with Zoho CRM, or one has started failing, you need two numbers: how many API credits your organisation gets in 24 hours, and how many calls it can run at the same time. Many pages still quote older figures, so everything below comes from Zoho&rsquo;s current <a href="https://www.zoho.com/crm/developer/docs/api/v8/api-limits.html" target="_blank" rel="noopener">API v8 limits page</a> and related developer docs, checked on 21 October 2026. Zoho changes these from time to time, so check the page before you size a large project.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Credits:</strong> paid editions get 50,000 credits per rolling 24 hours plus a set number per user licence, up to an edition maximum. Most calls cost 1 credit; some cost more.</li>
  <li><strong>Concurrency:</strong> each organisation can run 10 to 25 calls at once per app, depending on edition, and only 10 at once of the heavier calls.</li>
  <li><strong>When you exceed either,</strong> Zoho returns HTTP 429. Credits recover as the 24-hour window rolls; concurrency recovers as calls finish.</li>
</ul>

<h2 id="credits">Daily credits by edition</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Edition</th><th scope="col">Credits per 24 hours</th><th scope="col">Maximum</th></tr></thead>
  <tbody>
    <tr><th scope="row">Free</th><td>5,000</td><td>5,000</td></tr>
    <tr><th scope="row">Standard / Starter</th><td>50,000 + 250 per user licence + add-ons</td><td>100,000</td></tr>
    <tr><th scope="row">Professional</th><td>50,000 + 500 per user licence + add-ons</td><td>3,000,000</td></tr>
    <tr><th scope="row">Enterprise / Zoho One</th><td>50,000 + 1,000 per user licence + add-ons</td><td>5,000,000</td></tr>
    <tr><th scope="row">Ultimate / CRM Plus</th><td>50,000 + 2,000 per user licence + add-ons</td><td>Unlimited</td></tr>
  </tbody>
</table>
</div>
<p>Two details matter. The window is <strong>rolling</strong>: Zoho counts the 24 hours back from each call, so there is no midnight reset to wait for. And <strong>trial editions</strong> get the same limits as the paid edition they trial, so a load test during a trial is a fair test.</p>
<p>A worked example: a company on Professional with 20 user licences gets 50,000 + (20 &times; 500) = 60,000 credits a day. On Enterprise, the same 20 users would get 70,000.</p>

<h2 id="costs">What each call costs</h2>
<p>Most API calls cost 1 credit. The ones that cost more are the ones integrations use most, so check them before you estimate.</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Call</th><th scope="col">Credits</th></tr></thead>
  <tbody>
    <tr><th scope="row">Insert, update or upsert records</th><td>1 per 10 records (up to 100 records a call)</td></tr>
    <tr><th scope="row">Get records using a custom view (cvid)</th><td>3</td></tr>
    <tr><th scope="row">COQL query</th><td>1 for up to 200 records, 2 up to 1,000, 3 up to 2,000</td></tr>
    <tr><th scope="row">Convert lead</th><td>5</td></tr>
    <tr><th scope="row">Send mail</th><td>20</td></tr>
    <tr><th scope="row">Bulk Read job</th><td>50 to start</td></tr>
    <tr><th scope="row">Bulk Write job</th><td>500 to start</td></tr>
    <tr><th scope="row">Mass convert leads</th><td>200</td></tr>
  </tbody>
</table>
</div>
<p>The cheapest way to write data is in batches. Upserting 100 records in one call costs 10 credits; sending the same 100 records one at a time costs 100.</p>

<h2 id="estimate">Estimating credits for your own integration</h2>
<p>Before you build, write down each job the integration will run, how often, and how many records it touches. Then price each job with the table above. For example, a sync that upserts 3,000 changed orders a day in batches of 100 makes 30 calls at 10 credits each, or 300 credits. A dashboard that polls a custom view every five minutes makes 288 calls a day at 3 credits each, or 864 credits. Neither comes close to 60,000.</p>
<p>The jobs that do use real budget are the ones that grow with your data: a full export of every contact each night with paged reads, a loop that sends one email per record, or a migration that writes records one at a time. Those are the jobs to move to Bulk Read, Bulk Write or batched calls first. Leave at least a third of the daily budget free for users, Deluge functions and apps you add later.</p>

<h2 id="concurrency">Concurrency: the limit most integrations hit first</h2>
<p>Concurrency is the number of calls that can be <em>active at the same moment</em>, counted per organisation per app. Zoho sets no per-minute cap; it limits how many calls are in flight.</p>
<ul>
  <li><strong>Concurrency:</strong> Free 5, Standard 10, Professional 15, Enterprise and Zoho One 20, Ultimate and CRM Plus 25.</li>
  <li><strong>Sub-concurrency:</strong> 10 for every edition, shared across the heavier calls: COQL queries, convert lead, send mail, composite requests, record fetches using a custom view or sort, inserts, updates and upserts of more than 10 records, and searches invoked from a function.</li>
</ul>
<p>This is why an integration can fail while the dashboard shows plenty of credits left. A sync that fires 30 parallel requests, or two schedulers that start on the same minute, will see 429 errors on Professional even though the daily budget is barely touched.</p>

<figure style="margin:2rem auto;max-width:640px">
<svg viewBox="0 0 640 200" role="img" aria-labelledby="cc-title cc-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="cc-title">Concurrency slots on a Professional edition</title>
  <desc id="cc-desc">Fifteen slots represent the calls Professional can run at once. As calls finish, slots free up; a sixteenth call arriving while all fifteen are busy receives an HTTP 429 response.</desc>
  <style>
    .cc-s{animation:cc-b 3s ease-in-out infinite}
    .cc-x{animation:cc-r 3s ease-in-out infinite}
    @keyframes cc-b{0%,100%{fill:#15803D}50%{fill:#86EFAC}}
    @keyframes cc-r{0%,40%{opacity:0}55%,85%{opacity:1}100%{opacity:0}}
    @media (prefers-reduced-motion: reduce){.cc-s{animation:none}.cc-x{animation:none;opacity:1}}
  </style>
  <text x="20" y="30" font-size="15" font-weight="700" fill="#1A1A2E">Professional: 15 calls at once</text>
  <g>
    <rect class="cc-s" x="20" y="50" width="30" height="50" rx="6" fill="#15803D"/><rect class="cc-s" x="56" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:.2s"/><rect class="cc-s" x="92" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:.4s"/><rect class="cc-s" x="128" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:.6s"/><rect class="cc-s" x="164" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:.8s"/>
    <rect class="cc-s" x="200" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:1s"/><rect class="cc-s" x="236" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:1.2s"/><rect class="cc-s" x="272" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:1.4s"/><rect class="cc-s" x="308" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:1.6s"/><rect class="cc-s" x="344" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:1.8s"/>
    <rect class="cc-s" x="380" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:2s"/><rect class="cc-s" x="416" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:2.2s"/><rect class="cc-s" x="452" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:2.4s"/><rect class="cc-s" x="488" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:2.6s"/><rect class="cc-s" x="524" y="50" width="30" height="50" rx="6" fill="#15803D" style="animation-delay:2.8s"/>
  </g>
  <g class="cc-x"><rect x="572" y="50" width="48" height="50" rx="6" fill="#FEE2E2" stroke="#B91C1C" stroke-width="2"/><text x="596" y="81" font-size="14" font-weight="700" fill="#B91C1C" text-anchor="middle">429</text></g>
  <text x="20" y="135" font-size="13" fill="#4B5563">Each bar is one call in flight. The 16th call that arrives while all 15 are busy is refused.</text>
  <text x="20" y="160" font-size="13" fill="#4B5563">Of the 15, no more than 10 may be heavy calls such as COQL, convert lead or bulk upserts.</text>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">Credits limit how much you do in a day; concurrency limits how much you do at once.</figcaption>
</figure>

<h2 id="large-reads">Reading large volumes: Get Records, COQL and Bulk Read</h2>
<ul>
  <li><strong>Get Records</strong> returns up to 200 records a page. Page numbers reach the first 2,000 records; beyond that you need the page token, which goes up to 100,000.</li>
  <li><strong>COQL</strong> returns up to 2,000 records a call, with up to 25 conditions in the WHERE clause, and up to 100,000 records for the same criteria across calls.</li>
  <li><strong>Bulk Read</strong> exports up to 200,000 records per page of a job, in a file that stays available for one day. It costs 50 credits to start, and download requests are limited to 10 a minute.</li>
</ul>
<p>For a nightly export of a large module, one Bulk Read job is far cheaper than thousands of paged reads. For a quick lookup of a few hundred records, COQL is simpler.</p>

<h2 id="deluge-mcp">Deluge, Zoho Flow and AI assistants count too</h2>
<p>API usage is not only from outside systems. Zoho&rsquo;s limits page says integration tasks in Deluge functions use credits at the same rate as the matching API, and count toward concurrency at the organisation level, although sub-concurrency does not apply to them. The API dashboard includes them in its figures.</p>
<p>The same goes for AI. Zoho&rsquo;s MCP FAQ says calls through Zoho MCP follow the normal API limits of each app, with no separate allowance. If you connect Claude or ChatGPT to Zoho CRM, as in our <a href="/insights/zoho-mcp-claude-chatgpt/">Zoho MCP guide</a>, an assistant that loops through records spends the same credits as any other integration. Our <a href="/insights/zoho-flow-vs-deluge/">Zoho Flow vs Deluge comparison</a> covers how Flow and Deluge are metered.</p>

<h2 id="monitor">Watching usage before it becomes a problem</h2>
<ul class="checklist">
  <li><strong>API dashboard:</strong> credits used and unused for a period, the top applications and users, and usage by module and IP address. Figures refresh with about a 15-minute delay and are kept for 30 days.</li>
  <li><strong>Alerts:</strong> by default, Zoho emails the super admin at 80%, 90% and 100% of credits. Under Setup, Developer Hub, APIs and SDKs, you can set up to three thresholds between 50% and 100% and add recipients.</li>
  <li><strong>Response header:</strong> once usage passes half of the daily limit, responses include an X-API-CREDITS-REMAINING header that an integration can read.</li>
  <li><strong>More credits:</strong> a super admin on a paid, card-billed account can raise the limit from the Credits tab on the same page. Extra credits are billed monthly for what you use, up to 500,000 extra or the edition maximum, whichever is lower.</li>
</ul>

<h2 id="design">Designing an integration that stays under the limits</h2>
<ol>
  <li><strong>Batch every write.</strong> Use insert, update or upsert with up to 100 records per call.</li>
  <li><strong>Sync changes, not everything.</strong> Read only records modified since the last run instead of the whole module.</li>
  <li><strong>Use webhooks or workflow triggers</strong> to push changes out of Zoho CRM instead of polling every few minutes.</li>
  <li><strong>Queue and throttle.</strong> Keep parallel calls below your edition&rsquo;s concurrency, leaving room for users, Deluge and other apps.</li>
  <li><strong>Retry 429s with back-off</strong>, and log them, so a busy minute does not lose data.</li>
  <li><strong>Use Bulk Read and Bulk Write</strong> for migrations and nightly exports.</li>
</ol>
<p>When an integration needs high volume, retries and two-way sync, it usually belongs in custom middleware rather than in Deluge alone. Our <a href="/zoho-integrations/">Zoho integrations</a> page explains how we build and monitor them, and our <a href="/insights/deluge-script-examples/">Deluge script examples</a> show smaller automations that call external APIs.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('How many API calls can I make in Zoho CRM per day?',
         'It depends on edition and user count. Paid editions get 50,000 credits per rolling 24 hours plus 250, 500, 1,000 or 2,000 per user licence on Standard, Professional, Enterprise and Ultimate, up to an edition maximum. The Free edition gets 5,000. Most calls cost 1 credit, but some, such as convert lead or Bulk Write, cost more.'),
        ('What does a 429 error from Zoho CRM mean?',
         'Zoho returns HTTP 429 when the 24-hour credit limit is used up or when too many calls are running at once for the app. If the dashboard still shows credits, the cause is concurrency: reduce parallel calls and retry with a back-off.'),
        ('Does the Zoho CRM API limit reset at midnight?',
         'No. Zoho uses a rolling 24-hour window counted from each call, so credits come back gradually as earlier calls fall outside the window.'),
        ('Do Deluge functions use API credits?',
         'Yes. Integration tasks in Deluge use credits at the same rate as the matching API and count toward concurrency at the organisation level. Sub-concurrency limits do not apply to them.'),
        ('Can I buy more Zoho CRM API credits?',
         'Yes. A super admin on a paid, card-billed account can set extra daily credits in Setup under Developer Hub, APIs and SDKs. They are billed monthly for what is used, up to 500,000 extra or the gap to the edition maximum, whichever is lower.'),
        ('Do AI assistants connected through Zoho MCP have their own limit?',
         'No. Zoho\'s MCP FAQ says calls through Zoho MCP follow the default API limits of each app, with no separate allowance.'),
    ],
))
