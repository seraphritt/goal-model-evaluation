**Goal Model – Multi‑Robot Resource Delivery Mission**

| **Name**                                                  | **Text**                                                                                                                   | **Runtime** | **Goal Type** | **Enquired Information / Target Condition** | **Relation**              | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------- | ------------------------------------------- | ------------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1 – Complete Resource Delivery Mission**               | Ensure all requested resources are collected from storage and delivered to the requesting agent at the specified location. | `;`         | Perform       | –                                           | AND (with G2, G9)         | OK                                                       | OK                 | OK                                                       |
| **G2 – Collect Required Resources**                       | Collect all requested resources from designated storage facilities.                                                        | `;`         | Perform       | –                                           | AND (with G3, G4)         | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G3 – Determine Collection Order**                       | Query waiting times and travel distances to compute optimal collection order.                                              | `-`         | Query         | waiting times, travel distances             | –                         | OK                                                       | Perform            | OK                                                       |
| **G4 – Execute Collection**                               | Execute the collection process for all required resources.                                                                 | `;`         | Perform       | –                                           | AND (with G5, G6, G7, G8) | OK                                                       | OK                 | OK                                                       |
| **G5 – Navigate to Storage**                              | Navigate to the designated storage location.                                                                               | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G6 – Send Request to Storage**                          | Send a message to the storage requesting the specified resources.                                                          | `-`         | Perform       | –                                           | –                         | Query. Enqueried information: resource to be collected   | OK                 | Query. Enqueried information: resource to be collected   |
| **G7 – Wait for Retrieval**                               | Wait until the requested resources are retrieved from the storage.                                                         | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G8 – Pick Resource**                                    | Pick up the retrieved resources from the storage.                                                                          | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G9 – Deliver Resources**                                | Deliver the collected resources to the specified destination.                                                              | `;`         | Perform       | –                                           | AND (with G10, G12)       | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G10 – Transport Resources**                             | Transport the resources from storage to destination, possibly over multiple runs.                                          | `;`         | Perform       | –                                           | AND (with G11, G12, G13)  | OK                                                       | OK                 | OK                                                       |
| **G11 – Navigate to Delivery Location**                   | Navigate to the destination where resources must be delivered.                                                             | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G12 – Deliver Resource**                                | Deliver the resources to the destination.                                                                                  | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G13 – Return to Storage / Next Run**                    | Return to storage (or next run) after delivery, if more resources remain.                                                  | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G15 – Handle Battery Low during Collection**            | Manage low-battery situation during the collection phase.                                                                  | `-`         | Perform       | –                                           | AND (with G16, G17)       | OK                                                       | OK                 | OK                                                       |
| **G16 – Go to Recharge Station**                          | Navigate to the charging station to recharge.                                                                              | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G17 – Assign Mission to Another Robot**                 | Assign the remaining collection task to another robot.                                                                     | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G18 – Handle Battery Low during Delivery**              | Manage low-battery situation during the delivery phase.                                                                    | `-`         | Perform       | –                                           | AND (with G19, G20)       | OK                                                       | OK                 | OK                                                       |
| **G19 – Return Resource to Checkpoint**                   | Return the resource to a checkpoint before battery depletion.                                                              | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G20 – Assign Remaining Task to Another Robot**          | Assign the remaining delivery task to another robot.                                                                       | `-`         | Perform       | –                                           | –                         | OKs                                                      | OK                 | OKs                                                      |
| **G21 – Handle Failure to Return Resource to Checkpoint** | Manage failure to return resource to checkpoint.                                                                           | `-`         | Perform       | –                                           | AND (with G22, G23)       | OK                                                       | OK                 | OK                                                       |
| **G22 – Trigger Alert**                                   | Trigger an alert when checkpoint return fails.                                                                             | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G23 – Send Report to Sector Manager**                   | Send a report of the failure to the sector manager.                                                                        | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |
| **G24 – Parallel Collection-Delivery for Multiple Items** | Parallelise collection-delivery tasks when multiple items are required from different storages.                            | `#`         | Perform       | –                                           | AND (with G25)            | OK                                                       | OK                 | OK                                                       |
| **G25 – Assign Multiple Robots to Parallel Tasks**        | Assign multiple robots to parallel collection-delivery tasks.                                                              | `-`         | Perform       | –                                           | –                         | OK                                                       | OK                 | OK                                                       |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1 – Navigate to Storage** | Move to the specified storage facility. | AND (to G5) | Storage facility | 1 |
| **AT2 – Send Request to Storage** | Send a request message to the storage for the needed resources. | AND (to G6) | Storage facility | 1 |
| **AT3 – Wait for Retrieval** | Wait until the requested resources are retrieved. | AND (to G7) | Storage facility | 1 |
| **AT4 – Pick Resource** | Pick up the retrieved resources. | AND (to G8) | Storage facility | 1 |
| **AT5 – Navigate to Delivery Location** | Move to the destination where resources must be delivered. | AND (to G11) | Destination | 1 |
| **AT6 – Deliver Resource** | Deliver the resources to the destination. | AND (to G12) | Destination | 1 |
| **AT7 – Go to Recharge Station** | Move to the charging station to recharge. | AND (to G16) | Recharge station | 1 |
| **AT8 – Assign Mission to Another Robot** | Assign the remaining task to another robot. | AND (to G17) | Current location | 1 |
| **AT9 – Return Resource to Checkpoint** | Return the resource to a checkpoint before battery depletion. | AND (to G19) | Checkpoint | 1 |
| **AT10 – Trigger Alert** | Trigger an alert when checkpoint return fails. | AND (to G22) | System | 1 |
| **AT11 – Send Report to Sector Manager** | Send a report of the failure to the sector manager. | AND (to G23) | Sector manager | 1 |
| **AT12 – Assign Multiple Robots to Parallel Tasks** | Assign multiple robots to parallel collection‑delivery tasks. | AND (to G25) | Current location | [1,3] |

---

### Summary of Logical Relationships

```
G1 -> G2, G9 [AND][;]
G2 -> G3, G4 [AND][;]
G3 -> – [leaf]
G4 -> G5, G6, G7, G8 [AND][;]
G5 -> AT1 [AND]
G6 -> AT2 [AND]
G7 -> AT3 [AND]
G8 -> AT4 [AND]
G9 -> G10, G12 [AND][;]
G10 -> G11, G12, G13 [AND][;]
G11 -> AT5 [AND]
G12 -> AT6 [AND]
G13 -> AT? [AND]   (optional)
G15 -> G16, G17 [AND][;]
G16 -> AT7 [AND]
G17 -> AT8 [AND]
G18 -> G19, G20 [AND][;]
G19 -> AT9 [AND]
G20 -> AT10 [AND]
G21 -> G22, G23 [AND][;]
G22 -> AT10 [AND]
G23 -> AT11 [AND]
G24 -> G25 [AND][#]
G25 -> AT12 [AND]
```

This goal‑task hierarchy captures all mission phases, battery‑management contingencies, failure handling, and parallel execution opportunities for a multi‑robot resource delivery system.
