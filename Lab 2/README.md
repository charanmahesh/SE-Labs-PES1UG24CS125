# Lab 2 — Agile Backlog Creation & Sprint Simulation in Jira

**Course:** Software Engineering (SE) — Lab 2  
**Name:** Charan M  
**SRN:** PES1UG24CS125  
**Section:** 5th Semester, Section B  

---

## 1. Objective

Use Jira to convert functional requirements into Agile backlog items (Epics and User Stories), prioritize and estimate them with Fibonacci-based Story Points, run and simulate sprints on a Scrum board, and analyse progress using a Burndown Chart.

## 2. Project Overview

The **Pharmacy Expiry & Re-order Dispatch Engine** is a pharmacy management system that dispenses medicines using FEFO (First Expiry, First Out) logic, tracks medicine batches and their expiry dates, and automates re-ordering of stock from suppliers.

| Field | Value |
| --- | --- |
| Project | Pharmacy Expiry & Re-order Dispatch Engine |
| Project Key | PERODE |
| Board | PERODE board |
| Method | Scrum |
| Epics | 3 |
| User Stories | 8 |
| Total Story Points | 31 |
| Sprints Completed | 2 |
| Workflow | To Do → In Progress → In Review → Done |

**Jira Workspace:** https://pes1ug24cs125.atlassian.net/jira/software/c/projects/PERODE/summary

> **Note:** The Active Sprint Board and backlog screenshots in the deliverable PDF were captured after the sprints had already been run, so the Epic child-item views are used as evidence of the backlog structure and completion status.

## 3. Epics and User Stories

### Epics

| Epic ID | Epic | Priority | Description |
| --- | --- | --- | --- |
| PERODE-1 | Medicine Dispensing & FEFO | High | Manage medicine dispensing using FEFO logic so valid batches with the nearest expiry are selected first, while allowing authorized overrides with proper justification and audit records. |
| PERODE-2 | Inventory & Expiry Management | Medium | Manage medicine batch information and monitor expiry dates so that inventory remains accurate and batches approaching expiry can be identified and acted upon. |
| PERODE-3 | Automated Re-order & Supplier Management | Medium | Automate purchase order generation and supplier interaction for restocking. |

### User Stories

| ID | User Story | Epic | Priority | Story Points |
| --- | --- | --- | --- | --- |
| PERODE-4 | Apply FEFO Picking Logic | PERODE-1 | Highest | 5 |
| PERODE-5 | Dispense Medicine | PERODE-1 | High | 5 |
| PERODE-6 | Override FEFO Selection | PERODE-1 | Medium | 3 |
| PERODE-7 | Record Medicine Batch | PERODE-2 | High | 3 |
| PERODE-8 | View Expiry Alerts | PERODE-2 | Medium | 3 |
| PERODE-9 | Generate Purchase Order | PERODE-3 | High | 8 |
| PERODE-10 | Acknowledge Purchase Order | PERODE-3 | Low | 2 |
| PERODE-11 | Confirm Stock Delivery | PERODE-3 | Low | 2 |
| | **Total** | | | **31** |

Stories are written in the standard format. For example, *PERODE-4*: "As a Pharmacy Clerk, I want the system to select the valid medicine batch with the earliest expiry date, so that older stock is dispensed first and medicine wastage is reduced." *PERODE-8*: "As a Pharmacy Clerk, I want to receive a daily list of medicine batches expiring within 30 days, so that I can identify and take action on medicines approaching expiry."

Story Points were assigned using the Fibonacci scale (2, 3, 5, 8) based on relative effort, complexity and risk. The most complex story, Generate Purchase Order, received the highest estimate (8), while simple supporting stories such as acknowledging an order or confirming delivery received 2.

## 4. Sprint Simulation

### Sprint 1 — PERODE Sprint 1
**Goal:** Deliver the core medicine dispensing (FEFO) flow and inventory/expiry management.

| ID | User Story | Points |
| --- | --- | --- |
| PERODE-4 | Apply FEFO Picking Logic | 5 |
| PERODE-5 | Dispense Medicine | 5 |
| PERODE-6 | Override FEFO Selection | 3 |
| PERODE-7 | Record Medicine Batch | 3 |
| PERODE-8 | View Expiry Alerts | 3 |
| | **Sprint Total** | **19** |

### Sprint 2 — PERODE Sprint 2
**Goal:** Deliver automated re-ordering and supplier management.

| ID | User Story | Points |
| --- | --- | --- |
| PERODE-9 | Generate Purchase Order | 8 |
| PERODE-10 | Acknowledge Purchase Order | 2 |
| PERODE-11 | Confirm Stock Delivery | 2 |
| | **Sprint Total** | **12** |

Stories moved through To Do → In Progress → In Review → Done on the Active Sprint board. All 8 stories were completed (all three Epics show 100% Done).

## 5. Burndown Analysis

| Sprint | Committed | Completed | Remaining |
| --- | --- | --- | --- |
| PERODE Sprint 1 | 19 pts | 19 pts | 0 pts |
| PERODE Sprint 2 | 12 pts | 12 pts | 0 pts |

The Burndown Chart screenshot included in the deliverable shows a flat line with no visible burndown data. This is because the sprints were completed in a very short span of time, so Jira did not record a gradual day-by-day reduction in remaining work. It should therefore not be read as a measure of real daily velocity.

## 6. Reflection (Summary)

1. **Did estimations reflect actual effort?** To a reasonable extent. Complex stories such as applying FEFO logic and generating purchase orders received higher points, while simple ones such as acknowledging purchase orders received fewer. The sprint results showed the estimates were generally reasonable.
2. **Was the backlog well-prioritized?** Yes. Core functionality such as FEFO picking and medicine dispensing was High/Highest priority, while supporting functions such as stock delivery confirmation were Low, so the most important functionality was addressed first.
3. **How did the simulated sprints align with the plan?** They aligned well. Core dispensing and inventory functionality went into the earlier sprint, and the supplier-management features followed in the next, grouped by priority and estimated effort.
4. **What did the burndown chart show about capacity?** It is meant to show how quickly planned story points are completed and how much work a team can realistically take on in a sprint. In this simulation, the compressed timeline meant the chart did not capture a gradual burndown.

## 7. Folder Contents

```
Lab2/
├── README.md
└── Lab2_Deliverable_PES1UG24CS125.pdf
```

## 8. Deliverables Checklist

- Jira backlog with Epics and User Stories
- Story point assignments
- Sprint board (Active Sprint view)
- Burndown chart
- Reflection questions answered (see deliverable PDF)
- Live Jira workspace available for instructor demonstration
