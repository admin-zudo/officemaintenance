# Cover scenes

Each article has one scene file here, `<slug>.html`, rendered by `render_cover.py <slug>`.

Shared styles and colour themes are in `_base.css`: `theme-blue`, `theme-green`, `theme-amber`, `theme-navy`.

Layouts to copy from (any scene can be combined with any theme):

| Layout | Example scene | Good for |
|---|---|---|
| panel-flow | `_template-panel.html` | A flow or connection between things |
| panel-compare | `zoho-crm-vs-hubspot.html` | Two options, with a text panel on the left |
| steps | `zoho-mcp-claude-chatgpt.html` | Levels, stages or a process in order |
| split | `zoho-flow-vs-deluge.html` | Two options as bold colour panels |
| rows | `zoho-for-manufacturing.html` | Three or four choices, ranked or numbered |

A new article's cover must not reuse the layout or the theme of the three most recent covers (see
`cover_style` in `blog/.automation-history.json`). New layouts are welcome when none fits: build them on
`_base.css`, keep `data-strict` on the body and `data-block` on every separate block, and record the layout
and theme in `tools/insights/articles_watch.py`.
