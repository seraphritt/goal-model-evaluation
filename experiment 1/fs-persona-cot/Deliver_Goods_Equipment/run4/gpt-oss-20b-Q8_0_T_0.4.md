## 1. Goal Model – Tables

| **Name**                                     | **Text**                                                     | **Runtime**            | **Goal Type** | **Target Condition**                                            | **Enquired Information** | **Relation**                   | **Justification**                                                                                                                                                                                | **Ground truth I**                                      | **Ground truth C** | **Consensus**                                           |
| -------------------------------------------- | ------------------------------------------------------------ | ---------------------- | ------------- | --------------------------------------------------------------- | ------------------------ | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | ------------------ | ------------------------------------------------------- |
| **G1 – Complete Resource Delivery Mission**  | Bring all requested resources to the specified destinations. | `#` (parallel)         | Achieve       | *All requested resources delivered to the specified locations.* | –                        | AND between G2 and G3          | The mission naturally splits into a *collection* phase and a *delivery* phase. For different items, distinct robots can perform these phases concurrently, so a parallel execution is justified. | OK                                                      | Perform            | OK                                                      |
| **G2 – Collect Resources**                   | Gather the required resources from storage.                  | `FALLBACK(G2.1, G2.2)` | Perform       | –                                                               | –                        | FALLBACK between G2.1 and G2.2 | Normal collection may fail if the robot’s battery drops below 10 %. The fallback guarantees that the mission continues by invoking the low-battery handling branch.                              | Achieve. Target condition: all resources were collected | Ok                 | Achieve. Target condition: all resources were collected |
| **G2.1 – Normal Collection**                 | Execute the standard collection workflow.                    | `;` (sequential)       | Perform       | –                                                               | –                        | AND between AT1, AT2, AT3      | The robot must *navigate → request → retrieve* in this order; thus a sequential AND is appropriate.                                                                                              | OK                                                      | Ok                 | OK                                                      |
| **G2.2 – Low-Battery Handling (Collection)** | Handle a low-battery situation during collection.            | `;` (sequential)       | Perform       | –                                                               | –                        | AND between AT6, AT8           | The robot first *returns to recharge* and then *assigns the mission* to another robot – a strict sequence.                                                                                       | OK                                                      | Ok                 | OK                                                      |
| **G3 – Deliver Resources**                   | Transport the collected resources to the requested location. | `FALLBACK(G3.1, G3.2)` | Perform       | –                                                               | –                        | FALLBACK between G3.1 and G3.2 | Delivery may fail if the battery drops below 30 %. The fallback ensures the mission continues by invoking the low-battery handling branch.                                                       | Achieve. Target condition: all resources were delivered | Ok                 | Achieve. Target condition: all resources were delivered |
| **G3.1 – Normal Delivery**                   | Execute the standard delivery workflow.                      | `;` (sequential)       | Perform       | –                                                               | –                        | AND between AT4, AT5           | The robot must *navigate → deliver* in this order; thus a sequential AND is appropriate.                                                                                                         | OK                                                      | Ok                 | OK                                                      |
| **G3.2 – Low-Battery Handling (Delivery)**   | Handle a low-battery situation during delivery.              | `;` (sequential)       | Perform       | –                                                               | –                        | AND between AT7, AT8, AT9      | The robot must *return to checkpoint → assign mission → trigger alert* in a strict order.                                                                                                        | OK                                                      | Ok                 | OK                                                      |


---

## 2. Task Model – Tables

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1 – Navigate to Storage** | Robot moves from its current location to the storage where the resource is located. | AND (with AT2, AT3) | *Storage* | 1 | Only one robot is needed to perform the navigation. |
| **AT2 – Request Resource** | Robot sends a message to the storage specifying the required resources and waits for confirmation. | AND (with AT1, AT3) | *Storage* | 1 | The request is a single, atomic action carried out by the robot that requested the resource. |
| **AT3 – Retrieve Resource** | Robot physically picks up the resource from the storage. | AND (with AT1, AT2) | *Storage* | 1 | Retrieval is performed by the same robot that requested the resource. |
| **AT4 – Navigate to Delivery Location** | Robot moves from the storage to the location where the resource must be delivered. | AND (with AT5) | *Delivery Location* | 1 | A single robot carries the resource to the destination. |
| **AT5 – Deliver Resource** | Robot hands the resource to the requesting agent at the delivery location. | AND (with AT4) | *Delivery Location* | 1 | Delivery is a one‑step action performed by the robot that has arrived. |
| **AT6 – Return to Recharge Station** | Robot returns to the charging station because its battery fell below 10 %. | AND (with AT8) | *Recharge Station* | 1 | The robot must recharge before it can continue the mission. |
| **AT7 – Return Resource to Checkpoint** | Robot brings the partially delivered resource back to a checkpoint because its battery fell below 30 %. | AND (with AT8, AT9) | *Checkpoint* | 1 | The resource must be safely stored before reassigning the task. |
| **AT8 – Assign Mission to Another Robot** | Robot informs the command center (or a central manager) to hand over the remaining task to another robot. | AND (with AT6 or AT7) | *Command Center* | 1 | Only the robot that detected the low battery performs the assignment. |
| **AT9 – Trigger Alert to Sector Manager** | If the robot cannot return the resource to the checkpoint, an alert is sent to the sector manager. | AND (with AT7) | *Sector Manager* | 1 | The alert is a necessary safety measure when the checkpoint return fails. |

---

## 3. Summary Table (All Goals & Tasks)

| **Type** | **ID** | **Title** | **Key Relation** | **Runtime / Justification** |
|----------|--------|-----------|------------------|-----------------------------|
| Goal | G1 | Complete Resource Delivery Mission | AND (G2, G3) | `#` – parallel execution of collection and delivery for different items |
| Goal | G2 | Collect Resources | FALLBACK (G2.1, G2.2) | Handles normal vs low‑battery collection |
| Goal | G2.1 | Normal Collection | AND (AT1, AT2, AT3) | Sequential navigation → request → retrieve |
| Goal | G2.2 | Low‑Battery Handling (Collection) | AND (AT6, AT8) | Return to recharge → assign mission |
| Goal | G3 | Deliver Resources | FALLBACK (G3.1, G3.2) | Handles normal vs low‑battery delivery |
| Goal | G3.1 | Normal Delivery | AND (AT4, AT5) | Sequential navigation → deliver |
| Goal | G3.2 | Low‑Battery Handling (Delivery) | AND (AT7, AT8, AT9) | Return to checkpoint → assign mission → trigger alert |
| Task | AT1 | Navigate to Storage | AND | Single robot navigation |
| Task | AT2 | Request Resource | AND | Single robot request |
| Task | AT3 | Retrieve Resource | AND | Single robot retrieval |
| Task | AT4 | Navigate to Delivery Location | AND | Single robot navigation |
| Task | AT5 | Deliver Resource | AND | Single robot delivery |
| Task | AT6 | Return to Recharge Station | AND | Single robot recharge |
| Task | AT7 | Return Resource to Checkpoint | AND | Single robot checkpoint return |
| Task | AT8 | Assign Mission to Another Robot | AND | Single robot assignment |
| Task | AT9 | Trigger Alert to Sector Manager | AND | Single robot alert |

---

## 4. Logical Relationships (Explicit)

```
G1 -> G2, G3 [AND][#]
   - Justification: The mission can be split into collection and delivery phases that can run in parallel for different items, reducing overall mission time.

G2 -> G2.1, G2.2 [FALLBACK][;]
   - Justification: Normal collection may fail if battery <10 %. The fallback ensures low‑battery handling is invoked.

G2.1 -> AT1, AT2, AT3 [AND][;]
   - Justification: Navigation, request, and retrieval must happen in sequence.

G2.2 -> AT6, AT8 [AND][;]
   - Justification: The robot must first return to recharge, then assign the mission.

G3 -> G3.1, G3.2 [FALLBACK][;]
   - Justification: Normal delivery may fail if battery <30 %. The fallback handles this.

G3.1 -> AT4, AT5 [AND][;]
   - Justification: Navigation to delivery location and actual delivery must occur sequentially.

G3.2 -> AT7, AT8, AT9 [AND][;]
   - Justification: The robot must return the resource to a checkpoint, assign the task, and trigger an alert if the return fails.

G2.1 -> AT1 [AND]
G2.1 -> AT2 [AND]
G2.1 -> AT3 [AND]
G2.2 -> AT6 [AND]
G2.2 -> AT8 [AND]
G3.1 -> AT4 [AND]
G3.1 -> AT5 [AND]
G3.2 -> AT7 [AND]
G3.2 -> AT8 [AND]
G3.2 -> AT9 [AND]
```

---

### Key Take‑aways

* **Parallelism** is captured at the top level (G1) to reflect the ability of multiple robots to work on different items simultaneously.
* **Fallbacks** are used to model battery‑driven contingencies, ensuring the mission can continue even when a robot cannot finish its current phase.
* **Sequential AND** relations within each sub‑goal enforce the strict ordering of actions required by the mission description.
* **Task properties** (Location, Number of Robots) are set to the minimal values needed for each action, as only one robot is required for each individual step.
