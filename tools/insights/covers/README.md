# Cover scenes

Each article has one scene file here, `<slug>.html`, rendered by `render_cover.py <slug>` into
`Asset/img/insights/<slug>.webp` (1600x900) and `Asset/og/<slug>.jpg` (1200x630).

## How a scene is built

- `_base.css` holds the four colour themes: `theme-blue`, `theme-green`, `theme-amber`, `theme-navy` (dark).
- `_kit.css` holds the building blocks. A scene is a grid with three areas:
  - **head**: tag, headline, one line, takeaway, logo. Styles: `card`, `bare`, `solid`, `bar`, `hero`, `center`, `band`.
  - **body**: the information. One body type per scene (see the table), with an optional row of three facts.
  - **foot**: logo and website address.
- Frames place the head: `f-left`, `f-right`, `f-top`, `f-bottom`.
- Because everything sits in a grid, blocks cannot overlap. `render_cover.py` still refuses to write an image
  when anything is crowded, cut off, or spilling out of its box.

## Starting layouts

34 ready layouts, `layout-NN-name.html`. Their text is sample text. Copy one to `<slug>.html` and replace every word.

| Body type | What it shows | Layout files |
|---|---|---|
| compare | Two options as cards with points | 01, 26 |
| split | Two options as bold colour panels | 10, 29 |
| table | Options compared area by area | 12 |
| tiers | Three levels side by side, one highlighted | 11 |
| scorecards | Three options with ratings | 13 |
| steps | Three or four stages as cards | 06, 14 |
| arrows | A process as a row of arrows | 16, 31 |
| timeline | Weeks or phases along a line | 15 |
| weeks | Stages down a vertical line | 04, 34 |
| rows | Three or four numbered choices | 03, 21, 33 |
| tiles | Six points in a grid | 02, 20, 30 |
| checklist | Six things to check or ask | 05, 25 |
| do and avoid | Two lists, good and bad | 09 |
| before and after | The change a project makes | 24 |
| matrix | Four quadrants, one highlighted | 08, 32 |
| number | One big figure with three supporting ones | 07, 28 |
| bars | Real quantities compared (only with real numbers) | 17 |
| levels | A funnel or pyramid | 19 |
| hub | One thing connected to four others | 18 |
| groups | Named groups of short items | 27 |
| question | A buyer's question and the short answer | 23 |
| statement | One strong line, attributed | 22 |

Older hand-built scenes also work as layouts: `_template-panel.html` (a flow of circles),
`zoho-crm-vs-hubspot.html`, `zoho-mcp-claude-chatgpt.html`, `zoho-flow-vs-deluge.html`, `zoho-for-manufacturing.html`.

## Rules for a new cover

1. Look at `cover_style` for recent articles in `blog/.automation-history.json`. Do not reuse a body type used
   by any of the last six covers, or a theme used by either of the last two.
2. Pick the body type that fits what the article actually says. Do not force content into a shape.
3. Any head style, frame and theme can be combined with any body type. Change them freely to get a new look,
   and add new body types to `_kit.css` when none fits (then add a row to the table above).
4. People: `who` boxes and the question and statement layouts carry a small flat illustrated figure. Three are
   drawn in the layouts (office worker, analyst, factory worker). Use one where a person fits the topic. Never
   photos or realistic faces.
5. Every word on the cover must be true and must match the article. Keep `data-strict` on the body and
   `data-block` on every separate block, and record the body type and theme as `cover` in
   `tools/insights/articles_watch.py`.
