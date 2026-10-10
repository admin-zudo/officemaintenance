"""Manufacturing guides, part A."""
from content_common import *

GUIDES = []

# ====================================================================== 1. Inventory accuracy
S = 'inventory-accuracy-for-manufacturers'
cover(S, 'Inventory accuracy', 'Why stock records drift', 'Five causes, one way to measure it, and the habits that keep it fixed.',
      two(m_tiles([('1', 'Late entries', 'Recorded at the end of the shift'), ('2', 'Unrecorded use', 'Scrap, samples and top-ups'),
                   ('3', 'Unit mix-ups', 'Bought in rolls, used in metres'), ('4', 'Moves', 'Stock shifted, system not told')])),
      theme='amber', alt='Four common causes of wrong stock records: late entries, unrecorded use, unit mix-ups and unrecorded moves')
F1 = fig(S + '-causes', m_rows([('Timing', 'Work happens now, the entry happens later'), ('Missing transactions', 'Scrap, samples, rework and top-ups never recorded'),
                                 ('Units and conversions', 'Purchase unit and usage unit are not the same'), ('Location', 'The total is right but the place is wrong')]),
         'Four numbered root causes of inventory inaccuracy: timing, missing transactions, units and conversions, and location',
         'Most stock errors trace back to one of four causes. Counting more often hides them; it does not remove them.', h=560, theme='amber', title='Where the errors come from')
F2 = fig(S + '-formula', m_formula('Record accuracy = records within tolerance &divide; records counted',
                                    [('120', 'item-locations counted this week'), ('102', 'matched the system within tolerance'), ('&plusmn;2%', 'tolerance used for bulk materials')],
                                    'Record accuracy = 102 &divide; 120 = 85%'),
         'Worked example of the record accuracy formula: 102 of 120 counted records within tolerance gives 85 percent',
         'A worked example. Measure by record, not by total value, or large errors in opposite directions cancel out.', h=400, theme='amber', title='How to measure it')
F3 = fig(S + '-count-app', phones([phone('Cycle count', 'Aisle B &middot; Bin B-04', pscan('Scan bin, then item') + pf('Item', 'Hinge 110&deg; soft-close') + pf('Counted quantity', '236') + pbtn('Save count')),
                                    phone('Variance found', 'System 250 &middot; Counted 236', pf('Difference', '-14 (5.6%)') + pf('Reason', 'Issued to job, not recorded') + pf('Recount by', 'Second counter') + pbtn('Send for approval', 'b'))],
                                   [('Blind count', 'The counter does not see the system quantity first'), ('Reason on every adjustment', 'So the cause gets fixed, not just the number')]),
         'Two concept phone screens for a cycle count: scanning a bin and entering a count, then recording a variance with a reason',
         'A concept for a cycle-count app on Zoho Creator. The variance screen asks for a reason before any stock is adjusted.', h=540, theme='amber', ui=True)
F4 = fig(S + '-abc', m_table(['Class', 'Typical items', 'Count how often', 'Tolerance'],
                              [['A', 'High value or high use', 'Every month', 'Exact'], ['B', 'Mid value, steady use', 'Every quarter', 'Within 1 to 2%'],
                               ['C', 'Low value, bulk', 'Twice a year', 'Within 5%'], ['Any', 'An item that just caused a stock-out', 'This week', 'Exact']], '.5fr 1.4fr 1fr 1fr'),
         'Cycle counting plan by ABC class with count frequency and tolerance for each class',
         'A starting cycle-count plan. Adjust the frequencies to the number of counters you actually have.', h=440, theme='amber', title='A cycle-count plan by class')
F5 = fig(S + '-dashboard', app('Stock Control', 'Concept on Zoho Analytics', ['Accuracy', 'Counts due', 'Adjustments', 'Reorder', 'Reports'], 'Accuracy', 'Inventory accuracy', 'Last 8 weeks &middot; all locations',
         kpis([('Record accuracy', '91%', '+6 pts in 8 weeks', 'up'), ('Counts done', '48 of 52', 'this week', 'fl'), ('Adjustments', '17', '9 with no reason', 'dn'), ('Stock-outs', '3', '-2 vs last month', 'up')])
         + g2(panel('Largest variances this week', table('minmax(0,1.2fr) 70px 80px 56px 122px', ['Item', '>System', '>Counted', '>Diff', 'Reason'],
                    [['Hinge 110&deg; soft-close', ('r', '250'), ('r', '236'), ('r', '-14'), ('st', 'y', 'Not issued')],
                     ['MDF 18 mm sheet', ('r', '64'), ('r', '61'), ('r', '-3'), ('st', 'r', 'Scrap missed')],
                     ['Edge tape oak 22 mm', ('r', '900 m'), ('r', '1,020 m'), ('r', '+120'), ('st', 'b', 'Unit mix-up')],
                     ['Drawer runner 450', ('r', '120'), ('r', '120'), ('r', '0'), ('st', 'g', 'Match')]]), '4 of 48'),
              panel('Accuracy by week', svg_line([[85, 84, 87, 88, 86, 89, 90, 91]], ['W34', 'W35', 'W36', 'W37', 'W38', 'W39', 'W40', 'W41'], ymax=100, h=330), '%'), '1.5fr'),
         actions='<span class="pilln">All locations</span>'),
         'Concept inventory accuracy dashboard with record accuracy, counts done, adjustments, stock-outs, a variance table and a weekly trend line',
         'A concept dashboard. The useful column is the reason: it tells you which process to fix.', h=640, ui=True)

GUIDES.append(dict(
    slug=S, title='Why Your Stock Records Are Wrong, and How to Fix Inventory Accuracy',
    seo_title='Fixing Inventory Accuracy in Manufacturing',
    desc='Why manufacturing stock records drift from reality, how to measure record accuracy, and the process and system changes that keep stock right.',
    lead='If planners walk to the shelf before they trust the screen, the stock system is costing you more than it saves. Counting harder is not the fix. Recording the work where it happens is.',
    category='Inventory', kind='problem', kind_label='Problem and solution', tone='amber', layout='toc-left', author='team', published=TODAY, keyword='inventory accuracy manufacturing',
    facts=[('The problem', 'System stock and shelf stock disagree'), ('The cause', 'Work is recorded late, or not at all'), ('The fix', 'Record at the point of work, then count by class'), ('Time to see change', 'Four to eight weeks')],
    hero_alt='Cover: why stock records drift, with four common causes', hero_cap='Four causes account for most wrong stock records in a small factory.',
    answer='Stock records go wrong when material moves or is used without a matching entry at that moment. Measure record accuracy by counting a sample each week, record every issue, move and scrap at the point of work with a scan, and require a reason on every adjustment. Cycle counting by ABC class then keeps it right.',
    body='''
<p>A purchasing manager once described her stock system to us as &ldquo;a list of what we used to have&rdquo;. Everyone in the building knew it was wrong, so everyone kept their own spreadsheet, and the spreadsheets disagreed with each other as well.</p>
<p>This is the most common problem we are asked to fix in small and midsized manufacturers. It is rarely a software problem. It is a recording problem that software can either hide or help with.</p>

<h2 id="what-it-costs">What inaccurate stock costs you</h2>
<p>The cost does not show up as one line in the accounts. It is spread across the business:</p>
<ul>
  <li><strong>Jobs that stop.</strong> The system said the part was there. It was not, and the job waits for a delivery.</li>
  <li><strong>Buying what you already have.</strong> The system said the part was not there. It was, in a different rack.</li>
  <li><strong>Safety stock that keeps growing.</strong> Nobody trusts the numbers, so everyone orders a bit extra.</li>
  <li><strong>Planners doing stock checks.</strong> Skilled people walk the floor with a clipboard every morning.</li>
  <li><strong>Costing you cannot trust.</strong> If usage is not recorded per job, job costs are guesses.</li>
</ul>

<h2 id="why-records-drift">Why records drift</h2>
<p>Stock is physically moved by many people, many times a day. The record only stays right if each of those movements produces an entry. When we trace errors back, they nearly always fall into four groups.</p>
''' + F1 + '''
<h3>Timing</h3>
<p>Material is issued at 8 am and entered at 5 pm, or on Friday. For those hours the system is wrong, and anything that reads it during that time, such as a reorder alert or a planner, acts on a wrong number. Batch entry also invites mistakes, because the person typing is working from memory or a paper sheet.</p>
<h3>Missing transactions</h3>
<p>Some movements have no form at all. Scrap goes in the bin. A sample goes to a customer. An operator tops up a job with three more brackets because two were damaged. Rework consumes extra material. None of it is theft or carelessness. There is simply nowhere quick to record it.</p>
<h3>Units and conversions</h3>
<p>You buy edge tape by the roll, store it by the roll and use it by the metre. If the item has one unit in the system and people enter whichever number is in front of them, the record drifts in both directions. The same happens with sheets and cut pieces, drums and litres, boxes and each.</p>
<h3>Location</h3>
<p>The total can be right while the record is still useless. If the system says 40 units in the main store and 30 of them are on a trolley by line 2, the picker will report a shortage.</p>

<h2 id="measure-it">Measure it before you fix it</h2>
<p>You need one number to track, and it should be simple enough to work out by hand. Use <strong>record accuracy</strong>: of the stock records you counted, how many matched the system within an agreed tolerance?</p>
''' + F2 + '''
<p>Three rules make the number honest:</p>
<ul>
  <li><strong>Count by item and location,</strong> not by item alone. &ldquo;Hinges, bin B-04&rdquo; is one record.</li>
  <li><strong>Set tolerances by type.</strong> Countable parts should match exactly. Bulk materials measured by weight or length can have a small tolerance.</li>
  <li><strong>Do not use stock value.</strong> A shortage of one item and a surplus of another cancel out in value and hide both errors.</li>
</ul>
<p>Take a first measurement before changing anything. A typical first result for a factory running on spreadsheets is far lower than people expect, and that number is what gets management attention.</p>

<h2 id="fix-at-source">Fix the recording, not the count</h2>
<p>A full stocktake corrects the numbers for a day. The causes are still there, so the errors return. The lasting fix is to make the entry part of the physical act.</p>
<ol>
  <li><strong>Record at the point of work.</strong> Issue, move, receive and scrap are recorded where they happen, on a phone or a fixed tablet, at that moment.</li>
  <li><strong>Scan, do not type.</strong> A barcode on the bin and on the item removes most keying errors. Labels cost very little compared with one stopped job.</li>
  <li><strong>One stock unit per item.</strong> Choose the unit you use on the floor. Convert on purchase, once, with a fixed factor held in the system.</li>
  <li><strong>Name every location.</strong> Racks, bins, trolleys, the quarantine cage and &ldquo;at subcontractor&rdquo; are all locations.</li>
  <li><strong>Give scrap and rework a button.</strong> If recording scrap takes ten seconds, it gets recorded.</li>
  <li><strong>Require a reason on every adjustment.</strong> Without a reason you correct the number and learn nothing.</li>
</ol>
''' + F3 + '''
''' + callout('A rule that works', 'Whoever moves it, records it. Do not create a stock clerk whose job is to enter other people&rsquo;s movements later. That rebuilds the timing problem.') + '''

<h2 id="cycle-counting">Then count a little, every week</h2>
<p>Once recording is under control, counting is a check on the process, not a repair job. Cycle counting means counting a small set of records every week so that each one is counted on a schedule.</p>
''' + F4 + '''
<p>Class the items by how much a wrong record would hurt: value, usage and how often they stop a job. Then:</p>
<ul>
  <li><strong>Count blind.</strong> The counter should not see the system quantity until they have entered their own.</li>
  <li><strong>Recount before adjusting.</strong> A second person recounts any variance outside tolerance.</li>
  <li><strong>Find the cause that week.</strong> While people still remember what happened.</li>
  <li><strong>Count at a quiet point.</strong> Before the shift starts, or with movements for that bin paused.</li>
</ul>

<h2 id="system-setup">Where this lives in the system</h2>
<p>You do not need a large ERP to do this well. For many small manufacturers the stock record sits in <strong>Zoho Inventory</strong>, which provides multi-warehouse stock, serial and batch tracking, barcode generation and scanning, reorder points and inventory adjustments. Zoho&rsquo;s own knowledge base is clear that Inventory does not include a manufacturing module, so production issues and scrap usually need something more.</p>
<p>That is where a small custom app helps. On <a href="/zoho-creator-development/">Zoho Creator</a> we build the screens operators actually use: issue to job, move, scrap, count. Creator forms can scan QR codes and barcodes on phones and tablets, and the app writes the result to the stock system through its API. Reporting sits on top in Zoho Analytics.</p>
''' + F5 + '''
<p>If you already run an ERP or an accounting package with stock, the same design applies. Keep that system as the record, and put a fast, scan-based screen in front of it. Our guide to <a href="''' + G + '''connect-sales-production-accounts/">connecting sales, production and accounts</a> covers the integration patterns.</p>

<h2 id="mistakes">Mistakes we see</h2>
<ul>
  <li><strong>Buying scanners before fixing the process.</strong> Scanning a wrong process gives you wrong data faster.</li>
  <li><strong>Too many locations on day one.</strong> Start with zones. Add bins where pick errors actually happen.</li>
  <li><strong>Adjusting without a reason code.</strong> The count gets fixed and the cause survives.</li>
  <li><strong>Backflushing against a wrong bill of materials.</strong> If the BOM says 4 and the job uses 5, every completed unit makes the record worse.</li>
  <li><strong>Treating it as a one-off project.</strong> Accuracy is a weekly routine with an owner.</li>
</ul>

<h2 id="next-steps">A 30-day start</h2>
<ol>
  <li><strong>Week 1:</strong> count 100 item-locations and work out record accuracy. Write down the reasons for each variance.</li>
  <li><strong>Week 2:</strong> pick the largest cause. Design the one screen that would have captured it.</li>
  <li><strong>Week 3:</strong> label the affected locations and items. Trial the screen in one area.</li>
  <li><strong>Week 4:</strong> start weekly cycle counts for class A items and publish the accuracy number where everyone can see it.</li>
</ol>
<p>If stock accuracy is blocking a bigger project, such as <a href="''' + G + '''production-tracking-zoho-creator/">production tracking</a> or <a href="''' + G + '''purchasing-reorder-points/">automatic reordering</a>, fix it first. Both depend on it.</p>
''',
    faqs=[('What is a good inventory record accuracy for a small manufacturer?',
           'Aim for the high nineties on the items that can stop production, measured by item and location. What matters more than the target is the trend and knowing the reason for each variance.'),
          ('Do we need barcode scanners to improve stock accuracy?',
           'Not dedicated scanners. A phone or tablet camera reading a printed label is enough to start. The gain comes from recording the movement at the moment it happens, with less typing.'),
          ('Should we do a full stocktake first?',
           'Do a sample count first to measure accuracy and find causes. A full stocktake is worth doing once the recording process has been fixed, otherwise the corrected numbers drift again within weeks.'),
          ('Can Zoho Inventory handle raw materials and work in progress?',
           'It handles raw materials and finished goods well, with batches, serial numbers and multiple warehouses. It has no manufacturing module, so issues to jobs, scrap and work in progress usually need a custom app or a separate manufacturing system alongside it.')],
    sources=[SRC['inv_features'], SRC['inv_mfg'], SRC['creator_scan']],
    related=['purchasing-reorder-points', 'production-tracking-zoho-creator', 'batch-traceability-food-manufacturer'],
    services=[SVC['mzoho'], SVC['creator'], SVC['integ']],
))

# ====================================================================== 2. Production tracking in Creator
S = 'production-tracking-zoho-creator'
cover(S, 'Build guide', 'Production tracking in Zoho Creator', 'Eight steps from a paper job card to live work-in-progress.',
      m_vt([('Steps 1-2', 'Model the job', 'Work orders, operations and stages'), ('Steps 3-5', 'Capture the work', 'Scan, quantities, scrap and holds'),
            ('Step 6', 'Connect it', 'Stock in, finished goods out'), ('Steps 7-8', 'See it and roll out', 'Dashboards, then one line first')]),
      theme='blue', alt='Cover: production tracking in Zoho Creator in eight steps grouped into four stages')
P1 = fig(S + '-model', m_cols([('Record', 'Work order', ['Product and quantity', 'Customer or stock', 'Due date', 'Current stage'], True), ('Record', 'Operations', ['One per routing stage', 'Planned time', 'Work centre']),
                                ('Record', 'Stage logs', ['Who and when', 'Good and scrap quantity', 'Time taken']), ('Record', 'Issues', ['Hold or rework', 'Reason', 'Who released it'])]),
         'Data model for production tracking: a work order has operations, each operation has stage logs, and issues record holds and rework',
         'The four records behind a production tracker. Everything on a dashboard is a count or a sum of stage logs.', h=480, title='Step 1: the data model')
P2 = fig(S + '-floor', phones([phone('My jobs', 'Assembly &middot; 4 waiting', pscan('Scan job card') + pf('WO-1042', 'Oak vanity 900 &middot; 12 units') + pf('WO-1047', 'Shelf unit S-8 &middot; 30 units') + pbtn('Start job', 'b')),
                                phone('WO-1042 &middot; Assembly', 'Started 09:14', pf('Good quantity', '8') + pf('Scrap quantity', '1') + pf('Scrap reason', 'Panel chipped') + pbtn('Complete stage'))],
                               [('Two taps to start', 'Scan the card, press start'), ('Scrap has a field', 'With a reason list, not free text'), ('Large buttons', 'Used with gloves, at arm&rsquo;s length')]),
         'Two concept phone screens for the shop floor: a job list with a scan button, and a stage completion form with good and scrap quantities',
         'A concept for the operator screens. If recording a stage takes more than a few seconds, people stop doing it.', h=560, ui=True)
P3 = fig(S + '-exceptions', m_steps([('On hold', 'Operator flags a problem and picks a reason', 'Job stops'), ('Review', 'Supervisor sees it on the board', 'Decide'),
                                      ('Rework or scrap', 'A rework stage is added, or quantity is written off', 'Recorded'), ('Release', 'Supervisor releases the job', 'Job resumes')],
                                     ['#E09E0F', '#226DB4', '#D9363A', '#089949']),
         'Four-step exception flow: a job is put on hold with a reason, reviewed, reworked or scrapped, then released',
         'Exceptions need their own path. Without one, held jobs look the same as slow jobs.', h=440, title='Step 5: holds and rework')
P4 = fig(S + '-lanes', m_lanes(['Order', 'Materials', 'Make', 'Finish'], [
            ('Sales', [('Order confirmed', 'CRM or order system'), None, None, ('Customer updated', 'Automatic email')]),
            ('Production app', [('Work order created', 'From the order line', 'hi'), ('Materials issued', 'Scan to job'), ('Stages logged', 'Good, scrap, time'), ('Job completed', 'All stages done', 'hi')]),
            ('Stock', [None, ('Components reduced', 'Stock system'), None, ('Finished goods added', 'Stock system')])]),
         'Swimlane showing how a production app connects sales and stock: orders create work orders, issues reduce component stock, completion adds finished goods',
         'The production app sits between sales and stock. It should never keep its own copy of stock levels.', h=500, title='Step 6: where it connects')
P5 = fig(S + '-board', app('Production Tracker', 'Concept on Zoho Creator', ['Board', 'Work orders', 'Stage logs', 'Holds', 'Reports'], 'Board', 'Work in progress', 'Thursday &middot; 14 jobs open',
         kanban([('Cutting', [('WO-1049 Kitchen K-22', 'Due 15 Oct &middot; 1 set', ('b', 'Running')), ('WO-1051 Wardrobe W-4', 'Due 17 Oct &middot; 3 units', ('n', 'Waiting'))]),
                 ('Edging', [('WO-1046 Door fronts D-3', 'Due 16 Oct &middot; 48 pcs', ('b', 'Running'))]),
                 ('Assembly', [('WO-1042 Oak vanity 900', 'Due 14 Oct &middot; 8 of 12', ('b', 'Running')), ('WO-1044 Shelf unit S-8', 'Due 09 Oct &middot; 30 units', ('r', 'Late'))]),
                 ('Finishing', [('WO-1038 Reception desk', 'Hold: colour query', ('y', 'On hold'))]),
                 ('Dispatch', [('WO-1036 Vanity 600', 'Packed &middot; 20 units', ('g', 'Ready'))])]),
         actions='<span class="pilln">Late: 1</span><span class="pilln">On hold: 1</span>'),
         'Concept work-in-progress board with jobs in columns for cutting, edging, assembly, finishing and dispatch, showing running, late and on-hold jobs',
         'A concept board built from stage logs. Late and held jobs are the two things a supervisor needs to see first.', h=620, ui=True)

GUIDES.append(dict(
    slug=S, title='How to Build Production Tracking in Zoho Creator',
    seo_title='Production Tracking in Zoho Creator: Build Guide',
    desc='A step-by-step build guide for production tracking in Zoho Creator: data model, shop-floor screens, scrap and holds, stock links and dashboards.',
    lead='A whiteboard and a stack of job cards work until the day someone asks where order 1042 is. Here is how we build a production tracker in Zoho Creator, in the order we build it.',
    category='Production', kind='steps', kind_label='Step-by-step build', tone='', layout='wide', author='arun', published=TODAY, keyword='production tracking Zoho Creator',
    facts=[('You need', 'A defined routing for your main products'), ('First version', 'One line, four to six weeks'), ('Built on', 'Zoho Creator, with a link to your stock system'), ('Not included', 'Capacity planning or MRP')],
    hero_alt='Cover: production tracking in Zoho Creator, eight steps in four stages', hero_cap='The eight steps, in build order.',
    answer='Model four records (work orders, operations, stage logs and issues), give operators a scan-and-tap screen for each stage, record good quantity, scrap and time, give holds their own path, and link issues and completions to your stock system. Build dashboards last, from the stage logs, and roll out on one line first.',
    body='''
<p>Zoho Creator has no production module. That is the point of it: you model your own process. It also means the result is only as good as the design. This is the sequence we follow, with the decisions that matter at each step.</p>
<p>Zoho ERP, which does have manufacturing orders and job cards, is currently published for India only. For manufacturers elsewhere, and for processes that do not fit a standard model, Creator is the practical route. Our article on <a href="/insights/zoho-for-manufacturing/">the three Zoho routes for manufacturers</a> compares them.</p>

<h2 id="step-1" class="mfg-step">Decide what a job is</h2>
<p>Start with the data model, on paper. Four records are enough for a first version.</p>
''' + P1 + '''
<ul>
  <li><strong>Work order:</strong> one product, one quantity, one due date. If a sales order has three lines, that is three work orders.</li>
  <li><strong>Operations:</strong> the stages this work order must pass through, copied from the product&rsquo;s routing when the order is created.</li>
  <li><strong>Stage logs:</strong> each time someone starts or finishes a stage. This is the only record operators create.</li>
  <li><strong>Issues:</strong> holds and rework, with a reason and a person who released it.</li>
</ul>
<p>Resist adding fields. Every field an operator must fill in is a reason not to use the screen.</p>

<h2 id="step-2" class="mfg-step">Model the routing</h2>
<p>A routing is the ordered list of stages for a product family: cutting, edging, assembly, finishing, dispatch. Store it once per family, not per product, and copy it to the work order when the order is created. That way a routing change affects new jobs only and old jobs keep their history.</p>
<p>Keep stages coarse. If two activities are always done by the same person at the same bench with no wait between them, they are one stage. You can split it later if you need the detail.</p>

<h2 id="step-3" class="mfg-step">Build the shop-floor screen first</h2>
<p>Most projects design the manager&rsquo;s dashboard first. Build the operator screen first, because it produces all the data.</p>
''' + P2 + '''
<p>Creator apps run as native iOS and Android apps, and form fields can scan QR codes and barcodes on a phone or tablet. Print a QR code on each job card that holds the work order number. The operator scans it, sees the current stage and presses start or complete. Design rules we hold to:</p>
<ul>
  <li>One screen per action. No menus on the shop floor.</li>
  <li>Buttons large enough to use with gloves.</li>
  <li>Pick lists, never free text, for scrap and hold reasons.</li>
  <li>A fixed tablet at each work centre works better than personal phones in most factories.</li>
</ul>
<p>Connectivity matters. Creator supports offline access in its mobile apps with some restrictions, so test your own forms in the dead spots of your building before you commit to a design.</p>

<h2 id="step-4" class="mfg-step">Capture quantity, scrap and time</h2>
<p>On completion, ask for three things: good quantity, scrap quantity and, if scrap is more than zero, a reason. Time comes from the start and complete timestamps, so nobody types it.</p>
<p>Partial completion is where simple trackers break. If a job of 12 units finishes 8 today, the stage is not complete. Log the 8 and keep the stage open. A short Deluge script on the stage log form can do the arithmetic. The sketch below shows the idea; field names will differ in your app.</p>
<pre><code>// Runs after a stage log is submitted (sketch)
wo = Work_Order[ID == input.Work_Order];
done = Stage_Log[Work_Order == input.Work_Order &amp;&amp; Stage == input.Stage].sum(Good_Qty);
if(done &gt;= wo.Planned_Qty)
{
    wo.Current_Stage = input.Next_Stage;
}</code></pre>
<p>More patterns like this are in our <a href="/insights/deluge-script-examples/">Deluge script examples</a>.</p>

<h2 id="step-5" class="mfg-step">Give exceptions their own path</h2>
<p>A job waiting for a decision is different from a job that is slow. If the system cannot tell them apart, supervisors will stop trusting the board.</p>
''' + P3 + '''
<p>Creator&rsquo;s approvals and Blueprint features suit this well: a hold needs a reason, only a supervisor can release it, and a rework decision adds a stage to that work order. Record who released it and when. That history is what you need later for <a href="''' + G + '''quality-ncr-capa-workflow/">quality reporting</a>.</p>

<h2 id="step-6" class="mfg-step">Connect it to orders and stock</h2>
<p>A tracker that is not connected becomes one more place to enter data. Three links matter.</p>
''' + P4 + '''
<ul>
  <li><strong>Orders in:</strong> a confirmed order line creates the work order. No retyping.</li>
  <li><strong>Materials out:</strong> issuing components to a job reduces stock in the stock system.</li>
  <li><strong>Finished goods in:</strong> completing the last stage adds finished stock and tells sales.</li>
</ul>
<p>The production app should never hold its own stock balance. It records movements and sends them to the system that owns stock, whether that is Zoho Inventory, an ERP or an accounting package. Our <a href="/zoho-integrations/">integration work</a> is mostly this.</p>
''' + callout('Know the limits', 'Zoho Inventory can build a finished item from components with an assembly, and that is useful for simple products. It has no work orders that move through stages. The Creator app carries the stages; the stock system carries the quantities.', True) + '''

<h2 id="step-7" class="mfg-step">Build the dashboards last</h2>
<p>By now every dashboard is a query over stage logs. Start with three views and add more only when someone asks a question the three cannot answer.</p>
''' + P5 + '''
<ul>
  <li><strong>The board:</strong> every open job, by stage, with late and held jobs marked.</li>
  <li><strong>The due list:</strong> jobs due in the next five days and the stage each is at.</li>
  <li><strong>The scrap report:</strong> scrap quantity by reason and by stage, per week.</li>
</ul>
<p>Deeper analysis, such as output per work centre over time, belongs in a reporting tool. See <a href="''' + G + '''manufacturing-dashboards-kpis/">which manufacturing KPIs are worth tracking</a>.</p>

<h2 id="step-8" class="mfg-step">Roll out on one line</h2>
<p>Choose the line with the most cooperative supervisor, not the most important one. Run paper and system side by side for one week, then remove the paper. Expect to change the operator screen several times in the first fortnight. That is the design working, not failing.</p>

<h2 id="worked-example">A worked example: one job, start to finish</h2>
<p>To make the steps concrete, follow one job through the finished app. The business is an example: a furniture workshop with four stages, cutting, edging, assembly and finishing.</p>
<ol>
  <li><strong>Monday, 08:10.</strong> A sales order for 12 oak vanity units is confirmed. The app creates work order WO-1042 with four operations and prints a job card with a QR code.</li>
  <li><strong>Monday, 09:30.</strong> The cutting operator scans the card and taps Start. The board shows WO-1042 in Cutting. Nobody has been asked for an update.</li>
  <li><strong>Monday, 14:05.</strong> Cutting is finished: 12 good, none scrapped. The job moves to the edging queue and the edging operator sees it on her phone.</li>
  <li><strong>Tuesday, 10:40.</strong> During assembly, one carcass is damaged. The operator records 11 good and 1 scrap, with the reason &ldquo;handling damage&rdquo;. The work order now shows a shortfall of one.</li>
  <li><strong>Tuesday, 10:41.</strong> The shortfall rule puts the job on hold for the supervisor, who chooses to remake one unit. A linked work order for one unit is raised.</li>
  <li><strong>Thursday.</strong> Both orders finish. Finished stock rises by 12 and the sales order is marked ready to ship.</li>
</ol>
<p>Nothing in that sequence is clever. What matters is that every event was recorded by the person who caused it, at the time, in about ten seconds. The planner&rsquo;s morning walk around the floor to ask &ldquo;where is it?&rdquo; is no longer needed, and the scrap has a reason attached that can be counted at the end of the month.</p>

<h2 id="limits">What this will not do</h2>
<p>Be clear with yourself about scope. A tracker like this tells you where every job is and what it consumed. It does not:</p>
<ul>
  <li>plan capacity or schedule work centres automatically;</li>
  <li>calculate material requirements from a forecast;</li>
  <li>replace a costing system, though it gives one much better data.</li>
</ul>
<p>If you need those, you are looking at a manufacturing ERP, and our comparison of <a href="''' + G + '''zoho-or-manufacturing-erp/">Zoho apps against a manufacturing ERP</a> will help you decide.</p>
''',
    faqs=[('How long does it take to build production tracking in Zoho Creator?',
           'A first version for one line, with work orders, stage logging, holds and a board, typically takes four to six weeks including a trial week on the floor. Integrations with stock and orders add time depending on the systems involved.'),
          ('Can operators use it without an internet connection?',
           'Zoho Creator mobile apps support offline access with some restrictions. Whether it suits you depends on which forms and scripts you need offline, so test with your own design before relying on it.'),
          ('Do we need Zoho Inventory as well?',
           'Not necessarily. The tracker needs a system that owns stock quantities. That can be Zoho Inventory, an ERP or an accounting package with stock. The tracker sends it issues and completions.'),
          ('Will this replace our ERP?',
           'No. It complements one. Zoho itself positions Creator as an extension layer beside a core system. It tracks work on the floor in a way most ERPs do not make easy.')],
    sources=[SRC['creator_features'], SRC['creator_scan'], SRC['creator_offline'], SRC['creator_mfg'], SRC['inv_mfg'], SRC['erp_mo']],
    related=['job-tracking-joinery-manufacturer', 'zoho-or-manufacturing-erp', 'manufacturing-dashboards-kpis'],
    services=[SVC['creator'], SVC['deluge'], SVC['mzoho']],
    cta_title='Want a production tracker built around your routing?', cta_text='Send us one job card and a description of your stages. We will sketch the data model and the operator screen before you commit to anything.',
))

# ====================================================================== 3. 90-day roadmap
S = 'spreadsheets-to-connected-system-roadmap'
cover(S, 'Roadmap', 'From spreadsheets to one connected system', 'A 90-day plan for a small manufacturer, one process at a time.',
      m_rows([('Days 1 to 15', 'Map the process and choose one'), ('Days 16 to 45', 'Build and trial the first workflow'), ('Days 46 to 75', 'Connect stock and accounts'), ('Days 76 to 90', 'Dashboards, handover, next choice')]),
      theme='green', solid=True, alt='Cover: a 90-day roadmap from spreadsheets to a connected system in four phases')
R1 = fig(S + '-timeline', m_timeline([('Days 1-15', 'Map', 'Walk the process, list the spreadsheets'), ('Days 16-45', 'Build', 'One workflow, trialled on the floor'),
                                       ('Days 46-75', 'Connect', 'Stock and accounts linked'), ('Days 76-90', 'Report', 'Dashboards and handover'), ('Day 91', 'Repeat', 'Choose the next process')]),
         'Timeline of the 90-day roadmap: map, build, connect, report, then repeat with the next process',
         'Four phases, then repeat. Each cycle leaves one more process off spreadsheets.', h=380, theme='green')
R2 = fig(S + '-matrix', m_matrix([('High pain, easy to fix', 'Start here', 'Job tracking, purchase approvals, quality checks'), ('High pain, hard to fix', 'Plan for it', 'Scheduling, costing, full stock control'),
                                   ('Low pain, easy to fix', 'Later, if cheap', 'Leave requests, visitor log'), ('Low pain, hard to fix', 'Leave it', 'Anything that works on paper today')]),
         'Two-by-two matrix for choosing a first process by pain and difficulty, with examples in each quadrant',
         'Choose the first process by pain and difficulty. The top-left quadrant earns trust for the harder ones.', h=520, theme='green', title='Which process first?')
R3 = fig(S + '-before-after', m_ba(dict(k='Day 0', h='Five disconnected files', li=['Orders in a sales spreadsheet', 'Job status on a whiteboard', 'Stock in another spreadsheet', 'Invoices typed again in accounts']),
                                    dict(k='Day 90', h='One connected flow', li=['Order creates the job', 'Stage scans update status', 'Issues and completions move stock', 'Dispatch raises the invoice'])),
         'Before and after comparison: five disconnected files on day 0, one connected flow from order to invoice on day 90',
         'The aim of the first 90 days is one connected flow, not a complete system.', h=480, theme='green')
R4 = fig(S + '-readiness', m_check(['One named owner on the floor', 'A process people already follow', 'Clean product and customer lists', 'A system that owns stock', 'Time for a one-week trial', 'Agreement to remove the old sheet']),
         'Readiness checklist of six items to confirm before starting, including a named owner and clean product lists',
         'Six things to confirm before you start. The last one is the one people skip.', h=420, theme='green', title='Ready to start?')
R5 = fig(S + '-tracker', app('Rollout Plan', 'Concept project tracker', ['Roadmap', 'Processes', 'Risks', 'Decisions'], 'Roadmap', 'Digital rollout', 'Day 38 of 90',
         kpis([('Processes mapped', '6', 'of 6', 'up'), ('Live', '1', 'job tracking', 'up'), ('In trial', '1', 'purchase approvals', 'fl'), ('Spreadsheets retired', '2', 'of 7', 'fl')])
         + panel('Process queue', table('minmax(0,1.5fr) 110px 110px 110px minmax(0,1fr)', ['Process', 'Pain', 'Effort', 'Status', 'Owner'],
                 [['Job tracking', ('st', 'r', 'High'), ('st', 'g', 'Low'), ('st', 'g', 'Live'), 'Production lead'],
                  ['Purchase approvals', ('st', 'r', 'High'), ('st', 'g', 'Low'), ('st', 'b', 'In trial'), 'Purchasing'],
                  ['Incoming quality checks', ('st', 'y', 'Medium'), ('st', 'g', 'Low'), ('st', 'n', 'Next'), 'Quality'],
                  ['Stock control', ('st', 'r', 'High'), ('st', 'r', 'High'), ('st', 'n', 'Planned'), 'Stores'],
                  ['Scheduling', ('st', 'y', 'Medium'), ('st', 'r', 'High'), ('st', 'n', 'Not yet'), 'Planner']]), 'ranked by pain and effort', 'flex:1')),
         'Concept rollout tracker listing six processes with pain, effort, status and owner, showing one live and one in trial',
         'A concept tracker for the rollout itself. A ranked queue stops the project turning into everything at once.', h=600, ui=True)

GUIDES.append(dict(
    slug=S, title='From Spreadsheets to a Connected System: A 90-Day Roadmap for Small Manufacturers',
    seo_title='From Spreadsheets to One System: A 90-Day Roadmap',
    desc='A practical 90-day plan to move a small manufacturer off spreadsheets: how to choose the first process, build it, connect stock and accounts, and repeat.',
    lead='Most failed software projects in small factories tried to replace everything at once. The ones that work replace one spreadsheet, prove it, and move to the next.',
    category='Digital transformation', kind='roadmap', kind_label='Roadmap and checklist', tone='green', layout='toc-right', author='team', published=TODAY, keyword='manufacturing digital transformation roadmap',
    facts=[('Scope', 'One process end to end'), ('Team', 'One owner, one builder'), ('Outcome', 'Two or three spreadsheets retired'), ('Then', 'Repeat with the next process')],
    hero_alt='Cover: 90-day roadmap in four phases', hero_cap='The four phases of the first 90 days.',
    answer='Map your processes in two weeks and choose one that hurts and is easy to fix. Build and trial that one workflow in a month, connect it to stock and accounts in the next month, then add dashboards and hand over. Retire the old spreadsheet on a named date, and repeat with the next process.',
    body='''
<p>Spreadsheets are not the problem. They are the reason a small factory can run at all. The problem starts when the same information lives in five of them and nobody knows which is current.</p>
<p>This roadmap is for a manufacturer with roughly 10 to 150 people who wants to stop that without betting the business on one large system. It assumes no particular software, although the examples use Zoho apps because that is what we build on.</p>

<h2 id="why-90-days">Why 90 days, and why one process</h2>
<p>Ninety days is long enough to finish something real and short enough that people still remember why it started. One process is small enough to get right. Finishing matters more than scope: a team that has seen one process work will ask for the next one, and a team that has watched a big project stall will resist all of them.</p>
''' + R1 + '''

<h2 id="phase-1">Days 1 to 15: map, then choose</h2>
<p>Walk each process with the person who does it, and write down what actually happens, including the workarounds. For each one, note:</p>
<ul>
  <li>which spreadsheets, whiteboards and paper forms it touches;</li>
  <li>where the same data is typed more than once;</li>
  <li>where people wait for information or go and look for it;</li>
  <li>what goes wrong, and how often.</li>
</ul>
<p>Then rank the processes on two questions: how much does it hurt, and how hard is it to fix?</p>
''' + R2 + '''
<p>Start in the top-left quadrant. Job tracking, purchase approvals and incoming quality checks are common first choices because they are contained: few people, few integrations, visible result. Full stock control and scheduling hurt more but depend on data you may not have yet. Our guide to <a href="''' + G + '''inventory-accuracy-for-manufacturers/">inventory accuracy</a> explains why.</p>
''' + R4 + '''

<h2 id="phase-2">Days 16 to 45: build one workflow and trial it</h2>
<p>Build the smallest version that could replace the spreadsheet. For job tracking, that is work orders, stages and one operator screen. Our <a href="''' + G + '''production-tracking-zoho-creator/">production tracking build guide</a> lists the steps.</p>
<ol>
  <li><strong>Week 3:</strong> agree the data model and the two or three screens. Sketch them on paper with the people who will use them.</li>
  <li><strong>Weeks 4 and 5:</strong> build. Review a working screen twice a week, on the floor, not in a meeting room.</li>
  <li><strong>Week 6:</strong> run it beside the old method on one line. Fix what the trial shows.</li>
</ol>
''' + callout('The date that matters', 'Agree at the start the date on which the old spreadsheet becomes read-only. Without that date, both methods run in parallel for months and the new one is blamed for the extra work.') + '''

<h2 id="phase-3">Days 46 to 75: connect stock and accounts</h2>
<p>A workflow that stands alone still needs retyping at its edges. This phase removes the retyping.</p>
''' + R3 + '''
<p>Typical connections for a first process:</p>
<ul>
  <li><strong>Orders in.</strong> A confirmed order creates the job.</li>
  <li><strong>Stock out and in.</strong> Issues reduce components; completions add finished goods.</li>
  <li><strong>Invoice out.</strong> Dispatch raises the invoice in your accounting system.</li>
</ul>
<p>Keep each system as the owner of one thing: the accounting package owns invoices, the stock system owns quantities, the new app owns the work. Our guide to <a href="''' + G + '''connect-sales-production-accounts/">integration patterns</a> covers how to keep them in step.</p>

<h2 id="phase-4">Days 76 to 90: report, hand over, choose again</h2>
<p>Only now build dashboards. With a month of real data you know which questions people actually ask. Three or four measures are enough to begin with; see <a href="''' + G + '''manufacturing-dashboards-kpis/">which KPIs are worth tracking</a>.</p>
<p>Handover means three things in writing: what the system does, who can change it, and what to do when it is wrong. Then go back to the ranked list and choose the next process.</p>
''' + R5 + '''

<h2 id="worked-example">A worked example: what the 90 days look like</h2>
<p>Here is the plan applied to an example business: a 30-person sheet-metal fabricator that quotes in one spreadsheet, schedules on a whiteboard and invoices from an accounting package.</p>
<ul>
  <li><strong>Days 1 to 15.</strong> The walk-through finds seven spreadsheets and one whiteboard. Scoring them shows that job status causes the most daily pain: the office phones the floor about a dozen times a day. Purchasing is painful too, but depends on stock figures nobody trusts. Job tracking is chosen.</li>
  <li><strong>Days 16 to 45.</strong> A work-order app is built with five stages. The laser cell trials it for a week with printed job cards and one shared tablet. Two changes come out of the trial: operators want to see the next three jobs, not just the current one, and &ldquo;waiting for material&rdquo; needs to be a hold reason.</li>
  <li><strong>Days 46 to 75.</strong> Confirmed quotes now create work orders, so nothing is typed twice. Completing a job creates a draft invoice in the accounting package. Stock is deliberately left alone, apart from a list of materials issued per job.</li>
  <li><strong>Days 76 to 90.</strong> A weekly report shows jobs finished on time and hours on hold by reason. The whiteboard is taken down. The team scores the remaining processes again and picks purchasing, now that material issues are being recorded.</li>
</ul>
<p>Notice what was not done. Nobody replaced the accounting package, nobody built a scheduling engine and nobody loaded a full stock file. Each of those may come later, with evidence from the first project to justify it.</p>
<h3>How to tell whether it worked</h3>
<p>Agree two or three plain measures before you start and take a baseline in the first fortnight. Good candidates are the number of status calls from the office to the floor, the time between finishing a job and invoicing it, and the number of jobs whose stage is unknown at 9 a.m. They are easy to count by hand, and they show whether people are using the system or working around it.</p>

<h2 id="who-you-need">Who you need</h2>
<ul>
  <li><strong>An owner from the floor.</strong> Someone the operators respect, with a few hours a week. This is the role projects most often lack.</li>
  <li><strong>A builder.</strong> In-house or outside. One person who can change a screen the same day a problem is found.</li>
  <li><strong>A decision-maker.</strong> Someone who can say &ldquo;we stop using the old sheet on the 1st&rdquo;.</li>
</ul>

<h2 id="mistakes">How these projects go wrong</h2>
<ul>
  <li><strong>Starting with the hardest process.</strong> Scheduling is tempting and depends on everything else being right.</li>
  <li><strong>Copying the spreadsheet.</strong> A system with 40 columns is still a spreadsheet. Model the process, not the file.</li>
  <li><strong>Designing in a meeting room.</strong> Screens designed away from the floor fail on the floor.</li>
  <li><strong>No retirement date.</strong> Parallel running that never ends.</li>
  <li><strong>Buying software before mapping.</strong> You end up changing the process to fit the tool.</li>
</ul>

<h2 id="next-steps">What to do this week</h2>
<p>List every spreadsheet that more than one person edits. That list is your map. Mark the one that causes the most arguments, and walk its process with the person who owns it. If you want a second opinion on where to start, our <a href="''' + M + '''workflows/">workflow overview</a> shows the processes we are asked to fix most often.</p>
''',
    faqs=[('Can a small manufacturer really move off spreadsheets in 90 days?',
           'Not entirely, and that is not the aim. In 90 days you can move one complete process off spreadsheets and connect it to stock and accounts. Repeating the cycle moves the rest.'),
          ('Should we buy an ERP instead?',
           'If you need planning, costing and finance in one system and your process fits a standard model, an ERP can be the right answer. If your main problem is a few disconnected processes, fixing those first is faster, cheaper and makes any later ERP decision better informed.'),
          ('Who should own the project?',
           'Someone from operations, not IT or accounts. The owner needs the respect of the people on the floor and the authority to retire the old method.'),
          ('What does a first process usually cost?',
           'It depends on scope and integrations. We price from an estimate of hours, and our pricing page explains the rates and includes a calculator.')],
    sources=[SRC['creator_features'], SRC['inv_features']],
    related=['production-tracking-zoho-creator', 'connect-sales-production-accounts', 'job-tracking-joinery-manufacturer'],
    services=[SVC['mwf'], SVC['bpa'], SVC['pricing']],
))
