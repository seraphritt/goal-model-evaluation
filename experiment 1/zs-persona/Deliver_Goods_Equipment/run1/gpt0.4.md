**Goal Model – Multi‑Robot Resource Delivery**

| **Name**                          | **Text**                                                                  | **Runtime**           | **Goal Type** | **Relation** | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| --------------------------------- | ------------------------------------------------------------------------- | --------------------- | ------------- | ------------ | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| G1 – Deliver Resources            | Deliver all requested resources to the specified destination.             | `;` (sequential)      | Achieve       | AND          | Perform                                                  | Perform            | Perform                                                  |
| G2 – Collect Resources            | Collect the required resources from the storages.                         | `FALLBACK(G2.1,G2.2)` | Perform       | OR           | Achieve. Target condition: all resources were collected  | ok                 | Achieve. Target condition: all resources were collected  |
| G2.1 – Request & Retrieve         | Navigate to the storage, request the resources, and wait for retrieval.   | `;` (sequential)      | Perform       | AND          | OK                                                       | OK                 | OK                                                       |
| G2.2 – Low-Battery Collection     | Handle a low-battery situation during collection.                         | `;` (sequential)      | Perform       | AND          | OK                                                       | OK                 | OK                                                       |
| G3 – Deliver Resources            | Deliver the collected resources to the destination.                       | `FALLBACK(G3.1,G3.2)` | Perform       | OR           | Achieve. Target condition: all resources were delivered. | ok                 | Achieve. Target condition: all resources were delivered. |
| G3.1 – Normal Delivery            | Navigate to the destination, deliver the resources, and confirm delivery. | `;` (sequential)      | Perform       | AND          | OK                                                       | OK                 | OK                                                       |
| G3.2 – Low-Battery Delivery       | Handle a low-battery situation during delivery.                           | `;` (sequential)      | Perform       | AND          | OK                                                       | OK                 | OK                                                       |
| G7 – Parallel Collection/Delivery | Parallelise collect-deliver tasks when multiple items are required.       | `#` (parallel)        | Perform       | AND          | OK                                                       | OK                 | OK                                                       |



> **Target Condition (G1)** – *All requested resources are present at the specified destination location.*

---

**Task Model**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| AT1 – Navigate to Storage | Robot navigates to the storage location to collect resources. | AND | storage | 1 |
| AT2 – Send Request | Robot sends a message to the storage specifying the requested resources. | AND | storage | 1 |
| AT3 – Wait for Retrieval | Robot waits until the storage retrieves the requested resources. | AND | storage | 1 |
| AT4 – Go to Recharge | Robot returns to the recharging station due to low battery. | AND | recharging station | 1 |
| AT5 – Assign to New Robot | Robot assigns the remaining mission to another robot. | AND | recharging station | 1 |
| AT6 – Navigate to Destination | Robot navigates to the specified destination location. | AND | destination | 1 |
| AT7 – Deliver Resources | Robot delivers the collected resources to the destination. | AND | destination | 1 |
| AT8 – Confirm Delivery | Robot confirms delivery of resources at the destination. | AND | destination | 1 |
| AT9 – Return to Checkpoint | Robot returns the resource to a checkpoint due to low battery. | AND | checkpoint | 1 |
| AT10 – Assign to New Robot (Delivery) | Robot assigns the remaining delivery task to another robot. | AND | checkpoint | 1 |
| AT12 – Trigger Alert | Robot triggers an alert and sends a report to the sector manager if it fails to return the resource to a checkpoint. | AND | sector manager | 1 |
| AT13 – Parallel Task Assignment | Robot assigns multiple robots to parallel collect‑deliver tasks for multiple items. | AND | mission control | [1,n] |
| AT14 – Monitor Parallel Tasks | Robot monitors the progress of parallel collect‑deliver tasks. | AND | mission control | 1 |

---

### Logical Relationships (Summary)

```
G1 -> G2, G3, G7 [AND][;]
G2 -> G2.1, G2.2 [OR][FALLBACK(G2.1,G2.2)]
G2.1 -> AT1, AT2, AT3 [AND][;]
G2.2 -> AT4, AT5 [AND][;]
G3 -> G3.1, G3.2 [OR][FALLBACK(G3.1,G3.2)]
G3.1 -> AT6, AT7, AT8 [AND][;]
G3.2 -> AT9, AT10, AT12 [AND][;]
G7 -> AT13, AT14 [AND][#]
```

This goal‑task decomposition captures the full multi‑robot mission: collection, delivery, battery‑aware contingencies, parallel execution for multiple items, and failure reporting. All goals are linked to concrete, executable tasks with clear locations and robot counts, enabling straightforward implementation in a multi‑robot system.

f1-score = 0.9333333333333333
macro-f1 = 0.3137254901960784
