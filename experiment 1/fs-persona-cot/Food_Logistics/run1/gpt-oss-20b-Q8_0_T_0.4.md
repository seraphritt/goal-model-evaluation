**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

---

## 1. Goal Table  

| **Name**                                 | **Text**                                                                                                                             | **Runtime**        | **Goal Type** | **Enquired Information / Target Condition** | **Relation**             | **Justification**                                                                                                                                           | **Ground truth I**                                   | **Ground truth C** | **Consensus**                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ------------- | ------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ---------------------------------------------------- |
| G1: Deliver Food to Inpatient Room       | Ensure that a meal is delivered from the kitchen to the specified inpatient room, including all necessary coordination and handling. | `;` (sequential)   | Perform       | –                                           | AND (G2, G3, G10, G9)    | The mission must open the door, fetch the order, decide the delivery method, deliver the meal, and retrieve dishes – each step must finish before the next. | OK                                                   | Ok                 | OK                                                   |
| G2: Retrieve Order from Kitchen          | Obtain the current meal delivery request from the kitchen system.                                                                    | `-`                | Perform       | –                                           | AND (AT1)                | The robot must know what to deliver before any other action.                                                                                                | OK                                                   | Ok                 | OK                                                   |
| G3: Determine Delivery Method            | Decide whether to deliver the meal directly to the patient’s table or leave it on a tray for later retrieval.                        | `FALLBACK(G5, G4)` | Perform       | –                                           | AND (G3.1, G3.2)         | The robot first queries the patient record (G3.1) and then attempts tray delivery; if that fails, it falls back to table delivery (G5 → G4).                | OK                                                   | Ok                 | OK                                                   |
| G3.1: Query Patient Retrieval Capability | Retrieve information about whether the patient or a companion can retrieve the meal from the tray.                                   | `-`                | Query         | “Patient retrieval capability”              | AND (AT15)               | The robot needs this knowledge to decide whether tray delivery is feasible.                                                                                 | OK                                                   | Ok                 | OK                                                   |
| G3.2: Decide Delivery (Fallback)         | Attempt tray delivery; if not possible, fall back to table delivery.                                                                 | `FALLBACK(G5, G4)` | Perform       | –                                           | OR (G5, G4)              | The robot first tries to deliver to a tray; if that fails (e.g., no retrieval capability), it falls back to table delivery.                                 | Achieve. Target condition: all food was delivered    | Ok                 | Achieve. Target condition: all food was delivered    |
| G4: Deliver to Table                     | Place the meal on the patient’s table.                                                                                               | `-`                | Perform       | –                                           | AND (AT3)                | Direct table delivery is a single, straightforward action.                                                                                                  | PL                                                   | Ok                 | PL                                                   |
| G5: Deliver to Tray                      | Leave the meal on a tray for the patient or companion to retrieve later.                                                             | `-`                | Perform       | –                                           | AND (AT4, AT5, AT6, AT7) | Tray delivery requires placing the meal, notifying the patient, tracking retrieval, and alerting on wrong retrieval.                                        | OK                                                   | Ok                 | OK                                                   |
| G6: Notify Patient of Meal               | Inform the patient that a meal is available on the tray.                                                                             | `-`                | Perform       | –                                           | AND (AT5)                | The patient must be aware of the meal to retrieve it.                                                                                                       | OK                                                   | Ok                 | OK                                                   |
| G7: Track Meal Retrieval                 | Monitor when and which patient retrieves the meal from the tray.                                                                     | `-`                | Perform       | –                                           | AND (AT6)                | Tracking ensures correct meal distribution and accountability.                                                                                              | OK                                                   | Ok                 | OK                                                   |
| G8: Alert Wrong Meal Retrieval           | Detect and alert if a patient retrieves a meal that does not belong to them.                                                         | `-`                | Perform       | –                                           | AND (AT7)                | Prevents misdelivery and ensures patient safety.                                                                                                            | OK                                                   | Ok                 | OK                                                   |
| G9: Retrieve Dishes                      | Collect dirty dishes from the inpatient room and bring them back to the kitchen.                                                     | `-`                | Perform       | –                                           | OR (G9.1, G9.2, G9.3)    | Dish retrieval can be done unassisted, with another robot, or with a human.                                                                                 | Achieve. Target condition: all dishes were retrieved | Ok                 | Achieve. Target condition: all dishes were retrieved |
| G9.1: Retrieve Dishes Unassisted         | Robot collects dishes alone.                                                                                                         | `-`                | Perform       | –                                           | AND (AT8)                | When the robot can handle the load, it can retrieve dishes alone.                                                                                           | OK                                                   | Ok                 | OK                                                   |
| G9.2: Retrieve Dishes Robot-Robot        | Two robots cooperate to retrieve dishes.                                                                                             | `-`                | Perform       | –                                           | AND (AT9)                | For heavier loads or limited capacity, cooperation is required.                                                                                             | OK                                                   | Ok                 | OK                                                   |
| G9.3: Retrieve Dishes Robot-Human        | Robot cooperates with a human to retrieve dishes.                                                                                    | `-`                | Perform       | –                                           | AND (AT10)               | When a human is available, they can assist.                                                                                                                 | OK                                                   | Ok                 | OK                                                   |
| G10: Open Room Door                      | Open the inpatient room door to allow the robot to enter or exit.                                                                    | `-`                | Perform       | –                                           | OR (G10.1, G10.2, G10.3) | Door opening can be performed by the robot alone, with a human, or with another robot.                                                                      | OK                                                   | Ok                 | OK                                                   |
| G10.1: Open Door Robot Alone             | Robot uses its door-opening mechanism to open the door.                                                                              | `-`                | Perform       | –                                           | AND (AT11)               | The robot may be capable of opening the door by itself.                                                                                                     | OK                                                   | Ok                 | OK                                                   |
| G10.2: Open Door with Human              | Human assists the robot in opening the door.                                                                                         | `-`                | Perform       | –                                           | AND (AT12)               | If the robot cannot open the door alone, a human can help.                                                                                                  | OK                                                   | Ok                 | OK                                                   |
| G10.3: Open Door with Robot              | Two robots cooperate to open the door.                                                                                               | `-`                | Perform       | –                                           | AND (AT13)               | For heavy doors or limited strength, cooperation is needed.                                                                                                 | OK                                                   | Ok                 | OK                                                   |
| G11: Coordinate with Human               | Coordinate with a human (patient, companion, nurse) for tasks requiring human assistance.                                            | `-`                | Perform       | –                                           | AND (AT14)               | Human coordination is necessary for tasks such as door opening or dish retrieval when a human is available.                                                 | OK                                                   | Ok                 | OK                                                   |


---

## 2. Task Table  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| AT1: Retrieve Order from Kitchen | The robot queries the kitchen system to obtain the meal delivery request. | AND (G2) | kitchen | 1 | Only one robot is needed to fetch the order. |
| AT2: Decide Delivery Method | The robot decides whether to deliver to table or tray based on patient retrieval capability. | AND (G3.2) | robot’s internal decision‑making | 1 | Decision is made by the robot alone. |
| AT3: Deliver Meal to Table | The robot transports the meal to the patient’s table and places it there. | AND (G4) | inpatient room | 1 | One robot can carry a meal and place it on the table. |
| AT4: Deliver Meal to Tray | The robot places the meal on a tray in the room for later retrieval. | AND (G5) | inpatient room | 1 | One robot can carry the meal and place it on the tray. |
| AT5: Notify Patient of Meal | The robot signals or communicates to the patient that a meal is available on the tray. | AND (G6) | inpatient room | 1 | The robot can use its communication interface to notify the patient. |
| AT6: Track Meal Retrieval | The robot monitors the room to detect when a patient retrieves the meal from the tray. | AND (G7) | inpatient room | 1 | Continuous monitoring can be performed by a single robot. |
| AT7: Alert Wrong Meal Retrieval | The robot compares the retrieved meal with the intended patient and alerts if a mismatch occurs. | AND (G8) | inpatient room | 1 | The robot can perform the comparison and send an alert. |
| AT8: Retrieve Dishes Unassisted | The robot collects dirty dishes from the room and transports them to the kitchen. | AND (G9.1) | inpatient room | 1 | The robot can carry the dishes alone. |
| AT9: Retrieve Dishes Robot‑Robot | Two robots cooperate to carry and transport dishes from the room to the kitchen. | AND (G9.2) | inpatient room | [2,2] | Cooperation is needed for heavier loads. |
| AT10: Retrieve Dishes Robot‑Human | The robot works with a human to collect dishes and bring them to the kitchen. | AND (G9.3) | inpatient room | 1 | The human assists in carrying the dishes. |
| AT11: Open Door Robot Alone | The robot uses its door‑opening mechanism to open the room door. | AND (G10.1) | room door | 1 | The robot can open the door by itself. |
| AT12: Open Door with Human | A human assists the robot in opening the door. | AND (G10.2) | room door | 1 | Human assistance may be required. |
| AT13: Open Door with Robot | Two robots cooperate to open the door. | AND (G10.3) | room door | [2,2] | Cooperation may be needed for heavy doors. |
| AT14: Coordinate with Human | The robot communicates with a human to coordinate tasks such as door opening or dish retrieval. | AND (G11) | inpatient room | 1 | The robot can handle communication with a human. |
| AT15: Query Patient Retrieval Capability | The robot queries the hospital database to determine if the patient or companion can retrieve a meal from the tray. | AND (G3.1) | hospital database | 1 | The robot accesses the database to get the information. |

---

## 3. Summary Table (All Goals & Tasks)

| **ID** | **Type** | **Short Title** |
|--------|----------|-----------------|
| G1 | Goal | Deliver Food to Inpatient Room |
| G2 | Goal | Retrieve Order from Kitchen |
| G3 | Goal | Determine Delivery Method |
| G3.1 | Goal | Query Patient Retrieval Capability |
| G3.2 | Goal | Decide Delivery (Fallback) |
| G4 | Goal | Deliver to Table |
| G5 | Goal | Deliver to Tray |
| G6 | Goal | Notify Patient of Meal |
| G7 | Goal | Track Meal Retrieval |
| G8 | Goal | Alert Wrong Meal Retrieval |
| G9 | Goal | Retrieve Dishes |
| G9.1 | Goal | Retrieve Dishes Unassisted |
| G9.2 | Goal | Retrieve Dishes Robot‑Robot |
| G9.3 | Goal | Retrieve Dishes Robot‑Human |
| G10 | Goal | Open Room Door |
| G10.1 | Goal | Open Door Robot Alone |
| G10.2 | Goal | Open Door with Human |
| G10.3 | Goal | Open Door with Robot |
| G11 | Goal | Coordinate with Human |
| AT1 | Task | Retrieve Order from Kitchen |
| AT2 | Task | Decide Delivery Method |
| AT3 | Task | Deliver Meal to Table |
| AT4 | Task | Deliver Meal to Tray |
| AT5 | Task | Notify Patient of Meal |
| AT6 | Task | Track Meal Retrieval |
| AT7 | Task | Alert Wrong Meal Retrieval |
| AT8 | Task | Retrieve Dishes Unassisted |
| AT9 | Task | Retrieve Dishes Robot‑Robot |
| AT10 | Task | Retrieve Dishes Robot‑Human |
| AT11 | Task | Open Door Robot Alone |
| AT12 | Task | Open Door with Human |
| AT13 | Task | Open Door with Robot |
| AT14 | Task | Coordinate with Human |
| AT15 | Task | Query Patient Retrieval Capability |

---

## 4. Logical Relationships  

| **Parent** | **Children** | **Relation** | **Runtime** | **Justification** |
|------------|--------------|--------------|-------------|-------------------|
| G1 | G2, G3, G10, G9 | AND | `;` | The mission must complete order retrieval, decide delivery, open the door, and retrieve dishes in sequence before the overall goal succeeds. |
| G2 | AT1 | AND | `-` | The order must be fetched before any other action. |
| G3 | G3.1, G3.2 | AND | `-` | The robot must first query the patient record, then decide delivery. |
| G3.1 | AT15 | AND | `-` | The query must be performed to inform the decision. |
| G3.2 | G5, G4 | OR (fallback) | `FALLBACK(G5, G4)` | Tray delivery is attempted first; if it fails (e.g., patient cannot retrieve), table delivery is used. |
| G4 | AT3 | AND | `-` | Direct table delivery is a single action. |
| G5 | AT4, AT5, AT6, AT7 | AND | `-` | Tray delivery requires placing the meal, notifying the patient, tracking retrieval, and alerting on wrong retrieval. |
| G6 | AT5 | AND | `-` | Notification is part of tray delivery. |
| G7 | AT6 | AND | `-` | Tracking is part of tray delivery. |
| G8 | AT7 | AND | `-` | Alerting is part of tray delivery. |
| G9 | G9.1, G9.2, G9.3 | OR | `-` | Dish retrieval can be done unassisted, with another robot, or with a human. |
| G9.1 | AT8 | AND | `-` | Unassisted retrieval is a single action. |
| G9.2 | AT9 | AND | `-` | Robot‑robot cooperation is a single action. |
| G9.3 | AT10 | AND | `-` | Robot‑human cooperation is a single action. |
| G10 | G10.1, G10.2, G10.3 | OR | `-` | Door opening can be performed by the robot alone, with a human, or with another robot. |
| G10.1 | AT11 | AND | `-` | Robot‑alone opening is a single action. |
| G10.2 | AT12 | AND | `-` | Human assistance is a single action. |
| G10.3 | AT13 | AND | `-` | Robot‑robot cooperation is a single action. |
| G11 | AT14 | AND | `-` | Human coordination is a single action. |
| G3.1 | AT15 | AND | `-` | The query must be performed to inform the decision. |

---

### Final Remarks  

* **Sequential vs. Parallel** – The top‑level goal is sequential because the robot must first open the door, then fetch the order, decide the delivery method, deliver the meal, and finally retrieve dishes.  
* **Fallback** – The fallback operator is used for the delivery method decision to capture the uncertainty about the patient’s ability to retrieve the meal from a tray.  
* **OR Decompositions** – Dish retrieval and door opening are naturally OR decomposed because they can be performed in multiple ways depending on the environment and available partners.  
* **Task Allocation** – Each task is assigned to a single robot unless cooperation is explicitly required (e.g., dish retrieval with another robot or door opening with a human).  

This goal model explicitly captures the mission’s structure, the decision points, the uncertainty, and the required coordination among robots and humans.
