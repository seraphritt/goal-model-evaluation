**Goal Model – Multi‑Robot Resource Delivery Mission**  
*(Depth‑first numbering, “#” = parallel, “;” = sequential, “FALLBACK(a,b)” = fallback)*  

| **Name**     | **Text**                                                                | **Runtime**                                  | **Goal Type** | **Target / Enquired**                        | **Relation**        | **Justification**                                                                                                                                          | **Ground truth I** | **Ground truth C** | **Ground truth E** |
| ------------ | ----------------------------------------------------------------------- | -------------------------------------------- | ------------- | -------------------------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------ | ------------------ |
| **G1**       | Deliver the requested resources to the specified location.              | `;`                                          | Achieve       | *Resources are at the destination location.* | Root (no parent)    | The mission’s ultimate objective is to have the resources delivered. The collection and delivery phases must happen one after the other, hence sequential. | Perform.                   |                    |                    |
| **G2**       | Collect resources from storage places.                                  | `;`                                          | Perform       | –                                            | AND with **G1**     | Collection must finish before delivery can start.                                                                                                          |  Achieve. Target condition: all resources were collected.                 |                    |                    |
| **G2.1**     | Determine the optimal order of storages based on waiting time and path. | `-`                                          | Query         | *Optimal sequence of storages.*              | AND with **G2**     | The robot needs this information before it can assign itself to a storage.                                                                                 | OK                   |                    |                    |
| **G2.2**     | Assign robots to storage tasks based on the determined order.           | `-`                                          | Perform       | –                                            | AND with **G2**     | After the order is known, robots must be assigned accordingly.                                                                                             |   OK                 |                    |                    |
| **G2.3**     | Robots travel to storage, request resources, and wait for retrieval.    | `#`                                          | Perform       | –                                            | AND with **G2**     | Multiple robots can execute these steps in parallel.                                                                                                       |  OK                  |                    |                    |
| **G2.4**     | Handle low battery during collection.                                   | `FALLBACK(G2.4.1,G2.4.2)`                    | Perform       | –                                            | AND with **G2**     | If the battery drops to 10 %, the robot can either recharge or hand the task to another robot.                                                             |  OK                  |                    |                    |
| **G2.4.1**   | Robot returns to recharging station.                                    | `-`                                          | Perform       | –                                            | AND with **G2.4**   | Primary fallback when battery is low.                                                                                                                      | OK                   |                    |                    |
| **G2.4.2**   | Assign remaining collection task to another robot.                      | `-`                                          | Perform       | –                                            | AND with **G2.4**   | Alternative fallback if recharging is not possible.                                                                                                        |  OK                  |                    |                    |
| **G3**       | Deliver collected resources to destination.                             | `#`                                          | Perform       | –                                            | AND with **G1**     | Delivery can be performed by several robots in parallel.                                                                                                   |  Achieve. Target condition: all resources were delivered.                  |                    |                    |
| **G3.1**     | Robots deliver resources to specified location.                         | `#`                                          | Perform       | –                                            | AND with **G3**     | Each robot can deliver its load independently.                                                                                                             |   OK                 |                    |                    |
| **G3.2**     | Handle low battery during delivery.                                     | `FALLBACK(FALLBACK(G3.2.1,G3.2.1.2),G3.2.2)` | Perform       | –                                            | AND with **G3**     | If battery drops to 30 %, the robot can either return to a checkpoint (with a fallback to alert) or hand the task to another robot.                        |  OK                  |                    |                    |
| **G3.2.1**   | Return resource to checkpoint if battery low.                           | `FALLBACK(G3.2.1.1,G3.2.1.2)`                | Perform       | –                                            | AND with **G3.2**   | Primary action; if it fails, an alert must be triggered.                                                                                                   |  OK                  |                    |                    |
| **G3.2.1.1** | Robot returns resource to checkpoint.                                   | `-`                                          | Perform       | –                                            | AND with **G3.2.1** | The actual return action.                                                                                                                                  |   OK                 |                    |                    |
| **G3.2.1.2** | Trigger alert and report to sector manager if return fails.             | `-`                                          | Perform       | –                                            | AND with **G3.2.1** | Failure handling.                                                                                                                                          | OK                   |                    |                    |
| **G3.2.2**   | Assign remaining delivery task to another robot.                        | `-`                                          | Perform       | –                                            | AND with **G3.2**   | Alternative when the robot cannot return to the checkpoint.                                                                                                |                    | OK                   |                    |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Robot travels to storage location. | AND with **G2.3** | *Storage* | 1 | Each robot must reach the storage to request resources. |
| **AT2** | Robot sends message to storage with resource specification. | AND with **G2.3** | *Storage* | 1 | The robot must explicitly request the needed items. |
| **AT3** | Robot waits until resources are retrieved. | AND with **G2.3** | *Storage* | 1 | The robot must wait for the storage to hand over the load. |
| **AT4** | Robot returns to recharging station. | AND with **G2.4.1** | *Recharging station* | 1 | Battery low triggers a recharge. |
| **AT5** | Robot assigns remaining collection task to another robot. | AND with **G2.4.2** | *Current location* | 1 | Alternative to recharging. |
| **AT6** | Robot delivers resource to specified destination. | AND with **G3.1** | *Destination* | 1 | The core delivery action. |
| **AT7** | Robot returns resource to checkpoint. | AND with **G3.2.1.1** | *Checkpoint* | 1 | Primary fallback when battery is low during delivery. |
| **AT8** | Robot triggers alert and sends report to sector manager. | AND with **G3.2.1.2** | *Sector manager* | 1 | Failure handling if return to checkpoint fails. |
| **AT9** | Robot assigns remaining delivery task to another robot. | AND with **G3.2.2** | *Current location* | 1 | Alternative when the robot cannot return to the checkpoint. |
| **AT10** | Robot queries waiting time and path to determine optimal order. | AND with **G2.1** | *Planning area* | 1 | The robot must compute the order before assignment. |
| **AT11** | Robot assigns robots to storage tasks based on determined order. | AND with **G2.2** | *Planning area* | [1,n] | Multiple robots can be assigned in parallel. |

---

### Summary Table (Goals + Tasks)

| **ID** | **Type** | **Title** | **Runtime / Relation** |
|--------|----------|-----------|------------------------|
| G1 | Goal | Deliver Requested Resources to Destination | `;` (sequential) |
| G2 | Goal | Collection Phase | `;` |
| G2.1 | Goal | Determine Storage Order | `-` |
| G2.2 | Goal | Assign Robots to Storage Tasks | `-` |
| G2.3 | Goal | Execute Collection Tasks | `#` |
| G2.4 | Goal | Battery Management during Collection | `FALLBACK(G2.4.1,G2.4.2)` |
| G2.4.1 | Goal | Recharge Robot | `-` |
| G2.4.2 | Goal | Assign Mission to Another Robot | `-` |
| G3 | Goal | Delivery Phase | `#` |
| G3.1 | Goal | Deliver Resources to Destination | `#` |
| G3.2 | Goal | Battery Management during Delivery | `FALLBACK(FALLBACK(G3.2.1,G3.2.1.2),G3.2.2)` |
| G3.2.1 | Goal | Return to Checkpoint | `FALLBACK(G3.2.1.1,G3.2.1.2)` |
| G3.2.1.1 | Goal | Return Resource to Checkpoint | `-` |
| G3.2.1.2 | Goal | Alert on Failure | `-` |
| G3.2.2 | Goal | Assign Remaining Task to Another Robot | `-` |
| AT1 | Task | Go to Storage | AND with G2.3 |
| AT2 | Task | Send Request to Storage | AND with G2.3 |
| AT3 | Task | Wait for Retrieval | AND with G2.3 |
| AT4 | Task | Recharge Robot | AND with G2.4.1 |
| AT5 | Task | Assign Mission to Another Robot | AND with G2.4.2 |
| AT6 | Task | Deliver to Destination | AND with G3.1 |
| AT7 | Task | Return to Checkpoint | AND with G3.2.1.1 |
| AT8 | Task | Alert to Sector Manager | AND with G3.2.1.2 |
| AT9 | Task | Assign Remaining Delivery Task to Another Robot | AND with G3.2.2 |
| AT10 | Task | Determine Storage Order | AND with G2.1 |
| AT11 | Task | Assign Robots to Storage Tasks | AND with G2.2 |

---

### Logical Relationships

- **G1 → G2, G3**  
  *Relation*: AND, Runtime `;` (sequential)  
  *Justification*: The mission must first collect resources before delivering them.

- **G2 → G2.1, G2.2, G2.3, G2.4**  
  *Relation*: AND, Runtime `;` (sequential)  
  *Justification*: Determining order, assigning robots, executing collection, and handling battery are distinct, sequential steps within the collection phase.

- **G2.3 → AT1, AT2, AT3**  
  *Relation*: AND, Runtime `#` (parallel)  
  *Justification*: Each robot can perform the three sub‑tasks concurrently.

- **G2.4 → AT4, AT5**  
  *Relation*: AND, Runtime `FALLBACK` (fallback)  
  *Justification*: If battery is low, the robot can either recharge (AT4) or hand the task to another robot (AT5).

- **G3 → G3.1, G3.2**  
  *Relation*: AND, Runtime `#` (parallel)  
  *Justification*: Delivery and battery management can proceed concurrently across robots.

- **G3.1 → AT6**  
  *Relation*: AND, Runtime `#` (parallel)  
  *Justification*: Each robot can deliver its load independently.

- **G3.2 → AT7, AT8, AT9**  
  *Relation*: AND, Runtime `FALLBACK` (nested fallback)  
  *Justification*: Battery low during delivery triggers either a return to checkpoint (AT7) with a fallback to alert (AT8) or handing over the task to another robot (AT9).

- **G2.1 → AT10**  
  *Relation*: AND, Runtime `-`  
  *Justification*: The query task is the only child of the query goal.

- **G2.2 → AT11**  
  *Relation*: AND, Runtime `-`  
  *Justification*: The assignment task is the only child of the perform goal.

---

**Why this structure?**  
The mission is naturally split into two major phases—collection and delivery—each with its own sub‑tasks and failure handling. Parallel execution is exploited where multiple robots can act independently (e.g., collecting from different storages, delivering to different destinations). Fallbacks capture the battery‑low contingencies, ensuring that the mission can continue by either recharging or handing over the task. The query goal for determining the optimal storage order reflects the need for information before planning. All relations are explicitly justified by the mission description.
