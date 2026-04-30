**Goal Model – Multi‑Robot Food Delivery**

| **Name**                                       | **Text**                                                                                                             | **Runtime**                | **Goal Type** | **Target Condition / Enquired Information**                        | **Relation** | **Ground truth I**                                    | **Ground truth C** | **Consensus**                                         |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------- | ------------------------------------------------------------------ | ------------ | ----------------------------------------------------- | ------------------ | ----------------------------------------------------- |
| **G1: Deliver Food to Inpatient Room**         | Achieve that food is delivered to the inpatient room and the patient receives the correct meal, with dishes cleaned. | `;` (sequential)           | Achieve       | *Food delivered to room, patient has correct meal, dishes cleaned* | **Root**     | Perform                                               | Perform            | Perform                                               |
| **G2: Receive Delivery Request**               | Perform the reception of an order from the kitchen.                                                                  | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G3: Prepare Delivery**                       | Perform the picking-up and loading of meals onto the robot.                                                          | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G4: Deliver Food**                           | Deliver the food to the patient – either directly to the table or to the robot’s tray.                               | `FALLBACK(G4.1,G4.2)`      | Perform       | –                                                                  | OR           | Achieve. target condition: all food was delivered.    | OK                 | Achieve. target condition: all food was delivered.    |
| **G4.1: Deliver to Table**                     | Perform direct delivery of the meal onto the patient’s table.                                                        | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G4.2: Deliver to Tray**                      | Deliver the meal to the robot’s tray for patient retrieval.                                                          | `;` (sequential)           | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G4.2.1: Query Patient Retrieval Capability** | Query the patient record to determine if the patient can retrieve the meal from the tray.                            | `-`                        | Query         | *Whether patient can retrieve meal from tray*                      | AND          | OK                                                    | OK                 | OK                                                    |
| **G4.2.2: Notify Patient**                     | Inform the patient which meal to retrieve.                                                                           | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G4.2.3: Wait for Retrieval**                 | Wait for the patient to retrieve the meal.                                                                           | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G4.2.4: Track Retrieval**                    | Track which meal was retrieved and update the status.                                                                | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G4.2.5: Alert Wrong Meal**                   | Alert if the patient retrieves the wrong meal.                                                                       | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G4.2.6: Retrieve Dish**                      | Retrieve dirty dishes from the room.                                                                                 | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G5: Retrieve Dishes**                        | Retrieve dirty dishes – can be unassisted, with two robots, or with a human.                                         | `FALLBACK(G5.1,G5.2,G5.3)` | Perform       | –                                                                  | OR           | Achieve. Target condition: all dishes were retrieved. | OK                 | Achieve. Target condition: all dishes were retrieved. |
| **G5.1: Unassisted Retrieval**                 | Robot retrieves dishes alone.                                                                                        | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G5.2: Two Robots Retrieval**                 | Two robots cooperate to retrieve dishes.                                                                             | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G5.3: Human-Assisted Retrieval**             | Robot retrieves dishes with human assistance.                                                                        | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G6: Open Door**                              | Open the room door – can be robot-only, human-only, or robot-assisted.                                               | `FALLBACK(G6.1,G6.2,G6.3)` | Perform       | –                                                                  | OR           | OK                                                    | OK                 | OK                                                    |
| **G6.1: Robot Opens Door**                     | Robot opens the door alone.                                                                                          | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G6.2: Human Opens Door**                     | Human opens the door.                                                                                                | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |
| **G6.3: Robot with Human Opens Door**          | Robot assists a human in opening the door.                                                                           | `-`                        | Perform       | –                                                                  | AND          | OK                                                    | OK                 | OK                                                    |

---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1: Receive Delivery Request** | Robot receives an order from the kitchen. | AND | kitchen | 1 |
| **AT2: Prepare Delivery** | Robot picks up meals and loads them onto its tray. | AND | kitchen | 1 |
| **AT3: Deliver to Table** | Robot delivers the meal directly onto the patient’s table. | AND | inpatient room | 1 |
| **AT4: Deliver to Tray** | Robot delivers the meal to its tray for patient retrieval. | AND | inpatient room | 1 |
| **AT5: Query Patient Retrieval Capability** | Retrieve patient record to determine if the patient can retrieve the meal. | AND | offline (hospital information system) | 0 |
| **AT6: Notify Patient** | Robot informs the patient which meal to retrieve. | AND | inpatient room | 1 |
| **AT7: Wait for Retrieval** | Robot waits until the patient retrieves the meal. | AND | inpatient room | 1 |
| **AT8: Track Retrieval** | Robot tracks which meal was retrieved and updates the status. | AND | inpatient room | 1 |
| **AT9: Alert Wrong Meal** | Robot alerts if the patient retrieves the wrong meal. | AND | robot (internal) | 1 |
| **AT10: Retrieve Dish (Unassisted)** | Robot retrieves dirty dishes from the room. | AND | inpatient room | 1 |
| **AT11: Open Door (Robot)** | Robot opens the room door. | AND | room door | 1 |
| **AT12: Wait for Human to Open Door** | Robot waits for a human to open the door. | AND | room door | 0 |
| **AT13: Robot‑Assisted Door Opening** | Robot assists a human in opening the door. | AND | room door | 1 |
| **AT14: Retrieve Dish (Two Robots)** | Two robots cooperate to retrieve dishes. | AND | inpatient room | 2 |
| **AT15: Retrieve Dish (Human‑Assisted)** | Robot retrieves dishes with human assistance. | AND | inpatient room | 1 |

---

### Logical Relationships (Tree)

```
G1 -> G2, G3, G4, G5, G6 [AND][;]
G2 -> AT1 [AND]
G3 -> AT2 [AND]
G4 -> G4.1, G4.2 [OR][FALLBACK(G4.1,G4.2)]
G4.1 -> AT3 [AND]
G4.2 -> G4.2.1, G4.2.2, G4.2.3, G4.2.4, G4.2.5, G4.2.6 [AND][;]
G4.2.1 -> AT5 [AND]
G4.2.2 -> AT6 [AND]
G4.2.3 -> AT7 [AND]
G4.2.4 -> AT8 [AND]
G4.2.5 -> AT9 [AND]
G4.2.6 -> AT10 [AND]
G5 -> G5.1, G5.2, G5.3 [OR][FALLBACK(G5.1,G5.2,G5.3)]
G5.1 -> AT10 [AND]
G5.2 -> AT14 [AND]
G5.3 -> AT15 [AND]
G6 -> G6.1, G6.2, G6.3 [OR][FALLBACK(G6.1,G6.2,G6.3)]
G6.1 -> AT11 [AND]
G6.2 -> AT12 [AND]
G6.3 -> AT13 [AND]
```

This goal‑task decomposition captures the full mission of the multi‑robot system, including decision points for patient retrieval capability, dish handling, and door opening, while clearly specifying the execution order, parallelism, and fallback alternatives.
