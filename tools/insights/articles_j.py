# Article content, part J (26 October 2026 run).

ARTICLES = []

# ------------------------------------------------------------------ Zoho Creator vs Quickbase
ARTICLES.append(dict(
    slug='zoho-creator-vs-quickbase',
    title='Zoho Creator vs Quickbase: Pricing Models, Limits and Fit for Operations Teams',
    seo_title='Zoho Creator vs Quickbase (2026 Comparison)',
    description='Zoho Creator vs Quickbase compared: per-user plans against a platform minimum and read-based entitlements, record and call limits, offline mobile use on the shop floor, portals, AI, SSO and sandboxes, and which fits an operations or manufacturing team.',
    lead='Zoho Creator and Quickbase are both low-code platforms that operations teams use to replace spreadsheets with real applications: production trackers, quality logs, asset registers and supplier portals. They are priced in very different ways, and that difference shapes which one fits long before you compare features.',
    category='Comparisons', keyword='zoho creator vs quickbase',
    published='2026-10-26', modified='2026-10-26',
    cover_alt='Zoho Creator vs Quickbase: how you pay shapes the choice. Two colour panels. Zoho Creator: per user, monthly or yearly; free plan with one app; offline forms in the mobile app on every plan; 3 portal users free, more as an add-on. Quickbase: per user, billed annually, plus a platform minimum; Team, Business and Enterprise plans; SSO and sandbox from Business; offline forms through FastField, sold separately. Facts below: Creator trial 15 days, Quickbase trial 30 days, Quickbase plans also meter integration reads',
    caption='Both build solid operations apps. The pricing model and the shop-floor setup usually decide between them.',
    related=['zoho-creator-vs-power-apps', 'zoho-creator-vs-airtable', 'zoho-preventive-maintenance-vs-cmms'],
    body='''
<p>Most comparisons of Zoho Creator and Quickbase are review-site grids of star ratings. They rarely explain the part that decides the bill: Zoho Creator charges per user with published plan limits, while Quickbase combines per-user plans with a platform minimum and an entitlement measured in &ldquo;reads&rdquo;.</p>
<p>Every plan detail below was checked on Zoho&rsquo;s and Quickbase&rsquo;s own pages on 26 October 2026. We do not quote prices, because both change; see the official <a href="https://www.zoho.com/creator/pricing.html" target="_blank" rel="noopener">Zoho Creator pricing</a> and <a href="https://www.quickbase.com/plans-and-pricing" target="_blank" rel="noopener">Quickbase plans</a> pages. We build on Zoho, so read this with that in mind; we say where Quickbase is the better fit.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Choose Zoho Creator</strong> if you want to start small and monthly, need offline data entry in the mobile app, want external portals for customers or suppliers, or already run Zoho CRM, Books or Inventory.</li>
  <li><strong>Choose Quickbase</strong> if you are a larger operations team that wants single sign-on, a sandbox and Gantt views on its mid-tier plan, Pipelines for integrations, and can commit to an annual contract with a platform minimum.</li>
  <li><strong>Before you compare,</strong> list who will use the app, who outside the company needs access, and which systems it must send data to. Those three answers change the price of each platform more than any feature.</li>
</ul>

<h2 id="at-a-glance">Zoho Creator and Quickbase at a glance</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">Zoho Creator</th><th scope="col">Quickbase</th></tr></thead>
  <tbody>
    <tr><th scope="row">Plans</th><td>Free, Standard, Professional, Enterprise, plus a custom Flex plan</td><td>Team, Business, Enterprise</td></tr>
    <tr><th scope="row">How you pay</th><td>Per user, monthly or yearly</td><td>Per user, billed annually, plus a platform minimum; a usage-based option is also offered</td></tr>
    <tr><th scope="row">Free option and trial</th><td>Free plan with one app; 15-day trial of paid plans</td><td>No free plan listed; 30-day trial with Business features</td></tr>
    <tr><th scope="row">Published limits</th><td>Records, storage, script statements and external calls per plan</td><td>App space and storage vary by plan; amounts not published</td></tr>
    <tr><th scope="row">Scripting</th><td>Deluge, Zoho&rsquo;s scripting language</td><td>No-code builder; Pipelines for automation and integration</td></tr>
    <tr><th scope="row">Mobile and offline</th><td>Native iOS and Android apps; offline forms on every plan</td><td>Quickbase mobile app; offline forms through FastField, a separate product</td></tr>
    <tr><th scope="row">External users</th><td>Customer portals: 3 users free, more as an add-on</td><td>Public (&ldquo;everyone on the internet&rdquo;) access counts toward integration reads</td></tr>
    <tr><th scope="row">Single sign-on</th><td>SAML SSO included on Enterprise, an add-on below</td><td>SSO with SCIM provisioning from Business</td></tr>
    <tr><th scope="row">Test environment</th><td>Developer environments on paid plans</td><td>Sandbox from Business</td></tr>
    <tr><th scope="row">AI</th><td>Zia agents to plan, build and test apps; bring your own key from OpenAI, Google or Anthropic</td><td>Optional AI Intelligence Pack add-on; Pave, a separate AI app builder</td></tr>
  </tbody>
</table>
</div>

<h2 id="pricing-models">Two pricing models, two kinds of surprise</h2>
<p><strong>Zoho Creator</strong> is licensed per user. Zoho&rsquo;s pricing FAQ says you buy a licence for each unique person who accesses your applications, and you can pay monthly or yearly. The Free plan covers one app for basic needs, and after the 15-day trial an account moves to the Free plan. The surprise with Creator is usually the user count: a production tracker that thirty supervisors open needs thirty licences, unless some of them are better served through a portal.</p>
<p><strong>Quickbase</strong> lists Team and Business at a price per user per month, billed annually, and notes that the price shown does not include the platform minimum. Its FAQ explains that instead of focusing pricing on seats, Quickbase charges a platform minimum fee, and that all users on an account must be on the same plan. There is also a usage-based option priced on the collective use of all users rather than the number of users. Enterprise is quoted.</p>
<p>The less visible part is the entitlement. Quickbase&rsquo;s help centre says pricing is based on <strong>reads</strong>. On user-based plans only integration reads count: reads by external software through the API, Pipelines steps that send data out of Quickbase, and activity by public users who are not signed in. On usage-based plans, ordinary user reads (opening forms, reports and dashboards) count too. Quickbase does not stop workflows at the limit; its account team contacts you about buying more. So for Quickbase, ask how many reads your integrations and public forms will generate, not just how many people will log in.</p>

<h2 id="limits">Limits that shape the design</h2>
<p>Zoho publishes its Creator limits per plan, which makes sizing a project straightforward:</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Zoho Creator limit</th><th scope="col">Standard</th><th scope="col">Professional</th><th scope="col">Enterprise</th></tr></thead>
  <tbody>
    <tr><th scope="row">Applications</th><td>1</td><td>Unlimited</td><td>Unlimited</td></tr>
    <tr><th scope="row">Records</th><td>25,000 per user</td><td>100,000 per user</td><td>250,000 per user</td></tr>
    <tr><th scope="row">File storage</th><td>1 GB per user</td><td>3 GB per user</td><td>5 GB per user</td></tr>
    <tr><th scope="row">Deluge execution statements</th><td>10,000</td><td>20,000</td><td>50,000</td></tr>
    <tr><th scope="row">External calls (webhooks, integration tasks)</th><td>100 per user a day</td><td>250 per user a day</td><td>500 per user a day</td></tr>
    <tr><th scope="row">Data sources / custom connectors</th><td>5 / 5</td><td>15 / 10</td><td>30 / 20</td></tr>
  </tbody>
</table>
</div>
<p>The Free plan allows 5,000 records and 250 MB of storage. Because Creator&rsquo;s record and storage allowances grow with users, a small team with a lot of historical data can hit the record cap before it hits anything else; plan archiving early.</p>
<p>Quickbase says each plan comes with different amounts of application space and storage, but its pricing page does not publish the figures. Ask for them in writing, along with your read entitlement, before you sign.</p>

<h2 id="shop-floor">The shop floor: mobile, offline and scanning</h2>
<p>For a factory or warehouse, the mobile experience often decides the platform.</p>
<p><strong>Zoho Creator</strong> apps run in native iOS and Android apps on every plan, including Free. Zoho&rsquo;s help documents offline components: you add a form or report to the app&rsquo;s offline list, users enter data without a connection, and entries submit when the device is back online. Reports are view-only offline, some form features (formula fields that depend on other inputs, and workflows that run before submission) do not work offline, and mandatory and no-duplicate checks run only when the entries sync. Text and number fields can scan barcodes and QR codes from a phone or tablet, with formats such as Code 128, EAN-13 and QR.</p>
<p><strong>Quickbase</strong> has its own mobile app for viewing dashboards and reports and adding or editing records; its help page lists Android 12 and iOS 17 or later. For offline forms, Quickbase sells <strong>FastField</strong>, a mobile forms product with its own per-seat plans, offline capability and a native integration that sends data into Quickbase apps. Quickbase&rsquo;s manufacturing page positions the platform for production scheduling, quality control and compliance, shop floor management and maintenance.</p>
<p>So if supervisors will log output or inspections in areas with poor Wi-Fi, Creator covers it in the base product, while Quickbase covers it with a second subscription. Our guide to <a href="/insights/zoho-preventive-maintenance-vs-cmms/">preventive maintenance on Zoho or a CMMS</a> shows a typical shop-floor app built this way.</p>

<h2 id="portals">Customers, suppliers and contractors</h2>
<p>Creator&rsquo;s customer portals let people outside the company sign in to submit and track their own records, such as a supplier confirming a delivery date or a customer raising a complaint. Portal users are not counted as internal users. Three are free on paid plans, and more are bought as an add-on that supports up to 500,000 portal users per portal.</p>
<p>Quickbase can open an app to the public, and that activity is counted as integration reads rather than tied to a licence. For a handful of external contributors, either works; for hundreds of suppliers or customers, price both models with your real numbers.</p>

<h2 id="integrations">Integrations and automation</h2>
<p><strong>Zoho Creator</strong> integrates with other Zoho apps built in, and its Deluge scripts can call any REST API; our guide to <a href="/insights/deluge-invokeurl-api-calls/">calling external APIs with Deluge invokeurl</a> shows how. If your CRM, accounts or stock already run on Zoho, a Creator app can read and write those records without middleware.</p>
<p><strong>Quickbase</strong> uses Pipelines for automation and integration, plus open APIs and pre-built integrations listed by plan. Remember the billing rule: Pipelines steps that bring data into Quickbase are not billable, while steps that send data out are. Enterprise adds on-premises connectivity and data warehouse integrations, and Business and Enterprise can add Quickbase Extensions, a pack of nine add-ons such as document generation and e-signature.</p>

<h2 id="ai-governance">AI, security and governance</h2>
<p>Zoho lists Zia agents for planning, building and testing Creator apps, a choice of Zoho&rsquo;s own models or your own key from OpenAI, Google or Anthropic, and access to app data from AI assistants through MCP. Paid plans include an allowance of AI calls per month (200 on Standard, 1,000 on Professional and Enterprise). Quickbase offers an optional AI Intelligence Pack on every plan, and sells Pave separately as an AI app builder billed by runtime credits.</p>
<p>On governance, Quickbase&rsquo;s Business plan adds SSO with SCIM provisioning, a sandbox, Gantt charts and FDA and HIPAA compliance, and keeps audit logs for 6 months on Team, 1 year on Business and 3 years on Enterprise. Creator includes an audit trail and developer environments on paid plans, with SAML SSO included on Enterprise and available as an add-on on Standard and Professional. If regulated record-keeping is central, compare the audit retention you need against both.</p>

<h2 id="choose">Which one fits</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Your situation</th><th scope="col">Usually the better fit</th></tr></thead>
  <tbody>
    <tr><th scope="row">You want to start with one app and pay monthly</th><td>Zoho Creator</td></tr>
    <tr><th scope="row">Shop-floor data entry without reliable Wi-Fi</th><td>Zoho Creator, or Quickbase with FastField</td></tr>
    <tr><th scope="row">Many suppliers or customers need to log in</th><td>Zoho Creator portals; price Quickbase reads too</td></tr>
    <tr><th scope="row">CRM, accounts or stock already on Zoho</th><td>Zoho Creator</td></tr>
    <tr><th scope="row">SSO, SCIM and a sandbox on a mid-tier plan</th><td>Quickbase Business</td></tr>
    <tr><th scope="row">Builders who want no scripting at all</th><td>Quickbase</td></tr>
  </tbody>
</table>
</div>
<p>If you are also weighing Microsoft or Airtable, our comparisons of <a href="/insights/zoho-creator-vs-power-apps/">Zoho Creator vs Power Apps</a> and <a href="/insights/zoho-creator-vs-airtable/">Zoho Creator vs Airtable</a> use the same approach.</p>

<h2 id="trial-plan">A two-week trial plan</h2>
<ul class="checklist">
  <li>Pick one real process, such as a daily production log or an incoming inspection, and build it on both trials.</li>
  <li>Count internal users, external users and every system the app must send data to.</li>
  <li>Test the mobile form on the factory floor with the connection switched off.</li>
  <li>Ask Quickbase for your platform minimum, app space and read entitlement in writing.</li>
  <li>Check Creator&rsquo;s record, storage and external call limits against a year of your data.</li>
</ul>
<p>If you choose Creator and want help designing the app or connecting it to the rest of your systems, our <a href="/zoho-creator-development/">Zoho Creator development</a> page explains how we work.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Is Zoho Creator cheaper than Quickbase?',
         'It depends on your users and integrations. Zoho Creator is priced per user with a free plan and monthly billing. Quickbase is priced per user, billed annually, plus a platform minimum, with an entitlement based on reads. Price both with your real user counts on the official pricing pages.'),
        ('Does Quickbase work offline?',
         'Quickbase\'s mobile app help page does not describe offline use. Quickbase sells FastField, a separate mobile forms product with offline capability and a native integration that sends data into Quickbase apps.'),
        ('Does Zoho Creator work offline?',
         'Yes. In the Creator mobile app on iOS and Android, you can make forms and reports available offline on all plans. Entries are submitted when the device reconnects, and reports are view-only while offline.'),
        ('What are reads in Quickbase pricing?',
         'Reads are Quickbase\'s usage entitlement. On user-based plans only integration reads count, such as API calls, Pipelines steps that send data out and public access. On usage-based plans, users opening forms, reports and dashboards count as well.'),
        ('Does Quickbase have a free plan?',
         'Quickbase\'s plans page lists Team, Business and Enterprise and a 30-day free trial with Business features, but no free plan. Zoho Creator has a free plan with one app and 5,000 records.'),
    ],
))

# ------------------------------------------------------------------ Deluge invokeurl
ARTICLES.append(dict(
    slug='deluge-invokeurl-api-calls',
    title='Deluge invokeurl: How to Call External APIs from Zoho, With Code',
    seo_title='Deluge invokeurl: Calling APIs [With Code]',
    description='How to call external REST APIs from Zoho with the Deluge invokeurl task: syntax, connections, JSON requests, reading status codes, timeouts, allowed ports in Indian and EU data centres, limits, and receiving calls into Zoho CRM.',
    lead='Sooner or later every Zoho project has to talk to a system Zoho does not integrate with: a factory database, a logistics API, a payment gateway. In Deluge that job falls to one task, invokeurl. Getting a call to work is easy. Making it reliable takes a few habits most examples skip.',
    category='Deluge', keyword='deluge invokeurl',
    published='2026-10-26', modified='2026-10-26',
    cover_alt='Calling APIs with invokeurl: four habits for reliable API calls, shown as four arrows. Step 1 Connect: credentials in a connection. Step 2 Send: headers and a JSON body. Step 3 Check: read the status code. Step 4 Log: save failed calls to retry. A Deluge code snippet calls invokeurl with type POST, a connection and detailed true, and a developer figure gives the takeaway: check the status code, not just the body. Facts: a 40-second invokeurl timeout, 5,000,000 Zoho CRM calls a day, and 3 extra ports allowed in the India and EU data centres',
    caption='A call that works once is easy. A call that keeps working needs a connection, a status check and somewhere to log failures.',
    related=['deluge-script-examples', 'zoho-flow-vs-deluge', 'zoho-crm-api-limits'],
    body='''
<p>Deluge is the scripting language inside Zoho CRM, Creator, Books and other Zoho apps. When a script needs data from, or has to send data to, a system outside Zoho, it uses the <code>invokeurl</code> task. Zoho&rsquo;s Deluge reference spells it <code>invokeUrl</code>; Zoho CRM&rsquo;s examples use <code>invokeurl</code>. This guide covers the syntax, authentication, error handling and the limits that trip up real integrations, with code you can adapt.</p>
<p>All syntax and limits below were checked against Zoho&rsquo;s own documentation on 26 October 2026: the <a href="https://www.zoho.com/deluge/help/webhook/invokeurl-api-task.html" target="_blank" rel="noopener">invokeUrl task reference</a>, the Deluge connections guide and the Zoho CRM functions limits page.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Use a connection</strong> for authentication, never a token pasted into the script.</li>
  <li><strong>Add <code>detailed: true</code></strong> and check <code>responseCode</code> before you trust the response.</li>
  <li><strong>Design for the limits:</strong> the call times out after 40 seconds, each Zoho app caps daily calls, and in Zoho&rsquo;s Indian and EU data centres only a few non-standard ports are allowed outside Creator.</li>
</ul>

<h2 id="syntax">The syntax, parameter by parameter</h2>
<pre><code>response = invokeurl
[
    url: "https://api.example.com/v1/orders"
    type: POST
    headers: headerMap
    body: payload.toString()
    connection: "example_api"
    detailed: true
];</code></pre>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Parameter</th><th scope="col">What it does</th></tr></thead>
  <tbody>
    <tr><th scope="row"><code>url</code></th><td>The full request URL, including any query string. URLs with self-created SSL certificates cannot be called.</td></tr>
    <tr><th scope="row"><code>type</code></th><td>GET, POST, PUT, PATCH, DELETE or OPTIONS. Defaults to GET.</td></tr>
    <tr><th scope="row"><code>headers</code></th><td>A map of request headers, such as Content-Type.</td></tr>
    <tr><th scope="row"><code>body</code></th><td>The request body as text, a file or a map. Cannot be used together with <code>parameters</code>.</td></tr>
    <tr><th scope="row"><code>parameters</code></th><td>The older way to send a body; for GET and DELETE it acts as query parameters.</td></tr>
    <tr><th scope="row"><code>files</code></th><td>Files for a multipart form upload.</td></tr>
    <tr><th scope="row"><code>connection</code></th><td>The link name of the connection that authenticates the call.</td></tr>
    <tr><th scope="row"><code>detailed</code></th><td><code>true</code> returns the status code and headers as well as the content. Defaults to <code>false</code>.</td></tr>
    <tr><th scope="row"><code>response-format</code></th><td><code>FILE</code> returns the response as a file; <code>NONE</code> ignores it.</td></tr>
  </tbody>
</table>
</div>
<p>Content types follow the body: text is sent as text/plain, a map as multipart/form-data, and a file as application/octet-stream. A Content-Type header overrides the default, which is why JSON calls set it explicitly.</p>

<h2 id="connections">Authentication: always use a connection</h2>
<p>A connection stores credentials outside the script and handles token refresh. Zoho offers ready-made services for many apps, and custom services for anything else, with these authentication types: API key (sent as a query string, form data or header), Basic, OAuth 2 (authorization code, authorization code with PKCE, or client credentials), OAuth 1 and AWS Signature Version 4.</p>
<p>Three details matter in production. The link name you reference in the script must start with a lowercase letter and can be up to 50 characters. Connections unused for more than six months are revoked automatically, so a quarterly job can fail for that reason alone. And editing or deleting a custom service revokes every connection made from it. Note in your documentation which scripts use which connection.</p>

<h2 id="get-example">Example 1: fetch data and update a record</h2>
<p>A Zoho CRM function that asks a logistics API for a shipment&rsquo;s status and saves it on the deal. The API and field names are placeholders.</p>
<pre><code>// Argument: dealId
deal = zoho.crm.getRecordById("Deals", dealId);
awb = deal.get("Tracking_Number");
if (awb == null)
{
    return "No tracking number";
}
response = invokeurl
[
    url: "https://api.example-logistics.com/v1/shipments/" + awb
    type: GET
    connection: "logistics_api"
    detailed: true
];
if (response.get("responseCode") == 200)
{
    data = response.get("responseText").toString().toMap();
    update = Map();
    update.put("Shipment_Status", data.get("status"));
    zoho.crm.updateRecord("Deals", dealId, update);
    return "Updated";
}
return "Lookup failed: " + response.get("responseCode");</code></pre>

<h2 id="post-example">Example 2: send JSON to another system</h2>
<p>A manufacturer often needs to push a confirmed order from Zoho CRM or Creator into a production or warehouse system. Build a map, convert it to text and set the content type:</p>
<pre><code>payload = Map();
payload.put("order_ref", order.get("Order_No"));
payload.put("item_code", order.get("Item_Code"));
payload.put("quantity", order.get("Quantity"));
payload.put("due_date", order.get("Due_Date").toString("yyyy-MM-dd"));

headerMap = Map();
headerMap.put("Content-Type", "application/json");

response = invokeurl
[
    url: "https://mes.example.com/api/production-orders"
    type: POST
    headers: headerMap
    body: payload.toString()
    connection: "factory_mes"
    detailed: true
];</code></pre>
<p>If the receiving system expects form fields instead of JSON, send the map without converting it and set the content type to application/x-www-form-urlencoded.</p>

<figure style="margin:2rem auto;max-width:660px">
<svg viewBox="0 0 660 210" role="img" aria-labelledby="iu-title iu-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="iu-title">How a reliable invokeurl call flows</title>
  <desc id="iu-desc">A Deluge script sends a request through a connection to an external API. The response comes back with a status code. A 2xx code updates the Zoho record. Any other code, or a timeout, writes a row to an error log that a scheduled function retries later.</desc>
  <style>
    .iu-dot{animation:iu-move 4s linear infinite}
    .iu-d2{animation-delay:2s}
    @keyframes iu-move{0%{transform:translateX(0);opacity:0}10%{opacity:1}85%{opacity:1}100%{transform:translateX(196px);opacity:0}}
    @media (prefers-reduced-motion: reduce){.iu-dot{animation:none;opacity:0}}
  </style>
  <defs><marker id="iu-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#067A3B"/></marker></defs>
  <rect x="20" y="62" width="160" height="66" rx="12" fill="#ECFDF3" stroke="#067A3B" stroke-width="1.5"/>
  <text x="100" y="91" font-size="14" font-weight="700" fill="#1A1A2E" text-anchor="middle">Deluge script</text>
  <text x="100" y="111" font-size="12" fill="#4B5563" text-anchor="middle">invokeurl + connection</text>
  <rect x="250" y="62" width="160" height="66" rx="12" fill="#067A3B"/>
  <text x="330" y="91" font-size="14" font-weight="700" fill="#fff" text-anchor="middle">External API</text>
  <text x="330" y="111" font-size="12" fill="#D1FAE5" text-anchor="middle">40-second timeout</text>
  <rect x="480" y="20" width="160" height="58" rx="12" fill="#fff" stroke="#067A3B" stroke-width="1.5"/>
  <text x="560" y="45" font-size="13.5" font-weight="700" fill="#1A1A2E" text-anchor="middle">2xx: update record</text>
  <text x="560" y="63" font-size="12" fill="#4B5563" text-anchor="middle">responseCode checked</text>
  <rect x="480" y="112" width="160" height="58" rx="12" fill="#fff" stroke="#B45309" stroke-width="1.5"/>
  <text x="560" y="137" font-size="13.5" font-weight="700" fill="#1A1A2E" text-anchor="middle">Other: log it</text>
  <text x="560" y="155" font-size="12" fill="#4B5563" text-anchor="middle">retry from a schedule</text>
  <path d="M188 95H242" stroke="#067A3B" stroke-width="2" marker-end="url(#iu-a)"/>
  <path d="M418 88C445 80 455 56 472 52" stroke="#067A3B" stroke-width="2" fill="none" marker-end="url(#iu-a)"/>
  <path d="M418 102C445 110 455 134 472 140" stroke="#B45309" stroke-width="2" stroke-dasharray="6 5" fill="none" marker-end="url(#iu-a)"/>
  <text x="330" y="196" font-size="12" fill="#4B5563" text-anchor="middle">Every call that gets a response counts against the app&#8217;s external call limit</text>
  <circle class="iu-dot" cx="196" cy="95" r="5" fill="#0AB058"/>
  <circle class="iu-dot iu-d2" cx="196" cy="95" r="5" fill="#0AB058"/>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">Check the status, then either update the record or log the failure. Never let a failed call pass silently.</figcaption>
</figure>

<h2 id="status">Check the status code, not just the body</h2>
<p>Without <code>detailed: true</code>, invokeurl returns only the content, so an error page or an error message in JSON looks like a normal reply. With it, the response is a map with three keys: <code>responseCode</code> (the HTTP status), <code>responseText</code> (the content) and <code>responseHeader</code> (a map of headers, such as content-type).</p>
<p>A simple rule set covers most integrations: a 2xx code is success; 400 to 404 mean the request or credentials are wrong and retrying will not help; 429 means you are sending too fast; 5xx and timeouts are worth one later retry. Wrap the call in <code>try</code> and <code>catch</code> so a timeout reaches the same handling as an error code; our <a href="/insights/deluge-script-examples/">Deluge script examples</a> show that pattern with <code>throw</code>.</p>
<p>Deluge scripts run inside time limits, so do not retry in a loop. Write the failed payload to a log record (a custom module in CRM or a form in Creator) and let a scheduled function retry it later. That also gives someone a list to check when the other system was down.</p>

<h2 id="limits">Timeouts and limits to design around</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Limit</th><th scope="col">What Zoho documents</th></tr></thead>
  <tbody>
    <tr><th scope="row">invokeurl timeout</th><td>A socket timeout error if the API takes more than 40 seconds to respond</td></tr>
    <tr><th scope="row">Zoho CRM function run time</th><td>10 seconds for buttons, related lists, validation rules and REST API functions; 30 seconds for automation; 15 minutes for scheduled functions</td></tr>
    <tr><th scope="row">Zoho CRM daily calls</th><td>5,000,000 invokeurl GET and POST requests a day; 10 MB response size</td></tr>
    <tr><th scope="row">Zoho Creator daily calls</th><td>External calls (webhooks and integration tasks): 100, 250 or 500 per user a day on Standard, Professional and Enterprise</td></tr>
    <tr><th scope="row">File downloads</th><td>Up to 5 MB in Creator; elsewhere 15 MB from Zoho domains and 5 MB from other domains</td></tr>
    <tr><th scope="row">Counting</th><td>Every execution that receives a response counts, including each pass through a loop</td></tr>
  </tbody>
</table>
</div>
<p>The run-time limits matter most. A button that calls a slow API has 10 seconds in Zoho CRM, even though invokeurl itself would wait 40. For slow or bulk work, have the function hand the job to a scheduled function, or to middleware that replies at once and does the heavy lifting; our <a href="/insights/zoho-flow-vs-deluge/">Zoho Flow vs Deluge guide</a> explains when that is worth it. Calls to Zoho CRM&rsquo;s own API from Deluge also use API credits, as our <a href="/insights/zoho-crm-api-limits/">Zoho CRM API limits</a> guide explains.</p>

<h2 id="ports">The port rule that catches Indian factories</h2>
<p>Many factory systems, such as a local MES, a weighbridge server or a machine data gateway, expose their API on a non-standard port like 8080. Zoho&rsquo;s invokeurl limitations page lists the ports allowed for services other than Zoho Creator: 21 non-standard ports in the US and China data centres, but only <strong>8011, 9001 and 8082</strong> in the Indian and EU data centres. Zoho Creator allows every port from 80 to 65535 in all data centres.</p>
<p>So a Zoho CRM account on the Indian data centre cannot call <code>https://factory.example.com:8080</code> directly. Publish the API on the standard HTTPS port behind a reverse proxy, use one of the allowed ports, or make the call from Creator. Check this before you promise a go-live date.</p>

<h2 id="zoho-to-zoho">Calling other Zoho apps: use invokeapi</h2>
<p>For Zoho-to-Zoho calls, first look for a built-in integration task such as <code>zoho.crm.updateRecord</code>. When you need an API endpoint that has no task, Deluge&rsquo;s <code>invokeapi</code> takes a service name and a path instead of a full URL, and works out the domain for your data centre itself. Zoho lists it for Zoho CRM, Books, Invoice, Billing, Inventory, Bookings, Creator and WorkDrive. That avoids hard-coding <code>.com</code> or <code>.in</code> addresses that break if an account moves.</p>

<h2 id="inbound">The other direction: letting systems call Zoho CRM</h2>
<p>invokeurl sends requests out. To receive them, a Zoho CRM function can be exposed as a REST API from its Overview tab, with an API key or OAuth 2.0. The function reads the incoming request through <code>crmAPIRequest</code> (method, parameters, body and headers) and can set the status code and body it returns with <code>crmAPIResponse</code>. Zoho recommends OAuth 2.0 for production, and treating an API key URL as a secret.</p>

<h2 id="checklist">Before you go live</h2>
<ul class="checklist">
  <li>Credentials sit in a connection, and the connection owner is documented.</li>
  <li>Every call uses <code>detailed: true</code> and checks <code>responseCode</code>.</li>
  <li>Timeouts and error codes reach a log record, not just an <code>info</code> line.</li>
  <li>The function finishes inside its run-time limit with a slow API response.</li>
  <li>The target port is allowed in your Zoho data centre.</li>
  <li>Daily call volumes, including loops, are well under the app&rsquo;s limit.</li>
</ul>
<p>If you have integrations that fail quietly, or a factory system you need to connect to Zoho, our <a href="/zoho-integrations/">Zoho integrations</a> and <a href="/deluge-development/">Deluge development</a> pages explain how we work.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('What is invokeurl in Deluge?',
         'invokeurl is the Deluge task for calling web APIs over HTTP from Zoho apps such as Zoho CRM, Creator and Books. It supports GET, POST, PUT, PATCH, DELETE and OPTIONS, with headers, a body, files and a connection for authentication.'),
        ('How do I send JSON with invokeurl?',
         'Build a map, pass it as body with toString(), and add a Content-Type header of application/json. Without that header, a map is sent as multipart form data by default.'),
        ('What is the invokeurl timeout?',
         'Zoho\'s documentation says invokeurl throws a socket timeout error if the API takes more than 40 seconds to respond. The function running it may have a shorter limit, such as 10 seconds for a Zoho CRM button.'),
        ('Why does invokeurl fail on port 8080?',
         'For services other than Zoho Creator, Zoho allows only certain non-standard ports. In the Indian and EU data centres the list is 8011, 9001 and 8082, so port 8080 is blocked there. Zoho Creator allows ports 80 to 65535.'),
        ('Does invokeurl count against API limits?',
         'Yes. Every execution that receives a response counts against the app\'s external call limit, including each pass through a loop. Zoho CRM allows 5,000,000 invokeurl GET and POST requests a day, and calls to Zoho CRM\'s own API also use API credits.'),
    ],
))
