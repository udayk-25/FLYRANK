# FL-04: Brand Identity Kit
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 3)  
**Date:** July 18, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Typography
We use two free fonts imported from Google Fonts, prioritizing geometric shapes and UI clarity:

* **Heading Font**: **Outfit**  
  * *Purpose*: Modern, geometric, geometric sans-serif that gives page headings an intentional, high-performance look.
  * *Import Link*: `<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">`
* **Body Font**: **Inter**  
  * *Purpose*: The industry standard for high-readability UI and paragraphs, optimized for screens and small text sizes.
  * *Import Link*: `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">`

---

## 2. Color Palette
Our slate and sky color scheme ensures that our code and performance data remain the loudest, most readable items on the page:

| Color Role | Color Name | Hex Code | Visual Preview |
| :--- | :--- | :--- | :--- |
| **Primary (Brand)** | Slate 900 | `#0F172A` | Sleek, dark navy/slate for hero headers and prominent cards. |
| **Accent (Highlight)** | Sky 600 | `#0284C7` | Professional blue for links, key metrics, and call-to-action details. |
| **Background** | Stone 50 | `#FAFAFA` | Off-white background to prevent eye strain and feel warm/premium. |
| **Text** | Slate 800 | `#1E293B` | Soft, dark charcoal for high-contrast, highly readable paragraphs. |
| **Muted/Borders** | Slate 200 | `#E2E8F0` | Light gray line borders, dividers, and card outlines. |

---

## 3. Logo Monogram (Inline SVG)
Below is a modern, responsive monogram vector logo representing the initial **"U"** (for Uday). It uses Slate 900 for the main structure and a Sky 600 accent dot, structured on a clean geometric grid:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="80" height="80">
  <!-- Outer border circle -->
  <circle cx="50" cy="50" r="45" fill="none" stroke="#0F172A" stroke-width="6"/>
  <!-- The Monogram U -->
  <path d="M35,30 L35,55 C35,63.28 41.72,70 50,70 C58.28,70 65,63.28 65,55 L65,30" 
        fill="none" stroke="#0F172A" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Sky 600 accent dot inside the U loop -->
  <circle cx="50" cy="52" r="5" fill="#0284C7" />
</svg>
```

---

## 4. Claude Project Standing Instruction
Copy and paste this style note directly into your Claude Project Custom Instructions to enforce brand consistency across all UI code generation tasks:

```markdown
Style Note (Strict UI Rules):
- Fonts: Headings 'Outfit', Body 'Inter' (sans-serif).
- Colors: Primary #0F172A, Accent #0284C7, Bg #FAFAFA, Text #1E293B, Border #E2E8F0.
- Layout: Minimalist, engineering-focused clarity, prioritizing high-readability, large margins, and clean borders.
```

---
*End of Report*
