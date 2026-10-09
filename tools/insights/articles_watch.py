# Review notes per article. insights_gen.py copies these into blog/.automation-history.json, which is the
# index an automated run reads first, so it does not need to open every article.
#
#   checked     date the facts were last verified against the sources ('' = never verified by a review run)
#   volatility  how quickly the facts go out of date: 'high' re-check after 14 days, 'medium' 45, 'low' 120
#   facts       the specific claims that can expire or change
#   sources     where to verify them
WATCH = {
    'zoho-crm-vs-hubspot': dict(
        checked='2026-10-09', volatility='high',
        facts=['Zoho CRM free edition: up to 3 users', 'HubSpot free tools: up to 2 users',
               'HubSpot Professional and Enterprise have a required one-time onboarding fee',
               'HubSpot Marketing Hub price depends on marketing contacts',
               'Sequences not in HubSpot Free or Starter; Starter workflows limited',
               'Zoho CRM: Blueprint from Professional; Zia and sandbox from Enterprise'],
        sources=['https://www.zoho.com/crm/zohocrm-pricing.html', 'https://www.zoho.com/crm/comparison.html',
                 'https://www.hubspot.com/pricing/sales', 'https://www.hubspot.com/pricing/marketing']),
    'zoho-mcp-claude-chatgpt': dict(
        checked='2026-10-09', volatility='high',
        facts=['Zoho MCP is free to use for now', 'MCP calls follow each app\'s normal API limits',
               'Two modes: Authorize on Demand, Authorize via Connections (Super Admin only)',
               'Logs kept 30 days', 'About 100 tools per server recommended, 300 maximum',
               'Claude custom connectors: Pro, Max, Team, Enterprise; Owners add on Team and Enterprise',
               'ChatGPT write actions in beta on Business, Enterprise, Edu; Pro read and fetch only',
               'Zoho CRM publishes four ready-made MCP servers', 'Menu names in the six setup steps'],
        sources=['https://www.zoho.com/mcp/', 'https://help.zoho.com/portal/en/kb/mcp/help-support/articles/zoho-mcp-faq',
                 'https://help.zoho.com/portal/en/kb/mcp/implementation-guide/articles/zoho-mcp-implementation-guide',
                 'https://www.zoho.com/crm/developer/docs/mcp/setup/claude.html',
                 'https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp',
                 'https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt']),
    'zoho-creator-vs-power-apps': dict(
        checked='', volatility='medium',
        facts=['Power Apps licensing: premium connectors, Dataverse and Power Pages need extra licences',
               'Zoho Creator plans include database, Deluge, portals and mobile apps; Creator is in Zoho One'],
        sources=['https://www.zoho.com/creator/pricing.html',
                 'https://www.microsoft.com/en-us/power-platform/products/power-apps/pricing']),
    'migrate-hubspot-salesforce-to-zoho-crm': dict(
        checked='', volatility='low',
        facts=['Import order and migration steps in Zoho CRM', 'Typical duration: two to four weeks for a small migration'],
        sources=['https://help.zoho.com/portal/en/kb/crm']),
    'zoho-crm-implementation-cost': dict(
        checked='', volatility='medium',
        facts=['Zudo Works rate of US$15 per hour (confirm with Arunkumar if it changes)',
               'Hour ranges for starter, standard and advanced projects', 'Zoho CRM edition names'],
        sources=['https://www.zoho.com/crm/zohocrm-pricing.html', '/pricing/']),
    'deluge-script-examples': dict(
        checked='', volatility='low',
        facts=['Deluge task names and syntax used in the ten examples'],
        sources=['https://www.zoho.com/deluge/help/']),
    'zoho-agentic-ai-hyperautomation': dict(
        checked='', volatility='high',
        facts=['Zia features by edition', 'Zia LLM, Zia Agents and Agent Studio: availability by product and region',
               'Support for third-party models in Zia'],
        sources=['https://www.zoho.com/zia/', 'https://www.zoho.com/crm/zia.html']),
    'zoho-analytics-agentic-data-foundations-2026': dict(
        checked='', volatility='medium',
        facts=['Zoho Analytics connectors and sync frequency by plan', 'Ask Zia capabilities'],
        sources=['https://www.zoho.com/analytics/']),
    'zoho-partner-software-development': dict(
        checked='', volatility='low',
        facts=['Advice only; few facts that expire'],
        sources=[]),
    'zoho-partner-program-explained': dict(
        checked='', volatility='high',
        facts=['Partner tiers: Authorized, Advanced, Premium', 'US$5,000 revenue threshold for Authorized',
               'Advanced above 400 points and Premium above 600 points out of 1,000',
               'Zudo Works\' own partner status (update the wording once it is approved)'],
        sources=['https://www.zoho.com/partners/', 'https://www.zoho.com/partners/find-partner.html']),
}
