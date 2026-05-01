# Goal & Task Model for Multi‑Robot Resource Delivery Mission  

Below is a complete goal‑model decomposition (tree structure) and the corresponding task list for the described multi‑robot system.  
All IDs are generated in a depth‑first traversal order, as required.

---

## 1. Goal Table  

| **Name**                                            | **Text**                                                                                | **Runtime**      | **Goal Type** | **Target Condition / Enquired Info** | **Relation** | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                       |
| --------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------- | ------------- | ------------------------------------ | ------------ | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1 – Deliver Requested Resources to Destination** | Deliver the requested resources from storage to the destination requested by the agent. | `;` (sequential) | Perform       | –                                    | Root         | Ok                                                       | OK                 | Ok                                                       |
| **G2 – Collect Resources from Storage**             | Collect the required resources from the designated storage locations.                   | `;` (sequential) | Perform       | –                                    | AND          | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G4 – Plan Route to Storage**                      | Determine optimal route to storage considering waiting time and path.                   | `-` (leaf)       | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G5 – Request Resource**                           | Send message to storage specifying required resources.                                  | `-`              | Perform       | –                                    | AND          | Query. Enqueried information: Resources to be collected  | OK                 | Query. Enqueried information: Resources to be collected  |
| **G6 – Wait for Retrieval**                         | Wait until resources are retrieved from storage.                                        | `-`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G7 – Handle Low Battery in Collection**           | Manage low battery during collection phase (10 % threshold).                            | `;`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G8 – Return to Recharge Station**                 | Navigate to recharge station to recharge battery.                                       | `-`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G9 – Assign Mission to Another Robot**            | Assign remaining collection mission to another robot.                                   | `-`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G3 – Deliver Resources to Destination**           | Deliver collected resources to the specified location.                                  | `;`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G10 – Handle Low Battery in Delivery**            | Manage low battery during delivery phase (30 % threshold).                              | `;`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G13 – Return Resource to Checkpoint**             | Return resource to checkpoint if battery low during delivery.                           | `-`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G14 – Assign Remaining Task to Another Robot**    | Assign remaining delivery task to another robot.                                        | `-`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G15 – Deliver Resource**                          | Deliver the resource to the destination location.                                       | `-`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G16 – Trigger Alert on Failure**                  | Trigger alert if resource cannot be returned to checkpoint.                             | `-`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |
| **G17 – Send Report to Sector Manager**             | Send report to sector manager after alert.                                              | `-`              | Perform       | –                                    | AND          | OK                                                       | OK                 | OK                                                       |


---

## 2. Task Table  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1 – Navigate to Storage** | Robot navigates to the storage location to collect resources. | AND | *storage* | 1 |
| **AT2 – Send Request Message** | Robot sends request message to storage with resource specifications. | AND | *storage* | 1 |
| **AT3 – Wait for Retrieval** | Robot waits until resources are retrieved from storage. | AND | *storage* | 1 |
| **AT4 – Navigate to Delivery Location** | Robot navigates to destination to deliver resource. | AND | *destination* | 1 |
| **AT5 – Deliver Resource** | Robot delivers the resource at destination. | AND | *destination* | 1 |
| **AT6 – Navigate to Recharge Station** | Robot navigates to recharge station to recharge battery. | AND | *recharge station* | 1 |
| **AT7 – Assign Mission to Another Robot** | Robot assigns remaining mission to another robot. | AND | *central* | 1 |
| **AT8 – Return Resource to Checkpoint** | Robot returns resource to checkpoint during low battery. | AND | *checkpoint* | 1 |
| **AT9 – Trigger Alert** | Robot triggers alert to sector manager. | AND | *sector manager* | 1 |
| **AT10 – Send Report** | Robot sends report to sector manager. | AND | *sector manager* | 1 |
| **AT11 – Assign Parallel Robots** | Robot assigns parallel robots for multiple‑item collection. | AND | *central* | [1,5] |

---

## 3. Summary Table (Goals + Tasks)  

| **ID** | **Type** | **Title** | **Text** | **Runtime / Relation** | **Location** | **Robots** |
|--------|----------|-----------|----------|------------------------|--------------|------------|
| G1 | Goal | Deliver Requested Resources to Destination | Deliver the requested resources from storage to the destination requested by the agent. | `;` (sequential) | – | – |
| G2 | Goal | Collect Resources from Storage | Collect the required resources from the designated storage locations. | `;` | – | – |
| G4 | Goal | Plan Route to Storage | Determine optimal route to storage considering waiting time and path. | `-` | – | – |
| AT1 | Task | Navigate to Storage | Robot navigates to the storage location to collect resources. | AND | *storage* | 1 |
| G5 | Goal | Request Resource | Send message to storage specifying required resources. | `-` | – | – |
| AT2 | Task | Send Request Message | Robot sends request message to storage with resource specifications. | AND | *storage* | 1 |
| G6 | Goal | Wait for Retrieval | Wait until resources are retrieved from storage. | `-` | – | – |
| AT3 | Task | Wait for Retrieval | Robot waits until resources are retrieved from storage. | AND | *storage* | 1 |
| G7 | Goal | Handle Low Battery in Collection | Manage low battery during collection phase (10 % threshold). | `;` | – | – |
| G8 | Goal | Return to Recharge Station | Navigate to recharge station to recharge battery. | `-` | – | – |
| AT6 | Task | Navigate to Recharge Station | Robot navigates to recharge station to recharge battery. | AND | *recharge station* | 1 |
| G9 | Goal | Assign Mission to Another Robot | Assign remaining collection mission to another robot. | `-` | – | – |
| AT7 | Task | Assign Mission to Another Robot | Robot assigns remaining mission to another robot. | AND | *central* | 1 |
| G3 | Goal | Deliver Resources to Destination | Deliver collected resources to the specified location. | `;` | – | – |
| G10 | Goal | Handle Low Battery in Delivery | Manage low battery during delivery phase (30 % threshold). | `;` | – | – |
| G13 | Goal | Return Resource to Checkpoint | Return resource to checkpoint if battery low during delivery. | `-` | – | – |
| AT8 | Task | Return Resource to Checkpoint | Robot returns resource to checkpoint during low battery. | AND | *checkpoint* | 1 |
| G14 | Goal | Assign Remaining Task to Another Robot | Assign remaining delivery task to another robot. | `-` | – | – |
| AT7 | Task | Assign Mission to Another Robot | Robot assigns remaining mission to another robot. | AND | *central* | 1 |
| G15 | Goal | Deliver Resource | Deliver the resource to the destination location. | `-` | – | – |
| AT4 | Task | Navigate to Delivery Location | Robot navigates to destination to deliver resource. | AND | *destination* | 1 |
| AT5 | Task | Deliver Resource | Robot delivers the resource at destination. | AND | *destination* | 1 |
| G16 | Goal | Trigger Alert on Failure | Trigger alert if resource cannot be returned to checkpoint. | `-` | – | – |
| AT9 | Task | Trigger Alert | Robot triggers alert to sector manager. | AND | *sector manager* | 1 |
| G17 | Goal | Send Report to Sector Manager | Send report to sector manager after alert. | `-` | – | – |
| AT10 | Task | Send Report | Robot sends report to sector manager. | AND | *sector manager* | 1 |
| AT11 | Task | Assign Parallel Robots | Robot assigns parallel robots for multiple‑item collection. | AND | *central* | [1,5] |

---

## 4. Logical Relationships (Tree Structure)

```
G1 -> G2, G3 [AND][;]

G2 -> G4, G5, G6, G7 [AND][;]
G4 -> AT1 [AND][-]
G5 -> AT2 [AND][-]
G6 -> AT3 [AND][-]
G7 -> G8, G9 [AND][;]
G8 -> AT6 [AND][-]
G9 -> AT7 [AND][-]

G3 -> G10, G15 [AND][;]
G10 -> G13, G14 [AND][;]
G13 -> AT8 [AND][-]
G14 -> AT7 [AND][-]
G15 -> AT4, AT5 [AND][;]

G16 -> AT9 [AND][-]
G17 -> AT10 [AND][-]

AT11 is not attached to a parent goal in this simplified model but represents the optional parallel‑robot assignment for multiple items.
```

---

### Notes

* **Runtime annotations**  
  * `;` – sequential execution of the child goals/tasks.  
  * `#` – parallel execution (used only in the main goal G1 if parallel collection/delivery were required).  
  * `-` – leaf goal/task (no children).  
  * `FALLBACK(exp1,exp2)` – not used in this simplified model but can be inserted where fallback behavior is required (e.g., if returning to checkpoint fails).

* **Goal Types** – All goals in this mission are **Perform** goals because they describe concrete actions that robots must execute. No **Query** or **Achieve** goals are needed.

* **Task Assignment** – Each task is assigned to a single robot (`Number of Robots: 1`) except for AT11 which allows a variable number of robots `[1,5]` to handle parallel collection when multiple items are requested.

* **Battery Management** – Low‑battery handling is split into two separate goals (G7 for collection, G10 for delivery) to keep the model modular and to enable independent monitoring of battery thresholds (10 % and 30 %).

* **Alert & Reporting** – G16 and G17 handle failure notification and reporting to the sector manager.  

Feel free to adapt the model (e.g., add fallback operators or merge tasks) to fit more detailed operational constraints.
