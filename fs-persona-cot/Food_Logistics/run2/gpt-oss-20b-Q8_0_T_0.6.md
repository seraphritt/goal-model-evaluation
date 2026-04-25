**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

| **Name**   | **Text**                                                    | **Runtime**                        | **Goal Type** | **Target Condition / Enquired Information**                                            | **Relation**         | **Justification**                                                                                                                              | **Ground truth I**                                   | **Ground truth C** | **Ground truth E** |
| ---------- | ----------------------------------------------------------- | ---------------------------------- | ------------- | -------------------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ------------------ |
| **G1**     | Support Inpatient Care via Food Delivery and Dish Retrieval | `#`                                | Achieve       | “All requested meals delivered to patients and all dishes cleaned from patient rooms.” | –                    | Food delivery and dish retrieval are independent activities that can be carried out concurrently; parallel execution maximises throughput.     | Perform                                              |  Perform                  |                    |
| **G2**     | Deliver Food to Inpatient Room                              | `AND`                              | Perform       | –                                                                                      | `AND`                | Both the capability query and the choice of delivery mode must be satisfied before the delivery can succeed.                                   | Achieve. Target condition: all food was delivered    |  Ok                  |                    |
| **G2.1**   | Query Patient Fetch Capability                              | `-`                                | Query         | “Whether patient, companion or nurse can retrieve food from the tray.”                 | `AND` (to G2)        | The system must know the fetch-capability before deciding the delivery mode.                                                                   | OK                                                   |  Ok                  |                    |
| **G2.4**   | Choose Delivery Mode                                        | `FALLBACK(G2.2, G2.3)`             | Perform       | –                                                                                      | `AND` (to G2)        | After the capability has been queried, the system attempts the preferred mode (patient fetch). If that fails, it falls back to table delivery. | OK                                                   |  Ok                  |                    |
| **G2.2**   | Deliver to Table                                            | `-`                                | Perform       | –                                                                                      | `FALLBACK` (to G2.4) | Direct table delivery is the default when patient fetch is not possible.                                                                       | OK                                                   |  Ok                  |                    |
| **G2.3**   | Patient Fetch Meal                                          | `-`                                | Perform       | –                                                                                      | `FALLBACK` (to G2.4) | Patient fetch is attempted when the patient (or companion/nurse) is capable of retrieving the meal.                                            | OK                                                   |  Ok                  |                    |
| **G3**     | Retrieve Dirty Dishes from Inpatient Room                   | `AND`                              | Perform       | –                                                                                      | `AND` (to G1)        | Dish retrieval must be combined with door opening; both are required for the goal.                                                             | OK                                                   |  Ok                  |                    |
| **G3.4**   | Open Room Door                                              | `FALLBACK(G3.4.1, G3.4.2)`         | Perform       | –                                                                                      | `AND` (to G3)        | Door opening can be performed by a robot or a human; the system falls back to the available option.                                            | OK                                                   |  Ok                  |                    |
| **G3.4.1** | Robot Opens Door                                            | `-`                                | Perform       | –                                                                                      | `FALLBACK` (to G3.4) | Robot-initiated door opening is preferred when available.                                                                                      | OK                                                   |  Ok                  |                    |
| **G3.4.2** | Human Opens Door                                            | `-`                                | Perform       | –                                                                                      | `FALLBACK` (to G3.4) | Human door opening is used when the robot cannot open the door.                                                                                | OK                                                   |  Ok                  |                    |
| **G3.5**   | Retrieve Dishes                                             | `FALLBACK(G3.5.1, G3.5.2, G3.5.3)` | Perform       | –                                                                                      | `AND` (to G3)        | Three mutually exclusive retrieval strategies are available; the system tries them in order of preference.                                     | Achieve. Target condition: all dishes were retrieved |  Ok                  |                    |
| **G3.5.1** | Retrieve Unassisted                                         | `-`                                | Perform       | –                                                                                      | `FALLBACK` (to G3.5) | The robot can retrieve dishes alone if it has the necessary manipulator.                                                                       | OK                                                   |  Ok                  |                    |
| **G3.5.2** | Retrieve with Two Robots                                    | `-`                                | Perform       | –                                                                                      | `FALLBACK` (to G3.5) | Two robots cooperate when a single robot’s payload is insufficient.                                                                            | OK                                                   |  Ok                  |                    |
| **G3.5.3** | Retrieve with Human                                         | `-`                                | Perform       | –                                                                                      | `FALLBACK` (to G3.5) | Human assistance is used when the robot cannot retrieve the dishes alone.                                                                      | OK                                                   |  Ok                  |                    |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|---|---|---|---|---|---|
| **AT1** | Navigate to the patient room for delivery | `AND` (to G2.2) | patient_room | 1 | Robot must physically reach the room to deliver food. |
| **AT2** | Manipulate food onto the patient’s table | `AND` (to G2.2) | patient_room | 1 | Requires the robot’s manipulation skill. |
| **AT3** | Confirm delivery to the patient | `AND` (to G2.2) | patient_room | 1 | Robot verifies that food has been placed correctly. |
| **AT4** | Wait for patient to fetch meal | `AND` (to G2.3) | patient_room | 1 | Robot must remain present until the patient picks up. |
| **AT5** | Display meal identifier for patient | `AND` (to G2.3) | patient_room | 1 | Helps the patient identify the correct meal. |
| **AT6** | Monitor patient’s retrieval action | `AND` (to G2.3) | patient_room | 1 | Robot detects whether the correct meal was taken. |
| **AT19** | Record meal retrieval timestamp and location | `AND` (to G2.3) | hospital | 1 | Maintains audit trail for each meal. |
| **AT20** | Alert if wrong meal retrieved | `AND` (to G2.3) | patient_room | 1 | Ensures patient receives correct food. |
| **AT7** | Robot opens the room door | `AND` (to G3.4.1) | room_door | 1 | Robot performs door opening when available. |
| **AT8** | Human opens the room door | `AND` (to G3.4.2) | room_door | 0 | Human action; robot not required. |
| **AT9** | Navigate to the patient room for dish retrieval | `AND` (to G3.5.1) | patient_room | 1 | Robot must reach the room to pick up dishes. |
| **AT10** | Pick up dishes from the table | `AND` (to G3.5.1) | patient_room | 1 | Robot’s manipulator collects dishes. |
| **AT11** | Dispose dishes at waste bin | `AND` (to G3.5.1) | waste_bin | 1 | Robot transports and discards dishes. |
| **AT12** | Robot 1 navigates to the patient room | `AND` (to G3.5.2) | patient_room | 1 | First robot initiates the retrieval. |
| **AT13** | Robot 2 assists in lifting dishes | `AND` (to G3.5.2) | patient_room | 1 | Second robot provides extra payload. |
| **AT14** | Transfer dishes between robots | `AND` (to G3.5.2) | patient_room | 2 | Both robots cooperate to move dishes. |
| **AT15** | Dispose dishes at waste bin | `AND` (to G3.5.2) | waste_bin | 1 | One robot completes disposal after transfer. |
| **AT16** | Wait for human to pick up dishes | `AND` (to G3.5.3) | patient_room | 1 | Robot waits until the human arrives. |
| **AT17** | Human picks up dishes | `AND` (to G3.5.3) | patient_room | 0 | Human action; robot not required. |
| **AT18** | Robot assists human in moving dishes | `AND` (to G3.5.3) | patient_room | 1 | Robot helps the human lift or transport dishes. |

---

### Summary Table (Goals & Tasks)

| **Type** | **ID** | **Title** | **Text** | **Runtime / Relation** | **Location** | **Number of Robots** | **Justification** |
|---|---|---|---|---|---|---|---|
| **Goal** | G1 | Support Inpatient Care via Food Delivery and Dish Retrieval | All requested meals delivered to patients and all dishes cleaned from patient rooms. | `#` | – | – | Parallel execution of delivery and dish retrieval. |
| **Goal** | G2 | Deliver Food to Inpatient Room | – | `AND` | – | – | Query and delivery mode selection required. |
| **Goal** | G2.1 | Query Patient Fetch Capability | – | `-` | – | – | Determine fetch capability. |
| **Goal** | G2.4 | Choose Delivery Mode | – | `FALLBACK(G2.2, G2.3)` | – | – | Prefer patient fetch; fallback to table delivery. |
| **Goal** | G2.2 | Deliver to Table | – | `-` | – | – | Direct delivery. |
| **Goal** | G2.3 | Patient Fetch Meal | – | `-` | – | – | Patient fetch. |
| **Goal** | G3 | Retrieve Dirty Dishes from Inpatient Room | – | `AND` | – | – | Must open door first. |
| **Goal** | G3.4 | Open Room Door | – | `FALLBACK(G3.4.1, G3.4.2)` | – | – | Robot or human. |
| **Goal** | G3.4.1 | Robot Opens Door | – | `-` | – | – | Robot door opening. |
| **Goal** | G3.4.2 | Human Opens Door | – | `-` | – | – | Human door opening. |
| **Goal** | G3.5 | Retrieve Dishes | – | `FALLBACK(G3.5.1, G3.5.2, G3.5.3)` | – | – | Three retrieval strategies. |
| **Goal** | G3.5.1 | Retrieve Unassisted | – | `-` | – | – | Robot alone. |
| **Goal** | G3.5.2 | Retrieve with Two Robots | – | `-` | – | – | Two‑robot cooperation. |
| **Goal** | G3.5.3 | Retrieve with Human | – | `-` | – | – | Human assistance. |
| **Task** | AT1 | Navigate to Patient Room for Delivery | `AND` (to G2.2) | patient_room | 1 | Robot must reach room. |
| **Task** | AT2 | Manipulate Food onto Table | `AND` (to G2.2) | patient_room | 1 | Requires manipulation skill. |
| **Task** | AT3 | Confirm Delivery | `AND` (to G2.2) | patient_room | 1 | Verification step. |
| **Task** | AT4 | Wait for Patient to Fetch Meal | `AND` (to G2.3) | patient_room | 1 | Await patient. |
| **Task** | AT5 | Display Meal Identifier | `AND` (to G2.3) | patient_room | 1 | Helps patient. |
| **Task** | AT6 | Monitor Retrieval | `AND` (to G2.3) | patient_room | 1 | Detects correct meal. |
| **Task** | AT19 | Record Meal Retrieval | `AND` (to G2.3) | hospital | 1 | Audit trail. |
| **Task** | AT20 | Alert Wrong Meal | `AND` (to G2.3) | patient_room | 1 | Corrects error. |
| **Task** | AT7 | Robot Opens Door | `AND` (to G3.4.1) | room_door | 1 | Robot action. |
| **Task** | AT8 | Human Opens Door | `AND` (to G3.4.2) | room_door | 0 | Human action. |
| **Task** | AT9 | Navigate to Patient Room for Dish Retrieval | `AND` (to G3.5.1) | patient_room | 1 | Robot must reach room. |
| **Task** | AT10 | Pick Up Dishes | `AND` (to G3.5.1) | patient_room | 1 | Manipulation. |
| **Task** | AT11 | Dispose Dishes | `AND` (to G3.5.1) | waste_bin | 1 | Disposal. |
| **Task** | AT12 | Robot 1 Navigates to Room | `AND` (to G3.5.2) | patient_room | 1 | First robot. |
| **Task** | AT13 | Robot 2 Assists | `AND` (to G3.5.2) | patient_room | 1 | Second robot. |
| **Task** | AT14 | Transfer Dishes Between Robots | `AND` (to G3.5.2) | patient_room | 2 | Cooperation. |
| **Task** | AT15 | Dispose Dishes | `AND` (to G3.5.2) | waste_bin | 1 | Final disposal. |
| **Task** | AT16 | Wait for Human | `AND` (to G3.5.3) | patient_room | 1 | Await human. |
| **Task** | AT17 | Human Picks Up Dishes | `AND` (to G3.5.3) | patient_room | 0 | Human action. |
| **Task** | AT18 | Robot Assists Human | `AND` (to G3.5.3) | patient_room | 1 | Assistance. |

---

### Logical Relationships

| **Parent → Children** | **Relation** | **Justification** |
|---|---|---|
| **G1 → G2, G3** | `AND` | Both food delivery and dish retrieval must be completed to satisfy the overall care goal. |
| **G1 → G2, G3** | `#` (parallel) | Delivery and retrieval can occur concurrently; no dependency between them. |
| **G2 → G2.1, G2.4** | `AND` | The system must first know fetch capability, then decide on delivery mode. |
| **G2.1 → (none)** | – | Leaf query. |
| **G2.4 → G2.2, G2.3** | `FALLBACK(G2.2, G2.3)` | Prefer patient fetch; if not possible, deliver to table. |
| **G2.2 → (none)** | – | Leaf perform. |
| **G2.3 → (none)** | – | Leaf perform. |
| **G3 → G3.4, G3.5** | `AND` | Door must be opened before dishes can be retrieved. |
| **G3.4 → G3.4.1, G3.4.2** | `FALLBACK(G3.4.1, G3.4.2)` | Robot or human can open the door. |
| **G3.4.1 → (none)** | – | Leaf perform. |
| **G3.4.2 → (none)** | – | Leaf perform. |
| **G3.5 → G3.5.1, G3.5.2, G3.5.3** | `FALLBACK(G3.5.1, G3.5.2, G3.5.3)` | Three mutually exclusive strategies for dish retrieval. |
| **G3.5.1 → (none)** | – | Leaf perform. |
| **G3.5.2 → (none)** | – | Leaf perform. |
| **G3.5.3 → (none)** | – | Leaf perform. |
| **AT1 → G2.2** | `AND` | Task required for table delivery. |
| **AT2 → G2.2** | `AND` | Same. |
| **AT3 → G2.2** | `AND` | Same. |
| **AT4 → G2.3** | `AND` | Task required for patient fetch. |
| **AT5 → G2.3** | `AND` | Same. |
| **AT6 → G2.3** | `AND` | Same. |
| **AT19 → G2.3** | `AND` | Logging. |
| **AT20 → G2.3** | `AND` | Error handling. |
| **AT7 → G3.4.1** | `AND` | Robot door open. |
| **AT8 → G3.4.2** | `AND` | Human door open. |
| **AT9 → G3.5.1** | `AND` | Navigation for unassisted retrieval. |
| **AT10 → G3.5.1** | `AND` | Dish pickup. |
| **AT11 → G3.5.1** | `AND` | Disposal. |
| **AT12 → G3.5.2** | `AND` | Robot 1 navigation. |
| **AT13 → G3.5.2** | `AND` | Robot 2 assistance. |
| **AT14 → G3.5.2** | `AND` | Transfer between robots. |
| **AT15 → G3.5.2** | `AND` | Disposal. |
| **AT16 → G3.5.3** | `AND` | Wait for human. |
| **AT17 → G3.5.3** | `AND` | Human pickup. |
| **AT18 → G3.5.3** | `AND` | Robot assistance. |

---

**Notes on Justifications**

* **Parallel vs Sequential** – The root goal G1 is marked as parallel (`#`) because food delivery and dish retrieval are independent and can be performed concurrently, increasing overall throughput.  
* **Fallback** – The use of `FALLBACK` for G2.4, G3.4, and G3.5 captures the uncertainty in capability (patient fetch, door opening, retrieval method). The system attempts the preferred option first; if it fails (e.g., patient cannot fetch or robot cannot open door), it falls back to the next alternative.  
* **AND Decomposition** – Whenever multiple tasks or sub‑goals must all be satisfied for a parent goal to succeed (e.g., opening the door and retrieving dishes), we use `AND`.  
* **Query Goals** – G2.1 is a query goal because it simply retrieves information from the patient record; no action is performed.  
* **Perform Goals** – All other non‑query goals are perform goals because they involve actual robot actions.  

This goal model provides a clear, hierarchical, and executable representation of the multi‑robot food delivery and dish retrieval mission, explicitly handling uncertainty, cooperation, and task allocation.
