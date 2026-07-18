# FL-08: Three Roads — Choosing Your Stack
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 4)  
**Date:** July 18, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Context and Constraints

To build a high-performance portfolio website that aligns with my brand identity and showcases my engineering work, I evaluated my options under four strict constraints:

1.  **Cost**: Free only (including hosting, subdomain registration, and third-party widgets).
2.  **Honest Skill Level**: Strong backend logic (Node.js, Express, SQL, Python, ML modeling) and moderate frontend layout skills (HTML5, CSS3, ES6 JavaScript).
3.  **Portfolio Goals**: Needs to serve the sitemap content map (Landing, Farmer Trade System details, and Search Intelligence ML Pipeline details) with an embedded Cal.com booking scheduler.
4.  **Work Display Requirements**: Needs to display inline SVG vector logos, code snippets with syntax highlighting, visual SVG data charts, and terminal test log screenshots.
5.  **Dynamic Requirement**: Currently, there are **no dynamic database backend requirements** for the portfolio site itself. The model predictions and trade dashboards are showcased via static visual assets, raw code, and embedded cal.com widget interactions. Thus, a backend is **not yet** necessary.

---

## 2. The Three Roads (Options)

I compared three stack paths representing different levels of complexity:

| Dimension | Option 1: Simplest (No-Code Builder) | Option 2: The Middle Road (Vanilla HTML/CSS/JS) | Option 3: Most Powerful (React / Next.js) |
| :--- | :--- | :--- | :--- |
| **Technology** | **Carrd** (Free Subdomain tier) | **Vanilla HTML5, CSS3, ES6 JavaScript** | **Next.js Framework** (React, TailwindCSS) |
| **Hosting (Free)**| Carrd subdomain (`name.carrd.co`) | **GitHub Pages** (`username.github.io/repo`) | **Vercel** (`name.vercel.app`) |
| **Backend Need**  | None | **None** | None (except optional Serverless functions) |
| **REAL Trade-off**| Immediate drag-and-drop design, but zero control over custom CSS variables, raw code files, or SVG monogram logo rendering. | **100% control over design variables, fonts, and inline SVGs. Zero compile overhead, but requires manual header/footer duplication.** | Highly modular component reuse, but introduces huge package dependencies (`node_modules`), complex build scripts, and larger bundle sizes. |

---

## 3. Pressure-Testing the Options

### What breaks if I pick the Simplest (Option 1 - Carrd)?
Choosing Carrd breaks my ability to implement the **FL-04 Identity Kit**. I cannot control custom root CSS variables, embed raw SVG files cleanly, or display code files with syntax highlighting on the free tier. It looks like a generic marketing landing page, which contradicts my claim of building "responsive, transactionally reliable web applications."

### What do I maintain if I pick the Most Powerful (Option 3 - Next.js)?
Choosing Next.js introduces a large compile and maintenance burden over time. I must maintain NPM dependencies, resolve potential security alerts in sub-dependencies, and manage Vercel deployment logs. A simple three-page portfolio does not justify the complexity of a React rendering lifecycle or a Webpack/Turbopack bundler.

### Can I finish this build in two weeks?
Yes. Hand-coding three static HTML/CSS files takes less than a week. Bypassing framework configuration, routing packages, and bundler troubleshooting means I can focus 100% on the copy, design layouts, and asset verification.

---

## 4. Final Decision and Rationale

### Chosen Stack: Option 2 (Vanilla HTML5 / CSS3 / ES6 JS)
I decided to build my portfolio using a **Vanilla HTML/CSS/JS stack hosted on GitHub Pages**.

### Why I Rejected the Alternatives:
1.  **Why I rejected Carrd (Option 1)**: It lacks the control needed to display my code assets and custom branding. It makes me look like a non-technical marketer rather than an engineer.
2.  **Why I rejected Next.js (Option 3)**: It introduces unnecessary build dependencies, config complexity, and bundle bloat. A major goal of my sitemap claim is that pages load in under 2 seconds. Vanilla HTML/CSS guarantees this performance out of the box with zero runtime overhead.

### Can I maintain this?
Absolutely. Since there are **no compile steps, node packages, or databases**, this site has **zero maintenance overhead**. I can open these raw files in any editor five years from now, and they will run instantly in any browser. It perfectly fits my skill level and displays my code and charts with maximum credibility.

---
*End of Report*
