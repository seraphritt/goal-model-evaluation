**Goal‑Model – Multi‑Robot Resource Delivery Mission**

| **Name**                                   | **Text**                                                                                | **Runtime**                    | **Goal Type** | **Target Condition / Enquired Info**                                     | **Relation** | **Justification**                                                                                    | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| ------------------------------------------ | --------------------------------------------------------------------------------------- | ------------------------------ | ------------- | ------------------------------------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1**: Fulfill Resource Delivery Mission  | Deliver the requested resources to the specified location.                              | `;`                            | Achieve       | “All requested resources have been delivered to the specified location.” | AND          | Collection must be finished before delivery; hence the two main sub-goals are executed sequentially. | Perform                                                  | Perform            | Perform                                                  |
| **G2**: Collect Resources                  | Gather the required resources from the designated storage locations.                    | `FALLBACK(G2.1, G2.3)`         | Perform       | –                                                                        | OR           | Normal collection (G2.1) vs low-battery contingency (G2.3). Only one branch has to succeed.          | Achieve. Target condition: all resources were collected. | Ok                 | Achieve. Target condition: all resources were collected. |
| **G2.1**: Plan & Request Resources         | Plan optimal route and request the resources from storage.                              | `;`                            | Perform       | –                                                                        | AND          | Planning must be finished before the request can be sent.                                            | OK                                                       | Ok                 | OK                                                       |
| **G2.1.1**: Plan Collection Route          | Compute optimal path and waiting times to the storage.                                  | `-`                            | Query         | “Optimal path and estimated waiting times.”                              | –            | The robot needs this information to decide where to go next.                                         | OK                                                       | Ok                 | OK                                                       |
| **G2.1.2**: Request Resources              | Send a request to the storage and wait until the resources are retrieved.               | `-`                            | Perform       | –                                                                        | –            | Direct action that must be executed after planning.                                                  | Query. Enqueried information: resources to be collected  | Ok                 | Query. Enqueried information: resources to be collected  |
| **G2.3**: Handle Low Battery in Collection | If battery <10 %, return to charging station and re-assign the mission.                 | `-`                            | Perform       | –                                                                        | –            | Low-battery contingency that must be handled immediately.                                            | OK                                                       | Ok                 | OK                                                       |
| **G3**: Deliver Resources                  | Transport the collected resources to the destination.                                   | `FALLBACK(G3.1, G3.2)`         | Perform       | –                                                                        | OR           | Normal delivery (G3.1) vs low-battery contingency (G3.2).                                            | Achieve. Target condition: all resources were delivered  | Ok                 | Achieve. Target condition: all resources were delivered  |
| **G3.1**: Deliver to Destination           | Move the resources to the specified location.                                           | `-`                            | Perform       | –                                                                        | –            | Core delivery action.                                                                                | OK                                                       | Ok                 | OK                                                       |
| **G3.2**: Handle Low Battery in Delivery   | If battery <30 %, return the resource to a checkpoint and re-assign the remaining task. | `;`                            | Perform       | –                                                                        | AND          | Both return and re-assignment must happen in sequence.                                               | OK                                                       | Ok                 | OK                                                       |
| **G3.2.1**: Return to Checkpoint           | Return the resource to a checkpoint for safety.                                         | `FALLBACK(G3.2.1.1, G3.2.1.2)` | Perform       | –                                                                        | OR           | First try to return; if that fails, trigger an alert.                                                | Ok                                                       | Ok                 | Ok                                                       |
| **G3.2.1.1**: Deliver to Checkpoint        | Move the resource to the checkpoint.                                                    | `-`                            | Perform       | –                                                                        | –            | Primary action.                                                                                      | OK                                                       | Ok                 | OK                                                       |
| **G3.2.1.2**: Alert Sector Manager         | Send an alert if return to checkpoint fails.                                            | `-`                            | Perform       | –                                                                        | –            | Fail-safe mechanism.                                                                                 | OK                                                       | Ok                 | OK                                                       |
| **G3.2.2**: Re-assign Remaining Task       | Assign the remaining delivery task to another robot.                                    | `-`                            | Perform       | –                                                                        | –            | Needed after low-battery to keep mission progressing.                                                | OK                                                       | Ok                 | OK                                                       |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1**: Plan Collection Route | Compute optimal path and waiting times to storage. | AND (with G2.1.1) | Robot’s planning module | 1 | Robot must calculate route before moving. |
| **AT2**: Evaluate Waiting Time & Path | Estimate waiting times at storage and path length. | AND (with G2.1.1) | Robot’s planning module | 1 | Needed for optimal route selection. |
| **AT3**: Wait for Resources | Wait until resources are retrieved from storage. | AND (with G2.1.2) | Storage | 1 | Robot must pause until retrieval is complete. |
| **AT4**: Send Request Message | Send precise resource request to storage. | AND (with G2.1.2) | Storage | 1 | Initiates the resource transfer. |
| **AT5**: Re‑assign Mission | Assign collection task to another robot. | AND (with G2.3) | Control center | 1 | Ensures continuity when battery is low. |
| **AT6**: Deliver Resources | Transport resources to the destination location. | AND (with G3.1) | Destination | 1 | Core delivery action. |
| **AT7**: Return Resource to Checkpoint | Place resource at checkpoint location. | AND (with G3.2.1.1) | Checkpoint | 1 | Safety action during low‑battery. |
| **AT8**: Re‑assign Remaining Task | Assign remaining delivery task to another robot. | AND (with G3.2.2) | Control center | 1 | Keeps delivery progressing after low‑battery. |
| **AT9**: Trigger Alert | Send alert if return to checkpoint fails. | AND (with G3.2.1.2) | Control center | 1 | Fail‑safe notification. |
| **AT10**: Move to Storage | Navigate robot to storage location. | AND (with G2.1.1) | Storage | 1 | Physical movement to storage. |
| **AT11**: Move to Destination | Navigate robot to destination. | AND (with G3.1) | Destination | 1 | Physical movement to delivery point. |
| **AT12**: Move to Checkpoint | Navigate robot to checkpoint. | AND (with G3.2.1.1) | Checkpoint | 1 | Physical movement to checkpoint. |
| **AT13**: Move to Charging Station | Navigate robot to charging station. | AND (with G2.3) | Charging station | 1 | Low‑battery contingency movement. |
| **AT14**: Send Request to Storage | Send resource request to storage. | AND (with G2.1.2) | Storage | 1 | Duplicate of AT4 (illustrative). |
| **AT15**: Receive Confirmation | Receive confirmation that resources are retrieved. | AND (with G2.1.2) | Storage | 1 | Confirms successful retrieval. |

---

### Summary Table (All Goals & Tasks)

| **Type** | **ID** | **Title** | **Runtime / Relation** | **Justification** |
|----------|--------|-----------|------------------------|-------------------|
| Goal | G1 | Fulfill Resource Delivery Mission | `;` (AND) | Sequential: must collect before deliver. |
| Goal | G2 | Collect Resources | `FALLBACK(G2.1,G2.3)` (OR) | Normal vs low‑battery. |
| Goal | G2.1 | Plan & Request Resources | `;` (AND) | Plan before request. |
| Goal | G2.1.1 | Plan Collection Route | `-` | Query for path info. |
| Goal | G2.1.2 | Request Resources | `-` | Direct action. |
| Goal | G2.3 | Handle Low Battery in Collection | `-` | Low‑battery contingency. |
| Goal | G3 | Deliver Resources | `FALLBACK(G3.1,G3.2)` (OR) | Normal vs low‑battery. |
| Goal | G3.1 | Deliver to Destination | `-` | Core delivery. |
| Goal | G3.2 | Handle Low Battery in Delivery | `;` (AND) | Return + re‑assign. |
| Goal | G3.2.1 | Return to Checkpoint | `FALLBACK(G3.2.1.1,G3.2.1.2)` (OR) | Return or alert. |
| Goal | G3.2.1.1 | Deliver to Checkpoint | `-` | Primary return. |
| Goal | G3.2.1.2 | Alert Sector Manager | `-` | Fail‑safe. |
| Goal | G3.2.2 | Re‑assign Remaining Task | `-` | Continuation after low‑battery. |
| Task | AT1 | Plan Collection Route | AND | Robot plans before moving. |
| Task | AT2 | Evaluate Waiting Time & Path | AND | Needed for optimal route. |
| Task | AT3 | Wait for Resources | AND | Must wait until retrieval. |
| Task | AT4 | Send Request Message | AND | Initiates transfer. |
| Task | AT5 | Re‑assign Mission | AND | Continuity after low battery. |
| Task | AT6 | Deliver Resources | AND | Core delivery action. |
| Task | AT7 | Return Resource to Checkpoint | AND | Safety during low battery. |
| Task | AT8 | Re‑assign Remaining Task | AND | Keeps mission going. |
| Task | AT9 | Trigger Alert | AND | Notify on failure. |
| Task | AT10 | Move to Storage | AND | Physical movement to storage. |
| Task | AT11 | Move to Destination | AND | Physical movement to destination. |
| Task | AT12 | Move to Checkpoint | AND | Physical movement to checkpoint. |
| Task | AT13 | Move to Charging Station | AND | Low‑battery contingency. |
| Task | AT14 | Send Request to Storage | AND | Duplicate of AT4. |
| Task | AT15 | Receive Confirmation | AND | Confirms retrieval. |

---

### Logical Relationships (Parent → Children)

| **Parent** | **Children** | **Relation / Runtime** | **Justification** |
|------------|--------------|------------------------|-------------------|
| **G1** → G2, G3 | `;` (AND) | Collection must finish before delivery. |
| **G2** → G2.1, G2.3 | OR (FALLBACK) | Normal collection vs low‑battery contingency. |
| **G2.1** → G2.1.1, G2.1.2 | AND (`;`) | Planning must precede requesting. |
| **G2.1.1** → AT1, AT2 | AND | Robot must compute route and evaluate waiting times. |
| **G2.1.2** → AT4, AT3, AT15 | AND | Robot sends request, waits, and confirms retrieval. |
| **G2.3** → AT13, AT5 | AND | Low‑battery robot returns to charge and re‑assigns. |
| **G3** → G3.1, G3.2 | OR (FALLBACK) | Normal delivery vs low‑battery contingency. |
| **G3.1** → AT6, AT11 | AND | Deliver resources and move to destination. |
| **G3.2** → G3.2.1, G3.2.2 | AND (`;`) | Return to checkpoint and re‑assign remaining task. |
| **G3.2.1** → G3.2.1.1, G3.2.1.2 | OR (FALLBACK) | Attempt to return; if fails, alert. |
| **G3.2.1.1** → AT12, AT7 | AND | Move to checkpoint and place resource. |
| **G3.2.1.2** → AT9 | AND | Trigger alert. |
| **G3.2.2** → AT8 | AND | Re‑assign remaining task. |

---

#### Key Justifications

* **Sequential (`;`)** – Used where a natural order of operations exists (planning before requesting, collection before delivery).
* **Parallel (`#`)** – Not explicitly used in this model because each robot handles one collection‑delivery cycle; parallelism is achieved by assigning *multiple* robots to different items, represented by independent branches (G2/G3) rather than simultaneous execution of sub‑tasks.
* **Fallback (`FALLBACK`)** – Captures low‑battery contingencies that must be handled if the primary branch fails. The OR relation reflects that only one branch needs to succeed.
* **AND** – Required when all sub‑goals or tasks must be achieved for the parent to succeed (e.g., moving to storage *and* waiting for resources).

This goal model captures the mission’s structure, contingencies, and parallelism while providing a clear mapping to actionable tasks for the multi‑robot system.
