const fs = require('fs');
const path = require('path');

const posts = [
  {
    "id": "zoho-crm-guide",
    "title": "Getting Started with Zoho CRM: A Practical Implementation Guide",
    "category": "Zoho",
    "date": "Aug 15, 2026",
    "author": "Zudo Works Team",
    "excerpt": "A step-by-step walkthrough for businesses implementing Zoho CRM for the first time, covering setup, data migration, customization, automation, and team adoption strategies that actually work.",
    "file": "zoho-crm-guide.html"
  },
  {
    "id": "integration-mistakes",
    "title": "5 Integration Mistakes That Cost Businesses Time and Money",
    "category": "Integrations",
    "date": "Aug 8, 2026",
    "author": "Zudo Works Team",
    "excerpt": "Common pitfalls in system integration projects and how to avoid them. From scope creep and data mapping errors to testing gaps, learn from real implementation experience.",
    "file": "integration-mistakes.html"
  },
  {
    "id": "automation-processes",
    "title": "How to Identify Which Business Processes to Automate First",
    "category": "Automation",
    "date": "Aug 1, 2026",
    "author": "Zudo Works Team",
    "excerpt": "A practical framework for prioritizing automation opportunities based on impact, complexity, and ROI — with real examples from Zoho and custom implementations.",
    "file": "automation-processes.html"
  },
  {
    "id": "zoho-one-comparison",
    "title": "Zoho One vs. Individual Zoho Products: Which Approach Is Right for Your Business?",
    "category": "Zoho",
    "date": "Jul 25, 2026",
    "author": "Zudo Works Team",
    "excerpt": "A comparison of the Zoho One bundle versus purchasing individual Zoho products, with guidance on when each option makes financial and operational sense.",
    "file": "zoho-one-comparison.html"
  },
  {
    "id": "custom-software",
    "title": "When to Build Custom Software vs. Using Off-the-Shelf Solutions",
    "category": "Development",
    "date": "Jul 18, 2026",
    "author": "Zudo Works Team",
    "excerpt": "A decision framework for business leaders evaluating whether to invest in custom software development or adopt and customize an existing platform like Zoho.",
    "file": "custom-software.html"
  },
  {
    "id": "cost-of-not-digitizing",
    "title": "The Real Cost of Not Digitizing: What Manual Processes Are Costing Your Business",
    "category": "Digital Transformation",
    "date": "Jul 10, 2026",
    "author": "Zudo Works Team",
    "excerpt": "An analysis of the hidden costs of manual business processes — from wasted employee hours and data entry errors to missed opportunities and compliance risk.",
    "file": "cost-of-not-digitizing.html"
  }
];

const templateHtml = fs.readFileSync(path.join(__dirname, 'blog', 'index.html'), 'utf-8');

// Find the parts to split the template
const splitStart = templateHtml.indexOf('<section class="page-hero">');
const splitEnd = templateHtml.indexOf('<section class="cta-banner">');

if (splitStart === -1 || splitEnd === -1) {
    console.error("Could not find split points in index.html");
    process.exit(1);
}

const headerPart = templateHtml.substring(0, splitStart);
const footerPart = templateHtml.substring(splitEnd);

posts.forEach(post => {
    const postContent = `
    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="/">Home</a><span class="breadcrumb-sep" aria-hidden="true">/</span>
            <a href="/blog/">Blog</a><span class="breadcrumb-sep" aria-hidden="true">/</span>
            <span class="breadcrumb-current" aria-current="page">${post.title}</span>
        </nav>
        <span class="badge badge-primary" style="margin-bottom: var(--space-4);">${post.category}</span>
        <h1>${post.title}</h1>
        <p style="margin-bottom: var(--space-4);">${post.excerpt}</p>
        <div style="font-size: var(--text-sm); color: var(--color-muted);">By ${post.author} &bull; ${post.date}</div>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <div class="prose">
            <p>This is the full content for <strong>${post.file}</strong>. In a real scenario, this file would contain the complete article text.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            <h2>Key Takeaways</h2>
            <ul>
                <li>Important point 1</li>
                <li>Important point 2</li>
                <li>Important point 3</li>
            </ul>
            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
      </div>
    </section>
    `;

    const fullHtml = headerPart + postContent + footerPart;
    fs.writeFileSync(path.join(__dirname, 'blog', post.file), fullHtml);
    console.log(`Generated ${post.file}`);
});
