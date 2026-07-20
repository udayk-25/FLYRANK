# FL-13: Build Your MVP Agent — Execution & Build Log
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 6)  
**Date:** July 20, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Core Job Verification & Execution Trace

The MVP agent controller (`scripts/capstone_agent.py`) executes its primary mission end-to-end without manual intervention:

```text
=== STARTING CAPSTONE AGENT RUN ===
[16:22:56] [Agent Init] Autonomous Search Agent initialized.
[16:22:56] [Tool 1: DuckDB Query] Reading dataset slice: data/raw/content_refresh_anonymized.csv
[16:22:57] [Tool 1: DuckDB Query] Ingested 26,254 rows matching active visibility criteria.
[16:22:57] [Tool 2: ML Scoring] Evaluating organic decay priority...
[16:22:57] [Tool 2: ML Scoring] Score Complete | Base Rate: 59.1% | Precision@50: 58.0%
[16:22:57] [Tool 3: Brief Writer] Generating markdown briefs...
[16:22:57] [Tool 3: Brief Writer] Saved brief to: work/outputs/briefs/refresh_brief_top50.md
[16:22:57] [Tool 3: Brief Writer] Saved run receipt to: work/outputs/briefs/agent_run_receipt.json
=== AGENT RUN COMPLETED SUCCESSFULLY ===
```

---

## 2. Live Tool Connections

The MVP agent connects to three real local data sources and tools:

1.  **DuckDB In-Memory Data Warehouse (`tool_query_warehouse`)**: Connects directly to `data/raw/content_refresh_anonymized.csv` to query active records with SQL filters (`impressions_90d >= 10`).
2.  **Scikit/NumPy Priority Scoring Engine (`tool_score_decay_priority`)**: Computes transparent priority scores, maps reason codes (`STALE_HIGH_VISIBILITY`), and caps the recommendation queue at the top 50 items (Precision@50).
3.  **Filesystem Brief Writer (`tool_generate_briefs`)**: Generates structured Markdown editorial briefs (`refresh_brief_top50.md`) and logs a JSON run receipt (`agent_run_receipt.json`).

---

## 3. Build Log — Iteration, Fixes, & Cuts

### What Broke & What Was Changed
*   **Fix 01: DuckDB Query Type Errors**: Initial SQL query returned `NaN` values for missing `avg_position = 0` rows, causing pandas float conversion issues. Fixed by casting SQL logical comparisons directly inside DuckDB: `LOWER(trend_direction) = 'down' AS is_declining`.
*   **Fix 02: Missing Directory Handling**: The agent failed on first run because `work/outputs/briefs/` did not exist. Added `os.makedirs(self.output_dir, exist_ok=True)` in `__init__`.
*   **Fix 03: Windows UTF-8 Output Encoding**: PowerShell console output threw Unicode encoding errors when writing bullet points. Fixed by setting `$env:PYTHONIOENCODING="utf-8"` and specifying `encoding="utf-8"` in Python file handles.

### Deviations & Cuts from FL-12 Spec
*   **Cut Feature: External Email Notification**: The original spec considered adding an email webhook tool. Cut from MVP scope to keep the agent 100% self-contained, free, and executable locally without third-party API dependencies.

---

## 4. Raw Run Screen Capture Layout

To demonstrate the working MVP loop, a 2-minute unedited screen capture was recorded:

1.  **0:00 - 0:25**: Launching terminal in `FLYRANK` workspace and running `$env:PYTHONIOENCODING="utf-8"; python scripts/capstone_agent.py`.
2.  **0:25 - 0:55**: Viewing live stdout trace logging DuckDB ingestion of 26,254 rows and scoring completion.
3.  **0:55 - 1:40**: Opening the generated `work/outputs/briefs/refresh_brief_top50.md` file in VS Code to inspect the rendered markdown table and editorial action items.
4.  **1:40 - 2:00**: Inspecting the accompanying JSON run receipt (`agent_run_receipt.json`).

---
*End of Report*
