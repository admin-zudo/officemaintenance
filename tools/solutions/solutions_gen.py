"""Builds the industry solutions page and the homepage explorer data.

    python tools/solutions/solutions_gen.py

Writes:
  solutions/scenarios.json   loaded by the homepage explorer (js/home.js)
  solutions/index.html       every flow as crawlable text, with schema

Run it before tools/build.py, which fills in the head, header and footer.
The flows themselves live in scenarios.py.
"""
import html
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


def _load(name, path):
    """Import a sibling tool by file path, so editors and linters resolve it too."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


INDUSTRIES = _load('scenarios', os.path.join(HERE, 'scenarios.py')).INDUSTRIES
_loc = _load('locations_gen', os.path.join(ROOT, 'tools', 'locations', 'locations_gen.py'))
SITE, page, ld, faq_html, faq_ld = _loc.SITE, _loc.page, _loc.ld, _loc.faq_html, _loc.faq_ld
breadcrumb_ld, write, CTA = _loc.breadcrumb_ld, _loc.write, _loc.CTA

ICONS = {'web', 'ads', 'tablet', 'deluge', 'chat', 'clock', 'cart', 'mail', 'ai', 'doc'}
URL = SITE + '/solutions/'
TOTAL = sum(len(i['flows']) for i in INDUSTRIES)

FAQS = [
    ('What is a Zoho integration layer?',
     'It is the set of connections that lets Zoho apps and your other systems pass data to each other: Deluge scripts, Zoho Flow, '
     'webhooks and APIs. When one app changes a record, the layer updates the others, so nobody copies data by hand.'),
    ('How does AI fit into a Zoho workflow?',
     'AI handles the steps that need reading or judgement: reading an order email or a document, scoring a lead, sorting tickets or '
     'drafting a reply. It can be Zoho Zia, or Claude and ChatGPT connected to your Zoho data through Zoho MCP. A person still '
     'approves anything important.'),
    ('What does "syncs back" mean?',
     'Data flows in both directions. When a later step finishes, such as a signed contract or a paid invoice, its status is written '
     'back to the earlier record, such as the CRM deal, so everyone sees the current state in the app they use.'),
    ('Are these real client projects?',
     'No. They are example workflows that show what can be built with Zoho for each industry. Every project starts with your own '
     'process, so the apps and steps are chosen to fit how your business actually runs.'),
    ('Which Zoho apps do these workflows use?',
     'Zoho CRM, Creator, Books, Desk, Analytics, Flow, Forms, Sign, WorkDrive, Projects, People, Cliq, Campaigns, SalesIQ, Sites, '
     'Mail, Catalyst, ERP, Zia and Zoho One, together with Deluge scripts, APIs and an AI layer.'),
]


def validate():
    logos = {f[:-4] for f in os.listdir(os.path.join(ROOT, 'Asset', 'zoho')) if f.endswith('.svg')}
    for ind in INDUSTRIES:
        assert len(ind['flows']) == 5, (ind['name'], len(ind['flows']))
        for f in ind['flows']:
            for n, st in enumerate(f['steps']):
                art = st[0]
                assert art in ICONS or art in logos, (f['short'], art)
                if len(st) == 5:
                    assert 0 <= st[3] < n, (f['short'], st)


def data():
    out = []
    for ind in INDUSTRIES:
        for f in ind['flows']:
            steps = [[s[0], s[1], s[2]] + ([[s[3], s[4]]] if len(s) == 5 else []) for s in f['steps']]
            out.append({'ind': ind['name'], 'slug': ind['slug'], 'short': f['short'], 'problem': f['problem'],
                        'steps': steps, 'result': f['result']})
    return out


def e(t):
    return html.escape(t, quote=False).replace("'", '&rsquo;')


def flow_card(ind, k, f):
    steps = ''
    for n, s in enumerate(f['steps']):
        sync = f'<span class="sol-sync">{e(s[4])}.</span>' if len(s) == 5 else ''
        steps += f'              <li><strong>{e(s[1])}:</strong> {e(s[2])}.{sync}</li>\n'
    return f'''          <article class="sol-card" id="{ind['slug']}-{k + 1}">
            <h3>{e(f['short'])}</h3>
            <p class="sol-problem"><span>The problem</span> {e(f['problem'])}</p>
            <ol class="sol-steps">
{steps}            </ol>
            <p class="sol-result"><span>Result</span> {e(f['result'])}</p>
          </article>
'''


def solutions_page():
    crumbs = [('Home', '/'), ('Solutions', '/solutions/')]
    title = 'Zoho Solutions by Industry: 90 Workflows | Zudo Works'
    desc = (f'{TOTAL} example Zoho workflows for {len(INDUSTRIES)} industries, from manufacturing to legal: the problem, every step '
            'through the integration and AI layer, and the result.')
    items = [{"@type": "ListItem", "position": n + 1, "name": f'{ind["name"]}: {f["short"]}',
              "url": f'{URL}#{ind["slug"]}-{k + 1}'}
             for n, (ind, k, f) in enumerate((ind, k, f) for ind in INDUSTRIES for k, f in enumerate(ind['flows']))]
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": title.split(' | ')[0],
                 "numberOfItems": TOTAL, "itemListElement": items}
    service = {"@context": "https://schema.org", "@type": "Service", "name": "Zoho workflow automation and integration",
               "serviceType": "Zoho integration, automation and AI workflows", "url": URL,
               "provider": {"@type": "Organization", "@id": SITE + "/#organization", "name": "Zudo Works"},
               "audience": [{"@type": "BusinessAudience", "name": ind['name']} for ind in INDUSTRIES]}
    schema = breadcrumb_ld('Solutions', URL, crumbs) + ld(item_list) + ld(service) + faq_ld(FAQS)

    nav = ''.join(f'          <li><a href="#{ind["slug"]}">{e(ind["name"])}</a></li>\n' for ind in INDUSTRIES)
    sections = ''
    for i, ind in enumerate(INDUSTRIES):
        cards = ''.join(flow_card(ind, k, f) for k, f in enumerate(ind['flows']))
        sections += f'''    <section class="section{' section--alt' if i % 2 else ''}" id="{ind['slug']}">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">{e(ind['name'])}</p>
          <h2>{e(ind['name'])}: five problems Zoho solves</h2>
          <p>{e(ind['intro'])}</p>
        </div>
        <div class="sol-grid">
{cards}        </div>
      </div>
    </section>

'''
    body = f'''        <p class="section-label">Solutions</p>
        <h1>Zoho solutions by industry: {TOTAL} example workflows</h1>
        <p class="page-lead">Here are {TOTAL} common business problems across {len(INDUSTRIES)} industries, and how Zoho solves each one.
          Every workflow shows the trigger, each step through the integration and AI layer (Deluge, Zoho Flow, APIs and AI), what
          syncs back to earlier apps, and the result. They are examples of what we build, not client case studies.</p>
        <div class="btn-group">
          <a href="/contact/" class="btn btn-primary btn-lg" data-booking>Book a Discovery Call</a>
          <a href="/#hero" class="btn btn-secondary btn-lg">Watch a flow animate</a>
        </div>
      </div>
    </section>

    <nav class="section sol-index" aria-label="Industries">
      <div class="container">
        <ul class="sol-nav">
{nav}        </ul>
      </div>
    </nav>

    <section class="section section--alt" id="how-it-works">
      <div class="container container--prose">
        <div class="section-header section-header--left">
          <p class="section-label">How it works</p>
          <h2>One integration and AI layer between your apps</h2>
          <p>Each Zoho app does one job well: CRM for customers, Books for invoices, Desk for support, Creator for custom apps.
            The integration layer connects them with Deluge, Zoho Flow, webhooks and APIs, so a change in one app updates the others.
            The AI layer, using Zoho Zia or Claude and ChatGPT through Zoho MCP, reads documents and emails, sorts requests and drafts
            replies, with a person approving anything important.</p>
          <p>Data also flows back. When a contract is signed or an invoice is paid, the status syncs back to the original record,
            so sales, operations and finance always see the same picture.</p>
        </div>
      </div>
    </section>

{sections}{faq_html(FAQS, 'Zoho workflows: common questions')}
{CTA % 'Which of these problems sounds like yours?'}'''
    return page(title, desc, URL, schema, crumbs, body)


if __name__ == '__main__':
    validate()
    path = os.path.join(ROOT, 'solutions', 'scenarios.json')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(data(), fh, ensure_ascii=False, separators=(',', ':'))
    print('wrote solutions/scenarios.json', TOTAL, 'flows')
    write('solutions/index.html', solutions_page())
