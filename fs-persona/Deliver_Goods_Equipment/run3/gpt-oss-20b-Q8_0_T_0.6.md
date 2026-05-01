**Goal Model – Multi‑Robot Resource Delivery Mission**

---

## 1. Goals
| **Name**                                     | **Text**                                                                                              | **Runtime**      | **Goal Type** | **Target Condition / Enquired Info** | **Relation** | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------- | ------------- | ------------------------------------ | ------------ | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1 – Complete Mission**                    | Ensure that all requested resources are collected from storage and delivered to the requesting agent. | `;` (sequential) | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.1 – Plan Collection Route**             | Compute the optimal order of storages to visit based on waiting-time + path estimate.                 | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |
| **G1.2 – Collect Resources**                 | Execute the collection phase, including navigation, request, and handling low-battery.                | `#` (parallel)   | Perform       | –                                    | AND          | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G1.2.1 – Request & Retrieve**              | Go to a storage, send request, and wait until the resources are retrieved.                            | `-`              | Perform       | –                                    | –            | Query. Enqueried info: resources to be collected.        | OK                 | Query. Enqueried info: resources to be collected.        |
| **G1.2.3 – Handle Low Battery (Collection)** | If battery ≤10 %, return to recharge and hand over the mission to another robot.                      | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |
| **G1.3 – Deliver Resources**                 | Execute the delivery phase, including transport, checkpoint handling, and low-battery management.     | `#` (parallel)   | Perform       | –                                    | AND          | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G1.3.1 – Transport to Destination**        | Carry the retrieved resources from storage to the specified delivery location.                        | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |
| **G1.3.2 – Handle Low Battery (Delivery)**   | If battery ≤30 %, return to a checkpoint and re-assign the remaining load.                            | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |
| **G1.3.3 – Return to Checkpoint**            | Return the partially delivered resources to a checkpoint for hand-over.                               | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |
| **G1.4 – Handle Failure**                    | Deal with any failure that occurs during the mission.                                                 | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |
| **G1.4.1 – Trigger Alert & Report**          | Send an alert and report to the sector manager if a checkpoint return fails.                          | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |
| **G1.5 – Parallelize Tasks**                 | Assign multiple robots to different sub-tasks to reduce overall mission time.                         | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |
| **G1.5.1 – Assign Robots to Parallel Tasks** | Distribute the collection and delivery subtasks among available robots.                               | `-`              | Perform       | –                                    | –            | OK                                                       | OK                 | OK                                                       |

---

## 2. Tasks

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1 – Compute Route** | Compute the optimal collection route. | AND | Planning Center | 1 |
| **AT2 – Navigate to Storage** | Move to the specified storage location. | AND | Storage A / B / … | 1 |
| **AT3 – Send Request** | Send a message to the storage with the requested resource specification. | AND | Storage | 1 |
| **AT4 – Wait for Retrieval** | Wait until the storage confirms that the resources are ready. | AND | Storage | 1 |
| **AT5 – Navigate to Destination** | Move to the delivery location. | AND | Destination | 1 |
| **AT6 – Transport Resource** | Carry the resources to the delivery location. | AND | Destination | 1 |
| **AT7 – Return to Recharge** | Return to the charging station when battery ≤10 %. | AND | Recharge Station | 1 |
| **AT8 – Return to Checkpoint** | Return to a checkpoint when battery ≤30 % during delivery. | AND | Checkpoint | 1 |
| **AT9 – Assign Remaining Task** | Re‑assign the remaining load to another robot. | AND | Current Location (Control Center) | 1 |
| **AT10 – Trigger Alert** | Send an alert and report to the sector manager. | AND | Manager Office / System | 1 |
| **AT11 – Assign Parallel Tasks** | Allocate subtasks to available robots. | AND | Control Center | 1 |

---

## 3. Summary Table (Goals & Tasks)

| **ID** | **Type** | **Title** | **Runtime** | **Relation** |
|--------|----------|-----------|-------------|--------------|
| G1 | Goal | Complete Mission | `;` | AND |
| G1.1 | Goal | Plan Collection Route | `-` | – |
| G1.2 | Goal | Collect Resources | `#` | AND |
| G1.2.1 | Goal | Request & Retrieve | `-` | – |
| G1.2.3 | Goal | Handle Low Battery (Collection) | `-` | – |
| G1.3 | Goal | Deliver Resources | `#` | AND |
| G1.3.1 | Goal | Transport to Destination | `-` | – |
| G1.3.2 | Goal | Handle Low Battery (Delivery) | `-` | – |
| G1.3.3 | Goal | Return to Checkpoint | `-` | – |
| G1.4 | Goal | Handle Failure | `-` | – |
| G1.4.1 | Goal | Trigger Alert & Report | `-` | – |
| G1.5 | Goal | Parallelize Tasks | `-` | AND |
| G1.5.1 | Goal | Assign Robots to Parallel Tasks | `-` | – |
| AT1 | Task | Compute Route | AND | Planning Center |
| AT2 | Task | Navigate to Storage | AND | Storage |
| AT3 | Task | Send Request | AND | Storage |
| AT4 | Task | Wait for Retrieval | AND | Storage |
| AT5 | Task | Navigate to Destination | AND | Destination |
| AT6 | Task | Transport Resource | AND | Destination |
| AT7 | Task | Return to Recharge | AND | Recharge Station |
| AT8 | Task | Return to Checkpoint | AND | Checkpoint |
| AT9 | Task | Assign Remaining Task | AND | Control Center |
| AT10 | Task | Trigger Alert | AND | Manager Office |
| AT11 | Task | Assign Parallel Tasks | AND | Control Center |

---

## 4. Logical Relationships (Tree Structure)

```
G1  -> G1.1, G1.2, G1.3, G1.4, G1.5  [AND][;]
G1.2 -> G1.2.1, G1.2.3                [AND][#]
G1.3 -> G1.3.1, G1.3.2, G1.3.3        [AND][#]
G1.5 -> G1.5.1                         [AND][-]

G1.1 -> AT1                           [AND][-]
G1.2.1 -> AT2, AT3, AT4               [AND][-]
G1.2.3 -> AT7, AT9                    [AND][-]
G1.3.1 -> AT5, AT6                    [AND][-]
G1.3.2 -> AT7, AT9                    [AND][-]
G1.3.3 -> AT8, AT9                    [AND][-]
G1.4.1 -> AT10                        [AND][-]
G1.5.1 -> AT11                        [AND][-]
```

Each “`[AND][-]`” indicates that the goal is satisfied when all its child goals/tasks are satisfied, and the child is a leaf (no further decomposition). Parallelism is indicated by `#`, and sequential execution by `;`.  

This goal‑model captures the full multi‑robot mission, decomposing high‑level objectives into actionable tasks while explicitly handling battery contingencies, parallel execution, and failure reporting.
