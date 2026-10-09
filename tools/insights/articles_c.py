# Article content, part C.

ARTICLES = []

# ------------------------------------------------------------------ Analytics (rewrite)
ARTICLES.append(dict(
    slug='zoho-analytics-agentic-data-foundations-2026',
    title='Getting Your Data Ready for AI in Zoho Analytics: A Practical Foundation',
    seo_title='Zoho Analytics and AI: Building a Data Foundation That Works (2026)',
    description='How to prepare your business data in Zoho Analytics for reliable dashboards and AI features like Ask Zia: connecting sources, modeling data, cleaning it, securing it and keeping it fresh.',
    lead='AI features in analytics tools are impressive in demos and disappointing on messy data. Before you ask Zia a question about revenue, make sure the answer can be right. This is how we set up Zoho Analytics so dashboards and AI insights can be trusted.',
    category='Analytics', keyword='zoho analytics ai',
    published='2026-09-15', modified='2026-10-09',
    cover_alt='An analytics dashboard with revenue charts and a pipeline breakdown built from several connected data sources',
    caption='Good dashboards and good AI answers come from the same place: connected, clean, well-modeled data.',
    related=['zoho-agentic-ai-hyperautomation', 'zoho-crm-implementation-cost', 'deluge-script-examples'],
    body='''
<p>Zoho Analytics can pull data from Zoho CRM, Books, Desk, Creator and, by Zoho&rsquo;s count, more than 500 other sources, then turn it into reports, dashboards and answers to questions typed in plain English. That last part, <strong>Ask Zia</strong>, is where many teams start. It is also where bad data becomes visible fastest.</p>
<p>When an executive asks &ldquo;what was revenue by region last quarter?&rdquo; and gets a number that doesn&rsquo;t match the finance report, trust in the whole system drops. The fix is not a better AI. It is a better foundation.</p>

<h2 id="connect-sources">1. Connect the right sources, in the right way</h2>
<p>Zoho Analytics has native connectors for Zoho apps and for many common business systems and databases, plus file imports and APIs for everything else. A few rules keep things manageable:</p>
<ul>
  <li><strong>Prefer native connectors</strong> over file uploads. They sync on a schedule, so dashboards stay current without anyone remembering to re-upload a spreadsheet.</li>
  <li><strong>Bring in only what you will use.</strong> Importing every module from every app slows syncs and clutters the workspace.</li>
  <li><strong>Choose sync frequency per source.</strong> Sales pipeline data may need refreshing several times a day; accounting data after each day&rsquo;s close is usually enough. The plan sets the ceiling: at the time of writing, Zoho&rsquo;s <a href="https://www.zoho.com/analytics/pricing.html" target="_blank" rel="noopener">pricing page</a> lists a data refresh rate of once a day on Basic, 8 times a day on Standard and Premium, and 24 times a day on Enterprise.</li>
  <li><strong>Keep one workspace per subject area</strong> (sales, finance, support) or one combined workspace with clear folders, rather than many overlapping copies.</li>
</ul>

<h2 id="model-data">2. Model the data so it joins correctly</h2>
<p>Most wrong numbers come from joins, not formulas. When CRM deals, Books invoices and Desk tickets sit in one workspace, Analytics needs to know how they relate.</p>
<ul>
  <li><strong>Define lookup columns</strong> between tables, for example invoice customer to CRM account, so reports can blend data automatically.</li>
  <li><strong>Agree on one customer key.</strong> If CRM and Books use different customer IDs, store the Books ID on the CRM account (a small Deluge function can keep it in sync) and join on that.</li>
  <li><strong>Use query tables</strong> (SQL views inside Analytics) for logic that many reports share, such as &ldquo;active customers&rdquo; or &ldquo;net revenue&rdquo;. Define it once and every report agrees.</li>
  <li><strong>Watch for many-to-many joins</strong> that double-count values, such as joining deals to contacts when a deal has several contacts.</li>
</ul>

<h2 id="clean-data">3. Clean data at the source, not in the dashboard</h2>
<p>It is tempting to fix messy values with formulas in Analytics. That works until the next report, which needs the same fix. Clean data where it is created instead:</p>
<ul>
  <li>Use picklists instead of free text for region, industry, lead source and product category.</li>
  <li>Make fields mandatory at the stage where they become known, using layout rules or Blueprint.</li>
  <li>Deduplicate accounts and contacts in the CRM.</li>
  <li>Standardize dates, currencies and units across systems.</li>
</ul>
<p>When a value can only be fixed in Analytics, add a clearly named formula column and document it, so the next person understands where the number comes from.</p>

<h2 id="define-metrics">4. Define your metrics in writing</h2>
<p>&ldquo;Revenue&rdquo; can mean bookings, invoiced amount or cash received. &ldquo;Active customer&rdquo; can mean bought this year or has an open subscription. AI tools cannot resolve that ambiguity for you.</p>
<p>Write a one-page glossary of your key metrics, with the exact table, filter and formula behind each. Then build those definitions as query tables or aggregate formulas in Analytics and use them everywhere. Natural-language questions become far more reliable when the underlying columns have clear names and consistent meanings.</p>

<h2 id="security">5. Secure the data before sharing it</h2>
<ul>
  <li><strong>Share dashboards, not raw tables,</strong> with most users.</li>
  <li><strong>Use user filters</strong> (row-level security) so sales reps or regional managers only see their own data.</li>
  <li><strong>Review who has workspace admin rights</strong> regularly, especially when people change roles.</li>
  <li><strong>Be deliberate about AI access</strong> to sensitive data such as salaries or customer personal information, and follow your data-protection obligations in each country you operate in.</li>
</ul>

<h2 id="ai-features">6. Then use the AI features</h2>
<p>With the foundation in place, Zoho Analytics&rsquo; AI features become useful:</p>
<ul>
  <li><strong>Ask Zia</strong> answers natural-language questions with charts, which is ideal for quick questions that don&rsquo;t justify a new report.</li>
  <li><strong>Zia Insights</strong> generates plain-language summaries of a chart, such as the biggest contributors to a change.</li>
  <li><strong>Forecasts and anomaly detection</strong> highlight trends and unusual movements worth investigating.</li>
</ul>
<p>Two things are worth knowing in late 2026. Zoho now describes Ask Zia as an AI agent that can create reports and dashboards and suggest actions, and its pricing page lists the LLM-powered version on the Premium and Enterprise plans only. Zoho Analytics also has an MCP Server, so an outside AI assistant can query the same workspace. Both make the earlier steps matter more: an agent that builds its own reports will use whatever joins and column names it finds. Our <a href="/insights/zoho-mcp-claude-chatgpt/">Zoho MCP guide</a> explains how to give an assistant safe access.</p>
<p>Treat AI answers like a capable new analyst: fast and helpful, but worth checking against a trusted report until you have seen it get things right consistently.</p>

<h2 id="checklist">A one-week starter checklist</h2>
<ol>
  <li>List the five questions leadership asks most often.</li>
  <li>Identify the systems and fields that answer each one.</li>
  <li>Connect those sources with native connectors and sensible sync schedules.</li>
  <li>Set up lookups between tables and one customer key.</li>
  <li>Write metric definitions and build them as query tables.</li>
  <li>Build one dashboard that answers the five questions, with user filters.</li>
  <li>Only then, try Ask Zia on the same questions and compare answers.</li>
</ol>
<p>Need help connecting Zoho Analytics to your CRM, Books or other systems? See our <a href="/zoho-integrations/">Zoho integrations</a> service. If you run a factory, our guide to <a href="/insights/zoho-for-manufacturing/">Zoho for manufacturing</a> covers where production data comes from.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('What is Ask Zia in Zoho Analytics?',
         'Ask Zia is the AI assistant in Zoho Analytics. You type a question such as "revenue by region last quarter" and it builds a chart or table from your data. Zoho lists the LLM-powered Ask Zia agent on its Premium and Enterprise plans. Its accuracy depends on clean, well-named and correctly joined data.'),
        ('How do I combine Zoho CRM and Zoho Books data in Zoho Analytics?',
         'Connect both apps with their native connectors, then define lookup relationships between related tables, ideally on a shared customer ID. Reports can then blend deals, invoices and payments, and query tables can hold shared metric definitions.'),
        ('How often does Zoho Analytics sync data?',
         'Native connectors sync on a schedule you choose, up to the limit of your plan. At the time of writing, Zoho lists a data refresh rate of once a day on the Basic plan, 8 times a day on Standard and Premium, and 24 times a day on Enterprise. Many teams sync sales data several times a day and accounting data daily.'),
    ],
))

# ------------------------------------------------------------------ Hiring guide (merged rewrite)
ARTICLES.append(dict(
    slug='zoho-partner-software-development',
    title='How to Choose a Zoho Development Partner or Developer: A Buyer&rsquo;s Checklist',
    seo_title='How to Choose a Zoho Developer or Zoho Partner: Buyer’s Checklist (2026)',
    description='What the Zoho Partner program means, when an independent Zoho developer is a better fit, the questions to ask before hiring, red flags to watch for and what your contract should cover.',
    lead='Choosing who builds your Zoho system matters more than which edition you buy. A good developer saves you money for years; a poor one leaves you with automations nobody understands. This checklist is what we would want a client to ask us.',
    category='Buying guide', keyword='how to choose a zoho developer',
    published='2026-09-15', modified='2026-10-08',
    cover_alt='A hiring checklist on a clipboard with items for experience, references, ownership and documentation',
    caption='A short checklist protects you from the most common problems in Zoho projects.',
    related=['zoho-crm-implementation-cost', 'zoho-creator-vs-power-apps', 'migrate-hubspot-salesforce-to-zoho-crm'],
    body='''
<p>Search for &ldquo;Zoho developer&rdquo; and you will find official Zoho Partners, specialist agencies, freelancers on marketplaces and generalist IT firms that &ldquo;also do Zoho&rdquo;. All of them can be the right choice. This guide helps you tell which one is right for your project.</p>
<p>A note on transparency: Zudo Works has applied to the Zoho Partner program and the application is in progress. Until it is approved we do not describe ourselves as a Zoho Partner. Our CTO, Arunkumar V, received the &ldquo;Master of Creator (Global Winner)&rdquo; award at the Zoho Creator Partner Hackathon 2025. We mention this so you can weigh our advice accordingly.</p>

<h2 id="partner-vs-developer">Zoho Partner, developer or agency: what&rsquo;s the difference?</h2>
<p><strong>Zoho Partners</strong> are companies in Zoho&rsquo;s official partner program. Partners can resell Zoho licences, are listed in Zoho&rsquo;s partner directory, and have met Zoho&rsquo;s requirements for their partner level. That is a useful signal of commitment to the platform.</p>
<p><strong>Independent Zoho developers and agencies</strong> build on Zoho without being in the partner program. Many are highly skilled, particularly in Deluge, Zoho Creator and integrations. You buy licences from Zoho directly and pay the developer only for their work.</p>
<p>Neither label guarantees quality. What matters is relevant experience, clear communication and how they hand the system over to you.</p>

<h2 id="what-you-need">Start with what you actually need</h2>
<ul>
  <li><strong>Configuration</strong> (fields, layouts, pipelines, standard automation): many Zoho admins and partners can do this well.</li>
  <li><strong>Custom logic</strong> (Deluge functions, complex Blueprint, scheduled jobs): you need someone who writes and maintains code.</li>
  <li><strong>Custom apps</strong> on Zoho Creator: look for real Creator projects, not just CRM experience.</li>
  <li><strong>Integrations</strong> with non-Zoho systems: look for API and middleware experience beyond Zoho Flow.</li>
  <li><strong>Custom software</strong> outside Zoho: you need a team that also builds web applications.</li>
</ul>
<p>Matching the provider to the type of work avoids both overpaying for simple setup and underpaying for complex builds.</p>

<h2 id="questions">Ten questions to ask before you hire</h2>
<ol>
  <li><strong>What have you built that is similar to our project?</strong> Ask for a walkthrough, screenshots or a demo, not just a list of logos.</li>
  <li><strong>Who will actually do the work?</strong> Make sure the person in the sales call is either the builder or works closely with them.</li>
  <li><strong>Which Zoho apps and editions have you worked with?</strong> Feature availability differs by edition; experienced developers know where the limits are.</li>
  <li><strong>How do you handle data migration?</strong> Listen for test imports, legacy ID fields and record-count checks.</li>
  <li><strong>How will you document what you build?</strong> You want a list of modules, fields, automations and functions, and what each one does.</li>
  <li><strong>Who owns the code and configuration?</strong> It should be you, in your own Zoho account.</li>
  <li><strong>How do you test?</strong> A sandbox or test records, and a sign-off step before go-live.</li>
  <li><strong>What happens after launch?</strong> Ask about support, response times and how small changes are billed.</li>
  <li><strong>How do you price?</strong> Hourly, fixed price or a mix, and what is excluded.</li>
  <li><strong>Can we speak to a past client or see reviews?</strong> Independent reviews on platforms such as Clutch or Upwork are hard to fake.</li>
</ol>

<h2 id="red-flags">Red flags</h2>
<ul>
  <li>They want the Zoho account in their name, or ask you to pay licences through them without a clear reason.</li>
  <li>They cannot explain their approach in plain language.</li>
  <li>No mention of documentation, testing or training.</li>
  <li>A fixed price with no written scope.</li>
  <li>They promise everything is possible &ldquo;out of the box&rdquo; without asking about your process.</li>
  <li>They claim partner status, certifications or client results they cannot show you. A real partner can point you to their listing in Zoho&rsquo;s partner directory.</li>
</ul>

<h2 id="contract">What your agreement should cover</h2>
<ul>
  <li><strong>Scope:</strong> modules, automations, integrations, data migration and reports included.</li>
  <li><strong>Deliverables:</strong> documentation, training sessions and an admin handover.</li>
  <li><strong>Ownership:</strong> all configuration, code and data belong to you; admin access stays with you.</li>
  <li><strong>Timeline and milestones</strong> with review points.</li>
  <li><strong>Price and payment terms,</strong> including how change requests are handled.</li>
  <li><strong>Support after launch:</strong> what is included and for how long. We include one month of free support and onboarding after every build.</li>
  <li><strong>Confidentiality and data protection,</strong> especially if you operate in the UK, EU or Australia.</li>
</ul>

<h2 id="pricing">What should it cost?</h2>
<p>Rates vary widely by country and type of provider. What you can compare is the estimated hours for the same scope and what is included. Our <a href="/insights/zoho-crm-implementation-cost/">Zoho CRM cost guide</a> shows typical effort for three project sizes, and our <a href="/pricing/">pricing page</a> shows how we charge: US$15 per hour, or a fixed price for defined projects.</p>

<h2 id="next-steps">Next steps</h2>
<p>Write a one-page brief: what you want to change, who will use the system, which tools it must connect to and when you need it. Send the same brief to two or three providers and compare how they respond. The quality of their questions usually tells you more than their proposal.</p>
<p>If you would like us to be one of them, <a href="/contact/">get in touch</a> or see our <a href="/work/">project experience</a>.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Do I need an official Zoho Partner to implement Zoho?',
         'No. Partners can resell licences and are vetted by Zoho, which is a useful signal, but independent Zoho developers and agencies also build high-quality systems. Judge providers on relevant experience, documentation, testing and support.'),
        ('Is Zudo Works a Zoho Partner?',
         'Our Zoho Partner application is in progress. Until it is approved we do not describe ourselves as a Zoho Partner. Our CTO, Arunkumar V, received the "Master of Creator (Global Winner)" award at the Zoho Creator Partner Hackathon 2025.'),
        ('Who should own the Zoho account?',
         'You should. Keep the subscription and the super-admin account in your company\'s name, and give your developer an admin user. That way you keep control of your data and configuration if you change providers.'),
    ],
))

# ------------------------------------------------------------------ Zoho Partner Program explainer
ARTICLES.append(dict(
    slug='zoho-partner-program-explained',
    title='Zoho Partner Program Explained: Authorized, Advanced and Premium Partners',
    seo_title='Zoho Partner Program: Authorized, Advanced and Premium Partners (2026)',
    description='What an authorized Zoho partner is, how Zoho ranks Authorized, Advanced and Premium partners, how to verify a partner and when an independent Zoho developer fits better.',
    lead='Search for a Zoho partner and you will see dozens of firms calling themselves authorized, certified or premium. This guide explains what those labels actually mean in Zoho&rsquo;s program, how to check them in two minutes, and how to decide what kind of help your project needs.',
    category='Buying guide', keyword='zoho partner',
    published='2026-10-08', modified='2026-10-08',
    cover_alt='A card showing the three Zoho partner tiers, Authorized, Advanced and Premium, beside a directory search for verifying a partner',
    caption='Zoho ranks consulting partners in three tiers and lists them in its Find a Partner directory.',
    related=['zoho-partner-software-development', 'zoho-crm-implementation-cost', 'zoho-creator-vs-power-apps'],
    body='''
<p>&ldquo;Zoho partner&rdquo; is one of the most searched phrases by businesses about to implement Zoho CRM, Zoho Creator or Zoho One. It is also one of the most loosely used. Some firms are listed partners in Zoho&rsquo;s official program, some have certifications but no partner listing, and some simply describe themselves as a &ldquo;Zoho partner&rdquo; in the everyday sense of the word.</p>
<p>The requirements below come from Zoho&rsquo;s own <a href="https://www.zoho.com/partners/partner-tiers.html" rel="noopener" target="_blank">partner tiers page</a>, checked in October 2026. Zoho reviews its program from time to time, so confirm the current rules there before you rely on them.</p>
<p>A note on transparency: Zudo Works has applied to the Zoho Partner program and the application is in progress. Until it is approved we do not describe ourselves as a Zoho Partner. That is exactly why we wrote this guide: you should be able to check any provider&rsquo;s claim, including ours.</p>

<h2 id="what-is">What is a Zoho partner?</h2>
<p>A Zoho partner is a company that has joined Zoho&rsquo;s partner program to sell, implement and support Zoho products. Partners can resell Zoho licences, are trained and certified on Zoho products and, once they reach the Authorized tier, can be listed in Zoho&rsquo;s official <a href="https://www.zoho.com/partners/find-zoho-partner.html" rel="noopener" target="_blank">Find a Partner</a> directory.</p>
<p>Being a partner is a commercial relationship with Zoho. It tells you the firm has met Zoho&rsquo;s requirements; it does not, on its own, tell you whether they are the right fit for your specific project.</p>

<h2 id="tiers">Zoho partner tiers: Authorized, Advanced and Premium</h2>
<p>Zoho ranks its consulting partners in three public tiers. New partners start in an onboarding stage and must qualify for the first tier.</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Tier</th><th scope="col">What Zoho requires</th><th scope="col">What it tells you</th></tr></thead>
  <tbody>
    <tr><th scope="row">Authorized</th><td>Reach a US$5,000 revenue threshold, obtain the required certifications and show implementation success within six months of onboarding</td><td>The firm is active, certified and has delivered projects. Authorized is the minimum tier for a directory listing.</td></tr>
    <tr><th scope="row">Advanced</th><td>A value score above 400 points (out of 1,000)</td><td>Consistent licence sales, customer results and certified staff</td></tr>
    <tr><th scope="row">Premium</th><td>A value score above 600 points (out of 1,000)</td><td>Zoho&rsquo;s highest tier: larger practices with strong sales and customer metrics</td></tr>
  </tbody>
</table>
</div>
<p>Partners who do not meet the Authorized criteria within six months may be re-evaluated or removed from the program. Tiers are reassessed every year, and updated tiers take effect by January of the following year.</p>

<h2 id="value-score">How Zoho scores its partners</h2>
<p>The value score behind the Advanced and Premium tiers has four parts, with a maximum of 1,000 points:</p>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">What is measured</th><th scope="col">Maximum points</th></tr></thead>
  <tbody>
    <tr><th scope="row">Revenue</th><td>Year-on-year growth in Zoho licensing revenue (up to 400) and new customers (up to 100)</td><td>500</td></tr>
    <tr><th scope="row">Customer success</th><td>Customer retention (up to 100) and customer satisfaction ratings (up to 100), with points deducted for validated escalations</td><td>200</td></tr>
    <tr><th scope="row">Market readiness</th><td>Zoho certifications (up to 100), qualifying project scope documents or marketplace integrations (up to 50) and Zoho-approved case studies (up to 50)</td><td>200</td></tr>
    <tr><th scope="row">Zoho engagement</th><td>Size of the Zoho sales practice (up to 25) and Zoho-related campaigns and branding (up to 75)</td><td>100</td></tr>
  </tbody>
</table>
</div>
<p>Half of the available points relate to licence revenue and customer numbers. In practice, a higher tier usually means a bigger Zoho sales practice. It is a useful signal of scale and commitment, but it is not a direct measure of technical depth in Deluge, Zoho Creator or custom integrations.</p>

<h2 id="verify">How to verify an authorized Zoho partner in two minutes</h2>
<ol>
  <li><strong>Search the official directory.</strong> Open Zoho&rsquo;s <a href="https://www.zoho.com/partners/find-zoho-partner.html" rel="noopener" target="_blank">Find a Partner</a> page and search for the company by name or filter by country. Authorized, Advanced and Premium partners with an approved profile are listed there with their tier.</li>
  <li><strong>Ask for their partner profile link.</strong> A genuine partner can send it immediately. Check that the company name and country match the firm you are talking to.</li>
  <li><strong>Check the wording.</strong> &ldquo;Zoho Certified&rdquo; usually refers to individual certifications, which are useful but not the same as partner status. &ldquo;Zoho Partner&rdquo; without a tier or directory listing is worth a follow-up question.</li>
  <li><strong>Ask which products they are certified on.</strong> A CRM-focused partner may have little Zoho Creator or Zoho Books experience, and the reverse.</li>
  <li><strong>Ask for similar work.</strong> Whatever the label, ask for a walkthrough of a project like yours.</li>
</ol>

<h2 id="by-country">Finding a Zoho partner in your country</h2>
<p>The Find a Partner directory can be filtered by country, which helps if you need on-site workshops, invoicing in your currency or a provider who knows local tax rules. For most projects, though, Zoho implementation is delivered remotely: workshops, configuration, data migration and training all happen over video calls and screen sharing.</p>
<ul>
  <li><strong>India:</strong> Zoho was founded and is headquartered in Chennai, and India has a large community of Zoho providers in Delhi NCR, Mumbai, Bengaluru, Hyderabad, Pune, Chennai and beyond. See <a href="/locations/india/">Zoho consultants in India</a>.</li>
  <li><strong>United States:</strong> providers are spread across every state; time-zone overlap matters more than city. See <a href="/locations/united-states/">Zoho consultants for the United States</a>.</li>
  <li><strong>United Kingdom:</strong> check experience with UK GDPR, VAT and Making Tax Digital if you use Zoho Books. See <a href="/locations/united-kingdom/">Zoho consultants for the UK</a>.</li>
  <li><strong>Australia and New Zealand:</strong> check GST setup in Zoho Books and experience with Xero, which many businesses there use. See <a href="/locations/australia/">Australia</a> and <a href="/locations/new-zealand/">New Zealand</a>.</li>
  <li><strong>Europe and elsewhere</strong> (for example the Czech Republic, Germany, the Middle East or Southeast Asia): look for experience with your Zoho data centre and local requirements. See <a href="/locations/">all countries we work with</a>.</li>
</ul>

<h2 id="resellers">Zoho resellers vs implementation partners</h2>
<p>Many partners do both, but they are different jobs:</p>
<ul>
  <li><strong>Reselling</strong> means selling you Zoho licences. You can also buy licences directly from Zoho.</li>
  <li><strong>Implementation</strong> means designing and building your system: modules, fields, Blueprint, Deluge functions, integrations, data migration and training.</li>
</ul>
<p>Whoever you buy licences from, keep the Zoho account and its super-admin login in your own company&rsquo;s name. Ask a reseller who owns the account, how billing works and what happens if you change provider later.</p>

<h2 id="partner-or-developer">Do you need a Zoho partner or a Zoho developer?</h2>
<ul>
  <li><strong>Choose a listed partner</strong> when you want to buy licences and services from one firm, need a large multi-team rollout, or your procurement rules require a vendor with an official Zoho status.</li>
  <li><strong>An independent Zoho developer or team can fit better</strong> when most of the work is custom: Zoho Creator apps, Deluge functions, integrations with non-Zoho systems or custom software around Zoho.</li>
  <li><strong>Many businesses use both:</strong> licences directly from Zoho or through a partner, and a specialist developer for the custom build.</li>
</ul>
<p>Our <a href="/insights/zoho-partner-software-development/">checklist for choosing a Zoho development partner</a> lists the ten questions to ask any provider, and the red flags to watch for.</p>

<h2 id="zudo-works">Where Zudo Works fits</h2>
<p>We are an independent Zoho development team based in Chennai, India, working with businesses in the United States, United Kingdom, Australia, New Zealand and India. Our Zoho Partner application is in progress. Our CTO, Arunkumar V, received the &ldquo;Master of Creator (Global Winner)&rdquo; award from Zoho Creator at the Zoho Creator Partner Hackathon 2025. We charge US$15 per hour, quote fixed prices for defined projects, and include one month of free support and onboarding after every build. You buy your Zoho licences directly from Zoho, in your own name.</p>
<p>See our <a href="/zoho-development/">Zoho development services</a>, <a href="/work/">past project work</a> or <a href="/pricing/#calculator">estimate your project cost</a>.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('What is an authorized Zoho partner?',
         'An Authorized Zoho Partner is a company in the first tier of Zoho\'s partner program. To qualify, a partner must reach a US$5,000 revenue threshold, obtain the required certifications and show implementation success within six months of onboarding. Authorized partners with an approved profile are listed in Zoho\'s Find a Partner directory.'),
        ('What is the difference between Authorized, Advanced and Premium Zoho partners?',
         'They are Zoho\'s three partner tiers. Authorized is the entry tier. Advanced partners score more than 400 points and Premium partners more than 600 points out of 1,000 in Zoho\'s annual value scoring, which measures licence revenue, customer success, certifications and engagement with Zoho.'),
        ('How do I verify a Zoho partner?',
         'Search for the company in Zoho\'s official Find a Partner directory at zoho.com/partners, or ask the firm for its partner profile link. Check that the name, country and tier match. "Zoho Certified" usually refers to individual certifications rather than partner status.'),
        ('How does a company become a Zoho partner?',
         'A company applies to Zoho\'s partner program and, after onboarding, must reach the Authorized tier requirements within six months: a US$5,000 revenue threshold, the required certifications and successful implementations. Tiers are then reviewed every year.'),
        ('Is Zudo Works a Zoho Partner?',
         'Our Zoho Partner application is in progress, so we do not describe ourselves as a Zoho Partner. We are an independent Zoho development team. Our CTO, Arunkumar V, received the "Master of Creator (Global Winner)" award from Zoho Creator at the Zoho Creator Partner Hackathon 2025.'),
    ],
))

# ------------------------------------------------------------------ Zoho for manufacturing
ARTICLES.append(dict(
    slug='zoho-for-manufacturing',
    title='Does Zoho Have Manufacturing Software? Zoho ERP, Inventory and Creator Compared',
    seo_title='Zoho for Manufacturing: ERP, Inventory, Creator',
    description='What Zoho actually offers a manufacturer: assemblies in Zoho Inventory, the manufacturing module in Zoho ERP, and custom apps on Zoho Creator, plus when dedicated MRP software is the better choice.',
    lead='Manufacturers ask one question about Zoho more than any other: can it run production? The answer depends on which Zoho product you mean, and the three options are very different. This guide separates them, using Zoho&rsquo;s own documentation.',
    category='Manufacturing', keyword='zoho for manufacturing',
    published='2026-10-09', modified='2026-10-09',
    cover_alt='Three Zoho routes for a manufacturer: Zoho Inventory for simple assembly, Zoho ERP for bills of materials and job cards, and Zoho Creator for custom processes',
    caption='Zoho gives a manufacturer three routes. They suit different factories, and one of them is sold only in India today.',
    related=['zoho-flow-vs-deluge', 'zoho-creator-vs-power-apps', 'zoho-analytics-agentic-data-foundations-2026'],
    body='''
<p>Search for &ldquo;Zoho for manufacturing&rdquo; and you will find confident answers that contradict each other. Some say Zoho has no production features at all. Others describe a full manufacturing ERP. Both are describing a real product, just not the same one.</p>
<p>Zoho has three separate ways to support production. Everything below was checked against Zoho&rsquo;s product pages and help documentation in October 2026. Where Zoho does not state something, we say so.</p>

<h2 id="short-answer">The short answer</h2>
<ul>
  <li><strong>Zoho Inventory</strong> handles simple assembly: it turns components into a finished item and adjusts stock. Zoho&rsquo;s own knowledge base says it does not yet have a manufacturing module.</li>
  <li><strong>Zoho ERP</strong> is a separate product with a real manufacturing module: bills of materials, manufacturing orders, job cards, a shop floor view, work centers, subcontracting and quality inspections. Zoho launched it in India in January 2026 and it is not part of Zoho One.</li>
  <li><strong>Zoho Creator</strong> is a low-code platform. You can build production tracking, quality or maintenance apps around your own process, or a planning system of your own. Nothing is ready-made; it is built for you.</li>
</ul>

<h2 id="three-routes">The three routes at a glance</h2>
<div class="table-wrap">
<table>
  <thead><tr><th scope="col">Area</th><th scope="col">Zoho Inventory</th><th scope="col">Zoho ERP</th><th scope="col">Zoho Creator</th></tr></thead>
  <tbody>
    <tr><th scope="row">What it is</th><td>Stock and order management</td><td>A full ERP with finance, supply chain, payroll and manufacturing</td><td>A low-code platform for custom apps</td></tr>
    <tr><th scope="row">Bill of materials</th><td>A component list on an assembly item</td><td>A Bill of Materials module, including subcontract BOMs</td><td>Whatever you design</td></tr>
    <tr><th scope="row">Production orders</th><td>An assembly record that consumes components</td><td>Manufacturing orders with job cards and operations</td><td>Whatever you design</td></tr>
    <tr><th scope="row">Shop floor and work centers</th><td>No</td><td>Yes: shop floor, work centers and work center timings</td><td>Built to order, for example shift logs or job tracking</td></tr>
    <tr><th scope="row">Quality checks</th><td>No</td><td>Quality templates, rules and inspections</td><td>Built to order, for example NCR and CAPA</td></tr>
    <tr><th scope="row">Where it is sold</th><td>Globally; plans vary by country</td><td>Published for India at the time of writing</td><td>Globally</td></tr>
    <tr><th scope="row">In Zoho One?</th><td>Yes</td><td>No, it is a separate product</td><td>Yes</td></tr>
    <tr><th scope="row">Effort to start</th><td>Low</td><td>An ERP implementation</td><td>A custom build</td></tr>
  </tbody>
</table>
</div>
<p>Plans and limits change, so confirm them on the official pricing pages for <a href="https://www.zoho.com/inventory/pricing/" target="_blank" rel="noopener">Zoho Inventory</a>, <a href="https://www.zoho.com/en-in/erp/pricing/" target="_blank" rel="noopener">Zoho ERP</a> and <a href="https://www.zoho.com/creator/pricing.html" target="_blank" rel="noopener">Zoho Creator</a>.</p>

<figure style="margin:2rem auto;max-width:420px">
<svg viewBox="0 0 360 400" role="img" aria-labelledby="mfg-flow-title mfg-flow-desc" style="width:100%;height:auto;display:block;font-family:Inter,sans-serif">
  <title id="mfg-flow-title">Where each Zoho app fits in a make-to-order flow</title>
  <desc id="mfg-flow-desc">Five steps from top to bottom. Quote: Zoho CRM. Sales order: Zoho Inventory or Zoho ERP. Materials: Zoho Inventory or Zoho ERP. Production: Zoho ERP or a Zoho Creator app. Dispatch and invoice: Zoho Inventory and Zoho Books, or Zoho ERP.</desc>
  <style>
    .mf-dot{animation:mf-move 7s linear infinite}
    @keyframes mf-move{0%{transform:translateY(0);opacity:0}6%{opacity:1}94%{opacity:1}100%{transform:translateY(320px);opacity:0}}
    @media (prefers-reduced-motion: reduce){.mf-dot{animation:none;opacity:0}}
  </style>
  <line x1="28" y1="40" x2="28" y2="360" stroke="#C9DCEF" stroke-width="3" stroke-linecap="round"/>
  <g font-size="15" font-weight="700" fill="#1A1A2E">
    <text x="56" y="36">1. Quote</text>
    <text x="56" y="116">2. Sales order</text>
    <text x="56" y="196">3. Materials</text>
    <text x="56" y="276">4. Production</text>
    <text x="56" y="356">5. Dispatch and invoice</text>
  </g>
  <g font-size="13" fill="#4B5563">
    <text x="56" y="56">Zoho CRM</text>
    <text x="56" y="136">Zoho Inventory or Zoho ERP</text>
    <text x="56" y="216">Zoho Inventory or Zoho ERP</text>
    <text x="56" y="296">Zoho ERP, or a Zoho Creator app</text>
    <text x="56" y="376">Inventory and Books, or Zoho ERP</text>
  </g>
  <g fill="#fff" stroke="#226DB4" stroke-width="3">
    <circle cx="28" cy="40" r="9"/><circle cx="28" cy="120" r="9"/><circle cx="28" cy="200" r="9"/>
    <circle cx="28" cy="280" r="9" stroke="#E07A0F"/><circle cx="28" cy="360" r="9"/>
  </g>
  <circle class="mf-dot" cx="28" cy="40" r="5" fill="#226DB4"/>
</svg>
<figcaption style="font-size:.875rem;color:#6B7280;text-align:center;margin-top:.75rem">Step 4 is the one to examine. The other four are standard Zoho.</figcaption>
</figure>

<h2 id="zoho-inventory">Route 1: Zoho Inventory, for simple assembly</h2>
<p>Zoho Inventory has <strong>composite items</strong> in two types. An <em>assembly</em> (formerly called a bundle) is for physically building one item from components: when you create the assembly, component stock goes down and the finished item gets its own stock. A <em>kit</em> groups existing items for sale without any assembly work. A composite item can contain another composite item, and a service such as labour can be one of the components, though not the only one.</p>
<p>That is enough for a business that packs sets, assembles a product from a fixed list of parts or does light finishing. It is not production management. Zoho says so directly: its knowledge base article on the subject states that Zoho Inventory does not yet support manufacturing modules, and suggests composite items as a workaround for basic assemblies that do not need a bill of materials.</p>
<p>This route has no work orders that move through stages, no routing, no capacity planning and no material requirements planning. Serial and batch tracking and bin locations depend on the plan.</p>
<p><strong>Choose it when</strong> your &ldquo;production&rdquo; is one step, takes minutes or hours, and you mainly need accurate stock and costs.</p>

<h2 id="zoho-erp">Route 2: Zoho ERP, a real manufacturing module</h2>
<p><a href="https://www.zoho.com/en-in/erp/" target="_blank" rel="noopener">Zoho ERP</a> is the product many older articles do not know about. Zoho launched it in India in January 2026 as a single system for finance, supply chain, billing, payroll and spending, with purpose-built versions for manufacturing, distribution, retail and non-profits.</p>
<p>Its help documentation has full sections for the things Zoho Inventory lacks:</p>
<ul>
  <li><strong>Bill of Materials,</strong> including creating a manufacturing order straight from a BOM.</li>
  <li><strong>Manufacturing orders</strong> with job cards, operations and a manufacturing dashboard.</li>
  <li><strong>Shop floor</strong> screens and shop floor staff, with work centers, work center types and timings.</li>
  <li><strong>Subcontract manufacturing:</strong> subcontract BOMs, subcontract orders, purchase orders and material transfers.</li>
  <li><strong>Quality:</strong> templates, rules, inspections and inspection worklists.</li>
</ul>
<p>The product is moving quickly. Zoho&rsquo;s 2026 update notes list a work center calendar, manufacturing orders created from sales orders and quality inspections on purchase receipts. Some newer features are in early access or limited to higher plans.</p>
<p>Three limits matter before you plan around it:</p>
<ol>
  <li><strong>Availability.</strong> At the time of writing, Zoho&rsquo;s ERP site, its rupee pricing and its tax and payroll features are published for India. We could not find an announced date for other countries. If you are outside India, ask Zoho first.</li>
  <li><strong>It is not in Zoho One.</strong> Zoho&rsquo;s pricing page states this plainly. Zoho ERP is licensed separately, per user, and each plan has a yearly cap on transactions.</li>
  <li><strong>It is an ERP project.</strong> Moving finance, stock and production into one system needs data migration, opening balances, process design and training.</li>
</ol>
<p><strong>Choose it when</strong> you are in India, you want finance and production in one Zoho system, and your process fits a standard BOM, job card and work center model.</p>

<h2 id="zoho-creator">Route 3: Zoho Creator, built around your process</h2>
<p>Zoho Creator is a low-code platform: forms, a database, workflows, Deluge scripts, mobile apps and portals. It contains no manufacturing logic until someone builds it.</p>
<p>Zoho&rsquo;s own manufacturing page for Creator is careful about this. It describes Creator as a digital extension layer that sits beside a core system such as SAP, Oracle, Infor or NetSuite, with that system remaining the source of records. The examples it gives are the processes ERPs handle poorly: safety and near-miss reports, purchase requisitions, shift handover logs, permits and gate passes, engineering change requests, vendor onboarding, quality NCR and CAPA, and maintenance breakdowns. Zoho also has a page about building a material requirements planning solution on Creator, and that too is something you design, not a product you switch on.</p>
<p>So Creator fits two situations well:</p>
<ul>
  <li><strong>Beside an ERP or an accounting system,</strong> to digitize the paper, spreadsheet and WhatsApp processes around production.</li>
  <li><strong>As the production system for a specific process</strong> that standard software models badly, for example job work with customer-supplied material, made-to-measure products or a multi-stage process with its own approvals.</li>
</ul>
<p>The cost is the build and its upkeep. An app that tracks jobs through stages is a contained project. A full planning engine with scheduling and capacity is a serious software project, and should be compared honestly with buying one. Our <a href="/zoho-creator-development/">Zoho Creator development</a> page explains how we scope this kind of build, and <a href="/insights/zoho-creator-vs-power-apps/">Zoho Creator vs Power Apps</a> compares it with Microsoft&rsquo;s platform.</p>
<p><strong>Choose it when</strong> your process is the unusual part, or when you already have a system of record and need the workflows around it.</p>

<h2 id="around-production">What Zoho covers well around production</h2>
<p>Most of a manufacturer&rsquo;s software is not production software, and this is where Zoho is strongest:</p>
<ul>
  <li><strong>Zoho CRM</strong> for enquiries, quotes, dealers and distributors, samples and repeat orders, with custom modules where a standard pipeline does not fit.</li>
  <li><strong>Zoho Books</strong> for invoicing, purchases and tax, linked to Zoho Inventory for stock.</li>
  <li><strong>Zoho Analytics</strong> for dashboards that combine sales, stock, purchase and production data. The same rules apply as in our guide to <a href="/insights/zoho-analytics-agentic-data-foundations-2026/">building a data foundation in Zoho Analytics</a>.</li>
  <li><strong>Zoho IoT,</strong> a separate low-code platform that Zoho positions for machine monitoring, predictive maintenance and energy tracking.</li>
</ul>
<p>Connecting these to a non-Zoho production system is an integration job; our guide to <a href="/insights/zoho-flow-vs-deluge/">Zoho Flow, Deluge and custom middleware</a> explains which tool suits which integration.</p>

<h2 id="dedicated-mrp">When dedicated manufacturing software is the better choice</h2>
<p>If scheduling and planning are the hard part of your business, look at software built for exactly that. These are fair descriptions taken from each vendor&rsquo;s own site:</p>
<ul>
  <li><strong>MRPeasy</strong> describes itself as MRP software for small manufacturers and says it is ideal for companies with 10 to 200 employees. It covers production planning, inventory, sales, procurement and finances.</li>
  <li><strong>Odoo Manufacturing</strong> offers an MRP scheduler that plans work at each work center by capacity, tablets on the shop floor, automatic quality checks, maintenance requests and product lifecycle management.</li>
  <li><strong>ERPNext</strong> is open-source ERP with multi-level BOMs, work orders, job cards, production planning, subcontracting and capacity planning.</li>
  <li><strong>Katana</strong> offers bills of materials with subassemblies, a shop floor app and tracking of outsourced production, aimed at small and mid-sized product businesses.</li>
  <li><strong>TranZact</strong> is built for Indian MSME manufacturers and says it works alongside systems such as Tally.</li>
</ul>
<p>Choosing one of these does not rule Zoho out. A common and sensible design is a dedicated MRP for production, with Zoho CRM in front for sales and Zoho Analytics on top for reporting.</p>

<h2 id="how-to-decide">How to decide: five questions</h2>
<ol>
  <li><strong>How many steps does production have?</strong> One step points to Zoho Inventory. Several operations across machines or people points to Zoho ERP or dedicated MRP.</li>
  <li><strong>Do you need scheduling and capacity planning,</strong> or only tracking of what was made and what it consumed?</li>
  <li><strong>Where are you?</strong> Zoho ERP is an option today in India. Elsewhere, plan around Zoho Inventory, Creator or a dedicated product.</li>
  <li><strong>Which system holds the accounts?</strong> If Tally, SAP or another system stays, you need integration, not replacement.</li>
  <li><strong>How standard is your process?</strong> The more unusual it is, the stronger the case for a Creator app built around it.</li>
</ol>

<h2 id="first-project">A sensible first project</h2>
<p>Whatever you choose for production, start with the part that is safe to change. For most manufacturers that is the front office: enquiries, quotes and order follow-up in Zoho CRM, with stock and invoicing connected. It shows quickly whether your team will use the system, and it does not touch the shop floor.</p>
<p>Then map production on paper before choosing software for it: every stage, who records what, and which numbers you need at the end of the day. That page usually makes the choice between the three routes clear. To size the work, <a href="/pricing/#calculator">estimate your project</a>.</p>

<h2 id="faq">Frequently asked questions</h2>
''',
    faqs=[
        ('Does Zoho have an MRP or manufacturing module?',
         'Zoho ERP has a manufacturing module with bills of materials, manufacturing orders, job cards, shop floor screens, work centers, subcontract manufacturing and quality inspections. Zoho launched it in India in January 2026. Zoho Inventory does not have a manufacturing module; it offers assemblies and kits through composite items.'),
        ('Does Zoho Inventory have a bill of materials?',
         'Not as a separate module. An assembly in Zoho Inventory has a list of components that are consumed when the finished item is built, which works for simple, single-step assembly. Zoho\'s knowledge base says manufacturing modules are not yet supported in Zoho Inventory.'),
        ('Is Zoho ERP included in Zoho One?',
         'No. Zoho\'s ERP pricing page states that Zoho ERP is not included in Zoho One. It is a separate product with its own per-user plans.'),
        ('Is Zoho ERP available outside India?',
         'At the time of writing, Zoho\'s ERP website, pricing and tax features are published for India, and we could not find an announced date for other countries. Check with Zoho for your country before planning around it.'),
        ('Can Zoho Creator be used as a manufacturing ERP?',
         'It can be built into one, but nothing is ready-made. Zoho positions Creator for manufacturers as an extension layer beside a core system, for processes such as quality NCR and CAPA, maintenance, shift handover and engineering changes. A full planning and scheduling engine on Creator is a substantial custom build.'),
    ],
))
