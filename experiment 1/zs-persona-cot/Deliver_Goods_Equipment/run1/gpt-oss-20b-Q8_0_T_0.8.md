**Goal Model – Multi‑Robot Resource Delivery Mission**

| **Name**                                              | **Text**                                                                                                                                                                                                | **Runtime**                | **Goal Type** | **Target Condition / Enquired Info**               | **Relation**    | **Justification**                                                                                                | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------- | -------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1 – Deliver resources to destination**             | Ensure that the requested resources are physically located at the destination and handed over to the requesting agent.                                                                                  | `;` (sequential)           | Achieve       | *Resource at destination & delivered to requester* | N/A (root)      | Collection must finish before delivery can start; therefore the two high-level phases are executed sequentially. | Perform                                                  | OK                 | Perform                                                  |
| **G2 – Perform collection phase**                     | Execute all activities that bring the required resources from storage to the robot.                                                                                                                     | `#` (parallel)             | Perform       |                                                    | AND (with G1)   | Multiple robots may collect from different storages simultaneously; the sub-tasks can therefore run in parallel. | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G2.1 – Navigate to storage location**               | Move the robot to the storage place where the needed resources are located.                                                                                                                             | `-` (leaf)                 | Perform       |                                                    | AND (with G2)   | This is a prerequisite for any subsequent action in the collection phase.                                        | OK                                                       | OK                 | OK                                                       |
| **G2.2 – Request resources**                          | Send a precise request message to the storage, specifying the exact resources needed.                                                                                                                   | `-`                        | Perform       |                                                    | AND (with G2)   | Must happen after reaching the storage.                                                                          | Query. enquired information: resources to be collected.  | OK                 | Query. enquired information: resources to be collected.  |
| **G2.3 – Wait for retrieval**                         | Remain idle until the storage confirms that the resources have been retrieved and are ready for pickup.                                                                                                 | `-`                        | Perform       |                                                    | AND (with G2)   | Logical successor of the request.                                                                                | OK                                                       | OK                 | OK                                                       |
| **G2.4 – Handle battery low during collection**       | If the robot’s battery falls below 10 % during collection, it must either recharge or hand the task over to another robot.                                                                              | `FALLBACK(AT1, AT2)`       | Perform       |                                                    | AND (with G2)   | The mission specifies a fallback: first try to recharge, otherwise delegate the task.                            | OK                                                       | OK                 | OK                                                       |
| **G3 – Perform delivery phase**                       | Execute all activities that move the collected resources from the robot to the destination location.                                                                                                    | `#` (parallel)             | Perform       |                                                    | AND (with G1)   | Multiple robots may deliver concurrently after the collection phase completes.                                   | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G3.1 – Deliver resources to destination**           | Physically transport the resources to the specified delivery location and hand them over to the requester.                                                                                              | `-`                        | Perform       |                                                    | AND (with G3)   | Core of the delivery phase.                                                                                      | OK                                                       | OK                 | OK                                                       |
| **G3.2 – Handle battery low during delivery**         | If the robot’s battery falls below 30 % during delivery, it must return the resource to a checkpoint and hand the remaining delivery over to another robot; if it cannot return, an alert is triggered. | `FALLBACK(G3.2.1, G3.2.2)` | Perform       |                                                    | AND (with G3)   | The mission explicitly defines a two-step fallback: attempt to return, otherwise alert.                          | OK                                                       | OK                 | OK                                                       |
| **G3.2.1 – Return resource to checkpoint & delegate** | Return the resource to a designated checkpoint and assign the remaining delivery to another robot.                                                                                                      | `AND(AT3, AT4)`            | Perform       |                                                    | AND (with G3.2) | Both actions must succeed for the fallback to be considered successful.                                          | OK                                                       | OK                 | OK                                                       |
| **G3.2.2 – Trigger alert & send report**              | If returning to the checkpoint fails, trigger an alert and send a report to the sector manager.                                                                                                         | `AND(AT5, AT6)`            | Perform       |                                                    | AND (with G3.2) | Both alert and report are required to complete the failure handling.                                             | OK                                                       | OK                 | OK                                                       |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1 – Go to recharge station** | Move the robot to the nearest recharge station to replenish its battery. | AND (with G2.4) | Recharge station | 1 | Only the robot with low battery needs to recharge. |
| **AT2 – Assign mission to another robot** | Inform another available robot of the pending collection task so it can continue the mission. | AND (with G2.4) | Current location / central command | 1 | Delegation is performed by the low‑battery robot. |
| **AT3 – Return resource to checkpoint** | Move the robot carrying a resource back to a predefined checkpoint before handing it over. | AND (with G3.2.1) | Checkpoint | 1 | Required step in the battery‑low delivery fallback. |
| **AT4 – Assign remaining task to another robot** | Notify a second robot of the remaining delivery task, including the checkpoint location of the resource. | AND (with G3.2.1) | Checkpoint | 1 | Enables the new robot to pick up the resource without confusion. |
| **AT5 – Trigger alert** | Raise an alarm indicating that the robot could not return the resource to the checkpoint. | AND (with G3.2.2) | Current location | 1 | Immediate notification of a critical failure. |
| **AT6 – Send report to sector manager** | Transmit a detailed report of the failure to the sector manager for further action. | AND (with G3.2.2) | Central command | 1 | Completes the failure‑handling protocol. |
| **AT7 – Navigate to storage location** | Move the robot to the storage location where the resources are kept. | AND (with G2.1) | Storage location (variable) | 1 | Precursor to requesting resources. |
| **AT8 – Request resources** | Send a message to the storage specifying the exact resources required. | AND (with G2.2) | Storage location | 1 | Needed to trigger the storage to prepare the items. |
| **AT9 – Wait for retrieval** | Remain at the storage until the storage confirms that the resources are ready for pickup. | AND (with G2.3) | Storage location | 1 | Synchronisation point before pickup. |
| **AT10 – Navigate to delivery location** | Move the robot to the destination where the resources must be delivered. | AND (with G3.1) | Delivery location | 1 | Precursor to the actual delivery. |
| **AT11 – Deliver resource** | Physically hand the resource over to the requesting agent at the destination. | AND (with G3.1) | Delivery location | 1 | Final step of the delivery phase. |

---

### Summary Table (All Goals & Tasks)

| **ID** | **Title** | **Type** | **Runtime / Relation** | **Justification** |
|--------|-----------|----------|------------------------|-------------------|
| G1 | Deliver resources to destination | Achieve | `;` (sequential) | Collection must finish before delivery |
| G2 | Perform collection phase | Perform | `#` (parallel) | Multiple robots can collect concurrently |
| G2.1 | Navigate to storage | Perform | AND (with G2) | Precedes request |
| G2.2 | Request resources | Perform | AND (with G2) | Follows navigation |
| G2.3 | Wait for retrieval | Perform | AND (with G2) | After request |
| G2.4 | Handle battery low during collection | Perform | `FALLBACK(AT1, AT2)` | Fallback: recharge or delegate |
| G3 | Perform delivery phase | Perform | `#` (parallel) | Multiple robots can deliver concurrently |
| G3.1 | Deliver resources to destination | Perform | AND (with G3) | Core delivery |
| G3.2 | Handle battery low during delivery | Perform | `FALLBACK(G3.2.1, G3.2.2)` | Fallback: return or alert |
| G3.2.1 | Return resource to checkpoint & delegate | Perform | `AND(AT3, AT4)` | Both must succeed |
| G3.2.2 | Trigger alert & send report | Perform | `AND(AT5, AT6)` | Both needed for failure handling |
| AT1 | Go to recharge station | Task | AND (with G2.4) | Only low‑battery robot recharges |
| AT2 | Assign mission to another robot | Task | AND (with G2.4) | Delegation by low‑battery robot |
| AT3 | Return resource to checkpoint | Task | AND (with G3.2.1) | Needed for fallback |
| AT4 | Assign remaining task to another robot | Task | AND (with G3.2.1) | Enables new robot to pick up |
| AT5 | Trigger alert | Task | AND (with G3.2.2) | Immediate notification |
| AT6 | Send report to sector manager | Task | AND (with G3.2.2) | Completes failure protocol |
| AT7 | Navigate to storage location | Task | AND (with G2.1) | Precursor to request |
| AT8 | Request resources | Task | AND (with G2.2) | Triggers storage to prepare |
| AT9 | Wait for retrieval | Task | AND (with G2.3) | Synchronises pickup |
| AT10 | Navigate to delivery location | Task | AND (with G3.1) | Precursor to delivery |
| AT11 | Deliver resource | Task | AND (with G3.1) | Final hand‑over |

---

### Logical Relationships

- **G1 → G2, G3**  
  - **Relation:** AND  
  - **Runtime:** `;` (sequential)  
  - **Justification:** Collection must complete before delivery can begin.

- **G2 → G2.1, G2.2, G2.3, G2.4**  
  - **Relation:** AND  
  - **Runtime:** `#` (parallel)  
  - **Justification:** Multiple robots can perform collection steps in parallel; sub‑tasks are prerequisites for the next step.

- **G3 → G3.1, G3.2**  
  - **Relation:** AND  
  - **Runtime:** `#` (parallel)  
  - **Justification:** Multiple robots can deliver concurrently; sub‑tasks must all be achieved.

- **G2.4 → AT1, AT2**  
  - **Relation:** AND (but governed by fallback at goal level)  
  - **Runtime:** `FALLBACK(AT1, AT2)`  
  - **Justification:** If battery <10 %, first attempt to recharge; if recharging fails, delegate to another robot.

- **G3.2 → G3.2.1, G3.2.2**  
  - **Relation:** AND (but governed by fallback)  
  - **Runtime:** `FALLBACK(G3.2.1, G3.2.2)`  
  - **Justification:** If battery <30 %, try to return resource; if return fails, alert and report.

- **G3.2.1 → AT3, AT4**  
  - **Relation:** AND  
  - **Runtime:** `AND(AT3, AT4)`  
  - **Justification:** Both returning the resource and delegating the remaining task must succeed.

- **G3.2.2 → AT5, AT6**  
  - **Relation:** AND  
  - **Runtime:** `AND(AT5, AT6)`  
  - **Justification:** Both alerting and reporting are required in failure.

- **AT1 → AT2** (within G2.4)  
  - **Relation:** AND (implicit)  
  - **Justification:** Delegation occurs after recharge or as a fallback.

- **AT3 → AT4** (within G3.2.1)  
  - **Relation:** AND (implicit)  
  - **Justification:** Delegation only after resource is safely at the checkpoint.

- **AT5 → AT6** (within G3.2.2)  
  - **Relation:** AND (implicit)  
  - **Justification:** Alert must be raised before reporting.

---

This goal model captures all mission requirements, explicitly encodes the sequential and parallel execution patterns, and defines precise fallback behaviour for battery‑related failures. Each goal and task is justified with reference to the mission description, ensuring traceability and clarity for implementation in a multi‑robot system.
