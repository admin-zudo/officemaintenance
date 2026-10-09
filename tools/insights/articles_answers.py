# Two-to-three sentence answers shown at the top of each article (featured snippets, AI answers).
ANSWERS = {
    'zoho-creator-vs-power-apps':
        'Choose Zoho Creator if you already use Zoho apps and want the database, logic, portals and mobile apps in one '
        'product with per-user pricing. Choose Power Apps if your business runs on Microsoft 365 and your data already '
        'lives in SharePoint, Dataverse or SQL Server. The deciding factors are where your data lives, who uses the app '
        'and which licences each option needs.',
    'migrate-hubspot-salesforce-to-zoho-crm':
        'Map objects and fields first, create users and picklists in Zoho CRM, add a legacy ID field to every module, '
        'then import in order: accounts, contacts, leads, deals, activities and attachments. Automations do not '
        'migrate, so rebuild the ones you still need. A small, clean migration takes two to four weeks.',
    'zoho-crm-implementation-cost':
        'A Zoho CRM implementation typically takes 40 to 70 hours for a small starter setup, 100 to 180 hours for a '
        'standard rollout and 200 to 400 hours for an advanced multi-team project. At US$15 per hour that is roughly '
        'US$600 to US$6,000, plus Zoho licence fees paid directly to Zoho.',
    'deluge-script-examples':
        'Deluge is Zoho\'s scripting language for automating CRM, Creator, Books and other Zoho apps. The most useful '
        'scripts create invoices from won deals, flag duplicate records, create follow-up tasks, send scheduled '
        'reminders and call external APIs with invokeurl. All ten examples below are patterns from real projects.',
    'zoho-agentic-ai-hyperautomation':
        'AI in Zoho CRM is most useful today for summaries, drafting emails, data clean-up and prioritizing leads and '
        'deals. Actions involving money, customer commitments, deletions or key stage changes should stay rule-based '
        'or human-approved. Clean data, a defined process and clear permissions matter more than the AI model.',
    'zoho-analytics-agentic-data-foundations-2026':
        'To get reliable dashboards and AI answers from Zoho Analytics, connect sources with native connectors, join '
        'tables on a shared customer ID, clean data where it is created, and define key metrics once as query tables. '
        'Only then rely on Ask Zia, and check its answers against a trusted report.',
    'zoho-partner-software-development':
        'You do not need an official Zoho Partner to implement Zoho; you need relevant, demonstrable experience. Ask '
        'to see similar projects, who will do the work, how data migration and testing are handled, and what is '
        'documented. Keep the Zoho account in your own name and agree support after launch in writing.',
    'zoho-partner-program-explained':
        'A Zoho partner is a company in Zoho\'s official partner program, ranked in three tiers: Authorized, Advanced '
        'and Premium. Authorized partners have met a US$5,000 revenue threshold plus certification and project-success '
        'requirements; Advanced and Premium partners score above 400 and 600 points out of 1,000. Verify any partner '
        'in Zoho\'s Find a Partner directory.',
    'zoho-crm-vs-hubspot':
        'Choose Zoho CRM if sales, operations and finance need to share customer data, you want to customize the '
        'system around your process and you want predictable per-user pricing. Choose HubSpot if marketing leads the '
        'business and you want website, email and CRM in one product. The biggest cost difference appears at '
        'HubSpot\'s Professional tier, which adds a higher seat price and a required onboarding fee.',
    'zoho-mcp-claude-chatgpt':
        'Zoho MCP lets an AI assistant such as Claude or ChatGPT use tools in your Zoho apps. Create a server in the '
        'Zoho MCP console, add only the tools you need, copy the MCP URL into your assistant and authorize with your '
        'Zoho account. Start with read-only tools, keep each user on their own authorization, and require '
        'confirmation before any change.',
    'zoho-for-manufacturing':
        'Zoho offers a manufacturer three routes. Zoho Inventory handles simple assembly but has no manufacturing '
        'module. Zoho ERP, launched in India in January 2026 and sold separately from Zoho One, has bills of '
        'materials, manufacturing orders, job cards, work centers, subcontracting and quality checks. Zoho Creator '
        'is for custom production apps built around your own process.',
    'zoho-flow-vs-deluge':
        'Use Zoho Flow for simple app-to-app automation with a few steps; it is metered by tasks, and each action '
        'in a flow counts as one. Use Deluge when the logic runs inside one Zoho app and must act at an exact point '
        'in a process. Use custom middleware for high volume, long-running jobs, retries or two-way sync.',
}
