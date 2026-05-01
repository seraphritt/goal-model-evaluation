## 1. Goal Model – Tables

| **Name**                                                    | **Text**                                                                             | **Runtime** | **Goal Type** | **Target Condition / Enquired Info**                           | **Relation** | **Justification**                                                                                                               | **Ground truth I** | **Ground truth C** | **Consensus**                                            |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------- | ------------- | -------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------ | -------------------------------------------------------- |
| **G1**: Deliver Requested Resources to Requesting Agent     | Achieve delivery of all requested resources to the specified location.               | `;`         | Achieve       | *All requested resources delivered to the specified location.* | – (root)     | The mission’s ultimate objective is to deliver resources; collection must finish before delivery, hence a sequential structure. |                    | Ok                 | Perform.                                                 |
| **G2**: Collection Phase                                    | Perform collection of resources from storage.                                        | `#`         | Perform       | –                                                              | AND          | Collection must be completed before delivery; multiple robots can collect from different storages concurrently.                 |                    | Ok                 | Achieve. Target condition: all resources were collected. |
| **G3**: Delivery Phase                                      | Perform delivery of collected resources to the requesting agent.                     | `#`         | Perform       | –                                                              | AND          | Delivery follows collection; multiple robots can deliver concurrently.                                                          |                    | Ok                 | Achieve. Target condition: all resources were delivered. |
| **G2.1**: Plan Collection Order                             | Estimate waiting time and path to determine the order of storages.                   | `-`         | Perform       | –                                                              | AND          | Planning is a prerequisite for any collection action.                                                                           |                    | Ok                 | OK                                                       |
| **G2.2**: Request Resources                                 | Send a message to storage with the precise specification of the requested resources. | `-`         | Perform       | –                                                              | AND          | The robot must request resources before they can be retrieved.                                                                  |                    | Ok                 | Query. Enqueried information: resources to be collected  |
| **G2.3**: Wait for Retrieval                                | Wait until the resources have been retrieved from the storage.                       | `-`         | Perform       | –                                                              | AND          | The robot must wait for the storage to hand over the items.                                                                     |                    | Ok                 | Ok                                                       |
| **G2.4**: Battery Low in Collection                         | Detect battery level below 10 % during collection.                                   | `-`         | Perform       | –                                                              | AND          | Battery threshold triggers recharging and reassignment.                                                                         |                    | Ok                 | OK                                                       |
| **G2.5**: Reassign Mission                                  | Assign the remaining collection task to another robot.                               | `-`         | Perform       | –                                                              | AND          | After recharging, the mission must continue with another robot.                                                                 |                    | Ok                 | OK                                                       |
| **G2.6**: Parallel Collection Assignment                    | Assign multiple robots to parallel collect tasks.                                    | `-`         | Perform       | –                                                              | AND          | Parallelization reduces overall mission time.                                                                                   |                    | Ok                 | OK                                                       |
| **G3.1**: Navigate to Delivery Location                     | Move the robot to the specified delivery location.                                   | `-`         | Perform       | –                                                              | AND          | The robot must reach the delivery point before handing over items.                                                              |                    | Ok                 | OK                                                       |
| **G3.2**: Return Resource to Checkpoint                     | Return the resource to a checkpoint if battery < 30 % during delivery.               | `-`         | Perform       | –                                                              | AND          | Safety measure that allows another robot to pick up the resource.                                                               |                    | Ok                 | OK                                                       |
| **G3.3**: Deliver Resources                                 | Deliver the resources to the requesting agent.                                       | `-`         | Perform       | –                                                              | AND          | Final step of the delivery phase.                                                                                               |                    | Ok                 | Achieve. Target condition: all resources were delivered  |
| **G3.4**: Battery Low in Delivery                           | Detect battery level below 30 % during delivery.                                     | `-`         | Perform       | –                                                              | AND          | Battery threshold triggers checkpoint return and reassignment.                                                                  |                    | Ok                 | OK                                                       |
| **G3.5**: Reassign Mission                                  | Assign the remaining delivery task to another robot.                                 | `-`         | Perform       | –                                                              | AND          | After checkpoint return, another robot must finish the delivery.                                                                |                    | Ok                 | OK                                                       |
| **G3.6**: Parallel Delivery Assignment                      | Assign multiple robots to parallel delivery tasks.                                   | `-`         | Perform       | –                                                              | AND          | Parallelization reduces overall mission time.                                                                                   |                    | Ok                 | OK                                                       |
| **G5**: Failure Handling                                    | Handle failures such as failure to return a resource to a checkpoint.                | `#`         | Perform       | –                                                              | AND          | Failure handling can occur concurrently with other phases.                                                                      |                    | Ok                 | OK                                                       |
| **G5.1**: Alert on Failure to Return Resource to Checkpoint | Trigger an alert if the resource cannot be returned to the checkpoint.               | `-`         | Perform       | –                                                              | AND          | Immediate notification is required for safety.                                                                                  |                    | Ok                 | Ok                                                       |
| **G5.2**: Report to Sector Manager                          | Send a report to the sector manager after an alert.                                  | `-`         | Perform       | –                                                              | AND          | Reporting is mandatory after an alert.                                                                                          |                    | Ok                 | OK                                                       |

---

## 2. Task Model – Tables

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1**: Estimate Waiting Time and Path | Compute waiting time and path to each storage to plan the order of visits. | AND | *Robot (planning)* | 1 | Planning is performed by a single robot before any collection. |
| **AT2**: Send Resource Request Message | Send a message to the storage with the precise specification of the requested resources. | AND | *Storage* | 1 | The robot must communicate with the storage to request items. |
| **AT3**: Wait for Resource Retrieval | Wait until the storage retrieves the resources. | AND | *Storage* | 1 | The robot must wait for the storage to hand over the items. |
| **AT4**: Check Battery Level (Collection) | Monitor battery level during collection. | AND | *Robot* | 1 | Battery monitoring is essential to trigger recharging. |
| **AT5**: Return to Recharging Station | Return the robot to the recharging station when battery < 10 %. | AND | *Recharging station* | 1 | Recharge is required before the robot can continue. |
| **AT6**: Assign Mission to Another Robot | Assign the remaining collection or delivery task to another robot. | AND | *Robot* | 1 | Reassignment ensures continuity after recharging or checkpoint return. |
| **AT7**: Navigate to Delivery Location | Move the robot to the delivery location. | AND | *Delivery location* | 1 | The robot must reach the delivery point before handing over items. |
| **AT8**: Return Resource to Checkpoint | Return the resource to a checkpoint when battery < 30 % during delivery. | AND | *Checkpoint* | 1 | Safety measure that allows another robot to pick up the resource. |
| **AT9**: Deliver Resources | Deliver the resources to the requesting agent. | AND | *Delivery location* | 1 | Final hand‑over of items. |
| **AT10**: Trigger Alert | Trigger an alert if the resource cannot be returned to the checkpoint. | AND | *Robot* | 1 | Immediate notification is required for safety. |
| **AT11**: Send Report to Sector Manager | Send a report to the sector manager after an alert. | AND | *Robot* | 1 | Reporting is mandatory after an alert. |
| **AT12**: Assign Parallel Collection Tasks | Assign multiple robots to parallel collect tasks. | AND | *Robot* | [1,n] | Parallelization reduces overall mission time. |
| **AT13**: Assign Parallel Delivery Tasks | Assign multiple robots to parallel delivery tasks. | AND | *Robot* | [1,n] | Parallelization reduces overall mission time. |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Type** | **Text** | **Runtime / Relation** | **Justification** |
|--------|----------|----------|------------------------|-------------------|
| G1 | Goal (Achieve) | Deliver requested resources to requesting agent | `;` (sequential) | Collection must finish before delivery. |
| G2 | Goal (Perform) | Collection Phase | `#` (parallel) | Multiple robots can collect concurrently. |
| G3 | Goal (Perform) | Delivery Phase | `#` (parallel) | Multiple robots can deliver concurrently. |
| G2.1 | Goal (Perform) | Plan Collection Order | `-` | Planning prerequisite. |
| G2.2 | Goal (Perform) | Request Resources | `-` | Must request before retrieval. |
| G2.3 | Goal (Perform) | Wait for Retrieval | `-` | Must wait for storage. |
| G2.4 | Goal (Perform) | Battery Low in Collection | `-` | Battery threshold triggers recharging. |
| G2.5 | Goal (Perform) | Reassign Mission | `-` | Continue mission after recharge. |
| G2.6 | Goal (Perform) | Parallel Collection Assignment | `-` | Parallelization. |
| G3.1 | Goal (Perform) | Navigate to Delivery Location | `-` | Must reach delivery point. |
| G3.2 | Goal (Perform) | Return Resource to Checkpoint | `-` | Safety measure. |
| G3.3 | Goal (Perform) | Deliver Resources | `-` | Final delivery. |
| G3.4 | Goal (Perform) | Battery Low in Delivery | `-` | Battery threshold triggers checkpoint. |
| G3.5 | Goal (Perform) | Reassign Mission | `-` | Continue mission after checkpoint. |
| G3.6 | Goal (Perform) | Parallel Delivery Assignment | `-` | Parallelization. |
| G5 | Goal (Perform) | Failure Handling | `#` | Failure handling can run concurrently. |
| G5.1 | Goal (Perform) | Alert on Failure to Return Resource to Checkpoint | `-` | Immediate notification. |
| G5.2 | Goal (Perform) | Report to Sector Manager | `-` | Mandatory reporting. |
| AT1 | Task | Estimate Waiting Time and Path | AND | Planning. |
| AT2 | Task | Send Resource Request Message | AND | Request. |
| AT3 | Task | Wait for Resource Retrieval | AND | Wait. |
| AT4 | Task | Check Battery Level (Collection) | AND | Battery monitoring. |
| AT5 | Task | Return to Recharging Station | AND | Recharge. |
| AT6 | Task | Assign Mission to Another Robot | AND | Reassignment. |
| AT7 | Task | Navigate to Delivery Location | AND | Navigation. |
| AT8 | Task | Return Resource to Checkpoint | AND | Safety. |
| AT9 | Task | Deliver Resources | AND | Delivery. |
| AT10 | Task | Trigger Alert | AND | Alert. |
| AT11 | Task | Send Report to Sector Manager | AND | Reporting. |
| AT12 | Task | Assign Parallel Collection Tasks | AND | Parallelization. |
| AT13 | Task | Assign Parallel Delivery Tasks | AND | Parallelization. |

---

## 4. Logical Relationships

| **Parent** | **Children** | **Relation** | **Runtime** | **Justification** |
|------------|--------------|--------------|-------------|-------------------|
| **G1** | G2, G3 | AND | `;` | Collection must finish before delivery. |
| **G2** | G2.1, G2.2, G2.3, G2.4, G2.5, G2.6 | AND | `#` | Collection tasks can run in parallel across multiple robots. |
| **G3** | G3.1, G3.2, G3.3, G3.4, G3.5, G3.6 | AND | `#` | Delivery tasks can run in parallel across multiple robots. |
| **G5** | G5.1, G5.2 | AND | `#` | Failure handling can occur concurrently with other phases. |
| **G2.1** | AT1 | AND | `-` | Planning is a single action. |
| **G2.2** | AT2 | AND | `-` | Requesting resources is a single action. |
| **G2.3** | AT3 | AND | `-` | Waiting is a single action. |
| **G2.4** | AT4 | AND | `-` | Battery monitoring is a single action. |
| **G2.5** | AT6 | AND | `-` | Reassignment is a single action. |
| **G2.6** | AT12 | AND | `-` | Parallel assignment is a single action. |
| **G3.1** | AT7 | AND | `-` | Navigation is a single action. |
| **G3.2** | AT8 | AND | `-` | Return to checkpoint is a single action. |
| **G3.3** | AT9 | AND | `-` | Delivery is a single action. |
| **G3.4** | AT4 | AND | `-` | Battery monitoring is a single action. |
| **G3.5** | AT6 | AND | `-` | Reassignment is a single action. |
| **G3.6** | AT13 | AND | `-` | Parallel assignment is a single action. |
| **G5.1** | AT10 | AND | `-` | Alert is a single action. |
| **G5.2** | AT11 | AND | `-` | Reporting is a single action. |

---

### Why this structure?

1. **Sequential vs Parallel** – The mission naturally splits into a *collection* phase followed by a *delivery* phase; hence G1 uses a sequential (`;`) runtime.  
2. **Parallelism** – Within each phase, multiple robots can operate concurrently (e.g., collecting from different storages or delivering to different destinations). Therefore, G2 and G3 use parallel (`#`) runtimes.  
3. **Battery & Failure Handling** – Battery thresholds and failure events are independent of the main flow and can happen at any time; they are modeled as separate goals (G2.4, G2.5, G3.4, G3.5, G5) that are executed in parallel with the main phases.  
4. **Task Granularity** – Each leaf goal is decomposed into a single task that a robot can execute. All tasks are AND‑related to their parent goal because the goal is only satisfied when the task succeeds.  
5. **Parallel Assignment Tasks** – AT12 and AT13 capture the explicit parallelization strategy described in the mission (multiple robots assigned to parallel collect‑deliver tasks).  

This goal model faithfully captures the mission’s structure, constraints, and parallel execution opportunities while providing a clear mapping from high‑level objectives to concrete robot actions.
