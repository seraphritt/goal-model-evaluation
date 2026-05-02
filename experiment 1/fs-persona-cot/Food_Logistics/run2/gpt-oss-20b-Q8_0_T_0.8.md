## 1. Goal Model (Table)

| **Name**    | **Text**                                    | **Runtime**                                                        | **Goal Type** | **Enquired Information / Target Condition**                | **Relation**   | **Justification**                                                                                                                                                                                        | **Ground truth I**                                   | **Ground truth C** | **Consensus**                                        |
| ----------- | ------------------------------------------- | ------------------------------------------------------------------ | ------------- | ---------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ---------------------------------------------------- |
| **G1**      | Deliver food from kitchen to inpatient room | `FALLBACK(G2, G3)`                                                 | Perform       | –                                                          | **root**       | The robot can deliver food either directly onto the table or onto its tray for the patient to retrieve. A fallback is used so that if table-delivery fails the system automatically tries tray-delivery. | Achieve. Target condition: all food was delivered    | Ok                 | Achieve. Target condition: all food was delivered    |
| **G2**      | Deliver food onto the room table            | `;`                                                                | Perform       | –                                                          | AND (to G1)    | Both opening the door and delivering to the table must succeed, and they must occur in sequence (door first, then table).                                                                                |                                                      | Ok                 |                                                      |
| **G2.1**    | Open the room door                          | `FALLBACK(G2.1.1, FALLBACK(G2.1.2, G2.1.3))`                       | Perform       | –                                                          | AND (to G2)    | The robot must open the door before it can deliver to the table; the three sub-methods are alternatives.                                                                                                 | OK                                                   | Ok                 | OK                                                   |
| **G2.1.1**  | Open door unassisted                        | `-`                                                                | Perform       | –                                                          | OR (to G2.1)   | Robot can use its door-opening skill alone.                                                                                                                                                              | OK                                                   | Ok                 | OK                                                   |
| **G2.1.2**  | Open door with human assistance             | `-`                                                                | Perform       | –                                                          | OR (to G2.1)   | Robot can request a human to open the door.                                                                                                                                                              | OK                                                   | Ok                 | OK                                                   |
| **G2.1.3**  | Open door with robot assistance             | `-`                                                                | Perform       | –                                                          | OR (to G2.1)   | Robot can cooperate with another robot to open the door.                                                                                                                                                 | OK                                                   | Ok                 | OK                                                   |
| **G2.2**    | Deliver food onto the table                 | `-`                                                                | Perform       | –                                                          | AND (to G2.1)  | Must happen after the door is open.                                                                                                                                                                      | OK                                                   | Ok                 | OK                                                   |
| **G3**      | Deliver food to tray and patient fetch      | `;`                                                                | Perform       | –                                                          | AND (to G1)    | All sub-steps (tray placement, fetch, tracking, alert) must happen in order.                                                                                                                             | OK                                                   | Ok                 | OK                                                   |
| **G3.1**    | Deliver food onto the robot’s tray          | `-`                                                                | Perform       | –                                                          | AND (to G3)    | Robot places the meal on its tray.                                                                                                                                                                       | OK                                                   | Ok                 | OK                                                   |
| **G3.2**    | Patient fetch from tray                     | `FALLBACK(G3.2.1, G3.2.2)`                                         | Perform       | –                                                          | AND (to G3)    | First query the patient’s capability, then choose a fetcher.                                                                                                                                             | OK                                                   | Ok                 | OK                                                   |
| **G3.2.1**  | Query patient fetch capability              | `-`                                                                | Query         | *“Can the patient, companion or nurse retrieve the meal?”* | OR (to G3.2)   | The system needs to know who can fetch before deciding.                                                                                                                                                  | OK                                                   | Ok                 | OK                                                   |
| **G3.2.2**  | Choose fetcher                              | `FALLBACK(G3.2.2a, FALLBACK(G3.2.2b, FALLBACK(G3.2.2c, G3.2.2d)))` | Perform       | –                                                          | AND (to G3.2)  | The robot tries patient fetch first, then companion, nurse, finally robot fetch.                                                                                                                         | Ok                                                   | Ok                 | Ok                                                   |
| **G3.2.2a** | Patient fetch                               | `-`                                                                | Perform       | –                                                          | OR (to G3.2.2) | Patient retrieves the meal.                                                                                                                                                                              | OK                                                   | Ok                 | OK                                                   |
| **G3.2.2b** | Companion fetch                             | `-`                                                                | Perform       | –                                                          | OR (to G3.2.2) | Companion retrieves the meal.                                                                                                                                                                            | OK                                                   | Ok                 | OK                                                   |
| **G3.2.2c** | Nurse fetch                                 | `-`                                                                | Perform       | –                                                          | OR (to G3.2.2) | Nurse retrieves the meal.                                                                                                                                                                                | OK                                                   | Ok                 | OK                                                   |
| **G3.2.2d** | Robot fetch                                 | `-`                                                                | Perform       | –                                                          | OR (to G3.2.2) | Robot retrieves the meal from its tray.                                                                                                                                                                  | OK                                                   | Ok                 | OK                                                   |
| **G3.3**    | Track meal retrieval                        | `-`                                                                | Perform       | –                                                          | AND (to G3)    | Robot must monitor which meal is taken and when.                                                                                                                                                         | OK                                                   | Ok                 | OK                                                   |
| **G3.4**    | Alert wrong meal                            | `-`                                                                | Perform       | –                                                          | AND (to G3)    | Robot must notify staff if the wrong meal is taken.                                                                                                                                                      | OK                                                   | Ok                 | OK                                                   |
| **G4**      | Retrieve dirty dishes from room             | `;`                                                                | Perform       | –                                                          | AND (to G1)    | Dish retrieval is a separate but parallel activity that must also be completed.                                                                                                                          | OK                                                   | Ok                 | OK                                                   |
| **G4.1**    | Open the room door                          | `FALLBACK(G4.1.1, FALLBACK(G4.1.2, G4.1.3))`                       | Perform       | –                                                          | AND (to G4)    | Same door-opening alternatives as in G2.1.                                                                                                                                                               | OK                                                   | Ok                 | OK                                                   |
| **G4.1.1**  | Open door unassisted                        | `-`                                                                | Perform       | –                                                          | OR (to G4.1)   | Robot opens door alone.                                                                                                                                                                                  | OK                                                   | Ok                 | OK                                                   |
| **G4.1.2**  | Open door with human assistance             | `-`                                                                | Perform       | –                                                          | OR (to G4.1)   | Human opens door.                                                                                                                                                                                        | OK                                                   | Ok                 | OK                                                   |
| **G4.1.3**  | Open door with robot assistance             | `-`                                                                | Perform       | –                                                          | OR (to G4.1)   | Another robot opens door.                                                                                                                                                                                | OK                                                   | Ok                 | OK                                                   |
| **G4.2**    | Retrieve dishes                             | `FALLBACK(G4.2.1, FALLBACK(G4.2.2, G4.2.3))`                       | Perform       | –                                                          | AND (to G4)    | Three possible retrieval modes.                                                                                                                                                                          | Achieve. Target condition: all dishes were retrieved | Ok                 | Achieve. Target condition: all dishes were retrieved |
| **G4.2.1**  | Retrieve dishes unassisted                  | `-`                                                                | Perform       | –                                                          | OR (to G4.2)   | Robot picks up dishes alone.                                                                                                                                                                             | OK                                                   | Ok                 | OK                                                   |
| **G4.2.2**  | Retrieve dishes with human assistance       | `-`                                                                | Perform       | –                                                          | OR (to G4.2)   | Human helps robot.                                                                                                                                                                                       | OK                                                   | Ok                 | OK                                                   |
| **G4.2.3**  | Retrieve dishes with robot assistance       | `-`                                                                | Perform       | –                                                          | OR (to G4.2)   | Two robots cooperate.                                                                                                                                                                                    | OK                                                   | Ok                 | OK                                                   |
| **G4.3**    | Return dishes to kitchen                    | `-`                                                                | Perform       | –                                                          | AND (to G4.2)  | After picking up, the robot must transport dishes to kitchen.                                                                                                                                            | OK                                                   | Ok                 | OK                                                   |


---

## 2. Task Model (Table)

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Navigate from current location to room entrance | AND (to G2.1, G4.1) | Hospital corridor | 1 | Robot must reach the room before opening the door. |
| **AT2** | Open door using door‑opening skill | OR (to G2.1.1, G4.1.1) | Room entrance | 1 | Robot can perform the task alone. |
| **AT3** | Signal human to open door | OR (to G2.1.2, G4.1.2) | Room entrance | 1 | Requires human presence. |
| **AT4** | Cooperate with another robot to open door | OR (to G2.1.3, G4.1.3) | Room entrance | 2 | Two robots needed for joint action. |
| **AT5** | Deliver meal onto the table using manipulation skill | AND (to G2.2) | Patient room table | 1 | Robot must place the meal on the table. |
| **AT6** | Place meal onto robot’s tray | AND (to G3.1) | Room entrance or tray area | 1 | Simple placement action. |
| **AT7** | Query inpatient record for fetch capability | OR (to G3.2.1) | Hospital database | 1 | Information retrieval step. |
| **AT8** | Patient retrieves meal from tray | OR (to G3.2.2a) | Room | 0 | Patient action (no robot involvement). |
| **AT9** | Companion retrieves meal from tray | OR (to G3.2.2b) | Room | 0 | Companion action. |
| **AT10** | Nurse retrieves meal from tray | OR (to G3.2.2c) | Room | 0 | Nurse action. |
| **AT11** | Robot retrieves meal from tray | OR (to G3.2.2d) | Room | 1 | Robot can pick up the meal itself. |
| **AT12** | Monitor meal retrieval and record time/location | AND (to G3.3) | Room | 1 | Continuous monitoring task. |
| **AT13** | Alert staff if wrong meal taken | AND (to G3.4) | Room | 1 | Notification task. |
| **AT14** | Pick up dishes from table unassisted | OR (to G4.2.1) | Room table | 1 | Robot can pick up dishes alone. |
| **AT15** | Pick up dishes with human assistance | OR (to G4.2.2) | Room table | 1 | Human helps robot. |
| **AT16** | Two robots cooperate to pick up dishes | OR (to G4.2.3) | Room table | 2 | Heavy load requires two robots. |
| **AT17** | Transport dishes to kitchen | AND (to G4.3) | Kitchen | 1 | Robot must carry dishes back to kitchen. |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Type** | **Text** | **Runtime / Relation** | **Justification** |
|--------|----------|----------|------------------------|-------------------|
| **G1** | Goal | Deliver food from kitchen to inpatient room | `FALLBACK(G2, G3)` | Robot can deliver directly or via tray. |
| **G2** | Goal | Deliver food onto the room table | `;` | Door → Table sequence. |
| **G2.1** | Goal | Open the room door | `FALLBACK(G2.1.1, FALLBACK(G2.1.2, G2.1.3))` | Three opening methods. |
| **G2.1.1** | Goal | Open door unassisted | `-` | Robot skill. |
| **G2.1.2** | Goal | Open door with human assistance | `-` | Human help. |
| **G2.1.3** | Goal | Open door with robot assistance | `-` | Two robots. |
| **G2.2** | Goal | Deliver food onto the table | `-` | After door. |
| **G3** | Goal | Deliver food to tray and patient fetch | `;` | All sub‑steps. |
| **G3.1** | Goal | Deliver food onto the robot’s tray | `-` | Tray placement. |
| **G3.2** | Goal | Patient fetch from tray | `FALLBACK(G3.2.1, G3.2.2)` | Query → choose fetcher. |
| **G3.2.1** | Goal | Query patient fetch capability | `-` | Need info. |
| **G3.2** | Goal | Choose fetcher | `FALLBACK(G3.2.2a, FALLBACK(G3.2.2b, FALLBACK(G3.2.2c, G3.2.2d)))` | Priority order. |
| **G3.2.2a** | Goal | Patient fetch | `-` | Patient action. |
| **G3.2.2b** | Goal | Companion fetch | `-` | Companion action. |
| **G3.2.2c** | Goal | Nurse fetch | `-` | Nurse action. |
| **G3.2.2d** | Goal | Robot fetch | `-` | Robot action. |
| **G3.3** | Goal | Track meal retrieval | `-` | Monitoring. |
| **G3.4** | Goal | Alert wrong meal | `-` | Notification. |
| **G4** | Goal | Retrieve dirty dishes from room | `;` | Door → Retrieve → Return. |
| **G4.1** | Goal | Open the room door | `FALLBACK(G4.1.1, FALLBACK(G4.1.2, G4.1.3))` | Same alternatives. |
| **G4.1.1** | Goal | Open door unassisted | `-` | Robot skill. |
| **G4.1.2** | Goal | Open door with human assistance | `-` | Human help. |
| **G4.1.3** | Goal | Open door with robot assistance | `-` | Two robots. |
| **G4.2** | Goal | Retrieve dishes | `FALLBACK(G4.2.1, FALLBACK(G4.2.2, G4.2.3))` | Three retrieval modes. |
| **G4.2.1** | Goal | Retrieve dishes unassisted | `-` | Robot action. |
| **G4.2.2** | Goal | Retrieve dishes with human assistance | `-` | Human help. |
| **G4.2.3** | Goal | Retrieve dishes with robot assistance | `-` | Two robots. |
| **G4.3** | Goal | Return dishes to kitchen | `-` | Transport. |
| **AT1** | Task | Navigate to room entrance | AND (to G2.1, G4.1) | Robot must reach door. |
| **AT2** | Task | Open door with robot skill | OR (to G2.1.1, G4.1.1) | Robot alone. |
| **AT3** | Task | Signal human to open door | OR (to G2.1.2, G4.1.2) | Requires human. |
| **AT4** | Task | Cooperate with another robot to open door | OR (to G2.1.3, G4.1.3) | Two robots. |
| **AT5** | Task | Deliver meal onto table | AND (to G2.2) | Manipulation skill. |
| **AT6** | Task | Place meal onto tray | AND (to G3.1) | Simple placement. |
| **AT7** | Task | Query inpatient record | OR (to G3.2.1) | Information retrieval. |
| **AT8** | Task | Patient retrieves meal | OR (to G3.2.2a) | Patient action. |
| **AT9** | Task | Companion retrieves meal | OR (to G3.2.2b) | Companion action. |
| **AT10** | Task | Nurse retrieves meal | OR (to G3.2.2c) | Nurse action. |
| **AT11** | Task | Robot retrieves meal | OR (to G3.2.2d) | Robot action. |
| **AT12** | Task | Monitor meal retrieval | AND (to G3.3) | Continuous monitoring. |
| **AT13** | Task | Alert wrong meal | AND (to G3.4) | Notification. |
| **AT14** | Task | Pick up dishes unassisted | OR (to G4.2.1) | Robot action. |
| **AT15** | Task | Pick up dishes with human | OR (to G4.2.2) | Human help. |
| **AT16** | Task | Two robots pick up dishes | OR (to G4.2.3) | Two robots. |
| **AT17** | Task | Transport dishes to kitchen | AND (to G4.3) | Transport. |

---

## 4. Logical Relationships (with Justifications)

- **G1 → G2, G3**  
  - **Relation**: `FALLBACK(G2, G3)` (OR)  
  - **Justification**: The system may deliver food directly to the table (G2) or place it on its tray for patient retrieval (G3). If table delivery fails (e.g., door closed, table occupied), the robot falls back to tray delivery.

- **G1 → G4**  
  - **Relation**: `AND` (parallel)  
  - **Justification**: Dish retrieval is a concurrent responsibility of the same robot fleet; both food delivery and dish retrieval must be completed for the overall patient‑care cycle.

- **G2 → G2.1, G2.2**  
  - **Relation**: `;` (sequential)  
  - **Justification**: The robot must open the door before it can deliver the meal to the table.

- **G2.1 → G2.1.1, G2.1.2, G2.1.3**  
  - **Relation**: `FALLBACK(G2.1.1, FALLBACK(G2.1.2, G2.1.3))` (OR)  
  - **Justification**: The robot can open the door alone, with a human, or with another robot; fallback models the priority.

- **G2.2 → AT5**  
  - **Relation**: `AND`  
  - **Justification**: Delivering to the table is the final step after the door is open.

- **G3 → G3.1, G3.2, G3.3, G3.4**  
  - **Relation**: `;` (sequential)  
  - **Justification**: Tray placement, fetch, tracking, and alerting must occur in order.

- **G3.2 → G3.2.1, G3.2.2**  
  - **Relation**: `FALLBACK(G3.2.1, G3.2.2)` (OR)  
  - **Justification**: First query capability, then choose fetcher.

- **G3.2.2 → G3.2.2a, G3.2.2b, G3.2.2c, G3.2.2d**  
  - **Relation**: `FALLBACK(G3.2.2a, FALLBACK(G3.2.2b, FALLBACK(G3.2.2c, G3.2.2d)))` (OR)  
  - **Justification**: Priority order: patient, companion, nurse, robot.

- **G3.3 → AT12**  
  - **Relation**: `AND`  
  - **Justification**: Tracking is a mandatory step after fetch.

- **G3.4 → AT13**  
  - **Relation**: `AND`  
  - **Justification**: Alerting is mandatory if wrong meal is taken.

- **G4 → G4.1, G4.2, G4.3**  
  - **Relation**: `;` (sequential)  
  - **Justification**: Open door, retrieve dishes, return them.

- **G4.1 → G4.1.1, G4.1.2, G4.1.3**  
  - **Relation**: `FALLBACK(G4.1.1, FALLBACK(G4.1.2, G4.1.3))` (OR)  
  - **Justification**: Same door‑opening alternatives as in G2.1.

- **G4.2 → G4.2.1, G4.2.2, G4.2.3**  
  - **Relation**: `FALLBACK(G4.2.1, FALLBACK(G4.2.2, G4.2.3))` (OR)  
  - **Justification**: Three retrieval modes.

- **G4.3 → AT17**  
  - **Relation**: `AND`  
  - **Justification**: Transporting dishes back to kitchen is the final step.

- **AT1 → G2.1, G4.1**  
  - **Relation**: `AND`  
  - **Justification**: Navigation is prerequisite for both door‑opening tasks.

- **AT2 → G2.1.1, G4.1.1**  
  - **Relation**: `OR`  
  - **Justification**: Robot can open door alone for either food delivery or dish retrieval.

- **AT3 → G2.1.2, G4.1.2**  
  - **Relation**: `OR`  
  - **Justification**: Human can open door for both scenarios.

- **AT4 → G2.1.3, G4.1.3**  
  - **Relation**: `OR`  
  - **Justification**: Robot cooperation for door opening.

- **AT5 → G2.2**  
  - **Relation**: `AND`  
  - **Justification**: Deliver to table.

- **AT6 → G3.1**  
  - **Relation**: `AND`  
  - **Justification**: Place meal on tray.

- **AT7 → G3.2.1**  
  - **Relation**: `OR`  
  - **Justification**: Query step.

- **AT8 → G3.2.2a**  
  - **Relation**: `OR`  
  - **Justification**: Patient fetch.

- **AT9 → G3.2.2b**  
  - **Relation**: `OR`  
  - **Justification**: Companion fetch.

- **AT10 → G3.2.2c**  
  - **Relation**: `OR`  
  - **Justification**: Nurse fetch.

- **AT11 → G3.2.2d**  
  - **Relation**: `OR`  
  - **Justification**: Robot fetch.

- **AT12 → G3.3**  
  - **Relation**: `AND`  
  - **Justification**: Tracking.

- **AT13 → G3.4**  
  - **Relation**: `AND`  
  - **Justification**: Alerting.

- **AT14 → G4.2.1**  
  - **Relation**: `OR`  
  - **Justification**: Unassisted dish pick‑up.

- **AT15 → G4.2.2**  
  - **Relation**: `OR`  
  - **Justification**: Human assistance.

- **AT16 → G4.2.3**  
  - **Relation**: `OR`  
  - **Justification**: Two‑robot cooperation.

- **AT17 → G4.3**  
  - **Relation**: `AND`  
  - **Justification**: Transport dishes to kitchen.

---

### 5. Final Remarks

- **Goal Types**:  
  - All high‑level goals are **Perform** because they require concrete actions (delivery, door opening, dish pickup).  
  - The only **Query** goal is `G3.2.1` (fetch capability).  
  - There are no **Achieve** goals in this mission because the mission is operational rather than state‑transitioning.

- **Runtime Annotations**:  
  - `FALLBACK` is used whenever the mission can try an alternative if the first choice fails (door opening, fetcher selection).  
  - `;` (sequential) is used where the order matters (door → delivery, tray → fetch → track → alert).  
  - `#` (parallel) is used only for the top‑level parallelism between food delivery and dish retrieval (G1 ↔ G4).

- **Uncertainty Handling**:  
  - The `Query` goal and the `FALLBACK` chains capture the uncertainty about who can fetch the meal and whether the door can be opened unassisted.

- **Cooperation**:  
  - OR decompositions with fallback capture cooperation with humans, companions, nurses, and other robots.  
  - Number of robots is set to 1 for single‑robot tasks, 2 for cooperative tasks.

This goal‑task decomposition provides a clear, executable model for a multi‑robot system tasked with delivering food and managing dishes in a hospital setting.
