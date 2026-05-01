**Goal Model – Multi‑Robot Resource Delivery**

| **Name** | **Text**                          | **Runtime**        | **Goal Type** | **Target / Enquired Info** | **Relation**        | **Justification**                                                                                                                                   | **Ground truth I**                                      | **Ground truth C** | **Consensus**                                           |
| -------- | --------------------------------- | ------------------ | ------------- | -------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------ | ------------------------------------------------------- |
| **G1**   | Execute Resource Delivery Mission | `;`                | Perform       | –                          | AND (G2, G3)        | The mission must first complete the collection phase before the delivery phase can start.                                                           | ok                                                      | Ok                 | ok                                                      |
| **G2**   | Collection Phase                  | `FALLBACK(G4, G5)` | Perform       | –                          | FALLBACK (G4, G5)   | Normal collection is attempted; if the robot’s battery falls below 10 % the mission must fall back to the low-battery handling branch.              | Achieve. Target condition: all resources were collected | Ok                 | Achieve. Target condition: all resources were collected |
| **G4**   | Normal Collection                 | `;`                | Perform       | –                          | AND (AT1, AT2, AT3) | All sub-tasks must be performed in order to successfully collect the resources.                                                                     | OK                                                      | Ok                 | OK                                                      |
| **G5**   | Battery Low in Collection         | `;`                | Perform       | –                          | AND (AT7, AT8)      | When the battery is low the robot must recharge and reassign the mission.                                                                           | OK                                                      | Ok                 | OK                                                      |
| **G3**   | Delivery Phase                    | `FALLBACK(G6, G7)` | Perform       | –                          | FALLBACK (G6, G7)   | Normal delivery is attempted; if the battery falls below 30 % the mission must fall back to the low-battery handling branch.                        | Achieve. Target condition: all resources were delivered | Ok                 | Achieve. Target condition: all resources were delivered |
| **G6**   | Normal Delivery                   | `;`                | Perform       | –                          | AND (AT4, AT5)      | All sub-tasks must be performed in order to deliver the resources.                                                                                  | OK                                                      | Ok                 | OK                                                      |
| **G7**   | Battery Low in Delivery           | `;`                | Perform       | –                          | AND (AT6, AT8, AT9) | When the battery is low the robot must return the resources to a checkpoint, reassign the task, and, if the return fails, alert the sector manager. | OK                                                      | Ok                 | OK                                                      |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Navigate to Storage | AND (G4) | Storage | 1 | The robot must physically reach the storage location to collect resources. |
| **AT2** | Send Resource Request | AND (G4) | Storage | 1 | The robot must request the required resources before they can be retrieved. |
| **AT3** | Wait for Retrieval | AND (G4) | Storage | 1 | The robot must wait until the storage system has supplied the resources. |
| **AT4** | Navigate to Destination | AND (G6) | Destination | 1 | The robot must travel to the delivery location. |
| **AT5** | Transport Resources | AND (G6) | Path (Storage → Destination) | 1 | The robot must carry the resources, possibly making multiple runs. |
| **AT6** | Return to Checkpoint | AND (G7) | Checkpoint | 1 | The robot must return the resources to a safe location when battery is low. |
| **AT7** | Recharge at Station | AND (G5) | Charging Station | 1 | The robot must recharge to continue the mission. |
| **AT8** | Reassign Mission | AND (G5, G7) | Current Location | 1 | The robot must hand over the remaining task to another robot when its battery is insufficient. |
| **AT9** | Send Alert to Sector Manager | AND (G7) | Command Center | 1 | If the robot cannot return the resources to a checkpoint, an alert must be sent. |

---

### Summary Table (Goals & Tasks)

| **ID** | **Type** | **Title** | **Runtime / Relation** |
|--------|----------|-----------|------------------------|
| G1 | Goal | Execute Resource Delivery Mission | `;` (AND to G2, G3) |
| G2 | Goal | Collection Phase | `FALLBACK(G4,G5)` |
| G4 | Goal | Normal Collection | `;` (AND to AT1, AT2, AT3) |
| G5 | Goal | Battery Low in Collection | `;` (AND to AT7, AT8) |
| G3 | Goal | Delivery Phase | `FALLBACK(G6,G7)` |
| G6 | Goal | Normal Delivery | `;` (AND to AT4, AT5) |
| G7 | Goal | Battery Low in Delivery | `;` (AND to AT6, AT8, AT9) |
| AT1 | Task | Navigate to Storage | AND (G4) |
| AT2 | Task | Send Resource Request | AND (G4) |
| AT3 | Task | Wait for Retrieval | AND (G4) |
| AT4 | Task | Navigate to Destination | AND (G6) |
| AT5 | Task | Transport Resources | AND (G6) |
| AT6 | Task | Return to Checkpoint | AND (G7) |
| AT7 | Task | Recharge at Station | AND (G5) |
| AT8 | Task | Reassign Mission | AND (G5, G7) |
| AT9 | Task | Send Alert to Sector Manager | AND (G7) |

---

### Logical Relationships (with Justification)

1. **G1 → G2, G3**  
   *Relation:* **AND** with **sequential** execution (`;`).  
   *Justification:* The mission must first collect resources before any delivery can occur.

2. **G2 → G4, G5**  
   *Relation:* **FALLBACK(G4, G5)**.  
   *Justification:* Normal collection is attempted; if the robot’s battery falls below 10 %, the mission falls back to the low‑battery handling branch.

3. **G4 → AT1, AT2, AT3**  
   *Relation:* **AND** with **sequential** execution (`;`).  
   *Justification:* The robot must navigate to storage, request resources, and wait for retrieval in that order.

4. **G5 → AT7, AT8**  
   *Relation:* **AND** with **sequential** execution (`;`).  
   *Justification:* When low on battery, the robot first recharges, then reassigns the remaining task.

5. **G3 → G6, G7**  
   *Relation:* **FALLBACK(G6, G7)**.  
   *Justification:* Normal delivery is attempted; if the battery falls below 30 %, the mission falls back to the low‑battery handling branch.

6. **G6 → AT4, AT5**  
   *Relation:* **AND** with **sequential** execution (`;`).  
   *Justification:* The robot must navigate to the destination and then transport the resources.

7. **G7 → AT6, AT8, AT9**  
   *Relation:* **AND** with **sequential** execution (`;`).  
   *Justification:* When low on battery during delivery, the robot must return the resources to a checkpoint, reassign the remaining task, and if the return fails, send an alert.

---

**Key Design Choices**

* **Sequential vs. Parallel** – Collection and delivery are strictly sequential at the mission level; within each phase the sub‑tasks are performed sequentially.  
* **Fallback** – Battery‑related contingencies are modeled as fallback branches, ensuring that the mission can recover from low‑battery events by reassigning tasks.  
* **Parallel Execution** – The top‑level mission could be run in parallel by multiple robots, but the goal model preserves the logical dependencies and recovery behavior.  
* **Task Granularity** – Tasks are kept at the lowest actionable level (movement, messaging, recharging) so that robots can be directly assigned to them.  

This goal model fully captures the mission requirements, provides a clear operational structure for the multi‑robot system, and offers justifications for every decomposition and relation.
