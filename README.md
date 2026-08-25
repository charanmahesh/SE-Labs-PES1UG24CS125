# Lab 1 — Requirements Engineering & UML Use-Case Modelling

**Course:** Software Engineering
**Student:** Charan M (PES1UG24CS125), Section B
**Institution:** PES University, Bengaluru
**Problem Statement:** #15 — Healthcare & Telemedicine

## Project: Pharmacy Expiry & Re-order Dispatch Engine

Hospital pharmacies need an automated stock management engine that tracks batch expiry
dates, generates First-Expired-First-Out (FEFO) dispensing lists, and triggers automated
purchase orders when stock hits a defined safety threshold.

**Stakeholders / Actors:** Pharmacy Clerk, Pharmacy Manager, Inventory Supplier

## Repository Contents

| File | Description |
|---|---|
| `PES1UG24CS125_Requirements_Table_Lab1.docx` | Requirements table — 5 Functional Requirements (FR-001–FR-005) and 2 Nonfunctional Requirements (NFR-001, NFR-002), each with ID, Type, Description, Priority, Acceptance Criteria, and Rationale |
| `PES1UG24CS125_UseCase_Diagram_Lab1.pdf` | UML use-case diagram showing all actors, use cases, and `<<include>>` / `<<extend>>` relationships |
| `PES1UG24CS125_UseCase_Flow_Lab1.docx` | One-page use-case flow specification for UC-01 (Dispense Medicine — FEFO Checkout): preconditions, postconditions, main success scenario, and alternate flows |

## Requirements Summary

- **FR-001:** Enforce FEFO picking order at checkout (given)
- **FR-002:** Record batch number, quantity, and expiry date at stock receipt
- **FR-003:** Generate a daily expiry alert list for batches expiring within 30 days
- **FR-004:** Allow manual FEFO override with a mandatory justification note
- **FR-005:** Allow supplier acknowledgement of dispatched purchase orders
- **NFR-001:** Auto-generate and dispatch purchase orders under threshold, meeting latency/security benchmarks (given)
- **NFR-002:** Retain a 3-year tamper-evident audit trail for regulatory compliance

## Use-Case Model

**Actors:** Pharmacy Clerk, Pharmacy Manager, Inventory Supplier

**Use Cases:**
1. UC-01 — Dispense Medicine (FEFO Checkout)
2. UC-02 — Apply FEFO Picking Logic (`<<include>>`d by UC-01)
3. UC-03 — Record Batch Receipt & Expiry Date
4. UC-04 — Generate Purchase Order
5. UC-05 — Approve High-Value Purchase Order (`<<extend>>`s UC-04)
6. UC-06 — Confirm Stock Delivery

## Tools Used

- Requirements table & use-case flow: Microsoft Word (.docx)
- UML use-case diagram: exported as PDF

## Lab Objective

From the problem statement scenario, elicit key functions and constraints; write clear,
verifiable functional and nonfunctional requirements; then translate them into a UML
use-case diagram and a use-case flow document.
