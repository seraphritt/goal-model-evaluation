**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

| **Name**                                      | **Text**                                                                                                                  | **Runtime**                | **Goal Type** | **Target Condition / Enquired Info**                                                      | **Relation**  | **Justification**                                                                                                                                                                  | Ground truth I                                         | Ground truth C | Ground truth E |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------- | ----------------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------- | -------------- |
| **G1 – Deliver food to patient**              | Deliver a requested meal to the inpatient’s room, ensuring the correct meal is received and the patient is satisfied.     | `;`                        | Achieve       | “Meal delivered to patient’s room; patient receives correct meal; all retrievals logged.” | AND           | The robot must first determine if the patient can retrieve from the tray (query) and then decide on the delivery method. The two sub-steps must happen in order, hence sequential. | OK                                                     | Perform               |                |
| **G1.1 – Query patient retrieval capability** | Enquire whether the patient can fetch the meal from the robot’s tray, based on the patient record and companion presence. | `-`                        | Query         | “Can patient retrieve food from tray?”                                                    | AND           | Both the patient record and the presence of a companion are required to answer the query; both must be obtained.                                                                   | OK                                                     | OK               |                |
| **G1.2 – Select delivery method**             | Choose the appropriate delivery method (tray or table) based on the query result.                                         | `FALLBACK(G1.2.1, G1.2.2)` | Perform       | –                                                                                         | OR (fallback) | If tray delivery fails (e.g., patient cannot retrieve), the robot falls back to table delivery. The fallback operator captures this binary decision.                               | OK                                                     | OK               |                |
| **G1.2.1 – Deliver to tray**                  | Place the food on the robot’s tray so that the patient can retrieve it.                                                   | `-`                        | Perform       | –                                                                                         | AND           | All required actions (open door, place food, monitor & alert) must be completed.                                                                                                   | OK                                                     | OK               |                |
| **G1.2.2 – Deliver to table**                 | Place the food directly onto the patient’s table.                                                                         | `-`                        | Perform       | –                                                                                         | AND           | Requires opening the door and placing the food on the table.                                                                                                                       | OK                                                     | OK               |                |
| **G2 – Retrieve dirty dishes**                | Collect all dirty dishes from the patient’s room and bring them to the kitchen or dish-washing station.                   | `-`                        | Perform       | –                                                                                         | AND           | Both opening the door and retrieving the dishes must be performed.                                                                                                                 | Achieve. Target condition: all dishes were retreieved. | OK               |                |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1 – Open room door** | Robot opens the inpatient room door. | AND (within parent goal) | Patient room | `[1,2]` | Door opening may be performed alone or with a human/another robot; the range allows cooperation. |
| **AT2 – Place food on table** | Robot places the food onto the patient’s table. | AND (within G1.2.2) | Patient room table | `1` | One robot with manipulation skill is sufficient. |
| **AT3 – Place food on tray** | Robot places the food onto its own tray for patient retrieval. | AND (within G1.2.1) | Patient room | `1` | One robot performs the manipulation. |
| **AT4 – Assist patient retrieval** | Robot assists the patient (or companion) in picking up the meal from the tray. | AND (within G1.2.1) | Patient room | `1` | Single robot provides guidance or physical assistance. |
| **AT5 – Monitor & track retrieval** | Robot observes the patient’s pickup, logs the meal ID, time, and location. | AND (within G1.2.1) | Patient room | `1` | Continuous monitoring is performed by the same robot. |
| **AT6 – Alert wrong meal** | If the patient retrieves an incorrect meal, the robot issues an alarm. | AND (within G1.2.1) | Patient room | `1` | Immediate notification is required; one robot can handle it. |
| **AT7 – Retrieve dishes** | Robot collects all dirty dishes from the room. | AND (within G2) | Patient room | `[1,2]` | Dish retrieval may be done alone or with another robot/human. |
| **AT8 – Open door for dish retrieval** | Robot opens the door to allow dish retrieval. | AND (within G2) | Patient room | `[1,2]` | Cooperation may be needed; the range allows it. |
| **AT9 – Read inpatient record** | Robot queries the central database for the patient’s retrieval capability. | AND (within G1.1) | Hospital server | `1` | One robot accesses the database. |
| **AT10 – Check companion presence** | Robot observes whether a companion is present in the room. | AND (within G1.1) | Patient room | `1` | Direct observation by the robot. |

---

### Summary Table (Goals & Tasks)

| **ID** | **Type** | **Title** | **Runtime / Relation** | **Justification** |
|--------|----------|-----------|------------------------|-------------------|
| G1 | Goal (Achieve) | Deliver food to patient | `;` (sequential) | Must query before selecting method. |
| G1.1 | Goal (Query) | Query patient retrieval capability | `-` | Requires patient record & companion check. |
| G1.2 | Goal (Perform) | Select delivery method | `FALLBACK(G1.2.1, G1.2.2)` | Fallback to table if tray fails. |
| G1.2.1 | Goal (Perform) | Deliver to tray | `-` | Must perform all sub‑tasks. |
| G1.2.2 | Goal (Perform) | Deliver to table | `-` | Must perform all sub‑tasks. |
| G2 | Goal (Perform) | Retrieve dirty dishes | `-` | Must perform all sub‑tasks. |
| AT1 | Task | Open room door | AND | Needed by many goals. |
| AT2 | Task | Place food on table | AND | Specific to table delivery. |
| AT3 | Task | Place food on tray | AND | Specific to tray delivery. |
| AT4 | Task | Assist patient retrieval | AND | Needed when patient picks up. |
| AT5 | Task | Monitor & track retrieval | AND | Logging after pickup. |
| AT6 | Task | Alert wrong meal | AND | Immediate notification. |
| AT7 | Task | Retrieve dishes | AND | Dish collection. |
| AT8 | Task | Open door for dish retrieval | AND | Door opening for dish task. |
| AT9 | Task | Read inpatient record | AND | Query capability. |
| AT10 | Task | Check companion presence | AND | Verify companion. |

---

### Logical Relationships

- **G1 → G1.1, G1.2** [AND]  
  *Justification:* The robot must first query the patient’s capability (G1.1) before it can decide on the delivery method (G1.2). Both steps are required in sequence.

- **G1.2 → G1.2.1, G1.2.2** [FALLBACK(G1.2.1, G1.2.2)]  
  *Justification:* If delivering to the tray fails (e.g., patient cannot retrieve), the robot falls back to table delivery. The fallback operator captures this decision logic.

- **G1.2.1 → AT1, AT3, AT5, AT6** [AND]  
  *Justification:* All these actions (open door, place food on tray, monitor retrieval, alert wrong meal) must occur for successful tray delivery.

- **G1.2.2 → AT1, AT2** [AND]  
  *Justification:* Opening the door and placing food on the table are the only required actions for table delivery.

- **G1.1 → AT9, AT10** [AND]  
  *Justification:* Both reading the patient record and checking companion presence are necessary to answer the query.

- **G2 → AT8, AT7** [AND]  
  *Justification:* Dish retrieval requires door opening and dish collection.

---

This goal model decomposes the mission into clear, operational goals and tasks, explicitly captures decision points (query, fallback), and provides the necessary runtime annotations and justifications for each decomposition.
