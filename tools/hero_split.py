"""Two-column page heroes: the copy and team stats on the left, the scenario explorer
(or a side panel) on the right.

    python tools/hero_split.py        # applies to the hand-written pages listed below (idempotent)

The location, solutions and insights generators call split_hero() themselves. tools/build.py then
fills the @stats and @explorer markers from tools/partials/.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# page -> which flows its explorer plays (see js/home.js; '' for all of them),
# or ('panel', name) for a side panel instead of the explorer
PAGES = {
    'services/index.html': '',
    'zoho-development/index.html': '',
    'zoho-creator-development/index.html': 'app:zoho-creator',
    'zoho-crm-development/index.html': 'app:zoho-crm',
    'deluge-development/index.html': 'app:deluge',
    'zoho-integrations/index.html': 'sync',
    'business-process-automation/index.html': 'app:ai',
    'custom-software-development/index.html': 'app:zoho-catalyst,zoho-creator',
    'support-maintenance/index.html': 'app:zoho-desk',
    'work/index.html': '',
    'about/index.html': '',
    'pricing/index.html': ('panel', 'pricing'),
    'contact/index.html': ('panel', 'contact'),
}

CHECK = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>')
ARROW = '<span aria-hidden="true">&rarr;</span>'


def _list(items):
    return ''.join(f'                <li><span class="hero-panel-icon">{CHECK}</span>{t}</li>\n' for t in items)


def _steps(items):
    return ''.join(f'                <li><span class="hero-panel-num">{n}</span><span><strong>{a}</strong> {b}</span></li>\n'
                   for n, (a, b) in enumerate(items, 1))


def _links(items):
    return ''.join(f'                <li><a href="{u}">{t} {ARROW}</a></li>\n' for u, t in items)


# Side panels for pages where the explorer does not fit the page's job
PANELS = {
    'pricing': ('Every project includes', 'ul', 'hero-panel-list', _list([
        'A written proposal with scope, timeline and cost before any work starts',
        'Design, build and testing in stages, with regular demos',
        'Documentation your team can maintain',
        'Training for administrators and users',
        'One month of free support and onboarding after launch',
        'Zoho licences in your own name, so you own the account and the data',
    ]), f'<a class="hero-panel-link" href="#calculator">Estimate my project {ARROW}</a>'),
    'contact': ('What happens next', 'ol', 'hero-panel-steps', _steps([
        ('We reply within 6 hours,', 'with a few questions or times for a call.'),
        ('A discovery call', 'about how the work flows today and what has to change.'),
        ('A written proposal', 'with scope, timeline and cost, before any work starts.'),
    ]), '<p class="hero-panel-note">Prefer email? <a href="mailto:admin@zudoworks.com">admin@zudoworks.com</a></p>'),
    'insights': ('Start here', 'ul', 'hero-panel-links', _links([
        ('/insights/zoho-crm-implementation-cost/', 'How much a Zoho CRM implementation costs'),
        ('/insights/zoho-partner-software-development/', 'How to choose a Zoho development partner'),
        ('/insights/deluge-script-examples/', '10 Deluge script examples you can reuse'),
        ('/solutions/', 'Zoho solutions by industry: 90 example workflows'),
    ]), ''),
}


def panel_html(name):
    title, tag, cls, items, extra = PANELS[name]
    return ('            <div class="hero-panel">\n'
            f'              <p class="hero-panel-title">{title}</p>\n'
            f'              <{tag} class="{cls}">\n{items}              </{tag}>\n'
            + (f'              {extra}\n' if extra else '')
            + '            </div>\n')


HERO = re.compile(r'(<section class="page-hero page-hero--service">\s*<div class="container">\s*'
                  r'<nav class="breadcrumb".*?</nav>)(.*?)(\s*</div>\s*</section>)', re.S)


def split_hero(html, flows='', panel=None):
    """Wrap the hero copy and add the stats and the explorer (or a panel). Unchanged if already split."""
    if 'class="hero-split"' in html:
        return html
    if panel:
        visual = f'          <div class="hero-split-visual">\n{panel_html(panel)}          </div>\n'
    else:
        visual = (f'          <div class="hero-split-visual" data-fx-filter="{flows}">\n'
                  '            <!-- @explorer -->\n'
                  '            <!-- @/explorer -->\n'
                  '          </div>\n')

    def wrap(m):
        copy = m.group(2).strip('\n')
        copy = '\n'.join('    ' + line if line.strip() else line for line in copy.split('\n'))
        return (m.group(1) + '\n'
                '        <div class="hero-split">\n'
                '          <div class="hero-split-copy">\n'
                f'{copy}\n'
                '            <!-- @stats -->\n'
                '            <!-- @/stats -->\n'
                '          </div>\n'
                + visual +
                '        </div>' + m.group(3))

    out, n = HERO.subn(wrap, html, count=1)
    if not n:
        raise ValueError('page hero not found')
    return out


if __name__ == '__main__':
    for rel, flows in PAGES.items():
        path = os.path.join(ROOT, rel)
        html = open(path, encoding='utf-8').read()
        new = split_hero(html, panel=flows[1]) if isinstance(flows, tuple) else split_hero(html, flows)
        if new != html:
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new)
            print('split', rel)
