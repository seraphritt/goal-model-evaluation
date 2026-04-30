## 1. Goal Model – Tables
| **Name**                                       | **Text**                                                                             | **Runtime**           | **Goal Type** | **Target Condition / Enquired Info**                                                                     | **Relation**    | **Justification**                                                                                                                                           | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                       |
| ---------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------- | ------------- | -------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1: Deliver Resources**                      | Deliver the required resources to the requesting agent at the specified location.    | `#`                   | Achieve       | *Resources are physically located at the destination and the requesting agent has acknowledged receipt.* | – (root)        | The mission can be performed by several robots in parallel (collection and delivery), so the top-level goal is executed concurrently.                       | Perform.                                                 | OK                 | Perform.                                                 |
| **G2: Collect Resources**                      | Collect the required resources from storage locations.                               | `#`                   | Perform       | –                                                                                                        | `AND` (with G1) | Collection must be completed before delivery, but several storages can be accessed in parallel by different robots.                                         | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G3: Deliver Resources**                      | Deliver the collected resources to the specified destination.                        | `#`                   | Perform       | –                                                                                                        | `AND` (with G1) | Delivery is a distinct phase that can run concurrently with other deliveries performed by other robots.                                                     | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G4: Handle Low-Battery in Collection**       | Handle a low-battery situation that occurs during the collection phase.              | `FALLBACK(AT4, AT5)`  | Perform       | –                                                                                                        | `AND` (with G2) | If the battery falls below 10 %, the robot either recharges or hands the task over; the fallback captures the two mutually exclusive alternatives.          | OK                                                       | OK                 | OK                                                       |
| **G5: Handle Low-Battery in Delivery**         | Handle a low-battery situation that occurs during the delivery phase.                | `FALLBACK(AT7, AT8)`  | Perform       | –                                                                                                        | `AND` (with G3) | If the battery falls below 30 %, the robot either returns to a checkpoint or hands the remaining delivery over; the fallback captures the two alternatives. | OK                                                       | OK                 | OK                                                       |
| **G6: Handle Failure to Return to Checkpoint** | Handle a failure to return the resource to a checkpoint during low-battery delivery. | `FALLBACK(AT9, AT10)` | Perform       | –                                                                                                        | `AND` (with G5) | If the robot cannot return to the checkpoint, an alert is triggered and a report is sent; the fallback captures the two required actions.                   | OK                                                       | OK                 | OK                                                       |
| **G7: Parallel Collection Assignment**         | Distribute collection tasks across multiple robots to parallelize collection.        | `#`                   | Perform       | –                                                                                                        | `AND` (with G2) | Multiple robots can be assigned to different storages, so the goal is executed in parallel.                                                                 | OK                                                       | OK                 | OK                                                       |

---

## 2. Task Model – Tables

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|--------------------|
| **AT1: Estimate Waiting Time & Path** | Compute the estimated waiting time and path to the nearest storage location that contains the required resources. | `AND` (with G2) | Robot’s current location | 1 | Only the robot that will perform the collection needs to compute the estimate. |
| **AT2: Request Resources** | Send a message to the storage specifying the requested resources and wait for retrieval. | `AND` (with G2) | Storage location | 1 | The request is an action performed by the collecting robot. |
| **AT3: Retrieve Resources** | Physically pick up the requested resources from the storage. | `AND` (with G2) | Storage location | 1 | Retrieval is performed by the robot that has already requested the items. |
| **AT4: Go to Recharge Station** | Navigate to the nearest recharging station to recharge battery. | `AND` (with G4) | Recharge station | 1 | The robot must recharge itself before continuing. |
| **AT5: Assign Mission to Another Robot** | Notify the control system to assign the remaining collection task to another robot. | `AND` (with G4) | Control center | 1 | Only the robot that detected low battery needs to hand over the task. |
| **AT6: Deliver Resources** | Transport the collected resources to the specified destination location. | `AND` (with G3) | Destination location | 1 | Delivery is performed by the robot that holds the items. |
| **AT7: Return Resource to Checkpoint** | Return the partially delivered resource to the nearest checkpoint for safety. | `AND` (with G5) | Checkpoint location | 1 | The robot must ensure the resource is safe when battery is low. |
| **AT8: Assign Remaining Delivery to Another Robot** | Notify the control system to assign the remaining delivery task to another robot. | `AND` (with G5) | Control center | 1 | The robot that is low on battery hands over the remaining delivery. |
| **AT9: Trigger Alert** | Generate an alert for failure to return resource to checkpoint. | `AND` (with G6) | Robot’s current location | 1 | The robot that failed to return the resource must notify the sector manager. |
| **AT10: Send Report** | Send a detailed report of the failure to the sector manager. | `AND` (with G6) | Sector manager office | 1 | The report must reach the sector manager for action. |
| **AT11: Determine Delivery Location** | Determine the exact delivery destination for the resources. | `AND` (with G3) | Destination location | 1 | The robot needs to know where to deliver before moving. |
| **AT12: Parallel Collection Assignment** | Distribute collection tasks across multiple robots to parallelize collection. | `AND` (with G7) | Control center | `[1,∞]` | Multiple robots can be assigned; the range allows any number of robots to participate. |

---

## 3. Summary Table (Goals & Tasks)

| **Goal ID** | **Goal Title** | **Goal Type** | **Runtime** | **Relation to Parent** | **Tasks** |
|-------------|----------------|---------------|-------------|------------------------|-----------|
| G1 | Deliver Resources | Achieve | `#` | – | – |
| G2 | Collect Resources | Perform | `#` | `AND` (with G1) | AT1, AT2, AT3, G4, G7 |
| G3 | Deliver Resources | Perform | `#` | `AND` (with G1) | AT11, AT6, G5 |
| G4 | Handle Low‑Battery in Collection | Perform | `FALLBACK(AT4, AT5)` | `AND` (with G2) | AT4, AT5 |
| G5 | Handle Low‑Battery in Delivery | Perform | `FALLBACK(AT7, AT8)` | `AND` (with G3) | AT7, AT8, G6 |
| G6 | Handle Failure to Return to Checkpoint | Perform | `FALLBACK(AT9, AT10)` | `AND` (with G5) | AT9, AT10 |
| G7 | Parallel Collection Assignment | Perform | `#` | `AND` (with G2) | AT12 |

---

## 4. Logical Relationships

| **Parent Goal** | **Children** | **Relation** | **Runtime** | **Justification** |
|-----------------|--------------|--------------|-------------|-------------------|
| **G1** | G2, G3, G7 | `AND` | `#` | The mission is achieved only when collection, delivery, and parallel assignment are all completed; the `#` allows concurrent execution of these phases by different robots. |
| **G2** | AT1, AT2, AT3, G4, G7 | `AND` | `#` | All collection sub‑tasks and the low‑battery handler must succeed; the `#` permits parallel collection from multiple storages. |
| **G3** | AT11, AT6, G5 | `AND` | `#` | Delivery requires determining the destination, moving the resources, and handling low battery; `#` allows parallel deliveries. |
| **G4** | AT4, AT5 | `AND` | `FALLBACK(AT4, AT5)` | If battery <10 % the robot either recharges (AT4) or hands over the task (AT5); the fallback captures the mutually exclusive alternatives. |
| **G5** | AT7, AT8, G6 | `AND` | `FALLBACK(AT7, AT8)` | If battery <30 % the robot either returns to a checkpoint (AT7) or hands over the remaining delivery (AT8); the fallback captures the alternatives. |
| **G6** | AT9, AT10 | `AND` | `FALLBACK(AT9, AT10)` | Failure to return to a checkpoint triggers an alert (AT9) and a report (AT10); the fallback ensures both are performed. |
| **G7** | AT12 | `AND` | `#` | Parallel collection assignment can be carried out concurrently with other collection tasks; `#` allows multiple robots to be assigned. |

---

### Overall Reasoning

1. **Mission Decomposition** – The description separates *collection* and *delivery* phases; thus two high‑level perform goals are created (G2 and G3).  
2. **Parallelism** – The text explicitly allows multiple robots to perform collection and delivery in parallel, so the `#` operator is used at the top level and for the collection/delivery sub‑goals.  
3. **Battery Management** – Low‑battery situations are handled by dedicated sub‑goals (G4, G5) that use a `FALLBACK` operator to capture the two possible actions (recharge or hand‑over).  
4. **Failure Handling** – A failure to return to a checkpoint triggers an alert and a report; this is captured by G6 with a `FALLBACK`.  
5. **Task Assignment** – The ability to assign tasks to multiple robots is represented by G7 and its single task AT12, allowing dynamic parallelism.  
6. **Goal Types** – The top‑level goal is an *Achieve* goal because it specifies a future world state (resources at destination). All other goals are *Perform* goals because they describe concrete actions that must be executed.  

This model provides a clear, hierarchical decomposition of the mission into goals and tasks, explicitly captures parallelism, fallback behavior, and failure handling, and justifies every design choice based on the mission description.
