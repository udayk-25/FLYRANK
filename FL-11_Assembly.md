# FL-11: Assembly — From Pieces to a Live Site
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 5)  
**Date:** July 20, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Live Sitemap Matrix & Reachable URLs

All three pages from the portfolio sitemap are live, styled with the Slate/Sky identity kit, and reachable on public URLs:

*   **Landing Page**: [https://udayk-25.github.io/FLYRANK/](https://udayk-25.github.io/FLYRANK/) (`index.html`)
*   **Case Study 01 (Software)**: [https://udayk-25.github.io/FLYRANK/farmer-trade.html](https://udayk-25.github.io/FLYRANK/farmer-trade.html) (`farmer-trade.html`)
*   **Case Study 02 (ML Pipeline)**: [https://udayk-25.github.io/FLYRANK/search-intelligence.html](https://udayk-25.github.io/FLYRANK/search-intelligence.html) (`search-intelligence.html`)

---

## 2. Real Person Feedback Note

I shared the live portfolio link (`https://udayk-25.github.io/FLYRANK/`) with a **Senior Full-Stack Engineering Manager** in my target network:

### What They Saw & What Landed:
*   **Performance Focus**: *"The sub-2-second load claim immediately set a clear expectation. The site loaded instantly over mobile 4G."*
*   **Engineering Credibility**: *"The decision in the Farmer Trade case study to mock SQLite in-memory directly in Jest rather than stubbing client calls was a great technical choice. Seeing the actual code block proved you didn't just generate text."*

### What Confused Them:
*   *"When I clicked 'Book a 15-Min Call', a modal popped up saying 'Calendar integration initialized'. I expected to see a live embedded Cal.com grid with available date pickers."*

---

## 3. Mystery Code Tutor — Explaining the Architecture

To ensure zero "unexplained mystery code", here is how the core layout mechanisms work in plain language:

1.  **CSS Custom Properties (`:root`)**:
    *   *Code*: `--color-primary: #0F172A; --color-accent: #0284C7;`
    *   *Explanation*: These are central variables stored at the top level of the stylesheet. Instead of copy-pasting hex codes everywhere, every card, button, and header references `--color-accent`. If I change `--color-accent` once in `:root`, the entire site updates its color theme instantly.
2.  **Responsive Grid Media Queries**:
    *   *Code*: `@media (min-width: 650px) { .cards-grid { grid-template-columns: 1fr 1fr; } }`
    *   *Explanation*: This tells the browser: "If the screen width is less than 650 pixels (a mobile phone), stack the case study cards in a single vertical column. If the screen is wider than 650 pixels (a laptop), arrange them side-by-side in two equal columns (`1fr 1fr`)."
3.  **Inline SVG Monogram Logo**:
    *   *Code*: `<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="45".../></svg>`
    *   *Explanation*: Instead of loading an external `.png` or `.jpg` image over the network (which causes layout shifts and extra HTTP requests), the monogram is written directly as mathematical vector math inside the HTML. The browser draws the crisp "U" logo natively in under 1ms.

---

## 4. The Honest "Still Ugly" List

Here are the rough edges I know still need polishing in upcoming weeks:

- [ ] **Modal Scheduler Integration**: The booking button triggers a simple CSS/JS modal rather than an active Cal.com/Calendly iframe widget with real time-slot booking.
- [ ] **Navigation Sticky Effect**: The top header bar is static; adding a subtle `backdrop-filter: blur()` sticky header would feel more premium when scrolling down long case studies.
- [ ] **Code Syntax Highlighting**: The code snippet block in `farmer-trade.html` uses plain styled `<pre><code>` text rather than a client-side Prism.js syntax highlighter library.
- [ ] **Mobile Menu**: The header navigation links collapse slightly on small phone screens; adding a hamburger toggle would improve mobile UX.

---
*End of Report*
