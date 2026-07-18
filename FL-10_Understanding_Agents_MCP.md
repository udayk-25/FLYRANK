# FL-10: Understanding Agents & MCP
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 4)  
**Date:** July 18, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Technical Explainer: Workflows vs. Agents

### What is a Workflow?
A **workflow** is a deterministic, structured sequence of execution steps. In a workflow, inputs travel along a pre-defined path from one node to another. Each node performs a specific task (such as formatting text, executing a regex, or running a prompt) and hands the output to the next node. The execution graph is static; there is no branching or routing unless it has been explicitly hard-coded beforehand. Even when powered by Large Language Models (LLMs), a workflow remains predictable, highly controllable, and easy to audit because the LLM is only responsible for executing the individual instructions at each node, rather than deciding *what* node to run next.

### What is an Agent?
An **agent** is an autonomous system where the LLM functions as the central routing and decision engine. Instead of following a fixed script, the agent is given a top-level goal, a set of tools (such as database access, web search, or code compilers), and a feedback loop. The agent evaluates the environment, decides which tool to call, processes the results, and dynamically chooses the next action. If a tool call fails or produces an error, the agent can self-correct, backtrack, or try an alternative approach. The execution path is not pre-determined; it is constructed on the fly based on runtime feedback.

### Classification of the FL-09 Case-Writing Pipeline
The "Draft, Critique, Revise" pipeline built in the previous assignment (FL-09) is a **Workflow**, not an agent. 

*   **Reasoning**: The execution sequence is fixed: `Input -> Draft Node -> Critique Node -> Revise Node -> Final Output`. The prompt node handoffs are linear and hard-coded. The writer node cannot choose to query a repository instead of drafting; the critique node cannot decide to skip the revision if the draft is perfect; and the system has no feedback loops allowing the reviser to send the copy back to the critique node if it fails validation. It is a highly structured prompt chain.

---

## 2. Model Context Protocol (MCP) Primer

The **Model Context Protocol (MCP)** is an open-standard, client-server protocol designed by Anthropic. It functions like a standardized "USB-C port" for AI applications, allowing LLM clients (such as Claude Desktop or development containers) to securely connect to external data sources and execution tools (MCP servers) via a unified API.

MCP defines three primary data primitives:
1.  **Tools**: Executable functions that the model can invoke to perform actions in the physical or digital world (e.g., writing a file, running a shell command, or executing a Python script). Tools require explicit user approval for execution.
2.  **Resources**: Read-only data streams or files that the client exposes to the model (e.g., database schemas, system logs, or API endpoints).
3.  **Prompts**: Standardized, pre-configured templates that the server exposes to help the client structure model queries.

---

## 3. Upgrading the Case Study Pipeline to a True Agent

To transform the static FL-09 case-writing workflow into an autonomous agent, we would need to implement a **ReAct (Reasoning and Acting) loop** equipped with filesystem and command tools via MCP:

```
Goal: Generate a verified case study for the Farmer Trade System.
[Agent Loop]:
1. Read project files (Tool: view_file C:\Downloads\FLYRANK\scripts\01_prepare_features.py).
2. Check testing suite (Tool: run_command "npm run test").
3. Analyze test results:
   - If coverage is < 100%, search for missing tests (Tool: grep_search "describe").
   - If coverage is 100%, proceed to compile draft.
4. Draft & Critique: Write the copy and run a self-critique check.
5. If critique score is < 9.0, recursively edit and re-evaluate.
6. Write completed file directly to disk (Tool: write_to_file portfolio/cases/farmer_trade.md).
```

By giving the LLM autonomous control over the filesystem tools, the execution becomes dynamic. The agent decides when the research is complete, self-corrects based on test errors, and outputs the finished file only when its internal validation criteria are met.

---

## 4. MCP Verification Evidence

Below is the execution evidence showing three local filesystem tasks running tool calls using the Antigravity MCP client:

### Task 1: Inspecting the workspace directory structure (`list_dir`)
*   **Command**: `list_dir` on path `c:\Users\Uday\Downloads\FLYRANK\work\notebooks`
*   **Output**:
```json
[
  {"name": "w01_research_question.ipynb", "sizeBytes": 20498},
  {"name": "w02_ml_task_framing.ipynb", "sizeBytes": 16905},
  {"name": "w03_data_contract.ipynb", "sizeBytes": 12884}
]
```

### Task 2: Reading the content of `FL-09_No_Code_Workflows.md` (`view_file`)
*   **Command**: `view_file` on path `c:\Users\Uday\Downloads\FLYRANK\FL-09_No_Code_Workflows.md` (Lines 1 to 15)
*   **Output**:
```markdown
1: # FL-09: No-Code Workflows — Draft, Critique, Revise
2: **Track:** General AI Fluency  
3: **Phase:** Onboarding (Week 4)  
4: **Date:** July 18, 2026  
5: **Author:** Uday (Software Engineer Intern, FlyRank)  
6: 
7: ---
8: 
9: ## 1. Workflow Architecture
10: 
11: This workflow is a three-stage **"Draft, Critique, Revise"** pipeline built to compile...
```

### Task 3: Finding files with specific query terms (`grep_search`)
*   **Command**: `grep_search` on path `c:\Users\Uday\Downloads\FLYRANK` with query `"trend_pct"`
*   **Output**:
```json
[
  {
    "Filename": "c:\\Users\\Uday\\Downloads\\FLYRANK\\work\\notebooks\\w03_data_contract.ipynb",
    "LineNumber": 16,
    "LineContent": "   \"\\\"trend_pct\\\": available because it represents...\""
  },
  {
    "Filename": "c:\\Users\\Uday\\Downloads\\FLYRANK\\data\\raw\\content_refresh_anonymized.csv",
    "LineNumber": 1,
    "LineContent": "...position_tier,trend_direction,trend_pct"
  }
]
```

---
*End of Report*
