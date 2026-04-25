**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

---

## 1. Goal Tables  

| **Name**                               | **Text**                                                                                                                            | **Runtime**                            | **Goal Type** | **Target Condition / Enquired Information**                             | **Relation**                                                                                                                                                                        | **Justification**                                                                                                             | Ground truth I                                        | Ground truth C | Ground truth E |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------- | -------------- |
| **G1: Ensure meal & dishes**           | Ensure that the inpatient receives the correct meal and all dishes are removed from the room, and the robot returns to the kitchen. | `;`                                    | Achieve       | “Meal delivered to patient; all dishes removed; robot back at kitchen.” | –                                                                                                                                                                                   | Sequential: the robot must finish the meal delivery before it can safely collect dishes without interfering with the patient. | Perform.                                              | Perform          |                |
| **G2: Deliver food to patient**        | Perform the delivery of food to the inpatient.                                                                                      | `FALLBACK(G2.1, G2.2)`                 | Perform       | –                                                                       | OR (fallback) – the robot first tries to deliver directly to the table; if that fails (e.g., table inaccessible, patient unable to fetch), it falls back to fetching from its tray. |                                                                                                                               | Achieve. Target condition: all food was delivered.    | OK               |                |
| **G2.1: Deliver to table**             | Deliver the meal onto the patient’s table.                                                                                          | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Direct manipulation of the table – a single robot with the special manipulation skill suffices.                               | OK                                                    | OK               |                |
| **G2.2: Fetch from tray**              | Fetch the meal from the robot’s tray and hand it to the patient.                                                                    | `AND(G3, G2.2.1, G2.2.2, G2.2.3)`      | Perform       | –                                                                       | AND – all sub-tasks must succeed: open the door, indicate the meal, track retrieval, and alert if wrong.                                                                            | OK                                                                                                                            | OK                                                    | OK               |                |
| **G3: Open room door**                 | Open the patient room door.                                                                                                         | `FALLBACK(G3.1, G3.2)`                 | Perform       | –                                                                       | OR (fallback) – robot first attempts to open alone; if the door is locked or requires assistance, it falls back to asking a human.                                                  |                                                                                                                               | OK                                                    | OK               |                |
| **G3.1: Open door by robot alone**     | Robot opens the door using its mechanical arm.                                                                                      | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Robot-only operation when the door is not locked.                                                                             | OK                                                    | OK               |                |
| **G3.2: Open door with human**         | Human opens the door while robot waits.                                                                                             | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Human assistance required when the door is locked or the robot cannot reach the handle.                                       | OK                                                    | OK               |                |
| **G2.2.1: Indicate meal to patient**   | Robot verbally or visually indicates which meal the patient should take.                                                            | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Needed for patients who can fetch but need guidance.                                                                          | OK                                                    | OK               |                |
| **G2.2.2: Track meal retrieval**       | Robot records the time and location when the patient takes the meal.                                                                | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Enables later verification that the correct meal was taken.                                                                   | OK                                                    | OK               |                |
| **G2.2.3: Alert wrong meal**           | Robot alerts staff if the patient takes a meal that is not the one ordered.                                                         | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Safety & quality-control measure.                                                                                             | OK                                                    | OK               |                |
| **G4: Retrieve dishes**                | Retrieve all dirty dishes from the patient room.                                                                                    | `FALLBACK(G4.1, FALLBACK(G4.2, G4.3))` | Perform       | –                                                                       | OR (fallback) – first try unassisted; if that fails, try with another robot; if that fails, ask a human.                                                                            |                                                                                                                               | Achieve. Target condition: all dishes were retrieved. | OK               |                |
| **G4.1: Unassisted dish retrieval**    | Robot picks up dishes on its own.                                                                                                   | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Possible when dishes are few and robot has sufficient reach.                                                                  | OK                                                    | OK               |                |
| **G4.2: Cooperate with another robot** | Two robots cooperate to lift heavy or many dishes.                                                                                  | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Required when dish load exceeds one robot’s capacity.                                                                         | OK                                                    | OK               |                |
| **G4.3: Cooperate with human**         | Human assists the robot in picking up dishes.                                                                                       | `-`                                    | Perform       | –                                                                       | –                                                                                                                                                                                   | Needed when the robot cannot reach or the patient is present.                                                                 | OK                                                    | OK               |                |


---

## 2. Task Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1: Navigate to kitchen** | Robot moves from its current location to the kitchen. | AND (child of G2.1 & G2.2) | Kitchen | 1 | Robot must be in the kitchen to pick up meals. |
| **AT2: Pick up meal** | Robot uses its manipulator to grab the ordered meal. | AND | Kitchen | 1 | One robot is sufficient; the manipulator is specialized. |
| **AT3: Navigate to patient room** | Robot travels from kitchen to the patient’s room. | AND | Patient room | 1 | Direct path needed before any door operation. |
| **AT4: Open door** | Robot attempts to open the room door. | OR (child of G3) | Room door | 1 | Robot’s arm may open the handle; if not, fallback to human. |
| **AT5: Deliver meal to table** | Robot places the meal onto the patient’s table. | AND (child of G2.1) | Patient room table | 1 | Direct manipulation; no assistance required. |
| **AT6: Return to kitchen** | Robot returns to the kitchen after delivery. | AND (child of G2.1 & G2.2) | Kitchen | 1 | Allows robot to pick up next meal. |
| **AT7: Navigate to kitchen** | (Duplicate for clarity in G2.2) | AND (child of G2.2) | Kitchen | 1 | Same as AT1; included for completeness. |
| **AT8: Pick up meal** | (Duplicate for G2.2) | AND | Kitchen | 1 | Same as AT2. |
| **AT9: Navigate to patient room** | (Duplicate for G2.2) | AND | Patient room | 1 | Same as AT3. |
| **AT10: Open door** | (Duplicate for G2.2) | OR (child of G3) | Room door | 1 | Same as AT4. |
| **AT11: Deliver meal to patient** | Robot hands the meal to the patient. | AND (child of G2.2) | Patient room | 1 | Requires patient to be present and able to receive. |
| **AT12: Indicate meal to patient** | Robot announces or displays the meal ID. | AND (child of G2.2.1) | Patient room | 1 | Needed for patients who can fetch but need guidance. |
| **AT13: Track meal retrieval** | Robot logs the time and location of meal pickup. | AND (child of G2.2.2) | Patient room | 1 | Enables later verification. |
| **AT14: Alert wrong meal** | Robot triggers an alarm if wrong meal detected. | AND (child of G2.2.3) | Patient room | 1 | Safety measure. |
| **AT15: Return to kitchen** | (Duplicate for G2.2) | AND | Kitchen | 1 | Same as AT6. |
| **AT16: Navigate to door** | Robot moves to the room door. | AND (child of G3) | Room door | 1 | Needed before attempting to open. |
| **AT17: Open door by robot** | Robot uses its arm to open the door. | OR (child of G3.1) | Room door | 1 | Robot‑only operation. |
| **AT18: Ask human to open door** | Robot signals a human to open the door. | OR (child of G3.2) | Room door | 1 | Human assistance required. |
| **AT19: Navigate to patient room** | Robot moves to the patient room for dish retrieval. | AND (child of G4) | Patient room | 1 | Positioning before retrieval. |
| **AT20: Retrieve dishes unassisted** | Robot picks up dishes on its own. | OR (child of G4.1) | Patient room | 1 | Possible when dish load is light. |
| **AT21: Retrieve dishes with another robot** | Two robots cooperate to lift dishes. | OR (child of G4.2) | Patient room | [2,2] | Needed when dishes are heavy or many. |
| **AT22: Retrieve dishes with human** | Human assists robot in picking up dishes. | OR (child of G4.3) | Patient room | 1 | Needed when robot cannot reach or patient is present. |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Type** | **Title** | **Runtime / Relation** | **Location / Condition** | **Notes** |
|--------|----------|-----------|------------------------|--------------------------|-----------|
| G1 | Goal | Ensure meal & dishes | `;` (sequential) | – | Top‑level achieve goal |
| G2 | Goal | Deliver food to patient | `FALLBACK(G2.1, G2.2)` | – | OR fallback |
| G2.1 | Goal | Deliver to table | `-` | – | Perform |
| G2.2 | Goal | Fetch from tray | `AND(G3, G2.2.1, G2.2.2, G2.2.3)` | – | Perform |
| G3 | Goal | Open room door | `FALLBACK(G3.1, G3.2)` | – | Perform |
| G3.1 | Goal | Open door by robot | `-` | – | Perform |
| G3.2 | Goal | Open door with human | `-` | – | Perform |
| G2.2.1 | Goal | Indicate meal | `-` | – | Perform |
| G2.2.2 | Goal | Track retrieval | `-` | – | Perform |
| G2.2.3 | Goal | Alert wrong meal | `-` | – | Perform |
| G4 | Goal | Retrieve dishes | `FALLBACK(G4.1, FALLBACK(G4.2, G4.3))` | – | Perform |
| G4.1 | Goal | Unassisted dish retrieval | `-` | – | Perform |
| G4.2 | Goal | Cooperate with another robot | `-` | – | Perform |
| G4.3 | Goal | Cooperate with human | `-` | – | Perform |
| AT1 | Task | Navigate to kitchen | AND | Kitchen | 1 robot |
| AT2 | Task | Pick up meal | AND | Kitchen | 1 robot |
| AT3 | Task | Navigate to patient room | AND | Patient room | 1 robot |
| AT4 | Task | Open door | OR | Room door | 1 robot |
| AT5 | Task | Deliver meal to table | AND | Patient room table | 1 robot |
| AT6 | Task | Return to kitchen | AND | Kitchen | 1 robot |
| AT7 | Task | Navigate to kitchen | AND | Kitchen | 1 robot |
| AT8 | Task | Pick up meal | AND | Kitchen | 1 robot |
| AT9 | Task | Navigate to patient room | AND | Patient room | 1 robot |
| AT10 | Task | Open door | OR | Room door | 1 robot |
| AT11 | Task | Deliver meal to patient | AND | Patient room | 1 robot |
| AT12 | Task | Indicate meal | AND | Patient room | 1 robot |
| AT13 | Task | Track retrieval | AND | Patient room | 1 robot |
| AT14 | Task | Alert wrong meal | AND | Patient room | 1 robot |
| AT15 | Task | Return to kitchen | AND | Kitchen | 1 robot |
| AT16 | Task | Navigate to door | AND | Room door | 1 robot |
| AT17 | Task | Open door by robot | OR | Room door | 1 robot |
| AT18 | Task | Ask human to open door | OR | Room door | 1 robot |
| AT19 | Task | Navigate to patient room | AND | Patient room | 1 robot |
| AT20 | Task | Retrieve dishes unassisted | OR | Patient room | 1 robot |
| AT21 | Task | Retrieve dishes with another robot | OR | Patient room | [2,2] robots |
| AT22 | Task | Retrieve dishes with human | OR | Patient room | 1 robot |

---

## 4. Logical Relationships (with Justifications)

| **Parent → Children** | **Relation** | **Runtime** | **Justification** |
|------------------------|--------------|-------------|-------------------|
| **G1 → G2, G4** | AND | `;` | The robot must deliver food **and** retrieve dishes; these are independent but both must finish before the mission is complete. Sequential execution (`;`) is chosen because dish retrieval should occur after delivery to avoid interference with the patient. |
| **G2 → G2.1, G2.2** | OR (fallback) | `FALLBACK(G2.1, G2.2)` | The robot first attempts to deliver directly to the table. If that fails (e.g., table inaccessible, patient unable to fetch), it falls back to fetching from its tray. |
| **G2.2 → G3, G2.2.1, G2.2.2, G2.2.3** | AND | `AND(...)` | All sub‑tasks must succeed: open the door, indicate the meal, track retrieval, and alert if wrong. |
| **G3 → G3.1, G3.2** | OR (fallback) | `FALLBACK(G3.1, G3.2)` | Robot first tries to open the door alone; if the door is locked or unreachable, it falls back to asking a human. |
| **G4 → G4.1, G4.2, G4.3** | OR (nested fallback) | `FALLBACK(G4.1, FALLBACK(G4.2, G4.3))` | The robot attempts unassisted retrieval first; if that fails (e.g., too many dishes), it tries cooperation with another robot; if that fails, it asks a human. |
| **AT1–AT6 → G2.1** | AND | – | All tasks are required to deliver to the table. |
| **AT7–AT15 → G2.2** | AND | – | All tasks are required to fetch from the tray. |
| **AT16–AT18 → G3** | OR | – | Robot may open the door itself or ask a human. |
| **AT19–AT22 → G4** | OR | – | Robot may retrieve dishes unassisted, with another robot, or with a human. |

---

### Key Design Decisions & Justifications

| Decision | Reasoning |
|----------|-----------|
| **Sequential top‑level (G1)** | The robot must finish meal delivery before it can safely collect dishes; parallel execution could lead to interference with the patient. |
| **Fallback between delivery methods** | The mission description explicitly states the robot can choose between table delivery or tray retrieval; fallback captures this choice. |
| **Fallback for door opening** | The robot may or may not be able to open the door; fallback ensures a human can assist if needed. |
| **Nested fallback for dish retrieval** | Dish retrieval may succeed unassisted, but if not, cooperation with another robot or a human is possible; nested fallback preserves priority order. |
| **AND for sub‑tasks within fetch** | All steps (door opening, indication, tracking, alert) are necessary for a successful fetch operation. |
| **OR for tasks that involve cooperation** | Tasks that involve human or another robot are alternatives; only one is needed to succeed. |
| **Number of robots** | Tasks that require cooperation with another robot explicitly use `[2,2]`; tasks that involve a human use `1` robot (robot + human). |
| **Task locations** | Each task is assigned a location that matches the mission description (kitchen, patient room, door). |
| **Goal types** | All high‑level operational objectives are `Perform` because they involve actions; the top‑level is `Achieve` because it specifies a desired world state. |

---

**End of Goal Model**
