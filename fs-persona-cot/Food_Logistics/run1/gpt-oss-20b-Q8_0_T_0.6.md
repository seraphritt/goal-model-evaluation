**Goal‑Model – Multi‑Robot Food Delivery**

| **Name**                                      | **Text**                                                                                                                                         | **Runtime**                          | **Goal Type** | **Target Condition / Enquired Info**                            | **Relation**             | **Justification**                                                                                                                                                                                                                                                                                   | **Ground truth I**                                   | **Ground truth C** | **Ground truth E** |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ | ------------- | --------------------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ------------------ |
| **G1 Deliver Food to Inpatient Room**         | Achieve that food from the kitchen is delivered to the inpatient’s room, either placed on the table or placed in the tray for patient retrieval. | ;                                    | Achieve       | Food is delivered to patient (on table or retrieved from tray). | AND (with G2-G13)        | The root objective is only satisfied after all sub-processes (order retrieval, transport, delivery, assistance, dish retrieval, door opening, and the required queries) have been successfully completed, and the sequence is important (e.g., you cannot open the door before the robot is ready). | OK                                                   |  Ok                  |                    |
| **G2 Retrieve Order from Kitchen**            | Perform the action of fetching the requested meal(s) from the kitchen.                                                                           | -                                    | Perform       | –                                                               | AND (with AT1)           | This is a concrete, atomic action that must be executed; the goal succeeds as soon as the robot has picked up the meal(s).                                                                                                                                                                          | Query. Enqueried information: meals requested.       |  Ok                  |                    |
| **G3 Transport to Room**                      | Perform the action of moving from the kitchen to the patient’s room.                                                                             | -                                    | Perform       | –                                                               | AND (with AT2)           | A simple movement task that must finish before delivery can start.                                                                                                                                                                                                                                  | OK                                                   |  Ok                  |                    |
| **G4 Deliver to Room**                        | Deliver the food to the patient’s room, choosing the appropriate mode of delivery.                                                               | FALLBACK(G4.1, G4.2)                 | Perform       | –                                                               | OR (between G4.1 & G4.2) | The robot first attempts the preferred “table delivery” (G4.1). If that fails (e.g., table is occupied or manipulation skill unavailable), it falls back to “tray delivery” (G4.2).                                                                                                                 | Achieve. Target condition: all food was delivered    |  Ok                  |                    |
| **G4.1 Deliver to Table**                     | Deliver the food onto the patient’s table using the robot’s manipulation skill.                                                                  | -                                    | Perform       | –                                                               | AND (with AT3)           | Requires a specialised manipulation skill; the goal is achieved when the meal is placed on the table.                                                                                                                                                                                               | OK                                                   |  Ok                  |                    |
| **G4.2 Deliver to Tray**                      | Deliver the food onto the patient’s tray for later retrieval.                                                                                    | -                                    | Perform       | –                                                               | AND (with AT4)           | If table delivery is impossible, the meal is placed on the tray.                                                                                                                                                                                                                                    | OK                                                   |  Ok                  |                    |
| **G5 Assist Retrieval**                       | Assist the patient (or a helper) in retrieving the meal from the tray.                                                                           | FALLBACK(FALLBACK(G5.1, G5.2), G5.3) | Perform       | –                                                               | OR (between G5.1-G5.3)   | The robot first tries to let the patient retrieve the meal (G5.1). If the patient cannot (e.g., physically unable), it falls back to a companion (G5.2). If no companion is present, it falls back to a nurse (G5.3).                                                                               | OK                                                   |  Ok                  |                    |
| **G5.1 Patient Retrieval**                    | Let the patient retrieve the meal directly from the tray.                                                                                        | -                                    | Perform       | –                                                               | AND (with AT5)           | Requires the patient to be able to reach the tray.                                                                                                                                                                                                                                                  | OK                                                   |  Ok                  |                    |
| **G5.2 Companion Retrieval**                  | Let a companion retrieve the meal from the tray.                                                                                                 | -                                    | Perform       | –                                                               | AND (with AT5)           | Companion must be present; the robot merely indicates which meal to take.                                                                                                                                                                                                                           | OK                                                   |  Ok                  |                    |
| **G5.3 Nurse Retrieval**                      | Let a nurse retrieve the meal from the tray.                                                                                                     | -                                    | Perform       | –                                                               | AND (with AT5)           | Nurse is the last resort if neither patient nor companion can retrieve.                                                                                                                                                                                                                             | OK                                                   |  Ok                  |                    |
| **G6 Dish Retrieval**                         | Retrieve dirty dishes from the patient’s room.                                                                                                   | FALLBACK(FALLBACK(G6.1, G6.2), G6.3) | Perform       | –                                                               | OR (between G6.1-G6.3)   | The robot first tries to do it alone (G6.1). If that fails (e.g., dish too heavy), it falls back to robot-cooperation (G6.2). If still impossible, it falls back to human-assistance (G6.3).                                                                                                        | Achieve. Target condition: all dishes were retrieved |  Ok                  |                    |
| **G6.1 Retrieve Dish Unassisted**             | Pick up and bring the dish to the kitchen without help.                                                                                          | -                                    | Perform       | –                                                               | AND (with AT8)           | Simple action; succeeds when the dish is carried away.                                                                                                                                                                                                                                              | OK                                                   |  Ok                  |                    |
| **G6.2 Retrieve Dish with Robot Cooperation** | Two robots cooperate to pick up a dish that is too heavy for one.                                                                                | -                                    | Perform       | –                                                               | AND (with AT9)           | Requires two robots; succeeds when both coordinate to move the dish.                                                                                                                                                                                                                                | OK                                                   |  Ok                  |                    |
| **G6.3 Retrieve Dish with Human Cooperation** | Robot and a human cooperate to pick up a dish.                                                                                                   | -                                    | Perform       | –                                                               | AND (with AT10)          | Human must provide extra strength; goal succeeds when the dish is moved.                                                                                                                                                                                                                            | OK                                                   |  Ok                  |                    |
| **G7 Open Door**                              | Open the patient room door so the robot can enter or exit.                                                                                       | FALLBACK(FALLBACK(G7.1, G7.2), G7.3) | Perform       | –                                                               | OR (between G7.1-G7.3)   | The robot first attempts to open the door alone (G7.1). If that fails (door locked, too heavy), it falls back to human help (G7.2). If no human is present, it falls back to a second robot’s assistance (G7.3).                                                                                    |                                                      |  Ok                  |                    |
| **G7.1 Open Door Robot Alone**                | Robot uses its door-opening mechanism to open the door.                                                                                          | -                                    | Perform       | –                                                               | AND (with AT11)          | Simple action; succeeds when the door is opened.                                                                                                                                                                                                                                                    | Ok                                                   |  Ok                  |                    |
| **G7.2 Open Door with Human**                 | Human opens the door while the robot approaches.                                                                                                 | -                                    | Perform       | –                                                               | AND (with AT12)          | Requires human presence; goal succeeds when door is opened.                                                                                                                                                                                                                                         | OK                                                   |  Ok                  |                    |
| **G7.3 Open Door with Robot**                 | Two robots cooperate to open a heavy door.                                                                                                       | -                                    | Perform       | –                                                               | AND (with AT13)          | Requires coordination of two robots; succeeds when door is opened.                                                                                                                                                                                                                                  | OK                                                   |  Ok                  |                    |
| **G8 Query Patient Retrieval Capability**     | Query the patient record to decide whether the patient can retrieve the meal from the tray.                                                      | -                                    | Query         | Boolean: `canRetrieve`                                          | AND (with AT15)          | The robot needs this information to decide whether to fall back to assistance.                                                                                                                                                                                                                      | OK                                                   |  Ok                  |                    |
| **G9 Query Companion Presence**               | Query the patient record or room sensors to determine if a companion is present.                                                                 | -                                    | Query         | Boolean: `companionPresent`                                     | AND (with AT16)          | Needed to decide whether companion assistance is possible.                                                                                                                                                                                                                                          | ok                                                   |  Ok                  |                    |
| **G10 Query Nurse Availability**              | Query the nurse scheduling system to see if a nurse can assist.                                                                                  | -                                    | Query         | Boolean: `nurseAvailable`                                       | AND (with AT17)          | Needed to decide whether nurse assistance is possible.                                                                                                                                                                                                                                              | OK                                                   |  Ok                  |                    |
| **G11 Query Door State**                      | Query the door sensor to check if the door is already open.                                                                                      | -                                    | Query         | Boolean: `doorOpen`                                             | AND (with AT18)          | Allows the robot to skip opening if the door is already open.                                                                                                                                                                                                                                       | OK                                                   |  Ok                  |                    |
| **G12 Query Tray Status**                     | Query the robot’s tray to know how many meals are on it.                                                                                         | -                                    | Query         | Integer: `trayCount`                                            | AND (with AT19)          | Needed to indicate which meal the patient should pick up.                                                                                                                                                                                                                                           | OK                                                   |  Ok                  |                    |
| **G13 Query Dirty Dishes**                    | Query the room to detect if there are dirty dishes to be removed.                                                                                | -                                    | Query         | Boolean: `dirtyDishesPresent`                                   | AND (with AT20)          | Determines whether dish-retrieval sub-tasks must be executed.                                                                                                                                                                                                                                       | OK                                                   |  Ok                  |                    |


---

### Task‑Model (Leaf Actions)

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1 Fetch Order** | Robot picks up the meal(s) from the kitchen counter. | AND (with G2) | kitchen | 1 | Only one robot is needed to fetch a meal; no cooperation required. |
| **AT2 Move to Room** | Robot traverses the hallway to the patient’s room. | AND (with G3) | hallway → room | 1 | Straight‑forward movement; single robot suffices. |
| **AT3 Deliver to Table** | Robot places the meal onto the patient’s table using its manipulation skill. | AND (with G4.1) | patient room | 1 | Requires the robot’s manipulation capability; no other robot needed. |
| **AT4 Deliver to Tray** | Robot places the meal onto the patient’s tray. | AND (with G4.2) | patient room | 1 | Simple placement; no additional resources. |
| **AT5 Indicate Meal** | Robot signals to the patient (or helper) which meal to pick up. | AND (with G5.1‑G5.3) | patient room | 1 | The robot must communicate the correct meal; no extra robots. |
| **AT6 Track Meal Retrieval** | Robot logs the time and location of the meal’s retrieval. | AND (with G5.1‑G5.3) | patient room | 1 | Monitoring task; single robot can log data. |
| **AT7 Alert Wrong Meal** | Robot notifies staff if the wrong meal is retrieved. | AND (with G5.1‑G5.3) | patient room | 1 | Simple alert; no cooperation needed. |
| **AT8 Retrieve Dish Unassisted** | Robot picks up a dish and carries it to the kitchen. | AND (with G6.1) | patient room | 1 | Dish small enough for one robot. |
| **AT9 Retrieve Dish with Robot Cooperation** | Two robots coordinate to lift a heavy dish. | AND (with G6.2) | patient room | [2,2] | Dish too heavy for a single robot; requires two robots. |
| **AT10 Retrieve Dish with Human Cooperation** | Robot and a human lift a dish together. | AND (with G6.3) | patient room | 1 | Human provides additional strength; robot alone insufficient. |
| **AT11 Open Door Robot Alone** | Robot uses its door‑opening mechanism to open the door. | AND (with G7.1) | room door | 1 | Robot has built‑in door‑opening tool. |
| **AT12 Open Door with Human** | Human opens the door while robot approaches. | AND (with G7.2) | room door | 1 | Human needed if robot cannot open alone. |
| **AT13 Open Door with Robot** | Two robots coordinate to open a heavy door. | AND (with G7.3) | room door | [2,2] | Door too heavy for one robot; requires cooperation. |
| **AT14 Wait for Human Signal** | Robot waits for a human to signal that the door can be opened. | AND (with G7.2) | room door | 1 | Human must indicate readiness; robot waits. |
| **AT15 Query Patient Retrieval Capability** | Robot reads patient record to check retrieval ability. | AND (with G8) | patient record system | 1 | Needed to decide if assistance is required. |
| **AT16 Query Companion Presence** | Robot checks room sensors or record for a companion. | AND (with G9) | room sensors / record | 1 | Determines if companion can help. |
| **AT17 Query Nurse Availability** | Robot queries the nurse scheduling system. | AND (with G10) | nurse schedule system | 1 | Needed to decide if nurse can assist. |
| **AT18 Query Door State** | Robot reads the door sensor to check if the door is open. | AND (with G11) | door sensor | 1 | Allows robot to skip opening if already open. |
| **AT19 Query Tray Status** | Robot checks its tray for the number of meals. | AND (with G12) | robot tray | 1 | Needed to inform patient which meal to take. |
| **AT20 Query Dirty Dishes** | Robot checks the room for dirty dishes. | AND (with G13) | patient room | 1 | Determines if dish‑retrieval sub‑tasks must run. |

---

### Summary Table (Goals & Tasks)

| **Goal/Task ID** | **Title** | **Type** | **Runtime / Relation** | **Justification** |
|------------------|-----------|----------|------------------------|-------------------|
| G1 | Deliver Food to Inpatient Room | Achieve | ; (AND with G2‑G13) | Sequential completion of all sub‑processes is required. |
| G2 | Retrieve Order from Kitchen | Perform | - (AND with AT1) | Atomic action. |
| G3 | Transport to Room | Perform | - (AND with AT2) | Atomic action. |
| G4 | Deliver to Room | Perform | FALLBACK(G4.1,G4.2) (OR) | Prefer table delivery; fallback to tray. |
| G4.1 | Deliver to Table | Perform | - (AND with AT3) | Requires manipulation skill. |
| G4.2 | Deliver to Tray | Perform | - (AND with AT4) | Alternative when table delivery fails. |
| G5 | Assist Retrieval | Perform | FALLBACK(FALLBACK(G5.1,G5.2),G5.3) (OR) | Patient → Companion → Nurse fallback. |
| G5.1 | Patient Retrieval | Perform | - (AND with AT5) | Patient may retrieve directly. |
| G5.2 | Companion Retrieval | Perform | - (AND with AT5) | Companion can help. |
| G5.3 | Nurse Retrieval | Perform | - (AND with AT5) | Nurse as last resort. |
| G6 | Dish Retrieval | Perform | FALLBACK(FALLBACK(G6.1,G6.2),G6.3) (OR) | Unassisted → Robot‑cooperation → Human‑cooperation. |
| G6.1 | Retrieve Dish Unassisted | Perform | - (AND with AT8) | Small dish. |
| G6.2 | Retrieve Dish with Robot Cooperation | Perform | - (AND with AT9) | Heavy dish. |
| G6.3 | Retrieve Dish with Human Cooperation | Perform | - (AND with AT10) | Human needed. |
| G7 | Open Door | Perform | FALLBACK(FALLBACK(G7.1,G7.2),G7.3) (OR) | Robot alone → Human help → Robot‑cooperation. |
| G7.1 | Open Door Robot Alone | Perform | - (AND with AT11) | Built‑in mechanism. |
| G7.2 | Open Door with Human | Perform | - (AND with AT12) | Human needed. |
| G7.3 | Open Door with Robot | Perform | - (AND with AT13) | Heavy door. |
| G8 | Query Patient Retrieval Capability | Query | - (AND with AT15) | Needed for decision tree. |
| G9 | Query Companion Presence | Query | - (AND with AT16) | Needed for decision tree. |
| G10 | Query Nurse Availability | Query | - (AND with AT17) | Needed for decision tree. |
| G11 | Query Door State | Query | - (AND with AT18) | Skip opening if already open. |
| G12 | Query Tray Status | Query | - (AND with AT19) | Identify correct meal. |
| G13 | Query Dirty Dishes | Query | - (AND with AT20) | Trigger dish retrieval. |
| AT1 | Fetch Order | – | – | One robot fetches meal. |
| AT2 | Move to Room | – | – | Single robot movement. |
| AT3 | Deliver to Table | – | – | Manipulation skill required. |
| AT4 | Deliver to Tray | – | – | Simple placement. |
| AT5 | Indicate Meal | – | – | Communication needed. |
| AT6 | Track Meal Retrieval | – | – | Logging. |
| AT7 | Alert Wrong Meal | – | – | Notification. |
| AT8 | Retrieve Dish Unassisted | – | – | Small dish. |
| AT9 | Retrieve Dish with Robot Cooperation | – | – | Two robots needed. |
| AT10 | Retrieve Dish with Human Cooperation | – | – | Human needed. |
| AT11 | Open Door Robot Alone | – | – | Built‑in tool. |
| AT12 | Open Door with Human | – | – | Human opens. |
| AT13 | Open Door with Robot | – | – | Two robots needed. |
| AT14 | Wait for Human Signal | – | – | Human must signal. |
| AT15 | Query Patient Retrieval Capability | – | – | Read patient record. |
| AT16 | Query Companion Presence | – | – | Check sensors/record. |
| AT17 | Query Nurse Availability | – | – | Check schedule. |
| AT18 | Query Door State | – | – | Read sensor. |
| AT19 | Query Tray Status | – | – | Check robot tray. |
| AT20 | Query Dirty Dishes | – | – | Check room. |

---

### Logical Relationships (Tree Structure)

1. **G1 → G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13**  
   **Relation:** AND, Runtime: ;  
   **Justification:** The root goal requires that all sub‑tasks (order retrieval, transport, delivery, assistance, dish retrieval, door opening, and the necessary queries) are completed in order to successfully deliver food.

2. **G4 → G4.1, G4.2**  
   **Relation:** OR, Runtime: FALLBACK(G4.1, G4.2)  
   **Justification:** The robot first tries to deliver to the table; if that fails, it falls back to delivering to the tray.

3. **G5 → G5.1, G5.2, G5.3**  
   **Relation:** OR, Runtime: FALLBACK(FALLBACK(G5.1, G5.2), G5.3)  
   **Justification:** Patient attempts first; if unable, companion is tried; if still unavailable, nurse is used.

4. **G6 → G6.1, G6.2, G6.3**  
   **Relation:** OR, Runtime: FALLBACK(FALLBACK(G6.1, G6.2), G6.3)  
   **Justification:** Unassisted first; if fails, robot cooperation; if fails, human cooperation.

5. **G7 → G7.1, G7.2, G7.3**  
   **Relation:** OR, Runtime: FALLBACK(FALLBACK(G7.1, G7.2), G7.3)  
   **Justification:** Robot alone first; if not possible, human help; if not available, robot cooperation.

6. **Each leaf goal (G2–G13) → corresponding task (AT1–AT20)**  
   **Relation:** AND  
   **Justification:** A leaf goal is achieved only when its single task is successfully executed.

7. **G8, G9, G10, G11, G12, G13** (queries) → their tasks (AT15–AT20)  
   **Relation:** AND  
   **Justification:** Query goals are satisfied once the robot obtains the required information.

---

**Why this structure?**  
- **Sequential flow** (G1’s `;`) matches the real‑world process: you cannot open the door before the robot is ready, and you cannot deliver a meal before it has been retrieved and transported.  
- **Fallbacks** capture the uncertainty in the environment (patient ability, door state, dish weight, etc.) and provide a clear decision tree.  
- **OR decompositions** allow the system to choose the most suitable action when multiple options exist.  
- **AND decompositions** ensure that all necessary sub‑tasks (e.g., fetching the order, moving to the room, and delivering) are completed before proceeding.  
- **Task attributes** (location, number of robots) are derived directly from the mission description: e.g., dish retrieval might need two robots, while most tasks are single‑robot operations.  

This goal‑model gives a clear, formal blueprint for the multi‑robot system, enabling planners, schedulers, and verification tools to reason about task allocation, sequencing, and fallback strategies.
