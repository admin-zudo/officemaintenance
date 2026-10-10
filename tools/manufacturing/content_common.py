"""Shared helpers and verified source links for the Manufacturing content files."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figs import *  # noqa: F401,F403

TODAY = '2026-10-10'
M = '/manufacturing/'
G = M + 'guides/'
CS = M + 'case-studies/'

# Pages checked in October 2026 (title, url). Cite only what an article actually relies on.
SRC = dict(
    inv_features=('Zoho Inventory: features', 'https://www.zoho.com/inventory/features/'),
    inv_mfg=('Zoho Inventory knowledge base: manufacturing support', 'https://www.zoho.com/us/inventory/kb/general-overview/zom-manufacturing-support.html'),
    inv_composite=('Zoho Inventory help: composite items', 'https://www.zoho.com/us/inventory/help/items/composite-items.html'),
    erp=('Zoho ERP (India)', 'https://www.zoho.com/en-in/erp/'),
    erp_mo=('Zoho ERP help: manufacturing orders', 'https://www.zoho.com/en-in/erp/help/manufacturing-order/understanding-manufacturing-order.html'),
    creator_features=('Zoho Creator: features', 'https://www.zoho.com/creator/features.html'),
    creator_mfg=('Zoho Creator for manufacturing', 'https://www.zoho.com/creator/solutions/manufacturing/'),
    creator_scan=('Zoho Creator help: scanning QR codes and barcodes', 'https://help.zoho.com/portal/en/kb/creator/developer-guide/forms/add-and-manage-fields/articles/understand-scanning-qr-code-bar-code'),
    creator_offline=('Zoho Creator help: understanding offline access', 'https://help.zoho.com/portal/en/kb/creator/developer-guide/mobile/articles/understanding-offline-access'),
    creator_ai=('Zoho Creator: AI Modeler', 'https://www.zoho.com/creator/artificial-intelligence-modeler.html'),
    analytics=('Zoho Analytics: features', 'https://www.zoho.com/analytics/features.html'),
    books_editions=('Zoho Books knowledge base: country-specific editions', 'https://www.zoho.com/us/books/kb/general/different-country-edition.html'),
    flow=('Zoho Flow: pricing and limits', 'https://www.zoho.com/flow/pricing.html'),
    deluge_limits=('Deluge: limitations', 'https://www.zoho.com/deluge/help/limitations.html'),
    one_apps=('Zoho One: applications', 'https://www.zoho.com/one/applications/web.html'),
    mcp=('Zoho MCP', 'https://www.zoho.com/mcp/'),
)

SVC = dict(
    creator=('/zoho-creator-development/', 'Zoho Creator development'),
    integ=('/zoho-integrations/', 'Zoho integrations'),
    bpa=('/business-process-automation/', 'Business process automation'),
    custom=('/custom-software-development/', 'Custom software'),
    deluge=('/deluge-development/', 'Deluge development'),
    mzoho=(M + 'zoho-implementation/', 'Zoho implementation for manufacturers'),
    mai=(M + 'ai-automation/', 'AI in manufacturing'),
    mwf=(M + 'workflows/', 'Manufacturing workflows'),
    pricing=('/pricing/', 'Pricing'),
)


def two(main_html):
    """Force a tile or checklist grid to two columns (for the narrower hero panel)."""
    return main_html.replace('class="main m-tiles"', 'class="main m-tiles" style="grid-template-columns:repeat(2,minmax(0,1fr))"') \
                    .replace('class="main m-check"', 'class="main m-check" style="grid-template-columns:minmax(0,1fr)"')


def cover(slug, tag, h1, sub, right, theme='blue', solid=False, alt='', cap=''):
    """The 16:9 cover for a guide, case study or solution page. Also the card and social image."""
    fig(slug, hero(dict(tag=tag, h1=h1, sub=sub), right, solid), alt, cap, h=675, theme=theme, hero=True)


def callout(label, text, warn=False):
    return f'<div class="mfg-callout{" mfg-callout--warn" if warn else ""}"><p class="mfg-callout-label">{label}</p><p>{text}</p></div>'


def tablew(head, rows, cls='table-wrap'):
    th = ''.join(f'<th scope="col">{h}</th>' for h in head)
    tr = ''.join('<tr>' + f'<th scope="row">{r[0]}</th>' + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rows)
    return f'<div class="{cls}"><table{" class=\"mfg-table\"" if cls != "table-wrap" else ""}><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
