# FL-02: Frame it as Cases
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 2)  
**Date:** July 18, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Standing Instruction Voice Card
*Standing instructions added to the Claude Project configuration to control tone and formatting.*

> **"Direct, plain, precise, no corporate buzzwords."**

---

## 2. Case Studies (Three-Beat Format)

### Case Study A: The Farmer Trade System
* **Beat 1: The Problem**  
  Smallholder farmers struggle to find transparent prices and reliable buyers for their produce, while commercial buyers face unpredictable supply chains. Existing digital marketplaces are slow, bloated, and prone to transaction failures, preventing local users from trusting online trade.
* **Beat 2: What I Did (and Decided)**  
  I built the Farmer Trade System, a modular digital marketplace using Node.js and vanilla CSS. I decided against heavy CSS frameworks to ensure page load times remain under 2 seconds, even on low-bandwidth rural connections. I also wrote complete mocks and stubs to achieve 100% unit test path coverage for all payment and trade-execution endpoints.
* **Beat 3: What Came of It**  
  A blazing-fast, transactionally reliable trading application. The live test suite passes on the first run, proving the code works exactly as claimed. The entire codebase is public, allowing the hiring manager to run the tests and verify the sub-2-second load speed directly.

---

### Case Study B: Search Intelligence ML Pipeline
* **Beat 1: The Problem**  
  Search traffic decay is a silent killer for large web properties, but manually auditing thousands of pages to identify content refresh opportunities wastes hundreds of hours of editor review time on pages that are stable or growing.
* **Beat 2: What I Did (and Decided)**  
  I integrated an ML pipeline locally and trained a Random Forest model on 30,000 rows of anonymized search data. I chose to evaluate the model using **Precision@50** (of the top 50 pages flagged, what fraction are actually declining) to match the real-world editor review capacity, rather than optimizing for generic classification accuracy.
* **Beat 3: What Came of It**  
  A prioritized content refresh queue that achieved 74% Precision@50, beating the handwritten rule baseline (24% precision) by roughly 3x, and saving the client's editorial team from checking stable pages.

---

## 3. Bio & Contact Copy

### Bio
> **"I am a full-stack engineer who builds high-performance web applications. I believe code should be verified by test coverage, page loads should feel instantaneous, and machine learning should serve concrete operational decisions."**

### Contact/CTA
> **"Let's build something fast. Use the scheduler below to book a 15-minute introductory call."**

---

## 4. Copy Comparison (Before / After)

To illustrate the difference between generic AI-generated corporate copy and edited, evidence-backed claims, see the comparison below:

* **Generic AI Line (Before)**:  
  *"I am a highly motivated, results-driven software engineer who leverages cutting-edge technology and state-of-the-art machine learning models to optimize website performance and deliver high-impact solutions for businesses."*
* **Edited Version (After)**:  
  *"I build responsive, AI-integrated agricultural trading applications that load in under 2 seconds and achieve 100% unit test path coverage."*

---
*End of Report*
