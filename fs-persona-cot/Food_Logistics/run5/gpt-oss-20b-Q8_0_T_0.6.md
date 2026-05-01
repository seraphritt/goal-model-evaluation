**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

Below is the full goal model, expressed as a tree of goals and tasks.  
Each node contains the required annotations, a short justification, and the
runtime execution structure (parallel “#”, sequential “;”, or fallback
`FALLBACK(exp1,exp2)`).

---

## 1. Goal Table

| Name                                              | Text                                                                                          | Runtime                                                | Goal Type | Enquired Information / Target Condition | Relation                 | Justification                                                                    | Ground truth I                                       | Ground truth C | Consensus                                            |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------- | --------------------------------------- | ------------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------------- | -------------- | ---------------------------------------------------- |
| **G1: Deliver food to inpatient rooms**           | Deliver food from the kitchen to an inpatient room in response to a kitchen delivery request. | `;`                                                    | Perform   | –                                       | AND (to G2-G6)           | All steps must be carried out one after another to satisfy the delivery request. | OK                                                   | Ok             | OK                                                   |
| **G2: Obtain food from kitchen**                  | Pick up meals from the kitchen.                                                               | `-`                                                    | Perform   | –                                       | –                        | This is a concrete action that must be performed.                                | OK                                                   | Ok             | OK                                                   |
| **G3: Transport food to room**                    | Transport the meals from the kitchen to the patient’s room.                                   | `-`                                                    | Perform   | –                                       | –                        | A necessary movement step.                                                       | OK                                                   | Ok             | OK                                                   |
| **G4: Deliver food to patient or table**          | Deliver food to the patient or to the room table, choosing the best strategy.                 | `FALLBACK(G4.1, FALLBACK(G4.2, FALLBACK(G4.3, G4.4)))` | Perform   | –                                       | OR (fallback chain)      | Multiple delivery strategies exist; if one fails we fall back to the next.       | Achieve. Target condition: all food was delivered    | Ok             | Achieve. Target condition: all food was delivered    |
| **G4.1: Deliver to table**                        | Place the meal on the patient’s room table.                                                   | `-`                                                    | Perform   | –                                       | –                        | Requires the robot’s manipulation skill.                                         | OK                                                   | Ok             | OK                                                   |
| **G4.2: Deliver to tray and patient fetch**       | Place the meal on the robot’s tray so that the patient can fetch it.                          | `AND`                                                  | Perform   | –                                       | AND (to G4.2.1 & G4.2.2) | Must first know if the patient can fetch before attempting this strategy.        | OK                                                   | Ok             | OK                                                   |
| **G4.2.1: Query patient fetch capability**        | Ask whether the patient can retrieve the meal from the tray.                                  | `-`                                                    | Query     | patient fetch capability                | –                        | The robot needs this information to decide on the strategy.                      | OK                                                   | Ok             | OK                                                   |
| **G4.2.2: Deliver to tray and patient fetch**     | Place the meal on the tray and let the patient fetch it.                                      | `AND`                                                  | Perform   | –                                       | AND (to AT4 & AT5)       | Both placing and patient retrieval must succeed.                                 | OK                                                   | Ok             | OK                                                   |
| **G4.3: Deliver to tray and companion fetch**     | Place the meal on the tray so that a companion can fetch it.                                  | `AND`                                                  | Perform   | –                                       | AND (to G4.3.1 & G4.3.2) | Must confirm companion availability first.                                       | OK                                                   | Ok             | OK                                                   |
| **G4.3.1: Query companion fetch capability**      | Ask whether a companion visitor can retrieve the meal from the tray.                          | `-`                                                    | Query     | companion fetch capability              | –                        | Needed to decide on this strategy.                                               | OK                                                   | Ok             | OK                                                   |
| **G4.3.2: Deliver to tray and companion fetch**   | Place the meal on the tray and let the companion fetch it.                                    | `AND`                                                  | Perform   | –                                       | AND (to AT4 & AT20)      | Both placing and companion retrieval must succeed.                               | OK                                                   | Ok             | OK                                                   |
| **G4.4: Deliver to tray and robot fetch**         | Place the meal on the tray so that another robot can fetch it.                                | `AND`                                                  | Perform   | –                                       | AND (to G4.4.1 & G4.4.2) | Must confirm that another robot can fetch before attempting.                     | OK                                                   | Ok             | OK                                                   |
| **G4.4.1: Query robot fetch capability**          | Ask whether another robot can fetch the meal from the tray.                                   | `-`                                                    | Query     | robot fetch capability                  | –                        | Needed to decide on this strategy.                                               | OK                                                   | Ok             | OK                                                   |
| **G4.4.2: Deliver to tray and robot fetch**       | Place the meal on the tray and let another robot fetch it.                                    | `AND`                                                  | Perform   | –                                       | AND (to AT4 & AT7)       | Both placing and robot retrieval must succeed.                                   | PL                                                   | Ok             | PL                                                   |
| **G5: Retrieve dirty dishes**                     | Pick up dirty dishes from the patient’s room.                                                 | `AND`                                                  | Perform   | –                                       | AND (to G5.1-G5.3)       | All sub-tasks must be completed to finish dish retrieval.                        | OK                                                   | Ok             | OK                                                   |
| **G5.1: Open room door**                          | Open the patient’s room door.                                                                 | `FALLBACK(G5.1.1, G5.1.2)`                             | Perform   | –                                       | OR (fallback)            | Door opening may require a human or the robot itself; fallback if one fails.     | OK                                                   | Ok             | OK                                                   |
| **G5.1.1: Open door with human**                  | Human opens the door while the robot assists.                                                 | `-`                                                    | Perform   | –                                       | –                        | Human assistance is often needed.                                                | OK                                                   | Ok             | OK                                                   |
| **G5.1.2: Open door with robot**                  | Robot opens the door by itself.                                                               | `-`                                                    | Perform   | –                                       | –                        | If the robot can handle the door, this is the preferred path.                    | OK                                                   | Ok             | OK                                                   |
| **G5.2: Collect dishes**                          | Pick up the dirty dishes.                                                                     | `FALLBACK(G5.2.1, FALLBACK(G5.2.2, G5.2.3))`           | Perform   | –                                       | OR (fallback)            | Dish collection may be unassisted, with human help, or with two robots.          | Achieve. Target condition: all dishes were collected | Ok             | Achieve. Target condition: all dishes were collected |
| **G5.2.1: Collect dishes unassisted**             | Robot collects dishes alone.                                                                  | `-`                                                    | Perform   | –                                       | –                        | Preferred if the robot can carry the load.                                       | OK                                                   | Ok             | OK                                                   |
| **G5.2.2: Collect dishes with human**             | Robot collects dishes with human help.                                                        | `-`                                                    | Perform   | –                                       | –                        | Human assistance may be needed for heavier loads.                                | OK                                                   | Ok             | OK                                                   |
| **G5.2.3: Collect dishes with two robots**        | Two robots cooperate to collect dishes.                                                       | `-`                                                    | Perform   | –                                       | –                        | Used when the load exceeds a single robot’s capacity.                            | OK                                                   | Ok             | OK                                                   |
| **G5.3: Return dishes to kitchen**                | Transport the collected dishes back to the kitchen.                                           | `-`                                                    | Perform   | –                                       | –                        | Final step of dish retrieval.                                                    | OK                                                   | Ok             | OK                                                   |
| **G6: Track meal retrieval and alert wrong meal** | Keep track of which meal was retrieved and alert if a wrong meal is taken.                    | `AND`                                                  | Perform   | –                                       | AND (to G6.1 & G6.2)     | Both tracking and alerting must happen.                                          | OK                                                   | Ok             | OK                                                   |
| **G6.1: Track meal retrieval**                    | Record the meal ID and location of retrieval.                                                 | `-`                                                    | Perform   | –                                       | –                        | Needed for accountability.                                                       | OK                                                   | Ok             | OK                                                   |
| **G6.2: Alert wrong meal**                        | Notify staff if a wrong meal was retrieved.                                                   | `-`                                                    | Perform   | –                                       | –                        | Safety / quality-control action.                                                 | OK                                                   | Ok             | OK                                                   |


---

## 2. Task Table

| Name | Text | Relation | Location | Number of Robots | Justification |
|------|------|----------|----------|------------------|---------------|
| **AT1: Pick up meals from kitchen** | Pick up meals from the kitchen. | AND (to G2) | kitchen | 1 | One robot is sufficient to pick up the meals. |
| **AT2: Transport meals to room** | Transport the meals to the patient’s room. | AND (to G3) | kitchen → room | 1 | A single robot can carry the meals. |
| **AT3: Place meal on table** | Place the meal on the patient’s room table. | AND (to G4.1) | room table | 1 | Requires the robot’s manipulation skill. |
| **AT4: Place meal on robot tray** | Place the meal on the robot’s tray. | AND (to G4.2.2, G4.3.2, G4.4.2) | robot tray | 1 | Robot places the meal on its own tray. |
| **AT5: Patient retrieves meal from tray** | Patient retrieves the meal from the tray. | AND (to G4.2.2) | room | 1 (patient) | Patient fetches the meal. |
| **AT6: Nurse retrieves meal from tray** | Nurse retrieves the meal from the tray. | AND (to G4.3.2) | room | 1 (nurse) | Nurse fetches the meal. |
| **AT7: Robot retrieves meal from tray** | Another robot retrieves the meal from the tray. | AND (to G4.4.2) | robot tray | 1 (other robot) | Robot fetches the meal cooperatively. |
| **AT8: Human opens door** | Human opens the room door while the robot assists. | AND (to G5.1.1) | room door | 1 (robot) | Human assistance is often required. |
| **AT9: Robot opens door** | Robot opens the room door by itself. | AND (to G5.1.2) | room door | 1 | Robot can open the door if it has the capability. |
| **AT10: Robot collects dishes** | Robot collects the dirty dishes alone. | AND (to G5.2.1) | room | 1 | Preferred if load is manageable. |
| **AT11: Robot collects dishes with human** | Robot collects dishes with human help. | AND (to G5.2.2) | room | 1 | Human assistance may be needed for heavier loads. |
| **AT12: Two robots collect dishes** | Two robots cooperate to collect dishes. | AND (to G5.2.3) | room | 2 | Used when the load exceeds one robot’s capacity. |
| **AT13: Robot transports dishes to kitchen** | Robot transports the collected dishes back to the kitchen. | AND (to G5.3) | room → kitchen | 1 | Single robot can carry the dishes. |
| **AT14: Robot scans meal ID** | Robot scans the meal ID to track retrieval. | AND (to G6.1) | room | 1 | Needed for accountability. |
| **AT15: Robot alerts staff** | Robot alerts staff if the wrong meal was retrieved. | AND (to G6.2) | room | 1 | Safety / quality‑control action. |
| **AT16: Query patient record for patient fetch capability** | Robot queries patient record for the patient’s ability to fetch. | AND (to G4.2.1) | server | 1 | Needed before deciding on patient fetch strategy. |
| **AT17: Query robot fetch capability** | Robot queries the system to confirm another robot can fetch. | AND (to G4.4.1) | server | 1 | Needed before deciding on robot fetch strategy. |
| **AT18: Query nurse availability** | Robot queries nurse availability. | AND (to G4.3.1) | server | 1 | Needed before deciding on nurse fetch strategy. |
| **AT19: Query companion availability** | Robot queries companion availability. | AND (to G4.3.1) | server | 1 | Needed before deciding on companion fetch strategy. |
| **AT20: Companion retrieves meal from tray** | Companion retrieves the meal from the tray. | AND (to G4.3.2) | room | 1 (companion) | Companion fetches the meal. |

---

## 3. Summary Table (Goals + Tasks)

| ID | Type | Text |
|----|------|------|
| **G1** | Goal | Deliver food to inpatient rooms |
| **G2** | Goal | Obtain food from kitchen |
| **AT1** | Task | Pick up meals from kitchen |
| **G3** | Goal | Transport food to room |
| **AT2** | Task | Transport meals to room |
| **G4** | Goal | Deliver food to patient or table |
| **G4.1** | Goal | Deliver to table |
| **AT3** | Task | Place meal on table |
| **G4.2** | Goal | Deliver to tray and patient fetch |
| **G4.2.1** | Goal | Query patient fetch capability |
| **AT16** | Task | Query patient record for patient fetch capability |
| **G4.2.2** | Goal | Deliver to tray and patient fetch |
| **AT4** | Task | Place meal on robot tray |
| **AT5** | Task | Patient retrieves meal from tray |
| **G4.3** | Goal | Deliver to tray and companion fetch |
| **G4.3.1** | Goal | Query companion fetch capability |
| **AT19** | Task | Query companion availability |
| **G4.3.2** | Goal | Deliver to tray and companion fetch |
| **AT4** | Task | Place meal on robot tray |
| **AT20** | Task | Companion retrieves meal from tray |
| **G4.4** | Goal | Deliver to tray and robot fetch |
| **G4.4.1** | Goal | Query robot fetch capability |
| **AT17** | Task | Query robot fetch capability |
| **G4.4.2** | Goal | Deliver to tray and robot fetch |
| **AT4** | Task | Place meal on robot tray |
| **AT7** | Task | Robot retrieves meal from tray |
| **G5** | Goal | Retrieve dirty dishes |
| **G5.1** | Goal | Open room door |
| **G5.1.1** | Goal | Open door with human |
| **AT8** | Task | Human opens door |
| **G5.1.2** | Goal | Open door with robot |
| **AT9** | Task | Robot opens door |
| **G5.2** | Goal | Collect dishes |
| **G5.2.1** | Goal | Collect dishes unassisted |
| **AT10** | Task | Robot collects dishes |
| **G5.2.2** | Goal | Collect dishes with human |
| **AT11** | Task | Robot collects dishes with human |
| **G5.2.3** | Goal | Collect dishes with two robots |
| **AT12** | Task | Two robots collect dishes |
| **G5.3** | Goal | Return dishes to kitchen |
| **AT13** | Task | Robot transports dishes to kitchen |
| **G6** | Goal | Track meal retrieval and alert wrong meal |
| **G6.1** | Goal | Track meal retrieval |
| **AT14** | Task | Robot scans meal ID |
| **G6.2** | Goal | Alert wrong meal |
| **AT15** | Task | Robot alerts staff |
| **G4.2.1** | Goal | Query patient fetch capability |
| **AT16** | Task | Query patient record for patient fetch capability |
| **G4.3.1** | Goal | Query companion fetch capability |
| **AT19** | Task | Query companion availability |
| **G4.4.1** | Goal | Query robot fetch capability |
| **AT17** | Task | Query robot fetch capability |
| **G4.3.1** | Goal | Query nurse availability |
| **AT18** | Task | Query nurse availability |

---

## 4. Logical Relationships (Tree Structure)

```
G1 -> G2, G3, G4, G5, G6 [AND; sequential]
  Justification: All steps (obtain, transport, deliver, retrieve dishes, track) must be performed one after another.

G4 -> G4.1, G4.2, G4.3, G4.4 [OR (fallback chain)]
  Justification: Multiple delivery strategies exist; if one fails we fall back to the next.

G4.2 -> G4.2.1, G4.2.2 [AND]
  Justification: Must know patient fetch capability before attempting to place on tray and let patient fetch.

G4.2.2 -> AT4, AT5 [AND]
  Justification: Both placing on tray and patient retrieval must succeed.

G4.3 -> G4.3.1, G4.3.2 [AND]
  Justification: Must confirm companion availability before placing on tray and letting companion fetch.

G4.3.2 -> AT4, AT20 [AND]
  Justification: Both placing on tray and companion retrieval must succeed.

G4.4 -> G4.4.1, G4.4.2 [AND]
  Justification: Must confirm another robot can fetch before attempting to place on tray and let robot fetch.

G4.4.2 -> AT4, AT7 [AND]
  Justification: Both placing on tray and robot retrieval must succeed.

G5 -> G5.1, G5.2, G5.3 [AND]
  Justification: Door opening, dish collection, and dish return are all required for dish retrieval.

G5.1 -> G5.1.1, G5.1.2 [OR (fallback)]
  Justification: Door may be opened by human or robot; fallback if one fails.

G5.2 -> G5.2.1, G5.2.2, G5.2.3 [OR (fallback)]
  Justification: Dish collection may be unassisted, with human help, or with two robots; fallback if one fails.

G6 -> G6.1, G6.2 [AND]
  Justification: Tracking and alerting must both occur.

```

---

### Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Fallback for delivery strategies** | The description lists several possible ways to deliver the meal. If the robot cannot manipulate to place on the table, or if the patient cannot fetch, the robot must try alternative strategies. |
| **Query goals before each strategy** | The availability of patient, companion, nurse, or another robot is uncertain. The robot must query the patient record or staff availability before committing to a strategy. |
| **Parallel execution where possible** | Door opening and dish collection can be performed in parallel if resources allow, but the model uses fallback to keep the tree simple. |
| **AND for tasks within a goal** | Each sub‑task must be completed for the parent goal to succeed (e.g., placing on tray and patient retrieval). |
| **Sequential root execution** | The overall mission is naturally sequential: obtain → transport → deliver → dish retrieval → tracking. |
| **Perform goals for all concrete actions** | All operational steps are modeled as Perform goals because they are executed actions. |
| **Query goals for information retrieval** | Goals that only retrieve information are classified as Query goals, with the enquired information listed. |
| **No Achieve goals** | The mission’s objectives are all action‑based; there is no higher‑level state‑change goal beyond “food delivered”. |

---

**End of Goal Model**
