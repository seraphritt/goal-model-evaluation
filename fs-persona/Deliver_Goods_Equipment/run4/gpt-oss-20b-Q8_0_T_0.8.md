**Goal Model – Multi‑Robot Resource Collection & Delivery**

| **Name** | **Text**                                                     | **Runtime**      | **Goal Type** | **Target Condition / Enquired Info**              | **Relation**        | **Ground truth I**                                        | **Ground truth C** | **Consensus**                                             |
| -------- | ------------------------------------------------------------ | ---------------- | ------------- | ------------------------------------------------- | ------------------- | --------------------------------------------------------- | ------------------ | --------------------------------------------------------- |
| **G1**   | Deliver all requested resources to the specified destination | `;` (sequential) | Achieve       | *All requested resources are at the destination.* | AND (to G2, G3, G5) | OK                                                        | Perform            | OK                                                        |
| **G2**   | Collection Phase – gather resources from storage             | `;`              | Perform       | –                                                 | AND (to G2.1–G2.5)  | Achieve. Target condition: all resources were collected.  | OK                 | Achieve. Target condition: all resources were collected.  |
| **G2.1** | Determine optimal collection order                           | `-`              | Perform       | –                                                 | AND (to AT1)        | OK                                                        | OK                 | OK                                                        |
| **G2.2** | Navigate to the appropriate storage                          | `-`              | Perform       | –                                                 | AND (to AT2)        | OK                                                        | OK                 | OK                                                        |
| **G2.3** | Request the specified resources                              | `-`              | Perform       | –                                                 | AND (to AT3)        | Query. Enqueried information: resources to be colleceted. | OK                 | Query. Enqueried information: resources to be colleceted. |
| **G2.4** | Wait until resources are retrieved                           | `-`              | Perform       | –                                                 | AND (to AT4)        | OK                                                        | OK                 | OK                                                        |
| **G2.5** | Monitor battery level during collection                      | `-`              | Perform       | –                                                 | AND (to AT5)        | OK                                                        | OK                 | OK                                                        |
| **G3**   | Delivery Phase – transport resources to the destination      | `;`              | Perform       | –                                                 | AND (to G3.1–G3.4)  | Achieve. Target condition: all resources were delivered.  | OK                 | Achieve. Target condition: all resources were delivered.  |
| **G3.1** | Transport collected resources to the destination             | `-`              | Perform       | –                                                 | AND (to AT6)        | OK                                                        | OK                 | OK                                                        |
| **G3.2** | Return to a checkpoint if battery is low                     | `-`              | Perform       | –                                                 | AND (to AT7)        | OK                                                        | OK                 | OK                                                        |
| **G3.3** | Monitor battery level during delivery                        | `-`              | Perform       | –                                                 | AND (to AT12)       | OK                                                        | OK                 | OK                                                        |
| **G3.4** | Assign the remaining task to another robot                   | `-`              | Perform       | –                                                 | AND (to AT8)        | OK                                                        | OK                 | OK                                                        |
| **G4**   | Failure Handling – react to delivery failures                | `;`              | Perform       | –                                                 | AND (to G4.1, G4.2) | OK                                                        | OK                 | OK                                                        |
| **G4.1** | Alert when a resource cannot be returned to a checkpoint     | `-`              | Perform       | –                                                 | AND (to AT9)        | OK                                                        | OK                 | OK                                                        |
| **G4.2** | Report the failure to the sector manager                     | `-`              | Perform       | –                                                 | AND (to AT10)       | OK                                                        | OK                 | OK                                                        |
| **G5**   | Parallel Task Coordination – enable multi-robot execution    | `-`              | Perform       | –                                                 | AND (to G5.1)       | OK                                                        | OK                 | OK                                                        |
| **G5.1** | Assign multiple robots for parallel collect-deliver tasks    | `-`              | Perform       | –                                                 | AND (to AT11)       | OK                                                        | OK                 | OK                                                        |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Compute optimal collection order based on waiting time and path length. | AND | Planning module (non‑physical) | 1 |
| **AT2** | Robot travels to the target storage location. | AND | Storage location (variable) | 1 |
| **AT3** | Robot sends a request message to the storage specifying the needed resources. | AND | Storage location | 1 |
| **AT4** | Robot waits until the storage has retrieved the requested resources. | AND | Storage location | 1 |
| **AT5** | Continuously monitor the robot’s battery during collection. | AND | Robot’s onboard system | 1 |
| **AT6** | Transport the collected resources from storage to the destination. | AND | Destination location | 1 |
| **AT7** | Return the resource to a checkpoint when battery drops below 30 % during delivery. | AND | Checkpoint location | 1 |
| **AT8** | Assign the remaining delivery task to another robot after returning to the checkpoint. | AND | Central control | 1 |
| **AT9** | Send an alert to the central control when a resource cannot be returned to the checkpoint. | AND | Central control | 1 |
| **AT10** | Send a detailed failure report to the sector manager. | AND | Central control | 1 |
| **AT11** | Allocate multiple robots to parallel collect‑deliver tasks to reduce overall mission time. | AND | Central control | [1, N] |
| **AT12** | Continuously monitor the robot’s battery during delivery. | AND | Robot’s onboard system | 1 |

---

### Summary Table (Goals + Tasks)

| **ID** | **Title** | **Type** | **Runtime** | **Relation** |
|--------|-----------|----------|-------------|--------------|
| G1 | Deliver Resources | Achieve | `;` | AND (G2, G3, G5) |
| G2 | Collection Phase | Perform | `;` | AND (G2.1–G2.5) |
| G2.1 | Determine Order | Perform | `-` | AND (AT1) |
| G2.2 | Navigate to Storage | Perform | `-` | AND (AT2) |
| G2.3 | Request Resources | Perform | `-` | AND (AT3) |
| G2.4 | Wait for Retrieval | Perform | `-` | AND (AT4) |
| G2.5 | Monitor Battery (Collect) | Perform | `-` | AND (AT5) |
| G3 | Delivery Phase | Perform | `;` | AND (G3.1–G3.4) |
| G3.1 | Transport to Destination | Perform | `-` | AND (AT6) |
| G3.2 | Return to Checkpoint | Perform | `-` | AND (AT7) |
| G3.3 | Monitor Battery (Deliver) | Perform | `-` | AND (AT12) |
| G3.4 | Assign Remaining Task | Perform | `-` | AND (AT8) |
| G4 | Failure Handling | Perform | `;` | AND (G4.1, G4.2) |
| G4.1 | Alert on Failure | Perform | `-` | AND (AT9) |
| G4.2 | Report to Manager | Perform | `-` | AND (AT10) |
| G5 | Parallel Coordination | Perform | `-` | AND (G5.1) |
| G5.1 | Assign Multiple Robots | Perform | `-` | AND (AT11) |
| AT1 | Compute Order | – | – | – |
| AT2 | Navigate | – | – | – |
| AT3 | Request | – | – | – |
| AT4 | Wait | – | – | – |
| AT5 | Monitor Battery (Collect) | – | – | – |
| AT6 | Transport | – | – | – |
| AT7 | Return to Checkpoint | – | – | – |
| AT8 | Re‑assign Task | – | – | – |
| AT9 | Send Alert | – | – | – |
| AT10 | Send Report | – | – | – |
| AT11 | Parallel Allocation | – | – | – |
| AT12 | Monitor Battery (Deliver) | – | – | – |

---

### Logical Relationships

```
G1  -> G2, G3, G5  [AND][;]
G2  -> G2.1, G2.2, G2.3, G2.4, G2.5  [AND][;]
G3  -> G3.1, G3.2, G3.3, G3.4  [AND][;]
G4  -> G4.1, G4.2  [AND][;]
G5  -> G5.1  [AND][-]
G2.1 -> AT1  [AND][-]
G2.2 -> AT2  [AND][-]
G2.3 -> AT3  [AND][-]
G2.4 -> AT4  [AND][-]
G2.5 -> AT5  [AND][-]
G3.1 -> AT6  [AND][-]
G3.2 -> AT7  [AND][-]
G3.3 -> AT12 [AND][-]
G3.4 -> AT8  [AND][-]
G4.1 -> AT9  [AND][-]
G4.2 -> AT10 [AND][-]
G5.1 -> AT11 [AND][-]
```

*The runtime annotations (`;`, `#`, `-`) indicate sequential execution, parallel execution, or leaf goals/tasks, respectively.*
