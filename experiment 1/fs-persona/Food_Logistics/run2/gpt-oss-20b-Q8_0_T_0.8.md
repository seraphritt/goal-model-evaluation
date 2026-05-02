**Goal Model – Multi‑Robot Food‑Delivery Mission**
| **Name** | **Text**                                                                             | **Runtime**          | **Goal Type** | **Target Condition / Enquired Information**                 | **Relation** | **Ground truth I**                                 | **Ground truth C** | **Consensus**                                      |
| -------- | ------------------------------------------------------------------------------------ | -------------------- | ------------- | ----------------------------------------------------------- | ------------ | -------------------------------------------------- | ------------------ | -------------------------------------------------- |
| G1       | Deliver food from kitchen to inpatient room in response to delivery requests.        | #                    | Perform       | Food is delivered to the room and all dishes are retrieved. | AND          | OK                                                 | OK                 | OK                                                 |
| G2       | Receive delivery request from the kitchen.                                           | -                    | Perform       | Delivery request is received.                               | –            | OK                                                 | OK                 | OK                                                 |
| G3       | Check whether the patient, a companion or a nurse can retrieve a meal from the tray. | -                    | Query         | “Patient/companion/nurse can retrieve meal from tray?”      | –            | OK                                                 | OK                 | OK                                                 |
| G4       | Execute the food delivery.                                                           | FALLBACK(G4.1, G4.2) | Perform       | Food is delivered to the room.                              | OR           | Achieve. Target condition: all food was delivered. | OK                 | Achieve. Target condition: all food was delivered. |
| G4.1     | Deliver the meal directly onto the patient’s table.                                  | -                    | Perform       | Meal is placed on the table.                                | –            | OK                                                 | OK                 | OK                                                 |
| G4.2     | Deliver the meal onto a tray and manage patient retrieval.                           | ;                    | Perform       | Meal is delivered to the room and patient retrieves it.     | AND          | OK                                                 | OK                 | OK                                                 |
| G4.2.1   | Place the meal on the tray.                                                          | -                    | Perform       | Meal is placed on the tray.                                 | –            | OK                                                 | OK                 | OK                                                 |
| G4.2.2   | Assist the patient or companion/nurse in retrieving the meal.                        | -                    | Perform       | Patient retrieves the meal.                                 | –            | OK                                                 | OK                 | OK                                                 |
| G4.2.3   | Detect if the wrong meal was retrieved.                                              | -                    | Perform       | Wrong meal is detected.                                     | –            | OK                                                 | OK                 | OK                                                 |
| G4.2.4   | Alert the system when a wrong meal has been retrieved.                               | -                    | Perform       | Wrong-meal alert is sent.                                   | –            | OK                                                 | OK                 | OK                                                 |
| G5       | Retrieve all dirty dishes from the room.                                             | OR                   | Perform       | All dirty dishes are retrieved.                             | OR           | Achieve. All dishes were retrieved.                | OK                 | Achieve. All dishes were retrieved.                |
| G5.1     | Retrieve dishes unassisted by the robot.                                             | -                    | Perform       | Dishes are retrieved by the robot alone.                    | –            | OK                                                 | OK                 | OK                                                 |
| G5.2     | Retrieve dishes with cooperation from another robot.                                 | -                    | Perform       | Dishes are retrieved jointly with another robot.            | –            | OK                                                 | OK                 | OK                                                 |
| G5.3     | Retrieve dishes with cooperation from a human, patient, companion or nurse.          | -                    | Perform       | Dishes are retrieved with human help.                       | –            | OK                                                 | OK                 | OK                                                 |


---

**Task Model**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| AT1 | Navigate to the room and place the meal on the table. | AND (G4.1) | room | 1 |
| AT2 | Place the meal on the tray. | AND (G4.2.1) | room | 1 |
| AT3 | Assist the patient (or companion/nurse) in retrieving the meal. | AND (G4.2.2) | room | 1 |
| AT4 | Retrieve dirty dishes without human assistance. | AND (G5.1) | room | 1 |
| AT5 | Retrieve dirty dishes in cooperation with another robot. | AND (G5.2) | room | 2 |
| AT6 | Retrieve dirty dishes in cooperation with a human. | AND (G5.3) | room | 1 |
| AT7 | Open the room door (required for all delivery and retrieval tasks). | AND (G4.1, G4.2.1, G4.2.2, G4.2.3, G4.2.4, G5.1, G5.2, G5.3) | door | 1 |
| AT9 | Detect that the wrong meal was retrieved. | AND (G4.2.3) | robot | 1 |
| AT10 | Alert the system that a wrong meal has been retrieved. | AND (G4.2.4) | system | 1 |

---

### Logical Relationships Summary

- **G1** → G2, G3, G4, G5 [AND] Runtime: #  
- **G2** → (none) [leaf]  
- **G3** → (none) [leaf]  
- **G4** → G4.1, G4.2 [OR] Runtime: FALLBACK(G4.1, G4.2)  
- **G4.1** → AT1, AT7 [AND] Runtime: -  
- **G4.2** → G4.2.1, G4.2.2, G4.2.3, G4.2.4 [AND] Runtime: ;  
- **G4.2.1** → AT2, AT7 [AND] Runtime: -  
- **G4.2.2** → AT3, AT7 [AND] Runtime: -  
- **G4.2.3** → AT9, AT7 [AND] Runtime: -  
- **G4.2.4** → AT10, AT7 [AND] Runtime: -  
- **G5** → G5.1, G5.2, G5.3 [OR] Runtime: OR  
- **G5.1** → AT4, AT7 [AND] Runtime: -  
- **G5.2** → AT5, AT7 [AND] Runtime: -  
- **G5.3** → AT6, AT7 [AND] Runtime: -  

*The model captures the full set of mission objectives and operational tasks, their decomposition, and the execution semantics required for a multi‑robot food delivery and dish retrieval system in a hospital setting.*
