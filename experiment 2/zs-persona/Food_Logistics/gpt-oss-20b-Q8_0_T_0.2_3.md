**Goal Model – Multi‑Robot Food Delivery**

| **Name** | **Text** | **Runtime** | **Goal Type** | **Target Condition / Enquired Info** | **Relation** |
|----------|----------|-------------|---------------|-------------------------------------|--------------|
| **G1** – Deliver Food to Inpatient Room | Deliver a meal from the kitchen to the patient’s room (table or hand‑over). | G1.1; G1.2; G1.3; G1.4; G1.5; G1.6; G1.7; G1.8 | Achieve | Food is on the patient’s table or in the patient’s hand. | AND |
| **G1.1** – Receive Delivery Request | Receive an order‑by‑order request from the kitchen. | – | Perform | – | AND |
| **G1.2** – Transport Food to Room | Move the meal from the kitchen to the patient’s room. | – | Perform | – | AND |
| **G1.3** – Deliver Food to Patient | Deliver the meal to the patient (table or hand‑over). | FALLBACK(G1.3.1, G1.3.2) | Perform | Food placed on table or handed to patient. | AND |
| **G1.3.1** – Place Food on Table | Place the meal on the patient’s table using the robot’s manipulation skill. | – | Perform | – | AND |
| **G1.3.2** – Hand Food to Patient | Hand the meal directly to the patient, companion or nurse. | – | Perform | – | AND |
| **G1.4** – Retrieve Dishes | Remove dirty dishes from the patient’s room. | FALLBACK(FALLBACK(G1.4.1, G1.4.2), G1.4.3) | Perform | All dishes removed from the room. | AND |
| **G1.4.1** – Unassisted Retrieval | Robot retrieves dishes alone. | – | Perform | – | AND |
| **G1.4.2** – Two‑Robot Retrieval | Two robots cooperate to retrieve dishes. | – | Perform | – | AND |
| **G1.4.3** – Robot‑Human Retrieval | Robot cooperates with a human to retrieve dishes. | – | Perform | – | AND |
| **G1.5** – Open Door | Open the patient room door. | FALLBACK(G1.5.1, G1.5.2) | Perform | Door is open. | AND |
| **G1.5.1** – Robot Opens Door | Robot opens the door. | – | Perform | – | AND |
| **G1.5.2** – Human Opens Door | Human opens the door. | – | Perform | – | AND |
| **G1.6** – Determine Retrieval Method | Find out who can retrieve the meal from the tray. | G1.6.1#G1.6.2#G1.6.3 | Query | – | AND |
| **G1.6.1** – Query Patient Capability | Ask the patient record if the patient can retrieve food from the tray. | – | Query | Patient’s ability to retrieve food. | AND |
| **G1.6.2** – Query Companion Presence | Ask if a companion is present in the room. | – | Query | Companion present? | AND |
| **G1.6.3** – Query Nurse Availability | Ask if a nurse is available to help. | – | Query | Nurse available? | AND |
| **G1.7** – Track Meal Retrieval | Record when and where each meal was retrieved. | – | Perform | Retrieval logged. | AND |
| **G1.8** – Alert Wrong Meal | Notify staff if the wrong meal is taken. | – | Perform | Wrong‑meal alert triggered. | AND |

---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** – Receive Kitchen Request | Receive the delivery request from the kitchen. | AND | Kitchen | 1 |
| **AT2** – Transport Food | Move the meal from the kitchen to the patient’s room. | AND | Hallway | 1 |
| **AT3** – Place Food on Table | Place the meal on the patient’s table using manipulation skill. | AND | Patient room | 1 |
| **AT4** – Hand Food to Patient | Hand the meal to the patient, companion or nurse. | AND | Patient room | 1 |
| **AT5** – Retrieve Dishes Unassisted | Retrieve dirty dishes alone. | AND | Patient room | 1 |
| **AT6** – Retrieve Dishes with Two Robots | Retrieve dishes with two robots cooperating. | AND | Patient room | 2 |
| **AT7** – Retrieve Dishes with Robot & Human | Retrieve dishes with robot and human cooperation. | AND | Patient room | 1 |
| **AT8** – Robot Opens Door | Robot opens the patient room door. | AND | Patient room door | 1 |
| **AT9** – Human Opens Door | Human opens the patient room door. | AND | Patient room door | 0 |
| **AT10** – Query Patient Capability | Query patient record for ability to retrieve food from tray. | AND | Hospital database | 1 |
| **AT11** – Query Companion Presence | Query presence of companion in room. | AND | Patient room | 1 |
| **AT12** – Query Nurse Availability | Query nurse availability. | AND | Nurse station | 1 |
| **AT13** – Record Meal Retrieval | Log the time and location of meal retrieval. | AND | Robot memory | 1 |
| **AT14** – Alert Wrong Meal | Trigger an alert if the wrong meal is taken. | AND | Robot interface | 1 |

---

### Logical Relationships (Tree)

```
G1  -> G1.1, G1.2, G1.3, G1.4, G1.5, G1.6, G1.7, G1.8 [AND][sequential]

G1.3 -> G1.3.1, G1.3.2 [AND][FALLBACK(G1.3.1, G1.3.2)]

G1.4 -> G1.4.1, G1.4.2, G1.4.3 [AND][FALLBACK(FALLBACK(G1.4.1, G1.4.2), G1.4.3)]

G1.5 -> G1.5.1, G1.5.2 [AND][FALLBACK(G1.5.1, G1.5.2)]

G1.6 -> G1.6.1, G1.6.2, G1.6.3 [AND][parallel (G1.6.1#G1.6.2#G1.6.3)]

G1.3.1 -> AT3 [AND]
G1.3.2 -> AT4 [AND]
G1.4.1 -> AT5 [AND]
G1.4.2 -> AT6 [AND]
G1.4.3 -> AT7 [AND]
G1.5.1 -> AT8 [AND]
G1.5.2 -> AT9 [AND]
G1.6.1 -> AT10 [AND]
G1.6.2 -> AT11 [AND]
G1.6.3 -> AT12 [AND]
G1.7   -> AT13 [AND]
G1.8   -> AT14 [AND]
```

---

**Summary Table (Goals & Tasks)**

| **ID** | **Title** | **Type** | **Text** | **Runtime / Relation** | **Target Cond./Info** | **Location** | **Robots** |
|--------|-----------|----------|----------|------------------------|-----------------------|--------------|------------|
| G1 | Deliver Food to Inpatient Room | Goal | Deliver a meal from the kitchen to the patient’s room. | G1.1; G1.2; G1.3; G1.4; G1.5; G1.6; G1.7; G1.8 | Food on table or in hand | – | – |
| G1.1 | Receive Delivery Request | Goal | Receive an order‑by‑order request from the kitchen. | – | – | – | – |
| G1.2 | Transport Food to Room | Goal | Move the meal from the kitchen to the patient’s room. | – | – | – | – |
| G1.3 | Deliver Food to Patient | Goal | Deliver the meal to the patient (table or hand‑over). | FALLBACK(G1.3.1, G1.3.2) | Food on table or in hand | – | – |
| G1.3.1 | Place Food on Table | Goal | Place the meal on the patient’s table. | – | – | – | – |
| G1.3.2 | Hand Food to Patient | Goal | Hand the meal directly to the patient. | – | – | – | – |
| G1.4 | Retrieve Dishes | Goal | Remove dirty dishes from the patient’s room. | FALLBACK(FALLBACK(G1.4.1, G1.4.2), G1.4.3) | Dishes removed | – | – |
| G1.4.1 | Unassisted Retrieval | Goal | Robot retrieves dishes alone. | – | – | – | – |
| G1.4.2 | Two‑Robot Retrieval | Goal | Two robots cooperate to retrieve dishes. | – | – | – | – |
| G1.4.3 | Robot‑Human Retrieval | Goal | Robot cooperates with a human to retrieve dishes. | – | – | – | – |
| G1.5 | Open Door | Goal | Open the patient room door. | FALLBACK(G1.5.1, G1.5.2) | Door open | – | – |
| G1.5.1 | Robot Opens Door | Goal | Robot opens the door. | – | – | – | – |
| G1.5.2 | Human Opens Door | Goal | Human opens the door. | – | – | – | – |
| G1.6 | Determine Retrieval Method | Goal | Find out who can retrieve the meal from the tray. | G1.6.1#G1.6.2#G1.6.3 | – | – | – |
| G1.6.1 | Query Patient Capability | Goal | Ask patient record if the patient can retrieve food from the tray. | – | Patient’s ability to retrieve food | – | – |
| G1.6.2 | Query Companion Presence | Goal | Ask if a companion is present in the room. | – | Companion present? | – | – |
| G1.6.3 | Query Nurse Availability | Goal | Ask if a nurse is available to help. | – | Nurse available? | – | – |
| G1.7 | Track Meal Retrieval | Goal | Record when and where each meal was retrieved. | – | Retrieval logged | – | – |
| G1.8 | Alert Wrong Meal | Goal | Notify staff if the wrong meal is taken. | – | Wrong‑meal alert triggered | – | – |
| AT1 | Receive Kitchen Request | Task | Receive the delivery request from the kitchen. | AND | – | Kitchen | 1 |
| AT2 | Transport Food | Task | Move the meal from the kitchen to the patient’s room. | AND | – | Hallway | 1 |
| AT3 | Place Food on Table | Task | Place the meal on the patient’s table using manipulation skill. | AND | – | Patient room | 1 |
| AT4 | Hand Food to Patient | Task | Hand the meal to the patient, companion or nurse. | AND | – | Patient room | 1 |
| AT5 | Retrieve Dishes Unassisted | Task | Retrieve dirty dishes alone. | AND | – | Patient room | 1 |
| AT6 | Retrieve Dishes with Two Robots | Task | Retrieve dishes with two robots cooperating. | AND | – | Patient room | 2 |
| AT7 | Retrieve Dishes with Robot & Human | Task | Retrieve dishes with robot and human cooperation. | AND | – | Patient room | 1 |
| AT8 | Robot Opens Door | Task | Robot opens the patient room door. | AND | – | Patient room door | 1 |
| AT9 | Human Opens Door | Task | Human opens the patient room door. | AND | – | Patient room door | 0 |
| AT10 | Query Patient Capability | Task | Query patient record for ability to retrieve food from tray. | AND | – | Hospital database | 1 |
| AT11 | Query Companion Presence | Task | Query presence of companion in room. | AND | – | Patient room | 1 |
| AT12 | Query Nurse Availability | Task | Query nurse availability. | AND | – | Nurse station | 1 |
| AT13 | Record Meal Retrieval | Task | Log the time and location of meal retrieval. | AND | – | Robot memory | 1 |
| AT14 | Alert Wrong Meal | Task | Trigger an alert if the wrong meal is taken. | AND | – | Robot interface | 1 |

---

**Key Points**

* **Fallbacks** are used where a primary delivery or retrieval method may fail (e.g., placing on table first, then handing over; unassisted dish retrieval first, then two‑robot, then robot‑human).
* **Parallel queries** (patient capability, companion presence, nurse availability) are executed concurrently to reduce waiting time.
* **Sequential flow** from receiving the request to delivering the meal, retrieving dishes, and closing the door ensures a clear hand‑off between stages.
* **Robot‑human cooperation** is explicitly modeled for door opening and dish retrieval when the patient cannot act alone.
