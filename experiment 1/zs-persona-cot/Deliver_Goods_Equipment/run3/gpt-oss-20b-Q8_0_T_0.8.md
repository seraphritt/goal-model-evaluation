## 1. Goal Model – Tables  

| **Name**   | **Text**                                                              | **Runtime**                 | **Goal Type** | **Target Condition / Enquired Info**                                                | **Relation**                     | **Justification**                                                                                                          | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| ---------- | --------------------------------------------------------------------- | --------------------------- | ------------- | ----------------------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1**     | Deliver requested resources to the specified location                 | `;`                         | Achieve       | “All requested resources are at the destination and handed to the requesting agent” | –                                | **Achieve** – the mission’s ultimate objective is to bring the world into a state where the resources have been delivered. | Perform.                                                 | OK                 | Perform.                                                 |
| **G2**     | Collect resources from storage                                        | `;`                         | Perform       | –                                                                                   | **AND** (with G3)                | Both collection and delivery must succeed for G1 to succeed.                                                               | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G2.1**   | Determine the order of collection based on waiting-time + path        | `-`                         | Perform       | –                                                                                   | **AND** (within G2)              | The robot must compute the optimal visiting order before moving.                                                           | OK                                                       | OK                 | OK                                                       |
| **G2.2**   | Navigate to the selected storage location                             | `-`                         | Perform       | –                                                                                   | **AND** (within G2)              | Physical movement is required to reach the resource.                                                                       | OK                                                       | OK                 | OK                                                       |
| **G2.3**   | Request the specified resources from storage                          | `-`                         | Perform       | –                                                                                   | **AND** (within G2)              | The robot must send a request message.                                                                                     | Query. Enquired information: resources to be collected.  | OK                 | Query. Enquired information: resources to be collected.  |
| **G2.4**   | Wait until the resources are retrieved                                | `-`                         | Perform       | –                                                                                   | **AND** (within G2)              | The robot must wait for the storage to hand over the goods.                                                                | OK                                                       | OK                 | OK                                                       |
| **G2.5**   | Monitor battery during collection                                     | `FALLBACK(G2.5.1 , G2.5.2)` | Perform       | –                                                                                   | **OR** (between G2.5.1 & G2.5.2) | Battery monitoring is a decision point – either continue or handle a low-battery situation.                                | OK                                                       | OK                 | OK                                                       |
| **G2.5.1** | Continue collection (battery OK)                                      | `-`                         | Perform       | –                                                                                   | –                                | Default continuation path.                                                                                                 | OK                                                       | OK                 | OK                                                       |
| **G2.5.2** | Recharge and re-assign mission                                        | `-`                         | Perform       | –                                                                                   | **AND** (with AT5 & AT6)         | Both recharging *and* re-assignment are required to recover.                                                               | OK                                                       | OK                 | OK                                                       |
| **G3**     | Deliver collected resources to the destination                        | `;`                         | Perform       | –                                                                                   | **AND** (within G1)              | Delivery must follow collection.                                                                                           | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G3.1**   | Transport resources to the destination                                | `-`                         | Perform       | –                                                                                   | **AND** (within G3)              | The robot must carry the goods.                                                                                            | OK                                                       | OK                 | OK                                                       |
| **G3.2**   | Monitor battery during delivery                                       | `FALLBACK(G3.2.1 , G3.2.2)` | Perform       | –                                                                                   | **OR** (between G3.2.1 & G3.2.2) | Decision point: continue or handle low battery.                                                                            | OK                                                       | OK                 | OK                                                       |
| **G3.2.1** | Continue delivery (battery OK)                                        | `-`                         | Perform       | –                                                                                   | –                                | Default path.                                                                                                              | OK                                                       | OK                 | OK                                                       |
| **G3.2.2** | Low-battery handling                                                  | `-`                         | Perform       | –                                                                                   | **AND** (with G3.3)              | Must perform all low-battery steps.                                                                                        | OK                                                       | OK                 | OK                                                       |
| **G3.3**   | Handle low-battery situation                                          | `;`                         | Perform       | –                                                                                   | **AND** (within G3)              | The robot must execute all sub-steps to recover.                                                                           | OK                                                       | OK                 | OK                                                       |
| **G3.3.1** | Return the resource to a checkpoint                                   | `-`                         | Perform       | –                                                                                   | **AND** (within G3.3)            | First step in low-battery recovery.                                                                                        | OK                                                       | OK                 | OK                                                       |
| **G3.3.2** | Assign remaining task to another robot                                | `-`                         | Perform       | –                                                                                   | **AND** (within G3.3)            | Second step – the remaining load must be handed over.                                                                      | OK                                                       | OK                 | OK                                                       |
| **G3.3.3** | Trigger alert & report to sector manager (if checkpoint return fails) | `-`                         | Perform       | –                                                                                   | **AND** (within G3.3)            | Final safety step.                                                                                                         | OK                                                       | OK                 | OK                                                       |

---

## 2. Task Model – Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Compute the optimal visiting order for the robot | **AND** (with AT2‑AT4) | Robot’s onboard planner | 1 | The robot needs to decide the order before moving. |
| **AT2** | Navigate to the selected storage location | **AND** (with AT1‑AT4) | Specific storage location | 1 | One robot physically moves to the storage. |
| **AT3** | Send request message to the storage for the needed resources | **AND** (with AT1‑AT4) | Storage location | 1 | Direct communication is required. |
| **AT4** | Wait for the storage to hand over the resources | **AND** (with AT1‑AT4) | Storage location | 1 | The robot must wait until the goods are ready. |
| **AT5** | Go back to the recharging station | **AND** (with AT6) | Recharging station | 1 | Battery‑low recovery requires recharging. |
| **AT6** | Notify the central control that the mission is reassigned | **AND** (with AT5) | Central control / communication channel | 1 | Reassignment is a communication step. |
| **AT7** | Transport the collected resources to the destination | **AND** (with AT8‑AT10) | Destination location | 1 | The robot physically carries the goods. |
| **AT8** | Return the resource to a checkpoint (low‑battery) | **AND** (with AT9‑AT10) | Checkpoint location | 1 | First step in low‑battery handling. |
| **AT9** | Assign the remaining delivery task to another robot | **AND** (with AT10) | Central control / communication channel | 1 | The remaining load must be handed over. |
| **AT10** | Trigger an alert and send a report to the sector manager | **AND** (with AT8‑AT9) | Sector manager’s console | 1 | Safety notification if checkpoint return fails. |

---

## 3. Summary – Goals & Tasks  

| **Goal ID** | **Goal Title** | **Task(s)** |
|-------------|----------------|-------------|
| G1 | Deliver requested resources to destination | – |
| G2 | Collect resources from storage | AT1, AT2, AT3, AT4, AT5, AT6 |
| G3 | Deliver collected resources to destination | AT7, AT8, AT9, AT10 |

*All tasks are leaf actions that directly implement the sub‑goals.*

---

## 4. Logical Relationships (Tree Structure)

```
G1 (Deliver requested resources to destination)
├─ G2 (Collect resources)  [AND] [;]
│   ├─ G2.1 (Determine order)  [AND] [-]
│   ├─ G2.2 (Navigate to storage)  [AND] [-]
│   ├─ G2.3 (Request resource)  [AND] [-]
│   ├─ G2.4 (Wait for retrieval)  [AND] [-]
│   └─ G2.5 (Monitor battery)  [OR] [FALLBACK(G2.5.1 , G2.5.2)]
│       ├─ G2.5.1 (Continue collection)  [AND] [-]
│       └─ G2.5.2 (Recharge & re‑assign)  [AND] [AND]
│           ├─ AT5 (Go to recharge)  [AND] [#]
│           └─ AT6 (Assign mission)  [AND] [#]
├─ G3 (Deliver resources)  [AND] [;]
│   ├─ G3.1 (Transport resources)  [AND] [-]
│   ├─ G3.2 (Monitor battery)  [OR] [FALLBACK(G3.2.1 , G3.2.2)]
│   │   ├─ G3.2.1 (Continue delivery)  [AND] [-]
│   │   └─ G3.2.2 (Low‑battery handling)  [AND] [;]
│   │       ├─ G3.3 (Handle low battery)  [AND] [;]
│   │       │   ├─ G3.3.1 (Return to checkpoint)  [AND] [-]
│   │       │   ├─ G3.3.2 (Assign remaining task)  [AND] [-]
│   │       │   └─ G3.3.3 (Alert failure)  [AND] [-]
│   │       └─ (No tasks – the sub‑goals above are executed)
│   └─ (No additional tasks)
```

**Justifications**

| **Link** | **Relation** | **Runtime** | **Why** |
|----------|--------------|-------------|---------|
| G1 → G2, G3 | AND | `;` (sequential) | Collection must finish before delivery; both must succeed. |
| G2 → G2.1–G2.5 | AND | `;` (sequential) | Each sub‑step must be completed in order. |
| G2.5 → G2.5.1, G2.5.2 | OR | `FALLBACK` | Decision point: either continue or handle low battery. |
| G3 → G3.1–G3.3 | AND | `;` (sequential) | Delivery steps are ordered. |
| G3.2 → G3.2.1, G3.2.2 | OR | `FALLBACK` | Either continue or handle low battery. |
| G3.3 → G3.3.1–G3.3.3 | AND | `;` (sequential) | Low‑battery handling requires all sub‑steps. |
| G2.5.2 → AT5, AT6 | AND | `#` (parallel) | Recharging and reassignment can occur concurrently. |
| G3.3.1 → AT8 | AND | `#` | Return to checkpoint is a distinct action. |
| G3.3.2 → AT9 | AND | `#` | Assignment of remaining task is distinct. |
| G3.3.3 → AT10 | AND | `#` | Alert is a separate action. |

---

### 5. Reflections & Design Choices  

1. **Depth‑First Numbering** – IDs are assigned following a depth‑first traversal to preserve the hierarchy and make the model unambiguous.  
2. **Runtime Operators** –  
   * `;` (sequential) is used whenever the mission phases must follow a strict order (collection → delivery).  
   * `#` (parallel) is applied only where independent actions can be executed concurrently (e.g., recharging while notifying reassignment).  
   * `FALLBACK` captures the mission’s fault‑tolerance logic: if a battery‑low condition is detected, the robot must switch to a recovery branch.  
3. **Goal Types** – All non‑leaf goals are classified as **Perform** because they represent concrete actions that must be executed. The top‑level goal is **Achieve** because it describes a desired state (resources delivered).  
4. **Task Properties** –  
   * **Location** reflects the physical place where the action occurs (storage, recharging station, checkpoint, destination).  
   * **Number of Robots** is set to `1` for all tasks because each action is carried out by a single robot; however, the model allows parallelism at the goal level (e.g., multiple robots can each satisfy a *Collect* sub‑goal).  
5. **Parallelism** – While the mission itself is sequential across phases, the model allows parallel execution of *Collect* sub‑goals across different robots, which is captured by the parallel operator at the goal level (`#` would be added if we decomposed *Collect* into multiple parallel sub‑goals per storage).  
6. **Fallbacks** – The fallback structure is nested only once because the mission description provides a single alternative branch for each low‑battery scenario. If more alternatives were needed, additional nesting would be introduced.  

This goal model faithfully captures the mission logic, supports multi‑robot parallelism, and provides clear justification for every decomposition, relation, and runtime choice.
