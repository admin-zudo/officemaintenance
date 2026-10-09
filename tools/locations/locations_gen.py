"""Generate the /locations/ hub and one page per country we serve.

Run from the repo root, then run tools/build.py (which injects the shared
head, header and footer, and adds the pages to the sitemap):

    python tools/locations/locations_gen.py
    python tools/build.py

Each country page has its own content (time zones, Zoho data centre, local tax
and accounting tools, past project work) so it is useful to a visitor from that
country, not a copy with the name swapped. Keep partner wording honest: the
Zoho Partner application is in progress, so never call Zudo Works a Zoho Partner.
"""
import html, json, os

SITE = 'https://zudoworks.com'
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OG = SITE + '/Asset/og/zudo-works.jpg'
AWARD = '&ldquo;Master of Creator (Global Winner)&rdquo; award'
PARTNER_GUIDE = '/insights/zoho-partner-program-explained/'
CHOOSE_GUIDE = '/insights/zoho-partner-software-development/'

SERVICES = [
    ('/zoho-creator-development/', 'Zoho Creator development', 'Custom apps, portals, dashboards and mobile apps on Zoho Creator.'),
    ('/zoho-crm-development/', 'Zoho CRM implementation', 'Setup, customization, Blueprint, data migration and training.'),
    ('/deluge-development/', 'Deluge development', 'Functions, automations and fixes across Zoho apps.'),
    ('/zoho-integrations/', 'Zoho integrations', 'Connect Zoho with accounting, e-commerce, payment and in-house systems.'),
    ('/business-process-automation/', 'Business process automation', 'Approvals, notifications and hand-offs that run on their own.'),
    ('/support-maintenance/', 'Support and maintenance', 'Fixes, small changes and improvements after launch.'),
]

PROJECTS = {
    'trakas': ('Trakas Smokers Shop', 'USA &middot; Retail', 'A point-of-sale application and design system integrated with Zoho One, including Zoho CRM, Zoho Books and Zoho Analytics.'),
    'healthcare': ('Healthcare management', 'USA &middot; Healthcare', 'Custom injury-mapping widgets built in JavaScript and SVG, with full create, read, update and delete operations.'),
    'bestaccess': ('Best Access Doors', 'USA', 'Business application work for a US door and access-panel supplier.'),
    'avalon': ('Avalon Care Training', 'UK &middot; Training and education', 'A student management system with portals, automated PDF documents and role-based security.'),
    'asquare': ('A Square Loans', 'India &middot; Lending', 'A financial processing engine and a secure loan-management architecture.'),
}

COUNTRIES = [
    dict(
        slug='india', name='India', label='India', iso='IN',
        title='Zoho Consultants &amp; Developers in India | Zudo Works',
        desc='Chennai-based Zoho consultants and developers for businesses in every Indian state: Zoho CRM, Creator, Books (GST), Deluge and integrations. US$15/hour.',
        h1='Zoho consultants and developers in India',
        lead='Zudo Works is a Zoho development team based in Anna Nagar, Chennai, the city where Zoho itself was founded. We implement and customize Zoho CRM, Zoho Creator, Zoho Books and Zoho One for businesses across India, from Delhi NCR and Mumbai to Bengaluru, Hyderabad and Coimbatore.',
        partner_h='Looking for a Zoho partner in India?',
        partner=[
            'India has hundreds of firms offering Zoho services, and many describe themselves as Zoho partners. Here is exactly where we stand: Zudo Works is an independent Zoho development team. Our Zoho Partner application is in progress, and until it is approved we do not call ourselves a Zoho Partner or an authorized Zoho partner.',
            'If you need a listed partner, for example to buy licences through one, check Zoho&rsquo;s Find a Partner directory. Our guide to the <a href="%s" class="text-link">Zoho Partner Program and its Authorized, Advanced and Premium tiers</a> shows how to verify any partner in two minutes.' % PARTNER_GUIDE,
        ],
        how=[
            ('Same time zone', 'We work Monday to Friday, 9:00 to 18:00 IST, so calls, workshops and support happen in your normal working day. Visitors in India can call or WhatsApp us on +91 63854 35382.'),
            ('Zoho&rsquo;s India data centre', 'Accounts created in India usually run on Zoho&rsquo;s India data centre (zoho.in). We work in whichever data centre your account uses and keep your data in your own account.'),
            ('Books, GST and Tally', 'We set up Zoho Books for Indian GST, including e-invoicing and e-way bill workflows where your business needs them, and plan moves from Tally or spreadsheets with your accountant.'),
        ],
        local_h='Zoho for Indian businesses',
        local=[
            'Typical Zoho projects for Indian businesses combine Zoho CRM with Zoho Books, or replace spreadsheets with a Zoho Creator app for operations, field teams or approvals. Other common needs are WhatsApp notifications from Zoho CRM, payment-gateway links on invoices, dealer and distributor portals, and dashboards that combine sales and accounting data.',
            'We quote in US dollars at US$15 per hour, or a fixed price for defined projects. Zoho licences are billed by Zoho directly to you, in your own company&rsquo;s name.',
        ],
        areas_h='States and union territories we work with',
        areas_intro='We work remotely with businesses in every Indian state and union territory, with workshops and training over video call.',
        areas=[('States', ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']),
               ('Union territories', ['Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Jammu and Kashmir', 'Ladakh', 'Lakshadweep', 'Puducherry'])],
        cities='Chennai, Coimbatore, Madurai, Bengaluru, Hyderabad, Mumbai, Pune, Delhi, Noida, Gurugram, Kolkata, Ahmedabad, Jaipur, Kochi, Lucknow and Chandigarh',
        projects=['asquare'],
        faqs=[
            ('Is Zudo Works an authorized Zoho partner in India?',
             'Not yet. Our Zoho Partner application is in progress, so we do not describe ourselves as a Zoho Partner or an authorized Zoho partner. We are an independent Zoho development team in Chennai. Our CTO, Arunkumar V, received the "Master of Creator (Global Winner)" award from Zoho Creator at the Zoho Creator Partner Hackathon 2025.'),
            ('Do you work with businesses in Delhi, Mumbai and Bengaluru?',
             'Yes. We are based in Chennai and work with businesses in every Indian state and union territory, including Delhi NCR, Mumbai, Bengaluru, Hyderabad and Pune. Workshops, configuration, data migration and training all run over video calls and screen sharing.'),
            ('Can you set up Zoho Books for GST?',
             'Yes. We configure Zoho Books for Indian GST, including tax rates, invoice templates, and e-invoicing and e-way bill workflows where your business needs them, and connect Books with Zoho CRM or Zoho Inventory. We work alongside your accountant on tax decisions.'),
            ('How much does a Zoho developer cost in India?',
             'We charge US$15 per hour. Fixed-price projects are quoted from the estimated days and complexity, and you can get an indicative figure from the calculator on our pricing page. Every build includes one month of free support and onboarding.'),
            ('Do you sell Zoho licences?',
             'No. You buy Zoho licences directly from Zoho, in your own company\'s name, so you keep full ownership of your account and data. We design, build and support the system.'),
        ],
    ),
    dict(
        slug='united-states', name='the United States', label='United States', iso='US',
        title='Zoho Consultants &amp; Developers in the US | Zudo Works',
        desc='Zoho CRM, Zoho Creator, Deluge and integration development for businesses in all 50 US states, delivered remotely at US$15/hour.',
        h1='Zoho consultants and developers for US businesses',
        lead='We build and customize Zoho CRM, Zoho Creator, Zoho Books and Zoho One for small and growing businesses across the United States, from retail and healthcare to distribution and professional services. Everything is delivered remotely, documented and handed over in your own Zoho account.',
        partner_h='Looking for a Zoho partner in the US?',
        partner=[
            'If you are comparing Zoho partners in the United States, here is where we stand. Zudo Works is an independent Zoho development team; our Zoho Partner application is in progress, and until it is approved we do not call ourselves a Zoho Partner.',
            'What we offer today: a CTO who received the %s from Zoho Creator, US$15 per hour, fixed prices for defined projects and one month of free support after every build. Our <a href="%s" class="text-link">Zoho Partner Program guide</a> explains how to verify any partner.' % (AWARD, PARTNER_GUIDE),
        ],
        how=[
            ('Working across time zones', 'India is 9.5 hours ahead of US Eastern Daylight Time and 12.5 hours ahead of Pacific Daylight Time (10.5 and 13.5 hours in winter). Requests you send in your afternoon can be worked on while you sleep. Book calls at a time in your own time zone through our booking page.'),
            ('Zoho&rsquo;s US data centre', 'US accounts usually run on Zoho&rsquo;s US data centre (zoho.com). We work inside your account with an admin user, and you keep the super-admin login.'),
            ('Your existing tools', 'We connect Zoho with the tools US businesses commonly use, such as QuickBooks, Shopify, Stripe and Google Workspace, through native connectors, Deluge or custom middleware.'),
        ],
        local_h='Zoho for US businesses',
        local=[
            'Common Zoho projects for US businesses include moving from spreadsheets, HubSpot or Salesforce to Zoho CRM, building a Zoho Creator app for operations, or connecting an online store with Zoho Books and Zoho Inventory. We also build custom software around Zoho when a product alone doesn&rsquo;t fit.',
            'We charge US$15 per hour, with fixed prices for defined projects. See our <a href="/insights/zoho-crm-implementation-cost/" class="text-link">Zoho CRM implementation cost guide</a> for typical hours.',
        ],
        areas_h='States we work with',
        areas_intro='We work remotely with businesses in all 50 states and Washington, D.C.',
        areas=[('States', ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']),
               ('Federal district', ['Washington, D.C.'])],
        cities='New York, Los Angeles, Chicago, Houston, Dallas, Austin, Phoenix, Miami, Atlanta, Seattle, San Francisco, Denver, Boston and Philadelphia',
        projects=['trakas', 'healthcare', 'bestaccess'],
        faqs=[
            ('Is Zudo Works a Zoho partner in the US?',
             'Not yet. Our Zoho Partner application is in progress, so we do not describe ourselves as a Zoho Partner. We are an independent Zoho development team working with US businesses remotely. Our CTO, Arunkumar V, received the "Master of Creator (Global Winner)" award from Zoho Creator at the Zoho Creator Partner Hackathon 2025.'),
            ('How do you handle the time difference with the US?',
             'India is 9.5 to 13.5 hours ahead, depending on your time zone and the season. Work can progress overnight your time, and you choose a call time in your own time zone on our booking page.'),
            ('How much does it cost to hire a Zoho developer for a US business?',
             'We charge US$15 per hour, and quote a fixed price for defined projects based on the estimated days and complexity. Our pricing page has a calculator for an indicative estimate, and every build includes one month of free support and onboarding.'),
            ('Can you migrate us from HubSpot or Salesforce to Zoho CRM?',
             'Yes. We map your objects and fields, import data in the right order with legacy IDs, rebuild the automations you still need and check record counts before go-live.'),
        ],
    ),
    dict(
        slug='united-kingdom', name='the United Kingdom', label='United Kingdom', iso='GB',
        title='Zoho Consultants &amp; Developers in the UK | Zudo Works',
        desc='Zoho CRM, Zoho Creator, Zoho Books (VAT and MTD), Deluge and integrations for businesses across England, Scotland, Wales and Northern Ireland. US$15/hour.',
        h1='Zoho consultants and developers for UK businesses',
        lead='We implement and customize Zoho CRM, Zoho Creator, Zoho Books and Zoho One for UK businesses, with a working day that overlaps your whole morning. Every build is documented, handed over in your own Zoho account and followed by a free month of support.',
        partner_h='Looking for a Zoho partner in the UK?',
        partner=[
            'Here is where we stand if you are comparing UK Zoho partners: Zudo Works is an independent Zoho development team. Our Zoho Partner application is in progress, and until it is approved we do not call ourselves a Zoho Partner.',
            'Our CTO, Arunkumar V, received the %s from Zoho Creator at the Zoho Creator Partner Hackathon 2025. To check any provider&rsquo;s partner status, see our <a href="%s" class="text-link">guide to the Zoho Partner Program</a>.' % (AWARD, PARTNER_GUIDE),
        ],
        how=[
            ('Your morning is our afternoon', 'India is 4.5 hours ahead of UK summer time (5.5 hours in winter). Our working day covers your whole morning, so calls, workshops and quick fixes happen the same day.'),
            ('Data location and UK GDPR', 'Zoho runs a UK data centre (zoho.uk) as well as an EU one (zoho.eu). We work inside the account you choose and follow your data-protection requirements. See our <a href="/privacy/">privacy policy</a>.'),
            ('VAT, MTD and Xero', 'We set up Zoho Books for UK VAT and Making Tax Digital, or connect Zoho CRM with Xero or Sage if your accountant prefers them.'),
        ],
        local_h='Zoho for UK businesses',
        local=[
            'Common Zoho projects for UK businesses include training providers, care and service businesses that need a student, client or case management system, plus companies replacing spreadsheets with Zoho CRM and Zoho Creator. Portals, automated PDF documents and role-based access are common requirements.',
            'We charge US$15 per hour, with fixed prices for defined projects, and Zoho licences are billed by Zoho directly to you.',
        ],
        areas_h='Where we work in the UK',
        areas_intro='We work remotely with businesses in all four nations of the UK.',
        areas=[('Nations', ['England', 'Scotland', 'Wales', 'Northern Ireland'])],
        cities='London, Manchester, Birmingham, Leeds, Liverpool, Bristol, Sheffield, Newcastle, Nottingham, Leicester, Glasgow, Edinburgh, Aberdeen, Cardiff, Swansea and Belfast',
        projects=['avalon'],
        faqs=[
            ('Is Zudo Works a Zoho partner in the UK?',
             'Not yet. Our Zoho Partner application is in progress, so we do not describe ourselves as a Zoho Partner. We are an independent Zoho development team working with UK businesses remotely, with a working day that overlaps the UK morning.'),
            ('Can you set up Zoho Books for VAT and Making Tax Digital?',
             'Yes. We configure Zoho Books for UK VAT and Making Tax Digital, set up invoice templates and bank feeds, and connect Books with Zoho CRM or Zoho Inventory. We work alongside your accountant on tax decisions.'),
            ('Where is our data stored?',
             'In the Zoho data centre your account uses. Zoho offers a UK data centre (zoho.uk) and an EU data centre (zoho.eu). We work inside your account and do not copy your data elsewhere without agreement.'),
            ('What does a Zoho developer cost for a UK business?',
             'We charge US$15 per hour, and quote fixed prices for defined projects. Use the calculator on our pricing page for an indicative estimate. Every build includes one month of free support and onboarding.'),
        ],
    ),
    dict(
        slug='australia', name='Australia', label='Australia', iso='AU',
        title='Zoho Consultants &amp; Developers in Australia | Zudo Works',
        desc='Zoho CRM, Zoho Creator, Zoho Books (GST and BAS), Deluge and Xero integrations for businesses in every Australian state and territory. US$15/hour.',
        h1='Zoho consultants and developers for Australian businesses',
        lead='We implement and customize Zoho CRM, Zoho Creator, Zoho Books and Zoho One for Australian businesses, and connect them with the tools you already use, such as Xero. Our working day overlaps your afternoon, and every build includes a free month of support.',
        partner_h='Looking for a Zoho partner in Australia?',
        partner=[
            'If you are comparing Zoho partners in Australia: Zudo Works is an independent Zoho development team. Our Zoho Partner application is in progress, and until it is approved we do not call ourselves a Zoho Partner.',
            'You can check any provider&rsquo;s status in Zoho&rsquo;s Find a Partner directory. Our <a href="%s" class="text-link">Zoho Partner Program guide</a> explains the tiers and what they do and don&rsquo;t tell you.' % PARTNER_GUIDE,
        ],
        how=[
            ('Your afternoon is our morning', 'Sydney and Melbourne are 4.5 hours ahead of India (5.5 hours during daylight saving); Perth is 2.5 hours ahead. Our working day overlaps your afternoon on the east coast and from late morning in Perth.'),
            ('Zoho&rsquo;s Australian data centre', 'Australian accounts usually run on Zoho&rsquo;s Australian data centre (zoho.com.au). We work inside your account, and you keep the super-admin login.'),
            ('GST, BAS and Xero', 'We set up Zoho Books for Australian GST and BAS reporting, or connect Zoho CRM with Xero or MYOB if your accountant prefers them.'),
        ],
        local_h='Zoho for Australian businesses',
        local=[
            'Typical Zoho projects for Australian businesses connect Zoho CRM with an accounting system, automate quotes and job workflows for trades and service businesses, or replace spreadsheets with a Zoho Creator app for field teams.',
            'We charge US$15 per hour, with fixed prices for defined projects, and Zoho licences are billed by Zoho directly to you.',
        ],
        areas_h='States and territories we work with',
        areas_intro='We work remotely with businesses in every Australian state and territory.',
        areas=[('States', ['New South Wales', 'Victoria', 'Queensland', 'Western Australia', 'South Australia', 'Tasmania']),
               ('Territories', ['Australian Capital Territory', 'Northern Territory'])],
        cities='Sydney, Melbourne, Brisbane, Perth, Adelaide, Gold Coast, Canberra, Newcastle, Hobart and Darwin',
        projects=[],
        faqs=[
            ('Is Zudo Works a Zoho partner in Australia?',
             'Not yet. Our Zoho Partner application is in progress, so we do not describe ourselves as a Zoho Partner. We are an independent Zoho development team working with Australian businesses remotely.'),
            ('Can you connect Zoho CRM with Xero?',
             'Yes. We connect Zoho CRM with Xero so that contacts, quotes and invoices stay in sync, using Zoho\'s native integration where it fits and Deluge or middleware where you need custom rules.'),
            ('Which hours do you work for Australian clients?',
             'We work Monday to Friday, 9:00 to 18:00 India time, which is the afternoon on the Australian east coast and from late morning in Perth. You can choose a call time in your own time zone on our booking page.'),
            ('What does a Zoho developer cost for an Australian business?',
             'We charge US$15 per hour, and quote fixed prices for defined projects. The calculator on our pricing page gives an indicative estimate, and every build includes one month of free support and onboarding.'),
        ],
    ),
    dict(
        slug='new-zealand', name='New Zealand', label='New Zealand', iso='NZ',
        title='Zoho Consultants &amp; Developers in New Zealand | Zudo Works',
        desc='Zoho CRM, Zoho Creator, Zoho Books (GST), Deluge and Xero integrations for businesses across all New Zealand regions, delivered remotely at US$15/hour.',
        h1='Zoho consultants and developers for New Zealand businesses',
        lead='We implement and customize Zoho CRM, Zoho Creator, Zoho Books and Zoho One for New Zealand businesses, and connect them with Xero and the other tools you rely on. Every build is documented and followed by a free month of support.',
        partner_h='Looking for a Zoho partner in New Zealand?',
        partner=[
            'Zudo Works is an independent Zoho development team. Our Zoho Partner application is in progress, and until it is approved we do not call ourselves a Zoho Partner.',
            'Our CTO, Arunkumar V, received the %s from Zoho Creator. To verify any provider&rsquo;s partner status, see our <a href="%s" class="text-link">guide to the Zoho Partner Program</a>.' % (AWARD, PARTNER_GUIDE),
        ],
        how=[
            ('Working across time zones', 'New Zealand is 6.5 hours ahead of India (7.5 hours during daylight saving). Our morning is your afternoon, so calls are best in your afternoon, and work continues after your day ends.'),
            ('Any Zoho data centre', 'We work in whichever Zoho data centre your account uses; check the domain you log in to, such as zoho.com.au or zoho.com. You keep the super-admin login.'),
            ('GST and Xero', 'We set up Zoho Books for New Zealand GST, or connect Zoho CRM with Xero, the accounting system many New Zealand businesses already use.'),
        ],
        local_h='Zoho for New Zealand businesses',
        local=[
            'Typical requests include connecting Zoho CRM with Xero, automating quotes, jobs and approvals, and replacing spreadsheets with a Zoho Creator app.',
            'We charge US$15 per hour, with fixed prices for defined projects, and Zoho licences are billed by Zoho directly to you.',
        ],
        areas_h='Regions we work with',
        areas_intro='We work remotely with businesses in every region of New Zealand.',
        areas=[('North Island', ['Northland', 'Auckland', 'Waikato', 'Bay of Plenty', 'Gisborne', 'Hawke&rsquo;s Bay', 'Taranaki', 'Manawatū-Whanganui', 'Wellington']),
               ('South Island', ['Tasman', 'Nelson', 'Marlborough', 'West Coast', 'Canterbury', 'Otago', 'Southland'])],
        cities='Auckland, Wellington, Christchurch, Hamilton, Tauranga, Dunedin, Palmerston North and Nelson',
        projects=[],
        faqs=[
            ('Is Zudo Works a Zoho partner in New Zealand?',
             'Not yet. Our Zoho Partner application is in progress, so we do not describe ourselves as a Zoho Partner. We are an independent Zoho development team working with New Zealand businesses remotely.'),
            ('Can you integrate Zoho with Xero?',
             'Yes. We connect Zoho CRM and other Zoho apps with Xero so that contacts, quotes and invoices stay in sync, using native integrations where they fit and Deluge or middleware for custom rules.'),
            ('How do you handle the time difference with New Zealand?',
             'New Zealand is 6.5 to 7.5 hours ahead of India. Our morning overlaps your afternoon, so that is the best time for calls; you can pick a slot in your own time zone on our booking page.'),
            ('What does a Zoho developer cost for a New Zealand business?',
             'We charge US$15 per hour, and quote fixed prices for defined projects. The calculator on our pricing page gives an indicative estimate, and every build includes one month of free support and onboarding.'),
        ],
    ),
]

OTHER_REGIONS = [
    ('Europe', 'Czech Republic (Czechia), Germany, Ireland, the Netherlands, France, Spain, Italy, Poland, Sweden, Denmark, Belgium, Austria, Switzerland and Portugal',
     'Many European accounts run on Zoho&rsquo;s EU data centre (zoho.eu). We follow your GDPR requirements and work inside your account.'),
    ('Middle East', 'Saudi Arabia, the United Arab Emirates, Qatar, Oman, Bahrain and Kuwait',
     'Zoho has regional data centres including Saudi Arabia (zoho.sa). At a previous organization, our CTO worked on a legal case-management project for a client in Saudi Arabia.'),
    ('Asia', 'Singapore, Malaysia, Thailand, the Philippines, Indonesia, Vietnam, Sri Lanka, Bangladesh, Nepal and Japan',
     'At a previous organization, our CTO worked on a travel pricing engine for a business in Thailand and executive dashboards for a manufacturer in China.'),
    ('Americas and Africa', 'Canada, Mexico, Brazil, South Africa, Nigeria and Kenya',
     'Canadian accounts can use Zoho&rsquo;s Canadian data centre. Elsewhere we work in whichever data centre your account uses.'),
]

HUB_FAQS = [
    ('Which countries does Zudo Works work with?',
     'We are based in Chennai, India, and work remotely with businesses in the United States, the United Kingdom, Australia, New Zealand and India, as well as Europe, the Middle East, Asia and other regions.'),
    ('Is Zudo Works a Zoho partner?',
     'Our Zoho Partner application is in progress, so we do not describe ourselves as a Zoho Partner. We are an independent Zoho development team. Our CTO, Arunkumar V, received the "Master of Creator (Global Winner)" award from Zoho Creator at the Zoho Creator Partner Hackathon 2025.'),
    ('Can you work with a Zoho account outside my country?',
     'Yes. Zoho runs several regional data centres, such as zoho.com, zoho.eu, zoho.uk, zoho.in and zoho.com.au. We work in whichever data centre your account uses, and your data stays in your own account.'),
    ('How do you work with clients in other time zones?',
     'We work Monday to Friday, 9:00 to 18:00 India time. You choose a call time in your own time zone on our booking page, and written updates keep work moving between calls.'),
]

CHEVRON = '<svg class="faq-toggle" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>'


def plain(t):
    return html.unescape(t).replace('’', "'")


def ld(obj):
    return '  <script type="application/ld+json">\n' + json.dumps(obj, indent=2, ensure_ascii=False) + '\n  </script>\n'


def faq_html(faqs, heading):
    items = ''.join(f'''          <div class="faq-item">
            <button type="button" class="faq-question" aria-expanded="false">
              <span>{html.escape(q, quote=False)}</span>
              {CHEVRON}
            </button>
            <div class="faq-answer">
              <p>{html.escape(a, quote=False).replace("'", "&rsquo;")}</p>
            </div>
          </div>
''' for q, a in faqs)
    return f'''    <section class="section" id="faq">
      <div class="container container--prose">
        <div class="section-header section-header--left">
          <p class="section-label">FAQs</p>
          <h2>{heading}</h2>
        </div>
        <div class="faq-list">
{items}        </div>
      </div>
    </section>
'''


def faq_ld(faqs):
    return ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})


def breadcrumb_ld(name, url, crumbs):
    return ld({"@context": "https://schema.org", "@type": "WebPage", "name": name, "url": url,
               "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
                   {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(crumbs)]}})


def page(title, desc, url, schema, crumbs, body):
    t = title
    crumb_html = ''.join(
        f'          <a href="{u}">{n}</a>\n          <span class="breadcrumb-sep" aria-hidden="true">/</span>\n'
        for n, u in crumbs[:-1]) + f'          <span class="breadcrumb-current" aria-current="page">{crumbs[-1][0]}</span>\n'
    return f'''<!DOCTYPE html>
<html lang="en">

<head>
    <!-- @head -->
    <!-- @/head -->

  <title>{t}</title>
  <meta name="description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{OG}">
  <meta property="og:site_name" content="Zudo Works">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{OG}">
{schema}</head>

<body>
    <!-- @header -->
    <!-- @/header -->

  <main id="main-content">
    <section class="page-hero page-hero--service">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
{crumb_html}        </nav>
{body}
  </main>

    <!-- @footer -->
    <!-- @/footer -->
</body>

</html>
'''


CTA = '''    <section class="cta-banner">
      <div class="container">
        <h2>%s</h2>
        <p>Tell us what you want to build or fix. We reply within one business day with next steps.</p>
        <div class="btn-group justify-center">
          <a href="/contact/" class="btn btn-white btn-lg" data-booking>Book a Discovery Call</a>
          <a href="/contact/#contact-form" class="btn btn-outline-white btn-lg">Send Project Details</a>
        </div>
      </div>
    </section>
'''


def services_section(country):
    cards = ''.join(f'''          <article class="service-card">
            <h3><a href="{u}">{n}</a></h3>
            <p>{d}</p>
          </article>
''' for u, n, d in SERVICES)
    return f'''    <section class="section section--alt" id="services">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Services</p>
          <h2>Zoho services for businesses in {country}</h2>
        </div>
        <div class="service-grid">
{cards}        </div>
      </div>
    </section>
'''


def country_page(c):
    url = f'{SITE}/locations/{c["slug"]}/'
    crumbs = [('Home', '/'), ('Locations', '/locations/'), (c['label'], f'/locations/{c["slug"]}/')]
    areas_all = [a for _, group in c['areas'] for a in group]
    service = {
        "@context": "https://schema.org", "@type": "Service",
        "name": plain(c['h1'][0].upper() + c['h1'][1:]),
        "serviceType": "Zoho consulting and development",
        "url": url,
        "description": plain(c['desc']),
        "provider": {"@type": "Organization", "@id": SITE + "/#organization", "name": "Zudo Works"},
        "areaServed": {"@type": "Country", "name": c['label'],
                       "identifier": c['iso'],
                       "containsPlace": [{"@type": "AdministrativeArea", "name": plain(a)} for a in areas_all]},
        "offers": {"@type": "Offer", "priceCurrency": "USD", "priceSpecification": {
            "@type": "UnitPriceSpecification", "price": 15, "priceCurrency": "USD", "unitCode": "HUR", "unitText": "hour"}},
    }
    schema = breadcrumb_ld(plain(c['h1']), url, crumbs) + ld(service) + faq_ld(c['faqs'])

    partner = ''.join(f'          <p>{p}</p>\n' for p in c['partner'])
    how = ''.join(f'''          <div class="loc-card">
            <h3>{h}</h3>
            <p>{t}</p>
          </div>
''' for h, t in c['how'])
    local = ''.join(f'          <p>{p}</p>\n' for p in c['local'])
    groups = ''.join(f'''          <div class="area-group">
            <h3>{g}</h3>
            <ul class="area-list">
{"".join(f"              <li>{a}</li>{chr(10)}" for a in items)}            </ul>
          </div>
''' for g, items in c['areas'])
    projects = ''
    if c['projects']:
        cards = ''.join(f'''          <article class="project-card">
            <p class="project-card-meta">{PROJECTS[k][1]}</p>
            <h3>{PROJECTS[k][0]}</h3>
            <p>{PROJECTS[k][2]}</p>
          </article>
''' for k in c['projects'])
        projects = f'''    <section class="section" id="experience">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Experience</p>
          <h2>Project experience in {c['name']}</h2>
          <p class="provenance-note">Our CTO, Arunkumar V, worked on these projects as a developer at a previous organization. They were that organization&rsquo;s clients, not Zudo Works engagements. <a href="/work/" class="text-link">See all project experience</a></p>
        </div>
        <div class="project-grid">
{cards}        </div>
      </div>
    </section>

'''
    body = f'''        <p class="section-label">Zoho consultants &middot; {c['label']}</p>
        <h1>{c['h1']}</h1>
        <p class="page-lead">{c['lead']}</p>
        <div class="btn-group">
          <a href="/contact/" class="btn btn-primary btn-lg" data-booking>Book a Discovery Call</a>
          <a href="/pricing/#calculator" class="btn btn-secondary btn-lg">Estimate my project</a>
        </div>
      </div>
    </section>

    <section class="section" id="partner">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Choosing a Zoho partner</p>
          <h2>{c['partner_h']}</h2>
{partner}        </div>
      </div>
    </section>

    <section class="section section--alt" id="how">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">How we work</p>
          <h2>Working with us from {c['name']}</h2>
        </div>
        <div class="loc-grid">
{how}        </div>
      </div>
    </section>

    <section class="section" id="local">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Typical projects</p>
          <h2>{c['local_h']}</h2>
{local}        </div>
      </div>
    </section>

{services_section(c['name'])}
{projects}    <section class="section{' section--alt' if c['projects'] else ''}" id="areas">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Coverage</p>
          <h2>{c['areas_h']}</h2>
          <p>{c['areas_intro']}</p>
        </div>
        <div class="area-groups">
{groups}        </div>
        <p class="area-cities"><strong>Including:</strong> {c['cities']}.</p>
        <p class="area-cities">Not in {c['name']}? See <a href="/locations/" class="text-link">all countries we work with</a>.</p>
      </div>
    </section>

{faq_html(c['faqs'], 'Questions from businesses in ' + c['name'])}
{CTA % ('Start your Zoho project in ' + c['name'])}'''
    return page(c['title'], c['desc'], url, schema, crumbs, body)


def hub_page():
    url = SITE + '/locations/'
    crumbs = [('Home', '/'), ('Locations', '/locations/')]
    title = 'Zoho Consultants in the US, UK, AU, NZ &amp; India | Zudo Works'
    desc = 'Zudo Works works remotely with businesses in the US, UK, Australia, New Zealand, India, Europe, the Middle East and Asia. Find Zoho help for your country.'
    service = {"@context": "https://schema.org", "@type": "Service", "name": "Zoho consulting and development",
               "url": url, "provider": {"@type": "Organization", "@id": SITE + "/#organization", "name": "Zudo Works"},
               "areaServed": [{"@type": "Country", "name": c['label'], "url": f'{SITE}/locations/{c["slug"]}/'} for c in COUNTRIES]}
    schema = breadcrumb_ld('Locations', url, crumbs) + ld(service) + faq_ld(HUB_FAQS)
    cards = ''.join(f'''          <article class="service-card">
            <h3><a href="/locations/{c['slug']}/">Zoho consultants: {c['label']}</a></h3>
            <p>{c['areas_intro']}</p>
          </article>
''' for c in COUNTRIES)
    regions = ''.join(f'''          <div class="loc-card">
            <h3>{r}</h3>
            <p><strong>Including:</strong> {countries}.</p>
            <p>{note}</p>
          </div>
''' for r, countries, note in OTHER_REGIONS)
    body = f'''        <p class="section-label">Locations</p>
        <h1>Zoho consultants for businesses worldwide</h1>
        <p class="page-lead">Zudo Works is a Zoho and custom software team based in Chennai, India. We work remotely with businesses in the United States, the United Kingdom, Australia, New Zealand and India, and with clients across Europe, the Middle East and Asia.</p>
        <div class="btn-group">
          <a href="/contact/" class="btn btn-primary btn-lg" data-booking>Book a Discovery Call</a>
          <a href="/pricing/" class="btn btn-secondary btn-lg">See pricing</a>
        </div>
      </div>
    </section>

    <section class="section" id="countries">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Main markets</p>
          <h2>Choose your country</h2>
          <p>Each page covers time zones, Zoho data centres, local tax and accounting tools, and the states or regions we work with.</p>
        </div>
        <div class="service-grid">
{cards}        </div>
      </div>
    </section>

    <section class="section section--alt" id="other">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Other countries</p>
          <h2>Zoho help in Europe, the Middle East, Asia and beyond</h2>
          <p>Zoho projects are delivered remotely, so we can work with your business wherever it is.</p>
        </div>
        <div class="loc-grid">
{regions}        </div>
      </div>
    </section>

    <section class="section" id="partner">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Choosing a Zoho partner</p>
          <h2>Looking for a Zoho partner near you?</h2>
          <p>Zudo Works is an independent Zoho development team. Our Zoho Partner application is in progress, and until it is approved we do not call ourselves a Zoho Partner. Our CTO, Arunkumar V, received the {AWARD} from Zoho Creator at the Zoho Creator Partner Hackathon 2025.</p>
          <p>To find or verify a listed partner in any country, read our <a href="{PARTNER_GUIDE}" class="text-link">guide to the Zoho Partner Program</a>, and use our <a href="{CHOOSE_GUIDE}" class="text-link">checklist for choosing a Zoho development partner</a> to compare providers.</p>
        </div>
      </div>
    </section>

{faq_html(HUB_FAQS, 'Working with us from another country')}
{CTA % 'Wherever you are, start with one conversation'}'''
    return page(title, desc, url, schema, crumbs, body)


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        # keep the regions build.py has already filled in, so re-running is idempotent
        import re
        old = open(path, encoding='utf-8').read()
        for name in ('head', 'header', 'footer'):
            m = re.search(r'<!-- @%s -->\n.*?<!-- @/%s -->' % (name, name), old, re.S)
            if m:
                content = re.sub(r'<!-- @%s -->\n.*?<!-- @/%s -->' % (name, name), lambda _: m.group(0), content, count=1, flags=re.S)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print('wrote', rel)


if __name__ == '__main__':
    write('locations/index.html', hub_page())
    for c in COUNTRIES:
        write(f'locations/{c["slug"]}/index.html', country_page(c))
