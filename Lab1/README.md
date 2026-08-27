<div align="center">

# Lab 1 – Requirements Engineering & UML Use-Case Modelling

### Problem Statement #15: Pharmacy Expiry & Re-order Dispatch Engine

**Healthcare & Telemedicine**

</div>

## Overview

This repository contains the requirements engineering and UML use-case modelling work for **Problem Statement #15 – Pharmacy Expiry & Re-order Dispatch Engine**.

The system is a pharmacy stock management platform that enforces FEFO (First-Expired-First-Out) dispensing order, tracks medicine batches from receipt through checkout, generates expiry alerts, and automatically dispatches purchase orders to suppliers when stock falls below a safety threshold.

The primary stakeholders identified for the system are the **Pharmacy Clerk**, **Pharmacy Manager**, and **Inventory Supplier**.

## Problem Statement

The **Pharmacy Expiry & Re-order Dispatch Engine** is designed to support pharmacy stock management through automated batch tracking, FEFO-based dispensing, and supplier re-ordering.

The system allows the **Pharmacy Clerk** to dispense medicine at checkout while the system enforces FEFO picking order, prioritizing batches with the nearest expiry date. Batch details are recorded at the time of stock receipt, including batch number, quantity received, and expiry date.

The platform also supports:

- Daily expiry alerts for batches expiring within 30 days
- Manual FEFO override at checkout with a mandatory justification note
- Automatic purchase order generation when stock dips below a safety threshold
- Supplier acknowledgement and delivery confirmation for purchase orders
- A tamper-evident audit trail of expiry data and dispensing transactions

The problem statement specifically requires automated purchase order dispatch to meet defined latency and security benchmarks, and requires audit records to be retained, unaltered, for a minimum of **3 years**.

## System Objectives

The main objectives of the system are to:

1. Enforce FEFO picking order to minimize medicine wastage and protect patient safety.
2. Capture accurate batch-level data (batch number, quantity, expiry date) at stock receipt.
3. Alert pharmacy staff to batches nearing expiry.
4. Allow justified manual overrides of the FEFO-suggested batch.
5. Automatically trigger and track supplier purchase orders when stock runs low.
6. Maintain a secure, tamper-evident audit trail for regulatory compliance.

## Actors

| Actor | Description |
| :--- | :--- |
| **Pharmacy Clerk** | Dispenses medicine using FEFO checkout, records batch receipts, and may override the FEFO-suggested batch with a justification note. |
| **Pharmacy Manager** | Approves high-value purchase orders before they are dispatched to suppliers. |
| **Inventory Supplier** | Acknowledges dispatched purchase orders, provides expected delivery dates, and confirms stock delivery. |

## Requirements Engineering

The system requirements were identified from the assigned problem scenario and documented using a structured requirements table.

### Functional Requirements

The project contains exactly **five functional requirements**:

| ID | Function |
| :---: | :--- |
| **FR-001** | Enforce FEFO picking order by prioritizing batches with the nearest expiry date during sales checkout. |
| **FR-002** | Require a Pharmacy Clerk to record batch number, quantity received, and expiry date at stock receipt. |
| **FR-003** | Generate a daily expiry alert list of batches expiring within the next 30 days, grouped by medicine. |
| **FR-004** | Allow a Pharmacy Clerk to manually override the FEFO-suggested batch at checkout, given a justification note. |
| **FR-005** | Allow an Inventory Supplier to acknowledge a dispatched purchase order and provide an expected delivery date. |

### Non-Functional Requirements

The project contains exactly **two non-functional requirements**:

| ID | Type | Requirement |
| :---: | :---: | :--- |
| **NFR-001** | Performance & Security | Purchase order requests shall be automatically generated and dispatched when stock dips below the safety threshold, meeting target latency and security benchmarks. |
| **NFR-002** | Compliance & Auditability | A complete, tamper-evident audit trail of batch expiry data and dispensing transactions shall be retained for a minimum of 3 years. |

Each requirement includes a priority, measurable acceptance criteria, and rationale.

The complete requirements table is available in:

[**Requirements.md**](Requirements.md)

## UML Use-Case Model

The UML model represents the main interactions between the identified actors and the pharmacy stock management system.

### Use Cases

| ID | Use Case |
| :---: | :--- |
| **UC-01** | Dispense Medicine (FEFO Checkout) |
| **UC-02** | Apply FEFO Picking Logic |
| **UC-03** | Record Batch Receipt & Expiry Date |
| **UC-04** | Generate Purchase Order |
| **UC-05** | Approve High-Value Purchase Order |
| **UC-06** | Confirm Stock Delivery |

### UML Relationships

The diagram contains both required relationship types:

- **UC-01 `«include»` UC-02**
  Dispensing medicine at checkout includes applying the FEFO picking logic to rank available batches.

- **UC-05 `«extend»` UC-04**
  Approving a high-value purchase order extends the base purchase-order generation flow, applying only when the order value crosses a defined threshold.

The UML diagram also contains the required system boundary and all identified actors.

The completed diagram is available in:

[**Use_Case_Diagram.pdf**](Use_Case_Diagram.pdf)

## Use-Case Flow Specification

The selected core use case for the detailed flow specification is:

**UC-01 – Dispense Medicine (FEFO Checkout)**

### Primary Actor

**Pharmacy Clerk**

### Preconditions

- The Pharmacy Clerk is logged into the Pharmacy Stock Management System.
- At least one unexpired batch of the requested medicine exists in inventory.

### Postconditions

- The dispensed quantity is deducted from the selected batch's stock level.
- A dispensing transaction record (medicine, batch number, quantity, clerk ID, timestamp) is stored in the audit trail.
- If resulting stock falls below the safety threshold, a purchase order is automatically triggered (UC-04).

### Main Success Scenario

1. The Pharmacy Clerk selects "Dispense Medicine" and enters the medicine name and quantity requested.
2. The system retrieves all unexpired batches of that medicine and invokes UC-02 (Apply FEFO Picking Logic) to rank them by expiry date.
3. The system proposes the batch with the nearest expiry date and displays batch number, expiry date, and available quantity.
4. The Pharmacy Clerk confirms the proposed batch.
5. The system validates that the requested quantity does not exceed the batch's available stock.
6. The system deducts the dispensed quantity from the batch and updates the inventory in real time.
7. The system logs the transaction (medicine, batch number, quantity, clerk ID, timestamp) to the audit trail.
8. The system checks the medicine's remaining total stock against its safety threshold.
9. The system displays a dispensing confirmation and prints/emails a receipt to the clerk.
10. The use case ends successfully.

### Alternate Flow – Requested Quantity Exceeds Batch Stock

1. **At Step 5 of the Main Success Scenario, the requested quantity exceeds the proposed batch's available stock.**
2. The system displays an "Insufficient batch quantity" message and shows the next-nearest-expiry batch with available stock.
3. The Pharmacy Clerk chooses to split the order across batches or reduce the requested quantity.
4. If the clerk selects a batch other than the FEFO-proposed one, the system requires a justification note (FR-004) before proceeding.
5. The flow resumes at Step 5 of the Main Success Scenario with the newly selected batch.

### Alternate Flow – Stock Falls Below Safety Threshold

1. **At Step 8 of the Main Success Scenario, the medicine's remaining stock falls below its safety threshold.**
2. The system automatically invokes UC-04 (Generate Purchase Order) for the affected medicine.
3. The system notifies the Pharmacy Clerk that a re-order has been triggered.
4. The flow resumes at Step 9 of the Main Success Scenario.

The complete use-case flow specification is available in:

[**Use_Case_Flow.pdf**](Use_Case_Flow.pdf)

## Folder Structure

```text
Lab-1/
│
├── README.md
├── Requirements.md
├── Use_Case_Diagram.pdf
└── Use_Case_Flow.pdf
```

**GitHub:** [charanmahesh/SE-Labs-PES1UG24CS125](https://github.com/charanmahesh/SE-Labs-PES1UG24CS125)
