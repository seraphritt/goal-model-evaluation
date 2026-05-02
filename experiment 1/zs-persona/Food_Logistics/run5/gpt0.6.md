**Goal Model – Multi‑Robot Food Delivery System**

---

### 1. Goal Table  

| Name                                 | Text                                                                                                                                                                | Runtime | Goal Type | Target Condition / Enquired Information                                                       | Relation | Ground truth I                                        | Ground truth C                      | Consensus                                             |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------- | --------------------------------------------------------------------------------------------- | -------- | ----------------------------------------------------- | ----------------------------------- | ----------------------------------------------------- |
| **G1** – Food Delivery Cycle         | Achieve delivery of requested meals to inpatient rooms and completion of all related tasks (retrieval, dish cleaning, door opening).                                | `;`     | Achieve   | All requested meals delivered, correct meals retrieved, dishes cleaned, door opened.          | –        | Perform                                               | Perform                             | Perform                                               |
| **G1.1** – Retrieve Capability       | Query the system whether the patient can retrieve food from the tray, whether a companion/nurse is present, and whether the robot can manipulate food onto a table. | `-`     | Query     | Availability of patient/companion/nurse/robot retrieval options and robot manipulation skill. | AND      | OK                                                    | OK                                  | OK                                                    |
| **G1.2** – Deliver Food              | Perform the delivery of food to the patient.                                                                                                                        | `OR`    | Perform   | –                                                                                             | AND      | Achieve. Target condition: all food was delivered.    | Achieve: All patients received food | Achieve. Target condition: all food was delivered.    |
| **G1.2.1** – Table Delivery          | Deliver the food directly onto the patient’s table.                                                                                                                 | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.2.2** – Tray Retrieval          | Fetch the food from the robot’s tray with cooperation.                                                                                                              | `OR`    | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.2.2.1** – Fetch with Patient    | Fetch the food from the tray with the patient’s cooperation.                                                                                                        | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.2.2.2** – Fetch with Companion  | Fetch the food from the tray with a companion’s cooperation.                                                                                                        | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.2.2.3** – Fetch with Nurse      | Fetch the food from the tray with a nurse’s cooperation.                                                                                                            | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.2.2.4** – Fetch with Robot      | Fetch the food from the tray with another robot’s cooperation.                                                                                                      | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.3** – Meal-Retrieval Monitoring | Monitor that the correct meal is retrieved by the patient and alert if a wrong meal is taken.                                                                       | `AND`   | Perform   | –                                                                                             | AND      | OK                                                    | OK                                  | OK                                                    |
| **G1.3.1** – Indicate Meal           | Inform the patient which meal to retrieve.                                                                                                                          | `-`     | Perform   | –                                                                                             | AND      | OK                                                    | OK                                  | OK                                                    |
| **G1.3.2** – Monitor Retrieval       | Observe the patient’s retrieval action.                                                                                                                             | `-`     | Perform   | –                                                                                             | AND      | OK                                                    | OK                                  | OK                                                    |
| **G1.3.3** – Alert Wrong Meal        | Notify the system if the retrieved meal does not match the order.                                                                                                   | `-`     | Perform   | –                                                                                             | AND      | OK                                                    | OK                                  | OK                                                    |
| **G1.4** – Dish Retrieval            | Retrieve dirty dishes from the room.                                                                                                                                | `OR`    | Perform   | –                                                                                             | AND      | Achieve. Target condition: all dishes were retrieved. | OK                                  | Achieve. Target condition: all dishes were retrieved. |
| **G1.4.1** – Unassisted Retrieval    | Robot retrieves dishes alone.                                                                                                                                       | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.4.2** – Robot Cooperation       | Two robots cooperate to retrieve dishes.                                                                                                                            | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.4.3** – Human Cooperation       | Robot cooperates with a human to retrieve dishes.                                                                                                                   | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.5** – Door Opening              | Open the patient room door.                                                                                                                                         | `OR`    | Perform   | –                                                                                             | AND      | OK                                                    | OK                                  | OK                                                    |
| **G1.5.1** – Robot Opens Door        | Robot opens the door.                                                                                                                                               | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |
| **G1.5.2** – Human Opens Door        | Human opens the door.                                                                                                                                               | `-`     | Perform   | –                                                                                             | OR       | OK                                                    | OK                                  | OK                                                    |


---

### 2. Task Table  

| Name | Text | Relation | Location | Number of Robots |
|------|------|----------|----------|------------------|
| **AT1** – Deliver to Table | Robot places the food on the patient’s table. | AND | Patient room table | 1 |
| **AT2a** – Fetch with Patient | Robot fetches food from its tray with patient’s help. | AND | Patient room | 1 |
| **AT2b** – Fetch with Companion | Robot fetches food from its tray with companion’s help. | AND | Patient room | 1 |
| **AT2c** – Fetch with Nurse | Robot fetches food from its tray with nurse’s help. | AND | Patient room | 1 |
| **AT2d** – Fetch with Robot | Two robots cooperate to fetch food from the tray. | AND | Patient room | 2 |
| **AT3** – Indicate Meal | Robot informs patient which meal to retrieve. | AND | Patient room | 1 |
| **AT4** – Monitor Retrieval | Robot observes the patient’s meal‑retrieval action. | AND | Patient room | 1 |
| **AT5** – Alert Wrong Meal | Robot alerts if patient takes the wrong meal. | AND | Patient room | 1 |
| **AT6** – Unassisted Dish Retrieval | Robot cleans dishes alone. | AND | Patient room | 1 |
| **AT7** – Robot Cooperation Dish Retrieval | Two robots cooperate to clean dishes. | AND | Patient room | 2 |
| **AT8** – Human Cooperation Dish Retrieval | Robot cooperates with a human to clean dishes. | AND | Patient room | 1 robot + 1 human |
| **AT9** – Robot Opens Door | Robot opens the patient room door. | AND | Room door | 1 |
| **AT10** – Human Opens Door | Human opens the patient room door. | AND | Room door | 1 robot + 1 human |

---

### 3. Summary Table (Goals + Tasks)

| ID | Type | Title |
|----|------|-------|
| **G1** | Goal (Achieve) | Food Delivery Cycle |
| **G1.1** | Goal (Query) | Retrieve Capability |
| **G1.2** | Goal (Perform) | Deliver Food |
| **G1.2.1** | Goal (Perform) | Table Delivery |
| **G1.2.2** | Goal (Perform) | Tray Retrieval |
| **G1.2.2.1** | Goal (Perform) | Fetch with Patient |
| **G1.2.2.2** | Goal (Perform) | Fetch with Companion |
| **G1.2.2.3** | Goal (Perform) | Fetch with Nurse |
| **G1.2.2.4** | Goal (Perform) | Fetch with Robot |
| **G1.3** | Goal (Perform) | Meal‑Retrieval Monitoring |
| **G1.3.1** | Goal (Perform) | Indicate Meal |
| **G1.3.2** | Goal (Perform) | Monitor Retrieval |
| **G1.3.3** | Goal (Perform) | Alert Wrong Meal |
| **G1.4** | Goal (Perform) | Dish Retrieval |
| **G1.4.1** | Goal (Perform) | Unassisted Retrieval |
| **G1.4.2** | Goal (Perform) | Robot Cooperation |
| **G1.4.3** | Goal (Perform) | Human Cooperation |
| **G1.5** | Goal (Perform) | Door Opening |
| **G1.5.1** | Goal (Perform) | Robot Opens Door |
| **G1.5.2** | Goal (Perform) | Human Opens Door |
| **AT1** | Task | Deliver to Table |
| **AT2a** | Task | Fetch with Patient |
| **AT2b** | Task | Fetch with Companion |
| **AT2c** | Task | Fetch with Nurse |
| **AT2d** | Task | Fetch with Robot |
| **AT3** | Task | Indicate Meal |
| **AT4** | Task | Monitor Retrieval |
| **AT5** | Task | Alert Wrong Meal |
| **AT6** | Task | Unassisted Dish Retrieval |
| **AT7** | Task | Robot Cooperation Dish Retrieval |
| **AT8** | Task | Human Cooperation Dish Retrieval |
| **AT9** | Task | Robot Opens Door |
| **AT10** | Task | Human Opens Door |

---

### 4. Logical Relationships  

```
G1 -> G1.1, G1.2, G1.3, G1.4, G1.5   [AND][;]

G1.2 -> G1.2.1, G1.2.2                [OR][OR]

G1.2.2 -> G1.2.2.1, G1.2.2.2, G1.2.2.3, G1.2.2.4   [OR][OR]

G1.3 -> G1.3.1, G1.3.2, G1.3.3   [AND][&]

G1.4 -> G1.4.1, G1.4.2, G1.4.3   [OR][OR]

G1.5 -> G1.5.1, G1.5.2   [OR][OR]

G1.2.1 -> AT1   [AND]
G1.2.2.1 -> AT2a   [AND]
G1.2.2.2 -> AT2b   [AND]
G1.2.2.3 -> AT2c   [AND]
G1.2.2.4 -> AT2d   [AND]
G1.3.1 -> AT3   [AND]
G1.3.2 -> AT4   [AND]
G1.3.3 -> AT5   [AND]
G1.4.1 -> AT6   [AND]
G1.4.2 -> AT7   [AND]
G1.4.3 -> AT8   [AND]
G1.5.1 -> AT9   [AND]
G1.5.2 -> AT10  [AND]
```

*All relations marked `AND` indicate that the child must be satisfied for the parent to succeed.  
All `OR` relations indicate a fallback or alternative path.*
