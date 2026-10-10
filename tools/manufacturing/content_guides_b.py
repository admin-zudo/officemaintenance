"""Manufacturing guides, part B."""
from content_common import *

GUIDES = []

# ====================================================================== 4. Zoho apps or a manufacturing ERP
S = 'zoho-or-manufacturing-erp'
cover(S, 'Comparison', 'Zoho apps or a manufacturing ERP?', 'Two sound routes. The right one depends on how much planning you need.',
      m_rows([('Zoho apps and a custom app', 'Fits your process, built in steps'), ('A manufacturing ERP', 'Planning and costing in one system'), ('ERP plus an extension', 'A core system with custom apps beside it')]),
      theme='blue', alt='Cover: three routes for a small manufacturer: Zoho apps with a custom app, a manufacturing ERP, or an ERP with an extension layer')
E1 = fig(S + '-split', m_split(dict(k='Modular', h='Zoho apps and a custom app', s='Stock, sales and accounts apps, with production built on Creator', li=['Shaped around your process', 'Built and paid for in steps', 'No planning engine included', 'You own the design decisions']),
                                dict(k='All in one', h='A manufacturing ERP', s='One system with BOMs, orders, planning and costing', li=['Planning and costing included', 'A standard process to adopt', 'A bigger first project', 'Less freedom to differ']), '#1B5A96', '#7A4700'),
         'Side-by-side comparison of Zoho apps with a custom app against a manufacturing ERP, four points each',
         'The trade is flexibility against built-in planning. Neither route is the cheap one or the serious one.', h=520)
E2 = fig(S + '-table', m_table(['Question', 'Points to Zoho apps', 'Points to an ERP'],
                                [['How do you plan materials?', 'Per job, or simple reorder points', 'From a forecast, across many levels'], ['How deep are your BOMs?', 'One or two levels', 'Several levels with shared sub-assemblies'],
                                 ['How unusual is your process?', 'It is your advantage', 'It is close to standard'], ['Who will run the system?', 'An operations lead', 'Someone with ERP experience'],
                                 ['How do you want to pay?', 'In steps, as each part proves itself', 'One project, one go-live']], '1fr 1.15fr 1.15fr'),
         'Decision table of five questions with the answers that point to Zoho apps or to a manufacturing ERP',
         'Five questions that decide most cases. Answer them for the business you will be in two years from now.', h=520, title='Five questions that decide it')
E3 = fig(S + '-matrix', m_matrix([('Simple planning, unusual process', 'Zoho apps and a custom app', 'Make-to-order, project and job-shop work'), ('Complex planning, unusual process', 'ERP plus a custom extension', 'Keep the planning engine, build what is different'),
                                   ('Simple planning, standard process', 'Either works', 'Choose on cost and the team you have'), ('Complex planning, standard process', 'A manufacturing ERP', 'Repetitive production with deep BOMs')]),
         'Two-by-two matrix of planning complexity against process uniqueness, with a recommended route in each quadrant',
         'Plot yourself on two axes: how complex your planning is and how unusual your process is.', h=520, title='Where you sit')
E4 = fig(S + '-hybrid', m_arch([('People', 'who works where', ['Sales', 'Planner', 'Operators', 'Quality', 'Accounts']),
                                 ('Extension apps', 'built on Zoho Creator', ['Shop-floor tracking', 'Quality and NCR', 'Maintenance', 'Supplier portal'], True),
                                 ('Core system', 'the record of stock, orders and money', ['Items and BOMs', 'Stock', 'Purchasing', 'Costing and finance']),
                                 ('Reporting', 'one view across both', ['Zoho Analytics dashboards', 'Scheduled reports', 'Alerts'])]),
         'Architecture of the hybrid route: people use extension apps built on Zoho Creator, which sit on a core system that owns stock, orders and money, with reporting across both',
         'The hybrid route. The core system stays the record; custom apps handle the work it does badly.', h=540, title='ERP plus an extension layer')
E5 = fig(S + '-scenarios', m_rows([('A 25-person joinery', 'Every job is different; materials bought per job', 'Zoho apps and a custom job tracker'), ('A 60-person food producer', 'Recipes, batches and expiry dates; steady demand', 'An ERP or MRP system with batch control'),
                                    ('A 120-person engineering firm', 'ERP in place; shop floor still on paper', 'Keep the ERP, add extension apps')]),
         'Three example businesses and the route that suits each: a joinery, a food producer and an engineering firm',
         'Three examples. They are illustrations of the reasoning, not client projects.', h=520, title='Three example businesses')

GUIDES.append(dict(
    slug=S, title='Zoho Apps or a Manufacturing ERP? How to Choose',
    seo_title='Zoho Apps or a Manufacturing ERP? How to Choose',
    desc='How a small manufacturer should choose between Zoho apps with a custom production app and a manufacturing ERP: five questions, a matrix and three examples.',
    lead='We build on Zoho, so you would expect us to say Zoho. For some manufacturers a purpose-built ERP is the better answer, and it is cheaper to find that out before you start.',
    category='Software choice', kind='compare', kind_label='Comparison', tone='', layout='toc-left', author='arun', published=TODAY, keyword='Zoho vs manufacturing ERP',
    facts=[('Choose Zoho apps when', 'Your process is unusual and planning is simple'), ('Choose an ERP when', 'You plan materials from forecasts across deep BOMs'), ('Often right', 'An ERP core with custom apps beside it')],
    hero_alt='Cover: Zoho apps or a manufacturing ERP, three routes', hero_cap='Three routes, and most manufacturers fit one of them clearly.',
    answer='Choose Zoho apps with a custom production app when your process is unusual, your bills of materials are shallow and you buy materials per job or by reorder point. Choose a manufacturing ERP when you need material requirements planning across multi-level BOMs, capacity scheduling and standard costing. If you already run an ERP, keep it and add custom apps for what it handles badly.',
    body='''
<p>The question usually arrives as &ldquo;can Zoho run our factory?&rdquo; The honest answer has three parts, because &ldquo;Zoho&rdquo; is several products and &ldquo;run our factory&rdquo; means different things in a joinery and in a bottling plant.</p>
<p>This guide compares two approaches, not two brands. Our article on <a href="/insights/zoho-for-manufacturing/">what Zoho itself offers manufacturers</a> covers the products in detail.</p>

<div class="mfg-verdict">
  <div><h3>Zoho apps and a custom app</h3><p>Standard apps for stock, sales and accounts, with production tracking built on Zoho Creator around your own routing. Best when the process is what makes you different.</p></div>
  <div><h3>A manufacturing ERP</h3><p>One system with bills of materials, manufacturing orders, material planning and costing. Best when planning is the hard part and your process is close to standard.</p></div>
</div>

<h2 id="two-approaches">The two approaches</h2>
''' + E1 + '''
<h3>Zoho apps with a custom production app</h3>
<p>Stock sits in Zoho Inventory, or in the stock module of your accounting package. Sales sit in Zoho CRM. Accounts sit in Zoho Books or the package you already use. Production, the part none of those cover, is built as an app on Zoho Creator: work orders, stages, scrap, holds, whatever your process needs.</p>
<p>The gap to be clear about: Zoho Inventory has no manufacturing module. Zoho&rsquo;s knowledge base says so and suggests composite items for basic assemblies. Nothing in this route calculates what to buy and when from a forecast. You plan per job, or with reorder points.</p>
<h3>A manufacturing ERP</h3>
<p>Here one product holds items, multi-level bills of materials, routings, work orders, stock, purchasing and usually finance. Its planning engine can explode a sales forecast into purchase and production suggestions. There are many such systems for small manufacturers, from cloud MRP products to open-source ERPs.</p>
<p>Zoho has one too. Zoho ERP has manufacturing orders, job cards, work centres and quality inspections, but at the time of writing it is published for India only and is licensed separately from Zoho One.</p>

<h2 id="five-questions">Five questions that decide it</h2>
''' + E2 + '''
<h3>How do you plan materials?</h3>
<p>If you buy for each job once it is confirmed, or top up common materials when they fall below a level, you do not need a planning engine. If you must work out today what to order for products you will make in six weeks, across components shared by many products, you do. That calculation is the heart of an ERP and is expensive to build yourself.</p>
<h3>How deep are your bills of materials?</h3>
<p>A cabinet is panels, hardware and finish: one level. A machine with sub-assemblies that are made in-house, stocked and used in several products is three or four levels. Depth multiplies the planning work.</p>
<h3>How unusual is your process?</h3>
<p>An ERP gives you its process. That is a benefit if yours is ordinary and a cost if yours is what customers pay for. Custom steps, such as site measures, design approvals or customer-specific tests, fit poorly into standard screens.</p>
<h3>Who will run it?</h3>
<p>An ERP needs an owner who understands items, BOMs, costing methods and period ends. A modular set-up asks less at the start and grows with the team.</p>
<h3>How do you want to pay?</h3>
<p>A modular route can be bought one process at a time, each paying for the next. An ERP is mostly one project with one go-live. Our <a href="''' + G + '''spreadsheets-to-connected-system-roadmap/">90-day roadmap</a> describes the stepwise version.</p>

<h2 id="where-you-sit">Where you sit</h2>
<p>Two of those questions matter more than the rest: how complex your planning is, and how unusual your process is.</p>
''' + E3 + '''
<p>The top-right quadrant is the one people miss. A business with complex planning <em>and</em> an unusual process should not choose between the two approaches. It should run both.</p>

<h2 id="hybrid">The third route: an ERP with an extension layer</h2>
''' + E4 + '''
<p>Zoho describes Creator in exactly these terms for manufacturing: an extension layer beside a core system, with that system remaining the source of records. In practice the ERP keeps items, stock, purchasing and finance. Custom apps handle shop-floor data capture, quality records, maintenance requests and supplier portals, and pass results back through the ERP&rsquo;s API.</p>
<p>This is often the right answer for a manufacturer who already has an ERP and is unhappy with it. The complaint is rarely the planning engine. It is that operators will not use the screens.</p>

<h2 id="examples">Three examples</h2>
''' + E5 + '''
<ul>
  <li><strong>The joinery</strong> quotes each job, buys board and hardware against it and moves it through cutting, edging, assembly and fitting. Planning is simple; the process is specific. A job tracker on Creator, with stock and accounts in standard apps, fits. We describe one in our <a href="''' + CS + '''job-tracking-joinery-manufacturer/">joinery reference implementation</a>.</li>
  <li><strong>The food producer</strong> makes the same products every week from recipes, with lot numbers and expiry dates on everything. Requirements planning and batch control are core. That points to an ERP or MRP system. A custom app may still help with <a href="''' + G + '''batch-lot-traceability/">traceability records</a> on the floor.</li>
  <li><strong>The engineering firm</strong> already owns an ERP. Replacing it would be slow and risky. Adding shop-floor and quality apps beside it gets the result faster.</li>
</ul>

<h2 id="signs">Signs you have outgrown the modular route</h2>
<p>A modular set-up can be right for years and then stop being right. Watch for these:</p>
<ul>
  <li><strong>The buyer keeps a private spreadsheet</strong> to work out what to order for the next six weeks. That spreadsheet is a home-made planning engine.</li>
  <li><strong>Shared sub-assemblies run short</strong> because two products needed them in the same week and nothing added the demand together.</li>
  <li><strong>You cannot say what a product costs to make</strong> without a day of work, and margins are being questioned.</li>
  <li><strong>Custom logic keeps growing</strong> to imitate things an ERP does as standard.</li>
</ul>
<p>One of these is a nudge. Three together mean it is time to look at an ERP core, and to keep the custom apps as its extension layer.</p>

<h2 id="costs">What each route really costs</h2>
<p>Licence prices are the smallest part of either bill, and they change, so we do not quote them here. Compare these instead:</p>
<ul>
  <li><strong>Implementation effort.</strong> An ERP needs items, BOMs, routings, opening stock and opening balances loaded and checked before go-live. A modular build spreads that work.</li>
  <li><strong>Change afterwards.</strong> Custom apps are cheap to change. ERPs are cheap to keep standard and costly to bend.</li>
  <li><strong>The cost of the gap.</strong> If you choose modular and later need requirements planning, you will buy it then. If you choose an ERP and half of it goes unused, you paid for it anyway.</li>
</ul>
<p>For the custom side, our <a href="/pricing/">pricing page</a> explains how we estimate.</p>

<h2 id="mistakes">Mistakes to avoid</h2>
<ul>
  <li><strong>Choosing by demo.</strong> Demos show the standard process. Ask to see your awkward job in the system.</li>
  <li><strong>Rebuilding MRP by hand.</strong> If you need requirements planning, buy it. Do not ask a low-code app to imitate it.</li>
  <li><strong>Assuming an ERP fixes data.</strong> Wrong stock and wrong BOMs stay wrong in any system. Start with <a href="''' + G + '''inventory-accuracy-for-manufacturers/">inventory accuracy</a>.</li>
  <li><strong>Deciding for today&rsquo;s size.</strong> Answer the five questions for where you expect to be in two years.</li>
</ul>

<h2 id="next-steps">How to decide this month</h2>
<ol>
  <li>Write down how you plan materials today, in one paragraph.</li>
  <li>Pick your three most complex products and count the BOM levels.</li>
  <li>List the steps in your process that a standard system would not have.</li>
  <li>Place yourself on the matrix, then test the answer against one real job.</li>
</ol>
<p>If the answer is still unclear, send us the paragraph and the three products. We will tell you which route we would take, including when that is not us.</p>
''',
    faqs=[('Can Zoho replace a manufacturing ERP?',
           'For manufacturers with simple planning, Zoho apps with a custom production app on Zoho Creator can cover the work. They do not include a material requirements planning engine. Zoho ERP does have a manufacturing module, but at the time of writing it is published for India only.'),
          ('Is Zoho Inventory enough for a manufacturer?',
           'It manages stock, purchasing, batches and simple assemblies well. Zoho states that it does not have a manufacturing module, so work orders, routing and production tracking need a separate app or system.'),
          ('We already have an ERP. Should we replace it?',
           'Usually not. If the planning and finance side works, keep it and add custom apps for shop-floor capture, quality or maintenance. That delivers the improvement people want without the risk of a replacement.'),
          ('Which route is cheaper?',
           'It depends on what you need. A modular route starts smaller and spreads the cost. An ERP costs more to implement but includes planning and costing you would otherwise have to buy later. Compare total effort over three years, not licence prices.')],
    sources=[SRC['inv_mfg'], SRC['inv_composite'], SRC['erp'], SRC['erp_mo'], SRC['creator_mfg'], SRC['one_apps']],
    related=['production-tracking-zoho-creator', 'job-tracking-joinery-manufacturer', 'spreadsheets-to-connected-system-roadmap'],
    services=[SVC['mzoho'], SVC['creator'], SVC['custom']],
    cta_title='Not sure which route fits?', cta_text='Tell us how you plan materials and send three bills of materials. We will give you a straight answer, including when the answer is an ERP.',
))

# ====================================================================== 5. Batch and lot traceability
S = 'batch-lot-traceability'
cover(S, 'Traceability', 'Batch and lot traceability', 'What to record at each step so a recall takes hours, not days.',
      m_vt([('Receive', 'Supplier lot', 'Lot number, date, certificate'), ('Store', 'Location', 'Which lot is where'), ('Make', 'Batch record', 'Which lots went into which batch'), ('Ship', 'Dispatch record', 'Which batch went to which customer')]),
      theme='navy', alt='Cover: four points where traceability data is recorded: receive, store, make and ship')
T1 = fig(S + '-chain', m_cols([('Inputs', 'Supplier lots', ['Flour lot F-2207', 'Butter lot B-0913', 'Packaging lot P-551']), ('Production', 'Batch', ['Batch 24-1042', 'Line 2, 9 Oct', 'Operator and checks'], True),
                                ('Output', 'Finished lots', ['Pallet 1042-A', 'Pallet 1042-B']), ('Dispatch', 'Customers', ['Order 7781, 9 Oct', 'Order 7790, 10 Oct'])]),
         'Trace chain from supplier lots through a production batch to finished pallets and customer orders',
         'One batch and its links. Traceability is these links, recorded at the moment each one is made. Example data.', h=400, theme='navy', title='The chain you need to be able to follow')
T2 = fig(S + '-record', m_table(['Step', 'Record', 'Who records it', 'How'],
                                 [['Receiving', 'Supplier lot, quantity, date, certificate', 'Stores', 'Scan the delivery label'], ['Storage', 'Location of each lot', 'Stores', 'Scan bin, then lot'],
                                  ['Issue', 'Which lot went to which batch', 'Operator', 'Scan lot to batch'], ['Production', 'Batch number, line, time, checks', 'Operator', 'Batch record form'],
                                  ['Dispatch', 'Which finished lot to which order', 'Dispatch', 'Scan pallet to order']], '.7fr 1.5fr .8fr 1fr'),
         'Table of the five steps where traceability data is recorded, with the record, who records it and how',
         'Five recording points. If any one is missing, the chain breaks there.', h=500, theme='navy', title='What to record, and where')
T3 = fig(S + '-batch-screen', app('Batch Records', 'Concept on Zoho Creator', ['Batches', 'Lots in stock', 'Trace', 'Holds', 'Reports'], 'Batches', 'Batch 24-1042 &middot; Shortbread 200 g', 'Line 2 &middot; 9 Oct &middot; Released',
         fields([('Product', 'Shortbread 200 g'), ('Planned', '1,200 packs'), ('Produced', '1,176 packs'), ('Best before', '9 Apr 2027'), ('Line', 'Line 2'), ('Released by', 'Quality lead')])
         + g2(panel('Lots consumed', table('minmax(0,1.3fr) 110px 86px 96px', ['Ingredient', 'Lot', '>Qty', 'Scanned'],
                    [['Flour', ('sn', 'F-2207'), ('r', '150 kg'), ('st', 'g', 'Yes')], ['Butter', ('sn', 'B-0913'), ('r', '75 kg'), ('st', 'g', 'Yes')],
                     ['Sugar', ('sn', 'S-4410'), ('r', '50 kg'), ('st', 'g', 'Yes')], ['Film wrap', ('sn', 'P-551'), ('r', '1 roll'), ('st', 'y', 'Typed')]]), '4 lots'),
              panel('Checks and output', listing([('g', 'Metal detector check passed', '09:10 and 11:40'), ('g', 'Bake temperature in range', 'Logged every 30 minutes'), ('y', '24 packs rejected', 'Underweight; recorded as scrap'), ('', 'Output: pallets 1042-A and 1042-B', 'Labels printed with batch and best-before')])), '1.35fr')),
         'Illustrative batch record screen showing product, quantities, best-before date, the ingredient lots consumed and the checks carried out',
         'A concept batch record. The lots-consumed table is the link that most paper systems cannot follow backwards.', h=520, ui=True)
T4 = fig(S + '-recall', m_steps([('Pick a lot', 'Choose one ingredient lot at random', 'Start the clock'), ('Trace forward', 'Find every batch that used it', 'Batches listed'), ('Find the output', 'Find where each finished lot went', 'Customers listed'), ('Reconcile', 'Do the quantities add up?', 'Stop the clock')],
                                 ['#6CB4F5', '#3CCB7F', '#F9B21D', '#F28B3C']),
         'Four steps of a mock recall: pick a lot, trace forward to batches, find where the output went, and reconcile quantities',
         'A mock recall. Run one every quarter and write down how long it took.', h=440, theme='navy', title='Test it with a mock recall')
T5 = fig(S + '-trace-screen', app('Batch Records', 'Concept on Zoho Creator', ['Batches', 'Lots in stock', 'Trace', 'Holds', 'Reports'], 'Trace', 'Trace: butter lot B-0913', 'Forward trace &middot; run 10 Oct, 14:02',
         kpis([('Received', '500 kg', 'on 2 Oct', 'fl'), ('Used in', '5 batches', '375 kg', 'fl'), ('Still in stock', '125 kg', 'Chiller 2', 'fl'), ('Shipped to', '7 orders', '4 customers', 'fl')])
         + panel('Where it went', table('120px minmax(0,1.2fr) 100px 110px minmax(0,1fr) 110px', ['Batch', 'Product', '>Butter', 'Made', 'Shipped to', 'Status'],
                 [[('sn', '24-1039'), 'Shortbread 200 g', ('r', '75 kg'), '7 Oct', '2 orders', ('st', 'r', 'Shipped')], [('sn', '24-1040'), 'Butter biscuit 150 g', ('r', '75 kg'), '7 Oct', '1 order', ('st', 'r', 'Shipped')],
                  [('sn', '24-1042'), 'Shortbread 200 g', ('r', '75 kg'), '9 Oct', '2 orders', ('st', 'r', 'Shipped')], [('sn', '24-1044'), 'Oat slice 180 g', ('r', '75 kg'), '9 Oct', '2 orders', ('st', 'y', 'Part shipped')],
                  [('sn', '24-1047'), 'Shortbread 200 g', ('r', '75 kg'), '10 Oct', 'None yet', ('st', 'g', 'In warehouse')]]), 'quantities reconcile: 375 + 125 = 500 kg', 'flex:1'),
         actions='<span class="btns">Export list</span><span class="btnr">Place lot on hold</span>'),
         'Illustrative forward trace screen for one ingredient lot, listing the five batches that used it, what was shipped and what is still in the warehouse',
         'A concept trace screen. The reconciliation line is the test: received must equal used plus remaining.', h=540, ui=True)

GUIDES.append(dict(
    slug=S, title='Batch and Lot Traceability: What to Record at Each Step',
    seo_title='Batch and Lot Traceability: What to Record',
    desc='How to set up batch and lot traceability in a small factory: the five recording points, the link most systems miss, and how to test it with a mock recall.',
    lead='Traceability is not a report you run after a complaint. It is a set of links that either were recorded when the work happened or do not exist.',
    category='Traceability', kind='arch', kind_label='Technical guide', tone='dark', layout='wide', author='team', published=TODAY, keyword='batch traceability manufacturing',
    facts=[('Goal', 'Trace any lot forward and back'), ('Recording points', 'Five, from receiving to dispatch'), ('The weak link', 'Which lots went into which batch'), ('Proof', 'A timed mock recall')],
    hero_alt='Cover: four recording points for batch traceability', hero_cap='Traceability data is created at four physical moments. Miss one and the chain breaks.',
    answer='Give every received lot and every production batch a number, and record five links as they happen: lot received, lot stored, lot issued to a batch, batch produced, and finished lot shipped to an order. The link most systems miss is which input lots went into which batch. Prove it works with a timed mock recall.',
    body='''
<p>A customer rings to say there is a problem with a product they bought in March. Three questions follow at once. Which batch was it? What went into that batch? Where did the rest of it go?</p>
<p>A business with working traceability answers in an hour. A business without it recalls everything made that month, because it cannot prove the problem is smaller.</p>

<h2 id="what-it-means">What traceability means in practice</h2>
<p>The working standard is <strong>one step back, one step forward</strong>. For any item you can say who supplied it and who you sold it to. Inside the factory that expands into a chain.</p>
''' + T1 + '''
<p>Two terms, because they are often mixed up:</p>
<ul>
  <li>A <strong>lot</strong> is a quantity of a material received or made together, which you treat as identical. Your supplier assigns their lot number; you may add your own.</li>
  <li>A <strong>batch</strong> is one production run. It consumes input lots and produces finished lots.</li>
</ul>
<p>Traceability is the ability to walk that chain in either direction: <em>forward</em> from an ingredient to every customer who received it, and <em>backward</em> from a finished pack to every input.</p>

<h2 id="five-points">The five recording points</h2>
''' + T2 + '''
<h3>1. Receiving</h3>
<p>Record the supplier&rsquo;s lot number, your own if you assign one, quantity, date and any certificate that came with it. If one delivery contains two supplier lots, that is two records. Label anything you repack.</p>
<h3>2. Storage</h3>
<p>Know which lot is in which location. This is also what lets you use the oldest lot first and put a lot on hold in one action.</p>
<h3>3. Issue to production</h3>
<p>This is the link most systems lack. When flour is tipped into a mixer, someone must record <em>which lot</em> went into <em>which batch</em>. If two lots are used in one batch, both are recorded. If a part-used bag goes back to the store, the remaining quantity is recorded against the same lot.</p>
<h3>4. Production</h3>
<p>The batch record: batch number, product, line, date, operators, the checks carried out and the quantity produced, including rejects.</p>
<h3>5. Dispatch</h3>
<p>Record which finished lot went on which order. &ldquo;We shipped 40 cartons to that customer&rdquo; is not enough if the cartons came from two batches.</p>

<h2 id="batch-record">What a usable batch record looks like</h2>
''' + T3 + '''
<p>A batch record earns its keep when it is filled in during the run, not afterwards. Design rules that help:</p>
<ul>
  <li><strong>Scan lots, do not type them.</strong> Lot numbers are long and similar. The screen above flags the one that was typed.</li>
  <li><strong>Make the batch number at the start.</strong> The system issues it when the run begins, and everything attaches to it.</li>
  <li><strong>Record rejects.</strong> Without them, quantities will never reconcile.</li>
  <li><strong>Print the label from the record.</strong> Batch number and best-before date come from the system, not from a hand stamp.</li>
</ul>

<h2 id="where-systems-fit">Where the systems fit</h2>
<p>Stock systems handle the two ends of the chain well. Zoho Inventory, for example, offers serial and batch tracking, including batch expiry dates, across multiple warehouses, with barcode scanning. It can tell you which batch you received and which batch you shipped.</p>
<p>The middle is the problem. Zoho Inventory has no manufacturing module, so it does not record a production run consuming three ingredient lots and producing two finished lots with operator checks attached. That link needs a manufacturing system, or a batch record app built for it.</p>
<p>We build that app on <a href="/zoho-creator-development/">Zoho Creator</a>. Creator forms scan barcodes and QR codes on phones and tablets, which suits a production line. The app writes the consumption and the output back to the stock system, so quantities stay in one place. The principle is the same as in our <a href="''' + G + '''production-tracking-zoho-creator/">production tracking guide</a>: the app records the work, the stock system owns the numbers.</p>
''' + callout('What software cannot do', 'No system can record a lot that has no label. Before any software work, make sure every container in the building carries a lot number someone can scan or read.', True) + '''

<h2 id="mock-recall">Prove it with a mock recall</h2>
<p>You do not know whether traceability works until you test it. A mock recall is a timed drill.</p>
''' + T4 + '''
<p>Run it both ways: forward from an ingredient lot, and backward from a finished pack picked off the shelf. Then check the arithmetic. Quantity received should equal quantity used plus quantity still in stock, allowing for recorded waste.</p>
''' + T5 + '''
<p>Record how long the drill took and where it stalled. The stalls are your work list. Customers who audit their suppliers, and food regulators in most countries, expect you to be able to do this quickly and to show that you practise it. Check the specific requirements that apply to your products and markets.</p>

<h2 id="worked-example">A worked example: one complaint, traced</h2>
<p>An example bakery receives a call on a Friday: a customer has found a piece of blue plastic in a pack of shortbread. The pack carries batch 24-1042.</p>
<ol>
  <li><strong>Backward trace.</strong> The batch record lists four input lots. The film wrap, lot P-551, is the only blue material on the line. It was also the one lot typed in by hand, so the team checks the roll label against the record. It matches.</li>
  <li><strong>Forward trace on the suspect lot.</strong> Lot P-551 was used on three batches over two days. Two have shipped to four customers. One is still in the warehouse.</li>
  <li><strong>Contain.</strong> The warehoused batch and the rest of the roll are put on hold in one action. Stock on hold cannot be picked.</li>
  <li><strong>Notify.</strong> The four customers get a list of the exact pallets and delivery dates concerned.</li>
  <li><strong>Reconcile.</strong> Packs made, less packs rejected, less packs in the warehouse, equals packs shipped. The numbers agree, so nothing is unaccounted for.</li>
</ol>
<p>The whole exercise is a morning&rsquo;s work because three batches are in question, not a month of production. Without the lot-to-batch link, the bakery would know only that film was used &ldquo;that week&rdquo;, and every pack made that week would be suspect.</p>
<h3>Serial numbers, for discrete products</h3>
<p>If you make machines or assemblies, the same logic applies with serial numbers in place of finished lots. Record which component lots or serials went into each unit, and which customer each unit went to. A faulty batch of bearings then becomes a list of twelve machines and their owners.</p>

<h2 id="mistakes">Common mistakes</h2>
<ul>
  <li><strong>Recording by date instead of by lot.</strong> &ldquo;We used flour delivered that week&rdquo; pulls three lots into every recall.</li>
  <li><strong>Mixing lots in one bin.</strong> Once two lots share a silo or a bin without a record, they are one lot for recall purposes.</li>
  <li><strong>Forgetting packaging.</strong> Printed film and labels are inputs too, and a wrong label is a common cause of recalls.</li>
  <li><strong>Rework without a record.</strong> Product from one batch reworked into another carries its history with it.</li>
  <li><strong>Writing up records at the end of the shift.</strong> See the timing problem in our <a href="''' + G + '''inventory-accuracy-for-manufacturers/">inventory accuracy guide</a>.</li>
</ul>

<h2 id="next-steps">Where to start</h2>
<ol>
  <li>Run a mock recall on paper this week and time it.</li>
  <li>Find the step where the trail went cold. For most businesses it is issue to production.</li>
  <li>Label every lot in the building.</li>
  <li>Put one scan-based record at the weak step, then run the drill again.</li>
</ol>
<p>Our <a href="''' + CS + '''batch-traceability-food-manufacturer/">food manufacturer reference implementation</a> shows the whole design, from receiving to the trace screen.</p>
''',
    faqs=[('What is the difference between a batch and a lot?',
           'A lot is a quantity of material received or made together and treated as identical. A batch is one production run. A batch consumes input lots and produces one or more finished lots. Many businesses use the two words loosely, which is fine as long as each has a unique number.'),
          ('Can Zoho Inventory do batch traceability?',
           'It tracks batches and serial numbers for stock you receive and ship, including expiry dates. It does not record which input lots were consumed by which production run, because it has no manufacturing module. That link needs a batch record app or a manufacturing system alongside it.'),
          ('How fast should a trace be?',
           'Fast enough that you can limit a recall to the affected product the same day. Set your own target, run a mock recall each quarter and record the time. Check whether your customers or regulators set a specific limit.'),
          ('Do we need barcodes?',
           'Strongly recommended. Lot numbers are long and easy to mistype, and one wrong character breaks the chain. A phone camera reading a printed label is enough.')],
    sources=[SRC['inv_features'], SRC['inv_mfg'], SRC['creator_scan'], SRC['creator_features']],
    related=['batch-traceability-food-manufacturer', 'quality-ncr-capa-workflow', 'inventory-accuracy-for-manufacturers'],
    services=[SVC['creator'], SVC['mzoho'], SVC['integ']],
))

# ====================================================================== 6. Quality: inspections, NCR, CAPA
S = 'quality-ncr-capa-workflow'
cover(S, 'Quality', 'Inspections, NCRs and CAPA without paper', 'Three records, one flow, and the measures that show it is working.',
      m_rows([('Inspection', 'A planned check with a pass or fail result'), ('NCR', 'A record of something that failed'), ('CAPA', 'The action that stops it happening again')]),
      theme='green', alt='Cover: the three quality records: inspection, nonconformance report and corrective action')
Q1 = fig(S + '-flow', m_chev([('Detect', 'Inspection or complaint'), ('Contain', 'Hold the stock'), ('Decide', 'Rework, scrap, accept'), ('Find cause', 'Why did it happen?'), ('Prevent', 'Change and verify')],
                              ['#067A3B', '#089949', '#0B6E4F', '#1B5A96', '#226DB4']),
         'Five-stage nonconformance flow: detect, contain, decide the disposition, find the cause, and prevent recurrence',
         'The life of a nonconformance. Most paper systems stop after the third arrow.', h=320, theme='green')
Q2 = fig(S + '-dispositions', m_table(['Disposition', 'Use when', 'What the system must do'],
                                       [['Rework', 'It can be brought back to specification', 'Add a rework step and re-inspect'], ['Scrap', 'It cannot be recovered', 'Write off the stock with a reason'],
                                        ['Use as is', 'The deviation does not affect fit or function', 'Record who approved it'], ['Return to supplier', 'The fault came in with the material', 'Raise a return and a supplier NCR']], '.8fr 1.3fr 1.3fr'),
         'Table of four dispositions for nonconforming product: rework, scrap, use as is, and return to supplier',
         'Four dispositions. Each one should trigger an action somewhere else in the system.', h=460, theme='green', title='What happens to the product')
Q3 = fig(S + '-ncr-screen', app('Quality', 'Concept on Zoho Creator', ['Inspections', 'NCRs', 'CAPA', 'Suppliers', 'Reports'], 'NCRs', 'NCR-0318 &middot; Bracket BR-40 out of tolerance', 'Raised 8 Oct by line inspector &middot; Open 2 days',
         stepper([('Detected', 'd'), ('Contained', 'd'), ('Disposition', 'c'), ('Root cause', ''), ('CAPA', ''), ('Closed', '')])
         + g2(panel('Details', fields([('Found at', 'In-process check'), ('Work order', 'WO-2291'), ('Quantity affected', '140 of 600'), ('Defect', 'Hole position +0.6 mm'), ('Suspected source', 'Drill jig 3'), ('Stock status', 'On hold')], 2)),
              panel('Decision needed', listing([('y', 'Proposed: rework 140 pcs', 'Re-drill on jig 1, then re-inspect'), ('', 'Approver: quality lead', 'Waiting since 9 Oct, 08:30'), ('r', 'Jig 3 stopped', 'Maintenance request MR-077 raised')]) + acts(('btnp', 'Approve rework'), ('btns', 'Scrap'), ('btnr', 'Reject')), 'role: quality lead'), '1.2fr')),
         'Illustrative nonconformance report screen with a six-stage progress bar, defect details and a pending disposition decision',
         'A concept NCR screen. The progress bar makes it obvious when an NCR stops at disposition and never gets a root cause.', h=500, ui=True)
Q4 = fig(S + '-fpy', m_formula('First-pass yield = units passed first time &divide; units started',
                                [('600', 'brackets started on WO-2291'), ('460', 'passed inspection first time'), ('140', 'needed rework')], 'First-pass yield = 460 &divide; 600 = 77%. Reworked units count as failures here, even if they pass later.'),
         'Worked example of first-pass yield: 460 of 600 units passed first time, giving 77 percent',
         'First-pass yield, worked through. Counting reworked units as passes is the commonest way to flatter this number.', h=400, theme='green', title='The measure to start with')
Q5 = fig(S + '-dashboard', app('Quality', 'Concept on Zoho Analytics', ['Overview', 'NCRs', 'CAPA', 'Suppliers', 'Reports'], 'Overview', 'Quality overview', 'Last 12 weeks',
         kpis([('First-pass yield', '94.2%', '+1.8 pts', 'up'), ('Open NCRs', '11', '4 over 14 days', 'dn'), ('Avg days to close', '9', '-3 days', 'up'), ('CAPA overdue', '2', 'needs owner', 'dn')])
         + g2(panel('NCRs by cause', bars2([('Setup or jig', 82, '14'), ('Material', 59, '10'), ('Operator method', 41, '7'), ('Drawing unclear', 24, '4'), ('Handling damage', 18, '3')]) + note('Example data. The cause list is a fixed pick list, so the chart can be trusted.'), '38 in 12 weeks'),
              panel('First-pass yield by week', svg_line([[91, 92.5, 92, 93, 92.4, 93.8, 94, 93.1, 94.6, 95, 94.4, 94.2]], ['31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42'], ymin=88, ymax=96, h=250), '%, axis starts at 88'), '1fr')),
         'Illustrative quality dashboard with first-pass yield, open NCRs, days to close, overdue corrective actions, NCRs by cause and a weekly yield trend',
         'A concept quality dashboard. NCRs by cause only works if the cause is chosen from a list.', h=560, ui=True)

GUIDES.append(dict(
    slug=S, title='Digital Quality Control: Inspections, NCRs and CAPA Without Paper',
    seo_title='Digital Quality Control: NCR and CAPA Workflow',
    desc='How to run inspections, nonconformance reports and corrective actions in one digital workflow, with the fields, decisions and measures that matter.',
    lead='Paper quality systems record that something went wrong. They are much worse at making sure someone found out why and stopped it happening again.',
    category='Quality', kind='guide', kind_label='Practical guide', tone='green', layout='toc-left', author='team', published=TODAY, keyword='NCR CAPA workflow manufacturing',
    facts=[('Three records', 'Inspection, NCR, CAPA'), ('The usual gap', 'NCRs closed without a root cause'), ('First measure', 'First-pass yield'), ('Built with', 'Forms, approvals and a dashboard')],
    hero_alt='Cover: the three quality records', hero_cap='Three records carry a quality system. Each one feeds the next.',
    answer='Run quality as three linked records. An inspection is a planned check. A failed check raises a nonconformance report, which holds the stock and needs a disposition: rework, scrap, use as is or return. An NCR that could recur raises a corrective action with an owner, a due date and a later check that it worked. Track first-pass yield and time to close.',
    body='''
<p>Walk into the quality office of most small factories and you will find a filing cabinet of nonconformance forms. Each was filled in carefully. Almost none can answer the question that matters: is this the fourth time this has happened?</p>
<p>Moving quality records out of the cabinet is one of the most contained and most useful first projects. It touches few people, needs little integration and changes what managers can see within weeks.</p>

<h2 id="three-records">Three records, and how they connect</h2>
<ul>
  <li><strong>Inspection.</strong> A planned check against a specification: incoming goods, in-process, or final. The result is pass or fail, with measurements where they matter.</li>
  <li><strong>Nonconformance report (NCR).</strong> Raised when something fails, whether an inspection found it or a customer did. It describes the problem and records what was done with the affected product.</li>
  <li><strong>Corrective and preventive action (CAPA).</strong> Raised when the cause needs removing, not just the product fixing. It has an owner, a due date and a check that it worked.</li>
</ul>
''' + Q1 + '''
<p>The first three stages deal with the product. The last two deal with the process. A filing cabinet handles the first three. The value is in the last two.</p>

<h2 id="inspections">Inspections: check less, record better</h2>
<p>Start by listing where checks already happen. There are usually more than anyone realises, most of them unrecorded. For each, decide:</p>
<ul>
  <li><strong>What is checked,</strong> against which specification or drawing revision.</li>
  <li><strong>How many.</strong> Every unit, first-off and last-off, or a sample per batch.</li>
  <li><strong>What is recorded.</strong> A tick for visual checks; the actual measurement for critical dimensions.</li>
  <li><strong>What a fail does.</strong> It should raise an NCR and hold the stock automatically.</li>
</ul>
<p>Recording the measurement, not just pass or fail, is what lets you see a process drifting before it produces rejects.</p>

<h2 id="ncr">The NCR: contain first, then decide</h2>
<p>An NCR has two jobs in its first hour. It tells people there is a problem, and it stops the affected product moving. On paper the second job depends on someone walking to the store with a red tag. In a system, raising the NCR changes the stock status.</p>
''' + Q3 + '''
<p>Fields worth having, and no more:</p>
<ul>
  <li>where it was found, and by whom;</li>
  <li>the work order, batch or supplier delivery it relates to;</li>
  <li>quantity affected, and quantity checked;</li>
  <li>the defect, chosen from a list, with a photo;</li>
  <li>the suspected source, also from a list.</li>
</ul>
<p>Then comes the disposition: what happens to the product.</p>
''' + Q2 + '''
<p>&ldquo;Use as is&rdquo; deserves care. It is a legitimate decision, and it must be made by a named person with the authority to make it, sometimes with the customer&rsquo;s agreement. An approval step with a role attached handles that.</p>

<h2 id="capa">CAPA: the part that pays</h2>
<p>Not every NCR needs a corrective action. A one-off handling knock does not. A third NCR against the same jig does. Set a rule you can apply without debate, such as: any NCR above a set cost, any customer complaint, and any cause that appears three times in a quarter.</p>
<p>A corrective action needs four things:</p>
<ol>
  <li><strong>A root cause,</strong> reached by asking why until the answer is something you can change. &ldquo;Operator error&rdquo; is rarely a root cause. Why was the error possible?</li>
  <li><strong>An action</strong> that removes the cause: a fixture, a changed drawing, a supplier specification, a check added earlier.</li>
  <li><strong>An owner and a date.</strong></li>
  <li><strong>An effectiveness check,</strong> scheduled for some weeks later. Did the problem come back?</li>
</ol>
''' + callout('The check most systems skip', 'Schedule the effectiveness check when the action is created, not when it is completed. A corrective action is closed when it has been shown to work, not when the task was ticked off.') + '''

<h2 id="measures">What to measure</h2>
<p>Begin with one number, first-pass yield, and add others when it has become routine.</p>
''' + Q4 + '''
<ul>
  <li><strong>NCRs by cause.</strong> Shows where to spend effort. Only meaningful if the cause comes from a fixed list.</li>
  <li><strong>Days to close.</strong> Long-open NCRs usually mean held stock nobody has decided about.</li>
  <li><strong>Supplier NCRs.</strong> Rejections per supplier, against deliveries received.</li>
  <li><strong>Overdue corrective actions.</strong> The plainest sign of whether the system is alive.</li>
</ul>
''' + Q5 + '''
<p>More on choosing measures is in our guide to <a href="''' + G + '''manufacturing-dashboards-kpis/">manufacturing dashboards and KPIs</a>.</p>

<h2 id="worked-example">A worked example: one NCR, start to finish</h2>
<p>Follow NCR-0318 from the screen above. The business is an example, a small metal fabricator making brackets.</p>
<ol>
  <li><strong>Detect.</strong> An in-process check finds hole positions 0.6 mm out on brackets from work order WO-2291. The inspector raises the NCR on a tablet and attaches a photo of the gauge.</li>
  <li><strong>Contain.</strong> The system marks 140 brackets as on hold. The inspector checks the other 460 made that shift, which pass. Drill jig 3 is stopped and a maintenance request is raised.</li>
  <li><strong>Decide.</strong> The quality lead approves rework: re-drill on jig 1 and inspect every piece. A rework step is added to the work order, so the planner sees the delay.</li>
  <li><strong>Find the cause.</strong> Asking why three times gets there. The holes were out because the jig bush was worn. The bush was worn because it had no replacement interval. It had no interval because jigs were never on the maintenance schedule.</li>
  <li><strong>Prevent.</strong> The corrective action adds all drill jigs to planned maintenance, with a bush check every month. An effectiveness check is booked for six weeks later: any hole-position NCRs since?</li>
</ol>
<p>On paper, this NCR would have ended at step three with &ldquo;reworked, OK&rdquo;, and jig 4 would have produced the same fault in the spring.</p>

<h2 id="building-it">Building it</h2>
<p>This is a natural fit for a low-code platform. On <a href="/zoho-creator-development/">Zoho Creator</a> the three records are three forms linked to each other. Its approvals and Blueprint features enforce who can disposition and who can close. The mobile apps let an inspector raise an NCR with a photo from the line, and role-based access and audit trails cover who changed what.</p>
<p>Two connections make it much more useful:</p>
<ul>
  <li><strong>To stock,</strong> so that raising an NCR holds the affected quantity and scrapping it writes it off.</li>
  <li><strong>To production,</strong> so that a rework disposition adds a rework step to the work order. Our <a href="''' + G + '''production-tracking-zoho-creator/">production tracking guide</a> covers that side.</li>
</ul>
<p>If you run Zoho ERP in India, it includes quality templates, rules and inspections of its own. Elsewhere, and for NCR and CAPA in particular, a custom app is the usual route. If you hold or want a quality certification, these records are what an auditor will ask to see, so agree the fields with whoever manages your certification.</p>

<h2 id="mistakes">Mistakes to avoid</h2>
<ul>
  <li><strong>Free-text causes.</strong> You cannot count them. Use a list, with &ldquo;other&rdquo; reviewed monthly.</li>
  <li><strong>Raising a CAPA for everything.</strong> The list becomes unmanageable and people stop believing in it.</li>
  <li><strong>Blaming the operator.</strong> It ends the investigation one step early.</li>
  <li><strong>A form with 40 fields.</strong> The inspector on the line will not fill it in.</li>
  <li><strong>No link to stock.</strong> The NCR says &ldquo;on hold&rdquo; while the product ships.</li>
</ul>

<h2 id="next-steps">Getting started</h2>
<ol>
  <li>Pull the last three months of paper NCRs and sort them by cause. That exercise alone usually finds a repeat problem.</li>
  <li>Agree the defect list, the cause list and the four dispositions.</li>
  <li>Build the NCR first. Add inspections and CAPA once it is in daily use.</li>
  <li>Review open NCRs and overdue actions in a fixed weekly slot.</li>
</ol>
''',
    faqs=[('What is the difference between an NCR and a CAPA?',
           'An NCR records a specific failure and what was done with the affected product. A CAPA addresses the cause so the failure does not recur. Every CAPA starts from one or more NCRs, but most NCRs do not need a CAPA.'),
          ('Does every nonconformance need a corrective action?',
           'No. Set a rule, for example any customer complaint, any NCR above a cost threshold, and any cause that repeats. Raising a corrective action for everything overloads the system.'),
          ('Can this be built in Zoho Creator?',
           'Yes. Inspections, NCRs and corrective actions are linked forms with approvals, photos from the mobile app, role-based access and an audit trail. Linking it to your stock system makes holds and scrap automatic.'),
          ('How do we calculate first-pass yield?',
           'Divide the units that passed inspection the first time by the units started. Units that passed after rework count as failures for this measure.')],
    sources=[SRC['creator_features'], SRC['erp_mo'], SRC['creator_mfg']],
    related=['batch-lot-traceability', 'manufacturing-dashboards-kpis', 'production-tracking-zoho-creator'],
    services=[SVC['creator'], SVC['bpa'], SVC['mwf']],
))

# ====================================================================== 7. Reorder points and purchasing
S = 'purchasing-reorder-points'
cover(S, 'Purchasing', 'Reorder points, safety stock and approvals', 'Two formulas, a worked example and a purchase flow that does not stall.',
      two(m_tiles([('1', 'Reorder point', 'When to order'), ('2', 'Safety stock', 'The buffer for bad weeks'), ('3', 'Order quantity', 'How much, in real pack sizes'), ('4', 'Approval', 'Fast for small, careful for large')])),
      theme='blue', alt='Cover: four parts of a purchasing set-up: reorder point, safety stock, order quantity and approval')
U1 = fig(S + '-rop', m_formula('Reorder point = (average daily use &times; lead time) + safety stock',
                                [('40', 'hinges used per day, on average'), ('7', 'days from order to delivery'), ('170', 'hinges of safety stock')], 'Reorder point = (40 &times; 7) + 170 = 450 hinges'),
         'Worked example of the reorder point formula: 40 per day times 7 days plus 170 safety stock gives 450',
         'The reorder point, worked through with example numbers.', h=400, title='When to order')
U2 = fig(S + '-safety', m_formula('Safety stock = (max daily use &times; max lead time) &minus; (avg daily use &times; avg lead time)',
                                   [('55', 'most used in a day'), ('10', 'longest lead time, days'), ('40', 'average used per day'), ('7', 'average lead time, days')], 'Safety stock = (55 &times; 10) &minus; (40 &times; 7) = 550 &minus; 280 = 270 hinges'),
         'Worked example of a simple safety stock formula using maximum and average daily use and lead time, giving 270',
         'A simple safety stock method. It covers the worst week you have seen, which is cautious; trim it once you trust your data.', h=420, title='How much buffer')
U3 = fig(S + '-flow', m_lanes(['Trigger', 'Order', 'Receive', 'Pay'], [
            ('Stock system', [('Stock below reorder point', 'Alert raised', 'warn'), None, ('Stock increased', 'On receipt'), None]),
            ('Purchasing', [('Draft purchase order', 'Supplier and quantity filled in'), ('PO approved and sent', 'By value band', 'hi'), None, None]),
            ('Stores', [None, None, ('Goods checked in', 'Quantity and quality'), None]),
            ('Accounts', [None, None, None, ('Bill matched and paid', 'PO, receipt and invoice agree', 'hi')])]),
         'Swimlane of the purchase flow across stock, purchasing, stores and accounts, from a low-stock trigger to a matched and paid bill',
         'The purchase flow across four roles. The two dark steps are where controls belong.', h=520, title='From low stock to paid bill')
U4 = fig(S + '-reorder-screen', app('Purchasing', 'Concept on Zoho Inventory data', ['Reorder list', 'Purchase orders', 'Receipts', 'Suppliers', 'Reports'], 'Reorder list', 'Items at or below reorder point', '10 Oct &middot; 6 items',
         kpis([('To order today', '6', 'items', 'fl'), ('Waiting approval', '2', 'purchase orders', 'fl'), ('Late from supplier', '1', '3 days over', 'dn'), ('Stock-outs this month', '1', '-3 vs last month', 'up')])
         + panel('Suggested orders', table('minmax(0,1.5fr) 80px 86px 96px minmax(0,1fr) 96px 110px', ['Item', '>On hand', '>Reorder at', '>Suggest', 'Supplier', '>Lead time', 'Action'],
                 [['Hinge 110&deg; soft-close', ('r', '410'), ('r', '450'), ('r', '1,000'), 'Northfix', ('r', '7 days'), ('st', 'b', 'Draft PO')],
                  ['MDF 18 mm sheet', ('r', '22'), ('r', '30'), ('r', '40'), 'Board Supply', ('r', '3 days'), ('st', 'b', 'Draft PO')],
                  ['Edge tape oak 22 mm', ('r', '300 m'), ('r', '400 m'), ('r', '1,000 m'), 'Trimline', ('r', '5 days'), ('st', 'y', 'In approval')],
                  ['Drawer runner 450', ('r', '60'), ('r', '80'), ('r', '200'), 'Northfix', ('r', '7 days'), ('st', 'b', 'Draft PO')],
                  ['Lacquer clear 20 L', ('r', '2'), ('r', '3'), ('r', '6'), 'Coatings Co', ('r', '10 days'), ('st', 'r', 'PO late')]]), 'suggested quantity rounded to supplier pack size', 'flex:1'),
         actions='<span class="btnp">Create draft POs</span>'),
         'Illustrative reorder list showing items below their reorder point with stock on hand, suggested order quantity, supplier, lead time and action',
         'A concept reorder list. Suggested quantities are rounded to pack sizes, and a buyer still confirms each order.', h=540, ui=True)
U5 = fig(S + '-approvals', m_table(['Order value', 'Who approves', 'Target time'],
                                    [['Under a small limit', 'Nobody: the buyer places it', 'Same hour'], ['Up to a mid limit', 'Operations or production manager', 'Same day'],
                                     ['Above the mid limit', 'Manager and finance', 'Two working days'], ['New supplier, any value', 'Finance sets up the supplier first', 'Before the first order']], '1fr 1.3fr .8fr'),
         'Approval bands for purchase orders by value, with who approves and a target approval time',
         'Approval bands. Set your own limits; what matters is that small routine orders are not held up.', h=440, title='Approval by value')

GUIDES.append(dict(
    slug=S, title='Reorder Points, Safety Stock and Purchase Approvals: A Practical Setup',
    seo_title='Reorder Points, Safety Stock and PO Approvals',
    desc='How to set reorder points and safety stock for a small manufacturer, with formulas and worked examples, plus a purchase approval flow that keeps moving.',
    lead='Running out of a two-dollar hinge stops a two-thousand-dollar job. Reorder points are the simplest protection there is, and most factories set them once and never look again.',
    category='Purchasing', kind='guide', kind_label='Practical guide', tone='', layout='toc-right', author='team', published=TODAY, keyword='reorder point safety stock',
    facts=[('Formula 1', 'Reorder point'), ('Formula 2', 'Safety stock'), ('Depends on', 'Accurate stock and real lead times'), ('Review', 'Every quarter')],
    hero_alt='Cover: four parts of a purchasing set-up', hero_cap='Four settings per item. Most problems come from the first two being guesses.',
    answer='Set each item&rsquo;s reorder point to average daily use multiplied by supplier lead time, plus safety stock. Size safety stock from your worst recent demand and lead time. Round order quantities to supplier pack sizes, approve purchase orders in bands by value, and review the figures every quarter. None of it works unless stock records are accurate.',
    body='''
<p>Ask a storeman how he knows when to order something and the usual answer is &ldquo;when it looks low&rdquo;. That works while one experienced person does all the buying and never takes a holiday. It stops working the week they do.</p>
<p>This guide covers the two formulas you need, how to turn them into real orders, and how to approve those orders without creating a queue.</p>

<h2 id="first-condition">One condition before you start</h2>
<p>Reorder points compare a level with the stock the system believes you have. If the system is wrong, the alert is wrong. Before setting anything up, measure your record accuracy as described in our <a href="''' + G + '''inventory-accuracy-for-manufacturers/">inventory accuracy guide</a>. If it is poor, fix that first, at least for the items you plan to automate.</p>

<h2 id="reorder-point">The reorder point</h2>
<p>The reorder point is the stock level at which you place an order. It has to cover what you will use while you wait for the delivery, plus a buffer.</p>
''' + U1 + '''
<p>Two inputs deserve attention:</p>
<ul>
  <li><strong>Average daily use.</strong> Take it from actual issues over the last three months, not from memory. Use working days.</li>
  <li><strong>Lead time.</strong> Measure it from the day you place the order to the day stock is on the shelf and usable, including your own receiving and inspection time. Use what suppliers actually achieve, not what the quote said.</li>
</ul>

<h2 id="safety-stock">Safety stock</h2>
<p>Safety stock covers the weeks that are not average: a busy fortnight, a late delivery, or both together. There are statistical methods for sizing it. For a small manufacturer starting out, this simple one is easier to explain and to check.</p>
''' + U2 + '''
<p>It asks: if we had our busiest days during our slowest delivery, how much more would we need than in a normal cycle? The result is cautious. Treat it as a starting point, and reduce it item by item once you have a few months of reliable data.</p>
<p>Do not hold safety stock evenly. Give more to items that are cheap, slow to arrive and able to stop a job. Give little or none to expensive items you buy per order.</p>

<h2 id="order-quantity">How much to order</h2>
<p>The formulas say when. How much is a practical decision:</p>
<ul>
  <li><strong>Supplier minimums and pack sizes.</strong> If hinges come in boxes of 500, you order in 500s.</li>
  <li><strong>Price breaks,</strong> weighed against the cash and space the extra stock ties up.</li>
  <li><strong>Shelf life.</strong> Never order more of a perishable material than you will use inside its life.</li>
  <li><strong>Delivery cost.</strong> Combining items from one supplier into a weekly order is often cheaper than ordering each as it triggers.</li>
</ul>
<p>A workable default is a quantity that covers three to four weeks of average use, rounded up to a pack size. Adjust from there.</p>

<h2 id="what-it-does-not-fit">Where reorder points do not fit</h2>
<p>Reorder points assume steady use. They are the wrong tool for:</p>
<ul>
  <li><strong>Job-specific materials.</strong> A special veneer for one project should be bought against that job.</li>
  <li><strong>Strongly seasonal items.</strong> A fixed level is too high for half the year and too low for the rest. Review them before each season.</li>
  <li><strong>Items with long, lumpy demand.</strong> If you use 200 once a quarter, the average says three a day and the average is misleading.</li>
</ul>
<p>If most of your materials look like the last two, you may need requirements planning rather than reorder points. Our comparison of <a href="''' + G + '''zoho-or-manufacturing-erp/">Zoho apps and a manufacturing ERP</a> explains the difference.</p>

<h2 id="purchase-flow">The purchase flow</h2>
''' + U3 + '''
<p>Four roles touch a purchase, and the delays are in the handovers. The aim is that each handover is a status change in one system, not an email.</p>
''' + U4 + '''
<p>Three controls are worth their cost:</p>
<ol>
  <li><strong>A purchase order for everything.</strong> Even small orders. Without one, nobody can match the invoice.</li>
  <li><strong>Receiving against the order.</strong> Stores record what actually arrived, and short deliveries are visible the same day.</li>
  <li><strong>Three-way match before payment.</strong> The order, the receipt and the supplier&rsquo;s invoice agree on quantity and price. Differences go to the buyer, not straight to payment.</li>
</ol>

<h2 id="approvals">Approvals that do not stall</h2>
<p>Approval steps are where good purchasing set-ups go to die. A manager who must approve every box of screws will either become a bottleneck or approve without looking.</p>
''' + U5 + '''
<p>Set bands by value, and let routine reorders of approved items from approved suppliers skip approval below a limit. Send approval requests to a phone, show the approver the stock level and the last price paid, and escalate automatically if nothing happens within the target time.</p>

<h2 id="in-the-system">Setting it up</h2>
<p>Most stock systems support the basics. Zoho Inventory, for example, has reorder points that remind you when stock is low, purchase orders, bills, backorders, price lists for vendors and multi-warehouse stock. What it leaves to you is the judgement: which supplier, what quantity, whether to combine orders.</p>
<p>Two additions make a real difference:</p>
<ul>
  <li><strong>A reorder list with suggestions,</strong> like the screen above, that rounds to pack sizes and groups by supplier. This is a report or a small app over your stock data.</li>
  <li><strong>An approval workflow</strong> matched to your bands, built with the stock system&rsquo;s own approvals where they are enough, or with <a href="/business-process-automation/">workflow automation</a> where they are not.</li>
</ul>
''' + callout('Keep a person in the loop', 'We do not recommend purchase orders that send themselves. The system should prepare the order and a buyer should release it. Suppliers change prices, pack sizes and lead times more often than master data gets updated.') + '''

<h2 id="worked-example">A worked example: three items, three settings</h2>
<p>The formulas give different answers for different kinds of item, which is the point. Take three from an example joinery.</p>
<ul>
  <li><strong>Soft-close hinges.</strong> Cheap, used on almost every job, seven days from a reliable supplier. Reorder point 450, order 1,000 at a time in boxes of 500. Running out stops fitting, so the buffer is generous and the cost of holding it is small.</li>
  <li><strong>18 mm MDF sheet.</strong> Bulky, used steadily, three days from a local merchant. Reorder point 30 sheets, order 40. Lead time is short and space is tight, so the buffer is small.</li>
  <li><strong>Walnut veneer board.</strong> Expensive and used only on certain jobs. No reorder point at all. It is bought against each job when the order is confirmed, and the job&rsquo;s start date allows for the lead time.</li>
</ul>
<p>Sorting your items into these three groups, before calculating anything, is most of the work. The first group gets automated reminders, the second gets tight levels and frequent small orders, and the third stays with the planner.</p>

<h2 id="review">Review every quarter</h2>
<p>Usage changes, suppliers change, products are added and dropped. Each quarter, for your top items, check that average daily use and lead time are still right, look at every stock-out and ask whether the level or the data was wrong, and look at items that have not moved and consider reducing or removing their levels.</p>

<h2 id="next-steps">A first week</h2>
<ol>
  <li>List the 30 items that most often stop jobs.</li>
  <li>Pull three months of issues and the last five deliveries for each.</li>
  <li>Calculate reorder point and safety stock with the two formulas.</li>
  <li>Enter them, and review the alerts daily for a month before trusting them.</li>
</ol>
''',
    faqs=[('How do I calculate a reorder point?',
           'Multiply average daily use by the supplier lead time in days, then add safety stock. Use actual usage from the last three months and the lead time suppliers really achieve, including your own receiving time.'),
          ('How much safety stock should a small manufacturer hold?',
           'A simple starting method is maximum daily use times maximum lead time, minus average daily use times average lead time. It is cautious. Reduce it item by item as your data improves, and hold more for cheap items that can stop a job.'),
          ('Does Zoho Inventory support reorder points?',
           'Yes. Zoho Inventory has reorder points that remind you when stock is low, along with purchase orders, bills and backorders. Suggested quantities, grouping by supplier and approval bands usually need a report or a small workflow on top.'),
          ('Should purchase orders be created automatically?',
           'Create drafts automatically and let a buyer release them. Prices, pack sizes and lead times change, and a quick human check catches errors that master data does not.')],
    sources=[SRC['inv_features'], SRC['flow']],
    related=['inventory-accuracy-for-manufacturers', 'connect-sales-production-accounts', 'zoho-or-manufacturing-erp'],
    services=[SVC['mzoho'], SVC['bpa'], SVC['integ']],
))
