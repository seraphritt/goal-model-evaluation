## 1. Goal Model – Tables

| **Name**                                         | **Text**                                                                                                                  | **Runtime**                        | **Goal Type** | **Target Condition / Enquired Information** | **Relation** | **Justification**                                                        | **Ground truth I**                                      | **Ground truth C** | **Ground truth E** |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------- | ------------------------------------------- | ------------ | ------------------------------------------------------------------------ | ------------------------------------------------------- | ------------------ | ------------------ |
| **G1: Deliver Requested Resources**              | Deliver the requested resources to the specified location.                                                                | `;` (sequential)                   | Perform       | –                                           | **AND**      | Collection must finish before delivery can start.                        | OK                                                      | Ok                   |                    |
| **G2: Collect Resources**                        | Gather the requested resources from the storage locations.                                                                | `FALLBACK(G2.1, G2.3)`             | Perform       | –                                           | **FALLBACK** | Normal collection (`G2.1`) or low-battery re-assignment (`G2.3`).        | Achieve. Target condition: all resources were collected | Ok                   |                    |
| **G2.1: Plan Collection**                        | Estimate waiting time, compute a path, and decide on the next storage.                                                    | `;`                                | Perform       | –                                           | **AND**      | Both time estimation and path calculation are required before moving.    | OK                                                      | Ok                   |                    |
| **G2.2: Request Resources**                      | Send a request to the storage and wait for the resources to be retrieved.                                                 | `;`                                | Perform       | –                                           | **AND**      | Sending and waiting are two consecutive steps.                           | OK                                                      | Ok                   |                    |
| **G2.3: Handle Low Battery (Collection)**        | If the battery falls below 10 % the robot returns to recharge and hands the mission over.                                 | `;`                                | Perform       | –                                           | **AND**      | Return to recharge **and** notify another robot are both mandatory.      | OK                                                      | Ok                   |                    |
| **G3: Deliver Resources**                        | Transport the collected resources to the destination.                                                                     | `FALLBACK(G3.1, G3.2)`             | Perform       | –                                           | **FALLBACK** | Normal delivery (`G3.1`) or low-battery handling (`G3.2`).               | Achieve. Target condition: all resources were delivered | Ok                   |                    |
| **G3.1: Transport Resources to Destination**     | Move the resources from storage to the specified location.                                                                | `;`                                | Perform       | –                                           | **AND**      | Loading **and** navigation are required.                                 | OK                                                      | Ok                   |                    |
| **G3.2: Handle Low Battery (Delivery)**          | If the battery falls below 30 % return the resource to a checkpoint, hand over the rest of the task, or trigger an alert. | `FALLBACK( (G3.3 ; G3.4) , G3.5 )` | Perform       | –                                           | **FALLBACK** | Successful return & hand-over (`G3.3 ; G3.4`) or failure alert (`G3.5`). | OK                                                      | Ok                   |                    |
| **G3.3: Return Resource to Checkpoint**          | Return the resource to a safe checkpoint.                                                                                 | `;`                                | Perform       | –                                           | **AND**      | Navigation **and** drop are consecutive.                                 | OK                                                      | Ok                   |                    |
| **G3.4: Assign Remaining Task to Another Robot** | Inform another robot of the remaining delivery work.                                                                      | `;`                                | Perform       | –                                           | **AND**      | Identifying the robot **and** transferring the task are both needed.     | OK                                                      | Ok                   |                    |
| **G3.5: Trigger Alert on Failure**               | If the robot cannot return the resource, send an alert to the sector manager.                                             | `-`                                | Perform       | –                                           | **AND**      | The alert is a single action.                                            | OK                                                      | Ok                   |                    |


---

## 2. Task Model – Tables

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|---|---|---|---|---|---|
| **AT1: Retrieve Storage Info** | Query the storage location and available resources. | **AND** | *storage* | 1 | Only the robot that will collect the resources needs to know the inventory. |
| **AT2: Compute Path to Storage** | Calculate the shortest path to the chosen storage while considering waiting time. | **AND** | *robot’s current location* | 1 | Path planning is done by the same robot that will travel. |
| **AT3: Send Request Message** | Send a message to the storage with the exact resource specification. | **AND** | *robot at storage* | 1 | The requesting robot must be physically present to send the message. |
| **AT4: Wait for Retrieval** | Await confirmation that the resources have been retrieved. | **AND** | *robot at storage* | 1 | Waiting is a passive action performed by the same robot. |
| **AT5: Return to Recharge Station** | Navigate back to the nearest charging station. | **AND** | *RechargeStation* | 1 | The robot must physically return to recharge. |
| **AT6: Notify Other Robot** | Inform a different robot that it can take over the mission. | **AND** | *robot at recharge* | 1 | The robot that is recharging must notify the control‑center. |
| **AT7: Load Resources** | Pick up the requested resources from the storage. | **AND** | *storage* | 1 | Only one robot can load the resources at a time. |
| **AT8: Navigate to Destination** | Travel from storage to the specified delivery location. | **AND** | *destination* | 1 | The robot that loaded the resources must move to the destination. |
| **AT9: Navigate to Checkpoint** | Travel to the pre‑designated checkpoint. | **AND** | *Checkpoint* | 1 | The robot must physically reach the checkpoint. |
| **AT10: Drop Resource** | Place the resource at the checkpoint. | **AND** | *Checkpoint* | 1 | The robot that brought the resource must drop it. |
| **AT11: Identify Available Robot** | Query the control‑center for an idle robot. | **AND** | *ControlCenter* | 1 | The robot that is returning to the checkpoint must ask for help. |
| **AT12: Transfer Task** | Assign the remaining delivery task to the identified robot. | **AND** | *ControlCenter* | 1 | The robot that is recharging must transfer the task. |
| **AT13: Send Alert to Sector Manager** | Notify the sector manager that the robot failed to return the resource. | **AND** | *SectorManager* | 1 | The robot that cannot return the resource must trigger an alert. |
| **AT14: Report Failure** | Send a failure report to the sector manager. | **AND** | *SectorManager* | 1 | The alert and report are two consecutive actions. |

---

## 3. Summary Table – All Goals and Tasks

| **ID** | **Type** | **Title** | **Parent** | **Relation** | **Runtime / Justification** |
|---|---|---|---|---|---|
| G1 | Goal | Deliver Requested Resources | – | AND | `;` (collection then delivery) |
| G2 | Goal | Collect Resources | G1 | AND | `FALLBACK(G2.1, G2.3)` |
| G2.1 | Goal | Plan Collection | G2 | AND | `;` |
| G2.2 | Goal | Request Resources | G2 | AND | `;` |
| G2.3 | Goal | Handle Low Battery (Collection) | G2 | AND | `;` |
| G3 | Goal | Deliver Resources | G1 | AND | `FALLBACK(G3.1, G3.2)` |
| G3.1 | Goal | Transport Resources to Destination | G3 | AND | `;` |
| G3.2 | Goal | Handle Low Battery (Delivery) | G3 | AND | `FALLBACK((G3.3 ; G3.4), G3.5)` |
| G3.3 | Goal | Return Resource to Checkpoint | G3.2 | AND | `;` |
| G3.4 | Goal | Assign Remaining Task to Another Robot | G3.2 | AND | `;` |
| G3.5 | Goal | Trigger Alert on Failure | G3.2 | AND | `-` |
| AT1 | Task | Retrieve Storage Info | G2.1 | AND | – |
| AT2 | Task | Compute Path to Storage | G2.1 | AND | – |
| AT3 | Task | Send Request Message | G2.2 | AND | – |
| AT4 | Task | Wait for Retrieval | G2.2 | AND | – |
| AT5 | Task | Return to Recharge Station | G2.3 | AND | – |
| AT6 | Task | Notify Other Robot | G2.3 | AND | – |
| AT7 | Task | Load Resources | G3.1 | AND | – |
| AT8 | Task | Navigate to Destination | G3.1 | AND | – |
| AT9 | Task | Navigate to Checkpoint | G3.3 | AND | – |
| AT10 | Task | Drop Resource | G3.3 | AND | – |
| AT11 | Task | Identify Available Robot | G3.4 | AND | – |
| AT12 | Task | Transfer Task | G3.4 | AND | – |
| AT13 | Task | Send Alert to Sector Manager | G3.5 | AND | – |
| AT14 | Task | Report Failure | G3.5 | AND | – |

---

## 4. Logical Relationships – Narrative

1. **G1 → G2, G3**  
   *Relation:* **AND** (sequential `;`)  
   *Justification:* The mission requires that all resources be collected *before* they can be delivered. Therefore, both sub‑goals must be fulfilled in order.

2. **G2 → G2.1, G2.2, G2.3**  
   *Relation:* **FALLBACK** (`FALLBACK(G2.1, G2.3)`)  
   *Justification:* Under normal conditions the robot follows the plan (`G2.1`) and then requests the resources (`G2.2`). If the battery drops below 10 %, the robot must instead return to recharge and hand over the mission (`G2.3`). The fallback captures this alternative path.

3. **G2.1 → AT1, AT2**  
   *Relation:* **AND** (`;`)  
   *Justification:* Estimating waiting time and computing the path are two necessary sequential steps before moving to the storage.

4. **G2.2 → AT3, AT4**  
   *Relation:* **AND** (`;`)  
   *Justification:* The robot must first send a request and then wait for confirmation before proceeding.

5. **G2.3 → AT5, AT6**  
   *Relation:* **AND** (`;`)  
   *Justification:* The robot must return to recharge *and* notify another robot; both are mandatory for safe hand‑over.

6. **G3 → G3.1, G3.2**  
   *Relation:* **FALLBACK** (`FALLBACK(G3.1, G3.2)`)  
   *Justification:* Normal delivery (`G3.1`) is attempted first; if the battery falls below 30 % the robot must handle the low‑battery case (`G3.2`).

7. **G3.1 → AT7, AT8**  
   *Relation:* **AND** (`;`)  
   *Justification:* Loading the resources and then navigating to the destination are sequential.

8. **G3.2 → G3.3, G3.4, G3.5**  
   *Relation:* **FALLBACK** (`FALLBACK((G3.3 ; G3.4), G3.5)`)  
   *Justification:* The robot first attempts to return to a checkpoint and hand over the task; if that fails, it must trigger an alert.

9. **G3.3 → AT9, AT10**  
   *Relation:* **AND** (`;`)  
   *Justification:* Navigation to the checkpoint and dropping the resource are consecutive.

10. **G3.4 → AT11, AT12**  
    *Relation:* **AND** (`;`)  
    *Justification:* Identifying an available robot and transferring the task are sequential.

11. **G3.5 → AT13, AT14**  
    *Relation:* **AND** (`;`)  
    *Justification:* Sending an alert and reporting a failure are consecutive.

---

### Final Remarks

- **Parallelism** (`#`) is not explicitly used in the core mission flow because the description does not mandate simultaneous actions in a single robot’s workflow. However, the *fallback* constructs capture the possibility of hand‑over and parallel task allocation when multiple items are involved.  
- All goals and tasks are **AND**‑related unless a clear alternative path is described (captured by **FALLBACK**).  
- The model is **depth‑first** numbered, ensuring a unique identifier for every node.  
- Each task’s **Location** and **Number of Robots** are justified by the mission’s operational constraints.  

This goal model can now be instantiated in a multi‑robot planning system, enabling automatic decomposition, scheduling, and fault‑tolerance handling.
