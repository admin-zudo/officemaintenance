"""Upwork capability deck: 8 slides, 16:9, native shapes and editable text. Called by make_upwork.py.

Reuses the drawing helpers in tools/brochure/deck.py. Same rules as the PDF guide: no contact details
(Upwork rule), no prices, no client names or results, no partner claim.
"""
import importlib.util, os

from pptx import Presentation
from pptx.util import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('deck', os.path.join(os.path.dirname(HERE), 'brochure', 'deck.py'))
d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(d)

W, H = d.W, d.H
INK, BODY, MUTED, LINE, SOFT = d.INK, d.BODY, d.MUTED, d.LINE, d.SOFT
BLUE, BLUE_DK, BLUE_BG, GREEN, GREEN_BG = d.BLUE, d.BLUE_DK, d.BLUE_BG, d.GREEN, d.GREEN_BG
NAVY, NAVY2, SKY, AMBER_BG = d.NAVY, d.NAVY2, d.SKY, d.AMBER_BG
box, oval, text, pic, pic_fill, fit, brand_bar, chips, heading = d.box, d.oval, d.text, d.pic, d.pic_fill, d.fit, d.brand_bar, d.chips, d.heading
TOTAL = 8


def frame(s, img, n, section):
    pic(s, img['logo'], 0.6, 0.38, 0.3, 0.3)
    text(s, 0.98, 0.38, 3, 0.3, 'Zudo Works', size=11, color=INK, bold=True, anchor='m')
    text(s, W - 5.6, 0.38, 5, 0.3, section.upper(), size=9, color=MUTED, bold=True, align='r', anchor='m')
    box(s, 0.6, 0.86, W - 1.2, 0.012, fill=LINE)
    text(s, 0.6, H - 0.5, 5, 0.25, 'Zudo Works · Capability guide', size=9, color=MUTED)
    text(s, W - 1.6, H - 0.5, 1, 0.25, f'{n:02d} / {TOTAL:02d}', size=9, color=INK, bold=True, align='r')


def dot_list(s, x, y, w, items, size=10.5, gap=0.36, color=INK, dot=GREEN):
    for i, t in enumerate(items):
        yy = y + i * gap
        oval(s, x, yy + 0.08, 0.12, dot)
        text(s, x + 0.25, yy, w - 0.25, gap, t, size=size, color=color)


def build(path, img):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W), Inches(H)
    blank = prs.slide_layouts[6]
    prs.core_properties.title = 'Zudo Works: capabilities and how we work on Upwork'
    prs.core_properties.author = 'Zudo Works'

    # 1 · Cover
    s = prs.slides.add_slide(blank)
    box(s, 0, 0, W, H, fill='F3F7FC')
    pic_fill(s, img['handshake'], 7.3, 0, W - 7.3, H)
    pic(s, img['logo'], 0.7, 0.6, 0.55, 0.55)
    text(s, 1.38, 0.6, 4, 0.55, [[('Zudo Works', {'size': 18, 'bold': True, 'color': INK})], [('ZOHO & CUSTOM SOFTWARE DEVELOPMENT', {'size': 7.5, 'bold': True, 'color': MUTED})]], anchor='m', spacing=1.0)
    brand_bar(s, 0.7, 2.0)
    text(s, 0.7, 2.2, 6, 0.3, 'CAPABILITY GUIDE FOR UPWORK CLIENTS', size=10, color=BLUE, bold=True)
    text(s, 0.7, 2.55, 6.3, 2.0, [[('What we build, and ', {}), ('how we run your project on Upwork', {'color': BLUE})]], size=30, color=INK, bold=True, spacing=0.98)
    text(s, 0.7, 4.0, 6.0, 1.0, 'Our services, the ways we contract, how we communicate, how we handle your access and data, and what you receive at the end.', size=12.5, color=BODY, spacing=1.25)
    chips(s, 0.7, 5.05, 6.2, ['Zoho Creator', 'Zoho CRM', 'Deluge', 'Integrations', 'AI automation', 'Custom software'], size=9.5, fill='FFFFFF')
    text(s, 0.7, 6.85, 6, 0.3, 'Chennai, India · Working with the US, UK, Australia, New Zealand and the Middle East', size=9, color=MUTED)

    # 2 · At a glance
    s = prs.slides.add_slide(blank)
    frame(s, img, 2, 'At a glance')
    heading(s, 'At a glance', 'A small team of Zoho developers, not a sales layer', 'Zoho developers', size=26, w=12)
    text(s, 0.6, 2.0, 7.0, 0.9, 'We design, build and fix business systems on Zoho Creator, Zoho CRM and the wider Zoho suite, connect them to your other tools, and write custom code when Zoho is not the right tool. The person who scopes your job builds it.', size=12, color=BODY, spacing=1.2)
    facts = (('Technical lead', 'Arunkumar V, CTO · “Master of Creator (Global Winner)”, Zoho Creator Partner Hackathon 2025'),
             ('Contracts', 'Fixed-price milestones or hourly, entirely through Upwork'),
             ('Reply time', 'Within 6 hours on Upwork Messages, guaranteed'),
             ('After launch', 'One month of free support and onboarding on every build'))
    for i, (k, v) in enumerate(facts):
        y = 3.1 + i * 0.5
        box(s, 0.6, y - 0.06, 7.0, 0.012, fill=LINE)
        text(s, 0.6, y, 1.7, 0.45, k.upper(), size=8.5, color=MUTED, bold=True)
        text(s, 2.3, y, 5.3, 0.45, v, size=10.5, color=INK)
    stats = (('20+', 'Projects our team has worked on'), ('10+', 'Client businesses supported'), ('40+', 'Zoho products used'), ('1 month', 'Free support after every build'))
    for i, (b, t) in enumerate(stats):
        x, y = 8.2 + (i % 2) * 2.3, 2.0 + (i // 2) * 1.55
        box(s, x, y, 2.15, 1.4, fill='FFFFFF', line=LINE, r=0.14)
        text(s, x + 0.22, y + 0.18, 1.9, 0.6, b, size=24, color=INK, bold=True)
        text(s, x + 0.22, y + 0.78, 1.8, 0.55, t, size=9, color=MUTED)
    text(s, 8.2, 5.15, 4.5, 0.4, 'Team members’ project experience, much of it as developers at a previous organization.', size=8, color=MUTED)
    box(s, 0.6, 5.75, 12.1, 1.15, fill=SOFT, r=0.14)
    text(s, 0.9, 5.88, 11.6, 0.3, 'WE WILL TELL YOU EARLY WHEN', size=8.5, color=BLUE, bold=True)
    text(s, 0.9, 6.18, 11.6, 0.6, 'A standard Zoho feature already does the job · Zoho is the wrong platform for it · The deadline or scope does not fit the budget, before any money is spent', size=10.5, color=INK, spacing=1.2)

    # 3 · Services
    s = prs.slides.add_slide(blank)
    frame(s, img, 3, 'Services')
    heading(s, 'Services', 'Ten services, hire one or combine them', 'hire one or combine them', size=26, w=12)
    svcs = (('Zoho Creator development', 'Custom apps, portals, approvals, dashboards'), ('Zoho CRM implementation', 'Pipelines, Blueprint, assignment, migration'),
            ('Deluge development', 'Functions, schedules, webhooks, script repairs'), ('Integrations', 'APIs, webhooks, Zoho Flow, middleware'),
            ('Zoho suite setup', 'Zoho One, Books, Inventory, Desk, Analytics'), ('Data migration', 'Mapping, deduplication, trial import, counts'),
            ('Process automation', 'Approvals, reminders, quote-to-invoice'), ('AI automation', 'Zia, or Claude and ChatGPT via Zoho MCP'),
            ('Custom software', 'PHP, Laravel, Node.js web apps and tools'), ('Support and maintenance', 'Fixes, changes, monthly change log'))
    for i, (h, t) in enumerate(svcs):
        col, row = i % 2, i // 2
        x, y = 0.6 + col * 6.1, 2.0 + row * 0.98
        box(s, x, y, 5.95, 0.85, fill='FFFFFF', line=LINE, r=0.12)
        box(s, x + 0.2, y + 0.2, 0.45, 0.45, fill=BLUE_BG, r=0.1)
        text(s, x + 0.2, y + 0.2, 0.45, 0.45, f'{i + 1:02d}', size=10, color=BLUE, bold=True, align='c', anchor='m')
        text(s, x + 0.85, y + 0.12, 4.9, 0.35, h, size=12, color=INK, bold=True)
        text(s, x + 0.85, y + 0.45, 4.9, 0.35, t, size=9.5, color=MUTED)

    # 4 · Ways to work together
    s = prs.slides.add_slide(blank)
    frame(s, img, 4, 'Ways to work together')
    heading(s, 'Ways to work together', 'Three ways to contract, all through Upwork', 'all through Upwork', size=26, w=12)
    ways = (('FIXED PRICE', 'Milestones', 'Each milestone has a written deliverable. You fund it, we deliver, you review and release it. The next starts only after you approve.', 'New apps, CRM rollouts, migrations, integrations'),
            ('HOURLY', 'Tracked time', 'Logged with the Upwork desktop app and shown in your Work Diary. You set a weekly limit and see the hours before billing.', 'Fixes, investigations, unclear scope'),
            ('ONGOING', 'Support block', 'An hourly contract with a weekly limit, or a fixed monthly milestone for an agreed number of hours.', 'Keeping a live system healthy'))
    for i, (k, h, t, best) in enumerate(ways):
        x = 0.6 + i * 4.07
        box(s, x, 2.0, 3.9, 3.0, fill='FFFFFF', line=LINE, r=0.16)
        text(s, x + 0.3, 2.25, 3.3, 0.3, k, size=9, color=BLUE, bold=True)
        text(s, x + 0.3, 2.55, 3.3, 0.45, h, size=16, color=INK, bold=True)
        text(s, x + 0.3, 3.05, 3.3, 1.3, t, size=10, color=BODY, spacing=1.2)
        text(s, x + 0.3, 4.35, 3.3, 0.55, [[('Best for: ', {'bold': True, 'color': INK}), (best, {})]], size=9.5, color=BODY)
    box(s, 0.6, 5.3, 12.1, 1.6, fill=NAVY, r=0.16)
    text(s, 0.95, 5.48, 11.4, 0.35, 'Good first milestones', size=13, color='FFFFFF', bold=True)
    text(s, 0.95, 5.9, 11.4, 0.9, 'A review and written scope  ·  Fix one broken automation or sync  ·  One process built end to end  ·  A clickable prototype with sample data.  Scope changes become new milestones only after you approve them.', size=10.5, color='C9D5E6', spacing=1.25)

    # 5 · How a project runs
    s = prs.slides.add_slide(blank)
    frame(s, img, 5, 'How a project runs')
    heading(s, 'How a project runs', 'Six steps, with your sign-off between each', 'your sign-off', size=26, w=12)
    steps = (('Understand', 'The process, who does what, where it breaks'), ('Scope and plan', 'Written scope and milestones to approve'),
             ('Build safely', 'In a sandbox or test copy, not on live data'), ('Demo and adjust', 'Recorded demos at each milestone'),
             ('Test and go live', 'Written test cases, your sign-off, a way back'), ('Hand over', 'Docs, training, one free month of support'))
    box(s, 0.95, 2.43, 10.9, 0.025, fill=LINE)
    for i, (h, t) in enumerate(steps):
        x = 0.6 + i * 2.05
        last = i == len(steps) - 1
        oval(s, x, 2.1, 0.68, GREEN if last else 'FFFFFF', None if last else BLUE)
        text(s, x, 2.1, 0.68, 0.68, str(i + 1), size=15, color='FFFFFF' if last else BLUE, bold=True, align='c', anchor='m')
        text(s, x, 2.95, 1.9, 0.35, h, size=12, color=INK, bold=True)
        text(s, x, 3.3, 1.9, 0.8, t, size=9.5, color=MUTED, spacing=1.15)
    lw, lh = fit(img['lanes'], 12.1, 2.55)
    pic(s, img['lanes'], 0.6 + (12.1 - lw) / 2, 4.35, lw, lh)

    # 6 · Communication and reporting
    s = prs.slides.add_slide(blank)
    frame(s, img, 6, 'Communication and reporting')
    heading(s, 'Communication and reporting', 'You always know where the work stands', 'where the work stands', size=26, w=12)
    rules = ['One channel: Upwork Messages for questions, files, decisions and calls', 'Reply within 6 hours on working days, guaranteed',
             'A written update every week, even when the week was quiet', 'Recorded demos at the end of each milestone',
             'A regular call window agreed in your working hours', 'Delays and cost changes flagged early, with options']
    dot_list(s, 0.6, 2.1, 6.0, rules, size=11, gap=0.6)
    box(s, 7.0, 2.0, 5.7, 4.85, fill='FFFFFF', line=LINE, r=0.16)
    box(s, 7.0, 2.0, 5.7, 0.5, fill=SOFT, r=0.16)
    text(s, 7.3, 2.0, 3.5, 0.5, 'Weekly update · Week 3', size=10.5, color=INK, bold=True, anchor='m')
    text(s, 10.7, 2.0, 1.8, 0.5, 'Example format', size=8.5, color=MUTED, align='r', anchor='m')
    blocks = (('DONE THIS WEEK', 'Quote layout and approval Blueprint in the sandbox; deal-to-invoice function tested with 12 sample deals'),
              ('NEXT WEEK', 'Recorded demo of milestone 2 on Tuesday; start the Books payment sync'),
              ('NEEDS YOUR DECISION', 'Should discounts over 15% need manager approval?'),
              ('TIME AND BUDGET', 'Milestone 2 on track. Hourly items: 3.5 hours, in your Work Diary'))
    for i, (k, v) in enumerate(blocks):
        y = 2.7 + i * 1.02
        text(s, 7.3, y, 5.1, 0.28, k, size=8.5, color=BLUE, bold=True)
        text(s, 7.3, y + 0.28, 5.1, 0.7, v, size=10, color=BODY, spacing=1.15)

    # 7 · Access, security and handover
    s = prs.slides.add_slide(blank)
    frame(s, img, 7, 'Access, security and handover')
    heading(s, 'Access, security and handover', 'Your system, your data, your ownership', 'your ownership', size=26, w=12)
    cols = (('Access and security', ['A separate user with only the permissions needed', 'Sandbox or test copy wherever Zoho allows', 'No live changes without your approval', 'No passwords in chat; you invite our user', 'NDA on request; access removed at the end']),
            ('Ownership and quality', ['Everything is yours once paid, per Upwork’s terms', 'Zoho licences in your name; code in your repo', 'Written test cases and your sign-off', 'A rollback plan for every live change', 'No lock-in: anyone can take over from the docs']),
            ('The handover pack', ['Admin guide', 'Field and workflow list', 'Commented Deluge functions', 'Integration notes and failure alerts', 'Live training plus short recordings']))
    for i, (h, items) in enumerate(cols):
        x = 0.6 + i * 4.07
        box(s, x, 2.0, 3.9, 4.85, fill=SOFT if i == 2 else 'FFFFFF', line=None if i == 2 else LINE, r=0.16)
        text(s, x + 0.3, 2.22, 3.4, 0.4, h, size=13, color=INK, bold=True)
        dot_list(s, x + 0.3, 2.8, 3.4, items, size=10, gap=0.72, dot=BLUE if i == 2 else GREEN)

    # 8 · Who you work with and next step
    s = prs.slides.add_slide(blank)
    box(s, 0, 0, W, H, fill=NAVY)
    pic(s, img['logo'], 0.6, 0.5, 0.42, 0.42)
    text(s, 1.12, 0.5, 3, 0.42, 'Zudo Works', size=14, color='FFFFFF', bold=True, anchor='m')
    text(s, W - 3.6, 0.5, 3, 0.42, f'{TOTAL:02d} / {TOTAL:02d}', size=9, color='8597B2', bold=True, align='r', anchor='m')
    heading(s, 'Next step', 'Reply to our proposal here on Upwork', None, y=1.3, size=30, color='FFFFFF', kcolor=SKY)
    for i, (h, t) in enumerate((('Tell us the process', 'What you want to change, in a few lines.'),
                                 ('Your setup', 'Which Zoho apps and edition, and what else is involved.'),
                                 ('Your timing', 'The deadline and anything it depends on.'))):
        x = 0.6 + i * 2.5
        box(s, x, 2.6, 2.35, 1.6, fill=NAVY2, r=0.14)
        oval(s, x + 0.25, 2.8, 0.36, GREEN)
        text(s, x + 0.25, 2.8, 0.36, 0.36, str(i + 1), size=11, color='FFFFFF', bold=True, align='c', anchor='m')
        text(s, x + 0.25, 3.28, 1.95, 0.35, h, size=11, color='FFFFFF', bold=True)
        text(s, x + 0.25, 3.62, 1.95, 0.55, t, size=9, color='C9D5E6', spacing=1.15)
    text(s, 0.6, 4.5, 7.4, 0.6, 'We reply within 6 hours with questions or a suggested first milestone. A review or a single fix is a good way to start, with no commitment to anything larger.', size=12, color='C9D5E6', spacing=1.25)
    x0 = 8.45
    box(s, x0, 1.3, W - 0.6 - x0, 5.55, fill=NAVY2, r=0.2)
    pic_fill(s, img['cto'], x0 + 0.35, 1.65, W - 0.6 - x0 - 0.7, 2.7, focus=0.3)
    text(s, x0 + 0.35, 4.5, 4, 0.35, 'Arunkumar V', size=16, color='FFFFFF', bold=True)
    text(s, x0 + 0.35, 4.85, 4, 0.3, 'Chief Technology Officer', size=10, color=SKY, bold=True)
    text(s, x0 + 0.35, 5.25, W - 0.6 - x0 - 0.7, 0.7, '“Master of Creator (Global Winner)” award, Zoho Creator Partner Hackathon 2025', size=10, color='FFFFFF', spacing=1.15)
    text(s, x0 + 0.35, 5.95, W - 0.6 - x0 - 0.7, 0.7, 'Scopes and builds your project. You talk to the people who do the work.', size=9, color='C9D5E6', spacing=1.15)

    prs.save(path)
    return len(prs.slides)
