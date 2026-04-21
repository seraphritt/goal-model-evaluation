**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

| **Name**                                     | **Text**                                                                            | **Runtime**                                                         | **Goal Type** | **Enquired Information / Target Condition**        | **Relation**   | **Ground truth I**                                    | **Ground truth C** | **Ground truth E** |
| -------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------- | -------------------------------------------------- | -------------- | ----------------------------------------------------- | ------------------ | ------------------ |
| **G1 – Deliver Food and Clean Room**         | Deliver food to the inpatient room and retrieve dirty dishes.                       | `;`                                                                 | Perform       | –                                                  | Root           | OK                                                    | OK                   |                    |
| **G2 – Food Delivery**                       | Deliver food to the inpatient room.                                                 | `FALLBACK(G3,G4)`                                                   | Perform       | –                                                  | AND (to G1)    | Achieve. Target condition: all food was delivered.    | OK                   |                    |
| **G3 – Deliver Food to Table**               | Deliver the meal to the patient’s table.                                            | `-`                                                                 | Perform       | –                                                  | OR (to G2)     | OK                                                    | OK                   |                    |
| **G4 – Fetch Meal from Tray**                | Fetch the meal from the robot’s tray for the patient.                               | `;`                                                                 | Perform       | –                                                  | OR (to G2)     | OK                                                    | OK                   |                    |
| **G4.0 – Query Retrieval Capabilities**      | Query whether the patient can retrieve the meal and whether a companion is present. | `#`                                                                 | Query         | “Can patient retrieve meal? Is companion present?” | AND (to G4)    | OK                                                    | OK                   |                    |
| **G4.1 – Choose Retrieval Method**           | Decide the method for retrieving the meal based on the queried information.         | `-`                                                                 | Perform       | –                                                  | AND (to G4)    | OK                                                    | OK                   |                    |
| **G4.2 – Execute Retrieval**                 | Execute the retrieval of the meal, including validation.                            | `;`                                                                 | Perform       | –                                                  | AND (to G4)    | OK                                                    | OK                   |                    |
| **G4.2.0 – Retrieval Methods**               | Attempt retrieval using patient, companion, nurse, or robot cooperation.            | `FALLBACK(G4.2.0.1,FALLBACK(G4.2.0.2,FALLBACK(G4.2.0.3,G4.2.0.4)))` | Perform       | –                                                  | AND (to G4.2)  | OK                                                    | OK                   |                    |
| **G4.2.0.1 – Patient Retrieval**             | Patient retrieves the meal from the robot’s tray.                                   | `-`                                                                 | Perform       | –                                                  | OR (to G4.2.0) | OK                                                    | OK                   |                    |
| **G4.2.0.2 – Companion Retrieval**           | Companion retrieves the meal from the robot’s tray.                                 | `-`                                                                 | Perform       | –                                                  | OR (to G4.2.0) | OK                                                    | OK                   |                    |
| **G4.2.0.3 – Nurse Retrieval**               | Nurse retrieves the meal from the robot’s tray.                                     | `-`                                                                 | Perform       | –                                                  | OR (to G4.2.0) | OK                                                    | OK                   |                    |
| **G4.2.0.4 – Robot Cooperation Retrieval**   | Another robot cooperates to retrieve the meal from the tray.                        | `-`                                                                 | Perform       | –                                                  | OR (to G4.2.0) | OK                                                    | OK                   |                    |
| **G4.2.1 – Validation**                      | Log meal retrieval and verify meal correctness.                                     | `#`                                                                 | Perform       | –                                                  | AND (to G4.2)  | OK                                                    | OK                   |                    |
| **G5 – Retrieve Dirty Dishes**               | Retrieve dirty dishes from the inpatient room.                                      | `;`                                                                 | Perform       | –                                                  | AND (to G1)    | Achieve. Target condition: all dishes were retrieved. | OK                   |                    |
| **G5.1 – Check for Dirty Dishes**            | Check if there are dirty dishes in the room.                                        | `-`                                                                 | Query         | “Are there dirty dishes?”                          | AND (to G5)    | OK                                                    | OK                   |                    |
| **G5.2 – Open Door**                         | Open the room door to allow dish retrieval.                                         | `FALLBACK(G5.2.1,G5.2.2)`                                           | Perform       | –                                                  | AND (to G5)    | OK                                                    | OK                   |                    |
| **G5.2.1 – Robot opens door**                | Robot opens the room door.                                                          | `-`                                                                 | Perform       | –                                                  | OR (to G5.2)   | OK                                                    | OK                   |                    |
| **G5.2.2 – Human opens door**                | Human opens the room door.                                                          | `-`                                                                 | Perform       | –                                                  | OR (to G5.2)   | OK                                                    | OK                   |                    |
| **G5.3 – Retrieve Dishes**                   | Retrieve dirty dishes from the room.                                                | `FALLBACK(G5.3.1,FALLBACK(G5.3.2,G5.3.3))`                          | Perform       | –                                                  | AND (to G5)    | OK                                                    | OK                   |                    |
| **G5.3.1 – Unassisted Retrieval**            | Robot retrieves dishes alone.                                                       | `-`                                                                 | Perform       | –                                                  | OR (to G5.3)   | OK                                                    | OK                   |                    |
| **G5.3.2 – Two Robot Cooperation Retrieval** | Two robots retrieve dishes together.                                                | `-`                                                                 | Perform       | –                                                  | OR (to G5.3)   | OK                                                    | OK                   |                    |
| **G5.3.3 – Human Assistance Retrieval**      | Robot retrieves dishes with human assistance.                                       | `-`                                                                 | Perform       | –                                                  | OR (to G5.3)   | OK                                                    | OK                   |                    |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1 – Deliver Meal to Table** | Deliver the meal to the patient’s table. | AND (to G3) | Inpatient room | 1 |
| **AT2 – Query Patient Retrieval Capability** | Query the patient’s ability to retrieve the meal. | AND (to G4.0) | Robot (internal) | 1 |
| **AT3 – Query Companion Presence** | Query whether a companion is present in the room. | AND (to G4.0) | Inpatient room | 1 |
| **AT4 – Decide Retrieval Method** | Decide which method to use for meal retrieval. | AND (to G4.1) | Robot | 1 |
| **AT5 – Patient retrieves meal** | Patient picks up the meal from the robot’s tray. | OR (to G4.2.0) | Inpatient room | 1 |
| **AT6 – Companion retrieves meal** | Companion picks up the meal from the robot’s tray. | OR (to G4.2.0) | Inpatient room | 1 |
| **AT7 – Nurse retrieves meal** | Nurse picks up the meal from the robot’s tray. | OR (to G4.2.0) | Inpatient room | 1 |
| **AT8 – Robot fetches meal from tray** | Another robot cooperates to fetch the meal from the tray. | OR (to G4.2.0) | Robot’s tray | 2 |
| **AT9 – Scan room for dirty dishes** | Scan the room to detect dirty dishes. | AND (to G5.1) | Inpatient room | 1 |
| **AT10 – Robot retrieves dishes alone** | Robot picks up dirty dishes by itself. | OR (to G5.3) | Inpatient room | 1 |
| **AT11 – Two robots retrieve dishes together** | Two robots cooperate to pick up dirty dishes. | OR (to G5.3) | Inpatient room | 2 |
| **AT12 – Robot retrieves dishes with human assistance** | Robot picks up dishes with help from human. | OR (to G5.3) | Inpatient room | 1 |
| **AT13 – Robot opens door** | Robot opens the room door. | OR (to G5.2) | Room door | 1 |
| **AT14 – Human opens door** | Human opens the room door. | OR (to G5.2) | Room door | 0 |
| **AT15 – Log meal retrieval** | Log the retrieval event and location. | AND (to G4.2.1) | Robot | 1 |
| **AT16 – Verify meal correctness** | Verify that the correct meal was retrieved. | AND (to G4.2.1) | Robot | 1 |

---

### Logical Relationships Summary

```
G1 -> G2, G5 [AND][;]
G2 -> G3, G4 [OR][FALLBACK(G3,G4)]
G3 -> AT1 [AND]
G4 -> G4.0, G4.1, G4.2 [AND][;]
G4.0 -> AT2, AT3 [AND][#]
G4.1 -> AT4 [AND]
G4.2 -> G4.2.0, G4.2.1 [AND][;]
G4.2.0 -> G4.2.0.1, G4.2.0.2, G4.2.0.3, G4.2.0.4 [OR][FALLBACK(G4.2.0.1,FALLBACK(G4.2.0.2,FALLBACK(G4.2.0.3,G4.2.0.4))]
G4.2.0.1 -> AT5 [OR]
G4.2.0.2 -> AT6 [OR]
G4.2.0.3 -> AT7 [OR]
G4.2.0.4 -> AT8 [OR]
G4.2.1 -> AT15, AT16 [AND][#]
G5 -> G5.1, G5.2, G5.3 [AND][;]
G5.1 -> AT9 [AND]
G5.2 -> G5.2.1, G5.2.2 [OR][FALLBACK(G5.2.1,G5.2.2)]
G5.2.1 -> AT13 [OR]
G5.2.2 -> AT14 [OR]
G5.3 -> G5.3.1, G5.3.2, G5.3.3 [OR][FALLBACK(G5.3.1,FALLBACK(G5.3.2,G5.3.3))]
G5.3.1 -> AT10 [OR]
G5.3.2 -> AT11 [OR]
G5.3.3 -> AT12 [OR]
```

This goal‑task decomposition captures all mission requirements, handles uncertainty through query goals, and specifies fallback strategies for robot–human cooperation and multi‑robot collaboration.
