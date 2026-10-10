"""Manufacturing guides, part C."""
from content_common import *

GUIDES = []

# ====================================================================== 8. Dashboards and KPIs
S = 'manufacturing-dashboards-kpis'
cover(S, 'Reporting', 'Manufacturing dashboards and KPIs', 'Six measures worth tracking, how to calculate them and what to leave out.',
      two(m_tiles([('1', 'On-time delivery', 'Did we keep the promise?'), ('2', 'First-pass yield', 'Right first time?'), ('3', 'OEE', 'How well a machine ran'), ('4', 'WIP age', 'What is stuck?')])),
      theme='amber', alt='Cover: four of the measures covered in the guide: on-time delivery, first-pass yield, OEE and WIP age')
D1 = fig(S + '-table', m_table(['Measure', 'Formula', 'Needs this data'],
                                [['On-time delivery', 'Orders shipped by promise date &divide; orders shipped', 'Promise date and ship date'], ['First-pass yield', 'Units passed first time &divide; units started', 'Inspection results'],
                                 ['Scrap rate', 'Units scrapped &divide; units started', 'Scrap with a reason'], ['Schedule adherence', 'Jobs finished in the planned week &divide; jobs planned', 'Planned and actual finish'],
                                 ['WIP age', 'Days since each open job last moved', 'A time stamp per stage'], ['OEE', 'Availability &times; performance &times; quality', 'Run time, count, rejects']], '.8fr 1.5fr 1fr'),
         'Table of six manufacturing measures with the formula for each and the data it needs',
         'Six measures. The right-hand column decides which you can have today.', h=560, theme='amber', title='Six measures and what each needs')
D2 = fig(S + '-oee', m_formula('OEE = availability &times; performance &times; quality',
                                [('87.5%', 'Availability: ran 420 of 480 planned minutes'), ('90%', 'Performance: made 378 of a possible 420'), ('95%', 'Quality: 359 of 378 were good')], 'OEE = 0.875 &times; 0.90 &times; 0.95 = 74.8% for this shift, on this machine'),
         'Worked example of overall equipment effectiveness: 87.5 percent availability times 90 percent performance times 95 percent quality gives 74.8 percent',
         'OEE worked through for one shift with example numbers. The three parts are more useful than the total.', h=420, theme='amber', title='OEE, worked through')
D3 = fig(S + '-ops', app('Operations', 'Concept on Zoho Analytics', ['This week', 'Delivery', 'Quality', 'Machines', 'Reports'], 'This week', 'Operations: this week', 'Week 41 &middot; updated 10 minutes ago',
         kpis([('On-time delivery', '91%', '+4 pts', 'up'), ('First-pass yield', '94.2%', '+0.6 pts', 'up'), ('Jobs on hold', '3', '1 over 2 days', 'dn'), ('Oldest open job', '19 days', 'WO-2188', 'dn')])
         + g2(panel('On-time delivery by week', svg_bars([84, 86, 82, 88, 87, 90, 87, 91], ['34', '35', '36', '37', '38', '39', '40', '41'], ymax=100, target=95, unit='%', h=230), 'target 95%'),
              panel('Needs a decision today', listing([('r', 'WO-2188 has not moved for 6 days', 'Waiting on customer drawing approval'), ('y', '3 jobs due this week are still in cutting', 'Laser queue is 2 days long'), ('y', 'Scrap on Line 2 is twice its usual level', '14 units, reason: setup'), ('g', 'All purchase orders for next week received', '')]), 'exceptions first'), '1.25fr')),
         'Concept weekly operations dashboard with four headline numbers, an on-time delivery chart against target and a list of items needing a decision',
         'A concept operations dashboard. The right-hand panel matters most: it lists what somebody has to decide.', h=620, ui=True)
D4 = fig(S + '-dd', m_dd(['Show the trend, not just today', 'Put a target line on every chart', 'List exceptions with an owner', 'Fix each definition in writing', 'Review in the same meeting weekly'],
                          ['Twenty charts on one screen', 'Numbers nobody can act on', 'Averages that hide the bad job', 'Typing data in for the dashboard', 'Changing a formula quietly'], ('Good dashboards', 'Poor dashboards')),
         'Two lists contrasting good dashboard practice with poor practice, five points each',
         'What separates a dashboard people use from one they stop opening.', h=480, theme='amber')
D5 = fig(S + '-levels', m_tiers([('Operators', 'Line screen', 'Refreshed live', ['Today&rsquo;s jobs and their order', 'Count against target', 'Anything on hold']),
                                  ('Supervisors', 'Daily board', 'Checked each morning', ['Jobs late or stuck', 'Scrap by reason', 'People and machine cover']),
                                  ('Managers', 'Weekly review', 'Read in one meeting', ['Delivery and yield trends', 'Top three causes', 'Actions and owners'])], on=1),
         'Three levels of dashboard: a live line screen for operators, a daily board for supervisors and a weekly review for managers',
         'Three audiences, three screens. One dashboard for everyone suits no one.', h=500, theme='amber', title='Who needs to see what')
D6 = fig(S + '-wip', app('Operations', 'Concept on Zoho Analytics', ['This week', 'Delivery', 'Quality', 'Machines', 'Reports'], 'Delivery', 'Open jobs by age', 'Jobs that have not moved are listed first',
         panel('Work in progress', table('110px minmax(0,1.4fr) 110px 120px 96px minmax(0,1fr) 104px', ['Job', 'Product', 'Stage', '>Days in stage', 'Due', 'Blocked by', 'Status'],
               [[('sn', 'WO-2188'), 'Control cabinet C-12', 'Assembly', ('r', '6'), '8 Oct', 'Drawing approval', ('st', 'r', 'Late')], [('sn', 'WO-2203'), 'Bracket BR-40 &times; 600', 'Rework', ('r', '2'), '13 Oct', 'NCR-0318', ('st', 'y', 'At risk')],
                [('sn', 'WO-2207'), 'Guard panel GP-7 &times; 40', 'Cutting', ('r', '2'), '14 Oct', 'Laser queue', ('st', 'y', 'At risk')], [('sn', 'WO-2210'), 'Frame F-200 &times; 12', 'Welding', ('r', '1'), '16 Oct', '', ('st', 'g', 'On track')],
                [('sn', 'WO-2214'), 'Shelf unit S-8 &times; 30', 'Painting', ('r', '0'), '17 Oct', '', ('st', 'g', 'On track')]]), 'sorted by days in stage', 'flex:1'),
         actions='<span class="btns">Export</span>'),
         'Concept list of open jobs sorted by the number of days since they last moved, with stage, due date, what is blocking them and a status',
         'A concept WIP age report. Sorting by days in stage puts the stuck job at the top, whatever its due date.', h=450, ui=True)

GUIDES.append(dict(
    slug=S, title='Manufacturing Dashboards and KPIs: What to Measure First',
    seo_title='Manufacturing KPIs and Dashboards: What to Track',
    desc='Six manufacturing KPIs a small factory should track first, with formulas, a worked OEE example and rules for dashboards that people keep using.',
    lead='Most factory dashboards fail for a dull reason. They show numbers nobody was asked to act on, built on data somebody had to type in specially.',
    category='Reporting', kind='guide', kind_label='Practical guide', tone='amber', layout='wide', author='team', published=TODAY, keyword='manufacturing KPIs dashboard',
    facts=[('Start with', 'On-time delivery and first-pass yield'), ('Add later', 'OEE, once counts are automatic'), ('Rule', 'Every number has an owner'), ('Built with', 'Zoho Analytics over your live data')],
    hero_alt='Cover: four manufacturing measures', hero_cap='Four of the six measures in this guide. Start with the two on the left.',
    answer='Start with two measures you already hold the data for: on-time delivery and first-pass yield. Add scrap rate, schedule adherence and WIP age once jobs are tracked by stage. Leave OEE until run time and counts are recorded without extra typing. Give each number a written definition, a target and an owner, and review them weekly.',
    body='''
<p>A dashboard is the last thing to build, not the first. It can only show what the business already records, and it only earns its place if someone changes a decision because of it.</p>
<p>This guide picks six measures that suit a small manufacturer, shows how each is calculated and sets out the design rules that keep a dashboard in use after its first month.</p>

<h2 id="pick">How to pick a measure</h2>
<p>Put every candidate through three questions:</p>
<ol>
  <li><strong>Who will act on it?</strong> If you cannot name the person, leave it out.</li>
  <li><strong>What will they do when it is bad?</strong> If the answer is &ldquo;nothing we can do&rdquo;, leave it out.</li>
  <li><strong>Is the data recorded already, as part of the work?</strong> If someone must type it in for the report, it will stop being typed in.</li>
</ol>
<p>Six measures pass those questions for most small factories.</p>
''' + D1 + '''

<h2 id="delivery">On-time delivery</h2>
<p>The customer&rsquo;s view of your factory in one number. Divide the orders shipped on or before the promised date by all orders shipped in the period.</p>
<p>Two decisions make or break it:</p>
<ul>
  <li><strong>Which date?</strong> Use the date first promised to the customer. If the promise date is moved every time a job slips, the number will always look good and mean nothing. Keep the original date in its own field.</li>
  <li><strong>Whole orders or lines?</strong> An order shipped in two parts, one late, is late from the customer&rsquo;s side. Count whole orders unless customers accept part shipments as normal.</li>
</ul>

<h2 id="quality">First-pass yield and scrap rate</h2>
<p>First-pass yield is the share of units that passed inspection the first time, with no rework. Scrap rate is the share written off. Together they tell you how much of your capacity went into making things twice.</p>
<p>Both depend on scrap and rework being recorded with a reason chosen from a list. A total with no reasons tells you there is a problem and nothing about where. Our guide to <a href="''' + G + '''quality-ncr-capa-workflow/">inspections, NCRs and CAPA</a> covers the records behind these numbers.</p>

<h2 id="flow">Schedule adherence and WIP age</h2>
<p>Schedule adherence asks whether the jobs planned for a week were finished in that week. It measures the plan as much as the floor: a plan that is never met is a poor plan.</p>
<p>WIP age is less well known and often more useful. For every open job, count the days since it last moved to a new stage. Then sort the list with the oldest first.</p>
''' + D6 + '''
<p>A due-date list shows what is late. A WIP age list shows what is stuck, which is what you can still do something about. It needs one thing: a time stamp each time a job changes stage. That comes free with <a href="''' + G + '''production-tracking-zoho-creator/">stage-based production tracking</a>.</p>

<h2 id="oee">OEE, and when to wait</h2>
<p>Overall equipment effectiveness combines three ratios for one machine or line over one period.</p>
<ul>
  <li><strong>Availability:</strong> the time it ran, divided by the time it was planned to run.</li>
  <li><strong>Performance:</strong> what it made, divided by what it could have made in that run time at its ideal rate.</li>
  <li><strong>Quality:</strong> the good units, divided by all units made.</li>
</ul>
''' + D2 + '''
<p>In the example, the machine lost an hour to stoppages, ran a little slower than its ideal rate and rejected 19 units. The total, 74.8%, says little by itself. The three parts say where the loss was: mostly in stopped time.</p>
''' + callout('When to leave OEE alone', 'OEE needs run time, stop time, counts and rejects per machine. If operators have to write those on a sheet, the figures will be estimates and the number will mislead. Use it for machines where counts come from the machine or from a scan, and only for the one or two machines that limit your output.', True) + '''
<p>OEE also suits repetitive production better than job shops. If every job is different, the &ldquo;ideal rate&rdquo; is a guess, and schedule adherence and WIP age will tell you more.</p>

<h2 id="design">Designing the dashboard</h2>
''' + D3 + '''
<p>The screen above follows four rules.</p>
<ul>
  <li><strong>Few numbers.</strong> Four headline figures, each with its change since last period.</li>
  <li><strong>Trends with targets.</strong> A single week proves nothing. Eight weeks against a target line shows direction.</li>
  <li><strong>Exceptions as a list.</strong> The panel on the right names the jobs that need a decision. A manager can act on a list; a gauge only causes worry.</li>
  <li><strong>Freshness shown.</strong> If people cannot tell when the data was updated, they will not trust it.</li>
</ul>
''' + D4 + '''

<h2 id="audiences">Different screens for different people</h2>
''' + D5 + '''
<p>An operator needs to know what to run next and whether the line is ahead or behind. A supervisor needs today&rsquo;s problems. A manager needs trends and causes. Trying to serve all three with one screen produces something too detailed for the manager and too slow for the operator.</p>

<h2 id="worked-example">A worked example: from number to action</h2>
<p>An example fabricator reviews its dashboard on Monday. On-time delivery has dropped from 90% to 82% in a fortnight.</p>
<ol>
  <li>The late orders are listed. Seven of nine passed through the laser cutter.</li>
  <li>WIP age shows jobs waiting two days in the cutting queue, where half a day is normal.</li>
  <li>Hold reasons show the laser stopped three times for a nozzle fault.</li>
  <li>The action is a maintenance job and a temporary second shift on the laser, with a named owner and a date.</li>
</ol>
<p>The dashboard did not solve anything. It shortened the route from &ldquo;deliveries are slipping&rdquo; to &ldquo;fix the laser&rdquo; from a week of argument to one meeting. That is all a dashboard is for.</p>

<h2 id="building-it">Building it</h2>
<p>For businesses on Zoho, <a href="/zoho-integrations/">Zoho Analytics</a> is the usual tool. It connects to Zoho apps and to outside databases and files, schedules reports by email, raises data alerts when a figure crosses a threshold and includes forecasting. Its assistant, Ask Zia, answers questions typed in plain language. Dashboards can be embedded in a Creator app, so supervisors see them where they already work.</p>
<p>Three practical points:</p>
<ul>
  <li><strong>Write the definitions down</strong> before building anything. One page: name, formula, data source, owner, target.</li>
  <li><strong>Build from transactions,</strong> not from summaries someone keeps by hand.</li>
  <li><strong>Start with alerts on two numbers.</strong> A message when a job has not moved for three days does more than a screen nobody opens.</li>
</ul>

<h2 id="mistakes">Mistakes to avoid</h2>
<ul>
  <li><strong>Measuring what is easy.</strong> Machine hours are easy to count and rarely what limits you.</li>
  <li><strong>Moving the target date.</strong> It hides every late order.</li>
  <li><strong>Comparing people.</strong> A league table of operators teaches them to under-report scrap.</li>
  <li><strong>Building before the data exists.</strong> If stock or job status is unreliable, fix that first. See our <a href="''' + G + '''inventory-accuracy-for-manufacturers/">inventory accuracy guide</a>.</li>
</ul>

<h2 id="next-steps">A first month</h2>
<ol>
  <li>Calculate on-time delivery for the last three months by hand, from order and dispatch records.</li>
  <li>Write the one-page definition sheet for two measures.</li>
  <li>Build one screen with two numbers, two trends and an exceptions list.</li>
  <li>Review it in the same weekly meeting for a month, and note each decision it led to.</li>
</ol>
''',
    faqs=[('Which KPIs should a small manufacturer track first?',
           'On-time delivery and first-pass yield. Most businesses already hold the data for both, and they cover the two things customers notice: whether the order arrived when promised and whether it was right.'),
          ('How is OEE calculated?',
           'Multiply availability by performance by quality. Availability is run time over planned time, performance is actual output over possible output at the ideal rate, and quality is good units over total units.'),
          ('Is OEE worth tracking in a job shop?',
           'Often not at first. OEE suits repetitive production where an ideal rate is known. In a job shop, schedule adherence and WIP age usually say more and need less data.'),
          ('Can Zoho Analytics build manufacturing dashboards?',
           'Yes. It connects to Zoho apps and to other databases, and offers scheduled reports, data alerts, forecasting and a plain-language assistant. The quality of the dashboard depends on the quality of the data recorded underneath it.')],
    sources=[SRC['analytics'], SRC['creator_features']],
    related=['production-tracking-zoho-creator', 'quality-ncr-capa-workflow', 'ai-for-small-manufacturers'],
    services=[SVC['integ'], SVC['creator'], SVC['mwf']],
))

# ====================================================================== 9. AI for small manufacturers
S = 'ai-for-small-manufacturers'
cover(S, 'AI in practice', 'AI for small manufacturers', 'Where it helps today, where it does not, and how to test it safely.',
      m_rows([('Reads documents', 'Orders, delivery notes and certificates'), ('Answers questions', 'About your own jobs, stock and orders'), ('Flags what looks wrong', 'A person still decides')]),
      theme='navy', solid=True, alt='Cover: three things AI does well for a small manufacturer: reading documents, answering questions and flagging what looks wrong')
A1 = fig(S + '-matrix', m_matrix([('Low risk, data ready', 'Start here', 'Reading purchase orders, summarising shift notes'), ('Low risk, data not ready', 'Fix the data first', 'Answering questions about job status'),
                                   ('High risk, data ready', 'Assist only', 'Suggested reorders, quality triage'), ('High risk, data not ready', 'Not yet', 'Automatic scheduling, automatic pricing')]),
         'Two-by-two matrix of risk against data readiness with a recommended stance for each quadrant',
         'Plot each idea on two axes: what a wrong answer would cost, and whether the data exists.', h=520, theme='navy', title='Where to start')
A2 = fig(S + '-table', m_table(['Task', 'What the AI does', 'What a person does'],
                                [['Customer purchase orders', 'Reads the PDF and fills in a draft order', 'Checks and confirms'], ['Supplier documents', 'Pulls lot numbers and dates from certificates', 'Approves the receipt'],
                                 ['Questions about operations', 'Finds and totals the records', 'Judges the answer'], ['Defect photos', 'Sorts into likely categories', 'Makes the pass or fail call'],
                                 ['Demand and usage', 'Projects a trend from history', 'Sets the order quantity']], '.9fr 1.3fr .9fr'),
         'Table of five AI-assisted tasks showing what the AI does and what a person still does in each',
         'Five practical uses. In each one the AI prepares and a person decides.', h=520, theme='navy', title='Who does what')
A3 = fig(S + '-arch', m_arch([('People', 'approve, correct and decide', ['Sales admin', 'Buyer', 'Quality lead', 'Planner']),
                               ('Review step', 'every AI output lands here first', ['Draft shown beside the source', 'Confidence flags', 'Accept, edit or reject', 'Corrections logged'], True),
                               ('AI services', 'read, classify, predict, answer', ['Document extraction', 'Prediction models', 'Language model', 'Image classification']),
                               ('Your systems', 'the record of truth', ['Orders', 'Stock', 'Production', 'Quality', 'Accounts'])]),
         'Architecture showing AI services sitting above business systems, with a review step between the AI and the people who approve its output',
         'The pattern we use. AI output never writes straight to the record; it passes a review step first.', h=540, theme='navy', title='AI with a review step')
A4 = fig(S + '-review', app('Order Intake', 'Concept on Zoho Creator', ['Inbox', 'In review', 'Confirmed', 'Rejected', 'Accuracy log'], 'In review', 'Purchase order PO-88214 &middot; Harbour Fitouts', 'Received by email 09:12 &middot; read by AI 09:13',
         g2(panel('Extracted fields', table('minmax(0,1fr) minmax(0,1.3fr) 104px', ['Field', 'Value read', 'Check'],
                  [['Customer', 'Harbour Fitouts Ltd', ('st', 'g', 'Matched')], ['PO number', 'PO-88214', ('st', 'g', 'Clear')], ['Delivery date', '24 Oct 2026', ('st', 'g', 'Clear')],
                   ['Line 1', 'Oak vanity 900 &times; 12', ('st', 'g', 'Matched')], ['Line 2', 'Shelf unit S-8 &times; 30', ('st', 'g', 'Matched')], ['Line 3', '&ldquo;Vanity top, stone&rdquo; &times; 12', ('st', 'r', 'No match')],
                   ['Unit price, line 1', '412.00', ('st', 'y', 'Differs')]]), '7 fields &middot; 2 need attention'),
            panel('What needs you', listing([('r', 'Line 3 is not in the item list', 'Pick an item or ask the customer'), ('y', 'Price differs from the price list', 'Price list says 425.00'), ('g', 'Customer and delivery address matched', 'Existing account')])
                  + acts(('btnp', 'Confirm order'), ('btns', 'Edit'), ('btnr', 'Reject')) + note('Nothing is created in the order system until someone confirms.'), 'reviewer: sales admin'), '1.3fr')),
         'Concept review screen for an AI-read purchase order, listing each extracted field with a check status and the two items that need a person',
         'A concept review screen. The AI did the typing; the person spends their time on the two lines that need judgement.', h=560, ui=True)
A5 = fig(S + '-poc', m_steps([('Pick one task', 'Narrow, frequent, checkable', 'Week 1'), ('Gather examples', '50 to 100 real cases with the right answers', 'Week 1-2'), ('Run side by side', 'AI drafts, people work as normal', 'Week 3-4'), ('Measure, decide', 'Accuracy, time saved, errors caught', 'Week 5')],
                              ['#6CB4F5', '#3CCB7F', '#F9B21D', '#F28B3C']),
         'Four steps of a small AI proof of concept over five weeks: pick one task, gather examples, run side by side and measure',
         'A five-week proof of concept. Its purpose is to produce a number you can trust before anything goes live.', h=440, theme='navy', title='A small proof of concept')
A6 = fig(S + '-ask', app('Ask Operations', 'Concept assistant', [], '', 'Ask about jobs, stock and orders', 'Answers come from your records, with the source shown',
         chat([('q', 'Which jobs due this week are at risk?'), ('a', 'Three of 14 jobs due this week are at risk: WO-2188 (on hold 6 days, drawing approval), WO-2203 (in rework after NCR-0318) and WO-2207 (2 days in the laser queue).', 'Source: work orders and holds, read at 09:40 &middot; 14 records'),
               ('q', 'Do we have enough 18 mm MDF for next week?'), ('a', 'On hand: 22 sheets. Jobs planned next week need 31. A purchase order for 40 sheets is due on Monday.', 'Source: stock on hand, job materials, open purchase orders')])
         + note('Read-only. The assistant can look things up; it cannot change a record.'), side=False),
         'Concept assistant screen answering two questions about at-risk jobs and material availability, each answer citing the records it used',
         'A concept question-and-answer assistant. Each answer names its source, and the assistant has read-only access.', h=480, ui=True)

GUIDES.append(dict(
    slug=S, title='AI for Small Manufacturers: Where It Helps and Where It Does Not',
    seo_title='AI for Small Manufacturers: A Practical Guide',
    desc='A practical guide to AI in a small factory: five uses that work today, what to avoid, the review step every AI workflow needs and a five-week test.',
    lead='I am asked every week whether AI can run a factory. It cannot. It can take a surprising amount of typing, searching and sorting off your people, if you put a person where the judgement is.',
    category='AI and automation', kind='guide', kind_label='Opinionated guide', tone='dark', layout='toc-right', author='arun', published=TODAY, keyword='AI for small manufacturers',
    facts=[('Works today', 'Reading documents, answering questions'), ('Needs care', 'Predictions and image checks'), ('Not yet', 'Unsupervised decisions'), ('Always', 'A person approves')],
    hero_alt='Cover: three things AI does well for a small manufacturer', hero_cap='Three uses that work now. Each one ends with a person deciding.',
    answer='AI is useful in a small factory for narrow, frequent, checkable tasks: reading purchase orders and supplier documents, answering questions about your own data, sorting defect photos and projecting usage. It should prepare work for a person, not act alone. Start with one task, test it on 50 to 100 real examples, and measure accuracy before going live.',
    body='''
<p>There are two ways to get AI wrong in a factory. One is to ignore it because the claims are inflated. The other is to believe the claims and hand it decisions it has no business making. This guide is my attempt at the ground between.</p>
<p>I build these systems, so I have an interest. I have also seen enough of them to know which ones are still in use six months on. They share three features: the task is narrow, the output is easy to check, and a named person approves it.</p>

<h2 id="what-ai-is">What &ldquo;AI&rdquo; means here</h2>
<p>Four different technologies are sold under one word. They behave differently, so it helps to separate them.</p>
<ul>
  <li><strong>Document extraction.</strong> Reading text and fields from PDFs, scans and photos. Mature and dependable on clear documents.</li>
  <li><strong>Prediction.</strong> Estimating a number or a category from past records, such as next month&rsquo;s usage of a material. As good as the history it learns from.</li>
  <li><strong>Language models.</strong> Reading and writing text: summarising, answering questions, drafting. Fluent, and capable of being confidently wrong.</li>
  <li><strong>Image classification.</strong> Sorting photos into categories. Works when lighting and camera position are controlled.</li>
</ul>
<p>None of them understands your factory. Each one maps an input to an output, well or badly.</p>

<h2 id="where-to-start">Where to start</h2>
''' + A1 + '''
<p>Two questions place any idea on this grid. What happens if the answer is wrong? And does the data it needs already exist in a system?</p>
<p>A misread quantity on a draft order costs a correction if someone reviews it. A wrong production schedule costs a week. Start where mistakes are cheap and visible.</p>

<h2 id="five-uses">Five uses that work today</h2>
''' + A2 + '''
<h3>1. Reading customer purchase orders</h3>
<p>Customers send orders as PDFs in their own layouts. Someone retypes each into your system. Extraction reads the document, matches the customer and items against your lists and fills in a draft. The reviewer sees the draft beside the original and fixes what is flagged.</p>
''' + A4 + '''
<p>This is the use I recommend first. The task is frequent, the result is easy to check against the page, and the time saved is obvious. Our <a href="''' + CS + '''ai-purchase-order-intake/">order intake reference implementation</a> describes the full design.</p>
<h3>2. Reading supplier documents</h3>
<p>Delivery notes and certificates of conformity carry lot numbers, dates and test values that belong in your <a href="''' + G + '''batch-lot-traceability/">traceability records</a>. Extraction pulls them out at receiving so nobody types a 14-character lot number.</p>
<h3>3. Answering questions about your own data</h3>
<p>&ldquo;Which jobs due this week are at risk?&rdquo; is a query across work orders, holds and due dates. A language model connected to those records can answer it in a sentence.</p>
''' + A6 + '''
<p>Two rules apply. The assistant should be read-only, and every answer should name the records it used so a person can check. This also depends entirely on the data being right, which is why it sits in the &ldquo;fix the data first&rdquo; quadrant for most businesses.</p>
<h3>4. Sorting defect photos</h3>
<p>If inspectors photograph defects, a classifier can suggest a category: scratch, dent, misalignment. That speeds up recording and makes cause analysis more consistent. I would not let it make the pass or fail call without a long, measured trial.</p>
<h3>5. Projecting usage</h3>
<p>A prediction model can project material usage from history, which helps set <a href="''' + G + '''purchasing-reorder-points/">reorder points</a>. Treat the projection as one input to the buyer&rsquo;s decision. It knows nothing about the large order you are about to win.</p>

<h2 id="review-step">The review step</h2>
<p>Every design I am willing to put my name to has the same shape.</p>
''' + A3 + '''
<p>The AI never writes directly to the system of record. Its output goes to a review screen where a person accepts, edits or rejects it. Four details matter:</p>
<ul>
  <li><strong>Show the source.</strong> The reviewer sees the original document or the records behind an answer.</li>
  <li><strong>Flag doubt.</strong> Fields the model was unsure of, or that failed a check, are marked.</li>
  <li><strong>Log corrections.</strong> Each edit is recorded. That log is your accuracy measure.</li>
  <li><strong>Have a manual route.</strong> When the AI service is unavailable, people can still do the job.</li>
</ul>
''' + callout('Why not just let it run?', 'Because a system that is right 97 times in 100 is wrong three times, and it does not know which three. On 40 orders a day that is more than one wrong order every day. A review that takes thirty seconds is cheap insurance.', True) + '''

<h2 id="not-yet">What I would not use it for yet</h2>
<ul>
  <li><strong>Automatic scheduling.</strong> Schedules depend on things no system holds: a customer who will accept a delay, an operator who is slow on one machine.</li>
  <li><strong>Automatic purchasing.</strong> Draft the order, yes. Send it without a buyer, no.</li>
  <li><strong>Final quality decisions</strong> on anything safety-related or customer-critical.</li>
  <li><strong>Pricing and quoting</strong> without review. A fluent, wrong quote is still a commitment.</li>
  <li><strong>Anything with no data behind it.</strong> AI will not rescue a process that is not recorded.</li>
</ul>

<h2 id="data-and-security">Data and security questions to ask</h2>
<p>Before any AI feature goes near your documents, get plain answers to these:</p>
<ul>
  <li>Where is the data processed, and is it kept afterwards?</li>
  <li>Is it used to train models other customers use?</li>
  <li>What can the AI read, and what can it change? The safest answer to the second is &ldquo;nothing&rdquo;.</li>
  <li>Is every AI action logged with the user who approved it?</li>
  <li>What do customer contracts say about sharing their drawings or orders with a third party?</li>
</ul>
<p>Answers differ by product and plan, so check the current terms for whichever service you use.</p>

<h2 id="in-zoho">What exists in the Zoho platform</h2>
<p>If you run on Zoho, several of these pieces are already there. Zoho Creator includes an AI Modeler with prediction, OCR, object detection and keyword extraction, and supports custom models. Zoho Analytics has forecasting and a plain-language assistant. Zoho&rsquo;s agent tools allow a business to connect its own account with an outside model provider, and Zoho publishes an MCP server so that an assistant can read Zoho data with permission. Our article on <a href="/insights/zoho-mcp-claude-chatgpt/">connecting an AI assistant to Zoho</a> covers that last part.</p>
<p>Which of these you can use depends on your plan and region. Confirm before designing around one.</p>

<h2 id="poc">Test it with a small proof of concept</h2>
''' + A5 + '''
<p>A proof of concept exists to produce one number: how often was the AI right, on your documents, compared with your people? Collect 50 to 100 real examples with known correct answers. Run the AI alongside normal work for two weeks. Count field-level accuracy, the time a review takes, and the errors the review caught.</p>
<p>Set the pass mark before you start. If the test falls short, you have spent a few weeks, not a budget.</p>

<h2 id="next-steps">What to do next</h2>
<ol>
  <li>List the tasks where someone retypes, searches or sorts for more than an hour a day.</li>
  <li>Place each on the risk and readiness grid.</li>
  <li>Pick one from the top-left quadrant and collect examples.</li>
  <li>Run a five-week test with a pass mark agreed in advance.</li>
</ol>
<p>Our <a href="''' + M + '''ai-automation/">AI in manufacturing page</a> describes more use cases in the same format, each with its limits.</p>
''',
    faqs=[('Is AI worth it for a small manufacturer?',
           'For narrow tasks, yes. Reading purchase orders and supplier documents, and answering questions about your own data, save real time and are easy to check. Broad promises about AI running production are not realistic today.'),
          ('What should we try first?',
           'Reading incoming purchase orders into draft sales orders, with a person confirming each one. It is frequent, easy to verify against the document and low risk.'),
          ('Does AI replace our planner or buyer?',
           'No. It prepares drafts, projections and summaries. The planner and buyer still decide, because they know things that are not in any system.'),
          ('How do we know whether it is accurate enough?',
           'Test it on 50 to 100 real examples with known answers, run it beside normal work for two weeks and measure field-level accuracy. Set the pass mark before you start.'),
          ('Is our data safe?',
           'It depends on the service and plan. Ask where data is processed, whether it is retained or used for training, what the AI can change and whether actions are logged. Check customer contracts before sending their documents to any third party.')],
    sources=[SRC['creator_ai'], SRC['analytics'], SRC['mcp'], SRC['creator_features']],
    related=['ai-purchase-order-intake', 'manufacturing-dashboards-kpis', 'production-tracking-zoho-creator'],
    services=[SVC['mai'], SVC['bpa'], SVC['creator']],
    cta_title='Have a task you think AI could take on?', cta_text='Describe it and send a few sample documents. We will tell you whether it is a good candidate and what a five-week test would involve.',
))

# ====================================================================== 10. Connecting sales, production and accounts
S = 'connect-sales-production-accounts'
cover(S, 'Integration', 'Connecting sales, production and accounts', 'Decide who owns each record before you connect anything.',
      m_vt([('Sales', 'Customers and orders', 'Owned by the CRM or order system'), ('Stock', 'Items and quantities', 'Owned by the stock system'), ('Jobs', 'Work orders and stages', 'Owned by the production app'), ('Accounts', 'Invoices and payments', 'Owned by the accounting package')]),
      theme='blue', alt='Cover: four areas and the system that owns the records in each: sales, stock, production and accounts')
C1 = fig(S + '-owners', m_table(['Record', 'Owned by', 'Others may', 'Never'],
                                 [['Customer', 'CRM', 'Read it', 'Create a second copy'], ['Item and price', 'Stock system', 'Read it', 'Edit it locally'],
                                  ['Sales order', 'Order system', 'Read, update status', 'Change quantities'], ['Work order', 'Production app', 'Read progress', 'Move stages'],
                                  ['Stock quantity', 'Stock system', 'Post movements', 'Overwrite the total'], ['Invoice and payment', 'Accounting package', 'Read status', 'Edit amounts']], '.9fr 1fr 1fr 1fr'),
         'Table of six record types showing which system owns each, what other systems may do and what they must never do',
         'One owner per record. Most integration problems start with two systems both editing the same thing.', h=560, title='Who owns what')
C2 = fig(S + '-lanes', m_lanes(['Order', 'Make', 'Ship', 'Bill'], [
            ('CRM', [('Quote accepted', 'Order created', 'hi'), None, None, ('Payment status shown', 'Read only')]),
            ('Production app', [('Work order raised', 'From the order'), ('Stages completed', 'Scans on the floor', 'hi'), ('Marked ready', ''), None]),
            ('Stock system', [('Materials reserved', ''), ('Materials issued', 'Finished goods in'), ('Shipment posted', 'Stock reduced', 'hi'), None]),
            ('Accounts', [None, None, None, ('Invoice created', 'From the shipment', 'hi')])]),
         'Swimlane of the order-to-cash flow across CRM, production app, stock system and accounts, showing which system acts at each stage',
         'Order to cash across four systems. The dark cell in each column is the system that owns that step.', h=520, title='One order, four systems')
C3 = fig(S + '-methods', m_tiers([('Simplest', 'Built-in connection', 'Between apps from one vendor', ['No code to maintain', 'Fixed behaviour', 'Check what it syncs']),
                                   ('Flexible', 'Workflow tool or script', 'Zoho Flow or Deluge', ['Your own rules', 'Quick to change', 'Mind the limits']),
                                   ('Heavy duty', 'Custom middleware', 'A small service of your own', ['High volume', 'Queues and retries', 'Needs hosting'])], on=1),
         'Three integration methods: built-in connections, a workflow tool or script, and custom middleware, with three traits each',
         'Three ways to connect systems. Use the simplest one that meets the need.', h=500, title='Three ways to connect')
C4 = fig(S + '-monitor', app('Integration Monitor', 'Concept on Zoho Creator', ['Today', 'Failed', 'Retry queue', 'Mappings', 'Log'], 'Today', 'Sync activity', '10 Oct &middot; last run 2 minutes ago',
         kpis([('Messages today', '214', 'all flows', 'fl'), ('Succeeded', '209', '', 'fl'), ('Retried, then OK', '3', '', 'fl'), ('Need a person', '2', 'oldest 40 min', 'dn')])
         + panel('Needs attention', table('96px minmax(0,1fr) minmax(0,1.1fr) minmax(0,1.5fr) 110px', ['Time', 'Flow', 'Record', 'Reason', 'Action'],
                 [['09:12', 'Shipment &rarr; invoice', ('sn', 'SO-7790'), 'Customer has no tax code in accounts', ('st', 'r', 'Fix data')], ['09:31', 'Order &rarr; work order', ('sn', 'SO-7802'), 'Item BR-55 not found in production app', ('st', 'r', 'Map item')],
                  ['08:47', 'Stage log &rarr; stock', ('sn', 'WO-2210'), 'Stock system busy; retried after 5 minutes', ('st', 'g', 'Resolved')], ['08:02', 'Payment &rarr; CRM', ('sn', 'INV-3391'), 'Timed out; retried', ('st', 'g', 'Resolved')]]), 'failures are kept until someone clears them', 'flex:1'),
         actions='<span class="btns">Retry selected</span>'),
         'Concept integration monitor showing message counts for the day and a list of failed or retried syncs with the reason for each',
         'A concept integration monitor. Every failure has a reason a person can act on, and nothing fails silently.', h=560, ui=True)
C5 = fig(S + '-dd', m_dd(['One owner per record', 'One shared ID on every record', 'Retry, then tell a person', 'Sync events, not whole tables', 'Test with last month&rsquo;s real orders'],
                          ['Two-way sync of the same field', 'Matching on names', 'Failures written to a log nobody reads', 'Nightly bulk overwrites', 'Going live on all flows at once'], ('Do', 'Avoid')),
         'Two lists of integration practices to follow and to avoid, five each',
         'The habits that separate an integration that runs for years from one that needs weekly repair.', h=480)
C6 = fig(S + '-ids', m_cols([('CRM', 'Sales order', ['SO-7790', 'Customer C-0412', 'Item OV-900']), ('Production', 'Work order', ['WO-2291', 'Carries SO-7790', 'Item OV-900'], True),
                              ('Stock', 'Shipment', ['SH-5521', 'Carries SO-7790', 'Item OV-900']), ('Accounts', 'Invoice', ['INV-3402', 'Carries SO-7790', 'Customer C-0412'])]),
         'Four records for the same order in four systems, each carrying the same sales order number, customer code and item code',
         'The same order in four systems. The shared IDs are what make it one order and not four. Example data.', h=380, title='Shared IDs hold it together')

GUIDES.append(dict(
    slug=S, title='Connecting Sales Orders, Production and Accounts Without Double Entry',
    seo_title='Connect Sales Orders, Production and Accounts',
    desc='How to connect CRM, production, stock and accounting for a small manufacturer: record ownership, shared IDs, three integration methods and error handling.',
    lead='Double entry is the visible problem. The real one is that when two systems disagree, nobody knows which is right.',
    category='Integration', kind='arch', kind_label='Technical guide', tone='', layout='wide', author='team', published=TODAY, keyword='integrate sales production accounting',
    facts=[('First decision', 'Who owns each record'), ('Glue', 'One shared ID per order, item and customer'), ('Method', 'The simplest that works'), ('Must have', 'Visible failures and retries')],
    hero_alt='Cover: four areas and the system that owns each', hero_cap='Four areas, four owners. Agree this before any technical work.',
    answer='Give every record one owning system: customers in the CRM, items and quantities in the stock system, jobs in the production app, invoices in accounts. Carry the same order, item and customer IDs through all of them. Connect with the simplest method that works, send events as they happen, and make every failure visible to a person with a retry.',
    body='''
<p>A typical small manufacturer enters the same order four times: in a quote, on a job sheet, on a dispatch note and on an invoice. Each copy is a chance for a different quantity, a different price or a different address.</p>
<p>Connecting the systems removes the retyping. Done carelessly, it also creates a new problem: data that changes by itself, for reasons nobody can trace. This guide is about doing it carefully.</p>

<h2 id="ownership">Start with ownership, not technology</h2>
<p>Before choosing a tool, fill in one table. For every kind of record, name the one system allowed to create and change it.</p>
''' + C1 + '''
<p>The rule that follows is strict. Other systems may read a record, and may ask the owner to change it, but they keep no editable copy of their own. If a customer&rsquo;s address is wrong, it is corrected in the CRM and flows outwards. It is never fixed on the invoice alone.</p>
<p>The stock quantity row deserves a note. Other systems should post <em>movements</em>, such as &ldquo;issued 12&rdquo; or &ldquo;received 40&rdquo;, and let the stock system work out the total. An integration that writes &ldquo;quantity is now 236&rdquo; will sooner or later overwrite a change it did not know about. Our <a href="''' + G + '''inventory-accuracy-for-manufacturers/">inventory accuracy guide</a> explains why that matters.</p>

<h2 id="ids">Shared IDs</h2>
''' + C6 + '''
<p>Systems connect through identifiers, and three matter most.</p>
<ul>
  <li><strong>Customer code.</strong> The same in the CRM and in accounts. Matching on company name fails the first time someone types &ldquo;Ltd&rdquo; in one and &ldquo;Limited&rdquo; in the other.</li>
  <li><strong>Item code.</strong> One code per product and material, used everywhere. Clean this list before you integrate; it is the commonest cause of failed syncs.</li>
  <li><strong>Sales order number.</strong> Carried onto the work order, the shipment and the invoice, so any of them leads back to the others.</li>
</ul>
<p>Store the other system&rsquo;s ID on each record as well. When a work order holds the sales order&rsquo;s ID, an update can find its target directly and cannot create a duplicate by mistake.</p>

<h2 id="flow">The order-to-cash flow</h2>
''' + C2 + '''
<p>Read the diagram column by column. At each stage one system acts and the others are told.</p>
<ol>
  <li><strong>Order.</strong> An accepted quote becomes a sales order. That raises a work order and reserves materials.</li>
  <li><strong>Make.</strong> Operators complete stages. Materials are issued and finished goods received, as movements.</li>
  <li><strong>Ship.</strong> The stock system posts the shipment, which is the event that reduces stock.</li>
  <li><strong>Bill.</strong> The shipment creates the invoice in accounts. Payment status flows back to the CRM so sales can see it.</li>
</ol>
<p>Invoice from the shipment, not from the order. It means you bill what actually left the building, including part shipments.</p>

<h2 id="methods">Three ways to connect</h2>
''' + C3 + '''
<h3>Built-in connections</h3>
<p>Apps from one vendor usually connect to each other. Zoho Inventory, for example, integrates with Zoho Books and Zoho CRM, and with shipping carriers and online marketplaces. Use these first. Read exactly what each one syncs, and in which direction, before relying on it.</p>
<h3>A workflow tool or a script</h3>
<p>When the built-in behaviour is not enough, a workflow tool such as Zoho Flow, or a Deluge function, applies your own rules: &ldquo;when a sales order is confirmed and the item is made to order, create a work order with these stages.&rdquo; This covers most small manufacturers&rsquo; needs. Know the limits. Workflow tools meter tasks by plan, and some triggers check for changes on a schedule of minutes, not instantly. Scripts have execution limits per run. Our comparison of <a href="/insights/zoho-flow-vs-deluge/">Zoho Flow, Deluge and custom middleware</a> goes into detail.</p>
<h3>Custom middleware</h3>
<p>For high volumes, or when an outside system has an awkward interface, a small service of your own sits in the middle. It queues messages, retries failures and transforms data. It costs more to build and needs hosting and monitoring, so use it only when the first two will not do.</p>

<h2 id="accounts">A note on the accounting side</h2>
<p>Which accounting package you connect matters, and it varies by country. Zoho Books is published in country editions, including Australia, the United Kingdom, the United States and India, plus a global edition. New Zealand is not among the named editions at the time of writing. A New Zealand manufacturer therefore has two sensible options: use the global edition, or keep an accounting package built for New Zealand tax, such as Xero, and integrate with it.</p>
<p>Keeping your accounting package is a perfectly good decision. Your accountant knows it and your tax returns depend on it. The integration then sends invoices and bills to it and reads payment status back.</p>
''' + callout('Agree it with your accountant', 'Before automating invoices, ask whoever does your accounts how they want them to arrive: as drafts or approved, with which tax codes, to which revenue accounts. Ten minutes here prevents a month-end clean-up.') + '''

<h2 id="failures">Plan for failure</h2>
<p>Every integration fails sometimes. A system is briefly unavailable, an item is missing from a list, a customer has no tax code. What matters is what happens next.</p>
''' + C4 + '''
<ul>
  <li><strong>Retry what may be temporary.</strong> Time-outs and busy responses are retried automatically, a few times, with a pause between.</li>
  <li><strong>Tell a person about the rest.</strong> A missing item code will fail every time until someone fixes the data. It goes to a named person with the reason in plain words.</li>
  <li><strong>Keep the message.</strong> A failed update is held, not dropped, so it can be re-sent once the cause is fixed.</li>
  <li><strong>Make updates safe to repeat.</strong> Sending the same shipment twice must not create two invoices. Checking for the shared ID first prevents that.</li>
</ul>

<h2 id="worked-example">A worked example: one order, end to end</h2>
<p>An example joinery accepts a quote for 12 vanity units on Monday.</p>
<ol>
  <li>Sales marks the quote as won in the CRM. Sales order SO-7790 is created with customer code C-0412.</li>
  <li>Within a minute a work order appears in the production app, carrying SO-7790. Nobody typed it.</li>
  <li>Through the week, operators scan each stage. The CRM shows &ldquo;in assembly&rdquo; on the order, so sales can answer the customer without ringing the floor.</li>
  <li>On Friday dispatch ships 12 units. The stock system posts shipment SH-5521.</li>
  <li>The shipment creates invoice INV-3402 in accounts, as a draft for the bookkeeper to approve.</li>
  <li>When the customer pays, the CRM shows the order as paid.</li>
</ol>
<p>The order was typed once, at step one. Every later record was created from it and carries its number.</p>

<h2 id="rules">Rules worth keeping</h2>
''' + C5 + '''

<h2 id="next-steps">Where to begin</h2>
<ol>
  <li>Fill in the ownership table with the people who use each system.</li>
  <li>Clean the item and customer lists and agree the shared codes.</li>
  <li>Connect one flow, usually order to work order, and run it for two weeks.</li>
  <li>Add the monitor before adding the second flow.</li>
</ol>
<p>The <a href="''' + G + '''spreadsheets-to-connected-system-roadmap/">90-day roadmap</a> shows where integration fits in a wider plan.</p>
''',
    faqs=[('What is a system of record?',
           'The one system allowed to create and change a given kind of record. Other systems read from it or ask it to make changes. Deciding this for customers, items, orders, stock and invoices is the first step in any integration.'),
          ('Should the sync be two-way?',
           'Data can flow in both directions overall, but each field should have one owner. Two systems both editing the same field leads to changes overwriting each other.'),
          ('Can we keep Xero or another accounting package?',
           'Yes. Many manufacturers keep the accounting package their accountant already uses and connect it to their order and production systems. Invoices and bills are sent to it, and payment status is read back.'),
          ('Do we need custom middleware?',
           'Usually not. Built-in connections plus a workflow tool or script cover most small manufacturers. Middleware is worth it for high volumes or for systems with difficult interfaces.'),
          ('What happens when a sync fails?',
           'A well-built integration retries temporary errors automatically, holds the failed message, and tells a named person the reason for anything that needs a data fix. Failures should never be silent.')],
    sources=[SRC['inv_features'], SRC['books_editions'], SRC['flow'], SRC['deluge_limits']],
    related=['spreadsheets-to-connected-system-roadmap', 'purchasing-reorder-points', 'job-tracking-joinery-manufacturer'],
    services=[SVC['integ'], SVC['deluge'], SVC['mzoho']],
))
