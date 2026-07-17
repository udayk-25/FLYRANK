# FL-01: AI Workflow Audit & Tool Setup
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 1)  
**Date:** July 16, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Executive Summary

This workflow audit establishes a baseline for integrating AI tools into my daily activities as a software engineer intern at FlyRank. Following the classification framework from Ethan Mollick's *On-boarding your AI Intern*, tasks are divided into four quadrants: **Just Me**, **Collaborate with AI**, **Delegate to AI with Review**, and **Fully Automate**.

The goal is to optimize productivity by offloading repetitive and structured tasks to AI while retaining human ownership of critical, high-risk, and cognitive tasks.

---

## 2. Workflow Audit Table

Below is the classification of 12 recurring tasks from my study, work, and side-project activities.

| # | Task | Classification | One-Line Rationale |
| :--- | :--- | :--- | :--- |
| 1 | **Code review of peer pull requests** | **Just Me** | Requires deep understanding of team conventions, codebase context, and human accountability that cannot be offloaded to AI. |
| 2 | **Learning new programming frameworks (Anthropic Academy, etc.)** | **Just Me** | Learning is a personal cognitive process; while AI can explain concepts, the actual internalizing and understanding must be done by myself. |
| 3 | **Final sign-off on database schema changes** | **Just Me** | High-stakes structural changes require human risk assessment, security evaluation, and long-term maintenance responsibility. |
| 4 | **Writing/editing unit tests for API endpoints** | **Collaborate with AI** | AI excels at generating boilerplate test cases and covering edge cases, but I must define the business rules and mock assertions. |
| 5 | **Translating UI wireframes into HTML/CSS/JS** | **Collaborate with AI** | AI generates the base layout and responsive CSS quickly, while I refine the visual aesthetics, micro-animations, and UX. |
| 6 | **Designing system architecture & data flows** | **Collaborate with AI** | I set the high-level goals and constraints while collaborating with AI to brainstorm design patterns and alternative database relationships. |
| 7 | **Debugging complex runtime/production errors** | **Collaborate with AI** | AI helps parse log traces and suggest potential causes, while I verify the environment, reproduce the issue, and apply the fix. |
| 8 | **Drafting weekly status updates / standup notes** | **Delegate with Review** | I provide bullet points of raw actions, and AI formats them into polished, concise updates for the team, which I verify before sending. |
| 9 | **Writing documentation & README files** | **Delegate with Review** | AI generates comprehensive drafts based on code analysis, and I review for correctness, clarity, and formatting. |
| 10 | **Creating mock datasets for database seeds** | **Delegate with Review** | AI can generate hundreds of realistic records (JSON/CSV) conforming to a schema, requiring only a quick schema compatibility check from me. |
| 11 | **Linting and formatting code files** | **Fully Automate** | Fully handled by IDE tools (ESLint, Prettier) on commit hooks, requiring zero manual decision-making. |
| 12 | **Running automated CI/CD builds & test suites** | **Fully Automate** | Configured via GitHub Actions to run automatically on every push, notifying the team of success or failure. |

---

## 3. Claude Project Custom Instructions

Below are the custom instructions configured for my Claude Project (`farmer-trade-system`). These instructions ensure that Claude acts as a context-aware development partner.

```markdown
# Role & Persona
You are Antigravity, a senior software engineer and pair-programmer assisting me (Uday, an Engineering Intern at FlyRank). We are building a "Farmer Trade System" (a digital marketplace for agricultural trade). 

# Communication Style
- Keep explanations concise, technical, and professional.
- Focus on code solutions first, followed by short, bulleted rationale.
- Do not use conversational fluff (e.g., "I'd be happy to help", "Sure!").
- When suggesting file edits, use clean git-style diffs or specific replacement chunks.
- Always include clickable file links when referencing workspace files using `file:///` format.

# Technical Preferences
- Stack: HTML5, Vanilla CSS (unless Tailwind is explicitly requested), React/Next.js (if requested), Node.js, and SQL.
- Architecture: Keep code modular, clean, and well-documented. Avoid inline styles.
- SEO & Semantics: Use semantic HTML5 elements. Ensure responsive designs with CSS Flexbox/Grid.
- Testing: Prioritize writing unit tests with high coverage (aiming for 100% path coverage on critical logic).

# Current Goals
1. Audit and optimize our engineering workflows (FL-01).
2. Set up codebases for FL-02 through FL-04 (interactive tools, mock data generators, UI layouts).
3. Build the core services for the Farmer Trade System marketplace.
```

---

## 4. Target Tasks & Measurable Success Definitions

These three tasks from the audit will be carried forward to tasks **FL-02**, **FL-03**, and **FL-04**.

### Task 1: Writing Unit Tests for API Endpoints (Collaborate with AI)
* **Goal**: Automate unit test suite generation for backend API endpoints.
* **Measurable Success Definition**:
  1. Achieves **100% path coverage** for both happy paths (successful requests) and unhappy paths (validation errors, network timeouts, database errors).
  2. Uses **mocking/stubbing** for all external dependencies (e.g., database clients, payment gateway APIs) to ensure tests run fast and isolated.
  3. The test suite passes successfully on the first run with **zero side effects** (does not write to production/development databases).

### Task 2: Creating Mock Datasets for Database Seeds (Delegate with Review)
* **Goal**: Generate realistic testing data representing farmers, buyers, transactions, and products.
* **Measurable Success Definition**:
  1. Generates a reproducible SQL seed script or JSON file containing **100+ unique, schema-compliant records**.
  2. Data is **realistic and logical** (e.g., realistic names, chronological dates, valid relationships via foreign keys like connecting a product to an existing farmer ID).
  3. Seed scripts execute and load into the database in **under 5 seconds** without foreign key constraint violations.

### Task 3: Translating Wireframes/Layouts into Web Components (Collaborate with AI)
* **Goal**: Convert frontend designs/sketches into functional UI code.
* **Measurable Success Definition**:
  1. Layout matches the design layout exactly and is fully responsive (tested across mobile, tablet, and desktop views).
  2. Achieves **zero accessibility (a11y) violations** and a score of **90+** on Google Lighthouse.
  3. Written in clean, semantic HTML5 and vanilla CSS with **zero inline styling** and full separation of concerns.

---

## 5. Tool Setup & Verification

To satisfy the onboarding requirements, the following accounts and training have been initiated:

1. **Claude (Anthropic)**: Account active; Project `farmer-trade-system` created with the custom instructions above.
2. **ChatGPT (OpenAI)**: Account active; utilized for general ideation and framework research.
3. **Anthropic Academy**: Registered for the *AI Fluency: Framework & Foundations* course. Completed **Module 1: Foundations of AI Collaboration**.

> [!NOTE]
> ### 📸 Evidence Upload Placeholders
> For final grading, the following screenshots should be attached/embedded here:
> 
> * **Claude Project Custom Instructions Screenshot**:
>   `![Claude Project Setup](docs/images/claude_project_screenshot.png)`
> * **Anthropic Academy Module 1 Completion Screenshot**:
>   `![Academy Completion](docs/images/anthropic_academy_module1.png)`

---
*End of Report*
