## 1. Goal Model – Detailed Tables  

| **Name**                                    | **Text**                                                          | **Runtime**      | **Goal Type** | **Target Condition / Enquired Information**               | **Relation** | **Justification**                                                                                                         | **Ground truth I**                                      | **Ground truth C** | **Consensus**                                           |
| ------------------------------------------- | ----------------------------------------------------------------- | ---------------- | ------------- | --------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------ | ------------------------------------------------------- |
| **G1: Deliver Requested Resources**         | Achieve delivery of requested resources to the destination agent. | `;` (sequential) | Achieve       | *Resources delivered to destination and agent satisfied.* | AND          | Collection must finish before delivery starts; both phases are required for mission success.                              | OK                                                      | Perform            | OK                                                      |
| **G2: Perform Collection**                  | Perform collection of all required resources from the storages.   | `#` (parallel)   | Perform       | –                                                         | AND          | Multiple items can be collected simultaneously by different robots; battery-low handling is part of the collection phase. | Achieve. Target condition: all resources were collected | Ok                 | Achieve. Target condition: all resources were collected |
| **G2.1: Collect from Storage A**            | Collect resource from storage A.                                  | `;` (sequential) | Perform       | –                                                         | AND          | The robot must go, request, and wait in that order.                                                                       | OK                                                      | Ok                 | OK                                                      |
| **G2.2: Collect from Storage B**            | Collect resource from storage B.                                  | `;` (sequential) | Perform       | –                                                         | AND          | Same sequence of actions as G2.1.                                                                                         | OK                                                      | Ok                 | OK                                                      |
| **G2.3: Battery Low Handling (Collection)** | Handle a low-battery situation during collection.                 | `;` (sequential) | Perform       | –                                                         | AND          | The robot must first return to recharge, then hand the task over.                                                         | OK                                                      | Ok                 | OK                                                      |
| **G3: Perform Delivery**                    | Perform delivery of all collected resources to the destination.   | `#` (parallel)   | Perform       | –                                                         | AND          | Multiple deliveries can be carried out in parallel; battery-low handling is part of the delivery phase.                   | OK                                                      | Ok                 | OK                                                      |
| **G3.1: Deliver Item 1**                    | Deliver the first collected resource to the destination.          | `;` (sequential) | Perform       | –                                                         | AND          | The robot must run to the destination and hand over the item.                                                             | OK                                                      | Ok                 | OK                                                      |
| **G3.2: Deliver Item 2**                    | Deliver the second collected resource to the destination.         | `;` (sequential) | Perform       | –                                                         | AND          | Same sequence as G3.1.                                                                                                    | OK                                                      | Ok                 | OK                                                      |
| **G3.3: Battery Low Handling (Delivery)**   | Handle a low-battery situation during delivery.                   | `;` (sequential) | Perform       | –                                                         | AND          | The robot must return the item to a checkpoint, hand the task over, and trigger an alert if the return fails.             | OK                                                      | Ok                 | OK                                                      |

---

## 2. Task Model – Detailed Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1: Go to Storage A** | Robot moves to storage A to collect the resource. | AND | Storage A | 1 | A single robot performs the movement. |
| **AT2: Request Resource** | Robot sends a request message to storage A. | AND | Storage A | 1 | Communication is performed by the same robot. |
| **AT3: Wait for Retrieval** | Robot waits until the resource is retrieved. | AND | Storage A | 1 | Waiting is a passive activity performed by the robot. |
| **AT4: Go to Storage B** | Robot moves to storage B to collect the resource. | AND | Storage B | 1 | Same reasoning as AT1. |
| **AT5: Request Resource** | Robot sends a request message to storage B. | AND | Storage B | 1 | Same reasoning as AT2. |
| **AT6: Wait for Retrieval** | Robot waits until the resource is retrieved. | AND | Storage B | 1 | Same reasoning as AT3. |
| **AT7: Return to Recharging Station** | Robot returns to the recharging station due to low battery. | AND | Recharging Station | 1 | The robot must physically return to recharge. |
| **AT8: Assign Mission to Another Robot** | Robot assigns the remaining task to another robot. | AND | Recharging Station (or current location) | 1 | The robot must communicate the task to a spare robot. |
| **AT9: Make Runs to Destination** | Robot makes the necessary runs to deliver the resource to the destination. | AND | Destination | 1 | Movement to the destination is a core delivery action. |
| **AT10: Hand Over Resource** | Robot hands over the resource to the requesting agent. | AND | Destination | 1 | The hand‑over is the final delivery step. |
| **AT11: Make Runs to Destination (Item 2)** | Robot makes the necessary runs to deliver the second resource. | AND | Destination | 1 | Same as AT9. |
| **AT12: Hand Over Resource (Item 2)** | Robot hands over the second resource to the requesting agent. | AND | Destination | 1 | Same as AT10. |
| **AT13: Return Resource to Checkpoint** | Robot returns the resource to a checkpoint due to low battery. | AND | Checkpoint | 1 | The robot must bring the item to a safe spot. |
| **AT14: Assign Remaining Task to Another Robot** | Robot assigns the remaining delivery task to another robot after returning the item. | AND | Checkpoint | 1 | The robot must inform a spare robot of the new task. |
| **AT15: Trigger Alert & Send Report** | If the robot fails to return the resource to the checkpoint, trigger an alert and send a report to the sector manager. | AND | Checkpoint | 1 | The robot must notify the manager upon failure. |

---

## 3. Summary Table – Goals & Tasks  

| **ID** | **Title** | **Type** | **Key Attribute** |
|--------|-----------|----------|-------------------|
| **G1** | Deliver Requested Resources | Achieve | Resources delivered & agent satisfied |
| **G2** | Perform Collection | Perform | Parallel collection of items |
| **G2.1** | Collect from Storage A | Perform | Sequential go → request → wait |
| **G2.2** | Collect from Storage B | Perform | Sequential go → request → wait |
| **G2.3** | Battery Low Handling (Collection) | Perform | Return → assign |
| **G3** | Perform Delivery | Perform | Parallel delivery of items |
| **G3.1** | Deliver Item 1 | Perform | Sequential run → handover |
| **G3.2** | Deliver Item 2 | Perform | Sequential run → handover |
| **G3.3** | Battery Low Handling (Delivery) | Perform | Return → assign → alert |
| **AT1** | Go to Storage A | Task | 1 robot |
| **AT2** | Request Resource | Task | 1 robot |
| **AT3** | Wait for Retrieval | Task | 1 robot |
| **AT4** | Go to Storage B | Task | 1 robot |
| **AT5** | Request Resource | Task | 1 robot |
| **AT6** | Wait for Retrieval | Task | 1 robot |
| **AT7** | Return to Recharging Station | Task | 1 robot |
| **AT8** | Assign Mission to Another Robot | Task | 1 robot |
| **AT9** | Make Runs to Destination | Task | 1 robot |
| **AT10** | Hand Over Resource | Task | 1 robot |
| **AT11** | Make Runs to Destination (Item 2) | Task | 1 robot |
| **AT12** | Hand Over Resource (Item 2) | Task | 1 robot |
| **AT13** | Return Resource to Checkpoint | Task | 1 robot |
| **AT14** | Assign Remaining Task to Another Robot | Task | 1 robot |
| **AT15** | Trigger Alert & Send Report | Task | 1 robot |

---

## 4. Logical Relationships  

| **Parent** | **Children** | **Relation** | **Runtime** | **Justification** |
|------------|--------------|--------------|-------------|-------------------|
| **G1** | G2, G3 | AND | `;` (sequential) | Collection must finish before delivery; both phases are required for mission success. |
| **G2** | G2.1, G2.2, G2.3 | AND | `#` (parallel) | Multiple collection tasks can run concurrently; battery‑low handling is part of the collection phase. |
| **G2.1** | AT1, AT2, AT3 | AND | `;` (sequential) | The robot must first go to storage, request, then wait. |
| **G2.2** | AT4, AT5, AT6 | AND | `;` (sequential) | Same sequence as G2.1. |
| **G2.3** | AT7, AT8 | AND | `;` (sequential) | Low battery triggers return to recharge, then handover. |
| **G3** | G3.1, G3.2, G3.3 | AND | `#` (parallel) | Multiple deliveries can be carried out in parallel; battery‑low handling is part of the delivery phase. |
| **G3.1** | AT9, AT10 | AND | `;` (sequential) | Run to destination, then hand over. |
| **G3.2** | AT11, AT12 | AND | `;` (sequential) | Same sequence as G3.1. |
| **G3.3** | AT13, AT14, AT15 | AND | `;` (sequential) | Return to checkpoint, handover, and alert if return fails. |

---

### Rationale for Decompositions & Runtime Annotations  

* **Sequential (`;`)** is used whenever a strict order of actions is required (e.g., moving, requesting, waiting).  
* **Parallel (`#`)** is used when multiple robots can perform independent sub‑tasks simultaneously (e.g., collecting from different storages or delivering different items).  
* **Fallback** was not used because the mission does not present alternative plans; instead, battery‑low handling is a deterministic sequence of actions triggered by a condition.  

All relations between goals and tasks are **AND** because every child must be satisfied for the parent goal to be considered achieved. The model captures the mission’s requirement for parallelism, battery management, and failure handling while keeping the structure clear and traceable.
