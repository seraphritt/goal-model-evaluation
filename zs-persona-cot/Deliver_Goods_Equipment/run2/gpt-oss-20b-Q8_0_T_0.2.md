**Goal Model – Multi‑Robot Resource Delivery Mission**

| **Name**                                             | **Text**                                                                                        | **Runtime**                | **Goal Type** | **Target Condition / Enquired Information**                                          | **Relation** | **Justification**                                                                                              | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------- | ------------- | ------------------------------------------------------------------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1: Deliver Resources**                            | Deliver requested resources to the specified location.                                          | `;`                        | Achieve       | *Resources are delivered to the destination and the requesting agent receives them.* | AND          | The mission ends only after resources are collected **and** delivered; the two phases must occur sequentially. | Perform.                                                 | OK                 | Perform.                                                 |
| **G2: Collect Resources**                            | Collect required resources from storage.                                                        | `;`                        | Perform       | –                                                                                    | AND          | Collection is a linear chain of actions (go to storage, request, wait).                                        | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G2.1: Navigate to Storage**                        | Navigate to the storage location where the resource is located.                                 | `-`                        | Perform       | –                                                                                    | AND          | The robot must physically reach the storage before any request can be made.                                    | OK                                                       | OK                 | OK                                                       |
| **G2.2: Request Resource**                           | Send a request message to the storage with the precise specification of the required resources. | `-`                        | Perform       | –                                                                                    | AND          | The storage can only hand over the resource after receiving a request.                                         | Query. enquired information: resources to be collected.  | OK                 | Query. enquired information: resources to be collected.  |
| **G2.3: Wait for Retrieval**                         | Wait until the storage confirms that the resource has been retrieved.                           | `-`                        | Perform       | –                                                                                    | AND          | The robot cannot proceed to delivery until the resource is secured.                                            | OK                                                       | OK                 | OK                                                       |
| **G2.4: Monitor Battery (Collection)**               | Monitor battery level during collection; act accordingly.                                       | `FALLBACK(G2.4.1, G2.4.2)` | Perform       | –                                                                                    | OR           | The robot may either continue collecting if the battery is sufficient or must handle a low-battery situation.  | OK                                                       | OK                 | OK                                                       |
| **G2.4.1: Continue Collection**                      | Continue the collection routine.                                                                | `-`                        | Perform       | –                                                                                    | AND          | No battery issue – normal flow.                                                                                | OK                                                       | OK                 | OK                                                       |
| **G2.4.2: Handle Low Battery (Collection)**          | Handle a low-battery event during collection.                                                   | `;`                        | Perform       | –                                                                                    | AND          | Low battery requires two sequential actions: recharge and hand-over the mission.                               | OK                                                       | OK                 | OK                                                       |
| **G2.4.2.1: Return to Recharging Station**           | Return to the recharging station to replenish battery.                                          | `-`                        | Perform       | –                                                                                    | AND          | Recharge must finish before the robot can re-engage.                                                           | OK                                                       | OK                 | OK                                                       |
| **G2.4.2.2: Assign Mission to Another Robot**        | Assign the remaining collection task to another robot.                                          | `-`                        | Perform       | –                                                                                    | AND          | The new robot must know the storage location and remaining items.                                              | OK                                                       | OK                 | OK                                                       |
| **G3: Deliver Resources**                            | Deliver the collected resources to the destination.                                             | `;`                        | Perform       | –                                                                                    | AND          | Delivery is the second sequential phase of the mission.                                                        | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G3.1: Navigate to Destination**                    | Navigate to the destination location where the resource is needed.                              | `-`                        | Perform       | –                                                                                    | AND          | The robot must reach the destination before dropping off the resource.                                         | OK                                                       | OK                 | OK                                                       |
| **G3.2: Deliver Resource**                           | Drop off the resource at the destination.                                                       | `-`                        | Perform       | –                                                                                    | AND          | The resource is considered delivered only after this action.                                                   | OK                                                       | OK                 | OK                                                       |
| **G3.3: Monitor Battery (Delivery)**                 | Monitor battery level during delivery; act accordingly.                                         | `FALLBACK(G3.3.1, G3.3.2)` | Perform       | –                                                                                    | OR           | Normal delivery continues if battery is OK; otherwise a low-battery protocol is triggered.                     | OK                                                       | OK                 | OK                                                       |
| **G3.3.1: Continue Delivery**                        | Continue the delivery routine.                                                                  | `-`                        | Perform       | –                                                                                    | AND          | No battery issue – normal flow.                                                                                | OK                                                       | OK                 | OK                                                       |
| **G3.3.2: Handle Low Battery (Delivery)**            | Handle a low-battery event during delivery.                                                     | `;`                        | Perform       | –                                                                                    | AND          | The robot must return the resource to a checkpoint and hand-over the remaining task.                           | OK                                                       | OK                 | OK                                                       |
| **G3.3.2.1: Return Resource to Checkpoint**          | Return the resource to a safe checkpoint before re-engaging.                                    | `-`                        | Perform       | –                                                                                    | AND          | Prevents loss of goods if the robot cannot finish the delivery.                                                | OK                                                       | OK                 | OK                                                       |
| **G3.3.2.2: Assign Remaining Task to Another Robot** | Assign the rest of the delivery task to another robot.                                          | `-`                        | Perform       | –                                                                                    | AND          | The new robot must know the checkpoint and the destination.                                                    | OK                                                       | OK                 | OK                                                       |
| **G3.3.2.3: Failure Handling**                       | Handle a failure to return the resource to the checkpoint.                                      | `#`                        | Perform       | –                                                                                    | AND          | If the resource cannot be returned, alerting and reporting must happen concurrently.                           | OK                                                       | OK                 | OK                                                       |
| **G3.3.2.3.1: Send Alert**                           | Send an alert to the sector manager.                                                            | `-`                        | Perform       | –                                                                                    | AND          | Immediate notification is required to trigger human intervention.                                              | OK                                                       | OK                 | OK                                                       |
| **G3.3.2.3.2: Send Report**                          | Send a detailed report to the sector manager.                                                   | `-`                        | Perform       | –                                                                                    | AND          | A log of the failure must be sent for audit and recovery.                                                      | OK                                                       | OK                 | OK                                                       |
| **G7: Parallel Assignment Optimization**             | Optimize the mission by assigning parallel collect-deliver tasks to multiple robots.            | `#`                        | Perform       | –                                                                                    | AND          | Parallel execution reduces overall mission time; the two sub-goals can proceed concurrently.                   | OK                                                       | OK                 | OK                                                       |
| **G7.1: Assign Parallel Tasks**                      | Assign parallel collect-deliver tasks to additional robots.                                     | `-`                        | Perform       | –                                                                                    | AND          | Enables simultaneous execution of independent collection/delivery sequences.                                   | OK                                                       | OK                 | OK                                                       |
| **G7.2: Monitor Overall Progress**                   | Monitor the overall mission progress and coordination between robots.                           | `-`                        | Perform       | –                                                                                    | AND          | Ensures that all parallel tasks stay on schedule and resources are not duplicated.                             | OK                                                       | OK                 | OK                                                       |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1: Navigate to Storage** | The robot moves from its current location to the specified storage. | AND | *Storage* | 1 | Only the assigned robot can navigate to the storage. |
| **AT2: Request Resource** | The robot sends a request message to the storage with the resource specification. | AND | *Storage* | 1 | Communication occurs at the storage location. |
| **AT3: Wait for Retrieval** | The robot waits until the storage confirms the resource has been retrieved. | AND | *Storage* | 1 | No other robot is required while waiting. |
| **AT4: Navigate to Destination** | The robot moves from the storage to the destination where the resource is needed. | AND | *Destination* | 1 | The robot must physically travel to the destination. |
| **AT5: Deliver Resource** | The robot drops off the resource at the destination. | AND | *Destination* | 1 | Delivery is performed by the robot that holds the resource. |
| **AT6: Monitor Battery Level** | The robot continuously checks its battery level. | AND | *Self* | 1 | Battery monitoring is a continuous internal task. |
| **AT7: Return to Recharging Station** | The robot returns to the recharging station to recharge. | AND | *Recharging Station* | 1 | Only the robot with low battery can perform this. |
| **AT8: Assign Mission to Another Robot** | The robot informs another robot to take over the remaining task. | AND | *Current Location* | 1 | Communication is required between robots. |
| **AT9: Return Resource to Checkpoint** | The robot returns the resource to a safe checkpoint. | AND | *Checkpoint* | 1 | The resource must be secured before handing over. |
| **AT10: Send Alert** | The robot sends an alert to the sector manager. | AND | *Sector Manager* | 1 | Human‑operator notification is mandatory. |
| **AT11: Send Report** | The robot sends a detailed report to the sector manager. | AND | *Sector Manager* | 1 | Audit and recovery information must be transmitted. |
| **AT12: Assign Parallel Tasks** | The system assigns parallel collect‑deliver tasks to additional robots. | AND | *Central Control* | 1 | Coordination of multiple robots is handled by a central controller. |
| **AT13: Monitor Overall Progress** | The system monitors the progress of all parallel tasks. | AND | *Central Control* | 1 | Continuous monitoring ensures no deadlocks or resource conflicts. |

---

### Summary Table (Goals & Tasks)

| **ID** | **Title** |
|--------|-----------|
| **G1** | Deliver Resources |
| **G2** | Collect Resources |
| **G2.1** | Navigate to Storage |
| **G2.2** | Request Resource |
| **G2.3** | Wait for Retrieval |
| **G2.4** | Monitor Battery (Collection) |
| **G2.4.1** | Continue Collection |
| **G2.4.2** | Handle Low Battery (Collection) |
| **G2.4.2.1** | Return to Recharging Station |
| **G2.4.2.2** | Assign Mission to Another Robot |
| **G3** | Deliver Resources |
| **G3.1** | Navigate to Destination |
| **G3.2** | Deliver Resource |
| **G3.3** | Monitor Battery (Delivery) |
| **G3.3.1** | Continue Delivery |
| **G3.3.2** | Handle Low Battery (Delivery) |
| **G3.3.2.1** | Return Resource to Checkpoint |
| **G3.3.2.2** | Assign Remaining Task to Another Robot |
| **G3.3.2.3** | Failure Handling |
| **G3.3.2.3.1** | Send Alert |
| **G3.3.2.3.2** | Send Report |
| **G7** | Parallel Assignment Optimization |
| **G7.1** | Assign Parallel Tasks |
| **G7.2** | Monitor Overall Progress |
| **AT1** | Navigate to Storage |
| **AT2** | Request Resource |
| **AT3** | Wait for Retrieval |
| **AT4** | Navigate to Destination |
| **AT5** | Deliver Resource |
| **AT6** | Monitor Battery Level |
| **AT7** | Return to Recharging Station |
| **AT8** | Assign Mission to Another Robot |
| **AT9** | Return Resource to Checkpoint |
| **AT10** | Send Alert |
| **AT11** | Send Report |
| **AT12** | Assign Parallel Tasks |
| **AT13** | Monitor Overall Progress |

---

### Logical Relationships

| **Parent → Children** | **Relation** | **Runtime Annotation** | **Justification** |
|------------------------|--------------|------------------------|-------------------|
| **G1 → G2, G3, G7** | AND | `;` | Collection, delivery, and optional parallel optimization must all be satisfied before the mission succeeds; they are sequential in the overall flow. |
| **G2 → G2.1, G2.2, G2.3, G2.4** | AND | `;` | The collection phase is a linear sequence of actions. |
| **G2.4 → G2.4.1, G2.4.2** | OR | `FALLBACK(G2.4.1, G2.4.2)` | If battery is OK, continue; otherwise, handle low battery. |
| **G2.4.2 → G2.4.2.1, G2.4.2.2** | AND | `;` | The robot must recharge **and** hand over the task. |
| **G3 → G3.1, G3.2, G3.3** | AND | `;` | The delivery phase is a linear sequence. |
| **G3.3 → G3.3.1, G3.3.2** | OR | `FALLBACK(G3.3.1, G3.3.2)` | Normal delivery continues if battery is OK; otherwise, low‑battery protocol. |
| **G3.3.2 → G3.3.2.1, G3.3.2.2, G3.3.2.3** | AND | `;` | The robot must return the resource, assign the task, and handle failures. |
| **G3.3.2.3 → G3.3.2.3.1, G3.3.2.3.2** | AND | `#` | Alert and report are sent concurrently after a failure. |
| **G7 → G7.1, G7.2** | AND | `#` | Parallel assignment and monitoring can run concurrently. |
| **G2.1 → AT1** | AND | `-` | Navigation is a single concrete action. |
| **G2.2 → AT2** | AND | `-` | Requesting is a single concrete action. |
| **G2.3 → AT3** | AND | `-` | Waiting is a single concrete action. |
| **G2.4.1 → AT6** | AND | `-` | Battery monitoring continues. |
| **G2.4.2.1 → AT7** | AND | `-` | Recharge action. |
| **G2.4.2.2 → AT8** | AND | `-` | Mission hand‑over action. |
| **G3.1 → AT4** | AND | `-` | Navigation to destination. |
| **G3.2 → AT5** | AND | `-` | Delivery action. |
| **G3.3.1 → AT6** | AND | `-` | Battery monitoring continues. |
| **G3.3.2.1 → AT9** | AND | `-` | Return to checkpoint. |
| **G3.3.2.2 → AT8** | AND | `-` | Hand‑over remaining delivery. |
| **G3.3.2.3.1 → AT10** | AND | `-` | Alert action. |
| **G3.3.2.3.2 → AT11** | AND | `-` | Report action. |
| **G7.1 → AT12** | AND | `-` | Assign parallel tasks. |
| **G7.2 → AT13** | AND | `-` | Monitor progress. |

---

**Explanation of Design Choices**

1. **Sequential vs. Parallel** – The top‑level mission consists of a *collection* phase followed by a *delivery* phase; thus the root goal uses a sequential runtime (`;`). Within each phase, actions must occur in a fixed order, so child goals also use `;`. Parallelism is only introduced where the description explicitly allows it: assigning multiple robots to parallel collect‑deliver tasks (G7) and when the system must send an alert **and** a report concurrently (G3.3.2.3).  
2. **Fallback for Battery Management** – The mission specifies different battery thresholds for collection (10 %) and delivery (30 %). When a low‑battery situation is detected, the robot must *fallback* to a different behavior (recharge or return to checkpoint). This is captured by `FALLBACK(...)` at the battery‑monitoring goals.  
3. **Goal Types** – All high‑level operational objectives (collect, deliver, parallel assignment) are *Perform* goals because they are satisfied by executing a plan. The root *Deliver Resources* is an *Achieve* goal because it specifies a future world state (resource delivered). No *Query* goals are needed because the mission does not require passive information gathering.  
4. **Task Mapping** – Each leaf goal corresponds to a single concrete action (task). The location is chosen based on where the action logically occurs (e.g., navigation tasks at the target location, communication tasks at the storage or sector manager). The number of robots is set to 1 for actions that require a single robot; parallel goals (e.g., G7) involve multiple robots but each sub‑task is still performed by one robot at a time.  

This goal model gives a clear, hierarchical decomposition of the mission, explicitly captures the temporal and fallback constraints, and links every goal to concrete, executable tasks.
