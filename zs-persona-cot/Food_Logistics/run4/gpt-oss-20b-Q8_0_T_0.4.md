**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

---

## 1. Goal Table

| Name                                                    | Text                                                                                   | Runtime                                                  | Goal Type | Target Condition / Enquired Information                                | Relation                         | Justification                                                                                                                          | Ground truth I                                        | Ground truth C | Ground truth E |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------- | ---------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------- | -------------- |
| **G1**: *Deliver Food to Inpatient Room*                | Deliver food from the kitchen to the inpatient’s room.                                 | `;` (sequential)                                         | Achieve   | “Food is delivered to the inpatient’s room (table or tray).”           | AND (with G2, G3)                | The overall mission is only satisfied after the method is decided **and** the delivery is executed.                                    | OK                                                    | Perform          |                |
| **G2**: *Determine Delivery Method*                     | Decide whether to deliver food directly to the table or to the tray for patient fetch. | `-`                                                      | Query     | *Patient fetch capability, presence of companion, nurse availability.* | AND (with G1)                    | The delivery plan depends on patient and staff availability.                                                                           | OKs                                                   | OK               |                |
| **G3**: *Execute Delivery*                              | Perform the chosen delivery method.                                                    | `FALLBACK(G3.1, G3.2)`                                   | Perform   | –                                                                      | AND (with G1)                    | The delivery is performed after the method is selected; a fallback guarantees that if direct delivery fails, the tray-method is tried. | OK                                                    | Achieve               |                |
| **G3.1**: *Deliver Food to Table*                       | Robot delivers food directly to the room table.                                        | `-`                                                      | Perform   | –                                                                      | OR (with G3.2)                   | Direct table delivery is an alternative to tray-delivery.                                                                              | Ok                                                    | OK               |                |
| **G3.2**: *Deliver Food to Tray & Assist Patient Fetch* | Robot places food on the tray and assists the patient in fetching it.                  | `&`                                                      | Perform   | –                                                                      | OR (with G3.1)                   | This is the alternative when the patient can fetch.                                                                                    | Ok                                                    | OK               |                |
| **G3.2.1**: *Deliver Food to Tray*                      | Robot places the food on the patient’s tray.                                           | `-`                                                      | Perform   | –                                                                      | AND (with G3.2)                  | Must be done before the patient can fetch.                                                                                             | Ok                                                    | OK               |                |
| **G3.2.2**: *Assist Patient Fetch*                      | Robot assists the patient in retrieving food from the tray.                            | `&`                                                      | Perform   | –                                                                      | AND (with G3.2)                  | Assistance is required for patient fetch.                                                                                              | OK                                                    | OK               |                |
| **G3.2.2.1**: *Open Room Door*                          | Robot opens the room door to allow access.                                             | `-`                                                      | Perform   | –                                                                      | AND (with G3.2.2)                | Door must be opened for the patient to reach the tray.                                                                                 | OK                                                    | OK               |                |
| **G3.2.2.2**: *Indicate Meal*                           | Robot indicates which meal the patient should retrieve.                                | `-`                                                      | Perform   | –                                                                      | AND (with G3.2.2)                | Prevents wrong meal retrieval.                                                                                                         | OK                                                    | OK               |                |
| **G3.2.2.3**: *Track Retrieval*                         | Robot tracks when and where each meal is retrieved.                                    | `-`                                                      | Perform   | –                                                                      | AND (with G3.2.2)                | Tracking is needed for audit and safety.                                                                                               | OK                                                    | OK               |                |
| **G3.2.2.4**: *Alert Wrong Meal*                        | Robot alerts if a wrong meal is retrieved.                                             | `-`                                                      | Perform   | –                                                                      | AND (with G3.2.2)                | Safety check.                                                                                                                          | OK                                                    | OK               |                |
| **G3.2.2.5**: *Retrieve Dishes*                         | Robot retrieves dirty dishes from the room.                                            | `FALLBACK(FALLBACK(G3.2.2.5.1, G3.2.2.5.2), G3.2.2.5.3)` | Perform   | –                                                                      | AND (with G3.2.2)                | Dish retrieval can be done in several ways; fallback ensures success.                                                                  | Achieve. Target condition: all dishes were retrieved. | OK               |                |
| **G3.2.2.5.1**: *Retrieve Dishes Unassisted*            | Robot retrieves dishes without assistance.                                             | `-`                                                      | Perform   | –                                                                      | OR (with G3.2.2.5.2, G3.2.2.5.3) | Unassisted retrieval is possible if the robot can lift the dishes.                                                                     | Ok                                                    | OK               |                |
| **G3.2.2.5.2**: *Retrieve Dishes with Two Robots*       | Two robots cooperate to retrieve dishes.                                               | `-`                                                      | Perform   | –                                                                      | OR (with G3.2.2.5.1, G3.2.2.5.3) | Heavy dishes may require two robots.                                                                                                   | OK                                                    | OK               |                |
| **G3.2.2.5.3**: *Retrieve Dishes with Human*            | Robot retrieves dishes with human assistance.                                          | `-`                                                      | Perform   | –                                                                      | OR (with G3.2.2.5.1, G3.2.2.5.2) | Human help may be needed for awkward dishes or safety.                                                                                 | OK                                                    | OK               |                |


---

## 2. Task Table

| Name | Text | Relation | Location | Number of Robots | Justification |
|------|------|----------|----------|------------------|---------------|
| **AT1**: *Query Patient Fetch Capability* | Query the inpatient record to determine if the patient can fetch food from the tray. | AND (with G2) | hospital | 1 | Robot must know patient capability before deciding delivery method. |
| **AT2**: *Query Companion Presence* | Query the inpatient record to determine if a companion is present. | AND (with G2) | hospital | 1 | Companion may assist in fetching. |
| **AT3**: *Query Nurse Availability* | Query the nurse scheduling system to determine if a nurse is available for assistance. | AND (with G2) | hospital | 1 | Nurse may assist if patient or companion cannot. |
| **AT4**: *Deliver Food to Table* | Robot delivers the food to the patient’s table using special manipulation skill. | AND (with G3.1) | inpatient room | 1 | Direct table delivery is a single‑robot action. |
| **AT5**: *Deliver Food to Tray* | Robot places the food on the patient’s tray. | AND (with G3.2.1) | inpatient room | 1 | Required before patient fetch. |
| **AT6**: *Open Room Door* | Robot opens the room door to allow patient access. | AND (with G3.2.2.1) | room door | 1 | Door must be opened for patient to reach the tray. |
| **AT7**: *Indicate Meal to Patient* | Robot indicates which meal the patient should retrieve. | AND (with G3.2.2.2) | inpatient room | 1 | Prevents wrong meal retrieval. |
| **AT8**: *Track Meal Retrieval* | Robot tracks when and where each meal is retrieved. | AND (with G3.2.2.3) | inpatient room | 1 | Tracking needed for audit and safety. |
| **AT9**: *Alert Wrong Meal* | Robot alerts if a wrong meal is retrieved. | AND (with G3.2.2.4) | inpatient room | 1 | Safety check. |
| **AT10**: *Retrieve Dishes Unassisted* | Robot retrieves dirty dishes from the room without assistance. | AND (with G3.2.2.5.1) | inpatient room | 1 | Robot can lift dishes on its own. |
| **AT11**: *Retrieve Dishes with Two Robots* | Two robots cooperate to retrieve dirty dishes. | AND (with G3.2.2.5.2) | inpatient room | [2,2] | Heavy dishes may need two robots. |
| **AT12**: *Retrieve Dishes with Human* | Robot retrieves dirty dishes with human assistance. | AND (with G3.2.2.5.3) | inpatient room | 1 | Human help may be needed for awkward dishes or safety. |

---

## 3. Summary Table (Goals + Tasks)

| ID | Type | Text | Runtime / Goal Type | Relation | Justification |
|----|------|------|---------------------|----------|---------------|
| G1 | Goal | Deliver food from kitchen to inpatient room | `;` / Achieve | AND (with G2, G3) | Must decide method **and** execute delivery. |
| G2 | Goal | Determine delivery method | `-` / Query | AND (with G1) | Needed to choose between table or tray. |
| G3 | Goal | Execute delivery | `FALLBACK(G3.1,G3.2)` / Perform | AND (with G1) | Delivery performed after method selection; fallback ensures alternative. |
| G3.1 | Goal | Deliver food to table | `-` / Perform | OR (with G3.2) | Direct table delivery is an alternative. |
| G3.2 | Goal | Deliver food to tray & assist patient fetch | `&` / Perform | OR (with G3.1) | Alternative when patient can fetch. |
| G3.2.1 | Goal | Deliver food to tray | `-` / Perform | AND (with G3.2) | Must happen before patient fetch. |
| G3.2.2 | Goal | Assist patient fetch | `&` / Perform | AND (with G3.2) | Needed for patient retrieval. |
| G3.2.2.1 | Goal | Open room door | `-` / Perform | AND (with G3.2.2) | Door must be opened. |
| G3.2.2.2 | Goal | Indicate meal | `-` / Perform | AND (with G3.2.2) | Prevent wrong meal. |
| G3.2.2.3 | Goal | Track retrieval | `-` / Perform | AND (with G3.2.2) | Tracking required. |
| G3.2.2.4 | Goal | Alert wrong meal | `-` / Perform | AND (with G3.2.2) | Safety. |
| G3.2.2.5 | Goal | Retrieve dishes | `FALLBACK(FALLBACK(G3.2.2.5.1,G3.2.2.5.2),G3.2.2.5.3)` / Perform | AND (with G3.2.2) | Dish retrieval can be done in several ways. |
| G3.2.2.5.1 | Goal | Retrieve dishes unassisted | `-` / Perform | OR (with G3.2.2.5.2, G3.2.2.5.3) | Possible if robot can lift dishes. |
| G3.2.2.5.2 | Goal | Retrieve dishes with two robots | `-` / Perform | OR (with G3.2.2.5.1, G3.2.2.5.3) | Heavy dishes may need two robots. |
| G3.2.2.5.3 | Goal | Retrieve dishes with human | `-` / Perform | OR (with G3.2.2.5.1, G3.2.2.5.2) | Human help may be needed. |
| AT1 | Task | Query patient fetch capability | – | AND (with G2) | Needed for method decision. |
| AT2 | Task | Query companion presence | – | AND (with G2) | Companion may assist. |
| AT3 | Task | Query nurse availability | – | AND (with G2) | Nurse may assist. |
| AT4 | Task | Deliver food to table | – | AND (with G3.1) | Direct table delivery. |
| AT5 | Task | Deliver food to tray | – | AND (with G3.2.1) | Place food on tray. |
| AT6 | Task | Open room door | – | AND (with G3.2.2.1) | Door opening. |
| AT7 | Task | Indicate meal to patient | – | AND (with G3.2.2.2) | Prevent wrong meal. |
| AT8 | Task | Track meal retrieval | – | AND (with G3.2.2.3) | Tracking. |
| AT9 | Task | Alert wrong meal | – | AND (with G3.2.2.4) | Safety. |
| AT10 | Task | Retrieve dishes unassisted | – | AND (with G3.2.2.5.1) | Robot can lift dishes. |
| AT11 | Task | Retrieve dishes with two robots | – | AND (with G3.2.2.5.2) | Heavy dishes. |
| AT12 | Task | Retrieve dishes with human | – | AND (with G3.2.2.5.3) | Human help. |

---

## 4. Logical Relationships

| Relationship | Justification |
|--------------|---------------|
| **G1 → G2, G3** (AND; sequential `;`) | The overall mission first requires determining the delivery method **and** then executing the delivery. |
| **G2 → AT1, AT2, AT3** (AND) | The decision on delivery method depends on patient fetch capability, companion presence, and nurse availability. |
| **G3 → G3.1, G3.2** (OR; fallback) | Delivery is performed by either direct table delivery or tray‑delivery with assistance; if the first fails, the second is attempted. |
| **G3.1 → AT4** (AND) | Direct table delivery requires the robot to perform the delivery task. |
| **G3.2 → G3.2.1, G3.2.2** (AND) | Tray delivery requires placing the food on the tray **and** assisting the patient in fetching. |
| **G3.2.1 → AT5** (AND) | Placing food on the tray is a necessary sub‑task. |
| **G3.2.2 → G3.2.2.1, G3.2.2.2, G3.2.2.3, G3.2.2.4, G3.2.2.5** (AND) | All assistance steps must be performed. |
| **G3.2.2.1 → AT6** (AND) | Door opening is required before the patient can fetch. |
| **G3.2.2.2 → AT7** (AND) | The robot must indicate the correct meal. |
| **G3.2.2.3 → AT8** (AND) | Tracking is needed for audit. |
| **G3.2.2.4 → AT9** (AND) | Wrong‑meal detection is a safety step. |
| **G3.2.2.5 → AT10, AT11, AT12** (OR; fallback) | Dish retrieval can be unassisted, with two robots, or with human help; fallback ensures success. |
| **AT10, AT11, AT12** (AND with corresponding goal) | Each dish‑retrieval method is a concrete task that satisfies its goal. |

---

### Key Design Decisions & Justifications

| Decision | Reasoning |
|----------|-----------|
| **Depth‑first numbering** | Follows the required convention, ensuring unique IDs and clear hierarchy. |
| **Fallback for G3** | The mission description explicitly states that if one delivery method fails, another should be attempted. |
| **Parallel vs Sequential** | The overall mission is sequential: first decide method, then deliver. Within a delivery method, tasks are performed in sequence (e.g., open door → indicate meal → track retrieval). |
| **OR decomposition for dish retrieval** | Multiple ways to retrieve dishes are acceptable; any one suffices. |
| **AND decomposition for assistance steps** | All assistance steps (door opening, meal indication, tracking, alerting, dish retrieval) must happen together for a successful patient fetch. |
| **Query goals for patient/caretaker info** | The robot needs to know patient capability and available help before deciding on the delivery method. |
| **Task location “hospital” for queries** | Queries are performed by accessing hospital records or scheduling systems, which are considered part of the hospital infrastructure. |
| **Number of robots for dish retrieval with two robots** | Explicitly requires two robots; thus the range `[2,2]`. |
| **Single robot for all other tasks** | The mission description does not indicate need for multiple robots except for dish retrieval. |

---

**End of Goal Model**
