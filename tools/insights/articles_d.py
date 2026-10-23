# Article content, part D (October 2026 run).

ARTICLES = []

# ------------------------------------------------------------------ Zoho CRM Blueprint
ARTICLES.append(dict(
    slug='zoho-crm-blueprint-setup',
    title='Zoho CRM Blueprint: A Step-by-Step Setup Guide, With a Manufacturing Example',
    seo_title='Zoho CRM Blueprint Setup Guide [With Example]',
    description='How to design and build a Zoho CRM Blueprint: edition limits, states and transitions, Before, During and After settings, SLAs, automatic transitions, testing and the mistakes to avoid, using an enquiry-to-order process as the example.',
    lead='A Blueprint turns a sales process from a document nobody reads into steps the CRM enforces. Done well, it removes the follow-up chasing. Done badly, it blocks your team at every stage. This guide shows how to build one that people will actually use.',
    category='Zoho CRM', keyword='zoho crm blueprint',
    published='2026-10-12', modified='2026-10-12',
    cover_alt='Four Blueprint transitions for a manufacturer, owned by sales, engineers and costing, with the information each one requires, the Before, During and After parts of a transition, and edition limits of 3, 50 and 100 Blueprints',
    caption='A Blueprint is a set of gates. Each gate asks for exactly the information the next person needs.',
    related=['zoho-crm-implementation-cost', 'migrate-hubspot-salesforce-to-zoho-crm', 'zoho-for-manufacturing'],
    body='''
<p>Most CRMs record what happened. A Blueprint in Zoho CRM controls what happens next. It ties a process to a picklist field, usually the deal stage, and only lets a record move to the next stage when the right person has supplied the right information.</p>
<p>Every fact below about editions, limits and settings was checked against Zoho&rsquo;s feature comparison page and help documentation in October 2026. The example process is a design we use to explain the method, not a client project.</p>

<h2 id="what-it-does">What a Blueprint does</h2>
<p>Zoho describes a Blueprint as a flowchart of a business process. It has two building blocks:</p>
<ul>
  <li><strong>States</strong> are the stages of the process, taken from the values of the picklist you choose, for example the Stage field on Deals.</li>
  <li><strong>Transitions</strong> are the moves between states. Each one appears as a button on the record, and each has three parts: <em>Before</em> (who can use it, and on which records), <em>During</em> (what they must enter) and <em>After</em> (what the CRM does automatically once it runs).</li>
</ul>
<p>Once a record is in a Blueprint, the field that drives it is locked. A rep cannot simply change the stage from a dropdown; they have to use a transition and complete what it asks for.</p>

<h2 id="editions">Which Zoho CRM edition you need</h2>
<p>Blueprint is not in the Free or Standard editions. The limits below come from Zoho&rsquo;s complete feature list, and the Blueprint counts include the default Blueprints Zoho provides.</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Feature</th><th scope="col">Professional</th><th scope="col">Enterprise</th><th scope="col">Ultimate</th></tr></thead>
  <tbody>
    <tr><th scope="row">Blueprints</th><td>3</td><td>50</td><td>100</td></tr>
    <tr><th scope="row">Validation rules</th><td>5 per layout</td><td>10 per layout</td><td>25 per layout</td></tr>
    <tr><th scope="row">Approval processes</th><td>Not included</td><td>Up to 10 active per module</td><td>Up to 50 active per module</td></tr>
    <tr><th scope="row">User-defined SLA actions in a Blueprint</th><td>No</td><td>Yes</td><td>Yes</td></tr>
    <tr><th scope="row">Kiosks inside a transition</th><td>No</td><td>Yes</td><td>Yes</td></tr>
  </tbody>
</table>
</div>
<p>Three Blueprints on Professional is enough for one main sales process and one or two others. If you need separate processes for several product lines or modules, plan for Enterprise. Limits change, so confirm them on Zoho&rsquo;s <a href="https://www.zoho.com/crm/complete-feature-list.html" target="_blank" rel="noopener">feature comparison page</a> before you design around them. Our <a href="/insights/zoho-crm-implementation-cost/">Zoho CRM implementation cost guide</a> explains how edition choice affects the total cost.</p>

<h2 id="blueprint-or-workflow">Blueprint, workflow rule or approval process?</h2>
<p>These three tools overlap, and choosing the wrong one is the most common design mistake we see.</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Use</th><th scope="col">When</th><th scope="col">Example</th></tr></thead>
  <tbody>
    <tr><th scope="row">Workflow rule</th><td>Something should happen automatically when a record is created or changes, with no human step</td><td>Email the regional manager when a deal over a set value is created</td></tr>
    <tr><th scope="row">Approval process</th><td>One record needs a yes or no from a named approver before it is used</td><td>A discount above the agreed limit</td></tr>
    <tr><th scope="row">Blueprint</th><td>A record passes through several stages, different people own different stages, and each stage needs specific information</td><td>Enquiry, technical review, costing, quote, order</td></tr>
  </tbody>
</table>
</div>
<p>They also work together. A Blueprint transition can run the same kinds of actions a workflow can, and an approval can still sit on a single step inside the process.</p>

<h2 id="example">The example: enquiry to order for a manufacturer</h2>
<p>Sales processes in manufacturing have a feature generic CRM guides ignore: the quote depends on other departments. Engineering has to confirm the part can be made, and someone has to cost it, before sales can send a price. That makes it a good fit for a Blueprint, because each hand-off is a gate.</p>
<p>The process uses the Deals module and its Stage field, with five states:</p>
<figure style="margin:2rem auto;max-width:600px">
<svg viewBox="0 0 520 240" role="img" aria-labelledby="bp-title bp-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="bp-title">A five-state Blueprint from enquiry to order</title>
  <desc id="bp-desc">Five states in a row: Enquiry received, Technical review, Costing, Quote sent and Order won. A common transition called Mark lost is available from every state.</desc>
  <style>
    .bp-dot{animation:bp-move 8s linear infinite}
    @keyframes bp-move{0%{transform:translateX(0);opacity:0}5%{opacity:1}95%{opacity:1}100%{transform:translateX(440px);opacity:0}}
    @media (prefers-reduced-motion: reduce){.bp-dot{animation:none;opacity:0}}
  </style>
  <line x1="40" y1="60" x2="480" y2="60" stroke="#C9DCEF" stroke-width="4" stroke-linecap="round"/>
  <g fill="#fff" stroke="#226DB4" stroke-width="4">
    <circle cx="40" cy="60" r="14"/><circle cx="150" cy="60" r="14"/><circle cx="260" cy="60" r="14"/><circle cx="370" cy="60" r="14"/>
  </g>
  <circle cx="480" cy="60" r="14" fill="#089949" stroke="#089949" stroke-width="4"/>
  <circle class="bp-dot" cx="40" cy="60" r="7" fill="#226DB4"/>
  <g font-size="18" font-weight="700" fill="#1A1A2E" text-anchor="middle">
    <text x="45" y="108">Enquiry</text><text x="45" y="130">received</text>
    <text x="150" y="108">Technical</text><text x="150" y="130">review</text>
    <text x="260" y="108">Costing</text>
    <text x="370" y="108">Quote</text><text x="370" y="130">sent</text>
    <text x="475" y="108">Order</text><text x="475" y="130">won</text>
  </g>
  <rect x="40" y="172" width="440" height="46" rx="23" fill="#FDECEC"/>
  <text x="260" y="201" font-size="17" font-weight="700" fill="#B42318" text-anchor="middle">Common transition from any state: Mark lost</text>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">Four gates and one exit. Each gate asks only for what the next owner needs.</figcaption>
</figure>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Transition</th><th scope="col">Before: who</th><th scope="col">During: required</th><th scope="col">After: automatic</th></tr></thead>
  <tbody>
    <tr><th scope="row">Send for review</th><td>Sales</td><td>Drawing or specification attached, quantity, required date</td><td>Task for the engineering owner</td></tr>
    <tr><th scope="row">Approve for costing</th><td>Engineering</td><td>Checklist: material, process and tolerances confirmed; note on risks</td><td>Field update and email to costing</td></tr>
    <tr><th scope="row">Release price</th><td>Costing</td><td>Unit price and validity date, with a validation rule on the margin field</td><td>Task for sales to prepare the quote</td></tr>
    <tr><th scope="row">Mark quote sent</th><td>Sales</td><td>Quote associated with the deal, follow-up date</td><td>Follow-up task on that date</td></tr>
    <tr><th scope="row">Confirm order</th><td>Sales</td><td>Customer PO number and PO attached</td><td>Notify operations; optionally a webhook or function to create the sales order elsewhere</td></tr>
  </tbody>
</table>
</div>
<p>Notice what is not here: no state for every internal conversation, and no mandatory field that the person at that step cannot answer. That restraint is what keeps a Blueprint usable.</p>

<h2 id="build">Step by step: building it in Zoho CRM</h2>
<ol>
  <li><strong>Create the Blueprint.</strong> Go to Setup, then Process Management, then Blueprint, and click Create Blueprint. Choose the module (Deals), the layout and the field (Stage). Entry criteria are optional; without them, every record created in that layout enters the process.</li>
  <li><strong>Draw the states.</strong> Drag the stage values into the editor and connect them. The Start state is the picklist&rsquo;s &ldquo;None&rdquo; value, so the first transition takes a new record into its first real stage.</li>
  <li><strong>Add transitions</strong> between states and give each a verb-based name, such as &ldquo;Send for review&rdquo;. Names can be up to 50 characters.</li>
  <li><strong>Set Before.</strong> Choose who can run each transition (CRM users, or portal users) and add criteria that control when the button appears, for example only after a drawing has been attached.</li>
  <li><strong>Set During.</strong> Add fields from the deal or related modules and mark them mandatory or optional, add validation messages, checklists, notes, attachments, associated items such as tasks or quotes, and short instructions.</li>
  <li><strong>Set After.</strong> Add email notifications, tasks, field updates, new records, tags, webhooks or custom functions. Our <a href="/insights/deluge-script-examples/">Deluge script examples</a> show the kind of logic a function can add.</li>
  <li><strong>Add a common transition</strong> such as &ldquo;Mark lost&rdquo;. A common transition is available from every state, so you do not have to draw an exit from each one.</li>
  <li><strong>Test before you publish.</strong> Zoho&rsquo;s documentation points to Sandbox for testing a Blueprint without touching live data. Run a dozen deals through every path, including the awkward ones.</li>
</ol>

<h2 id="advanced">Automatic transitions, loops and SLAs</h2>
<p>Three newer options solve problems that used to need workarounds, and most guides skip them:</p>
<ul>
  <li><strong>Automatic transitions</strong> move a record to another state if nobody acts within a set time. Zoho&rsquo;s example is a five-day wait. In our process, a quote with no response could move automatically to a follow-up state.</li>
  <li><strong>Same-state loops</strong> are transitions whose start and end state are the same, so an action can be repeated until it succeeds. &ldquo;Log follow-up call&rdquo; on the Quote sent state is a natural use.</li>
  <li><strong>SLAs</strong> set the maximum time a record may stay in a state, who is alerted and when, including alerts before the deadline. From Enterprise, the SLA can also run actions of its own, such as a field update, a task or a webhook. A technical review that sits for a week is exactly what an SLA should catch.</li>
</ul>

<h2 id="users">What your team sees</h2>
<p>On the record, a Blueprint strip shows the current state and the available transition buttons. Transition owners also see their pending items under My Jobs. Clicking a button opens a short form with the During items.</p>
<p>Users can save a transition as a draft and finish it later, with some exceptions Zoho lists: not when layout rules run, when the form has only messages, when a widget is used, or in a continuous Blueprint. Blueprint also works in the Zoho CRM mobile apps, which matters for sales staff who visit factories and customers.</p>

<h2 id="mistakes">Six mistakes to avoid</h2>
<ol>
  <li><strong>Too many states.</strong> Model hand-offs between people, not every activity. Five to seven states is plenty for most sales processes.</li>
  <li><strong>Mandatory fields nobody can fill.</strong> If costing cannot know the delivery date, do not make it mandatory at costing.</li>
  <li><strong>Forgetting integrations and imports.</strong> Once a field drives a Blueprint, Zoho allows changes to it only through specific routes such as the transition API, workflow field updates and functions. Check any integration that writes the stage before you go live.</li>
  <li><strong>No way back.</strong> Real deals move backwards. Add transitions from costing back to technical review, or a loop, instead of forcing people to mark deals lost and recreate them.</li>
  <li><strong>Testing on live deals.</strong> Test in a sandbox or on a small set of clearly marked test records first.</li>
  <li><strong>Never looking at the data.</strong> Zoho provides Blueprint usage reports. Review where deals wait longest a month after launch, and adjust.</li>
</ol>
<p>If you are moving from another CRM, rebuild the process as a Blueprint rather than copying old automations; our <a href="/insights/migrate-hubspot-salesforce-to-zoho-crm/">migration plan</a> covers when to do that. For a manufacturer, the deal process is usually the first step towards a connected system; our guide to <a href="/insights/zoho-for-manufacturing/">Zoho for manufacturing</a> covers what comes after the order.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Which Zoho CRM edition includes Blueprint?',
         'Blueprint starts in the Professional edition, which allows 3 Blueprints. Enterprise allows 50 and Ultimate 100. Zoho counts its default Blueprints within these limits. Free and Standard do not include Blueprint.'),
        ('Can I use Blueprint on modules other than Deals?',
         'Yes. You choose the module, layout and picklist field when you create a Blueprint, so it is not limited to Deals. Pick the module where the process actually lives, for example Leads for qualification or a module that tracks samples or service requests.'),
        ('Can a rep change the stage manually once a Blueprint is active?',
         'No. The field that drives the Blueprint is locked on records in the process, and users move records with transition buttons. Zoho allows the field to be changed through routes such as the transition API, workflow field updates and functions.'),
        ('What is the difference between Blueprint and an approval process?',
         'An approval process gets a yes or no from a named approver on one record. A Blueprint runs a whole multi-stage process with different owners and required information at each stage. Approval processes start in the Enterprise edition.'),
        ('Does Blueprint work on the Zoho CRM mobile app?',
         'Yes. Users can see the Blueprint strip and run transitions from the Zoho CRM apps for Android and iOS, completing the required fields on the phone.'),
    ],
))

# ------------------------------------------------------------------ Zoho ERP vs Odoo
ARTICLES.append(dict(
    slug='zoho-erp-vs-odoo-manufacturing',
    title='Zoho ERP vs Odoo for Manufacturers in India: A Fair Comparison',
    seo_title='Zoho ERP vs Odoo for Manufacturers (India)',
    description='Zoho ERP and Odoo compared for Indian manufacturers: bills of materials, job cards, planning, quality, subcontracting, GST and e-invoicing, licensing and customisation, with the questions to ask in a demo.',
    lead='Until January 2026 the honest answer to &ldquo;Zoho or Odoo for manufacturing?&rdquo; was short: Zoho had no manufacturing module. Zoho ERP changed that in India. Most comparisons online still pit Odoo against Zoho Books or Zoho Inventory, which is the wrong match. This is the right one.',
    category='Manufacturing', keyword='zoho erp vs odoo',
    published='2026-10-12', modified='2026-10-12',
    cover_alt='Zoho ERP and Odoo for Indian manufacturers: what both cover, where Zoho ERP stands out and where Odoo stands out, with plan limits and licensing facts',
    caption='Both now run production in India. They differ most in planning depth, licensing and how much of the rest of your business already runs on Zoho.',
    related=['zoho-for-manufacturing', 'zoho-books-vs-tallyprime', 'zoho-flow-vs-deluge'],
    body='''
<p>Zoho ERP and Odoo are now both credible ways for an Indian manufacturer to run finance, stock and production in one system. They come from very different places. Zoho ERP grew out of Zoho&rsquo;s finance and operations apps and is sold as a cloud subscription in India. Odoo is a modular suite with an open-source Community edition and a licensed Enterprise edition, used worldwide. If a fully open-source ERP is on your list too, see our <a href="/insights/erpnext-vs-zoho-erp/">ERPNext vs Zoho ERP comparison</a>.</p>
<p>We build on Zoho, so read this with that in mind. We have kept every claim to what each vendor publishes on its own site, checked in October 2026, and we say where one product is the better fit.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Choose Zoho ERP</strong> if you are in India, your production follows a bill of materials, job card and work center model, and you want finance, GST, payroll and production in one Zoho system, especially if you already use Zoho CRM or other Zoho apps.</li>
  <li><strong>Choose Odoo</strong> if planning is the hard part of your business (scheduling by work center capacity, maintenance, engineering changes), if you need to run outside India, or if you want the option of an open-source edition you can host and modify yourself.</li>
  <li><strong>Either way,</strong> it is an ERP project. The software matters less than how well your BOMs, routings and opening stock are prepared.</li>
</ul>

<h2 id="comparison">Side-by-side comparison</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">Zoho ERP</th><th scope="col">Odoo</th></tr></thead>
  <tbody>
    <tr><th scope="row">What it is</th><td>One cloud ERP: finance, supply chain, payroll and manufacturing</td><td>A suite of apps you combine; Manufacturing is one app</td></tr>
    <tr><th scope="row">Bills of materials</th><td>Bill of Materials module, including subcontract BOMs</td><td>Multi-level BOMs</td></tr>
    <tr><th scope="row">Production</th><td>Manufacturing orders, job cards, shop floor, work centers, operations and cost templates</td><td>Manufacturing orders, work centers with a control panel, a documented Shop Floor app</td></tr>
    <tr><th scope="row">Planning</th><td>A planning module that schedules operations across work centers; a component requirements report</td><td>An MRP scheduler that plans work at each work center by OEE and capacity</td></tr>
    <tr><th scope="row">Quality</th><td>Quality templates, rules, inspections and an inspection worklist</td><td>Control points, quality checks and quality alerts</td></tr>
    <tr><th scope="row">Maintenance and engineering</th><td>Not part of the published manufacturing feature list</td><td>Preventive and corrective maintenance; PLM with versioning and engineering changes</td></tr>
    <tr><th scope="row">Subcontracting (job work)</th><td>Subcontract BOMs, subcontract orders and material transfers</td><td>Documented subcontracting flows</td></tr>
    <tr><th scope="row">GST compliance</th><td>GST filing, e-invoicing and e-way bills built in</td><td>India localization with GSTR-1 filing, GSTR-2B reconciliation, e-invoicing, e-way bills and TDS/TCS</td></tr>
    <tr><th scope="row">Licensing</th><td>Cloud subscription per user; yearly transaction caps per plan</td><td>Community (open source) or Enterprise (licensed)</td></tr>
    <tr><th scope="row">Where it is sold</th><td>Published for India at the time of writing</td><td>Worldwide</td></tr>
  </tbody>
</table>
</div>
<p>Check current plans on the official pricing pages for <a href="https://www.zoho.com/en-in/erp/pricing/" target="_blank" rel="noopener">Zoho ERP</a> and <a href="https://www.odoo.com/pricing" target="_blank" rel="noopener">Odoo</a>. We do not quote prices here because both change.</p>

<h2 id="production">Production: how deep does each go?</h2>
<p><strong>Zoho ERP</strong> covers the core of discrete production. A manufacturing order is created from a bill of materials, or from a sales order, and is broken into operations tracked on job cards at work centers. A shop floor screen shows daily production against plan, work center timings set when each work center is available, and cost templates attach costs to operations. Batches, lots and serial numbers can be linked through to finished goods. Reports include delayed job cards and a component requirements summary.</p>
<p><strong>Odoo</strong> goes further on planning and the engineering side. Its manufacturing page describes an MRP scheduler that schedules work at each work center based on OEE and capacity, a work center control panel, cost analysis and unbuild orders, which take a finished product apart to recover components. Separate apps add preventive and corrective maintenance and product lifecycle management with versioning and engineering change orders.</p>
<p>Two cautions. First, Odoo spreads these features across several apps, and which of them your edition includes is something to confirm in writing. Second, Zoho ERP is young and its documentation changes often. Judge both on what is live today, not on a roadmap.</p>

<h2 id="job-work">Job work and subcontracting</h2>
<p>Job work is everyday business for Indian manufacturers, in both directions: sending material out for plating, heat treatment or machining, and doing work on a customer&rsquo;s material.</p>
<ul>
  <li><strong>Zoho ERP</strong> has a subcontract manufacturing section with subcontract BOMs, subcontract orders, purchase orders and material transfers to the subcontractor.</li>
  <li><strong>Odoo</strong> documents subcontracting as part of Manufacturing, including a basic flow where components are supplied to the subcontractor and finished goods are received back.</li>
</ul>
<p>In a demo, ask each vendor to show stock lying with a job worker as a separate figure, and how the records support your GST reporting on goods sent for job work. That one scenario tells you more than a feature list. Our <a href="/insights/tranzact-vs-zoho-erp/">TranZact vs Zoho ERP comparison</a> applies the same test to TranZact.</p>

<h2 id="gst">GST, e-invoicing and payroll</h2>
<p>Both handle Indian compliance, in different ways.</p>
<p><strong>Zoho ERP</strong> includes GST filing, e-invoicing with registration on the Invoice Registration Portal, e-way bill generation and updates, and TDS forms. Payroll is part of the same product: pay runs, reimbursements, proof of investments, salary revisions and employee loans.</p>
<p><strong>Odoo&rsquo;s</strong> India localization files GSTR-1, reconciles vendor bills against GSTR-2B, produces a GSTR-3B report, uploads e-invoices to the NIC portal and generates e-way bills, including from receipts and deliveries in Inventory. TDS and TCS are supported with threshold alerts. Odoo&rsquo;s documentation names a specific GST Suvidha Provider that must be configured, and you need API credentials from the NIC and GST portals.</p>
<p>The practical difference: in Zoho ERP, statutory features come with the product and Zoho maintains them. In Odoo, they come from localization modules, and on a self-hosted or customised setup, keeping them current is part of your upgrade work.</p>

<h2 id="licensing">Licensing and cost structure</h2>
<p><strong>Zoho ERP</strong> has three plans. Standard requires at least five users and allows 100,000 transactions per organization per year. Premium allows up to 300,000 transactions a year, counting sales, purchase and manufacturing orders. Custom is quoted for very high volumes. Zoho prices full users and employees (internal staff with role-based access) separately, so count both groups. Zoho ERP is not included in Zoho One; it is a separate product with a 14-day free trial.</p>
<p><strong>Odoo</strong> comes as Community, which is open source, and Enterprise, which is licensed and built on top of Community. The choice affects which apps you get, how you host and who upgrades the system. Hosting, upgrade and support arrangements differ by plan, so read the pricing page with your partner.</p>
<p>For a fair cost comparison, count three years, not one: subscriptions, implementation, hosting where it applies, upgrades, and the internal time needed to keep masters clean. Transaction volume matters for Zoho ERP; customisation and upgrade effort matter most for Odoo. If you already use Zoho One, remember that Zoho ERP is licensed on top of it; our <a href="/insights/zoho-one-implementation-checklist/">Zoho One implementation checklist</a> explains how to plan for that.</p>

<h2 id="customisation">Customisation and the rest of your stack</h2>
<p>Zoho ERP supports custom functions written in Deluge, triggered by workflows, and its help documents an integration with Zoho CRM. If your sales team already works in Zoho CRM, or you use Zoho Analytics for reporting, staying inside one vendor reduces integration work. Where you need screens Zoho ERP does not offer, such as a maintenance log or an NCR and CAPA process, a Zoho Creator app can sit beside it (our <a href="/insights/zoho-preventive-maintenance-vs-cmms/">guide to preventive maintenance on Zoho or a CMMS</a> covers the maintenance case); our <a href="/insights/zoho-flow-vs-deluge/">guide to Zoho Flow, Deluge and middleware</a> explains how to connect the pieces.</p>
<p>Odoo is customised with Studio, its no-code tool, or with custom modules written by developers, and it has a large store of third-party apps. That flexibility is its strength and its cost: heavily customised Odoo systems need careful upgrade planning.</p>

<h2 id="decide">How to decide: six questions</h2>
<ol>
  <li><strong>Where will you operate?</strong> If you need the same ERP outside India today, Zoho ERP is not yet published there. For a small manufacturer elsewhere, our <a href="/insights/zoho-inventory-vs-katana/">Zoho Inventory vs Katana comparison</a> covers a lighter option.</li>
  <li><strong>How hard is your planning?</strong> If finite scheduling, maintenance and engineering changes are central, Odoo&rsquo;s published features go further.</li>
  <li><strong>How many transactions a year?</strong> Count sales, purchase and manufacturing orders against Zoho ERP&rsquo;s plan caps.</li>
  <li><strong>What else runs on Zoho?</strong> CRM, Analytics and Creator apps make Zoho ERP easier to connect.</li>
  <li><strong>Who will maintain it?</strong> An open-source, customised system needs a partner or an in-house developer for years, not months.</li>
  <li><strong>Can both run your real job?</strong> Give each vendor one real BOM with its routing and one job-work order, and ask them to run it end to end.</li>
</ol>
<p>If you are still deciding whether you need an ERP at all, start with our overview of <a href="/insights/zoho-for-manufacturing/">Zoho&rsquo;s three routes for manufacturers</a>. If your accounts are in Tally today, our <a href="/insights/zoho-books-vs-tallyprime/">Zoho Books vs TallyPrime comparison</a> covers that side of the decision, and our <a href="/manufacturing/">manufacturing solutions</a> page shows how we approach the build.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Is Zoho ERP better than Odoo for manufacturing?',
         'It depends on the factory. Zoho ERP suits Indian manufacturers with a standard BOM, job card and work center process who want finance, GST, payroll and production in one Zoho system. Odoo goes further on planning by work center capacity, maintenance and engineering changes, and is available worldwide.'),
        ('Does Zoho ERP have MRP?',
         'Zoho ERP has bills of materials, manufacturing orders, job cards, work centers, a planning module that schedules operations across work centers, and a component requirements summary report. Ask Zoho to demonstrate material planning on your own BOMs, because its published feature list does not describe a full MRP run.'),
        ('Is Odoo free for manufacturers?',
         'Odoo Community is open source, so there is no licence fee, but you still pay for hosting, implementation and upgrades. Odoo Enterprise is licensed. Check which manufacturing apps each edition includes on Odoo\'s own pages.'),
        ('Do both support GST e-invoicing and e-way bills?',
         'Yes. Zoho ERP includes GST filing, e-invoicing and e-way bills. Odoo\'s India localization supports GSTR-1 filing, GSTR-2B reconciliation, e-invoicing through the NIC portal and e-way bills, with a GST Suvidha Provider that must be configured.'),
        ('Is Zoho ERP part of Zoho One?',
         'No. Zoho states that Zoho ERP is not included in Zoho One and is sold separately with its own plans.'),
    ],
))

# ------------------------------------------------------------------ Zoho Books vs TallyPrime
ARTICLES.append(dict(
    slug='zoho-books-vs-tallyprime',
    title='Zoho Books vs TallyPrime: Which Fits a Growing Manufacturer or Trader?',
    seo_title='Zoho Books vs TallyPrime for Manufacturers',
    description='Zoho Books and TallyPrime compared for Indian manufacturers and traders: cloud or desktop, licensing, GST and e-invoicing, BOM and job work, CRM links and migration, plus when to keep Tally and connect Zoho around it.',
    lead='Most Indian manufacturers we speak to keep their books in Tally. The question is rarely whether Tally works; it does. The question is whether it still fits once sales, stock and production need to share data across people and places. Here is a fair comparison.',
    category='Comparisons', keyword='zoho books vs tally',
    published='2026-10-12', modified='2026-10-12',
    cover_alt='Two questions and answers: stay on Tally if production and job work live there, move to Zoho Books if sales, branches and owners need live data, and Tally can be kept alongside Zoho; with facts on Tally job work, the 25-user Zoho Books plan and e-invoicing',
    caption='Tally is strong at the books and the stock journal. Zoho Books is strong when sales, stock and accounts need the same live data.',
    related=['zoho-erp-vs-odoo-manufacturing', 'zoho-for-manufacturing', 'zoho-crm-vs-hubspot'],
    body='''
<p>TallyPrime and Zoho Books both do Indian accounting well: GST, e-invoicing, e-way bills, bank reconciliation and statutory reports. Comparing them feature by feature produces a long table of ticks on both sides and no decision.</p>
<p>The real differences are in how each one is built, how it handles production, and how it connects to the rest of the business. Every product fact below was checked on Tally&rsquo;s and Zoho&rsquo;s own sites in October 2026. We work on Zoho, so we have tried to be especially fair to Tally.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Stay on TallyPrime</strong> if your accountant and team know it well, your production is recorded through BOMs, manufacturing journals and job work vouchers that work for you, and most people who need the numbers sit in one office.</li>
  <li><strong>Move to Zoho Books</strong> if sales staff, branches or owners need live data from anywhere, you want quotes, orders and invoices to flow from Zoho CRM without re-entry, and your production is simple enough not to need a full manufacturing module.</li>
  <li><strong>Look at Zoho ERP</strong> instead of Zoho Books if you want to leave Tally and also run bills of materials, job cards and work centers in the same system.</li>
</ul>

<h2 id="how-built">How the two are built</h2>
<p><strong>TallyPrime</strong> is a desktop application for Windows. Tally&rsquo;s own FAQ says your data stays local and the software runs fully offline for day-to-day work. The Silver edition is for one computer at a time; Gold supports multiple users working at once on the same local network. You can buy a perpetual licence or a rental subscription. Tally Software Services (TSS) keeps the software updated with new releases and statutory changes, and powers connected services. To use TallyPrime from a browser or a Mac, Tally sells a separate Cloud Access service.</p>
<p><strong>Zoho Books</strong> is cloud software sold as a subscription, with iOS and Android apps. In India it comes in six plans, from Free (one user and an accountant) to Ultimate (25 users), and features such as e-invoicing, multiple locations, workflow rules and custom functions depend on the plan.</p>
<p>That single difference, local desktop or cloud, decides most of what follows.</p>

<h2 id="comparison">Side-by-side comparison</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">TallyPrime</th><th scope="col">Zoho Books (India)</th></tr></thead>
  <tbody>
    <tr><th scope="row">Where it runs</th><td>Windows desktop; browser access through the separate Cloud Access service</td><td>Cloud, in a browser, plus mobile apps</td></tr>
    <tr><th scope="row">Users</th><td>Silver: one computer at a time. Gold: multiple users on a local network</td><td>From 1 user plus an accountant (Free) to 25 users (Ultimate)</td></tr>
    <tr><th scope="row">Licence</th><td>Perpetual or rental; TSS for updates and connected services</td><td>Subscription by plan</td></tr>
    <tr><th scope="row">GST and e-invoicing</th><td>GST features, e-invoices with Tally as the GSP, e-way bills</td><td>GST filing and e-way bills on all plans; e-invoicing from the Standard plan</td></tr>
    <tr><th scope="row">Bills of materials</th><td>Single or multiple BOMs per item, with by-products, co-products and scrap</td><td>Not offered; composite items only on the Elite and Ultimate plans</td></tr>
    <tr><th scope="row">Production entries</th><td>Manufacturing Journal; WIP tracked through godowns</td><td>None; production needs Zoho ERP or a custom app</td></tr>
    <tr><th scope="row">Job work</th><td>Job Work In and Job Work Out orders with Material In and Material Out vouchers</td><td>Not offered as a feature</td></tr>
    <tr><th scope="row">CRM link</th><td>Through third-party connectors or custom integration</td><td>Two-way sync with Zoho CRM for customers, vendors and items</td></tr>
    <tr><th scope="row">Customisation</th><td>TDL, Tally&rsquo;s development language</td><td>Workflow rules from the Professional plan; custom functions and custom modules from Premium</td></tr>
  </tbody>
</table>
</div>
<p>Prices change and differ by edition, so compare them on the official pages for <a href="https://www.zoho.com/in/books/pricing/" target="_blank" rel="noopener">Zoho Books</a> and <a href="https://tallysolutions.com/tally-prime-faq-guide/" target="_blank" rel="noopener">TallyPrime</a>.</p>

<h2 id="production">Production and job work: where Tally is stronger</h2>
<p>For a manufacturer, this is the section that matters most, and here TallyPrime has the edge over Zoho Books.</p>
<p>TallyPrime lets you define one or more bills of materials for an item, including by-products, co-products and scrap. A Manufacturing Journal records components consumed and finished goods produced in one entry, and a cost estimation report shows production cost. Tally&rsquo;s own guidance is to track work in progress by moving stock between godowns such as raw material store, shop floor and quality check.</p>
<p>Job work is built in. A principal manufacturer records a Job Work Out order, sends material with a Material Out voucher and receives finished goods with a Material In voucher; a job worker does the reverse with Job Work In orders. Reports include stock with each job worker and issue and receipt variances.</p>
<p>Zoho Books has none of this. It tracks stock, and its higher plans add composite items and warehouses, but it has no bill of materials, no production entry and no job work orders. That is not a weakness of the product so much as its scope: Zoho Books is accounting software. In Zoho&rsquo;s range, production lives in <a href="/insights/zoho-erp-vs-odoo-manufacturing/">Zoho ERP</a>, or in a custom app, as our guide to <a href="/insights/zoho-for-manufacturing/">Zoho for manufacturing</a> explains.</p>
<p>So a manufacturer who records production in Tally today should not move to Zoho Books alone and expect the same coverage. If you want to keep Tally and add a production system beside it, our <a href="/insights/tranzact-vs-zoho-erp/">TranZact vs Zoho ERP comparison</a> covers that route.</p>

<h2 id="connected">Connected data: where Zoho Books is stronger</h2>
<p>Zoho Books is at its best when other people need the same numbers. Its integration with Zoho CRM syncs CRM accounts and contacts with Books customers both ways, can sync vendors and products, and lets sales staff raise quotes, sales orders and invoices from a Zoho Finance module inside CRM. Sales and accounts then work from the same customer records.</p>
<p>Because it is cloud software, branches, owners and an outside accountant see the same live data without copying company files. Bank feeds, workflow rules and, on higher plans, custom functions in Deluge let you automate routine steps. If you are also choosing a CRM, our <a href="/insights/zoho-crm-vs-hubspot/">Zoho CRM vs HubSpot comparison</a> covers that side.</p>
<p>TallyPrime has moved in this direction too. Release 7.1 added Docs by Ira, which creates entries from scanned purchase invoices and notes for review, and connected banking now covers ICICI Bank alongside Axis Bank, State Bank of India and Kotak Mahindra Bank. Remote and cloud access are available as separate services.</p>

<h2 id="third-option">The third option: keep Tally, connect Zoho around it</h2>
<p>Many manufacturers do not need to choose. The accounts team stays in TallyPrime, where it is fast and trusted, and the front office moves to Zoho: enquiries and quotes in Zoho CRM, stock and orders in Zoho Inventory, production tracking in a Zoho Creator app. Data then flows into Tally rather than being typed twice.</p>
<p>Zoho&rsquo;s own site lists a third-party Tally connector for Zoho Inventory that sends customers, vendors, items, sales and purchase transactions, e-invoice and e-way bill details into Tally. Note the direction: it moves data from Zoho Inventory into Tally, not back. For reporting, Zoho Analytics can read TallyPrime data directly through its own connector; see our <a href="/insights/zoho-analytics-vs-power-bi/">Zoho Analytics vs Power BI comparison</a>. For anything more, a custom integration is the route. This hybrid is often the lowest-risk first step, and it leaves the bigger accounting decision for later.</p>

<h2 id="migration">If you decide to move from Tally</h2>
<ol>
  <li><strong>Pick a clean cut-over date,</strong> ideally the start of a financial year or quarter.</li>
  <li><strong>Move masters first:</strong> chart of accounts, customers, vendors and items, mapping Tally groups and fields to Zoho&rsquo;s.</li>
  <li><strong>Enter opening balances</strong> from Tally&rsquo;s trial balance and opening stock from its stock summary on the cut-over date.</li>
  <li><strong>Bring across open items only:</strong> unpaid invoices and bills, open orders. Keep closed history in Tally for reference.</li>
  <li><strong>Run both in parallel for one GST period</strong> and reconcile the returns before switching Tally off.</li>
</ol>
<p>Zoho publishes a step-by-step guide for importing from Tally that follows this order, written for its GCC editions; the Indian process is similar, but confirm the India-specific steps with Zoho or your implementer.</p>

<h2 id="decide">Five questions to decide</h2>
<ol>
  <li>Who outside the accounts team needs live numbers, and from where?</li>
  <li>Do you record production and job work in Tally today, and does that work?</li>
  <li>Would sales benefit from seeing payments and stock inside the CRM?</li>
  <li>How many users need access, and which Zoho Books plan would that need?</li>
  <li>Is your accountant comfortable with the change, or will they keep a Tally copy anyway?</li>
</ol>
<p>Answer them honestly and the choice is usually clear. If production is central, compare Zoho ERP, not Zoho Books. If it is not, and people need shared live data, Zoho Books is the better fit.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Is Zoho Books better than Tally?',
         'Neither is better for every business. TallyPrime is stronger for production and job work entries and works offline on a desktop. Zoho Books is stronger when several people, branches or a CRM need the same live data. Manufacturers who want to leave Tally and also run production should compare Zoho ERP instead.'),
        ('Does Zoho Books support bill of materials?',
         'No. Zoho Books does not offer bills of materials or production entries. Its Elite and Ultimate plans include composite items. For manufacturing orders, job cards and BOMs in Zoho, look at Zoho ERP.'),
        ('Can Zoho Books generate e-invoices and e-way bills?',
         'Yes. Zoho Books generates e-way bills on all Indian plans and IRN-validated e-invoices from the Standard plan upwards. The Free plan does not include e-invoicing.'),
        ('Can I use TallyPrime and Zoho together?',
         'Yes. A common pattern keeps accounts in TallyPrime and uses Zoho CRM, Zoho Inventory or a Zoho Creator app for sales and operations, with data sent into Tally. Zoho lists a third-party connector that moves Zoho Inventory data into Tally.'),
        ('Can TallyPrime be used on the cloud?',
         'TallyPrime is a Windows desktop application. Tally sells a separate Cloud Access service that runs TallyPrime online, including from a Mac through a browser, and a Remote Access service for authorised remote users.'),
    ],
))
