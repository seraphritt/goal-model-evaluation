**Goal Model – Multi‑Robot Resource Delivery Mission**

| **Name**     | **Text**                                    | **Runtime**                   | **Goal Type** | **Target Condition / Enquired Info**                                                        | **Relation**                      | **Justification**                                                                            | Ground truth I                                           | Ground truth C | Consensus                                                |
| ------------ | ------------------------------------------- | ----------------------------- | ------------- | ------------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------------- | -------------------------------------------------------- |
| **G1**       | Complete Resource Delivery Mission          | `;`                           | Achieve       | “All requested resources are at the destination and the requesting agent confirms receipt.” | –                                 | This is the overall mission objective that must be achieved before the system can terminate. | Perform.                                                 | OK             | Perform.                                                 |
| **G2**       | Collect Required Resources                  | `FALLBACK(G2.1,G2.5)`         | Perform       | –                                                                                           | AND (between G2 and its children) | Collection must be completed before delivery; fallback is used when battery is low.          | Achieve. Target condition: all resources were collected. | OK             | Achieve. Target condition: all resources were collected. |
| **G2.1**     | Perform Collection Process                  | `;`                           | Perform       | –                                                                                           | AND                               | The collection process consists of a sequence of actions that must all be performed.         | OK                                                       | OK             | OK                                                       |
| **G2.1.1**   | Navigate to Storage                         | `-`                           | Perform       | –                                                                                           | AND                               | Robot must physically reach the storage to request resources.                                | OK                                                       | OK             | OK                                                       |
| **G2.1.2**   | Request Resource                            | `-`                           | Perform       | –                                                                                           | AND                               | The request triggers the storage to retrieve the items.                                      | Query. Enquired info: items to be retrieved.             | OK             | Query. Enquired info: items to be retrieved.             |
| **G2.1.3**   | Wait for Retrieval                          | `-`                           | Perform       | –                                                                                           | AND                               | The robot must wait until the storage has the items ready for pickup.                        | OK                                                       | OK             | OK                                                       |
| **G2.5**     | Assign Mission to Another Robot             | `AND`                         | Perform       | –                                                                                           | OR (fallback alternative)         | When battery <10 % the mission is transferred to another robot.                              | OK                                                       | OK             | OK                                                       |
| **G2.5.1**   | Return to Recharging Station                | `-`                           | Perform       | –                                                                                           | AND                               | Robot must recharge before it can be reassigned.                                             | OK                                                       | OK             | OK                                                       |
| **G2.5.2**   | Assign Mission to Another Robot             | `-`                           | Perform       | –                                                                                           | AND                               | The robot informs the central system to hand over the task.                                  | OK                                                       | OK             | OK                                                       |
| **G3**       | Deliver Resources to Destination            | `FALLBACK(G3.1,G3.5)`         | Perform       | –                                                                                           | AND                               | Delivery must be completed; fallback handles low-battery situations.                         | Achieve. Target condition: all resources were delivered. | OK             | Achieve. Target condition: all resources were delivered. |
| **G3.1**     | Perform Delivery Process                    | `;`                           | Perform       | –                                                                                           | AND                               | Loading, transport and delivery are sequential steps.                                        | OK                                                       | OK             | OK                                                       |
| **G3.1.1**   | Load Resource onto Robot                    | `-`                           | Perform       | –                                                                                           | AND                               | The robot must pick up the resource before moving it.                                        | OK                                                       | OK             | OK                                                       |
| **G3.1.2**   | Transport Resource to Destination           | `-`                           | Perform       | –                                                                                           | AND                               | The robot must move the resource to the delivery location.                                   | OK                                                       | OK             | OK                                                       |
| **G3.1.3**   | Deliver Resource                            | `-`                           | Perform       | –                                                                                           | AND                               | Final hand-over to the requesting agent.                                                     | OK                                                       | OK             | OK                                                       |
| **G3.5**     | Assign Remaining Delivery to Another Robot  | `AND`                         | Perform       | –                                                                                           | OR (fallback alternative)         | When battery <30 % the remaining delivery is handed over.                                    | OK                                                       | OK             | OK                                                       |
| **G3.5.1**   | Return Resource to Checkpoint or Send Alert | `FALLBACK(G3.5.1.1,G3.5.1.2)` | Perform       | –                                                                                           | OR                                | Two possible outcomes: successful return or failure that triggers an alert.                  | OK                                                       | OK             | OK                                                       |
| **G3.5.1.1** | Return Resource to Checkpoint               | `-`                           | Perform       | –                                                                                           | AND                               | The resource must be safely returned to a checkpoint.                                        | OK                                                       | OK             | OK                                                       |
| **G3.5.1.2** | Send Alert to Sector Manager                | `-`                           | Perform       | –                                                                                           | AND                               | Triggered if the robot cannot return the resource.                                           | OK                                                       | OK             | OK                                                       |
| **G3.5.2**   | Assign Remaining Delivery to Another Robot  | `-`                           | Perform       | –                                                                                           | AND                               | The robot informs the central system to hand over the rest of the delivery.                  | OK                                                       | OK             | OK                                                       |
| **G4**       | Parallel Collect-Deliver Tasks              | `#`                           | Perform       | –                                                                                           | AND                               | Parallelism reduces overall mission time when multiple items are required.                   | OK                                                       | OK             | OK                                                       |
| **G4.1**     | Assign Multiple Robots to Collection        | `-`                           | Perform       | –                                                                                           | AND                               | Multiple robots can simultaneously collect from different storages.                          | OK                                                       | OK             | OK                                                       |
| **G4.2**     | Assign Multiple Robots to Delivery          | `-`                           | Perform       | –                                                                                           | AND                               | Multiple robots can simultaneously deliver to different destinations.                        | OK                                                       | OK             | OK                                                       |

---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Navigate to Storage | AND | storage | 1 | A single robot must reach the storage to request resources. |
| **AT2** | Send Request Message | AND | robot’s current location | 1 | Only the robot at the storage sends the request. |
| **AT3** | Wait for Retrieval | AND | storage | 1 | The robot must wait at the storage until the items are ready. |
| **AT4** | Return to Recharging Station | AND | recharging station | 1 | The robot must recharge before it can be reassigned. |
| **AT5** | Assign Mission to Another Robot | AND | central command | 1 | The robot informs the central system to hand over the task. |
| **AT6** | Send Alert to Sector Manager | AND | central command | 1 | Alert is sent if the robot cannot return the resource. |
| **AT7** | Load Resource onto Robot | AND | storage | 1 | The robot picks up the resource before transport. |
| **AT8** | Transport Resource to Destination | AND | destination | 1 | The robot moves the resource to the delivery location. |
| **AT9** | Return Resource to Checkpoint | AND | checkpoint | 1 | The robot must return the resource to a safe location. |
| **AT10** | Assign Remaining Delivery to Another Robot | AND | central command | 1 | The robot informs the central system to hand over the rest of the delivery. |
| **AT11** | Send Alert if Failure to Return to Checkpoint | AND | central command | 1 | Triggered when the robot cannot return the resource. |
| **AT12** | Assign Robot to Storage (Parallel) | AND | storage | [1,n] | Multiple robots can be assigned to different storages concurrently. |
| **AT13** | Assign Robot to Delivery (Parallel) | AND | destination | [1,n] | Multiple robots can be assigned to deliver concurrently. |

---

### Summary Table (Goals & Tasks)

| **ID** | **Type** | **Title** | **Runtime / Relation** |
|--------|----------|-----------|------------------------|
| G1 | Goal | Complete Resource Delivery Mission | `;` |
| G2 | Goal | Collect Required Resources | `FALLBACK(G2.1,G2.5)` |
| G2.1 | Goal | Perform Collection Process | `;` |
| G2.1.1 | Goal | Navigate to Storage | `-` |
| G2.1.2 | Goal | Request Resource | `-` |
| G2.1.3 | Goal | Wait for Retrieval | `-` |
| G2.5 | Goal | Assign Mission to Another Robot | `AND` |
| G2.5.1 | Goal | Return to Recharging Station | `-` |
| G2.5.2 | Goal | Assign Mission to Another Robot | `-` |
| G3 | Goal | Deliver Resources to Destination | `FALLBACK(G3.1,G3.5)` |
| G3.1 | Goal | Perform Delivery Process | `;` |
| G3.1.1 | Goal | Load Resource onto Robot | `-` |
| G3.1.2 | Goal | Transport Resource to Destination | `-` |
| G3.1.3 | Goal | Deliver Resource | `-` |
| G3.5 | Goal | Assign Remaining Delivery to Another Robot | `AND` |
| G3.5.1 | Goal | Return Resource to Checkpoint or Send Alert | `FALLBACK(G3.5.1.1,G3.5.1.2)` |
| G3.5.1.1 | Goal | Return Resource to Checkpoint | `-` |
| G3.5.1.2 | Goal | Send Alert to Sector Manager | `-` |
| G3.5.2 | Goal | Assign Remaining Delivery to Another Robot | `-` |
| G4 | Goal | Parallel Collect‑Deliver Tasks | `#` |
| G4.1 | Goal | Assign Multiple Robots to Collection | `-` |
| G4.2 | Goal | Assign Multiple Robots to Delivery | `-` |
| AT1 | Task | Navigate to Storage | AND |
| AT2 | Task | Send Request Message | AND |
| AT3 | Task | Wait for Retrieval | AND |
| AT4 | Task | Return to Recharging Station | AND |
| AT5 | Task | Assign Mission to Another Robot | AND |
| AT6 | Task | Send Alert to Sector Manager | AND |
| AT7 | Task | Load Resource onto Robot | AND |
| AT8 | Task | Transport Resource to Destination | AND |
| AT9 | Task | Return Resource to Checkpoint | AND |
| AT10 | Task | Assign Remaining Delivery to Another Robot | AND |
| AT11 | Task | Send Alert if Failure to Return to Checkpoint | AND |
| AT12 | Task | Assign Robot to Storage (Parallel) | AND |
| AT13 | Task | Assign Robot to Delivery (Parallel) | AND |

---

### Logical Relationships

| **Parent → Children** | **Relation** | **Justification** |
|-----------------------|--------------|-------------------|
| G1 → G2, G3, G4 | AND | All three phases (collection, delivery, parallelism) must be completed for the mission to succeed. |
| G2 → G2.1, G2.5 | OR (fallback) | Normal collection or fallback to reassign mission when battery <10 %. |
| G2.1 → G2.1.1, G2.1.2, G2.1.3 | AND | Navigation, request, and wait must occur sequentially. |
| G2.5 → G2.5.1, G2.5.2 | AND | Must recharge before reassigning. |
| G3 → G3.1, G3.5 | OR (fallback) | Normal delivery or fallback to reassign when battery <30 %. |
| G3.1 → G3.1.1, G3.1.2, G3.1.3 | AND | Loading, transport, delivery are sequential. |
| G3.5 → G3.5.1, G3.5.2 | AND | Must return to checkpoint (or alert) before reassigning. |
| G3.5.1 → G3.5.1.1, G3.5.1.2 | OR (fallback) | Either successful return or alert if failure. |
| G4 → G4.1, G4.2 | AND (parallel) | Parallel collection and delivery tasks run concurrently. |
| G2.1.1 → AT1 | AND | The navigation goal is realized by the navigation task. |
| G2.1.2 → AT2 | AND | The request goal is realized by the request task. |
| G2.1.3 → AT3 | AND | The wait goal is realized by the wait task. |
| G2.5.1 → AT4 | AND | The recharge goal is realized by the recharge task. |
| G2.5.2 → AT5 | AND | The reassign goal is realized by the reassign task. |
| G3.1.1 → AT7 | AND | Loading goal realized by loading task. |
| G3.1.2 → AT8 | AND | Transport goal realized by transport task. |
| G3.1.3 → – | – | Delivery is the final state; no explicit task needed. |
| G3.5.1.1 → AT9 | AND | Return to checkpoint realized by return task. |
| G3.5.1.2 → AT6 | AND | Alert goal realized by alert task. |
| G3.5.2 → AT10 | AND | Reassign remaining delivery realized by reassign task. |
| G4.1 → AT12 | AND | Parallel collection assignment realized by task. |
| G4.2 → AT13 | AND | Parallel delivery assignment realized by task. |

---

**Justifications Overview**

* **Sequential vs. Parallel** – Collection and delivery steps must happen in order, so `;` is used. Parallelism is only employed when multiple items are involved, so `#` is chosen for G4.  
* **Fallback** – Battery‑driven contingencies are modeled with `FALLBACK`, reflecting the mission’s explicit “if battery low” clauses.  
* **Goal Types** – All high‑level objectives are **Perform** goals because they require concrete actions. The top‑level mission is an **Achieve** goal because it specifies a desired world state. No **Query** goals are needed as the mission does not require passive information retrieval.  
* **Task Allocation** – Each task is assigned to a single robot unless the description explicitly allows multiple robots (parallel assignments), in which case a range `[1,n]` is used. Locations are taken directly from the mission text (storage, recharging station, checkpoint, central command).  

This goal–task decomposition captures the mission’s structure, contingencies, and parallelism, providing a clear blueprint for multi‑robot coordination.
