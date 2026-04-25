## Goal Model – Multi‑Robot Resource Transfer Mission  

Below you will find a complete goal model that decomposes the mission description into a hierarchy of **goals** and **tasks**.  
All goals are numbered depth‑first (G1, G2, …) and all tasks are numbered depth‑first (AT1, AT2, …).  
Each goal and task is accompanied by a justification that explains why the chosen decomposition, runtime annotation, relation, and other attributes follow the mission description.

---

### 1. Goal Tables  

| Name                                                   | Text                                                                                                                           | Runtime | Goal Type | Enquired Information / Target Condition | Relation | Justification                                                                                                                                                                       | Ground truth I                                          | Ground truth C | Ground truth E |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------- | --------- | --------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------- | -------------- |
| **G1: Transfer resources from storage to destination** | The robot must collect the required resources from storage and deliver them to the requesting agent at the specified location. | **#**   | Perform   | N/A                                     | **AND**  | All sub-goals (collection, delivery, monitoring, handling, alerting) must be fulfilled. The mission allows multiple items to be processed concurrently, hence the parallel runtime. | OK                                                      | Ok             |                |
| **G2: Collect required resources**                     | The robot must navigate to the storage, request resources, and wait for retrieval.                                             | **;**   | Perform   | N/A                                     | **AND**  | Tasks must be performed in the order: navigate → request → wait.                                                                                                                    | Achieve. Target condition: all resources were collected | Ok             |                |
| **G3: Deliver collected resources**                    | The robot must navigate to the destination and deliver the resources.                                                          | **;**   | Perform   | N/A                                     | **AND**  | Tasks must be performed in the order: navigate → deliver.                                                                                                                           | Achieve. Target condition: all resources were delivered | Ok             |                |
| **G4: Monitor battery during collection**              | The robot must check its battery level during the collection phase.                                                            | **;**   | Query     | *battery level*                         | **AND**  | Battery level must be queried before deciding on low-battery handling.                                                                                                              | Perfom                                                  | Ok             |                |
| **G5: Monitor battery during delivery**                | The robot must check its battery level during the delivery phase.                                                              | **;**   | Query     | *battery level*                         | **AND**  | Battery level must be queried before deciding on low-battery handling.                                                                                                              | Perform                                                 | Ok             |                |
| **G6: Handle low battery during collection**           | If battery <10 % during collection, robot returns to charging station and assigns mission to another robot.                    | **;**   | Perform   | N/A                                     | **AND**  | Both actions (recharge, reassign) must be performed.                                                                                                                                | ok                                                      | Ok             |                |
| **G7: Handle low battery during delivery**             | If battery <30 % during delivery, robot returns resource to checkpoint and assigns remaining task to another robot.            | **;**   | Perform   | N/A                                     | **AND**  | All actions (checkpoint return, reassign) must be performed.                                                                                                                        | OK                                                      | Ok             |                |
| **G8: Assign mission to another robot**                | The robot assigns the mission to another robot.                                                                                | **;**   | Perform   | N/A                                     | **AND**  | Only one assignment action is needed.                                                                                                                                               | OK                                                      | Ok             |                |
| **G9: Return resource to checkpoint**                  | The robot returns the resource to a checkpoint.                                                                                | **;**   | Perform   | N/A                                     | **AND**  | Navigation and return actions must be performed.                                                                                                                                    | OK                                                      | Ok             |                |
| **G10: Trigger alert and send report**                 | In case of failure to return resource to checkpoint, an alert is triggered and report sent to sector manager.                  | **;**   | Perform   | N/A                                     | **AND**  | Both alert and report actions must be performed.                                                                                                                                    | OK                                                      | Ok             |                |


> **Decomposition** – All goals use **AND** decomposition because every child must be satisfied for the parent to succeed.  
> **Runtime** – `#` indicates parallel execution (G1), while `;` indicates sequential execution for all other goals.

---

### 2. Task Tables  

| Name | Text | Relation | Location | Number of Robots | Justification |
|------|------|----------|----------|------------------|---------------|
| **AT1: Navigate to storage** | Robot moves to the storage location where resources are located. | **AND** | *storage* | 1 | Only the assigned robot needs to navigate. |
| **AT2: Send request to storage** | Robot sends a message to the storage specifying the requested resources. | **AND** | *storage* | 1 | Only the assigned robot performs the request. |
| **AT3: Wait for resources** | Robot waits until resources are retrieved from storage. | **AND** | *storage* | 1 | Only the assigned robot waits. |
| **AT4: Navigate to checkpoint** | Robot moves to the checkpoint to return resources. | **AND** | *checkpoint* | 1 | Only the assigned robot performs navigation. |
| **AT5: Return resource to checkpoint** | Robot returns the resource to the checkpoint. | **AND** | *checkpoint* | 1 | Only the assigned robot returns the resource. |
| **AT6: Navigate to destination** | Robot moves to the destination where resources must be delivered. | **AND** | *destination* | 1 | Only the assigned robot moves. |
| **AT7: Deliver resources** | Robot delivers the resources to the requesting agent. | **AND** | *destination* | 1 | Only the assigned robot delivers. |
| **AT8: Navigate to charging station** | Robot moves to the charging station to recharge. | **AND** | *charging station* | 1 | Only the assigned robot recharges. |
| **AT9: Assign mission to another robot** | Robot assigns the mission to another robot. | **AND** | *central control* | 1 | Only the assigned robot performs assignment. |
| **AT10: Trigger alert** | Robot triggers an alert in case of failure. | **AND** | *central control* | 1 | Only the assigned robot triggers alert. |
| **AT11: Send report** | Robot sends report to sector manager. | **AND** | *central control* | 1 | Only the assigned robot sends report. |
| **AT12: Check battery level** | Robot checks its battery level. | **AND** | *robot* | 1 | Only the assigned robot checks battery. |

> **Relation** – All tasks are linked to their parent goal with **AND** because every task must be executed for the goal to succeed.  
> **Location** – Chosen to reflect the place where the action takes place (storage, checkpoint, destination, charging station, central control, robot).  
> **Number of Robots** – The mission description specifies a single robot performing each action; parallelism is achieved by assigning different robots to different sub‑missions (G1’s parallel runtime).

---

### 3. Summary Table (Goals & Tasks)  

| ID | Type | Title | Key Attribute | Relation | Runtime / Location | Justification |
|----|------|-------|---------------|----------|-------------------|---------------|
| G1 | Goal | Transfer resources from storage to destination | N/A | AND | # | Parallel sub‑missions allowed. |
| G2 | Goal | Collect required resources | N/A | AND | ; | Sequential collection steps. |
| G3 | Goal | Deliver collected resources | N/A | AND | ; | Sequential delivery steps. |
| G4 | Goal | Monitor battery during collection | battery level | AND | ; | Battery query needed. |
| G5 | Goal | Monitor battery during delivery | battery level | AND | ; | Battery query needed. |
| G6 | Goal | Handle low battery during collection | N/A | AND | ; | Recharge + reassign. |
| G7 | Goal | Handle low battery during delivery | N/A | AND | ; | Checkpoint return + reassign. |
| G8 | Goal | Assign mission to another robot | N/A | AND | ; | Assignment action. |
| G9 | Goal | Return resource to checkpoint | N/A | AND | ; | Navigation + return. |
| G10 | Goal | Trigger alert and send report | N/A | AND | ; | Alert + report. |
| AT1 | Task | Navigate to storage | storage | AND | storage | Single robot navigation. |
| AT2 | Task | Send request to storage | storage | AND | storage | Single robot request. |
| AT3 | Task | Wait for resources | storage | AND | storage | Single robot wait. |
| AT4 | Task | Navigate to checkpoint | checkpoint | AND | checkpoint | Single robot navigation. |
| AT5 | Task | Return resource to checkpoint | checkpoint | AND | checkpoint | Single robot return. |
| AT6 | Task | Navigate to destination | destination | AND | destination | Single robot navigation. |
| AT7 | Task | Deliver resources | destination | AND | destination | Single robot delivery. |
| AT8 | Task | Navigate to charging station | charging station | AND | charging station | Single robot recharge. |
| AT9 | Task | Assign mission to another robot | central control | AND | central control | Single robot assignment. |
| AT10 | Task | Trigger alert | central control | AND | central control | Single robot alert. |
| AT11 | Task | Send report | central control | AND | central control | Single robot report. |
| AT12 | Task | Check battery level | robot | AND | robot | Single robot battery check. |

---

### 4. Logical Relationships  

| Parent → Children | Relation & Runtime | Justification |
|-------------------|--------------------|---------------|
| **G1 → G2, G3, G4, G5, G6, G7, G8, G9, G10** | **AND** **[#]** | All sub‑goals must be satisfied for the mission to succeed; the mission allows parallel execution of multiple items. |
| **G2 → AT1, AT2, AT3** | **AND** **[;]** | Collection steps must be performed in order: navigate → request → wait. |
| **G3 → AT6, AT7** | **AND** **[;]** | Delivery steps must be performed in order: navigate → deliver. |
| **G4 → AT12** | **AND** **[;]** | Battery level must be queried before deciding on low‑battery handling. |
| **G5 → AT12** | **AND** **[;]** | Battery level must be queried before deciding on low‑battery handling. |
| **G6 → AT8, AT9** | **AND** **[;]** | Recharge and reassign must be performed. |
| **G7 → AT4, AT5, AT9** | **AND** **[;]** | Return to checkpoint, return resource, and reassign must be performed. |
| **G8 → AT9** | **AND** **[;]** | Assignment action. |
| **G9 → AT4, AT5** | **AND** **[;]** | Navigation to checkpoint and return resource. |
| **G10 → AT10, AT11** | **AND** **[;]** | Alert and report actions. |

---

### 5. Remarks & Justifications  

1. **Parallelism** – The mission explicitly states that “multiple robots can be assigned to parallel collect‑deliver tasks to reduce the time to finish the mission.” This is captured by the `#` runtime on the top‑level goal G1.  
2. **Sequentiality** – Within each sub‑mission (collection or delivery) the robot must perform actions in a fixed order (navigate → request → wait, etc.). Hence the `;` runtime for all other goals.  
3. **Battery Monitoring** – The description distinguishes two thresholds (10 % for collection, 30 % for delivery). These are represented as separate query goals (G4, G5) that feed into the low‑battery handling goals (G6, G7).  
4. **Fallback / Reassignment** – When a robot’s battery is low, it must return to a charging station or checkpoint and assign the remaining task to another robot. This is modeled as a perform goal (G6, G7) that triggers the assignment goal G8.  
5. **Alerting** – Failure to return a resource to a checkpoint triggers an alert and a report. This is captured by G10 and its two tasks (AT10, AT11).  
6. **Task Locations** – Each task’s location is chosen to match the place where the action logically occurs (storage, checkpoint, destination, charging station, central control, robot).  
7. **Number of Robots** – The mission description implies a single robot performing each action; parallelism is achieved by assigning different robots to different sub‑missions. Therefore, all tasks are assigned to **1** robot.  

---

This goal model provides a clear, hierarchical decomposition of the mission into intentional goals and concrete tasks, with explicit runtime annotations, relations, and justifications that directly reflect the mission description.
