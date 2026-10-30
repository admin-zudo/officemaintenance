# Article content, part E (14 October 2026 run).

ARTICLES = []

# ------------------------------------------------------------------ Airtable vs Zoho Tables vs Zoho Creator
ARTICLES.append(dict(
    slug='zoho-creator-vs-airtable',
    title='Zoho Creator vs Airtable (and Zoho Tables): Which One Fits Your Business?',
    seo_title='Zoho Creator vs Airtable (2026 Comparison)',
    description='Airtable, Zoho Tables and Zoho Creator compared: what each is built for, record limits, who you pay for, logic, external users, mobile and AI, plus Airtable\'s change of ownership and when to move from a shared database to a business app.',
    lead='Most &ldquo;Zoho Creator vs Airtable&rdquo; pages compare two products that are not quite the same kind of thing. Airtable&rsquo;s closest Zoho match is Zoho Tables. Zoho Creator is what you move to when a shared database has to become a business app. This guide compares all three, fairly.',
    category='Comparisons', keyword='zoho creator vs airtable',
    published='2026-10-14', modified='2026-10-30',
    cover_alt='Airtable, Zoho Tables and Zoho Creator compared in a table: what each is built for, record limits, logic, outside users and whether it is in Zoho One',
    caption='Two shared databases and one app platform. The right choice depends on who uses the data, not on how the grid looks.',
    related=['zoho-creator-vs-power-apps', 'deluge-script-examples', 'zoho-mcp-claude-chatgpt'],
    body='''
<p>Airtable made the spreadsheet-database popular: a grid that looks familiar, with linked records, views and automations behind it. Zoho offers two answers to it. <strong>Zoho Tables</strong> is the like-for-like product. <strong>Zoho Creator</strong> is a low-code platform for building complete business applications, with its own scripting language, mobile apps and portals.</p>
<p>Every plan, limit and feature below was checked on Airtable&rsquo;s and Zoho&rsquo;s own pricing pages and help articles on 14 October 2026 and re-checked on 30 October 2026. We do not quote prices, because they change and vary by country; follow the links to the official pricing pages for those.</p>

<h2 id="what-each-is">What each product is built for</h2>
<ul>
  <li><strong>Airtable</strong> organises data in bases made of linked tables, with views, automations, Interface Designer for simple app screens, and AI features such as Omni, a conversational builder that creates tables, interfaces and automations from a description. Its strength is speed: a team can model its data in an afternoon.</li>
  <li><strong>Zoho Tables</strong> is Zoho&rsquo;s collaborative database. It offers Grid, Kanban, Gallery, Calendar and Form views, linked records, automations, mobile apps for Android and iOS, and AI field types such as sentiment analysis and keyword extraction. It sits in the same category as Airtable.</li>
  <li><strong>Zoho Creator</strong> is an application platform. You build forms, reports and pages on its database, add logic in Deluge, run processes with workflows and Blueprints, and publish native iOS and Android apps and customer or supplier portals. Zoho now describes it as an AI app builder, with agents that turn a description into requirements and then into an app.</li>
</ul>
<p>So the real question is usually not &ldquo;Airtable or Creator?&rdquo; but &ldquo;do we need a shared database, or an application?&rdquo;</p>

<h2 id="at-a-glance">The three at a glance</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">Airtable</th><th scope="col">Zoho Tables</th><th scope="col">Zoho Creator</th></tr></thead>
  <tbody>
    <tr><th scope="row">Built for</th><td>Team databases and light apps</td><td>Team databases</td><td>Business applications</td></tr>
    <tr><th scope="row">Plans</th><td>Free, Team, Business, Enterprise Scale</td><td>Free, Professional</td><td>Free, Standard, Professional, Enterprise, Flex</td></tr>
    <tr><th scope="row">Who you pay for</th><td>Collaborators who can edit (commenters too on Team); read-only users are free</td><td>Users; Professional starts from 3 licences, with unlimited viewers</td><td>Users</td></tr>
    <tr><th scope="row">Record limit</th><td>Per base: 1,000 Free, 50,000 Team, 125,000 Business</td><td>Per base: 5,000 Free, 50,000 Professional</td><td>5,000 Free; then 25,000, 100,000 or 250,000 per user</td></tr>
    <tr><th scope="row">Logic</th><td>Automations and scripts</td><td>Automations and scheduled automations</td><td>Deluge scripts, workflows, Blueprints</td></tr>
    <tr><th scope="row">Outside users</th><td>Portals add-on, sold in seat packs</td><td>View-only users (unlimited on Professional) and forms</td><td>Portals: 3 users free, more as an add-on</td></tr>
    <tr><th scope="row">Mobile</th><td>iOS and Android apps</td><td>iOS and Android apps</td><td>Native iOS and Android apps for each app you build</td></tr>
    <tr><th scope="row">In Zoho One?</th><td>No</td><td>Yes, Professional</td><td>Yes</td></tr>
  </tbody>
</table>
</div>
<p>Confirm current limits on the official pages: <a href="https://airtable.com/pricing" target="_blank" rel="noopener">Airtable pricing</a>, <a href="https://www.zoho.com/tables/pricing.html" target="_blank" rel="noopener">Zoho Tables pricing</a> and the <a href="https://www.zoho.com/creator/pricing-comparison.html" target="_blank" rel="noopener">Zoho Creator plan comparison</a>.</p>

<h2 id="who-you-pay-for">Who you pay for: the difference most comparisons miss</h2>
<p>The three products count users differently, and that often decides the total cost more than the price per seat.</p>
<ul>
  <li><strong>Airtable charges per seat for people who change data.</strong> On Team, anyone with commenter access or higher is billable; on Business, Airtable lists owners, creators and editors as billable. Read-only collaborators, form submissions and share links are not charged on paid plans. A base that ten people edit and fifty people only read costs ten seats.</li>
  <li><strong>Zoho Tables</strong> charges per user, and its Professional plan includes unlimited view-only users. If your company already pays for Zoho One, Tables Professional is included.</li>
  <li><strong>Zoho Creator charges per user,</strong> and its record and storage allowances grow with the number of users. External users such as customers or suppliers are portal users instead: three are free, and more are bought as an add-on.</li>
</ul>
<p>Model the cost on your real user list: who edits, who only reads, and who sits outside the company.</p>

<h2 id="limits">Limits that shape the design</h2>
<p>Airtable and Zoho Tables set limits <em>per base</em>. On Airtable that is 50,000 records on Team and 125,000 on Business; on Zoho Tables it is 50,000 on Professional. That is plenty for a project tracker or a content calendar. It becomes a design constraint for transaction data such as orders, production logs or inspection results, which grow every day and never shrink.</p>
<p>Zoho Creator sets limits <em>per user</em> across the account: 25,000 records per user on Standard, 100,000 on Professional and 250,000 on Enterprise. Note that Standard allows one app, while Professional and Enterprise allow unlimited apps.</p>
<p>Other limits worth checking before you build: Airtable allows 75, 100 or 150 unique automations per base on Free, Team and Business, and 1,000 API calls a month per workspace on Free and 100,000 on Team. Zoho Tables allows 3 active automations per base on Free and 25 on Professional. Creator publishes its limits for Deluge statements, external calls and API calls per user per day on its comparison page.</p>

<h2 id="logic">Logic, processes and integrations</h2>
<p>For simple rules, all three work: when a record changes, notify someone or update a field. The difference shows when the process has stages, owners and rules about who may do what.</p>
<p>Creator was built for that. Deluge runs at exact points, such as when a form is submitted or a field changes; Blueprints enforce the stages of a process; and calls to other systems are part of the language. If Zoho CRM, Zoho Books or Zoho Inventory already hold your customers and orders, a Creator app works with the same records instead of syncing a copy. Our <a href="/insights/deluge-script-examples/">Deluge script examples</a> show the kind of logic involved.</p>
<p>Airtable&rsquo;s automations and scripting go a long way, and it has a large catalogue of integrations. It is at its best when the data and the people working on it sit in one team.</p>

<h2 id="external-users">Customers, suppliers and the shop floor</h2>
<p>Letting people outside the company in is where the products differ most.</p>
<ul>
  <li><strong>Airtable Portals</strong> is an add-on for Team, Business and Enterprise Scale. Seats come in packs starting at 15; a guest with editor access counts as a portal seat, while read-only guests do not. There can be one portal per base, sharing any number of its interfaces.</li>
  <li><strong>Zoho Creator</strong> includes portals in its plans, with three portal users free and more as an add-on, and per-app permission sets for what each type of user can see and do.</li>
</ul>
<p>On phones, Airtable&rsquo;s iOS and Android apps run its interfaces, though Airtable notes that interface pages cannot be opened in mobile browsers and that the apps may slow down with tens of thousands of records. Creator publishes each app you build as a native mobile app, which suits people who record work away from a desk.</p>

<h2 id="ai">AI and MCP</h2>
<p>Both vendors are moving fast here. Airtable offers Omni, now in its 2.0 version on all plans, and Field Agents, which act as researchers or content creators across records, with a monthly allowance of AI credits in each plan. Its MCP server lets assistants such as Claude, ChatGPT and Gemini work with Airtable data, and admins can switch it off, approve tools and limit them to chosen bases. Zoho Creator offers Zia, agents that plan, build and test an app from a description, a choice of Zoho&rsquo;s own models or your own key for OpenAI, Google or Anthropic models, and access from AI assistants through MCP.</p>
<p>Zoho MCP lists both Creator and Tables among the Zoho services an assistant such as Claude or ChatGPT can use; our <a href="/insights/zoho-mcp-claude-chatgpt/">Zoho MCP guide</a> explains the setup and which actions to allow.</p>

<h2 id="airtable-ownership">Airtable&rsquo;s change of ownership</h2>
<p>Airtable was acquired by Bending Spoons, and its newsroom says the deal closed in early September 2026. In a post on 12 October 2026, Airtable said that plans, prices and service offerings are unchanged, and announced an upgraded Omni assistant, Airtable Canvas for custom apps, a more powerful MCP and options to bring your own agents and keys.</p>
<p>Some of that has since shipped. Airtable&rsquo;s Fall 2026 release made Omni 2.0 and the upgraded MCP generally available, and added audit logs that show whether a person or an agent made each change. Canvas, for building apps, dashboards and presentations, is moving to an open beta; Airtable says it needs AI and Anthropic enabled as an AI provider across the organisation, and is not yet available to HIPAA or non-US data residency customers. Bringing your own agents and keys, and field- and record-level permissions for agents, are listed as coming soon. The release announced no price changes.</p>
<p>For a current customer this is a reason to watch the roadmap, not to move. For a new project it is one more question to ask any vendor: what happens to your data and pricing if the company changes hands.</p>

<h2 id="example">An example: replacing a production tracker spreadsheet</h2>
<p>Take a small manufacturer whose production planner keeps jobs in a shared spreadsheet. This is an illustration, not a client project.</p>
<figure style="margin:2rem auto;max-width:620px">
<svg viewBox="0 0 600 220" role="img" aria-labelledby="ca-title ca-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="ca-title">From a spreadsheet to a shared database to a business app</title>
  <desc id="ca-desc">Three stages from left to right. Spreadsheet: one file, one owner. Shared database, Airtable or Zoho Tables: linked records, views, one team. Business app, Zoho Creator: roles, stages, mobile and portals.</desc>
  <style>
    .ca-dot{animation:ca-move 7s ease-in-out infinite}
    @keyframes ca-move{0%{transform:translateX(0);opacity:0}8%{opacity:1}92%{opacity:1}100%{transform:translateX(400px);opacity:0}}
    @media (prefers-reduced-motion: reduce){.ca-dot{animation:none;opacity:0}}
  </style>
  <line x1="100" y1="50" x2="500" y2="50" stroke="#C9DCEF" stroke-width="4" stroke-linecap="round"/>
  <circle cx="100" cy="50" r="16" fill="#fff" stroke="#9AA4B2" stroke-width="4"/>
  <circle cx="300" cy="50" r="16" fill="#fff" stroke="#226DB4" stroke-width="4"/>
  <circle cx="500" cy="50" r="16" fill="#226DB4" stroke="#226DB4" stroke-width="4"/>
  <circle class="ca-dot" cx="100" cy="50" r="7" fill="#226DB4"/>
  <g font-size="19" font-weight="700" fill="#1A1A2E" text-anchor="middle">
    <text x="100" y="104">Spreadsheet</text><text x="300" y="104">Shared database</text><text x="500" y="104">Business app</text>
  </g>
  <g font-size="15" fill="#4B5563" text-anchor="middle">
    <text x="100" y="132">One file, one owner</text>
    <text x="300" y="132">Airtable or Zoho Tables</text><text x="300" y="154">Linked records, one team</text>
    <text x="500" y="132">Zoho Creator</text><text x="500" y="154">Roles, stages, mobile,</text><text x="500" y="176">portals</text>
  </g>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">Most teams do not need the last step. Move only when people outside the team need to work in the data.</figcaption>
</figure>
<ul>
  <li><strong>If only the office uses it,</strong> Airtable or Zoho Tables is enough. Jobs, customers and materials become linked tables, the planner gets a Kanban view by stage and a calendar of due dates, and an automation reminds the owner of a late job. Choose Zoho Tables if the company already uses Zoho One, Airtable if the team already knows it.</li>
  <li><strong>If operators must record work on the floor,</strong> customers want to see order status, and finished jobs should create invoices in Zoho Books, it has become an application. A Creator app gives operators a phone screen that shows only their jobs, gives customers a portal limited to their own orders, and passes completed jobs to accounts. Our guide to <a href="/manufacturing/guides/production-tracking-zoho-creator/">production tracking in Zoho Creator</a> covers that build in detail.</li>
</ul>

<h2 id="how-to-choose">How to choose</h2>
<ol>
  <li><strong>Choose Airtable</strong> if a team needs a flexible database quickly, most viewers only read, and your other systems are not Zoho.</li>
  <li><strong>Choose Zoho Tables</strong> if you want the same kind of tool and already pay for Zoho One, or want your data in the same account as your other Zoho apps.</li>
  <li><strong>Choose Zoho Creator</strong> if the data drives a process with stages and owners, people outside the office or the company must use it, or it has to work with Zoho CRM, Books or Inventory records directly.</li>
</ol>
<p>If you are also weighing Microsoft&rsquo;s platform, read our <a href="/insights/zoho-creator-vs-power-apps/">Zoho Creator vs Power Apps comparison</a>; for an operations platform priced by plan minimums and reads, see <a href="/insights/zoho-creator-vs-quickbase/">Zoho Creator vs Quickbase</a>. When an app is clearly needed, our <a href="/zoho-creator-development/">Zoho Creator development</a> page explains how we scope it.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Is Zoho Creator an alternative to Airtable?',
         'Partly. Zoho Creator can do what Airtable does, but it is a full low-code application platform with scripting, native mobile apps and portals. Zoho\'s like-for-like alternative to Airtable is Zoho Tables, a collaborative database with grid, Kanban, gallery, calendar and form views.'),
        ('Is Zoho Tables included in Zoho One?',
         'Yes. Zoho\'s pricing page for Zoho Tables states that Zoho One includes the Professional plan at no extra cost. Zoho Creator is also part of Zoho One.'),
        ('How many records can an Airtable base hold?',
         'Airtable\'s plans overview lists 1,000 records per base on Free, 50,000 on Team and 125,000 on the self-serve Business plan. Enterprise Scale limits are agreed with Airtable sales.'),
        ('Do read-only users cost money in Airtable or Zoho Creator?',
         'Airtable does not charge for read-only collaborators, form submissions or share links on its paid plans. Zoho Creator is priced per user, with external customers or suppliers handled as portal users: three are free and more are bought as an add-on.'),
        ('Did Airtable change its pricing after the Bending Spoons acquisition?',
         'Not so far. In a post on 12 October 2026, Airtable said its plans, prices and service offerings are unchanged after the acquisition closed in early September 2026, and its Fall 2026 release announced no price changes. Check Airtable\'s pricing page for current terms.'),
    ],
))

# ------------------------------------------------------------------ Zoho Inventory vs Katana
ARTICLES.append(dict(
    slug='zoho-inventory-vs-katana',
    title='Zoho Inventory vs Katana for Small Manufacturers: Assembly or Real Production?',
    seo_title='Zoho Inventory vs Katana for Manufacturers',
    description='Zoho Inventory and Katana compared for small manufacturers: assemblies versus manufacturing orders, shop floor, outsourced production, traceability, sales channels, accounting, plans and how Katana connects to Zoho through Zoho Flow.',
    lead='Zoho Inventory and Katana both promise to keep a small manufacturer&rsquo;s stock straight, and both connect to Shopify. Underneath, they answer different questions. Zoho Inventory records that something was assembled. Katana plans and tracks how it gets made. This guide shows where that line falls, using each vendor&rsquo;s own documentation.',
    category='Manufacturing', keyword='zoho inventory vs katana',
    published='2026-10-14', modified='2026-10-14',
    cover_alt='Four choices for a small manufacturer in a two-by-two grid: Zoho Inventory for one-step assembly, Katana for multi-step production, Zoho ERP for Indian manufacturers wanting finance and production together, and a Zoho Creator app for an unusual process',
    caption='The question is not which product is better, but whether your production is one step or several.',
    related=['zoho-for-manufacturing', 'zoho-erp-vs-odoo-manufacturing', 'zoho-flow-vs-deluge'],
    body='''
<p>A small manufacturer usually outgrows spreadsheets in the same order: stock first, then orders, then production. Zoho Inventory and Katana both cover the first two well. The difference is the third, and choosing the wrong one means either paying for planning you do not need or forcing production into a tool that only records it.</p>
<p>Everything below was checked on Zoho&rsquo;s and Katana&rsquo;s own pricing pages, product pages and help articles on 14 October 2026. Where a vendor does not state something, we say so. We do not quote prices; follow the links to the official pricing pages.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Zoho Inventory</strong> is stock and order management with <em>assemblies</em>: you build a finished item from components in one step, and stock moves accordingly. Zoho&rsquo;s own knowledge base says it does not yet support manufacturing modules.</li>
  <li><strong>Katana</strong> is inventory software built around production: bills of materials with subassemblies, manufacturing orders tracked on a shop floor app, material planning for make-to-stock and make-to-order, and outsourced production.</li>
</ul>
<p>If your production is one step that takes minutes, Zoho Inventory is simpler and fits naturally with Zoho Books and Zoho CRM. If it has several operations, people on the floor and materials to plan ahead, Katana is built for that job.</p>

<h2 id="at-a-glance">Side by side</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">Zoho Inventory</th><th scope="col">Katana</th></tr></thead>
  <tbody>
    <tr><th scope="row">Production</th><td>Assemblies of composite items, in one step</td><td>Manufacturing orders from bills of materials, including subassemblies</td></tr>
    <tr><th scope="row">Shop floor</th><td>No shop floor screens</td><td>Shop Floor App for operators, with no user limit</td></tr>
    <tr><th scope="row">Material planning</th><td>Reorder levels; assemble the shortfall from a sales order</td><td>Calculates material needs and timing for make-to-stock and make-to-order</td></tr>
    <tr><th scope="row">Outsourced production</th><td>No dedicated document</td><td>Outsourced purchase orders, with a stock location for each contractor</td></tr>
    <tr><th scope="row">Batch and serial</th><td>From the Premium plan, including on assemblies</td><td>Batch, serial and expiry tracking</td></tr>
    <tr><th scope="row">Accounting</th><td>Zoho Books, in the same Zoho account</td><td>Through integrations such as QuickBooks Online and Xero</td></tr>
    <tr><th scope="row">Plans</th><td>Free, Standard, Premium, Plus, Enterprise, priced per organisation with order, user and location limits</td><td>Free (up to 30 SKUs) and Advantage (custom-priced annual contract); unlimited users on both</td></tr>
    <tr><th scope="row">In Zoho One?</th><td>Yes</td><td>No; connects to Zoho through Zoho Flow</td></tr>
  </tbody>
</table>
</div>
<p>Check the current details on <a href="https://www.zoho.com/us/inventory/pricing/" target="_blank" rel="noopener">Zoho Inventory pricing</a> and <a href="https://katanamrp.com/pricing/" target="_blank" rel="noopener">Katana pricing</a>.</p>

<h2 id="production">Production: an assembly is not a manufacturing order</h2>
<p>This is the difference that matters, and most comparison sites skip it.</p>
<figure style="margin:2rem auto;max-width:620px">
<svg viewBox="0 0 600 250" role="img" aria-labelledby="ik-title ik-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="ik-title">An assembly in Zoho Inventory compared with a manufacturing order in Katana</title>
  <desc id="ik-desc">Top row, Zoho Inventory: components go straight to a finished item in one assembly step. Bottom row, Katana: components go through a manufacturing order with operations recorded on the shop floor before the finished item is received.</desc>
  <style>
    .ik-a{animation:ik-one 6s ease-in-out infinite}
    .ik-b{animation:ik-two 6s ease-in-out infinite}
    @keyframes ik-one{0%{transform:translateX(0);opacity:0}10%{opacity:1}45%{transform:translateX(380px);opacity:1}55%,100%{transform:translateX(380px);opacity:0}}
    @keyframes ik-two{0%{transform:translateX(0);opacity:0}10%{opacity:1}30%{transform:translateX(127px)}50%{transform:translateX(253px)}75%{transform:translateX(380px);opacity:1}85%,100%{transform:translateX(380px);opacity:0}}
    @media (prefers-reduced-motion: reduce){.ik-a,.ik-b{animation:none;opacity:0}}
  </style>
  <g font-size="16" font-weight="700" fill="#1A1A2E"><text x="20" y="30">Zoho Inventory: assembly</text><text x="20" y="150">Katana: manufacturing order</text></g>
  <line x1="110" y1="70" x2="490" y2="70" stroke="#C9DCEF" stroke-width="4" stroke-linecap="round"/>
  <circle cx="110" cy="70" r="13" fill="#fff" stroke="#226DB4" stroke-width="4"/>
  <circle cx="490" cy="70" r="13" fill="#089949" stroke="#089949" stroke-width="4"/>
  <circle class="ik-a" cx="110" cy="70" r="6" fill="#226DB4"/>
  <g font-size="14" fill="#4B5563" text-anchor="middle"><text x="110" y="104">Components</text><text x="300" y="60">Assemble</text><text x="490" y="104">Finished item</text></g>
  <line x1="110" y1="190" x2="490" y2="190" stroke="#C9DCEF" stroke-width="4" stroke-linecap="round"/>
  <g fill="#fff" stroke="#C77700" stroke-width="4"><circle cx="110" cy="190" r="13"/><circle cx="237" cy="190" r="13"/><circle cx="363" cy="190" r="13"/></g>
  <circle cx="490" cy="190" r="13" fill="#089949" stroke="#089949" stroke-width="4"/>
  <circle class="ik-b" cx="110" cy="190" r="6" fill="#C77700"/>
  <g font-size="14" fill="#4B5563" text-anchor="middle"><text x="110" y="224">Components</text><text x="237" y="224">Operation 1</text><text x="363" y="224">Operation 2</text><text x="490" y="224">Finished item</text></g>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">One step that records stock, or several steps that someone plans and tracks.</figcaption>
</figure>
<p><strong>In Zoho Inventory,</strong> a composite item lists its components, and creating an <em>assembly</em> consumes them and adds the finished item to stock. Components can include services such as labour, as long as at least one inventory item is included, and a composite item can contain another one. If a sales order or invoice asks for more than you have, an Assemble option calculates the shortfall and builds it. Deleting an assembly puts the components back. What it does not have is a document that moves through operations, a routing, or a screen for the people doing the work. Zoho&rsquo;s knowledge base states plainly that manufacturing modules are not yet supported and suggests composite items as the workaround for basic assemblies.</p>
<p><strong>In Katana,</strong> production is the centre of the product. Bills of materials include subassemblies and operations, manufacturing orders are tracked in real time, and operators see their task lists, priorities and instructions in the Shop Floor App. Katana calculates manufacturing cost from the bill of materials, operations and material used, and works out material needs and timing for both make-to-stock and make-to-order.</p>

<h2 id="outsourcing">Outsourced production</h2>
<p>Many small manufacturers send part of the work out: plating, machining, packing. Katana has a documented workflow for it. You create a separate stock location for each contractor, move materials there, and use an <strong>outsourced purchase order</strong> to track the job and receive the finished goods back. On receipt, Katana combines the contractor&rsquo;s fee with the cost of your materials at that location.</p>
<p>Zoho Inventory has no equivalent document. You can model a contractor as a separate warehouse and move stock with transfer orders, but the job itself, and its cost, has to be tracked around it. In India, Zoho ERP has a subcontract manufacturing section with subcontract bills of materials, orders and material transfers; our <a href="/insights/zoho-erp-vs-odoo-manufacturing/">Zoho ERP vs Odoo comparison</a> covers it.</p>

<h2 id="channels-accounts">Sales channels and accounting</h2>
<p>Both sell through the usual channels. Zoho Inventory&rsquo;s US edition lists Amazon, Etsy and eBay as marketplaces, and Shopify and Zoho Commerce as shopping carts. Katana names Shopify, Amazon, WooCommerce, BigCommerce and eBay among its integrations; on its Free plan, Shopify is the only e-commerce integration.</p>
<p>Accounting is where the two take opposite approaches. Zoho Inventory works with Zoho Books in the same Zoho account, and with Zoho CRM for the sales side. Katana does not present an accounting module of its own; it connects to QuickBooks Online and Xero. For a business outside the US, UK, Australia or New Zealand, check that the accounting product it pairs with handles your local tax rules. Our <a href="/insights/zoho-books-vs-quickbooks/">Zoho Books vs QuickBooks Online</a> comparison covers that side of the choice, and <a href="/insights/mrpeasy-vs-zoho/">MRPeasy vs Zoho</a> looks at another MRP that pairs with QuickBooks and Xero.</p>

<h2 id="zoho-connection">Running Katana alongside Zoho</h2>
<p>Choosing Katana for production does not mean leaving Zoho. Zoho Flow has a Katana connector. Its triggers include a sales order created, packed or delivered, a product created and a purchase order created; its actions include creating customers, products, sales orders and purchase orders, updating batch stock and fetching inventory. A common design is Zoho CRM for enquiries and quotes, with a won deal creating the sales order in Katana, and stock levels read back for the sales team.</p>
<p>Flow suits a handful of simple steps. For high volume or two-way sync, use code; our guide to <a href="/insights/zoho-flow-vs-deluge/">Zoho Flow, Deluge and custom middleware</a> explains the trade-offs. On AI, Katana lists API and MCP server access on its Advantage plan, and Zoho MCP lists Zoho Inventory among its supported services; our <a href="/insights/zoho-mcp-claude-chatgpt/">Zoho MCP guide</a> covers how to set limits on what an assistant may change.</p>

<h2 id="plans">Plans and users</h2>
<p>The two price in different ways, so compare them on your own numbers rather than a headline figure.</p>
<ul>
  <li><strong>Zoho Inventory</strong> is priced per organisation. Each plan caps orders a month, users and locations; the Free plan has one user and one location, and Enterprise has ten users and ten locations. Composite items are on every plan, and batch and serial tracking start at Premium. It is also included in Zoho One.</li>
  <li><strong>Katana</strong> has two plans. Free allows up to 30 SKUs, with unlimited SKUs for the first 15 days, and unlimited users, locations and integrations. Advantage removes the SKU limit and is quoted as one annual price that covers implementation, integrations and support. Both include the Shop Floor App.</li>
</ul>

<h2 id="other-routes">When neither is the answer</h2>
<p>Two other routes are worth a look. If you are in India and want finance, GST and production in one Zoho system, Zoho ERP has bills of materials, manufacturing orders, job cards, work centers and quality checks; it is sold separately from Zoho One, and our <a href="/insights/tranzact-vs-zoho-erp/">TranZact vs Zoho ERP comparison</a> sets it against another Indian option. If your process is unusual, such as made-to-measure products or job work on customer-supplied material, a Zoho Creator app built around it may fit better than either product. Our overview of <a href="/insights/zoho-for-manufacturing/">Zoho for manufacturing</a> compares these routes, and our <a href="/manufacturing/guides/zoho-or-manufacturing-erp/">guide to Zoho or a manufacturing ERP</a> helps decide when dedicated software is the safer choice.</p>

<h2 id="how-to-decide">How to decide: five questions</h2>
<ol>
  <li><strong>How many steps does production have?</strong> One quick step points to Zoho Inventory; several operations point to Katana.</li>
  <li><strong>Do operators need to record work?</strong> If yes, Zoho Inventory has no screen for them.</li>
  <li><strong>Do you plan materials ahead of orders?</strong> Katana plans needs and timing; Zoho Inventory works from reorder levels.</li>
  <li><strong>Where do your accounts live?</strong> Zoho Books favours Zoho Inventory; QuickBooks Online or Xero favours Katana.</li>
  <li><strong>Do you need traceability by batch?</strong> Both can, on the right plan. Our guide to <a href="/manufacturing/guides/batch-lot-traceability/">batch and lot traceability</a> lists what to record.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Does Zoho Inventory have manufacturing orders?',
         'No. Zoho Inventory has composite items, which you build through assemblies that consume components in one step. Zoho\'s knowledge base says it does not yet support manufacturing modules. Zoho ERP, sold in India, has manufacturing orders, job cards and work centers.'),
        ('Can Katana integrate with Zoho CRM or Zoho Books?',
         'Zoho Flow has a Katana connector with triggers such as a new sales order or purchase order and actions such as creating customers, products and sales orders. That makes links to Zoho CRM practical. For accounting, Katana names QuickBooks Online and Xero as its integrations, so a link to Zoho Books is something you build, for example as a flow in Zoho Flow.'),
        ('Is Katana free?',
         'Katana has a Free plan for up to 30 SKUs with unlimited users, locations and integrations, and unlimited SKUs for the first 15 days. The paid Advantage plan is custom-priced on an annual contract.'),
        ('Which is better for a business that only assembles kits?',
         'Zoho Inventory. If production is a single step, such as packing sets or assembling a product from a fixed list of parts, its assemblies and kits handle stock and costs without the extra setup of a production system.'),
        ('Does Katana handle subcontracting?',
         'Yes. Katana\'s outsourced manufacturing workflow uses a separate stock location for each contractor and an outsourced purchase order to track the job and receive finished goods, combining the contractor\'s fee with your material cost.'),
    ],
))
