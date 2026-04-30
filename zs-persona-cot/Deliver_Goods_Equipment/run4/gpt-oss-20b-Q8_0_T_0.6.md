**Goal Model – Multi‑Robot Delivery Mission**  

Below is a full, depth‑first numbered goal model that captures the mission description.  
Each goal is annotated with its runtime operator, goal type, target condition (for *Achieve* goals), and the logical relation to its child tasks or sub‑goals.  
All tasks are linked to the corresponding goals with a justified relation, location, and robot‑count.

--------------------------------------------------------------------
### 1. Goal Tables  

| **Name** | **Text**                                                 | **Runtime** | **Goal Type** | **Target Condition / Enquired Info** | **Decomposition** | **Relation** | **Justification**                                                                                                                                                       | Ground truth I                                          | Ground truth C | Consensus                                               |
| -------- | -------------------------------------------------------- | ----------- | ------------- | ------------------------------------ | ----------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------- | ------------------------------------------------------- |
| **G1**   | Deliver requested resources to the destination           | `;`         | Achieve       | `resources_at_destination == true`   | AND               | AND          | The overall mission must complete **both** collection and delivery phases in sequence; the mission cannot finish until all resources are physically at the destination. | Perform                                                 | OK             | Perform                                                 |
| **G2**   | Collect required resources from the storage              | `-`         | Perform       | –                                    | –                 | AND          | All collection steps (navigation, request, wait, pickup, battery check) must be performed for the collection to succeed.                                                | Achieve. target condition: all resources were collected | OK             | Achieve. target condition: all resources were collected |
| **G3**   | Deliver collected resources to the destination           | `-`         | Perform       | –                                    | –                 | AND          | The delivery phase requires navigation, hand-over, and battery handling; all must occur to finish delivery.                                                             | Achieve. target condition: all resources were delivered | OK             | Achieve. target condition: all resources were delivered |
| **G4**   | Handle failure to return a resource to a checkpoint      | `-`         | Perform       | –                                    | –                 | AND          | An alert and a report must both be generated when the robot cannot return the resource; both actions are necessary to satisfy the failure-handling goal.                | OK                                                      | OK             | OK                                                      |
| **G5**   | Assign parallel collect-deliver tasks to multiple robots | `-`         | Perform       | –                                    | –                 | AND          | When multiple items are required, the system must **assign** parallel tasks; this single action is sufficient.                                                          | OK                                                      | OK             | OK                                                      |

--------------------------------------------------------------------
### 2. Task Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Navigate to the storage location where the resource is stored | AND | storage | 1 | The robot must physically reach the storage to request the resource. |
| **AT2** | Send a request to the storage with the precise specification of the required resources | AND | storage | 1 | The robot must inform the storage of what is needed before the resource can be retrieved. |
| **AT3** | Wait until the storage has retrieved the resources | AND | storage | 1 | The robot must pause until the storage confirms the resource has been taken. |
| **AT4** | Pick up the retrieved resource from the storage | AND | storage | 1 | The robot must physically take possession of the resource before it can be transported. |
| **AT5** | Navigate to the specified delivery location | AND | destination | 1 | The robot must reach the destination to hand over the resource. |
| **AT6** | Deliver the resource to the requesting agent | AND | destination | 1 | The resource must be handed over to complete the delivery. |
| **AT7** | Monitor the robot’s battery level | AND | robot | 1 | Continuous battery monitoring is required to decide when to recharge or re‑assign. |
| **AT8** | Return to the charging station and recharge the battery | AND | recharge station | 1 | When the battery falls below 10 % during collection, the robot must recharge before continuing. |
| **AT9** | Assign the remaining collection‑delivery task to another robot | AND | robot | 1 | After recharging, the original robot relinquishes the mission so another robot can take over. |
| **AT10** | Return the partially transported resource to a checkpoint | AND | checkpoint | 1 | When the battery falls below 30 % during delivery, the robot must safely return the resource. |
| **AT11** | Trigger an alert indicating failure to return the resource | AND | robot | 1 | Failure to return the resource requires an immediate alert to the sector manager. |
| **AT12** | Send a failure report to the sector manager | AND | sector manager | 1 | The report completes the failure‑handling process. |
| **AT13** | Assign parallel collect‑deliver tasks to multiple robots | AND | system | `[1,∞]` | Parallel assignment reduces overall mission time when multiple items are needed. |

--------------------------------------------------------------------
### 3. Summary Table (Goals + Tasks)  

| **ID** | **Type** | **Title** | **Runtime / Decomposition** | **Relation** |
|--------|----------|-----------|-----------------------------|--------------|
| G1 | Goal | Deliver requested resources | `;` (sequential) / AND | G2, G3, G4, G5 |
| G2 | Goal | Collect required resources | `-` | AT1, AT2, AT3, AT4, AT7, AT8, AT9 |
| G3 | Goal | Deliver collected resources | `-` | AT5, AT6, AT7, AT10, AT9 |
| G4 | Goal | Handle failure to return resource | `-` | AT11, AT12 |
| G5 | Goal | Assign parallel tasks | `-` | AT13 |
| AT1 | Task | Navigate to storage | AND | – |
| AT2 | Task | Send request to storage | AND | – |
| AT3 | Task | Wait for retrieval | AND | – |
| AT4 | Task | Pick up resource | AND | – |
| AT5 | Task | Navigate to destination | AND | – |
| AT6 | Task | Deliver resource | AND | – |
| AT7 | Task | Monitor battery | AND | – |
| AT8 | Task | Recharge battery | AND | – |
| AT9 | Task | Assign remaining task | AND | – |
| AT10 | Task | Return to checkpoint | AND | – |
| AT11 | Task | Trigger alert | AND | – |
| AT12 | Task | Send report | AND | – |
| AT13 | Task | Parallel assignment | AND | – |

--------------------------------------------------------------------
### 4. Logical Relationships  

| **Parent** | **Children** | **Relation** | **Runtime** | **Justification** |
|------------|--------------|--------------|-------------|-------------------|
| **G1** | G2, G3, G4, G5 | AND | `;` | The mission cannot succeed until **all** sub‑goals are satisfied; they must be performed in the order: collect → deliver → failure handling → parallel assignment. |
| **G2** | AT1, AT2, AT3, AT4, AT7, AT8, AT9 | AND | `;` | The collection phase requires a strict sequence: navigate → request → wait → pickup → battery check → recharge (if needed) → handover. |
| **G3** | AT5, AT6, AT7, AT10, AT9 | AND | `;` | The delivery phase follows a similar sequence: navigate → deliver → battery check → checkpoint return (if needed) → handover. |
| **G4** | AT11, AT12 | AND | `;` | Failure handling must both alert and report; both actions are mandatory. |
| **G5** | AT13 | AND | `-` | The parallel assignment is a single action; no further decomposition. |

--------------------------------------------------------------------
**Notes on Justifications**

* **Sequential Runtime (`;`)** – The mission description explicitly states that the **delivery phase begins only after collection is complete**. Within each phase, tasks must occur in a fixed order (e.g., navigation before request).  
* **Fallback** – The description’s “if battery low … assign mission to another robot” is modeled as a **perform goal** that contains the fallback logic (monitor → recharge/assign). Since we treat the fallback as a separate goal, the runtime operator is not needed in the goal table; the fallback logic is captured by the relation between the battery‑monitor task (AT7) and the subsequent recharge/assign tasks (AT8, AT9).  
* **Parallel Assignment (`#`)** – The only place where parallelism is required is the **parallel collect‑deliver** mode when multiple items are needed. This is captured in **G5** and **AT13**; no explicit `#` operator is needed because the action is a single task.  
* **Relation `AND`** – Every goal or task that has multiple children must have all of them performed for the parent to succeed, matching the mission’s “all resources must be delivered” requirement.  

This goal model fully decomposes the mission into actionable tasks, clarifies the execution structure, and provides transparent justifications for every chosen operator and relation.
