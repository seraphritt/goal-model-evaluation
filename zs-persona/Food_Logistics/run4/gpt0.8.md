**Goal‑Model Summary**

| #   | **Goal ID & TITLE**                        | **Text**                                                                                         | **Runtime**                                    | **Goal Type** | **Target Condition / Enquired Information** | **Relation** | **Ground truth I**                                    | **Ground truth C** | **Ground truth E** |
| --- | ------------------------------------------ | ------------------------------------------------------------------------------------------------ | ---------------------------------------------- | ------------- | ------------------------------------------- | ------------ | ----------------------------------------------------- | ------------------ | ------------------ |
| 1   | **G1: Deliver Food to Inpatient Room**     | Deliver requested meals from the kitchen to the inpatient room in response to delivery requests. | `;` (sequential)                               | Perform       | Food is delivered to the inpatient room     | AND          | OK                                                    |  OK                  |                    |
| 2   | **G2: Obtain Food from Kitchen**           | Pick up the requested meals from the kitchen.                                                    | `;`                                            | Perform       | Meals are in robot’s tray                   | AND          | OK                                                    |  OK                  |                    |
| 3   | **G3: Transport Food to Room**             | Move the meals from the kitchen to the patient room.                                             | `;`                                            | Perform       | Meals are at patient-room location          | AND          | OK                                                    |  OK                  |                    |
| 4   | **G4: Deliver Food to Patient**            | Deliver the meals to the patient either onto the table or via the tray.                          | `FALLBACK(G4.1, G4.2)`                         | Perform       | Meals delivered to patient                  | OR           | Achieve. Target condition: all food was delivered.    |  OK                  |                    |
| 5   | **G4.1: Deliver to Table**                 | Place the meals onto the patient’s table.                                                        | `-`                                            | Perform       | Meals on table                              | AND          | OK                                                    |  OK                  |                    |
| 6   | **G4.2: Deliver to Tray**                  | Place the meals onto the patient’s tray for later retrieval.                                     | `;`                                            | Perform       | Meals on tray                               | AND          | OK                                                    |  OK                  |                    |
| 7   | **G4.2.1: Fetch from Tray**                | Fetch the meals from the robot’s tray.                                                           | `;`                                            | Perform       | Meals fetched from robot tray               | AND          | OK                                                    |  OK                  |                    |
| 8   | **G4.2.1.1: Query Patient Ability**        | Determine if patient can retrieve food from tray.                                                | `-`                                            | Query         | “Patient can retrieve food from tray?”      | AND          | OK                                                    |  OK                  |                    |
| 9   | **G4.2.1.2: Execute Fetch**                | Execute the fetch action using the appropriate method.                                           | `FALLBACK(G4.2.1.2.1, G4.2.1.2.2, G4.2.1.2.3)` | Perform       | Meals fetched                               | OR           | OK                                                    |  OK                  |                    |
| 10  | **G4.2.1.2.1: Patient Fetch**              | Patient fetches meals from robot tray.                                                           | `-`                                            | Perform       | Patient fetched meals                       | AND          | OK                                                    |  OK                  |                    |
| 11  | **G4.2.1.2.2: Nurse Fetch**                | Nurse fetches meals from robot tray.                                                             | `-`                                            | Perform       | Nurse fetched meals                         | AND          | OK                                                    |  OK                  |                    |
| 12  | **G4.2.1.2.3: Robot Fetch**                | Robot fetches meals from robot tray.                                                             | `-`                                            | Perform       | Robot fetched meals                         | AND          | OK                                                    |  OK                  |                    |
| 13  | **G4.2.2: Patient Retrieval**              | Patient retrieves the meal from the tray.                                                        | `-`                                            | Perform       | Patient retrieved meal                      | AND          | OK                                                    |  OK                  |                    |
| 14  | **G4.2.3: Alert Wrong Meal**               | Alert if a wrong meal is retrieved.                                                              | `-`                                            | Perform       | Wrong-meal alert issued                     | AND          | OK                                                    |  OK                  |                    |
| 15  | **G4.2.4: Track Meal Retrieval**           | Track when and where each meal was retrieved.                                                    | `-`                                            | Perform       | Meal retrieval logged                       | AND          | OK                                                    |  OK                  |                    |
| 16  | **G5: Retrieve Dishes**                    | Retrieve dirty dishes from the patient room.                                                     | `FALLBACK(G5.1, G5.2, G5.3)`                   | Perform       | Dishes retrieved                            | OR           | Achieve. Target condition: all dishes were retrieved. |  OK                  |                    |
| 17  | **G5.1: Unassisted Dish Retrieval**        | Robot retrieves dishes without assistance.                                                       | `-`                                            | Perform       | Dishes retrieved                            | AND          | OK                                                    |  OK                  |                    |
| 18  | **G5.2: Robot Cooperation Dish Retrieval** | Two robots cooperate to retrieve dishes.                                                         | `-`                                            | Perform       | Dishes retrieved                            | AND          | OK                                                    |  OK                  |                    |
| 19  | **G5.3: Human Cooperation Dish Retrieval** | Robot assists human to retrieve dishes.                                                          | `-`                                            | Perform       | Dishes retrieved                            | AND          | OK                                                    |  OK                  |                    |
| 20  | **G6: Open Room Door**                     | Open the patient room door to allow robot entry.                                                 | `FALLBACK(G6.1, G6.2)`                         | Perform       | Door opened                                 | OR           | OK                                                    |  OK                  |                    |
| 21  | **G6.1: Human Opens Door**                 | Human opens the room door.                                                                       | `-`                                            | Perform       | Door opened by human                        | AND          | OK                                                    |  OK                  |                    |
| 22  | **G6.2: Robot Opens Door**                 | Robot opens the room door.                                                                       | `-`                                            | Perform       | Door opened by robot                        | AND          | OK                                                    |  OK                  |                    |


---

**Task‑Model Summary**

| # | Task ID & TITLE | Text | Relation | Location | Number of Robots |
|---|-----------------|------|----------|----------|------------------|
| 1 | **AT1: Pick up Food from Kitchen** | Robot picks up requested meals from the kitchen. | AND | kitchen | 1 |
| 2 | **AT2: Transport Food to Room** | Robot transports meals from kitchen to patient room. | AND | hallway → patient_room | 1 |
| 3 | **AT3: Deliver to Table** | Robot places meals onto patient table. | AND | patient_room, patient_table | 1 |
| 4 | **AT4: Patient Fetch from Tray** | Patient fetches meals from robot’s tray. | AND | patient_room, robot_tray | 0 |
| 5 | **AT5: Nurse Fetch from Tray** | Nurse fetches meals from robot’s tray. | AND | patient_room, robot_tray | 0 |
| 6 | **AT6: Robot Fetch from Tray** | Robot fetches meals from robot’s tray. | AND | patient_room, robot_tray | 1 |
| 7 | **AT7: Patient Retrieves Meal** | Patient retrieves meal from tray. | AND | patient_room, patient_tray | 0 |
| 8 | **AT8: Alert Wrong Meal** | Robot alerts staff if wrong meal retrieved. | AND | patient_room | 1 |
| 9 | **AT9: Log Meal Retrieval** | Robot logs retrieval time and location. | AND | patient_room | 1 |
|10 | **AT10: Unassisted Dish Retrieval** | Robot picks up dishes from patient room. | AND | patient_room | 1 |
|11 | **AT11: Robot Cooperation Dish Retrieval** | Two robots cooperate to pick up dishes. | AND | patient_room | [2,2] |
|12 | **AT12: Human Cooperation Dish Retrieval** | Robot assists human in picking up dishes. | AND | patient_room | 1 |
|13 | **AT13: Human Opens Door** | Human opens the patient room door. | AND | patient_room_door | 0 |
|14 | **AT14: Robot Opens Door** | Robot opens the patient room door. | AND | patient_room_door | 1 |

---

### Logical Relationships (Tree‑Structure)

```
G1 -> G2, G3, G4 [AND][;]
G2 -> AT1 [AND]
G3 -> AT2 [AND]
G4 -> G4.1, G4.2 [OR][FALLBACK(G4.1, G4.2)]
G4.1 -> AT3 [AND]
G4.2 -> G4.2.1, G4.2.2, G4.2.3, G4.2.4 [AND][;]
G4.2.1 -> G4.2.1.1, G4.2.1.2 [AND][;]
G4.2.1.1 -> (query) [AND]
G4.2.1.2 -> G4.2.1.2.1, G4.2.1.2.2, G4.2.1.2.3 [OR][FALLBACK(...)]
G4.2.1.2.1 -> AT4 [AND]
G4.2.1.2.2 -> AT5 [AND]
G4.2.1.2.3 -> AT6 [AND]
G4.2.2 -> AT7 [AND]
G4.2.3 -> AT8 [AND]
G4.2.4 -> AT9 [AND]
G5 -> G5.1, G5.2, G5.3 [OR][FALLBACK(G5.1, G5.2, G5.3)]
G5.1 -> AT10 [AND]
G5.2 -> AT11 [AND]
G5.3 -> AT12 [AND]
G6 -> G6.1, G6.2 [OR][FALLBACK(G6.1, G6.2)]
G6.1 -> AT13 [AND]
G6.2 -> AT14 [AND]
```

These tables and relationships provide a complete, depth‑first numbered goal model that decomposes the multi‑robot food‑delivery mission into actionable tasks, explicitly handling uncertainty, cooperation, and fallback strategies.
