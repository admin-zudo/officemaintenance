"""Illustrative manufacturing case studies (reference implementations).

None of these is a client project. Each describes a composite business and a design we would build for it.
Do not add client names, quotes, logos or measured results here unless they are real and approved in writing.
"""
from content_common import *

CASES = []
SEC = ['summary', 'context', 'challenges', 'existing-process', 'root-cause', 'solution', 'architecture', 'workflow', 'before-after',
       'stages', 'integrations', 'controls', 'benefits', 'future', 'next']


def sections(titles, bodies):
    assert len(titles) == len(bodies) == 15, (len(titles), len(bodies))
    return [(SEC[i], titles[i], bodies[i]) for i in range(15)]


# ====================================================================== 1. Job tracking for a joinery (Arunkumar V)
S = 'job-tracking-joinery-manufacturer'
cover(S, 'Illustrative case study', 'Job tracking for a custom joinery', 'From a whiteboard and phone calls to live job status on the workshop floor.',
      m_vt([('Problem', 'Nobody knows where a job is', 'Status lives on a whiteboard'), ('Design', 'Scan at every stage', 'A Zoho Creator app on shared tablets'), ('Links', 'Orders, stock and invoices', 'One order number throughout'), ('Result', 'Status without asking', 'Stated as a direction, not a figure')]),
      theme='blue', alt='Cover: solution blueprint for job tracking for a custom joinery, summarised as problem, design, connections and expected result')
J1 = fig(S + '-before', m_lanes(['Quote', 'Plan', 'Make', 'Deliver'], [
            ('Office', [('Quote in a spreadsheet', 'Emailed as a PDF'), ('Job sheet typed again', 'Printed, walked to the floor', 'warn'), None, ('Invoice typed a third time', 'From the delivery docket', 'warn')]),
            ('Workshop', [None, ('Whiteboard updated', 'When someone remembers', 'warn'), ('Stages done', 'Not recorded anywhere', 'warn'), None]),
            ('Stores', [None, ('Board ordered by phone', 'From the job sheet'), ('Hardware taken from shelves', 'No record', 'warn'), None])]),
         'Swimlane of the existing process across office, workshop and stores, with the weak points highlighted',
         'The existing process. Red cells are where information was retyped or never recorded.', h=460, title='How a job ran before')
J2 = fig(S + '-causes', m_rows([('Status was a memory, not a record', 'The whiteboard showed what someone last wrote, not what had happened', ''), ('One job, three documents', 'Quote, job sheet and invoice were separate files with separate numbers', ''),
                                 ('Problems had no channel', 'A missing panel was a conversation, so nobody could count them', '')]),
         'Three root causes: status held in memory, three unlinked documents per job, and no channel for problems',
         'Three causes behind a dozen symptoms.', h=420, title='Root causes')
J3 = fig(S + '-arch', m_arch([('People', 'who uses it', ['Sales and estimating', 'Planner', 'Machinists and assemblers', 'Installers', 'Accounts']),
                               ('Job tracker', 'a Zoho Creator app', ['Work orders', 'Stage logs', 'Holds', 'Install bookings', 'Photos'], True),
                               ('Standard apps', 'each owns its own records', ['CRM: customers and quotes', 'Stock: board and hardware', 'Accounts: invoices']),
                               ('Reporting', 'Zoho Analytics', ['Jobs by stage', 'On-time delivery', 'Holds by reason'])]),
         'Solution architecture: people use a job tracker built on Zoho Creator, which exchanges data with CRM, stock and accounting apps, with reporting above',
         'The proposed architecture. The custom app covers only what the standard apps do not.', h=540, title='Solution architecture')
J4 = fig(S + '-board', app('Job Tracker', 'Concept on Zoho Creator', ['Board', 'Work orders', 'Holds', 'Installs', 'Reports'], 'Board', 'Workshop board', 'Thursday 8 Oct &middot; 13 jobs open',
         kanban([('Cutting', [('J-1042 &middot; Kitchen, 14 units', 'Due 16 Oct', ('g', 'On track')), ('J-1047 &middot; Shop counter', 'Due 20 Oct', ('g', 'On track'))]),
                 ('Edging', [('J-1039 &middot; Vanities &times; 12', 'Due 14 Oct', ('y', 'Due soon'))]),
                 ('Assembly', [('J-1035 &middot; Wardrobes &times; 6', 'Due 12 Oct', ('r', 'On hold')), ('J-1038 &middot; Reception desk', 'Due 15 Oct', ('g', 'On track'))]),
                 ('Finishing', [('J-1031 &middot; Kitchen, 22 units', 'Due 9 Oct', ('y', 'Due soon'))]),
                 ('Ready', [('J-1029 &middot; Shelving', 'Install booked 9 Oct', ('b', 'Booked'))])])),
         'Concept workshop board with jobs shown as cards in five stage columns, each with a due date and status',
         'Concept workshop board. It replaces the whiteboard, and it updates when an operator scans a job card.', h=480, ui=True)
J5 = fig(S + '-floor', phones([phone('Scan a job', 'Assembly bench 2', pscan('Scan the job card') + pf('Job', 'J-1038 &middot; Reception desk') + pf('Stage', 'Assembly') + pbtn('Start', 'b')),
                               phone('Finish stage', 'J-1038 &middot; Assembly', pf('Units completed', '1 of 1') + pf('Problems', 'None') + pf('Photo', 'Added') + pbtn('Complete stage')),
                               phone('Report a problem', 'J-1035 &middot; Assembly', pf('Reason', 'Part missing') + pf('Detail', 'Two doors short') + pf('Photo', 'Added') + pbtn('Put on hold', 'b'))]),
         'Three concept tablet screens for workshop staff: scan a job, finish a stage and report a problem',
         'Concept floor screens. Each takes one scan and one or two taps, with large buttons for gloved hands.', h=560, ui=True)
J6 = fig(S + '-job', app('Job Tracker', 'Concept on Zoho Creator', ['Board', 'Work orders', 'Holds', 'Installs', 'Reports'], 'Work orders', 'J-1035 &middot; Wardrobes &times; 6', 'Sales order SO-7781 &middot; due 12 Oct &middot; on hold since 7 Oct',
         stepper([('Cutting', 'd'), ('Edging', 'd'), ('Assembly', 'c'), ('Finishing', ''), ('Ready', ''), ('Installed', '')])
         + g2(panel('Stage log', table('minmax(0,1fr) 96px 96px minmax(0,1fr)', ['Stage', 'Started', 'Finished', 'By'],
                    [['Cutting', '5 Oct 08:20', '5 Oct 14:10', 'Machinist 1'], ['Edging', '6 Oct 07:45', '6 Oct 11:30', 'Machinist 2'], ['Assembly', '7 Oct 08:05', ('st', 'r', 'On hold'), 'Assembler 1']]), 'from floor scans'),
              panel('Open hold', listing([('r', 'Part missing: two doors short', 'Reported 7 Oct 09:40 with photo'), ('y', 'Planner: recut requested', 'Linked job J-1035-R, cutting today'), ('', 'Customer told of new date', 'Sales notified automatically')]) + acts(('btnp', 'Release hold'), ('btns', 'Add note')), 'owner: planner'), '1.3fr')),
         'Concept job detail screen with a six-stage progress bar, a stage log from floor scans and an open hold with its actions',
         'Concept job screen. Everything known about the job sits in one place, including why it stopped.', h=440, ui=True)
J7 = fig(S + '-ba', m_ba(dict(k='Before', h='Status by asking', li=['Whiteboard updated by memory', 'Three documents per job', 'Problems raised in passing', 'Invoice typed from a docket']),
                          dict(k='After', h='Status by scanning', li=['Board updates from floor scans', 'One order number throughout', 'Holds with a reason and an owner', 'Draft invoice created on delivery'])),
         'Before and after comparison of the job process: status by asking against status by scanning, four points each',
         'The change in one picture. No figures are claimed; these are differences in how the work is done.', h=460)
J8 = fig(S + '-stages', m_timeline([('Weeks 1-2', 'Map and design', 'Walk the floor, agree stages and hold reasons'), ('Weeks 3-5', 'Build and trial', 'One bench, printed job cards, one tablet'),
                                     ('Weeks 6-8', 'Connect', 'Orders in, draft invoices out'), ('Weeks 9-10', 'Report and hand over', 'Dashboard, training, whiteboard removed')]),
         'Four implementation stages over ten weeks: map and design, build and trial, connect, then report and hand over',
         'A staged plan. Each stage ends with something in daily use.', h=380, title='Implementation stages')
J9 = fig(S + '-dash', app('Job Tracker', 'Concept on Zoho Analytics', ['Board', 'Work orders', 'Holds', 'Installs', 'Reports'], 'Reports', 'Workshop report', 'Last 8 weeks &middot; example data',
         kpis([('Jobs open', '13', '2 on hold', 'fl'), ('Due this week', '5', '1 at risk', 'dn'), ('Avg days on hold', '1.6', 'per held job', 'fl'), ('Jobs with no stage', '0', 'all scanned', 'up')])
         + g2(panel('Hours on hold by reason', bars2([('Part missing', 88, '31 h'), ('Drawing query', 60, '21 h'), ('Machine down', 37, '13 h'), ('Waiting hardware', 26, '9 h'), ('Other', 9, '3 h')]) + note('Reasons come from a fixed list, so they can be counted.'), '8 weeks'),
              panel('Jobs completed per week', svg_bars([6, 7, 5, 8, 7, 8, 9, 8], ['34', '35', '36', '37', '38', '39', '40', '41'], h=230), 'count'), '1fr')),
         'Concept workshop report with open jobs, jobs due, average days on hold, hours on hold by reason and jobs completed per week',
         'Concept report with example data. Hours on hold by reason is the chart the whiteboard could never produce.', h=540, ui=True)

CASES.append(dict(
    slug=S, title='Job Tracking for a Custom Joinery: A Solution Blueprint',
    seo_title='Joinery Job Tracking: A Solution Blueprint',
    desc='A solution blueprint: how a 25-person custom joinery could replace its whiteboard with scan-based job tracking on Zoho Creator, linked to orders.',
    lead='A reference implementation for a make-to-order workshop where every job is different and the commonest question in the building is &ldquo;where is it up to?&rdquo;',
    category='Job tracking', template='dossier', author='arun', published=TODAY, keyword='job tracking joinery manufacturer',
    hero_alt='Cover: solution blueprint for job tracking for a custom joinery', hero_cap='The blueprint, summarised.',
    facts=[('Type', 'Solution blueprint'), ('Business', 'Typical 25-person custom joinery'), ('Region', 'New Zealand or Australia'), ('Core problem', 'No reliable job status'),
           ('Approach', 'Scan-based job tracker on Zoho Creator'), ('Connected to', 'CRM, stock and accounting'), ('Planned duration', 'About ten weeks, in four stages')],
    sections=sections(
        ['Executive summary', 'Business context', 'Operational challenges', 'The existing process', 'Root-cause analysis', 'The proposed solution', 'Solution architecture', 'The workflow, step by step',
         'Before and after', 'Implementation stages', 'Integrations and data flow', 'Security, validation and exceptions', 'Expected benefits and limitations', 'Where it could go next', 'Is this your workshop?'],
        ['''
<p>I wrote this reference implementation because the same request reaches me most months: a workshop that makes things to order has outgrown its whiteboard. The details vary; the shape does not.</p>
<p>The design below gives every job a card with a QR code. Staff scan it as work starts and finishes at each stage. A board on the wall and in the office shows where every job is, and a job that stops is put on hold with a reason and an owner. Orders arrive from the CRM and draft invoices leave for accounts, so nothing is typed twice.</p>
<p>It is deliberately small. It does not schedule, cost or plan materials. It answers one question well, and creates the data the next project will need.</p>
''', '''
<p>Picture a joinery of about 25 people: three in the office, eighteen in the workshop and four installers. It makes kitchens, wardrobes, shop fittings and reception desks for builders and fit-out firms. Every job is quoted individually. Around a dozen are open at any time, and each takes one to four weeks.</p>
<p>Board is bought per job. Hinges, runners and edge tape are kept in stock. The business uses an accounting package its accountant chose, a quoting spreadsheet and a large whiteboard.</p>
<p>It is typical of the businesses that ask us for this work.</p>
''', '''
<ul>
  <li><strong>No reliable status.</strong> Sales cannot tell a builder when a kitchen will be ready without walking to the workshop.</li>
  <li><strong>Late surprises.</strong> A job turns out to be short of two doors on the morning it was due to be installed.</li>
  <li><strong>Retyping.</strong> The same job is entered in the quote, on the job sheet and on the invoice.</li>
  <li><strong>Invisible delays.</strong> Jobs wait for drawings, hardware or a machine, and nobody records for how long.</li>
  <li><strong>Dependence on one person.</strong> The planner holds the real schedule in his head.</li>
</ul>
''', J1 + '''
<p>A quote is built in a spreadsheet and emailed. When the customer accepts, the office types a job sheet, prints it and takes it to the workshop. The planner writes the job on the whiteboard and orders board by phone.</p>
<p>The job moves through cutting, edging, assembly and finishing. The whiteboard is updated when somebody has a moment. When the job is delivered, the installer hands in a docket and accounts types an invoice from it.</p>
''', J2 + '''
<p>The symptoms look unrelated. They trace back to three causes.</p>
<p>First, status was never recorded as an event. Nothing in the process said &ldquo;assembly started at 08:05&rdquo;. The whiteboard was a summary of what people remembered.</p>
<p>Second, the quote, job sheet and invoice shared no number. Nothing tied them together except the people who handled them.</p>
<p>Third, a problem had nowhere to go. A missing panel was mentioned to whoever was nearby. It could not be assigned, chased or counted.</p>
''', '''
<p>The solution has four parts, in order of importance.</p>
<ol>
  <li><strong>A work order per job,</strong> created from the accepted quote, carrying the sales order number.</li>
  <li><strong>A scan at each stage.</strong> Staff scan the job card to start and to finish a stage. That is the whole of their data entry.</li>
  <li><strong>Holds.</strong> Anyone can stop a job with a reason from a short list and a photo. The planner owns every hold until it is released.</li>
  <li><strong>A live board,</strong> on a screen in the workshop and in the office.</li>
</ol>
''' + J4 + '''
<p>I would build it on Zoho Creator. It provides forms, mobile apps that scan QR codes on phones and tablets, approvals and role-based access without a long build. The <a href="''' + G + '''production-tracking-zoho-creator/">production tracking guide</a> walks through the same build in eight steps.</p>
''', J3 + '''
<p>The custom app sits between standard apps and does only what they do not. Customers and quotes stay in the CRM. Board and hardware stay in the stock system. Invoices stay in the accounting package. Each record has one owner, as set out in our guide to <a href="''' + G + '''connect-sales-production-accounts/">connecting sales, production and accounts</a>.</p>
<p>For a business in New Zealand I would expect the accounting package to stay as it is, with the tracker sending it draft invoices.</p>
''', J5 + '''
<ol>
  <li><strong>Order.</strong> Sales marks the quote as accepted. A work order is created with the standard stages, and a job card is printed.</li>
  <li><strong>Start.</strong> A machinist scans the card and taps Start. The board shows the job in Cutting.</li>
  <li><strong>Finish.</strong> When the stage is done, the machinist records the units completed and taps Complete. The job joins the next queue.</li>
  <li><strong>Problem.</strong> An assembler finds two doors missing, picks &ldquo;part missing&rdquo;, adds a photo and puts the job on hold.</li>
  <li><strong>Decide.</strong> The planner sees the hold, raises a recut as a linked job and tells sales the new date.</li>
  <li><strong>Ready.</strong> After finishing, the job is marked ready and an install is booked.</li>
  <li><strong>Deliver.</strong> The installer marks the job installed, with photos. A draft invoice appears in accounts.</li>
</ol>
''' + J6, J7 + '''
<p>The office stops walking to the workshop, because the board is on their screen. The planner stops being the only source of truth. Problems become records that can be counted, which is where improvement starts.</p>
<p>I have not put numbers on this. A real project would take a baseline first: status calls per day, days from delivery to invoice, and jobs with an unknown stage at 9 a.m.</p>
''', J8 + '''
<ul>
  <li><strong>Weeks 1 to 2.</strong> Walk two real jobs through the workshop. Agree the stages, the hold reasons and who owns holds.</li>
  <li><strong>Weeks 3 to 5.</strong> Build the tracker and trial it at one bench for a week. Expect changes; the trial exists to find them.</li>
  <li><strong>Weeks 6 to 8.</strong> Connect accepted quotes and draft invoices. Extend to every bench.</li>
  <li><strong>Weeks 9 to 10.</strong> Add the report, train the team and take the whiteboard down.</li>
</ul>
<p>Removing the whiteboard is part of the plan. While it stays up, people will keep two systems and trust neither.</p>
''', '''
<ul>
  <li><strong>CRM to tracker:</strong> an accepted quote creates a work order, with customer, items and due date.</li>
  <li><strong>Tracker to CRM:</strong> the current stage is written back to the order, so sales can see it.</li>
  <li><strong>Tracker to stock:</strong> hardware issued to a job is posted as a movement. Board bought per job is recorded against the job.</li>
  <li><strong>Tracker to accounts:</strong> marking a job installed creates a draft invoice for the bookkeeper to approve.</li>
</ul>
<p>Every message carries the sales order number. Failed messages are retried, then shown to a named person with the reason.</p>
''', '''
<ul>
  <li><strong>Roles.</strong> Workshop staff see jobs and stages, not prices. Sales see status, not stage logs they could edit.</li>
  <li><strong>Validation.</strong> A stage cannot finish before it starts. Units completed cannot exceed the order. A hold needs a reason.</li>
  <li><strong>Audit trail.</strong> Each scan records who, when and on which device.</li>
  <li><strong>Exceptions.</strong> Recuts are linked jobs, so their time and material are visible. A job on hold for more than two days is escalated.</li>
  <li><strong>Fallback.</strong> If the network drops, the printed job card still travels with the job and stages are entered when it returns.</li>
</ul>
''', J9 + '''
<p><strong>Expected benefits, stated as directions:</strong> fewer interruptions for the planner, earlier warning of late jobs, faster invoicing because the invoice is drafted on delivery, and a record of why jobs stop.</p>
<p><strong>Limitations:</strong></p>
<ul>
  <li>It does not schedule. The planner still decides the order of work.</li>
  <li>It does not cost jobs, though the stage times it records would feed a costing project later.</li>
  <li>It depends on people scanning. If a bench skips scans, the board is wrong.</li>
  <li>It is not a planning engine. A workshop with deep bills of materials should read our comparison of <a href="''' + G + '''zoho-or-manufacturing-erp/">Zoho apps and a manufacturing ERP</a>.</li>
</ul>
''', '''
<ul>
  <li><strong>Job costing,</strong> using the stage times and materials now recorded.</li>
  <li><strong>A customer view,</strong> so builders can check status themselves through a portal.</li>
  <li><strong>Reorder points</strong> for stocked hardware, described in our <a href="''' + G + '''purchasing-reorder-points/">purchasing guide</a>.</li>
  <li><strong>Capacity view,</strong> showing hours queued at each stage for the coming fortnight.</li>
</ul>
<p>Each of these depends on data the tracker creates. That is the argument for starting small.</p>
''', '''
<p>If this resembles your workshop, the useful first step costs nothing: walk one job from quote to invoice and write down every time it is retyped and every time someone has to ask where it is.</p>
<p>Send me that list. I will tell you what I would build first and what I would leave alone. More on our approach is on the <a href="''' + M + '''zoho-implementation/">Zoho implementation for manufacturers</a> page.</p>
''']),
    faqs=[('How long would a project like this take?',
           'The plan here is about ten weeks in four stages, with something in daily use at the end of each. The real duration depends on how many stages, integrations and exceptions your process has.'),
          ('Do staff need a phone each?',
           'No. One shared tablet per work area is usually enough. Staff scan the job card and tap one or two buttons.'),
          ('Would we have to change accounting software?',
           'No. The design keeps your existing accounting package and sends it draft invoices.')],
    sources=[SRC['creator_features'], SRC['creator_scan'], SRC['inv_features'], SRC['books_editions']],
    related=['production-tracking-zoho-creator', 'zoho-or-manufacturing-erp', 'connect-sales-production-accounts'],
))

# ====================================================================== 2. Batch traceability for a food manufacturer (development team)
S = 'batch-traceability-food-manufacturer'
cover(S, 'Illustrative case study', 'Batch traceability for a bakery', 'From paper batch sheets to a trace that takes minutes.',
      two(m_tiles([('1', 'Receive', 'Every lot labelled and scanned'), ('2', 'Make', 'Lots scanned into each batch'), ('3', 'Ship', 'Pallets scanned to orders'), ('4', 'Trace', 'Forward and back, on one screen')])),
      theme='green', alt='Cover: solution blueprint for batch traceability for a bakery in four parts: receive, make, ship and trace')
B1 = fig(S + '-ba', m_ba(dict(k='Before', h='Paper batch sheets', li=['Lot numbers handwritten', 'Sheets filed by date', 'A trace means reading folders', 'Holds by word of mouth']),
                          dict(k='After', h='Scanned batch records', li=['Lots scanned at each step', 'Records linked by batch', 'A trace is one search', 'A hold blocks picking'])),
         'Before and after comparison of traceability: paper batch sheets against scanned batch records, four points each',
         'What changes. The differences are in how records are made, with no figures claimed.', h=460, theme='green')
B2 = fig(S + '-gaps', m_table(['Step', 'What was recorded', 'The gap'],
                               [['Receiving', 'Delivery note filed', 'Supplier lot not copied to the bag'], ['Storage', 'Nothing', 'Two lots mixed in one bin'], ['Mixing', 'Lot written on the batch sheet', 'Often blank or illegible'],
                                ['Packing', 'Batch stamped on the pack', 'Film lot never recorded'], ['Dispatch', 'Invoice lists the product', 'Batch not on the order']], '.7fr 1.1fr 1.2fr'),
         'Table of five process steps showing what was recorded on paper and the traceability gap at each',
         'Where the paper trail broke. Every step recorded something, and no step recorded enough.', h=500, theme='green', title='The existing process and its gaps')
B3 = fig(S + '-arch', m_arch([('People', 'who scans what', ['Stores', 'Mixers', 'Packers', 'Dispatch', 'Quality lead']),
                               ('Batch app', 'built on Zoho Creator', ['Lot receipts', 'Batch records', 'Checks', 'Holds', 'Trace search'], True),
                               ('Stock system', 'owns quantities and expiry dates', ['Raw material lots', 'Finished lots', 'Locations', 'Shipments']),
                               ('Other systems', 'kept as they are', ['Accounting package', 'Label printer', 'Customer orders'])]),
         'Solution architecture: staff scan into a batch app on Zoho Creator, which sits on a stock system that owns quantities and expiry dates',
         'The proposed architecture. The batch app records the link the stock system cannot: which lots went into which batch.', h=540, theme='green', title='Solution architecture')
B4 = fig(S + '-receive', phones([phone('Receive a lot', 'Goods in &middot; Bay 1', pscan('Scan supplier label') + pf('Material', 'Butter, unsalted 25 kg') + pf('Supplier lot', 'B-0913') + pf('Use by', '28 Nov 2026') + pbtn('Print lot label', 'b')),
                                 phone('Issue to batch', 'Batch 24-1051 &middot; Mixer 2', pscan('Scan lot label') + pf('Lot', 'B-0913 &middot; Butter') + pf('Quantity', '75 kg') + pf('Oldest lot first?', 'Yes') + pbtn('Add to batch'))],
                                [('One scan per lot', 'The supplier label is read, not retyped.'), ('Oldest first', 'The app warns if an older lot is still in stock.'), ('Typed entries flagged', 'Anything keyed by hand is marked for a check.')]),
         'Two concept handheld screens, receiving a supplier lot and issuing a lot to a batch, with three design notes',
         'Concept handheld screens for stores and mixing. These two scans create the links a recall depends on.', h=600, theme='green', ui=True)
B5 = fig(S + '-batch', app('Batch Records', 'Concept on Zoho Creator', ['Today', 'Batches', 'Lots', 'Holds', 'Trace'], 'Batches', 'Batch 24-1051 &middot; Oat slice 180 g', 'Mixer 2 &middot; 10 Oct &middot; in progress',
         stepper([('Weigh', 'd'), ('Mix', 'd'), ('Bake', 'c'), ('Pack', ''), ('Check', ''), ('Release', '')])
         + g2(panel('Lots issued', table('minmax(0,1.2fr) 100px 86px 96px', ['Ingredient', 'Lot', '>Qty', 'Entry'],
                    [['Oats', ('sn', 'O-3318'), ('r', '120 kg'), ('st', 'g', 'Scanned')], ['Butter', ('sn', 'B-0913'), ('r', '75 kg'), ('st', 'g', 'Scanned')], ['Golden syrup', ('sn', 'G-0207'), ('r', '40 kg'), ('st', 'g', 'Scanned')], ['Flour', ('sn', 'F-2211'), ('r', '60 kg'), ('st', 'g', 'Scanned')]]), '4 of 4 required'),
              panel('Checks', listing([('g', 'Allergen changeover signed', '07:40, line cleaned after nut product'), ('g', 'Oven temperature in range', 'Logged 08:30 and 09:00'), ('', 'Metal detector check', 'Due at start of packing'), ('', 'Pack weight check', 'Due every 30 minutes')]), 'release needs all four'), '1.3fr')),
         'Concept batch record in progress with a six-step progress bar, the four ingredient lots issued and the checks completed and outstanding',
         'Concept batch record. The batch cannot be released until every required lot and check is present.', h=440, ui=True)
B6 = fig(S + '-trace', app('Batch Records', 'Concept on Zoho Creator', ['Today', 'Batches', 'Lots', 'Holds', 'Trace'], 'Trace', 'Mock recall: oats lot O-3318', 'Drill started 14:02 &middot; finished 14:09',
         kpis([('Received', '1,000 kg', '28 Sep', 'fl'), ('Batches affected', '6', '720 kg used', 'fl'), ('In warehouse', '2 batches', 'on hold', 'fl'), ('Customers', '5', '9 orders', 'fl')])
         + g2(panel('Reconciliation', fields([('Received', '1,000 kg'), ('Used in batches', '720 kg'), ('Still in stock', '275 kg'), ('Recorded waste', '5 kg'), ('Total accounted', '1,000 kg'), ('Difference', '0 kg')], 2) + note('Received must equal used plus stock plus waste.'), 'balanced'),
              panel('Customers to notify', table('minmax(0,1.2fr) 70px 96px 96px', ['Customer', '>Orders', 'Last ship', 'Status'],
                    [['Cafe group A', ('r', '3'), '8 Oct', ('st', 'y', 'To call')], ['Grocer B', ('r', '2'), '7 Oct', ('st', 'y', 'To call')], ['Distributor C', ('r', '2'), '6 Oct', ('st', 'y', 'To call')], ['Caterer D', ('r', '1'), '5 Oct', ('st', 'y', 'To call')], ['Cafe E', ('r', '1'), '2 Oct', ('st', 'y', 'To call')]]), 'from dispatch scans'), '1fr'),
         actions='<span class="btns">Export recall list</span>'),
         'Concept mock recall screen for one ingredient lot showing batches affected, a quantity reconciliation and the list of customers to notify',
         'Concept mock recall screen with example data. The drill is timed, and the reconciliation shows nothing is unaccounted for.', h=560, ui=True)
B7 = fig(S + '-holds', app('Batch Records', 'Concept on Zoho Creator', ['Today', 'Batches', 'Lots', 'Holds', 'Trace'], 'Holds', 'Stock on hold', '10 Oct &middot; 3 items',
         panel('Held stock cannot be picked or issued', table('110px minmax(0,1.2fr) 100px minmax(0,1.3fr) 110px 110px', ['Lot or batch', 'Item', '>Quantity', 'Reason', 'Placed by', 'Decision'],
               [[('sn', '24-1049'), 'Oat slice 180 g', ('r', '1,150 packs'), 'Mock recall drill on O-3318', 'Quality lead', ('st', 'b', 'Release')], [('sn', '24-1050'), 'Oat slice 180 g', ('r', '1,180 packs'), 'Mock recall drill on O-3318', 'Quality lead', ('st', 'b', 'Release')],
                [('sn', 'P-560'), 'Film wrap, printed', ('r', '2 rolls'), 'Print colour out of range', 'Goods in', ('st', 'y', 'Awaiting')]]), 'each hold has an owner', 'flex:1'),
         actions='<span class="btnp">Place a hold</span>'),
         'Concept list of stock on hold with the lot or batch, quantity, reason, who placed the hold and the decision status',
         'Concept holds screen. A hold placed here changes the stock status, so the product cannot be picked.', h=400, ui=True)
B8 = fig(S + '-stages', m_steps([('Label everything', 'Lot labels at goods in', 'Weeks 1-3'), ('Batch records', 'Scan lots into batches on one line', 'Weeks 4-7'), ('Dispatch', 'Scan pallets to orders', 'Weeks 8-10'), ('Prove it', 'Timed mock recalls, both directions', 'Weeks 11-12')],
                                 ['#3CCB7F', '#F9B21D', '#F28B3C', '#6CB4F5']),
         'Four implementation stages over twelve weeks: label everything, batch records, dispatch, and prove it with mock recalls',
         'Stages follow the product through the building, so each one closes a link in the chain.', h=440, theme='green', title='Implementation stages')

CASES.append(dict(
    slug=S, title='Batch Traceability for a Bakery: A Solution Blueprint',
    seo_title='Bakery Batch Traceability: A Blueprint',
    desc='A solution blueprint: how a 40-person bakery could move from paper batch sheets to scanned lot and batch records with a timed mock recall.',
    lead='A reference implementation for a food producer whose paper records are complete enough to pass an audit and too slow to use in a real recall.',
    category='Traceability', template='ba', author='team', published=TODAY, keyword='batch traceability food manufacturer',
    hero_alt='Cover: solution blueprint for batch traceability for a bakery', hero_cap='The blueprint in four parts.',
    facts=[('Type', 'Solution blueprint'), ('Business', 'Typical 40-person bakery'), ('Products', 'Biscuits and slices, packed'), ('Core problem', 'Slow, unreliable traces'),
           ('Approach', 'Scanned lot and batch records'), ('Connected to', 'Stock system and label printer'), ('Planned duration', 'About twelve weeks, in four stages')],
    sections=sections(
        ['Executive summary', 'Business context', 'Operational challenges', 'The existing process', 'Root-cause analysis', 'The proposed solution', 'Solution architecture', 'The workflow, step by step',
         'Before and after', 'Implementation stages', 'Integrations and data flow', 'Security, validation and exceptions', 'Expected benefits and limitations', 'Where it could go next', 'Does this sound familiar?'],
        ['''
<p>This reference implementation describes how our team would give a mid-sized bakery working traceability: the ability to follow any ingredient lot forward to the customers who received it, and any finished pack back to its inputs.</p>
<p>The design puts a lot label on everything at goods in, scans lots into each batch at mixing, and scans pallets to orders at dispatch. A batch app on Zoho Creator holds those links and sits beside a stock system that owns quantities and expiry dates. Success is defined by a timed mock recall, run in both directions.</p>
''', '''
<p>The business in this blueprint is a bakery of about 40 people making packaged biscuits and slices for cafes, grocers and distributors. It runs two lines, makes eight to twelve batches a day and receives around fifteen deliveries a week.</p>
<p>It has a food safety plan and is audited by its larger customers. Records are kept on paper batch sheets, filed by date. Stock is counted weekly on a spreadsheet.</p>
''', '''
<ul>
  <li><strong>A trace takes most of a day.</strong> Someone reads through folders of batch sheets, and the result is not always certain.</li>
  <li><strong>Blank and illegible lot numbers.</strong> A long code written by hand at 5 a.m. is often wrong.</li>
  <li><strong>Lots get mixed.</strong> A part-used bag is tipped into a bin that already holds another lot.</li>
  <li><strong>Holds are informal.</strong> &ldquo;Do not use that pallet&rdquo; is a note or a conversation.</li>
  <li><strong>Packaging is untraced.</strong> Printed film is an input, and the commonest cause of a labelling recall.</li>
</ul>
''', B2 + '''
<p>On paper the process looked complete. A delivery note was filed, the mixer wrote lot numbers on the batch sheet, the packer stamped the batch code and an invoice went out.</p>
<p>In practice each step kept its own record, and nothing joined them. To trace a lot, someone had to match handwriting on a batch sheet to a delivery note in another folder, then guess which orders the batch had gone to from the dates.</p>
''', '''
<p>We would summarise the cause in one sentence: the business recorded <em>documents</em>, and traceability needs <em>links</em>.</p>
<ul>
  <li><strong>No identity at the point of use.</strong> The supplier lot number was on the delivery note, not on the bag at the mixer.</li>
  <li><strong>Recording after the event.</strong> Batch sheets were often completed at the end of the run, from memory.</li>
  <li><strong>The dispatch link did not exist.</strong> Orders recorded products and quantities, never batches.</li>
  <li><strong>Nobody tested it.</strong> Without a timed drill, the weakness stayed hidden until it mattered.</li>
</ul>
<p>Our <a href="''' + G + '''batch-lot-traceability/">traceability guide</a> explains the five recording points this analysis is based on.</p>
''', '''
<p>The solution is four habits, each supported by a scan.</p>
<ol>
  <li><strong>Label at goods in.</strong> Every delivery is received by scanning the supplier label. The app prints an internal lot label for each pallet or bag.</li>
  <li><strong>Scan into the batch.</strong> At weighing, the operator scans each lot label. The batch record lists the required ingredients and will not close with one missing.</li>
  <li><strong>Label the output.</strong> Finished pallets get a label with the batch number and best-before date, printed from the record.</li>
  <li><strong>Scan out.</strong> Dispatch scans each pallet against the order.</li>
</ol>
''' + B4 + '''
<p>Scanning is the point. Zoho Creator forms read barcodes and QR codes on phones and tablets, so inexpensive handhelds are enough.</p>
''', B3 + '''
<p>Two systems share the work. The stock system owns what the business has and where: lots, quantities, locations and expiry dates. Zoho Inventory offers batch tracking with expiry dates and multiple warehouses, which suits this role.</p>
<p>The batch app owns what happened in production: which lots were consumed, which checks were done, who released the batch. Zoho Inventory has no manufacturing module, so this link has to live somewhere else. The app posts consumption and output to the stock system as movements.</p>
''', '''
<ol>
  <li><strong>Receive.</strong> Stores scan the supplier label on a butter delivery. The app records supplier lot, quantity and use-by date, and prints lot labels.</li>
  <li><strong>Store.</strong> Each pallet is scanned into a location.</li>
  <li><strong>Start a batch.</strong> The mixer selects the product. The app issues batch number 24-1051 and lists the ingredients needed.</li>
  <li><strong>Issue.</strong> Each lot is scanned as it is weighed. The app warns if an older lot of the same material is still in stock.</li>
  <li><strong>Check.</strong> Allergen changeover, oven temperature, metal detection and pack weights are recorded against the batch.</li>
  <li><strong>Pack and label.</strong> Pallet labels are printed with batch and best-before date. Rejected packs are recorded.</li>
  <li><strong>Release.</strong> The quality lead releases the batch once all lots and checks are present.</li>
  <li><strong>Dispatch.</strong> Pallets are scanned to orders.</li>
</ol>
''' + B5, B1 + '''
<p>The work on the floor changes little. People still weigh, mix, bake and pack. What changes is that each link is made by a scan at the moment it happens, and stored where it can be searched.</p>
''', B8 + '''
<p>The order matters. Batch records are worthless if the lots arriving at the mixer have no labels, so labelling comes first. Dispatch comes third because it needs finished-lot labels, which the batch record prints.</p>
<p>Each stage runs on one line for a week before it is extended. The final stage is not a build at all. It is two timed drills, one forward and one backward, repeated until the team is satisfied.</p>
''', '''
<ul>
  <li><strong>Batch app to stock system:</strong> lots consumed and finished lots produced, as stock movements.</li>
  <li><strong>Stock system to batch app:</strong> lots on hand by location, so the app can check oldest-first.</li>
  <li><strong>Batch app to label printer:</strong> lot and pallet labels.</li>
  <li><strong>Orders to batch app:</strong> open orders for dispatch scanning.</li>
</ul>
<p>The accounting package is untouched. Our <a href="''' + G + '''connect-sales-production-accounts/">integration guide</a> covers the ownership rules behind this list.</p>
''', B7 + '''
<ul>
  <li><strong>Holds.</strong> Placing a hold changes stock status, so held product cannot be picked or issued.</li>
  <li><strong>Release control.</strong> Only the quality role can release a batch, and only when it is complete.</li>
  <li><strong>Typed entries flagged.</strong> A lot number keyed by hand is marked for a second check.</li>
  <li><strong>Rework.</strong> Product reworked into another batch is issued like an ingredient, so its history follows it.</li>
  <li><strong>Audit trail.</strong> Every scan records the user, device and time. Records cannot be edited after release without a logged reason.</li>
  <li><strong>If the system is down.</strong> A paper batch sheet with the same fields is kept at each line and entered afterwards.</li>
</ul>
''', B6 + '''
<p><strong>Expected benefits, as directions:</strong> a trace becomes a search, the scope of any recall becomes narrower because it can be limited to the batches affected, lot numbers stop being transcribed by hand, and audits become a matter of showing a screen.</p>
<p><strong>Limitations:</strong></p>
<ul>
  <li>It records what people scan. A lot tipped in without a scan is invisible.</li>
  <li>It does not plan production or purchasing. A bakery that needs requirements planning should consider an ERP or MRP system with batch control.</li>
  <li>It supports a food safety plan and does not replace one. Regulatory requirements differ by country and product, and should be checked with a qualified adviser.</li>
  <li>Bulk materials stored in silos need a rule for how lots are treated when they mix.</li>
</ul>
''', '''
<ul>
  <li><strong>Supplier certificates read automatically</strong> at goods in, as described in our guide to <a href="''' + G + '''ai-for-small-manufacturers/">AI for small manufacturers</a>.</li>
  <li><strong>Digital quality records,</strong> linking nonconformances to batches. See the <a href="''' + G + '''quality-ncr-capa-workflow/">NCR and CAPA guide</a>.</li>
  <li><strong>Yield reporting</strong> by product and line, from planned and produced quantities.</li>
  <li><strong>Customer notifications</strong> drafted from the recall list.</li>
</ul>
''', '''
<p>If you are unsure how your own records would stand up, run a mock recall this week. Pick one ingredient lot, start a clock and find every customer who received it.</p>
<p>Tell us how long it took and where it stalled. We will suggest the smallest change that would shorten it. Our <a href="''' + M + '''workflows/">manufacturing workflows</a> page shows how traceability fits with the processes around it.</p>
''']),
    faqs=[('Why not do all of this in the stock system?',
           'A stock system tracks batches you receive and ship. Recording which input lots were consumed by which production run needs a manufacturing module or a batch record app. Zoho Inventory states that it has no manufacturing module.'),
          ('What hardware is needed?',
           'A label printer at goods in and at packing, and a phone or handheld with a camera at each scanning point.'),
          ('Does this make us compliant with food regulations?',
           'It provides the records most schemes ask for, but compliance depends on your products, markets and food safety plan. Check the requirements with a qualified adviser.')],
    sources=[SRC['inv_features'], SRC['inv_mfg'], SRC['creator_scan'], SRC['creator_features']],
    related=['batch-lot-traceability', 'quality-ncr-capa-workflow', 'inventory-accuracy-for-manufacturers'],
))

# ====================================================================== 3. AI-assisted purchase order intake (development team)
S = 'ai-purchase-order-intake'
cover(S, 'Illustrative case study', 'AI-assisted order intake', 'Customer purchase orders read into drafts, with a person confirming each one.',
      m_rows([('The AI reads', 'PDF purchase orders arriving by email'), ('Rules check', 'Customer, items, prices and dates'), ('A person confirms', 'Nothing is created until they do')]),
      theme='navy', solid=True, alt='Cover: solution blueprint for AI-assisted order intake in three parts: the AI reads, rules check and a person confirms')
I1 = fig(S + '-flow', m_chev([('Arrive', 'Email with a PDF'), ('Read', 'Fields extracted'), ('Check', 'Rules applied'), ('Review', 'A person confirms'), ('Create', 'Sales order raised')],
                              ['#3B5BDB', '#364FC7', '#1B5A96', '#0B6E4F', '#089949']),
         'Five-step flow for purchase order intake: arrive, read, check, review and create',
         'The flow. The fourth step is the one that makes the rest safe.', h=300, theme='navy')
I2 = fig(S + '-rules', m_table(['Check', 'Rule', 'If it fails'],
                                [['Customer', 'Matches an account by code or email domain', 'Reviewer picks the account'], ['Item', 'Matches an item code or a known customer part number', 'Reviewer maps it once; mapping is kept'],
                                 ['Price', 'Within tolerance of the price list', 'Flagged, with both prices shown'], ['Delivery date', 'Not earlier than standard lead time', 'Flagged for the planner'],
                                 ['Duplicate', 'Customer PO number not seen before', 'Blocked until a person decides']], '.7fr 1.4fr 1.1fr'),
         'Table of five validation checks applied to each extracted purchase order with the rule and what happens when it fails',
         'Five checks run on every order. The rules are ordinary code, not AI, so they behave the same way every time.', h=500, theme='navy', title='Validation rules')
I3 = fig(S + '-arch', m_arch([('People', 'review and decide', ['Sales admin', 'Planner', 'Sales manager']),
                               ('Review app', 'built on Zoho Creator', ['Inbox', 'Side-by-side review', 'Item mappings', 'Accuracy log'], True),
                               ('AI and rules', 'read, then check', ['Document extraction', 'Validation rules', 'Confidence flags']),
                               ('Systems of record', 'changed only after confirmation', ['CRM: customers', 'Stock: items and prices', 'Orders', 'Email inbox'])]),
         'Solution architecture: people work in a review app on Zoho Creator, which sits above extraction and validation rules and writes to systems of record only after confirmation',
         'The proposed architecture. The AI has no write access to orders; the review app does, after a person confirms.', h=540, theme='navy', title='Solution architecture')
I4 = fig(S + '-inbox', app('Order Intake', 'Concept on Zoho Creator', ['Inbox', 'In review', 'Confirmed', 'Rejected', 'Mappings', 'Accuracy log'], 'Inbox', 'Today&rsquo;s purchase orders', '10 Oct &middot; 9 received &middot; 3 waiting',
         kpis([('Received', '9', 'today', 'fl'), ('Ready to confirm', '4', 'no flags', 'up'), ('Need attention', '3', 'flags raised', 'dn'), ('Confirmed', '2', '', 'fl')])
         + panel('Queue', table('76px minmax(0,1.3fr) 110px 70px minmax(0,1.3fr) 110px', ['Time', 'Customer', 'PO number', '>Lines', 'Flags', 'Status'],
                 [['09:12', 'Fit-out customer A', ('sn', 'PO-88214'), ('r', '3'), 'Unknown item; price differs', ('st', 'r', 'Attention')], ['09:40', 'Builder B', ('sn', '4500118'), ('r', '6'), 'None', ('st', 'g', 'Ready')],
                  ['10:05', 'Retail chain C', ('sn', 'RC-22071'), ('r', '12'), 'Delivery date inside lead time', ('st', 'y', 'Attention')], ['10:31', 'Builder B', ('sn', '4500118'), ('r', '6'), 'Possible duplicate', ('st', 'r', 'Blocked')],
                  ['10:48', 'Fit-out customer D', ('sn', 'FD-0932'), ('r', '2'), 'None', ('st', 'g', 'Ready')]]), 'oldest first', 'flex:1')),
         'Concept order intake inbox with counts for the day and a queue of purchase orders showing customer, PO number, lines, flags and status',
         'Concept inbox. Orders with no flags can be confirmed in seconds; the reviewer spends time where the flags are.', h=540, ui=True)
I5 = fig(S + '-review', app('Order Intake', 'Concept on Zoho Creator', ['Inbox', 'In review', 'Confirmed', 'Rejected', 'Mappings', 'Accuracy log'], 'In review', 'Review: RC-22071 &middot; Retail chain C', '12 lines &middot; 1 flag &middot; source PDF shown alongside',
         g2(panel('Source document', listing([('', 'Purchase order RC-22071', 'Page 1 of 2 &middot; received 10:05'), ('', 'Deliver to: Store 14, loading dock', 'Address matched to customer record'), ('y', 'Required by: 16 Oct 2026', 'Highlighted: read as delivery date'), ('', '12 lines, shelving and counters', 'All item codes matched')]) + note('In the real screen this panel shows the PDF itself, with each extracted value highlighted on the page.'), 'PDF'),
            panel('Draft sales order', fields([('Customer', 'Retail chain C'), ('PO number', 'RC-22071'), ('Lines', '12, all matched'), ('Order value', 'Within price list'), ('Requested date', '16 Oct 2026'), ('Standard lead time', '10 working days')], 2)
                  + listing([('y', 'Requested date is inside standard lead time', 'Earliest standard date is 24 Oct')]) + acts(('btnp', 'Confirm with 24 Oct'), ('btns', 'Ask planner'), ('btnr', 'Reject')), 'reviewer: sales admin'), '.9fr')),
         'Concept review screen with the source purchase order on the left and the draft sales order on the right, flagging a delivery date inside standard lead time',
         'Concept review screen. Source and draft sit side by side, and the one flag is explained in plain words.', h=490, ui=True)
I6 = fig(S + '-accuracy', app('Order Intake', 'Concept on Zoho Analytics', ['Inbox', 'In review', 'Confirmed', 'Rejected', 'Mappings', 'Accuracy log'], 'Accuracy log', 'Accuracy log', 'Example data &middot; last 8 weeks',
         kpis([('Orders processed', '312', '8 weeks', 'fl'), ('Fields corrected', '4.1%', 'of all fields', 'fl'), ('Confirmed unchanged', '71%', 'of orders', 'fl'), ('Wrong orders created', '0', 'caught at review', 'up')])
         + g2(panel('Corrections by field', bars2([('Item code', 78, '38'), ('Unit price', 49, '24'), ('Delivery date', 33, '16'), ('Quantity', 14, '7'), ('Customer', 6, '3')]) + note('Most item corrections are first-time customer part numbers; each is mapped once.'), 'count'),
              panel('Fields corrected by week', svg_line([[7.8, 6.4, 5.9, 4.8, 4.2, 3.9, 3.6, 3.4]], ['34', '35', '36', '37', '38', '39', '40', '41'], ymax=10, h=230), '% of fields'), '1fr')),
         'Concept accuracy log showing orders processed, share of fields corrected, orders confirmed unchanged, corrections by field and a weekly trend',
         'Concept accuracy log with example data. Every correction a reviewer makes is counted, so accuracy is measured, not assumed.', h=540, ui=True)
I7 = fig(S + '-ba', m_ba(dict(k='Before', h='Typed from a PDF', li=['Each order keyed line by line', 'Customer part numbers looked up by hand', 'Price and date checked if time allows', 'Duplicates found by the customer']),
                          dict(k='After', h='Read, checked, confirmed', li=['Draft filled in from the PDF', 'Part numbers mapped once, then remembered', 'Price and date checked on every order', 'Duplicates blocked before creation'])),
         'Before and after comparison of order entry: typed from a PDF against read, checked and confirmed, four points each',
         'What changes for the sales administrator. The person stays; the typing goes.', h=520, theme='navy')
I8 = fig(S + '-stages', m_timeline([('Weeks 1-2', 'Collect and label', '100 past orders with the correct entries'), ('Weeks 3-5', 'Proof of concept', 'Extraction tested; pass mark agreed'),
                                     ('Weeks 6-8', 'Shadow running', 'Drafts made, people still key as normal'), ('Weeks 9-10', 'Go live', 'Review app replaces typing')]),
         'Four implementation stages over ten weeks: collect and label, proof of concept, shadow running and go live',
         'A staged plan with a decision point after the proof of concept.', h=380, theme='navy', title='Implementation stages')

CASES.append(dict(
    slug=S, title='AI-Assisted Purchase Order Intake: A Solution Blueprint',
    seo_title='AI Purchase Order Intake: A Blueprint',
    desc='A solution blueprint: reading customer purchase orders into draft sales orders with AI extraction, validation rules and human confirmation.',
    lead='A reference implementation for a manufacturer whose sales administrator spends the morning retyping purchase orders, and whose customers find the mistakes.',
    category='AI and automation', template='ai', author='team', published=TODAY, keyword='AI purchase order processing manufacturing',
    hero_alt='Cover: solution blueprint for AI-assisted order intake', hero_cap='The blueprint in three parts.',
    facts=[('Type', 'Solution blueprint'), ('Business', 'Typical 35-person shopfitting manufacturer'), ('Volume', 'Around 40 purchase orders a day'), ('Core problem', 'Manual order entry'),
           ('Approach', 'AI extraction, rules, human review'), ('AI can change', 'Nothing without confirmation'), ('Planned duration', 'About ten weeks, with a test first')],
    sections=sections(
        ['Executive summary', 'Business context', 'Operational challenges', 'The existing process', 'Root-cause analysis', 'The proposed solution', 'Solution architecture', 'The workflow, step by step',
         'Before and after', 'Implementation stages', 'Integrations and data flow', 'Security, validation and exceptions', 'Expected benefits and limitations', 'Where it could go next', 'Thinking about something similar?'],
        ['''
<p>This reference implementation shows how our team would apply AI to one narrow task in a manufacturing business: turning customer purchase orders, which arrive as PDFs in many layouts, into sales orders.</p>
<p>The AI reads each document and fills in a draft. Ordinary rules then check the customer, items, prices, dates and duplicates. A person reviews the draft beside the original and confirms it. Nothing is created in the order system until they do, and every correction is logged so accuracy can be measured.</p>
<p>We chose this task because it is frequent, easy to check and low in risk. That combination is what makes an AI project worth doing.</p>
''', '''
<p>The business in this blueprint is a manufacturer of shop fittings and shelving with about 35 staff. It sells to builders, fit-out firms and retail chains, and receives around 40 purchase orders a day by email. Each customer uses its own layout and often its own part numbers.</p>
<p>One sales administrator enters the orders, with help from a colleague at busy times. Customers, items and prices are already held in the CRM and stock system. The volumes are typical examples.</p>
''', '''
<ul>
  <li><strong>Hours of retyping.</strong> Order entry fills most of the morning, and orders received after lunch wait until the next day.</li>
  <li><strong>Keying errors.</strong> A 12 becomes a 21. The customer finds it on delivery.</li>
  <li><strong>Customer part numbers.</strong> Each must be translated to an internal code, from memory or a spreadsheet.</li>
  <li><strong>Unchecked prices and dates.</strong> There is rarely time to compare each line with the price list or the lead time.</li>
  <li><strong>Duplicates.</strong> A customer resends a purchase order, and it is entered twice.</li>
</ul>
''', '''
<p>An email arrives with a PDF. The administrator opens it, opens the order screen beside it and types: customer, purchase order number, delivery address, then each line. Unfamiliar part numbers are looked up. The order is saved and the email is filed.</p>
<p>Nothing about this is badly run. It is careful work done by a capable person, and it is exactly the kind of work that produces occasional errors however careful the person is.</p>
''' + I7, '''
<p>The root cause is not the administrator and not the customers. It is that information arrives in a form a person can read and a system cannot, so a person has to act as the translator.</p>
<ul>
  <li><strong>Unstructured input.</strong> Every customer&rsquo;s layout is different, which ruled out simple templates.</li>
  <li><strong>Knowledge held in one head.</strong> Which customer part number means which item was never written down.</li>
  <li><strong>Checks compete with speed.</strong> When the queue is long, verification is the first thing dropped.</li>
</ul>
<p>The first cause is what document extraction addresses. The second and third are addressed by ordinary software: a mapping table and validation rules.</p>
''', I1 + '''
<p>The solution has three layers, and only the first involves AI.</p>
<ol>
  <li><strong>Extraction.</strong> A document model reads the PDF and returns fields: customer, purchase order number, dates, and each line&rsquo;s part number, description, quantity and price.</li>
  <li><strong>Validation.</strong> Fixed rules compare those fields with what the business already knows.</li>
  <li><strong>Review.</strong> A person sees the draft beside the source, deals with any flags and confirms.</li>
</ol>
''' + I2 + '''
<p>Keeping the checks as plain rules is deliberate. A rule that says &ldquo;flag any price more than a set tolerance from the price list&rdquo; behaves identically every day and can be explained to an auditor.</p>
''', I3 + '''
<p>The review app is the centre of the design. It is the only component allowed to create sales orders, and it does so only when a named user confirms. The extraction service reads documents and returns data; it holds no credentials for the order system.</p>
<p>On Zoho, the review app would be built on Creator. Its AI Modeler includes OCR and supports custom models, and Zoho&rsquo;s agent tools allow a business to connect its own account with an outside model provider. Which option fits depends on plan, region and document quality, so the design treats the extraction service as replaceable.</p>
''', '''
<ol>
  <li><strong>Arrive.</strong> An email reaches the orders inbox. The attachment is saved to a new intake record.</li>
  <li><strong>Read.</strong> The extraction service returns the fields, each with a confidence score.</li>
  <li><strong>Check.</strong> The five rules run. Each failure becomes a flag in plain words.</li>
  <li><strong>Queue.</strong> The order appears in the inbox as ready, needing attention or blocked.</li>
</ol>
''' + I4 + '''
<ol start="5">
  <li><strong>Review.</strong> The administrator opens it. The PDF is on the left with extracted values highlighted, the draft on the right.</li>
  <li><strong>Resolve.</strong> An unknown part number is mapped to an item once; the mapping is kept for next time. A date inside lead time is confirmed with the standard date or sent to the planner.</li>
  <li><strong>Confirm.</strong> The sales order is created, linked to the original email and PDF.</li>
  <li><strong>Log.</strong> Any field the reviewer changed is recorded in the accuracy log.</li>
</ol>
''' + I5, '''
<p>The administrator&rsquo;s role moves from typing to checking. Orders with no flags take seconds. Attention goes to the few that need judgement: an unfamiliar item, a price that does not match, a date that cannot be met.</p>
<p>The checks that used to be skipped under pressure now run on every order, because a rule does not get tired at 11 a.m.</p>
<p>We have not attached savings to this. The proof of concept exists to measure them on real documents before anyone commits.</p>
''', I8 + '''
<ul>
  <li><strong>Weeks 1 to 2.</strong> Collect 100 past purchase orders across the main customers, with the sales orders that were actually entered. These are the answer key.</li>
  <li><strong>Weeks 3 to 5.</strong> Run extraction on them and measure field-level accuracy. Agree a pass mark first. If the test falls short, stop or change the approach.</li>
  <li><strong>Weeks 6 to 8.</strong> Shadow running. The system drafts every incoming order while the administrator keeps typing as normal. Drafts are compared with what was entered.</li>
  <li><strong>Weeks 9 to 10.</strong> Go live for two or three customers, then the rest.</li>
</ul>
<p>The decision point after week five is real. A proof of concept that cannot fail is a demonstration, not a test.</p>
''', '''
<ul>
  <li><strong>Email to review app:</strong> new messages and attachments from the orders inbox.</li>
  <li><strong>Review app to extraction service:</strong> the document goes out, fields come back.</li>
  <li><strong>CRM and stock system to review app:</strong> customers, items, price lists and lead times, read only.</li>
  <li><strong>Review app to order system:</strong> the confirmed sales order, with a link to the source document.</li>
</ul>
<p>From there the order follows the normal route into production and accounts, as described in our <a href="''' + G + '''connect-sales-production-accounts/">integration guide</a>.</p>
''', '''
<ul>
  <li><strong>Least access.</strong> The extraction service can read a document and nothing else. It cannot see the customer list or create records.</li>
  <li><strong>Human confirmation.</strong> No order is created without a named user confirming it. There is no auto-approve setting.</li>
  <li><strong>Duplicates blocked.</strong> A repeated customer purchase order number cannot be confirmed without a deliberate override.</li>
  <li><strong>Data handling.</strong> Before go-live, confirm where documents are processed, whether they are retained and whether they are used for training. Check customer contracts for restrictions on sharing their documents.</li>
  <li><strong>Audit trail.</strong> Each order keeps the source PDF, the extracted values, the changes made and who confirmed it.</li>
  <li><strong>Fallback.</strong> If extraction is unavailable, the review app opens a blank draft beside the PDF and the order is keyed as before.</li>
  <li><strong>Unreadable documents.</strong> Handwritten or badly scanned orders are routed straight to manual entry.</li>
</ul>
''', I6 + '''
<p><strong>Expected benefits, as directions:</strong> less time spent typing, orders entered on the day they arrive, price and date checks on every order, fewer keying errors reaching customers, and part-number knowledge held in the system.</p>
<p><strong>Limitations:</strong></p>
<ul>
  <li>Extraction will make mistakes. The design assumes it and relies on review to catch them.</li>
  <li>Accuracy depends on document quality. Clean PDFs read well; photographs of printed orders read poorly.</li>
  <li>New customers and new layouts need a period of closer checking.</li>
  <li>It does not negotiate, decide whether to accept an order or judge credit. People do.</li>
  <li>Running costs depend on the service and volume and should be estimated during the proof of concept.</li>
</ul>
''', '''
<ul>
  <li><strong>Supplier documents.</strong> The same pattern reads delivery notes and certificates at goods in.</li>
  <li><strong>Order acknowledgements</strong> drafted for the customer, for a person to send.</li>
  <li><strong>Questions about orders,</strong> answered from the order data by a read-only assistant.</li>
  <li><strong>Confidence-based routing,</strong> where clean, repeat orders from long-standing customers need only a one-click confirmation. We would consider this only after months of measured accuracy.</li>
</ul>
<p>Our guide to <a href="''' + G + '''ai-for-small-manufacturers/">AI for small manufacturers</a> explains how we judge which of these is worth doing.</p>
''', '''
<p>If order entry, or any other document-heavy task, takes hours a day in your business, the first step is small. Gather twenty recent examples and note how long each took to process and what went wrong.</p>
<p>Send us those and we will tell you whether it is a good candidate, and what a proof of concept would involve. The <a href="''' + M + '''ai-automation/">AI in manufacturing</a> page lists other use cases we would and would not recommend.</p>
''']),
    faqs=[('Why does a person still confirm every order?',
           'Because extraction is not perfect and cannot tell which of its answers are wrong. A short review catches errors before they become wrong orders, and the corrections provide a running measure of accuracy.'),
          ('Which AI model would be used?',
           'The design keeps the extraction service replaceable. Options include the OCR and custom model features in Zoho Creator or an outside provider connected with your own account. The proof of concept decides which reads your documents best.'),
          ('What happens to our customers&rsquo; documents?',
           'That depends on the service chosen. Before go-live you should confirm where documents are processed, how long they are kept and whether they are used for training, and check your customer contracts.'),
          ('How accurate is it?',
           'It varies with document quality and layout, which is why the plan starts with a test on 100 of your own past orders against a pass mark agreed in advance.')],
    sources=[SRC['creator_ai'], SRC['creator_features'], SRC['mcp']],
    related=['ai-for-small-manufacturers', 'connect-sales-production-accounts', 'manufacturing-dashboards-kpis'],
))
