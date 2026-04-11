## 1. Goal Model – Tables  

| **Name**                                                 | **Text**                                                                                 | **Runtime**                         | **Goal Type** | **Target Condition / Enquired Info**                                                        | **Relation**                | **Justification**                                                                       | **Ground truth I** | **Ground truth C** | **Ground truth E** |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------- | ------------- | ------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------- | ------------------ | ------------------ | ------------------ |
| **G1 – Deliver resources to requested location**         | Achieve the delivery of requested resources to the specified location.                   | `;` (sequential)                    | Achieve       | *Resources are delivered to the specified location and the requesting agent receives them.* | AND (with G2, G3)           | Collection must finish before delivery starts; both phases must succeed.                |                    |                    |                    |
| **G2 – Collection phase**                                | Perform the collection of required resources from storage.                               | `FALLBACK(G2_normal,G2_batteryLow)` | Perform       | –                                                                                           | AND (with G1)               | Normal collection is the primary plan; a fallback is needed for low-battery situations. |                    |                    |                    |
| **G2_normal – Normal collection**                        | Collect resources from storage under normal battery conditions.                          | `#` (parallel)                      | Perform       | –                                                                                           | AND (with G2.1-G2.4)        | Multiple storages can be visited concurrently to reduce mission time.                   |                    |                    |                    |
| **G2.1 – Navigate to storage**                           | Navigate to the storage location where the resource is located.                          | `-`                                 | Perform       | –                                                                                           | AND (with G2_normal)        | Required before any request can be sent.                                                |                    |                    |                    |
| **G2.2 – Request resource**                              | Send a message to the storage specifying the required resources and wait for a response. | `-`                                 | Perform       | –                                                                                           | AND (with G2_normal)        | Communication step that triggers the retrieval.                                         |                    |                    |                    |
| **G2.3 – Wait for retrieval**                            | Wait until the resources have been retrieved from the storage.                           | `-`                                 | Perform       | –                                                                                           | AND (with G2_normal)        | Synchronization point before pickup.                                                    |                    |                    |                    |
| **G2.4 – Pick up resource**                              | Pick up the retrieved resources.                                                         | `-`                                 | Perform       | –                                                                                           | AND (with G2_normal)        | Physical act of securing the goods.                                                     |                    |                    |                    |
| **G2_batteryLow – Handle low battery during collection** | Handle situation when battery <10 % during collection.                                   | `;` (sequential)                    | Perform       | –                                                                                           | AND (with G2.5, G2.6)       | Robot must first recharge and then hand over the task.                                  |                    |                    |                    |
| **G2.5 – Return to recharging station**                  | Navigate back to the recharging station to recharge.                                     | `-`                                 | Perform       | –                                                                                           | AND (with G2_batteryLow)    | Recharging is mandatory before any further action.                                      |                    |                    |                    |
| **G2.6 – Assign mission to another robot**               | Assign the remaining collection task to another robot.                                   | `-`                                 | Perform       | –                                                                                           | AND (with G2_batteryLow)    | Continuation of the mission by a fresh robot.                                           |                    |                    |                    |
| **G3 – Delivery phase**                                  | Perform delivery of collected resources to requested location.                           | `FALLBACK(G3_normal,G3_batteryLow)` | Perform       | –                                                                                           | AND (with G1)               | Primary delivery; fallback for low-battery situations.                                  |                    |                    |                    |
| **G3_normal – Normal delivery**                          | Deliver resources under normal battery conditions.                                       | `#` (parallel)                      | Perform       | –                                                                                           | AND (with G3.1, G3.2)       | Multiple deliveries can run concurrently.                                               |                    |                    |                    |
| **G3.1 – Navigate to delivery location**                 | Navigate to the specified delivery location.                                             | `-`                                 | Perform       | –                                                                                           | AND (with G3_normal)        | Must reach destination before handing over goods.                                       |                    |                    |                    |
| **G3.2 – Deliver resource**                              | Deliver the resource to the requesting agent at the location.                            | `-`                                 | Perform       | –                                                                                           | AND (with G3_normal)        | Core act that satisfies the mission.                                                    |                    |                    |                    |
| **G3_batteryLow – Handle low battery during delivery**   | Handle situation when battery <30 % during delivery.                                     | `;` (sequential)                    | Perform       | –                                                                                           | AND (with G3.4, G3.5, G3.6) | Must return the resource, hand over the task, and alert if failure.                     |                    |                    |                    |
| **G3.4 – Return resource to checkpoint**                 | Return the resource to a checkpoint.                                                     | `-`                                 | Perform       | –                                                                                           | AND (with G3_batteryLow)    | Preserves the resource for hand-over.                                                   |                    |                    |                    |
| **G3.5 – Assign remaining task to another robot**        | Assign remaining delivery task to another robot.                                         | `-`                                 | Perform       | –                                                                                           | AND (with G3_batteryLow)    | Continuation of the delivery by a fresh robot.                                          |                    |                    |                    |
| **G3.6 – Trigger alert if cannot return to checkpoint**  | Trigger an alert and send report to the sector manager.                                  | `-`                                 | Perform       | –                                                                                           | AND (with G3_batteryLow)    | Failure handling that informs human operators.                                          |                    |                    |                    |


---

## 2. Task Model – Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1 – Navigate to storage** | Navigate to storage location. | AND (with G2.1) | `StorageLocation` | 1 | One robot is needed to reach the storage. |
| **AT2 – Send request to storage** | Send request message to storage. | AND (with G2.2) | `StorageLocation` | 1 | Only the robot that arrived can request. |
| **AT3 – Wait for resource retrieval** | Wait until resource retrieved. | AND (with G2.3) | `StorageLocation` | 1 | The same robot must wait for the storage to deliver. |
| **AT4 – Pick up resource** | Pick up the retrieved resource. | AND (with G2.4) | `StorageLocation` | 1 | Physical act performed by the robot. |
| **AT5 – Navigate to recharging station** | Navigate back to the recharging station. | AND (with G2.5) | `RechargingStation` | 1 | Robot must go to the station to recharge. |
| **AT6 – Assign mission to another robot** | Assign mission to another robot. | AND (with G2.6) | `RechargingStation` | 1 | The robot that recharges hands over the task. |
| **AT7 – Navigate to delivery location** | Navigate to delivery location. | AND (with G3.1) | `DeliveryLocation` | 1 | Robot must reach the delivery point. |
| **AT8 – Deliver resource** | Deliver resource to requesting agent. | AND (with G3.2) | `DeliveryLocation` | 1 | Core delivery action. |
| **AT9 – Return to checkpoint** | Return resource to checkpoint. | AND (with G3.4) | `Checkpoint` | 1 | Needed when battery is low during delivery. |
| **AT10 – Assign remaining task to another robot** | Assign remaining delivery task to another robot. | AND (with G3.5) | `Checkpoint` | 1 | Hand‑over after returning to checkpoint. |
| **AT11 – Trigger alert** | Trigger alert and send report to sector manager. | AND (with G3.6) | `Checkpoint` | 1 | Failure handling action. |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Title** | **Type** | **Runtime** | **Key Relation** | **Justification** |
|--------|-----------|----------|-------------|------------------|-------------------|
| **G1** | Deliver resources to requested location | Achieve | `;` | AND (G2, G3) | Collection precedes delivery; both must succeed. |
| **G2** | Collection phase | Perform | `FALLBACK(G2_normal,G2_batteryLow)` | AND (G1) | Normal collection primary; fallback for low battery. |
| **G2_normal** | Normal collection | Perform | `#` | AND (G2.1‑G2.4) | Parallel visits to multiple storages. |
| **G2.1** | Navigate to storage | Perform | `-` | AND (G2_normal) | Needed before request. |
| **G2.2** | Request resource | Perform | `-` | AND (G2_normal) | Communication step. |
| **G2.3** | Wait for retrieval | Perform | `-` | AND (G2_normal) | Synchronization. |
| **G2.4** | Pick up resource | Perform | `-` | AND (G2_normal) | Physical act. |
| **G2_batteryLow** | Handle low battery during collection | Perform | `;` | AND (G2.5, G2.6) | Recharge then hand‑over. |
| **G2.5** | Return to recharging station | Perform | `-` | AND (G2_batteryLow) | Recharge mandatory. |
| **G2.6** | Assign mission to another robot | Perform | `-` | AND (G2_batteryLow) | Continue mission. |
| **G3** | Delivery phase | Perform | `FALLBACK(G3_normal,G3_batteryLow)` | AND (G1) | Primary delivery; fallback for low battery. |
| **G3_normal** | Normal delivery | Perform | `#` | AND (G3.1, G3.2) | Parallel deliveries possible. |
| **G3.1** | Navigate to delivery location | Perform | `-` | AND (G3_normal) | Reach destination. |
| **G3.2** | Deliver resource | Perform | `-` | AND (G3_normal) | Core action. |
| **G3_batteryLow** | Handle low battery during delivery | Perform | `;` | AND (G3.4, G3.5, G3.6) | Return, hand‑over, alert. |
| **G3.4** | Return resource to checkpoint | Perform | `-` | AND (G3_batteryLow) | Preserve resource. |
| **G3.5** | Assign remaining task to another robot | Perform | `-` | AND (G3_batteryLow) | Continue delivery. |
| **G3.6** | Trigger alert if cannot return to checkpoint | Perform | `-` | AND (G3_batteryLow) | Failure handling. |
| **AT1** | Navigate to storage | Task | – | AND (G2.1) | One robot reaches storage. |
| **AT2** | Send request to storage | Task | – | AND (G2.2) | Only the arrived robot can request. |
| **AT3** | Wait for resource retrieval | Task | – | AND (G2.3) | Same robot waits. |
| **AT4** | Pick up resource | Task | – | AND (G2.4) | Physical act. |
| **AT5** | Navigate to recharging station | Task | – | AND (G2.5) | Recharge location. |
| **AT6** | Assign mission to another robot | Task | – | AND (G2.6) | Hand‑over. |
| **AT7** | Navigate to delivery location | Task | – | AND (G3.1) | Reach delivery point. |
| **AT8** | Deliver resource | Task | – | AND (G3.2) | Core delivery. |
| **AT9** | Return to checkpoint | Task | – | AND (G3.4) | Low‑battery return. |
| **AT10** | Assign remaining task to another robot | Task | – | AND (G3.5) | Hand‑over at checkpoint. |
| **AT11** | Trigger alert | Task | – | AND (G3.6) | Failure alert. |

---

## 4. Logical Relationships – Decomposition Diagram (Textual)

```
G1 -> G2, G3 [AND][;]
   Justification: Collection must finish before delivery; both phases are required.

G2 -> G2_normal, G2_batteryLow [AND][FALLBACK(G2_normal,G2_batteryLow)]
   Justification: Normal collection is primary; fallback handles low battery.

G2_normal -> G2.1, G2.2, G2.3, G2.4 [AND][#]
   Justification: Multiple storage visits can be parallel; each step must be done.

G2.1 -> AT1 [AND]
   Justification: Navigation task is the concrete action.

G2.2 -> AT2 [AND]
G2.3 -> AT3 [AND]
G2.4 -> AT4 [AND]

G2_batteryLow -> G2.5, G2.6 [AND][;]
   Justification: Recharge first, then hand over.

G2.5 -> AT5 [AND]
G2.6 -> AT6 [AND]

G3 -> G3_normal, G3_batteryLow [AND][FALLBACK(G3_normal,G3_batteryLow)]
   Justification: Primary delivery; fallback for low battery.

G3_normal -> G3.1, G3.2 [AND][#]
   Justification: Parallel deliveries possible.

G3.1 -> AT7 [AND]
G3.2 -> AT8 [AND]

G3_batteryLow -> G3.4, G3.5, G3.6 [AND][;]
   Justification: Return resource, hand over, alert in sequence.

G3.4 -> AT9 [AND]
G3.5 -> AT10 [AND]
G3.6 -> AT11 [AND]
```

---

### Why the chosen operators?

| **Operator** | **When Used** | **Mission‑Driven Justification** |
|--------------|----------------|---------------------------------|
| `;` (sequential) | When one sub‑goal must finish before the next can start (e.g., G1 → G2 → G3, or battery‑handling steps). | The mission demands strict ordering: you cannot deliver before collecting, and you cannot hand over a task before recharging. |
| `#` (parallel) | When multiple independent sub‑tasks can be executed concurrently (e.g., visiting several storages or making several deliveries). | The description explicitly states that multiple robots can run in parallel to reduce total mission time. |
| `FALLBACK(exp1,exp2)` | When there is a primary plan and a backup plan that is only used if the primary fails (e.g., low battery). | The mission requires a fallback when battery drops below thresholds; the robot must switch to an alternative plan. |

---

### Goal Types – Rationale

| **Goal** | **Type** | **Why** |
|----------|----------|---------|
| G1 | Achieve | The mission’s ultimate objective is to bring resources to a location. |
| G2, G3, G2_normal, G3_normal, G2_batteryLow, G3_batteryLow | Perform | These are actions that must be executed; success depends on performing the actions. |
| None of the goals are Query or Achieve (other than G1) because the mission does not ask for information or state a target other than the final delivery. |

---

### Task Details – Why Locations & Robot Count

- **Location** is specified using meaningful variables (`StorageLocation`, `DeliveryLocation`, `RechargingStation`, `Checkpoint`) so that planners can bind them to real coordinates or zones.
- **Number of Robots** is set to `1` for all tasks because each task involves a single robot acting on a specific resource or location. Parallelism is achieved at the goal level (e.g., multiple `G2_normal` sub‑tasks can be instantiated for different storages, each with its own robot). If a mission requires many robots, the system can instantiate multiple instances of the same task with a robot range `[1,N]`.  

---

### Final Remarks

The goal model captures the hierarchical structure of the mission, the necessary sequencing, parallelism, and fallback handling required by the description. Each goal is annotated with a runtime operator that reflects the mission’s constraints, and each task is linked to its parent goal with a clear relation. The tables and decomposition diagram together provide a complete, justifiable blueprint that a multi‑robot system designer can use to generate plans, allocate robots, and monitor execution.
