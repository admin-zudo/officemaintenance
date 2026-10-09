"""Add or refresh "Related guides" article cards on service pages and the homepage.

Run from the repo root after insights_gen.py, then run tools/build.py.
The section is wrapped in <!-- @guides --> markers so re-running replaces it.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from insights_gen import BY_SLUG, card  # noqa: E402

GUIDES = {
    'index.html': ['zoho-for-manufacturing', 'zoho-crm-implementation-cost', 'deluge-script-examples'],
    'services/index.html': ['zoho-crm-implementation-cost', 'zoho-partner-software-development', 'zoho-creator-vs-power-apps'],
    'zoho-development/index.html': ['zoho-partner-program-explained', 'zoho-partner-software-development', 'zoho-crm-implementation-cost'],
    'zoho-creator-development/index.html': ['zoho-creator-vs-power-apps', 'zoho-for-manufacturing', 'deluge-script-examples'],
    'zoho-crm-development/index.html': ['migrate-hubspot-salesforce-to-zoho-crm', 'zoho-crm-implementation-cost', 'zoho-crm-vs-hubspot'],
    'deluge-development/index.html': ['deluge-script-examples', 'zoho-flow-vs-deluge', 'zoho-agentic-ai-hyperautomation'],
    'zoho-integrations/index.html': ['zoho-flow-vs-deluge', 'zoho-mcp-claude-chatgpt', 'zoho-analytics-agentic-data-foundations-2026'],
    'business-process-automation/index.html': ['zoho-agentic-ai-hyperautomation', 'zoho-flow-vs-deluge', 'zoho-mcp-claude-chatgpt'],
    'custom-software-development/index.html': ['zoho-creator-vs-power-apps', 'zoho-for-manufacturing', 'zoho-flow-vs-deluge'],
    'support-maintenance/index.html': ['zoho-partner-software-development', 'deluge-script-examples', 'zoho-crm-implementation-cost'],
    'work/index.html': ['zoho-partner-program-explained', 'zoho-partner-software-development', 'zoho-crm-implementation-cost'],
    'locations/index.html': ['zoho-partner-program-explained', 'zoho-partner-software-development', 'zoho-crm-implementation-cost'],
    'locations/india/index.html': ['zoho-partner-program-explained', 'zoho-crm-implementation-cost', 'zoho-for-manufacturing'],
    'locations/united-states/index.html': ['zoho-crm-vs-hubspot', 'zoho-crm-implementation-cost', 'zoho-partner-program-explained'],
    'locations/united-kingdom/index.html': ['zoho-partner-program-explained', 'zoho-crm-implementation-cost', 'zoho-creator-vs-power-apps'],
    'locations/australia/index.html': ['zoho-partner-program-explained', 'zoho-crm-implementation-cost', 'deluge-script-examples'],
    'locations/new-zealand/index.html': ['zoho-partner-program-explained', 'zoho-crm-implementation-cost', 'deluge-script-examples'],
}

HOME_INTRO = ('Practical guides written by our CTO from real project work.')


def section(slugs, home=False):
    title = 'From our Insights' if home else 'Related guides'
    intro = HOME_INTRO if home else 'Practical articles on the questions buyers ask us most.'
    cards = '\n'.join(card(BY_SLUG[s]) for s in slugs)
    return f'''    <!-- @guides -->
    <section class="section section--alt" id="guides">
      <div class="container">
        <div class="section-header section-header--left">
          <p class="section-label">Insights</p>
          <h2>{title}</h2>
          <p>{intro} <a href="/insights/" class="text-link">All articles</a></p>
        </div>
        <div class="post-grid">
{cards}
        </div>
      </div>
    </section>
    <!-- @/guides -->
'''


for path, slugs in GUIDES.items():
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'    <!-- @guides -->.*?<!-- @/guides -->\n', '', s, flags=re.S)
    block = section(slugs, home=(path == 'index.html'))
    m = re.search(r'\n( *)<section class="section" id="faq">', s) or re.search(r'\n( *)<section class="cta-banner"', s)
    if not m:
        sys.exit('no anchor in ' + path)
    s = s[:m.start() + 1] + block + s[m.start() + 1:]
    open(path, 'w', encoding='utf-8', newline='\n').write(s)
    print('guides ->', path)
