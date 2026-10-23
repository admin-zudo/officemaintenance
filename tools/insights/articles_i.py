# Article content, part I (23 October 2026 run).

ARTICLES = []

# ------------------------------------------------------------------ Zoho Analytics vs Power BI
ARTICLES.append(dict(
    slug='zoho-analytics-vs-power-bi',
    title='Zoho Analytics vs Power BI: Licences, Data Sources and Fit for Zoho and Tally Users',
    seo_title='Zoho Analytics vs Power BI (2026 Comparison)',
    description='Zoho Analytics vs Microsoft Power BI compared: how each is licensed, who needs a paid seat to view a report, refresh limits, on-premise and Tally data, AI features, and which fits a business that runs on Zoho or Microsoft 365.',
    lead='Zoho Analytics and Power BI can both turn sales, stock and finance data into dashboards. The real differences are in how you pay for viewers, how data reaches the tool, and which suite the rest of your business already runs on. For many Indian manufacturers there is one more question: how to get TallyPrime data in.',
    category='Comparisons', keyword='zoho analytics vs power bi',
    published='2026-10-23', modified='2026-10-23',
    cover_alt='Zoho Analytics vs Power BI: who pays for viewers decides the bill. A four-row table compares them. Licensing: Zoho Analytics plans bundle users and rows, Power BI is licensed per user. Viewing a shared report: on Zoho Analytics viewers count as plan users or a viewer add-on, on Power BI viewers need Pro unless the content is on F64 capacity or larger. Refresh: Zoho Analytics syncs business apps 1 to 24 times a day by plan, Power BI Pro refreshes 8 times a day and Premium Per User 48. Local data: Zoho Databridge runs on Windows, macOS and Linux, the Power BI gateway on Windows. Facts: Zoho Analytics has 500+ data sources, a TallyPrime connector built on Databridge, and Power BI Desktop is free for Windows',
    caption='Both tools build good dashboards. The bill and the data path decide which one fits.',
    related=['zoho-analytics-agentic-data-foundations-2026', 'zoho-one-vs-microsoft-365', 'zoho-books-vs-tallyprime'],
    body='''
<p>Most comparisons of Zoho Analytics and Power BI end with &ldquo;Power BI for Microsoft shops, Zoho for everyone else&rdquo;. That is a fair starting point, but it skips the two things that decide the bill and the workload: who needs a paid licence just to look at a report, and how your data gets into the tool every day.</p>
<p>Every plan detail below was checked on Zoho&rsquo;s and Microsoft&rsquo;s own pages on 23 October 2026. We do not quote prices, because both change; see the official <a href="https://www.zoho.com/analytics/pricing.html" target="_blank" rel="noopener">Zoho Analytics pricing</a> and <a href="https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing" target="_blank" rel="noopener">Power BI pricing</a> pages. We build on Zoho, so read this with that in mind; we say where Power BI is the better fit.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Choose Zoho Analytics</strong> if your data lives mostly in Zoho apps or TallyPrime, you want a plan that bundles users and data rows, and you want to share dashboards with many people without a paid seat for each viewer.</li>
  <li><strong>Choose Power BI</strong> if your business runs on Microsoft 365, your analysts already work in Excel and the Power BI Desktop app, and your data sits in SQL Server, SharePoint or Azure.</li>
  <li><strong>Count viewers before you compare.</strong> With Power BI Pro, anyone who opens a shared report needs a paid licence too, unless the content sits on Fabric capacity of F64 or larger. That one rule changes the comparison more than any feature.</li>
</ul>

<h2 id="licensing">Two ways to license the same dashboard</h2>
<p><strong>Zoho Analytics</strong> sells plans that bundle a number of users and data rows. Its pricing page lists Free, Basic, Standard, Premium and Enterprise, plus a Dedicated Compute option for very large data. The Free plan covers 2 users and 10,000 rows. Paid plans start at 2 users and 0.5 million rows on Basic, 5 users and 1 million rows on Standard, 15 users and 5 million rows on Premium, and 50 users and 50 million rows on Enterprise. You can add users, rows and viewers as add-ons, and pay monthly or yearly. Paid plans have a 15-day trial.</p>
<p><strong>Power BI</strong> is licensed per user. The Free licence lets one person build reports, but Microsoft&rsquo;s pricing page says you must upgrade to Pro or Premium to share them. <strong>Pro</strong> lets you publish and share, and Microsoft notes that people consuming that content need a paid per-user licence as well. <strong>Premium Per User</strong> raises the limits. <strong>Fabric capacity</strong> is bought for the organisation; on F64 or larger, Microsoft says content consumers can view and interact without their own paid licence, while authors still need Pro. Power BI Pro is also included in Microsoft 365 E5 and Office 365 E5.</p>
<p>So a dashboard for a production manager, a plant head and ten supervisors means twelve paid seats on Power BI Pro. On Zoho Analytics those twelve count against the plan&rsquo;s users or are bought as viewers.</p>

<h2 id="at-a-glance">Zoho Analytics and Power BI at a glance</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">Zoho Analytics</th><th scope="col">Power BI</th></tr></thead>
  <tbody>
    <tr><th scope="row">How you pay</th><td>Plans that bundle users and rows; add-ons for more</td><td>Per user (Pro or Premium Per User), or Fabric capacity</td></tr>
    <tr><th scope="row">Free option</th><td>Free plan: 2 users, 10,000 rows, 5 workspaces</td><td>Free licence and the free Desktop app; no sharing</td></tr>
    <tr><th scope="row">Viewing shared reports</th><td>Counted as plan users, or bought as viewers</td><td>Paid licence per viewer, except on F64 capacity or larger</td></tr>
    <tr><th scope="row">Refresh from business apps</th><td>1 a day on Basic, 8 on Standard and Premium, 24 on Enterprise</td><td>8 a day on Pro, 48 on Premium Per User and capacity</td></tr>
    <tr><th scope="row">Data model size</th><td>Set by the plan&rsquo;s row allowance</td><td>1 GB per model on Pro, 100 GB on Premium Per User</td></tr>
    <tr><th scope="row">Data sources</th><td>500+ sources; 50+ business app connectors on Standard and above</td><td>Wide connector library, centred on Microsoft and database sources</td></tr>
    <tr><th scope="row">Local data</th><td>Zoho Databridge on Windows, macOS or Linux</td><td>On-premises data gateway, a Windows application</td></tr>
    <tr><th scope="row">Where reports are built</th><td>In the browser</td><td>Mostly in Power BI Desktop for Windows, then published</td></tr>
    <tr><th scope="row">AI</th><td>Ask Zia, automated insights, predictive analytics; an MCP server for AI agents</td><td>Advanced AI on Premium; Copilot in Fabric with capacity</td></tr>
  </tbody>
</table>
</div>

<h2 id="data-sources">Getting your data in</h2>
<p><strong>Zoho apps.</strong> Zoho Analytics has its own connectors for Zoho CRM, Zoho Books, Zoho Inventory and other Zoho apps, each with ready-made reports. The sync frequency depends on the plan: once a day on Basic, up to 8 times on Standard and Premium, and up to 24 on Enterprise. Basic is limited to any two business app connectors; Standard and above include 50+. If your CRM, accounts and stock are already in Zoho, this is the shortest path to a dashboard.</p>
<p><strong>Microsoft data.</strong> Power BI is at home with Excel, SharePoint, SQL Server and Azure. Pro refreshes a dataset up to 8 times a day, and Premium Per User and capacity up to 48. If your figures already live in Microsoft systems, Power BI is the shorter path.</p>
<p><strong>Data inside your network.</strong> Both tools need a small program on a local machine to reach a database on your own server. Zoho&rsquo;s is <strong>Zoho Databridge</strong>, which runs on Windows, macOS and Linux and pulls data from databases such as MySQL, SQL Server, Oracle and PostgreSQL on a schedule. Microsoft&rsquo;s is the <strong>on-premises data gateway</strong>, a Windows application that connects local sources to Power BI and other Microsoft cloud services. It comes in a standard mode that many users share and a personal mode for one user.</p>

<figure style="margin:2rem auto;max-width:660px">
<svg viewBox="0 0 660 230" role="img" aria-labelledby="pb-title pb-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="pb-title">How factory data reaches each tool</title>
  <desc id="pb-desc">Zoho apps connect to Zoho Analytics through built-in connectors. Local databases and TallyPrime reach Zoho Analytics through Zoho Databridge. Microsoft sources connect to Power BI directly, and local sources reach Power BI through the on-premises data gateway on Windows.</desc>
  <style>
    .pb-dot{animation:pb-move 4.5s linear infinite}
    .pb-d2{animation-delay:1.5s}.pb-d3{animation-delay:3s}
    @keyframes pb-move{0%{transform:translateX(0);opacity:0}10%{opacity:1}80%{opacity:1}100%{transform:translateX(250px);opacity:0}}
    @media (prefers-reduced-motion: reduce){.pb-dot{animation:none;opacity:0}}
  </style>
  <defs><marker id="pb-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#B45309"/></marker></defs>
  <rect x="20" y="20" width="170" height="54" rx="10" fill="#FFFBEB" stroke="#B45309" stroke-width="1.5"/>
  <text x="105" y="44" font-size="13.5" font-weight="700" fill="#1A1A2E" text-anchor="middle">Zoho CRM, Books,</text>
  <text x="105" y="62" font-size="13.5" font-weight="700" fill="#1A1A2E" text-anchor="middle">Inventory</text>
  <rect x="20" y="90" width="170" height="54" rx="10" fill="#FFFBEB" stroke="#B45309" stroke-width="1.5"/>
  <text x="105" y="114" font-size="13.5" font-weight="700" fill="#1A1A2E" text-anchor="middle">TallyPrime, SQL</text>
  <text x="105" y="132" font-size="12" fill="#4B5563" text-anchor="middle">on your own server</text>
  <rect x="20" y="160" width="170" height="54" rx="10" fill="#fff" stroke="#B45309" stroke-width="1.5"/>
  <text x="105" y="184" font-size="13.5" font-weight="700" fill="#1A1A2E" text-anchor="middle">Excel, SharePoint,</text>
  <text x="105" y="202" font-size="13.5" font-weight="700" fill="#1A1A2E" text-anchor="middle">Azure</text>
  <rect x="470" y="40" width="170" height="64" rx="12" fill="#B45309"/>
  <text x="555" y="78" font-size="15" font-weight="700" fill="#fff" text-anchor="middle">Zoho Analytics</text>
  <rect x="470" y="140" width="170" height="64" rx="12" fill="#1A1A2E"/>
  <text x="555" y="178" font-size="15" font-weight="700" fill="#fff" text-anchor="middle">Power BI</text>
  <path d="M198 47H462" stroke="#B45309" stroke-width="2" marker-end="url(#pb-a)"/>
  <text x="330" y="40" font-size="11.5" fill="#4B5563" text-anchor="middle">built-in connectors</text>
  <path d="M198 112C300 112 360 86 462 82" stroke="#B45309" stroke-width="2" fill="none" marker-end="url(#pb-a)"/>
  <text x="300" y="98" font-size="11.5" fill="#4B5563" text-anchor="middle">Databridge</text>
  <path d="M198 124C300 124 360 160 462 166" stroke="#1A1A2E" stroke-width="2" stroke-dasharray="6 5" fill="none" marker-end="url(#pb-a)"/>
  <text x="262" y="152" font-size="11.5" fill="#4B5563" text-anchor="middle">gateway (Windows)</text>
  <path d="M198 187H462" stroke="#1A1A2E" stroke-width="2" marker-end="url(#pb-a)"/>
  <text x="330" y="207" font-size="11.5" fill="#4B5563" text-anchor="middle">native connectors</text>
  <circle class="pb-dot" cx="206" cy="47" r="5" fill="#F59E0B"/>
  <circle class="pb-dot pb-d2" cx="206" cy="47" r="5" fill="#F59E0B"/>
  <circle class="pb-dot pb-d3" cx="206" cy="187" r="5" fill="#F59E0B"/>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">Each tool has a short path for its own suite and a local agent for data on your server. Pick the tool whose short path matches where most of your data already is.</figcaption>
</figure>

<h2 id="tally">TallyPrime data, for Indian businesses</h2>
<p>Many Indian manufacturers and traders keep their accounts in TallyPrime even after they move sales or stock to the cloud. Zoho Analytics has a documented <strong>TallyPrime connector</strong> built on Zoho Databridge. You enable ODBC in TallyPrime, install Databridge (version 10.9.8 or later) on the Tally machine or a local server that can reach it, and choose what to sync: ledgers, godowns, stock items, vouchers and the trial balance, plus reports such as the balance sheet, profit and loss, stock summary and the sales and purchase registers. Data syncs every 3, 6 or 12 hours or daily, and every hour on Enterprise.</p>
<p>We could not find a Microsoft-built TallyPrime connector for Power BI. Teams that use the two together go through Tally&rsquo;s ODBC interface, scheduled exports, or a third-party connector sold separately, refreshed through the gateway. That works, but someone has to build, pay for and look after it. If you are still deciding whether Tally stays, our <a href="/insights/zoho-books-vs-tallyprime/">Zoho Books vs TallyPrime guide</a> covers that first.</p>

<h2 id="building">Building reports: browser or desktop</h2>
<p>Zoho Analytics is built and used in the browser, with native mobile apps. A sales manager can drag fields into a chart or ask a question of the data in plain English with <strong>Ask Zia</strong>.</p>
<p>Power BI reports are mostly built in <strong>Power BI Desktop</strong>, a free Windows application (Windows 10 or Windows Server 2016 or later, according to Microsoft&rsquo;s download page), and then published to the Power BI service. Desktop is where Power BI is strongest: its modelling and DAX formulas give an analyst fine control over complex calculations. So report authors need a Windows machine.</p>

<h2 id="ai">AI features</h2>
<p>Zoho lists Ask Zia, automated and diagnostic insights, predictive analytics, what-if analysis and anomaly detection on its pricing page, and offers an <strong>MCP server</strong> so AI agents and assistants can work with Zoho Analytics data.</p>
<p>Microsoft&rsquo;s pricing page lists advanced AI with Premium Per User and capacity, and Copilot in Fabric with capacity. Check which licence each AI feature needs before you count on it.</p>
<p>On either tool, define your key measures once and check AI answers against a trusted report; our guide to <a href="/insights/zoho-analytics-agentic-data-foundations-2026/">data foundations in Zoho Analytics</a> shows how.</p>

<h2 id="manufacturers">What a manufacturer should test</h2>
<p>For a factory, the useful first dashboards are usually plain: orders due this week against production, stock below reorder level, rejection and rework by product, and receivables by customer. Our guide to <a href="/manufacturing/guides/manufacturing-dashboards-kpis/">manufacturing dashboards and KPIs</a> lists what to measure first. In either trial, build one of these on your own data and check three things: how fresh the figures are when the shift supervisor opens it, how many people need a licence to see it, and who will fix it when a source changes.</p>

<h2 id="who-fits">Which one fits your business</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Your situation</th><th scope="col">Usually the better fit</th></tr></thead>
  <tbody>
    <tr><th scope="row">CRM, accounts and stock run on Zoho apps or Zoho One</th><td>Zoho Analytics</td></tr>
    <tr><th scope="row">Accounts in TallyPrime, and you want scheduled dashboards</th><td>Zoho Analytics</td></tr>
    <tr><th scope="row">Many people view dashboards, few people build them</th><td>Zoho Analytics, or Power BI on F64 capacity</td></tr>
    <tr><th scope="row">You are on Microsoft 365 E5, which includes Power BI Pro</th><td>Power BI</td></tr>
    <tr><th scope="row">Data in SQL Server, SharePoint or Azure, and analysts who know DAX</th><td>Power BI</td></tr>
    <tr><th scope="row">Report authors work on Macs</th><td>Zoho Analytics</td></tr>
  </tbody>
</table>
</div>
<p>Running both suites side by side is common. Our comparison of <a href="/insights/zoho-one-vs-microsoft-365/">Zoho One vs Microsoft 365</a> covers how the wider suites fit together, and Zoho Analytics is one of the apps included in Zoho One.</p>

<h2 id="trial-plan">A trial plan for both</h2>
<ul class="checklist">
  <li>Count the people who will build reports and the people who will only view them.</li>
  <li>List every data source, and mark which ones sit on your own server.</li>
  <li>Connect your two most important sources and note how often each refreshes on the plan you would buy.</li>
  <li>Rebuild one report you use every week, and have the person who reads it check the numbers.</li>
  <li>Share it with a viewer who has no licence yet, and see what they need.</li>
</ul>
<p>If you choose Zoho Analytics and need help connecting Tally, a factory database or a custom app, our <a href="/zoho-integrations/">Zoho integrations</a> page explains how we work.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Is Zoho Analytics cheaper than Power BI?',
         'It depends on how many people view reports. Power BI Pro is licensed per user, and people who view shared content also need a paid licence unless it sits on Fabric capacity of F64 or larger. Zoho Analytics plans bundle a set number of users and rows. Count your builders and viewers, then compare both official pricing pages.'),
        ('Do Power BI viewers need a licence?',
         'With Pro or Premium Per User, yes: Microsoft says people consuming shared content need a paid per-user licence. On Fabric capacity of F64 or larger, content consumers can view and interact without their own paid licence, while report authors still need Pro.'),
        ('Can Zoho Analytics connect to TallyPrime?',
         'Yes. Zoho Analytics has a TallyPrime connector built on Zoho Databridge, installed on the Tally machine or a local server. It syncs ledgers, stock items, vouchers and reports such as the balance sheet and stock summary every 3, 6 or 12 hours or daily, and hourly on the Enterprise plan.'),
        ('Can I use Power BI with Zoho CRM data?',
         'Yes, but it takes more work than using Zoho Analytics, which has a built-in Zoho CRM connector. With Power BI you would typically pull data through the Zoho CRM API, an export, or a third-party connector, and someone needs to maintain that link.'),
        ('Does Power BI work on a Mac?',
         'The Power BI service runs in a browser, so viewing reports works on any computer. Power BI Desktop, where most reports are built, is a Windows application; Microsoft\'s download page lists Windows 10 or Windows Server 2016 or later.'),
        ('Is Zoho Analytics included in Zoho One?',
         'Yes. Zoho Analytics is one of the apps listed in Zoho One. Check the plan details for the user and row allowances that come with your Zoho One subscription before you plan large data volumes around it.'),
    ],
))

# ------------------------------------------------------------------ Preventive maintenance: Zoho or a CMMS
ARTICLES.append(dict(
    slug='zoho-preventive-maintenance-vs-cmms',
    title='Preventive Maintenance on Zoho or a CMMS? Zoho Creator, Zoho FSM, MaintainX and Fiix Compared',
    seo_title='Zoho for Preventive Maintenance vs a CMMS',
    description='How a manufacturer can run machine maintenance on Zoho: a Zoho Creator maintenance app, Zoho FSM for servicing customers’ equipment, or a dedicated CMMS such as MaintainX or Fiix, with what each plan includes and when to choose which.',
    lead='Zoho has no product called a CMMS, yet many manufacturers run machine maintenance on Zoho. The question is not whether it can be done, but whether a maintenance app built around your Zoho data beats a ready-made CMMS that your maintenance team can start using next week.',
    category='Manufacturing', keyword='zoho preventive maintenance',
    published='2026-10-23', modified='2026-10-23',
    cover_alt='Preventive maintenance: Zoho or a CMMS? Three routes in numbered rows. One, a Zoho Creator app for your own plant, tied to Zoho stock and production and built to your own process. Two, Zoho FSM for machines you service at customer sites, where maintenance plans raise work orders. Three, a CMMS such as MaintainX or Fiix, ready-made software you can start this month, with parts and API features on higher tiers. Facts: Creator apps accept offline entry and sync later, Zoho FSM plans run daily to yearly, and the Fiix Free plan allows 25 active PMs. Beside them a factory worker figure with the takeaway: decide first where spare parts and machine history will live',
    caption='All three routes can schedule preventive work. They differ in where machine history and spare parts live.',
    related=['zoho-for-manufacturing', 'zoho-erp-vs-odoo-manufacturing', 'zoho-flow-vs-deluge'],
    body='''
<p>Ask a maintenance head what they need and the list is short: every machine in one register, preventive jobs that raise themselves on time, a quick way for an operator to report a breakdown, spare parts that are actually in the store, and a history that shows which machine keeps failing. A spreadsheet and a WhatsApp group can do some of this. None of it scales.</p>
<p>There are three sensible routes for a manufacturer that already uses Zoho or is considering it. Every product detail below was checked on Zoho&rsquo;s, MaintainX&rsquo;s and Fiix&rsquo;s own pages on 23 October 2026. We do not quote prices; see each vendor&rsquo;s pricing page.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Build a Zoho Creator app</strong> if you want maintenance tied to the stock, purchasing and production data you already keep in Zoho, and your process does not fit a standard CMMS.</li>
  <li><strong>Use Zoho FSM</strong> if the machines you maintain sit at your customers&rsquo; sites, for example if you sell and service equipment.</li>
  <li><strong>Buy a CMMS such as MaintainX or Fiix</strong> if you want proven maintenance software running within weeks, and you are happy to connect it to Zoho rather than run it inside Zoho.</li>
</ul>

<h2 id="what-zoho-offers">What Zoho offers for maintenance</h2>
<p>Zoho ERP and Zoho Inventory handle stock, purchasing and production, but neither lists a maintenance module among its features. Zoho covers maintenance in three other ways.</p>
<p><strong>Zoho Creator</strong> is Zoho&rsquo;s low-code platform. Zoho publishes a computerised maintenance management use case for it with six areas: a central database, work orders that run from request to completion with checklists, manuals and photos attached, an asset register with make, model, serial number, location, purchase date, cost and warranty, preventive schedules, spare parts inventory with bin locations, low-stock alerts and reordering, and a compliance area with an audit trail and safety checklists. Its schedules can be set by time interval, by meter reading (Zoho&rsquo;s example is every 500 hours of running), or by a condition. Zoho also offers a facility maintenance app template that you install and change to suit you.</p>
<p><strong>Zoho FSM</strong> (Field Service Management) is built for servicing equipment at customer sites. Its scheduled maintenance feature runs daily, weekly, monthly or yearly plans that create work orders and service appointments automatically, from templates that carry the customer, the asset and the parts needed, and sends them to the Dispatch Console.</p>
<p><strong>Zoho IoT</strong> is a separate platform for machine data. Zoho&rsquo;s manufacturing page describes machine monitoring for uptime, cycle time and OEE, AI-based models for predictive maintenance, and support for Modbus, MQTT, OPC-UA, HTTP and LoRaWAN.</p>

<figure style="margin:2rem auto;max-width:660px">
<svg viewBox="0 0 660 250" role="img" aria-labelledby="pm-title pm-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="pm-title">The preventive maintenance cycle</title>
  <desc id="pm-desc">A schedule falls due by date or by running hours and raises a work order. A technician does the job on a phone, scanning the machine tag and using spare parts. Parts used reduce stock, and the closed job adds to the machine's history, which sets the next schedule.</desc>
  <style>
    .pm-run{animation:pm-glow 6s ease-in-out infinite}
    .pm-s2{animation-delay:1.5s}.pm-s3{animation-delay:3s}.pm-s4{animation-delay:4.5s}
    @keyframes pm-glow{0%,30%,100%{fill:#fff}8%,22%{fill:#E0E7FF}}
    @media (prefers-reduced-motion: reduce){.pm-run{animation:none}}
  </style>
  <defs><marker id="pm-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#1E3A8A"/></marker></defs>
  <rect class="pm-run" x="20" y="30" width="190" height="76" rx="12" fill="#fff" stroke="#1E3A8A" stroke-width="2"/>
  <text x="115" y="62" font-size="15" font-weight="700" fill="#1E3A8A" text-anchor="middle">1. Schedule due</text>
  <text x="115" y="86" font-size="12.5" fill="#4B5563" text-anchor="middle">by date or running hours</text>
  <rect class="pm-run pm-s2" x="450" y="30" width="190" height="76" rx="12" fill="#fff" stroke="#1E3A8A" stroke-width="2"/>
  <text x="545" y="62" font-size="15" font-weight="700" fill="#1E3A8A" text-anchor="middle">2. Work order</text>
  <text x="545" y="86" font-size="12.5" fill="#4B5563" text-anchor="middle">checklist, assigned</text>
  <rect class="pm-run pm-s3" x="450" y="150" width="190" height="76" rx="12" fill="#fff" stroke="#1E3A8A" stroke-width="2"/>
  <text x="545" y="182" font-size="15" font-weight="700" fill="#1E3A8A" text-anchor="middle">3. Job on a phone</text>
  <text x="545" y="206" font-size="12.5" fill="#4B5563" text-anchor="middle">scan tag, use parts</text>
  <rect class="pm-run pm-s4" x="20" y="150" width="190" height="76" rx="12" fill="#fff" stroke="#1E3A8A" stroke-width="2"/>
  <text x="115" y="182" font-size="15" font-weight="700" fill="#1E3A8A" text-anchor="middle">4. History and stock</text>
  <text x="115" y="206" font-size="12.5" fill="#4B5563" text-anchor="middle">parts used, next due date</text>
  <path d="M218 68H442" stroke="#1E3A8A" stroke-width="2.5" marker-end="url(#pm-a)"/>
  <path d="M545 114V142" stroke="#1E3A8A" stroke-width="2.5" marker-end="url(#pm-a)"/>
  <path d="M442 188H218" stroke="#1E3A8A" stroke-width="2.5" marker-end="url(#pm-a)"/>
  <path d="M115 142V114" stroke="#1E3A8A" stroke-width="2.5" marker-end="url(#pm-a)"/>
  <text x="330" y="132" font-size="13" fill="#4B5563" text-anchor="middle">Every route below runs this same loop.</text>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">The loop is the same in a Creator app, Zoho FSM or a CMMS. What changes is where the parts stock and the machine history are kept.</figcaption>
</figure>

<h2 id="what-a-cmms-offers">What a dedicated CMMS offers</h2>
<p>A CMMS (computerised maintenance management system) is software built only for maintenance teams. MaintainX and Fiix are two examples, and both publish their plans openly.</p>
<ul>
  <li><strong>MaintainX</strong> has a free Basic plan with unlimited work orders, procedures and requester users, but only a few work orders with procedures attached, a small number of repeating work orders, and no API, meter-based maintenance or parts inventory. Its paid Essential and Premium plans are billed per user; Premium adds meter-based maintenance, parts inventory, purchase orders, time and cost tracking, work orders for outside contractors and REST API access. Enterprise adds IoT sensor integrations, single sign-on, multi-site management and an AI assistant. Requester accounts are free on every plan.</li>
  <li><strong>Fiix</strong> has a Free plan with 25 active preventive maintenance schedules and unlimited work orders, assets and parts, but no integrations. Basic adds unlimited schedules, standard reports and pass/fail inspections. Professional adds multi-site management, purchasing and RFQs, advanced analytics and Fiix&rsquo;s AI features. Enterprise adds failure codes, condition-based triggers, an audit trail and e-signature, and Fiix&rsquo;s Integration Hub, with ERP and custom API integrations at extra cost. Plans can be month-to-month or annual.</li>
</ul>
<p>Two things stand out. First, both put the features a factory needs most, such as parts inventory, purchasing, meter-based schedules and integrations, in the higher tiers. Second, a CMMS keeps its own parts store and purchasing, separate from the stock and purchase orders in your ERP, unless you connect them.</p>

<h2 id="comparison">The three routes side by side</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">Zoho Creator app</th><th scope="col">Zoho FSM</th><th scope="col">CMMS (MaintainX, Fiix)</th></tr></thead>
  <tbody>
    <tr><th scope="row">Built for</th><td>Your own plant, your own process</td><td>Equipment at customer sites</td><td>In-house maintenance teams</td></tr>
    <tr><th scope="row">Time to start</th><td>Weeks, to build and test</td><td>Days to weeks, to configure</td><td>Days, to set up assets and schedules</td></tr>
    <tr><th scope="row">Preventive schedules</th><td>By time, meter reading or condition, as you design them</td><td>Daily, weekly, monthly or yearly plans</td><td>Built in; meter-based on higher tiers</td></tr>
    <tr><th scope="row">Spare parts</th><td>In the app, or linked to Zoho Inventory or Zoho ERP stock</td><td>Parts listed on work order templates</td><td>Own parts store; on higher tiers</td></tr>
    <tr><th scope="row">Mobile and offline</th><td>Native iOS and Android apps; offline entry that syncs later; QR and barcode scanning</td><td>Android and iOS app for field agents</td><td>Mobile apps</td></tr>
    <tr><th scope="row">Link to Zoho data</th><td>Native</td><td>Native, within Zoho</td><td>Through an API or a connector</td></tr>
    <tr><th scope="row">Who maintains it</th><td>You or your Creator developer</td><td>The vendor, plus your configuration</td><td>The vendor</td></tr>
  </tbody>
</table>
</div>

<h2 id="when-creator">When a Zoho Creator app is the better choice</h2>
<p>Choose Creator when maintenance has to work with the rest of your Zoho data, not beside it. Typical signs:</p>
<ul>
  <li>Spare parts are bought and stocked in Zoho Inventory or Zoho ERP, and you do not want a second parts store to reconcile.</li>
  <li>A stopped machine should put the jobs planned on it on hold, so production and maintenance see the same status.</li>
  <li>Your checks are unusual: a pharmaceutical line clearance, a mould&rsquo;s shot count, or a customer audit format you must follow.</li>
  <li>Operators and technicians already use Zoho apps, and you want one login.</li>
</ul>
<p>Creator apps run natively on iOS and Android, accept data offline and sync it when the phone reconnects, and can scan QR codes and barcodes, so a technician can scan a machine tag and see its history. Creator is licensed per user, for every person who uses the app; see the <a href="https://www.zoho.com/creator/pricing.html" target="_blank" rel="noopener">Creator pricing page</a> for plans. Our <a href="/manufacturing/workflows/#wf-maintenance">maintenance request workflow</a> shows the scan-and-tap steps we design for the shop floor, and our <a href="/zoho-creator-development/">Zoho Creator development</a> page explains how we build them.</p>
<p>The cost of this route is ownership. Someone has to build the app, test it with the people who will use it, and keep it working as the plant changes.</p>

<h2 id="when-fsm">When Zoho FSM is the better choice</h2>
<p>If you make machines and also service them, your preventive work happens at customers&rsquo; sites. That is a field service problem: scheduling visits, dispatching technicians and recording what was done for each customer&rsquo;s asset. Zoho FSM&rsquo;s scheduled maintenance plans create those work orders and appointments automatically. Your own factory&rsquo;s machines are a different job and are better served by one of the other two routes.</p>

<h2 id="when-cmms">When a dedicated CMMS is the better choice</h2>
<ul>
  <li>You have a maintenance team that wants a proven tool now, not a project.</li>
  <li>You run several sites and want multi-site reporting without building it.</li>
  <li>You plan to add sensor data, and the CMMS tier you are buying supports it.</li>
  <li>Maintenance is largely separate from production planning and stock in your business.</li>
</ul>
<p>If you go this way, decide early which system owns spare parts and purchase orders. The usual pattern is that the CMMS raises a parts request and your ERP raises the purchase order, connected through the CMMS&rsquo;s API; check which tier includes that API before you buy. Our guide to <a href="/insights/zoho-flow-vs-deluge/">Zoho Flow, Deluge and custom middleware</a> covers how such a link is built.</p>

<h2 id="decide">Five questions to decide</h2>
<ol>
  <li><strong>Where are the machines?</strong> In your plant, or at customers&rsquo; sites?</li>
  <li><strong>Where do spare parts live?</strong> In your Zoho stock, or in a separate store the maintenance team runs?</li>
  <li><strong>How standard is your process?</strong> Would a CMMS fit it on day one?</li>
  <li><strong>How soon must it run?</strong> This month, or this quarter?</li>
  <li><strong>Who will own it</strong> in two years: a vendor, or you?</li>
</ol>
<p>If you are still choosing your core system, start with our overview of <a href="/insights/zoho-for-manufacturing/">every Zoho route for manufacturers</a>; our <a href="/insights/zoho-erp-vs-odoo-manufacturing/">Zoho ERP vs Odoo comparison</a> covers the case where you want maintenance inside the ERP itself, which Odoo offers and Zoho ERP does not.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Does Zoho have a CMMS?',
         'Not as a separate product. Zoho publishes a CMMS use case and a facility maintenance template for Zoho Creator, which you install and adapt, and Zoho FSM has scheduled maintenance for servicing equipment at customer sites. Zoho ERP and Zoho Inventory do not list a maintenance module.'),
        ('Can Zoho Creator schedule preventive maintenance by running hours?',
         'Yes, if you build it that way. Zoho\'s CMMS use case for Creator describes schedules by time interval, by meter reading, with the example of every 500 hours of running, and by condition. The meter readings have to be entered by a person or sent from a machine.'),
        ('Is MaintainX free?',
         'MaintainX has a free Basic plan with unlimited work orders and requester users, but it limits work orders with procedures attached and repeating work orders, and leaves out the API, meter-based maintenance and parts inventory. Those come with the paid plans, mostly Premium and above.'),
        ('Can a CMMS like MaintainX or Fiix connect to Zoho?',
         'Yes, through their APIs or a connector, but check the plan. MaintainX lists REST API access on Premium and above, and Fiix lists ERP and custom API integrations on Enterprise, some at extra cost. Decide which system owns spare parts and purchase orders before you build the link.'),
        ('What is the difference between Zoho FSM and a CMMS?',
         'Zoho FSM is field service software: it schedules and dispatches technicians to equipment at customer sites. A CMMS is built for a maintenance team looking after its own plant and machines. A manufacturer that services machines it has sold may need FSM; one that maintains its own production line needs a CMMS or a Creator app.'),
    ],
))
