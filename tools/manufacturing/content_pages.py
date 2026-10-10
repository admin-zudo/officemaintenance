"""Solution and hub pages for the Manufacturing section."""
from content_common import *

PAGES = []
BTN = [('Book a Discovery Call', '/contact/', 'btn-primary')]


def sec(sid, label, h2, inner, alt=False, intro='', narrow=False):
    intro = f'\n          <p>{intro}</p>' if intro else ''
    return f'''    <section class="section{' section--alt' if alt else ''}" id="{sid}">
      <div class="container{' container--prose' if narrow else ''}">
        <div class="section-header section-header--left">
          <p class="section-label">{label}</p>
          <h2>{h2}</h2>{intro}
        </div>
{inner}
      </div>
    </section>
'''


def grid(items, cls='service-grid', card='deliver-card'):
    out = ''
    for it in items:
        h = f'<a href="{it[2]}">{it[0]}</a>' if len(it) > 2 else it[0]
        out += f'          <div class="{card}">\n            <h3>{h}</h3>\n            <p>{it[1]}</p>\n          </div>\n'
    return f'        <div class="{cls}">\n{out}        </div>'


def problems(items): return grid(items, 'problem-grid problem-grid--4', 'problem-item')
def checks(items): return '        <ul class="check-list">\n' + ''.join(f'          <li>{x}</li>\n' for x in items) + '        </ul>'
def path(items): return '        <ol class="mfg-path">\n' + ''.join(f'          <li><h3>{h}</h3><p>{p}</p></li>\n' for h, p in items) + '        </ol>'
def figgrid(*f): return '        <div class="mfg-fig-grid">' + ''.join(f) + '</div>'
def cards(ALL, items): return '        <div class="post-grid">\n' + '\n'.join(ALL['_card'](i) for i in items) + '\n        </div>'


def uc(uid, title, kind, points, link=None):
    dl = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in points)
    more = f'<p class="mfg-uc-more"><a href="{link[0]}">{link[1]} &rarr;</a></p>' if link else ''
    return f'        <article class="mfg-uc" id="{uid}"><div class="mfg-uc-head"><h3>{title}</h3><span class="mfg-uc-kind">{kind}</span></div><dl>{dl}</dl>{more}</article>\n'


# ====================================================================== landing page
S = 'hub-manufacturing'
cover(S, 'Manufacturing', 'Connected operations for small manufacturers', 'Orders, stock, production, quality and accounts working from the same information.',
      two(m_tiles([('1', 'Sales orders', 'From quote to promise date'), ('2', 'Purchasing', 'Reorders and approvals'), ('3', 'Stock', 'Lots and locations'),
                   ('4', 'Production', 'Jobs by stage'), ('5', 'Quality', 'Checks and NCRs'), ('6', 'Accounts', 'Invoices and bills')])),
      theme='blue', alt='Cover: six connected areas of a factory: sales orders, purchasing, stock, production, quality and accounts')
L1 = fig(S + '-lanes', m_lanes(['Order', 'Buy', 'Make', 'Check', 'Ship and bill'], [
            ('Office', [('Quote accepted', 'Sales order created', 'hi'), ('PO approved', 'By value band'), None, None, ('Invoice drafted', 'From the shipment', 'hi')]),
            ('Stores', [None, ('Goods received', 'Lots labelled'), ('Materials issued', 'Scanned to the job'), None, ('Order picked', 'Scanned out')]),
            ('Shop floor', [None, None, ('Stages completed', 'Scan at each step', 'hi'), ('Problems put on hold', 'With a reason'), None]),
            ('Quality', [None, ('Incoming check', ''), None, ('Inspection recorded', 'Fail raises an NCR', 'hi'), None])]),
         'Swimlane of a connected factory across office, stores, shop floor and quality, from order through buying, making and checking to shipping and billing',
         'A connected factory in one picture. Each cell is a record made by the person doing the work, at the time.', h=520, title='What &ldquo;connected&rdquo; means in practice')
L2 = fig(S + '-ladder', m_steps([('Paper and spreadsheets', 'Information lives in files and heads', 'Where most start'), ('One process digital', 'Job tracking or quality on an app', 'First 90 days'), ('Systems connected', 'Orders, stock and accounts linked', 'Months 3-9'), ('Measured and assisted', 'Dashboards, alerts and AI help', 'When data is trusted')],
                                 ['#9AA5B8', '#226DB4', '#089949', '#E09E0F'], label='STAGE'),
         'Four stages of maturity: paper and spreadsheets, one process digital, systems connected, then measured and assisted',
         'Four stages. Skipping one usually means coming back to it.', h=440, title='A realistic path')
L3 = fig(S + '-ops', app('Operations', 'Concept dashboard', ['Today', 'Orders', 'Production', 'Stock', 'Quality'], 'Today', 'Today in the factory', 'Friday 10 Oct &middot; example data',
         kpis([('Orders due this week', '14', '3 at risk', 'dn'), ('Jobs in progress', '13', '2 on hold', 'fl'), ('Items to reorder', '6', '2 awaiting approval', 'fl'), ('Open NCRs', '4', '1 over 14 days', 'dn')])
         + g2(panel('Jobs by stage', bars2([('Cutting', 46, '3'), ('Machining', 62, '4'), ('Assembly', 46, '3'), ('Finishing', 31, '2'), ('Ready to ship', 15, '1')]) + note('Counts come from scans on the floor, not from a meeting.'), '13 open'),
              panel('Needs a decision', listing([('r', 'J-1035 on hold: part missing', 'Planner &middot; since Wednesday'), ('y', 'PO for hinges awaiting approval', 'Operations manager &middot; 1 day'), ('y', 'NCR-0318 awaiting disposition', 'Quality lead &middot; 2 days'), ('g', 'All deliveries for Monday received', '')]), 'with an owner'), '1fr')),
         'Illustrative daily operations dashboard with orders due, jobs in progress, items to reorder, open NCRs, jobs by stage and a list of decisions needed',
         'A concept daily view. It is built last, from records the earlier steps create.', h=520, ui=True)
L4 = fig(S + '-fit', m_dd(['Make-to-order and job-shop work', 'A process that standard software does not fit', 'Shallow bills of materials', 'A team that wants to improve in steps', 'An ERP in place that operators avoid'],
                           ['Forecast-driven planning across deep BOMs', 'A need for full MRP on day one', 'Heavily regulated validated systems', 'No one to own the system internally', 'Expecting software to fix wrong data'], ('A good fit for our approach', 'Better served elsewhere')),
         'Two lists: situations where a Zoho-based approach fits a manufacturer and situations better served by a manufacturing ERP or specialist system',
         'Where this approach fits and where it does not. We would rather say so before a project than during it.', h=480)


def landing(ALL):
    g, c = ALL['_guides'], ALL['_cases']
    pick = lambda *sl: [ALL[s] for s in sl]
    return (
        sec('problems', 'Sound familiar?', 'The problems we are usually asked to fix', problems([
            ('Nobody knows where a job is', 'Status lives on a whiteboard, and the office walks to the floor to find out.'),
            ('Stock figures nobody trusts', 'The system says 40, the shelf says 12, and buyers keep a private spreadsheet.'),
            ('The same order typed four times', 'Quote, job sheet, dispatch note and invoice, each a chance for a different number.'),
            ('Quality records in a cabinet', 'Every nonconformance is written down. Nobody can say whether it is the fourth time.')]))
        + sec('what-we-do', 'What we do', 'Three kinds of work',
              grid([('Zoho implementation for manufacturers', 'Stock, purchasing, sales and accounts on Zoho apps, with production built around your routing on Zoho Creator. Honest about what Zoho does not do.', M + 'zoho-implementation/'),
                    ('Manufacturing workflows', 'Job tracking, traceability, quality, purchasing and maintenance, designed as scan-and-tap steps for the people doing the work.', M + 'workflows/'),
                    ('AI in manufacturing', 'Narrow, checkable uses: reading purchase orders and supplier documents, answering questions about your own data. Always with a person approving.', M + 'ai-automation/')]),
              alt=True, intro='We are a Zoho development team. We design, build and connect business systems, and this section explains how we apply that to factories and workshops.')
        + sec('connected', 'The idea', 'One set of records, entered once', L1
              + '\n        <p>Most small factories already record nearly everything. The trouble is that each record sits in its own file, written after the event, by someone other than the person who did the work. Connecting operations means three changes: record at the point of work, give every order one number that follows it everywhere, and let each system own its own data.</p>\n'
              + checks(['Operators scan a job card; nobody keys a job number', 'A sales order creates the work order, and the shipment creates the invoice', 'Stock moves are posted as they happen, not at the end of the shift', 'A problem is a record with a reason and an owner, not a conversation',
                        'Managers see exceptions listed, not a wall of charts', 'Your accounting package stays, if it suits you']))
        + sec('path', 'How it happens', 'A realistic path, one process at a time', L2
              + '\n        <p>We do not recommend replacing everything at once. Pick the process that hurts most and is simple enough to finish, get it into daily use, then connect outwards. Our <a href="' + G + 'spreadsheets-to-connected-system-roadmap/">90-day roadmap</a> sets out the plan week by week.</p>', alt=True)
        + sec('what-it-looks-like', 'What you end up with', 'A daily view built from real records', L3
              + '\n        <p>Screens on these pages are concept mockups with example data. They show the kind of interface we design; they are not screenshots of a customer system or of a Zoho product.</p>')
        + sec('guides', 'Learn', 'Practical guides for manufacturers', cards(ALL, pick('inventory-accuracy-for-manufacturers', 'production-tracking-zoho-creator', 'zoho-or-manufacturing-erp'))
              + f'\n        <p class="mfg-more"><a href="{G}" class="btn btn-secondary">All {len(g)} guides</a></p>', alt=True,
              intro='Each guide explains one topic properly, with formulas, worked examples, diagrams and the mistakes to avoid.')
        + sec('case-studies', 'Reference implementations', 'Illustrative case studies', cards(ALL, c)
              + f'\n        <p class="mfg-more"><a href="{CS}" class="btn btn-secondary">About these case studies</a></p>',
              intro='These are designs for composite businesses, written to show how we would approach a problem. They are not client projects and claim no measured results.')
        + sec('fit', 'Straight answers', 'Where this approach fits, and where it does not', L4
              + '\n        <p>Zoho Inventory has no manufacturing module, and nothing in the standard Zoho apps calculates material requirements from a forecast. Zoho ERP does include manufacturing, but is published for India only at the time of writing. If you need full requirements planning, a manufacturing ERP is the better core, and we say so. Our comparison of <a href="' + G + 'zoho-or-manufacturing-erp/">Zoho apps and a manufacturing ERP</a> helps you decide.</p>', alt=True)
        + sec('how-we-work', 'Working with us', 'How a project runs', path([
            ('Walk the process', 'We follow two or three real jobs from order to invoice and write down every retyping and every question.'),
            ('Agree a small first step', 'One process, a written scope, a fixed price where the scope allows.'),
            ('Build and trial', 'A working version on one line or bench within weeks, changed in response to the people using it.'),
            ('Connect and hand over', 'Integrations, a report, training and documentation your team can maintain.')])
              + '\n        <p>Our <a href="/pricing/">pricing page</a> explains how we estimate, and <a href="/work/">our work</a> lists the kinds of systems we have built.</p>')
    )


PAGES.append(dict(
    route=M, crumb='Manufacturing', seo_title='Manufacturing Automation and Zoho Solutions', service_name='Manufacturing systems on Zoho', service_type='Manufacturing software implementation',
    desc='Zoho implementation, workflow automation and practical AI for small manufacturers: job tracking, stock, quality, traceability and integrations, with guides.',
    label='Manufacturing', h1='Connected operations for small and midsized manufacturers',
    lead='We help factories and workshops replace whiteboards, spreadsheets and retyping with systems that record work as it happens. Built on Zoho where it fits, and honest about where it does not.',
    buttons=BTN + [('Read the guides', G, 'btn-secondary')],
    facts=[('For', 'Make-to-order and batch manufacturers'), ('Built on', 'Zoho Creator, Inventory, CRM, Analytics'), ('Serving', 'New Zealand, Australia, UK, US and India')],
    hero=S, hero_alt='Cover: six connected areas of a factory', sections=landing,
    faqs=[('Can Zoho run a manufacturing business?',
           'For many small manufacturers, yes, as a combination: Zoho Inventory for stock and purchasing, Zoho CRM for sales, an accounting package, and a production app built on Zoho Creator. The standard apps do not include material requirements planning, so businesses that need it are better served by a manufacturing ERP.'),
          ('Do you work with manufacturers in New Zealand and Australia?',
           'Yes. We work remotely with businesses in New Zealand, Australia, the UK, the US and India. For New Zealand we usually recommend keeping the accounting package your accountant uses and integrating with it.'),
          ('Are the case studies real customers?',
           'No. They are illustrative reference implementations for composite businesses, labelled as such. They show how we would design a solution and do not claim client names, quotes or measured results.'),
          ('Where should a manufacturer start?',
           'With the one process that causes the most daily pain and is simple enough to finish in a few weeks. For most that is job tracking or quality records. Get it into daily use before connecting other systems.'),
          ('Do we have to replace our ERP or accounting software?',
           'No. If the core system works, we keep it and build beside it. Custom apps handle what it does badly, such as shop-floor data capture, and pass results back.')],
    cta=('Tell us how your factory runs today', 'Describe one job from order to invoice. We will tell you what we would build first, what we would leave alone and what it would cost.'),
))

# ====================================================================== Zoho implementation
S = 'hub-zoho'
cover(S, 'Zoho implementation', 'Zoho for manufacturers, set up properly', 'Standard apps for what they do well. A custom app for production. Clear about the gaps.',
      m_rows([('Zoho Inventory', 'Stock, lots, purchasing, shipping'), ('Zoho Creator', 'Production, quality and floor apps'), ('Zoho Analytics', 'Dashboards across all of it')]),
      theme='blue', solid=True, alt='Cover: three Zoho products and their role for a manufacturer: Inventory for stock, Creator for production and Analytics for dashboards')
Z1 = fig(S + '-map', m_table(['Need', 'Zoho product', 'What it covers', 'What it does not'],
                              [['Stock and purchasing', 'Zoho Inventory', 'Lots, serials, warehouses, reorder points, POs', 'Work orders, routing, MRP'], ['Production', 'Zoho Creator (custom app)', 'Work orders, stages, scrap, holds', 'A ready-made planning engine'],
                               ['Sales', 'Zoho CRM', 'Quotes, orders, customer history', 'Production scheduling'], ['Accounts', 'Zoho Books or your own', 'Invoices, bills, tax', 'Varies by country edition'],
                               ['Reporting', 'Zoho Analytics', 'Dashboards, alerts, forecasts', 'Fixing bad source data']], '.8fr .9fr 1.3fr 1fr'),
         'Table mapping five manufacturing needs to Zoho products, with what each covers and what it does not',
         'Which Zoho product does what for a manufacturer, including the gaps. Checked against Zoho&rsquo;s documentation in October 2026.', h=540, title='Product map')
Z2 = fig(S + '-arch', m_arch([('People and devices', 'office, floor and stores', ['Browser', 'Shared tablets', 'Phone scanning', 'Customer portal']),
                               ('Custom apps', 'Zoho Creator', ['Production tracking', 'Quality and NCR', 'Batch records', 'Maintenance'], True),
                               ('Standard apps', 'configured, not rebuilt', ['Zoho CRM', 'Zoho Inventory', 'Zoho Books or your accounts']),
                               ('Glue and reporting', 'integration and insight', ['Deluge', 'Zoho Flow', 'APIs', 'Zoho Analytics'])]),
         'Reference architecture for a manufacturer on Zoho: devices, custom Creator apps, standard Zoho apps, and an integration and reporting layer',
         'Our reference architecture. Standard apps are configured; only the parts that are unique to you are built.', h=540, title='Reference architecture')
Z3 = fig(S + '-stock', app('Stock', 'Concept on Zoho Inventory data', ['Items', 'Lots', 'Reorder', 'Purchase orders', 'Counts'], 'Lots', 'Lots in stock: butter, unsalted 25 kg', '3 lots &middot; 2 locations &middot; example data',
         kpis([('On hand', '425 kg', '17 cases', 'fl'), ('Reorder point', '300 kg', 'lead time 5 days', 'fl'), ('Earliest use-by', '14 Nov', 'lot B-0907', 'dn'), ('On order', '500 kg', 'due Tuesday', 'fl')])
         + panel('Lots, oldest first', table('110px 110px 96px minmax(0,1fr) 110px 110px', ['Lot', 'Received', '>On hand', 'Location', 'Use by', 'Status'],
                 [[('sn', 'B-0907'), '22 Sep', ('r', '50 kg'), 'Chiller 1, bay 2', '14 Nov', ('st', 'y', 'Use first')], [('sn', 'B-0913'), '2 Oct', ('r', '125 kg'), 'Chiller 2, bay 1', '28 Nov', ('st', 'g', 'Available')],
                  [('sn', 'B-0921'), '8 Oct', ('r', '250 kg'), 'Chiller 2, bay 3', '4 Dec', ('st', 'g', 'Available')]]), 'issue the oldest lot first', 'flex:1')),
         'Illustrative stock screen listing three lots of one material with received date, quantity, location, use-by date and status',
         'A concept stock view over Zoho Inventory data. Batch tracking, expiry dates and reorder points are standard features; the layout is ours.', h=460, ui=True)
Z4 = fig(S + '-phases', m_timeline([('Weeks 1-2', 'Discover', 'Walk the process, check data, choose the route'), ('Weeks 3-6', 'Foundation', 'Items, stock and one custom workflow'),
                                     ('Weeks 7-10', 'Connect', 'Orders, stock and accounts linked'), ('Weeks 11-12', 'Measure', 'Dashboards, training, handover')]),
         'Four implementation phases over twelve weeks: discover, foundation, connect and measure',
         'A typical first phase. Larger scopes repeat the middle two steps for each process.', h=380, title='How an implementation runs')
Z5 = fig(S + '-regions', m_table(['Region', 'Accounting', 'Notes'],
                                  [['New Zealand', 'Global edition of Zoho Books, or keep Xero or MYOB', 'No named NZ edition of Zoho Books at the time of writing'], ['Australia', 'Zoho Books Australia edition, or your own', 'Check GST and payroll needs with your accountant'],
                                   ['United Kingdom', 'Zoho Books UK edition, or your own', 'Confirm tax filing requirements before switching'], ['United States', 'Zoho Books US edition, or your own', 'Sales tax varies by state'],
                                   ['India', 'Zoho Books India edition; Zoho ERP available', 'Zoho ERP includes a manufacturing module']], '.7fr 1.3fr 1.3fr'),
         'Table of accounting options and notes by region: New Zealand, Australia, United Kingdom, United States and India',
         'What changes by region. Product availability shifts, so we confirm it at the start of every project.', h=520, title='Regional notes')
Z6 = fig(S + '-routes', m_tiers([('Route A', 'Zoho apps and a custom app', 'Unusual process, simple planning', ['Inventory, CRM, accounts', 'Production on Creator', 'Built in steps']),
                                  ('Route B', 'ERP plus Creator apps', 'An ERP you want to keep', ['ERP stays the core', 'Floor apps beside it', 'Results passed back']),
                                  ('Route C', 'A manufacturing ERP', 'Deep BOMs, forecast planning', ['MRP and costing built in', 'We will say so', 'Integration help if useful'])], on=0),
         'Three implementation routes: Zoho apps with a custom app, an ERP with Creator apps beside it, or a manufacturing ERP',
         'Three routes. We implement the first two and will tell you when the third is the right answer.', h=500, title='Three routes')


def zoho(ALL):
    return (
        sec('who', 'Is this for you?', 'When a Zoho-based set-up suits a manufacturer', problems([
            ('Your process is your advantage', 'Custom steps, approvals or tests that a standard ERP screen cannot hold.'),
            ('You plan per job or by reorder point', 'You do not need a forecast exploded through four levels of bill of materials.'),
            ('You want to improve in steps', 'One process at a time, each paying for the next, not one large go-live.'),
            ('You already use Zoho somewhere', 'CRM, Books or Inventory is in place and production is the missing piece.')]))
        + sec('product-map', 'The products', 'Which Zoho product does what', Z1 + '''
        <p>Three facts shape every design we do:</p>
''' + checks(['Zoho Inventory offers batch and serial tracking, multiple warehouses, reorder points, barcode scanning and composite items for simple assemblies',
              'Zoho&rsquo;s own knowledge base states that Zoho Inventory does not yet support manufacturing modules',
              'Zoho Creator covers the gap with custom apps: forms, mobile apps that scan barcodes, approvals, schedules and role-based access',
              'Zoho ERP has manufacturing orders, job cards and work centres, but is published for India and is licensed separately from Zoho One',
              'Zoho Analytics adds dashboards, scheduled reports, alerts and forecasting across all of them',
              'None of the standard apps performs material requirements planning from a forecast']), alt=True)
        + sec('routes', 'Choosing', 'Three routes, and how to pick', Z6
              + '\n        <p>The choice turns on two questions: how complex your planning is, and how unusual your process is. Our guide <a href="' + G + 'zoho-or-manufacturing-erp/">Zoho apps or a manufacturing ERP?</a> works through five questions and a matrix. If the answer is an ERP we cannot implement, we will still say so.</p>')
        + sec('architecture', 'Design', 'Reference architecture', Z2 + '''
        <p>The principle is to configure what is standard and build only what is yours. Customers and quotes live in the CRM. Items, lots and quantities live in the stock system. Work orders, stages and quality records live in custom apps, because that is where your process differs from everyone else&rsquo;s. Each record has one owner, and integrations carry events between them. The detail is in our guide to <a href="''' + G + '''connect-sales-production-accounts/">connecting sales, production and accounts</a>.</p>''', alt=True)
        + sec('deliverables', 'What we deliver', 'What an implementation includes',
              grid([('Process map and data check', 'Two or three real jobs walked from order to invoice, plus a review of item, customer and stock data before anything is built.'),
                    ('Stock and purchasing set-up', 'Items, units, lots or serials, locations, reorder points, purchase approvals and opening stock, loaded and checked.'),
                    ('A production app on Creator', 'Work orders, routing stages, shop-floor screens, scrap and holds, built around how you work.'),
                    ('Integrations', 'Orders to work orders, completions to stock, shipments to invoices, with visible failures and retries.'),
                    ('Dashboards and alerts', 'A small number of measures with written definitions, targets and owners.'),
                    ('Documentation and training', 'Admin notes, user guides and commented Deluge code, so your team can maintain it.')]) + '\n' + Z3)
        + sec('process', 'Timeline', 'How an implementation runs', Z4
              + '\n        <p>Twelve weeks is typical for a first phase covering stock, one production workflow and the main integrations. It depends on the state of your data more than on anything we build: clean item and customer lists shorten every step. The <a href="' + G + 'spreadsheets-to-connected-system-roadmap/">90-day roadmap</a> describes the same sequence from your side.</p>', alt=True)
        + sec('regions', 'Where you are', 'What changes by region', Z5 + '''
        <p>Zoho Books is published in country editions and a global edition. New Zealand is not among the named editions at the time of writing, so New Zealand manufacturers either use the global edition or, more often, keep the accounting package their accountant already uses and integrate with it. That is a sound choice anywhere: accounting software is the part of the stack we are least keen to change without a reason.</p>''')
        + sec('limits', 'Limits', 'What a Zoho set-up will not do', checks([
            'Plan materials from a forecast across multi-level bills of materials', 'Schedule finite capacity across machines automatically', 'Provide standard costing and variance analysis out of the box',
            'Replace a validated system in a heavily regulated industry', 'Fix stock figures that are wrong at the source', 'Work offline everywhere: Creator has offline access with restrictions, so we test it on your devices'])
              + '\n        <p>Some of these can be approximated with custom work. We would rather tell you when that is a poor idea. If you need requirements planning, buy it; do not ask a low-code app to imitate it.</p>', alt=True)
        + sec('learn', 'Go deeper', 'Guides for this work', cards(ALL, [ALL[s] for s in ('production-tracking-zoho-creator', 'inventory-accuracy-for-manufacturers', 'purchasing-reorder-points')]))
    )


PAGES.append(dict(
    route=M + 'zoho-implementation/', crumb='Zoho implementation', seo_title='Zoho Implementation for Manufacturers', service_name='Zoho implementation for manufacturers', service_type='Zoho implementation',
    desc='Zoho Inventory, Creator, CRM and Analytics set up for small manufacturers: what each covers, the gaps, three routes, a 12-week plan and regional notes.',
    label='Zoho implementation for manufacturers', h1='Zoho for manufacturers, set up properly and described honestly',
    lead='Zoho&rsquo;s standard apps handle stock, purchasing, sales and reporting well. They do not include a production module outside India. We fill that gap with an app built around your process, and tell you when an ERP is the better answer.',
    buttons=BTN + [('Zoho apps or an ERP?', G + 'zoho-or-manufacturing-erp/', 'btn-secondary')],
    facts=[('Stock and purchasing', 'Zoho Inventory'), ('Production and quality', 'Custom apps on Zoho Creator'), ('Reporting', 'Zoho Analytics')],
    hero=S, hero_alt='Cover: three Zoho products and their role for a manufacturer', sections=zoho,
    faqs=[('Does Zoho have a manufacturing module?',
           'Zoho Inventory does not; Zoho says so in its knowledge base and suggests composite items for simple assemblies. Zoho ERP includes manufacturing orders, job cards and work centres, but at the time of writing is published for India only. Elsewhere, production is usually built as a custom app on Zoho Creator.'),
          ('Is Zoho ERP included in Zoho One?',
           'No. At the time of writing Zoho ERP is licensed separately from Zoho One and is available for India.'),
          ('Can Zoho do MRP?',
           'The standard Zoho apps do not calculate material requirements from a forecast. Reorder points and per-job purchasing are supported. If you need full MRP, a manufacturing ERP is the better core system.'),
          ('How long does an implementation take?',
           'A first phase covering stock, one production workflow and the main integrations typically takes about twelve weeks. Clean item and customer data shortens it; complex routing and many integrations lengthen it.'),
          ('Can we keep Xero, MYOB or QuickBooks?',
           'Yes. We often keep the existing accounting package and integrate it with the order and production systems, sending invoices and bills and reading payment status back.'),
          ('Will our team be able to maintain it?',
           'That is the aim. We document the data model and workflows, comment the Deluge code and train an internal owner. Ongoing support is optional.')],
    cta=('Want to know which route fits your factory?', 'Tell us how you plan materials and send three bills of materials. You will get a straight answer, including when the answer is an ERP.'),
))

# ====================================================================== AI in manufacturing
S = 'hub-ai'
cover(S, 'AI in manufacturing', 'AI that prepares the work. People who decide.', 'Six practical uses for a small factory, each with its limits and a way to test it.',
      two(m_tiles([('1', 'Read', 'Orders and certificates'), ('2', 'Answer', 'Questions about your data'), ('3', 'Sort', 'Photos and requests'), ('4', 'Project', 'Usage from history')])),
      theme='navy', alt='Cover: four things AI does in a small factory: read documents, answer questions, sort photos and requests, and project usage')
X1 = fig(S + '-principles', m_check(['The task is narrow and happens often', 'A person can check the output quickly', 'A wrong answer is cheap to correct', 'The data already exists in a system', 'The AI cannot change records unaided', 'Accuracy is measured, not assumed']),
         'Six conditions for a good AI use case: narrow, checkable, cheap to correct, data exists, no unaided changes and measured accuracy',
         'Six tests we apply before recommending an AI use case. Failing two is usually enough to say no.', h=440, theme='navy', title='Our tests for a use case')
X2 = fig(S + '-pattern', m_cols([('Input', 'Something arrives', ['A PDF order', 'A photo', 'A question', 'A history of usage']), ('AI step', 'It is read or scored', ['Fields extracted', 'Category suggested', 'Records found', 'Trend projected'], True),
                                  ('Rules', 'It is checked', ['Against your lists', 'Against limits', 'For duplicates']), ('Person', 'Someone decides', ['Accept', 'Edit', 'Reject']), ('Record', 'Then it is saved', ['With the source', 'With who approved'])]),
         'Five-column pattern for AI workflows: input, AI step, rules, person and record',
         'The same five-part pattern sits behind every use case on this page.', h=500, theme='navy', title='One pattern, used six times')
X3 = fig(S + '-triage', app('Quality', 'Concept on Zoho Creator', ['Inspections', 'NCRs', 'Photo triage', 'Reports'], 'Photo triage', 'Defect photos awaiting category', '10 Oct &middot; 6 photos &middot; suggestions shown',
         panel('Suggested categories', table('96px minmax(0,1.1fr) minmax(0,1fr) 110px minmax(0,1fr) 110px', ['Photo', 'Part', 'Suggested', '>Confidence', 'Inspector says', 'Status'],
               [[('sn', 'IMG-4411'), 'Panel GP-7', 'Scratch', ('r', 'High'), 'Scratch', ('st', 'g', 'Accepted')], [('sn', 'IMG-4412'), 'Panel GP-7', 'Scratch', ('r', 'High'), 'Scratch', ('st', 'g', 'Accepted')],
                [('sn', 'IMG-4413'), 'Bracket BR-40', 'Dent', ('r', 'Low'), 'Hole position', ('st', 'y', 'Corrected')], [('sn', 'IMG-4414'), 'Frame F-200', 'Weld porosity', ('r', 'Medium'), '', ('st', 'b', 'To review')],
                [('sn', 'IMG-4415'), 'Frame F-200', 'Weld porosity', ('r', 'High'), '', ('st', 'b', 'To review')]]), 'the inspector makes the pass or fail call', 'flex:1')
         + note('Suggestions speed up recording. Corrections are logged and used to measure accuracy by category.')),
         'Illustrative defect photo triage screen listing photos with a suggested category, confidence level, the inspector&rsquo;s own category and status',
         'A concept triage screen. The model suggests a category; the inspector confirms or corrects it and decides pass or fail.', h=470, ui=True)
X4 = fig(S + '-forecast', app('Purchasing', 'Concept on Zoho Analytics', ['Reorder list', 'Usage forecast', 'Suppliers', 'Reports'], 'Usage forecast', 'Usage forecast: hinge 110&deg; soft-close', 'Weekly usage &middot; example data',
         g2(panel('Actual and projected weekly usage', svg_line([[190, 205, 198, 220, 210, 232, 225, 240, None, None, None, None], [None, None, None, None, None, None, None, 240, 246, 252, 258, 264]],
                                                                ['W34', '', 'W36', '', 'W38', '', 'W40', '', 'W42', '', 'W44', ''], w=560, h=250, ymin=140, ymax=300, names=['Actual', 'Projected'], dashed=(1,)), 'units per week'),
            panel('What the buyer sees', fields([('Current reorder point', '450'), ('Suggested', '520'), ('Reason', 'Usage trending up'), ('Not known to the model', 'Planned promotions')], 1)
                  + acts(('btnp', 'Update to 520'), ('btns', 'Keep 450')) + note('A projection from history. The buyer knows about orders the data does not.'), 'buyer decides'), '1.6fr')),
         'Illustrative usage forecast screen with a chart of actual and projected weekly usage and a suggested change to the reorder point for the buyer to accept or decline',
         'A concept forecast screen with example data. The projection is advice; the buyer changes the reorder point or leaves it.', h=560, ui=True)
X5 = fig(S + '-poc', m_timeline([('Week 1', 'Choose and define', 'One task, one pass mark'), ('Weeks 1-2', 'Collect examples', '50 to 100 with correct answers'), ('Weeks 3-4', 'Run alongside', 'AI drafts; people work as normal'), ('Week 5', 'Measure and decide', 'Go, change or stop')]),
         'Five-week proof of concept timeline: choose and define, collect examples, run alongside, then measure and decide',
         'Every use case starts with a proof of concept that is allowed to fail.', h=380, theme='navy', title='A five-week proof of concept')
X6 = fig(S + '-risk', m_table(['Risk', 'What it looks like', 'How the design answers it'],
                               [['Wrong output', 'A misread quantity or category', 'Human review before anything is saved'], ['Over-trust', 'Reviewers stop checking', 'Flags, spot audits and a visible accuracy log'],
                                ['Data exposure', 'Customer documents sent to a third party', 'Confirm processing terms; check contracts'], ['Too much access', 'An assistant that can change records', 'Read-only access; writes need a person'],
                                ['Service outage', 'The AI is unavailable', 'A manual route that always works']], '.7fr 1.1fr 1.3fr'),
         'Table of five risks in AI workflows with what each looks like and how the design answers it',
         'Five risks and the design answer to each. None of them is removed; all of them are managed.', h=500, theme='navy', title='Risks and controls')


def ai(ALL):
    pts = lambda *v: list(zip(['The problem', 'How it works', 'Data and integrations', 'Where Zoho or custom software fits', 'Expected benefits', 'Limitations', 'Security and human oversight', 'A small proof of concept'], v))
    ucs = (
        uc('uc-orders', 'Reading customer purchase orders', 'Document extraction', pts(
            'Customers send orders as PDFs in their own layouts, and someone retypes each one. It takes hours and produces occasional keying errors.',
            'A document model reads each PDF and fills in a draft sales order. Fixed rules check customer, items, prices, dates and duplicates. A person reviews the draft beside the original and confirms.',
            'Needs your customer list, item list with any customer part numbers, price lists and standard lead times. Reads from the orders inbox; writes to the order system only after confirmation.',
            'The review app is built on Zoho Creator, which includes OCR and custom models in its AI Modeler. An outside model can be connected where it reads your documents better.',
            'Less typing, same-day order entry, and price and date checks on every order instead of when time allows.',
            'Accuracy depends on document quality. Handwritten or photographed orders read poorly. New layouts need closer checking at first.',
            'The extraction service can read a document and nothing else. No order is created without a named person confirming. Every correction is logged.',
            'Take 100 past orders with the entries that were actually made. Measure field-level accuracy against a pass mark agreed in advance.'),
           (CS + 'ai-purchase-order-intake/', 'Read the reference implementation'))
        + uc('uc-supplier-docs', 'Reading supplier documents at goods in', 'Document extraction', pts(
            'Delivery notes and certificates carry lot numbers, dates and test values. Typing a 14-character lot number at a cold loading dock invites mistakes that break traceability.',
            'Stores photograph or scan the document. Lot number, quantity, dates and listed test values are extracted into the receipt, and the receiver confirms them against the label.',
            'Needs open purchase orders and the item list. Writes a goods receipt and lot record to the stock system after confirmation, with the document attached.',
            'A Creator form on a phone or tablet captures the image and shows the extracted fields. Zoho Inventory holds the lot, quantity and expiry date.',
            'Faster receiving, fewer mistyped lot numbers and certificates stored with the lot they belong to.',
            'Supplier layouts vary widely. Poor photographs and multi-lot delivery notes need manual correction. It reads what is printed; it cannot verify that the goods match.',
            'The receiver confirms every lot against the physical label. Typed overrides are flagged for a second check.',
            'Collect 50 delivery notes and certificates from your five main suppliers and measure how often lot number and date are read correctly.'),
           (G + 'batch-lot-traceability/', 'Read the traceability guide'))
        + uc('uc-assistant', 'Answering questions about operations', 'Language model with data access', pts(
            'Simple questions, such as which jobs are at risk or whether there is enough material for next week, require someone to open three systems and a spreadsheet.',
            'A language model is given read-only access to defined records. It turns a question into queries, totals the results and answers in a sentence, naming the records it used.',
            'Needs reliable work orders, holds, stock and purchase orders. If job status is not recorded as it happens, the answers will be wrong with great confidence.',
            'Zoho publishes an MCP server that lets an assistant read Zoho data with permission, and Zoho Analytics includes a plain-language assistant. A custom layer limits which records are exposed.',
            'Quicker answers for sales and managers, and fewer interruptions for the planner.',
            'It answers from data, so it inherits every error in the data. It can misread an ambiguous question. It is no use for anything not recorded.',
            'Read-only access, scoped to named modules. Every answer cites its source. No ability to create or change records.',
            'List the twenty questions asked most often. Test each against known answers and count how many are right.'),
           ('/insights/zoho-mcp-claude-chatgpt/', 'Read about connecting an assistant to Zoho'))
        + uc('uc-defects', 'Sorting defect photos', 'Image classification', pts(
            'Inspectors describe defects in their own words, so the same fault is recorded five ways and cause analysis becomes guesswork.',
            'When an inspector photographs a defect, a classifier suggests a category from your fixed list. The inspector accepts or corrects it and makes the pass or fail decision.',
            'Needs a few hundred labelled photos per category, taken in consistent lighting. Writes the category to the nonconformance record.',
            'Creator&rsquo;s AI Modeler supports object detection and custom models. The NCR workflow around it is a standard Creator app.',
            'More consistent categories, faster recording and cause charts that can be trusted.',
            'Sensitive to lighting, angle and camera. Rare defects have too few examples. It is not suitable as the sole judge of acceptance.',
            'The model suggests; the inspector decides. Low-confidence suggestions are marked. Corrections are tracked by category.',
            'Label 300 existing photos across four common defect types, hold back a quarter and measure how often the suggestion matches the inspector.'),
           (G + 'quality-ncr-capa-workflow/', 'Read the quality workflow guide'))
        + uc('uc-forecast', 'Projecting material usage', 'Prediction', pts(
            'Reorder points are set once and never revisited, so they drift away from real usage and cause stock-outs or excess.',
            'A model projects usage per item from history. Where the projection suggests a different reorder point, the buyer is shown the suggestion with the reason.',
            'Needs at least a year of reliable issue transactions per item. Reads stock movements; proposes changes to reorder points.',
            'Zoho Analytics includes forecasting over your stock data. Zoho Inventory holds the reorder points. A small report presents suggestions to the buyer.',
            'Reorder points that follow real usage, and a regular prompt to review them.',
            'Useless for new items and job-specific materials. It knows nothing about an order you are about to win or a product you are about to drop.',
            'Suggestions only. The buyer accepts or declines each change, and purchase orders are never sent automatically.',
            'Pick 30 steady items, project the last quarter from the year before it and compare with what was actually used.'),
           (G + 'purchasing-reorder-points/', 'Read the purchasing guide'))
        + uc('uc-requests', 'Triage of maintenance and support requests', 'Language model', pts(
            'Operators report machine problems in free text. Someone has to read each, work out the machine, the urgency and who should deal with it.',
            'A language model reads the request and proposes the machine, a category and a priority, and drafts a summary. The maintenance lead confirms before the job is assigned.',
            'Needs the machine list, categories and priority rules. Writes to a maintenance request app after confirmation.',
            'A Creator app holds requests, assignments and history. The model is called from a workflow; Zoho&rsquo;s agent tools allow connecting your own account with a model provider.',
            'Faster routing, more consistent priorities and a searchable history per machine.',
            'It can misjudge urgency from a short message. It does not replace a safety procedure: anything safety-related follows your existing rules first.',
            'A person confirms priority and assignment. Requests containing safety keywords bypass the model and go straight to a named person.',
            'Run the last 200 requests through the model and compare its category and priority with what the maintenance lead chose.'))
    )
    return (
        sec('stance', 'Our position', 'Where AI helps a factory, and where it does not', '''        <div class="split">
          <div>
            <p>AI is good at reading, sorting, searching and projecting. It is poor at judgement, and it cannot tell which of its own answers are wrong. That makes it a useful assistant and a bad decision-maker.</p>
            <p>Every use case below is designed the same way: the AI prepares something, rules check it, and a named person decides. We do not build systems that place orders, release product or change schedules by themselves.</p>
            <p>This page describes what we would build and how we would test it. It does not claim results. A proof of concept on your own documents is the only honest source of numbers.</p>
          </div>
          <ul class="chip-list">
            <li>Document extraction</li><li>Prediction</li><li>Language models</li><li>Image classification</li><li>Human review</li><li>Read-only access</li><li>Accuracy logs</li>
          </ul>
        </div>''')
        + sec('tests', 'Choosing', 'Six tests for a use case', X1 + '\n' + X2
              + '\n        <p>Our guide to <a href="' + G + 'ai-for-small-manufacturers/">AI for small manufacturers</a> explains the reasoning, including a risk and readiness grid for placing your own ideas.</p>', alt=True)
        + sec('use-cases', 'Use cases', 'Six use cases, each with its limits', ucs,
              intro='Each card covers the same eight points, so you can compare them: the problem, how it works, the data needed, where Zoho or custom software fits, benefits, limitations, oversight and a small test.')
        + sec('screens', 'What it looks like', 'Two concept screens', figgrid(X3, X4)
              + '\n        <p>Both screens are concept mockups with example data. In each, the AI output is a suggestion beside a decision that belongs to a person.</p>', alt=True)
        + sec('risks', 'Risks', 'Risks, and how the design answers them', X6
              + '\n        <p>Before any AI feature handles your documents, ask the provider where data is processed, whether it is retained, whether it is used for training and what the service can change. Answers differ by product, plan and region, so we confirm them for the specific service at the start of a project.</p>')
        + sec('poc', 'Getting started', 'Start with a proof of concept', X5 + '\n' + path([
            ('Choose one task', 'Narrow, frequent and easy to check. Agree the pass mark before testing.'),
            ('Collect real examples', 'Fifty to a hundred, with the correct answers taken from what your people actually did.'),
            ('Run alongside', 'The AI drafts while people work as normal. Nothing depends on it yet.'),
            ('Decide on evidence', 'Go live, change the approach or stop. All three are acceptable outcomes.')]), alt=True)
        + sec('learn', 'Go deeper', 'Related reading', cards(ALL, [ALL[s] for s in ('ai-for-small-manufacturers', 'ai-purchase-order-intake', 'manufacturing-dashboards-kpis')]))
    )


PAGES.append(dict(
    route=M + 'ai-automation/', crumb='AI automation', seo_title='AI in Manufacturing: Practical Use Cases', service_name='AI automation for manufacturers', service_type='AI workflow automation',
    desc='Six practical AI use cases for small manufacturers, each with how it works, data needed, limits, human oversight and a small proof of concept.',
    label='AI in manufacturing', h1='AI that prepares the work, with people who decide', tone='dark',
    lead='Reading purchase orders, checking supplier documents, answering questions about your own data. Useful, narrow and testable. We design every AI workflow with a review step, and we start with a proof of concept that is allowed to fail.',
    buttons=[('Discuss a Use Case', '/contact/', 'btn-primary'), ('Read the AI guide', G + 'ai-for-small-manufacturers/', 'btn-secondary')],
    facts=[('Pattern', 'AI prepares, rules check, a person decides'), ('First step', 'A five-week proof of concept'), ('AI can change', 'Nothing without confirmation')],
    hero=S, hero_alt='Cover: four things AI does in a small factory', sections=ai,
    faqs=[('What can AI realistically do in a small factory today?',
           'Read documents such as purchase orders and certificates, answer questions about data you already hold, suggest categories for defect photos and requests, and project usage from history. In each case it prepares work for a person to check.'),
          ('Will AI replace our staff?',
           'Not in any design we build. It removes typing, searching and sorting. Decisions about orders, quality, purchasing and scheduling stay with the people responsible for them.'),
          ('Is our data used to train AI models?',
           'It depends on the service and plan. Some providers do not train on business data by default and others need a setting or contract term. We confirm this for the specific service before any documents are processed.'),
          ('Do we need Zoho to use these?',
           'No, but it helps if your data is already there. Zoho Creator and Zoho Analytics include AI features, and Zoho publishes an MCP server for assistants. The same patterns work with other systems through their APIs.'),
          ('How much does an AI project cost?',
           'A proof of concept is small and fixed in scope. The full build depends on the use case and integrations, and running costs depend on volume and the service chosen. We estimate both after the proof of concept, when the numbers are real.'),
          ('What if the proof of concept fails?',
           'Then you have spent a few weeks and learned that the task is not ready, usually because of document quality or missing data. That is a useful result and far cheaper than finding out after go-live.')],
    cta=('Have a task you think AI could take on?', 'Describe it and send a few sample documents. We will tell you whether it passes our six tests and what a proof of concept would involve.',
         ('Discuss a Use Case', '/contact/'), ('See How We Price', '/pricing/')),
))

# ====================================================================== Workflows
S = 'hub-workflows'
cover(S, 'Workflows', 'Manufacturing workflows that people actually follow', 'Eight processes, each designed as a few scans and taps at the point of work.',
      m_vt([('Trigger', 'Something happens', 'An order, a low stock level, a failed check'), ('Steps', 'People act', 'One scan and one or two taps each'), ('Rules', 'The system checks', 'Validation, approvals, escalation'), ('Record', 'It is saved once', 'And passed to the systems that need it')]),
      theme='green', alt='Cover: the four parts of a workflow: trigger, steps, rules and record')
W1 = fig(S + '-map', m_pills([('Sell', ['Quote to order', 'Order status for customers']), ('Buy and store', ['Purchasing and approvals', 'Receiving and lot labels', 'Cycle counting']),
                               ('Make', ['Production tracking', 'Holds and rework', 'Batch records']), ('Check', ['Inspections', 'NCR and CAPA', 'Maintenance requests']), ('Ship and bill', ['Pick, pack and ship', 'Invoice from shipment'])]),
         'Map of manufacturing workflows grouped into sell, buy and store, make, check, and ship and bill',
         'The workflows we are asked for most, grouped by where they sit in the business.', h=520, theme='green', title='Workflow map')
W2 = fig(S + '-anatomy', m_cols([('1', 'Trigger', ['Order confirmed', 'Stock below level', 'Inspection failed', 'A scheduled time']), ('2', 'Steps', ['Scan to identify', 'Enter the minimum', 'Photo if useful'], True),
                                  ('3', 'Rules', ['Validate the entry', 'Route for approval', 'Escalate if late']), ('4', 'Record', ['Saved once', 'Sent to other systems', 'Shown on a board'])]),
         'Anatomy of a workflow in four parts: trigger, steps, rules and record',
         'Every workflow we design has the same four parts. The second column is where most of the design effort goes.', h=420, theme='green', title='Anatomy of a workflow')
W3 = fig(S + '-approvals', app('Approvals', 'Concept on Zoho Creator', ['Waiting for me', 'Sent by me', 'Completed', 'Rules'], 'Waiting for me', 'Waiting for your decision', 'Operations manager &middot; 4 items',
         panel('Approvals inbox', table('110px minmax(0,1.5fr) minmax(0,1fr) 100px 100px 110px', ['Type', 'What', 'Requested by', '>Value', 'Waiting', 'Action'],
               [['Purchase order', 'Hinges &times; 1,000, drawer runners &times; 200', 'Buyer', ('r', 'Mid band'), '1 day', ('st', 'b', 'Decide')], ['Use as is', 'NCR-0321: colour variance on 40 panels', 'Quality lead', ('r', ''), '3 hours', ('st', 'b', 'Decide')],
                ['Hold release', 'J-1035: recut doors received', 'Planner', ('r', ''), '20 min', ('st', 'b', 'Decide')], ['Stock adjustment', 'MDF 18 mm: count 19, system 22', 'Stores', ('r', '3 sheets'), '2 days', ('st', 'r', 'Overdue')]]), 'oldest first; overdue items escalate', 'flex:1')
         + note('Each row opens the record with the evidence attached: the quote, the photo, the count sheet.')),
         'Illustrative approvals inbox listing four items waiting for a manager: a purchase order, a use-as-is decision, a hold release and a stock adjustment',
         'A concept approvals inbox. One place for every decision a manager owes, with waiting time shown.', h=500, ui=True)
W4 = fig(S + '-maint', phones([phone('Report a fault', 'Laser cutter 1', pscan('Scan machine tag') + pf('Problem', 'Nozzle fault, cut quality') + pf('Machine stopped?', 'Yes') + pf('Photo', 'Added') + pbtn('Send request', 'b')),
                               phone('My requests', 'Maintenance &middot; 3 open', pf('MR-077 &middot; Drill jig 3', 'Bush worn &middot; High') + pf('MR-081 &middot; Laser cutter 1', 'Nozzle fault &middot; High') + pf('MR-079 &middot; Compressor', 'Service due &middot; Planned') + pbtn('Start MR-081'))],
                              [('Scan the machine', 'A tag on each machine identifies it; nobody types an asset number.'), ('Stopped or running', 'One question sets the priority.'), ('History per machine', 'Every request builds a record that planned maintenance can use.')]),
         'Two illustrative phone screens for maintenance: reporting a machine fault by scanning its tag, and a technician&rsquo;s list of open requests',
         'Concept maintenance screens. Reporting a fault takes one scan, one choice and a photo.', h=600, theme='green', ui=True)
W5 = fig(S + '-design', m_dd(['One scan identifies the job, lot or machine', 'Three fields or fewer per step', 'Reasons chosen from a short list', 'Large buttons for gloved hands', 'The old sheet removed on go-live'],
                              ['Typing long codes', 'Forms copied from the paper version', 'Free-text reasons nobody can count', 'A login on every scan', 'Running paper and app side by side'], ('On the floor, do', 'On the floor, avoid')),
         'Two lists of shop-floor design rules to follow and to avoid, five each',
         'Design rules for anything used on a shop floor. The right-hand list is where most failed rollouts went wrong.', h=480, theme='green')
W6 = fig(S + '-ship', app('Dispatch', 'Concept on Zoho Inventory data', ['Ready to pick', 'Picking', 'Packed', 'Shipped'], 'Ready to pick', 'Orders ready to pick', 'Friday 10 Oct &middot; 5 orders',
         kpis([('Ready to pick', '5', 'orders', 'fl'), ('Picking now', '2', '', 'fl'), ('Shipped today', '7', '', 'fl'), ('Short picks', '1', 'needs a decision', 'dn')])
         + panel('Pick queue', table('110px minmax(0,1.2fr) 80px minmax(0,1fr) 110px 110px', ['Order', 'Customer', '>Lines', 'Carrier', 'Ship by', 'Status'],
                 [[('sn', 'SO-7790'), 'Builder B', ('r', '6'), 'Own truck', 'Today', ('st', 'g', 'Ready')], [('sn', 'SO-7795'), 'Fit-out customer A', ('r', '3'), 'Courier', 'Today', ('st', 'g', 'Ready')],
                  [('sn', 'SO-7802'), 'Retail chain C', ('r', '12'), 'Freight', 'Monday', ('st', 'y', 'Short 1 line')], [('sn', 'SO-7804'), 'Fit-out customer D', ('r', '2'), 'Courier', 'Monday', ('st', 'g', 'Ready')]]), 'shipping creates the draft invoice', 'flex:1')),
         'Illustrative dispatch screen with counts of orders ready, picking and shipped, and a pick queue showing customer, lines, carrier, ship-by date and status',
         'A concept dispatch queue. Posting the shipment reduces stock and drafts the invoice in one step.', h=520, ui=True)


def wf(wid, title, kind, trig, steps, recs, conn, link):
    return uc(wid, title, kind, [('Trigger', trig), ('Steps on the floor', steps), ('Records created', recs), ('Connects to', conn)], link)


def workflows(ALL):
    blocks = (
        wf('wf-production', 'Production tracking', 'Make', 'A confirmed sales order, or a stock order raised by the planner.', 'Scan the job card to start a stage; record good and scrap quantities to finish it. Put the job on hold with a reason if something is wrong.',
           'Work order, stage logs with times, scrap with reasons, holds.', 'CRM for order status, stock system for materials issued and finished goods.', (G + 'production-tracking-zoho-creator/', 'Build guide: production tracking in Zoho Creator'))
        + wf('wf-inventory', 'Inventory and cycle counting', 'Buy and store', 'A scheduled count list for the day, or a movement on the floor.', 'Scan the bin, scan the item, enter the count. Differences beyond tolerance go to a supervisor before stock is adjusted.',
             'Count records, adjustments with a reason, accuracy by week.', 'Stock system for quantities; dashboards for record accuracy.', (G + 'inventory-accuracy-for-manufacturers/', 'Guide: why stock records drift'))
        + wf('wf-purchasing', 'Purchasing and approvals', 'Buy and store', 'Stock falls to its reorder point, or a job needs a material bought to order.', 'The buyer reviews a suggested order, adjusts and submits. Approval follows value bands. Stores receive against the order.',
             'Purchase order, approval history, goods receipt, three-way match.', 'Stock system and accounts for bills.', (G + 'purchasing-reorder-points/', 'Guide: reorder points and approvals'))
        + wf('wf-traceability', 'Batch and lot traceability', 'Make', 'A delivery arrives, a batch starts or a pallet ships.', 'Scan the supplier label at goods in, scan each lot into the batch, scan pallets to orders.',
             'Lot receipts, batch records with lots consumed, dispatch links, mock recall results.', 'Stock system for lots and expiry dates; label printer.', (G + 'batch-lot-traceability/', 'Guide: what to record at each step'))
        + wf('wf-quality', 'Inspections, NCR and CAPA', 'Check', 'A planned inspection point, a failed check or a customer complaint.', 'Record the result with a photo. A fail raises an NCR and holds the stock. A named person chooses the disposition.',
             'Inspection results, NCRs with cause and disposition, corrective actions with effectiveness checks.', 'Stock system for holds and scrap; production for rework steps.', (G + 'quality-ncr-capa-workflow/', 'Guide: digital quality control'))
        + wf('wf-maintenance', 'Maintenance requests', 'Check', 'An operator notices a fault, or a planned service falls due.', 'Scan the machine tag, choose the problem, say whether the machine is stopped and add a photo. The technician accepts and closes the job with notes.',
             'Requests, downtime, parts used and a history per machine.', 'Production holds, so a stopped machine shows on the board.', None)
        + wf('wf-order', 'Quote to order', 'Sell', 'A customer accepts a quote.', 'Sales marks the quote as won. Items, quantities and the promised date carry through without retyping.',
             'Sales order with one number used on every later record.', 'Production for the work order, stock for reservations, accounts for the invoice.', (G + 'connect-sales-production-accounts/', 'Guide: connecting sales, production and accounts'))
        + wf('wf-dispatch', 'Pick, pack, ship and invoice', 'Ship and bill', 'A job is marked ready, or stock is available for an order.', 'Pick from the list, scan items or pallets to the order, confirm the shipment.',
             'Shipment with lots or serials, proof of delivery, draft invoice.', 'Stock system to reduce stock, carriers, accounts for the invoice.', None)
    )
    return (
        sec('approach', 'Approach', 'Workflows are designed for the person doing the work', '''        <div class="split">
          <div>
            <p>A workflow fails when it asks a machinist to type a twelve-digit job number into a form copied from a paper sheet. It works when the job card is scanned, one number is entered and a large button is pressed.</p>
            <p>We design from the floor inwards. The first screen built is the one an operator uses, and it is trialled at one bench before anything else exists. Dashboards come last, because they can only show what the floor records.</p>
          </div>
          <ul class="chip-list">
            <li>Scan to identify</li><li>Three fields or fewer</li><li>Reasons from a list</li><li>Holds with an owner</li><li>Approvals by value</li><li>Escalation when late</li><li>One record, shared</li>
          </ul>
        </div>''')
        + sec('map', 'Scope', 'The workflows we build', W1 + '\n' + W2, alt=True)
        + sec('catalogue', 'Catalogue', 'Eight workflows in detail', blocks,
              intro='Each entry gives the trigger, what people do, what is recorded and what it connects to, with a link to the full guide where we have written one.')
        + sec('screens', 'What it looks like', 'Concept screens', W3 + '\n' + figgrid(W4, W6)
              + '\n        <p>These are concept mockups with example data, drawn to show the level of simplicity we aim for. They are not screenshots of Zoho products or of a customer system.</p>', alt=True)
        + sec('design-rules', 'Design rules', 'What makes a shop-floor workflow stick', W5
              + '\n        <p>The last rule on the left matters most. While the paper sheet is still on the bench, people will fill in both, trust neither and blame the app. Agree the date the old method is removed before the trial starts.</p>')
        + sec('built-with', 'Technology', 'What these are built with', '''        <div class="split">
          <p>Most of these workflows are apps on <a href="/zoho-creator-development/">Zoho Creator</a>, which provides forms, native mobile apps, barcode and QR scanning on phones and tablets, approvals, Blueprint stages, schedules and role-based access. Logic is written in <a href="/deluge-development/">Deluge</a>. Stock and purchasing sit in Zoho Inventory or your existing system, connected through <a href="/zoho-integrations/">integrations</a>. Where a process does not fit a platform, we build <a href="/custom-software-development/">custom software</a>.</p>
          <ul class="chip-list">
            <li>Zoho Creator</li><li>Deluge</li><li>Zoho Inventory</li><li>Zoho Flow</li><li>Zoho Analytics</li><li>REST APIs</li>
          </ul>
        </div>''', alt=True)
        + sec('learn', 'See it applied', 'Reference implementations', cards(ALL, ALL['_cases']))
    )


PAGES.append(dict(
    route=M + 'workflows/', crumb='Workflows', seo_title='Manufacturing Workflow Automation', service_name='Manufacturing workflow automation', service_type='Business process automation',
    desc='Eight manufacturing workflows designed for the shop floor: production tracking, stock, purchasing, traceability, quality, maintenance, orders and dispatch.',
    label='Manufacturing workflows', h1='Manufacturing workflows that people actually follow', tone='green',
    lead='Job tracking, traceability, quality, purchasing and maintenance, designed as a scan and a couple of taps for the person doing the work, and connected so nothing is entered twice.',
    buttons=BTN + [('See the workflows', '#catalogue', 'btn-secondary')],
    facts=[('Designed for', 'Operators, stores and inspectors'), ('Built on', 'Zoho Creator and Deluge'), ('Connected to', 'Stock, CRM and accounts')],
    hero=S, hero_alt='Cover: the four parts of a workflow', sections=workflows,
    faqs=[('Which workflow should we automate first?',
           'The one that causes the most daily pain and is simple enough to finish in a few weeks. For most small manufacturers that is production tracking or quality records.'),
          ('Do operators need their own devices?',
           'Usually not. One shared tablet or handheld per work area is enough. Operators scan a job card or machine tag and tap one or two buttons.'),
          ('Will it work without internet on the shop floor?',
           'Zoho Creator offers offline access on mobile with restrictions, so it depends on the workflow. We check coverage and test on your devices during the trial, and keep a paper fallback for outages.'),
          ('Can these workflows connect to our existing ERP?',
           'Yes, if the ERP has an API or supports imports. The workflow app records the work and passes results to the ERP, which remains the system of record.'),
          ('How long does one workflow take to build?',
           'A single workflow with a floor screen, rules and a board typically takes three to five weeks including a trial. Integrations and reporting add to that.')],
    cta=('Which process costs you the most time?', 'Describe it in a few lines. We will sketch the workflow, tell you what it would connect to and give you a price before you commit.'),
))

# ====================================================================== Guides hub
S = 'hub-guides'
cover(S, 'Guides', 'Manufacturing guides', 'Ten practical guides on stock, production, quality, purchasing, integration and AI.',
      two(m_tiles([('10', 'Guides', 'Each on one topic'), ('60+', 'Diagrams', 'Formulas, flows and screens'), ('3', 'By our CTO', 'Seven by the dev team'), ('0', 'Invented statistics', 'Sources are listed')])),
      theme='blue', alt='Cover: the manufacturing guides library, ten guides with diagrams and listed sources')


def guides_hub(ALL):
    by = lambda *sl: [ALL[s] for s in sl]
    return (
        sec('start', 'Start here', 'If you read only three', cards(ALL, by('spreadsheets-to-connected-system-roadmap', 'zoho-or-manufacturing-erp', 'inventory-accuracy-for-manufacturers')),
            intro='A plan, a software decision and the data problem that undermines both.')
        + sec('floor', 'On the floor', 'Production, quality and traceability', cards(ALL, by('production-tracking-zoho-creator', 'quality-ncr-capa-workflow', 'batch-lot-traceability')), alt=True)
        + sec('office', 'In the office', 'Purchasing, integration and reporting', cards(ALL, by('purchasing-reorder-points', 'connect-sales-production-accounts', 'manufacturing-dashboards-kpis')))
        + sec('ai', 'AI', 'Artificial intelligence, without the hype', cards(ALL, by('ai-for-small-manufacturers')), alt=True)
        + sec('how-written', 'About these guides', 'How the guides are written', checks([
            'Each explains one topic, with a short answer at the top', 'Formulas come with a worked example', 'Diagrams and concept screens are drawn for the guide and labelled',
            'Product facts were checked against the vendor&rsquo;s own pages, which are listed', 'Example businesses are illustrations, not clients', 'No statistics are quoted without a source'])
              + '\n        <p>Three guides are written by our CTO, Arunkumar V, and seven by the development team. Corrections are welcome through the <a href="/contact/">contact page</a>.</p>')
        + sec('cases', 'See it applied', 'Illustrative case studies', cards(ALL, ALL['_cases']), alt=True)
    )


PAGES.append(dict(
    route=G, crumb='Guides', seo_title='Manufacturing Guides for Small Manufacturers', collection='_guides',
    desc='Ten practical manufacturing guides: inventory accuracy, production tracking, traceability, quality, purchasing, KPIs, integration, software choice and AI.',
    label='Manufacturing guides', h1='Practical guides for small manufacturers',
    lead='Ten guides on the problems we are asked about most. Each one explains a topic properly, with formulas, worked examples, diagrams and the mistakes to avoid.',
    buttons=[('Start with the roadmap', G + 'spreadsheets-to-connected-system-roadmap/', 'btn-primary'), ('Illustrative case studies', CS, 'btn-secondary')],
    hero=S, hero_alt='Cover: the manufacturing guides library', sections=guides_hub, service_name='', service_type='',
    cta=('Want a guide applied to your factory?', 'Tell us which topic is closest to your problem. We will talk it through and suggest a first step.'),
))

# ====================================================================== Case studies hub
S = 'hub-cases'
cover(S, 'Case studies', 'Illustrative manufacturing case studies', 'Reference implementations for composite businesses. Not client projects.',
      m_rows([('Job tracking for a joinery', 'By Arunkumar V, CTO'), ('Batch traceability for a bakery', 'By the development team'), ('AI-assisted order intake', 'By the development team')]),
      theme='green', solid=True, alt='Cover: three illustrative manufacturing case studies: job tracking, batch traceability and AI-assisted order intake')
H1 = fig(S + '-structure', m_pills([('The situation', ['Executive summary', 'Business context', 'Challenges', 'Existing process', 'Root causes']), ('The design', ['Solution', 'Architecture', 'Workflow', 'Before and after', 'Stages']),
                                     ('The detail', ['Integrations and data', 'Security and exceptions', 'Benefits and limits', 'What could come next'])]),
         'The fifteen sections of each case study grouped into the situation, the design and the detail',
         'Every case study follows the same structure, so they can be compared.', h=440, theme='green', title='What each case study covers')


def cases_hub(ALL):
    return (
        sec('what', 'Read this first', 'What &ldquo;illustrative&rdquo; means here', '''        <div class="split">
          <div>
            <p>These case studies are reference implementations. Each describes a composite business, built from the kind of manufacturer that asks us for this work, and the design we would propose for it.</p>
            <p>They are not accounts of client projects. No client is named, no customer is quoted and no savings or improvements are claimed as measured. Screens are concept mockups, and any names or numbers inside them are made-up example data.</p>
            <p>We publish them because a worked design teaches more than a list of features. When we have client stories that customers have approved for publication, they will be labelled as such and kept separate.</p>
          </div>
          <ul class="chip-list">
            <li>Composite businesses</li><li>No client names</li><li>No invented results</li><li>Concept screens</li><li>Limits stated</li>
          </ul>
        </div>''', narrow=False)
        + sec('list', 'Reference implementations', 'Three illustrative case studies', cards(ALL, ALL['_cases']), alt=True)
        + sec('structure', 'Format', 'What each one covers', H1
              + '\n        <p>Each runs to fifteen sections: summary, context, challenges, the existing process, root causes, the proposed solution, architecture, the workflow step by step, before and after, implementation stages, integrations, security and exceptions, expected benefits and limitations, future improvements and a next step.</p>')
        + sec('guides', 'Background', 'Guides behind the designs', cards(ALL, [ALL[s] for s in ('production-tracking-zoho-creator', 'batch-lot-traceability', 'ai-for-small-manufacturers')]), alt=True)
    )


PAGES.append(dict(
    route=CS, crumb='Case studies', seo_title='Illustrative Manufacturing Case Studies', collection='_cases',
    desc='Three illustrative manufacturing case studies: job tracking for a joinery, batch traceability for a bakery and AI-assisted purchase order intake.',
    label='Illustrative case studies', h1='Illustrative manufacturing case studies', tone='green',
    lead='Reference implementations that show how we would solve a real kind of problem, from root cause to architecture to rollout. The businesses are composites, not clients, and no results are claimed.',
    buttons=[('Read the joinery case study', CS + 'job-tracking-joinery-manufacturer/', 'btn-primary'), ('Browse the guides', G, 'btn-secondary')],
    hero=S, hero_alt='Cover: three illustrative manufacturing case studies', sections=cases_hub, service_name='', service_type='',
    faqs=[('Are these real customer projects?',
           'No. They are illustrative reference implementations for composite businesses. No client names, quotes, logos or measured results are used.'),
          ('Why publish illustrative case studies?',
           'A complete worked design, with its architecture, workflow, controls and limits, is more useful to a manufacturer weighing a project than a list of features. Labelling it clearly as illustrative keeps it honest.'),
          ('Are the screens real software?',
           'They are concept mockups drawn for these pages, with example data. They are not screenshots of Zoho products or of a live customer system.'),
          ('Can you build what a case study describes?',
           'Yes. Each describes a design we would be comfortable building. Your version would start with a walk through your own process, because the details always differ.')],
    cta=('Have a process like one of these?', 'Send us a description of how it runs today. We will tell you what we would build first, what we would leave alone and what it would cost.'),
))
