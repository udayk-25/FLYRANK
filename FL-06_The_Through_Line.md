# FL-06: The Through-Line
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 3)  
**Date:** July 18, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. One-Line Claim

This is the single sentence that greets a visitor and summarizes what the portfolio proves:

> **"I build responsive, transactionally reliable web applications that load in under 2 seconds and achieve 100% unit test path coverage."**

---

## 2. Portfolio Content Map

This map outlines the structure of the three-page portfolio, listing ordered sections, their corresponding case studies, and their calls to action (which all ladder up to booking an introductory call).

### Page 1: Landing Page (The Entrypoint)
*   **Section 1: Hero Header**  
    *   *Content*: The one-line claim, a short sub-headline introducing Uday as a high-performance full-stack engineer, and a prominent CTA button.  
    *   *Visuals*: Quiet geometric background (`hero_geometric_bg.png`) and modern monogram logo.
*   **Section 2: Work (Featured Case Previews)**  
    *   *Content*: Visual cards linking to the detailed case studies. Lead with the **Farmer Trade System** (strongest engineering proof), followed by the **Search Intelligence ML Pipeline**.
*   **Section 3: About (Bio & Profile Card)**  
    *   *Content*: Brief professional bio card, a clean profile photo (`uday_headshot.jpg`), and a set of core skill badges (Node.js, SQLite, Jest, Python, Random Forest).
*   **Section 4: Booking Scheduler**  
    *   *Content*: An embedded interactive calendar scheduling widget (Cal.com / Calendly mockup) allowing the visitor to reserve a slot.
*   **Page CTA (The One Action)**:  
    *   > **"Select a time on the calendar below to book a 15-minute introductory call."**

---

### Page 2: Case Study Details (Farmer Trade System)
*   **Section 1: Hero Title**  
    *   *Content*: *"Farmer Trade System: Zero-Failure Agricultural Marketplace"* with links to the public code repository.
*   **Section 2: The Problem (Beat 1)**  
    *   *Content*: Explaining the trust and speed barriers in local agricultural trading, and why transaction failures destroy marketplace adoption.
*   **Section 3: What I Did (Beat 2)**  
    *   *Content*: Engineering decisions detailing how I built the platform with Node.js and vanilla CSS, bypassed heavy frameworks to keep load times under 2 seconds, and mocked database layers to achieve 100% unit test path coverage.
*   **Section 4: Outcome & Proof (Beat 3)**  
    *   *Content*: Highlight the metrics (sub-2s load time and 100% coverage). Show the terminal test suite run.
*   **Page CTA**:  
    *   > **"Verify the code quality yourself: [Review the GitHub Repository] or [Back to Landing to Schedule a Call]."**

---

### Page 3: Case Study Details (Search Intelligence ML Pipeline)
*   **Section 1: Hero Title**  
    *   *Content*: *"Search Intelligence: Prioritizing Content Refresh Opportunities"* with links to the client data notebook.
*   **Section 2: The Problem (Beat 1)**  
    *   *Content*: Large content inventories lose organic search visibility due to silent decay, wasting hundreds of editorial hours reviewing stable pages.
*   **Section 3: What I Did (Beat 2)**  
    *   *Content*: Built a Random Forest model on 30k pages. I decided to optimize for **Precision@50** to match real-world editor capacity, rather than generic classification accuracy.
*   **Section 4: Outcome & Proof (Beat 3)**  
    *   *Content*: Show that the model achieved 74% Precision@50 (beating the 24% baseline rule by 3x). Show the Python-generated feature importance SVG plot.
*   **Page CTA**:  
    *   > **"Review the ML framing notebook: [View w02_ml_task_framing.ipynb] or [Back to Landing to Schedule a Call]."**

---

## 3. "Still Need to Gather" Checklist

To prevent delays during build week, here is the checklist of assets and proofs still being finalized:

- [ ] **Farmer Trade System Application**:
  - [ ] Finalize the public Git repository link (`https://github.com/udayk-25/farmer-trade-system`).
  - [ ] Deploy the app live to Render/Vercel and retrieve the live link.
  - [ ] Take a clean, cropped screenshot of the terminal displaying the Jest Jest test run showing 100% test path coverage.
- [ ] **ML Internship Pipeline**:
  - [ ] Collect final precision and validation metrics from the full warehouse CSV release (Week 3 to Week 7).
  - [ ] Take a clean capture of the Matplotlib/Seaborn model evaluation graphs.
- [ ] **Identity & Profile**:
  - [ ] Retrieve a clean, cropped, professional headshot photo (`docs/images/uday_headshot.jpg`).
  - [ ] Set up the Cal.com or Calendly account and retrieve the booking link.

---
*End of Report*
