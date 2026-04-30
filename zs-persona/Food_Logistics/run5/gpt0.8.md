## Goal Model – Multi‑Robot Food Delivery System  

| **Name**                                         | **Text**                                                                                                             | **Runtime**                      | **Goal Type** | **Target Condition / Enquired Info**                   | **Relation**     | **Ground truth I**                                    | **Ground truth C** | **Consensus**                                         |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------- | ------------------------------------------------------ | ---------------- | ----------------------------------------------------- | ------------------ | ----------------------------------------------------- |
| **G1: Deliver Food to Patient**                  | Achieve delivery of a meal from the kitchen to an inpatient’s room and ensure the patient receives the correct meal. | `FALLBACK(G3,G2)`                | Achieve       | `Food delivered to patient and patient receives meal.` | OR (fallback)    | OK.                                                   | OK                 | OK.                                                   |
| **G2: Deliver Food to Table**                    | Deliver food directly onto the patient’s table in the room.                                                          | `;`                              | Perform       | –                                                      | AND (sequential) | OK                                                    | OK                 | OK                                                    |
| **G3: Deliver Food to Tray & Patient Retrieves** | Deliver food to the patient’s tray and let the patient retrieve it.                                                  | `;`                              | Perform       | –                                                      | AND (sequential) | OK                                                    | OK                 | OK                                                    |
| **G3.1: Deliver to Tray**                        | Place the meal onto the patient’s tray.                                                                              | `;`                              | Perform       | –                                                      | AND (sequential) | OK                                                    | OK                 | OK                                                    |
| **G3.2: Patient Retrieval Process**              | Enable the patient to retrieve the meal from the tray.                                                               | `;`                              | Perform       | –                                                      | AND (sequential) | OK                                                    | OK                 | OK                                                    |
| **G3.3: Monitor Retrieval & Alert**              | Watch the retrieval and alert if the wrong meal is taken.                                                            | `-`                              | Perform       | –                                                      | –                | OK                                                    | OK                 | OK                                                    |
| **G4: Query Patient Retrieval Capability**       | Enquire whether the patient can retrieve a meal from the tray.                                                       | `-`                              | Query         | `Can patient retrieve meal from tray?`                 | –                | OK                                                    | OK                 | OK                                                    |
| **G5: Retrieve Dirty Dishes**                    | Collect dirty dishes from the patient’s room.                                                                        | `;`                              | Perform       | –                                                      | AND (sequential) | Achieve. target condition: all dishes were retrieved. | OK                 | Achieve. target condition: all dishes were retrieved. |
| **G5.1: Open Door**                              | Open the patient room door (may require cooperation).                                                                | `FALLBACK(G5.1.1,G5.1.2,G5.1.3)` | Perform       | –                                                      | OR (fallback)    | OK                                                    | OK                 | OK                                                    |
| **G5.1.1: Open Door Unassisted**                 | Open the door without any assistance.                                                                                | `-`                              | Perform       | –                                                      | –                | OK                                                    | OK                 | OK                                                    |
| **G5.1.2: Request Human to Open Door**           | Ask a human (nurse, companion, or patient) to open the door.                                                         | `-`                              | Perform       | –                                                      | –                | OK                                                    | OK                 | OK                                                    |
| **G5.1.3: Request Robot to Open Door**           | Ask another robot to open the door.                                                                                  | `-`                              | Perform       | –                                                      | –                | OK                                                    | OK                 | OK                                                    |
| **G5.2: Retrieve Dishes**                        | Pick up the dirty dishes from the room.                                                                              | `-`                              | Perform       | –                                                      | –                | OK                                                    | OK                 | OK                                                    |
| **G5.3: Assist Patient Retrieval**               | Help the patient retrieve dishes if needed.                                                                          | `-`                              | Perform       | –                                                      | –                | OK                                                    | OK                 | OK                                                    |

---

## Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1: Receive Delivery Request** | Receive an order‑by‑order request from the kitchen. | – | Kitchen | 1 |
| **AT2: Navigate to Kitchen** | Move from current location to the kitchen. | – | Hospital | 1 |
| **AT3: Pick Up Meal** | Pick up the meal from the kitchen counter. | – | Kitchen | 1 |
| **AT4: Navigate to Patient Room** | Move to the patient’s room. | – | Hospital | 1 |
| **AT5: Deliver to Tray** | Place the meal onto the patient’s tray. | – | Patient Room | 1 |
| **AT6: Wait for Patient Retrieval** | Wait until the patient retrieves the meal. | – | Patient Room | 1 |
| **AT7: Monitor Retrieval & Alert** | Monitor retrieval and alert if the wrong meal is taken. | – | Patient Room | 1 |
| **AT8: Deliver to Table** | Place the meal onto the patient’s table. | – | Patient Room Table | 1 |
| **AT9: Retrieve Dirty Dishes** | Collect dirty dishes from the patient’s room. | – | Patient Room | 1 |
| **AT10: Open Door Unassisted** | Open the room door without assistance. | – | Patient Room Door | 1 |
| **AT11: Request Human to Open Door** | Ask a human to open the room door. | – | Patient Room | 1 |
| **AT12: Request Robot to Open Door** | Ask another robot to open the room door. | – | Patient Room | 1 |
| **AT13: Query Patient Record** | Query the patient record for retrieval capability. | – | Hospital Database | 1 |
| **AT14: Assist Patient Retrieval** | Assist the patient in retrieving the meal or dishes. | – | Patient Room | 1 |

---

## Summary of Logical Relationships

| **Goal** | **Children** | **Relation** | **Runtime** |
|----------|--------------|--------------|-------------|
| **G1** | G3, G2 | OR (fallback) | `FALLBACK(G3,G2)` |
| **G2** | AT1, AT2, AT3, AT4, AT8 | AND (sequential) | `;` |
| **G3** | G3.1, G3.2, G3.3 | AND (sequential) | `;` |
| **G3.1** | AT4, AT5 | AND (sequential) | `;` |
| **G3.2** | G4, AT6 | AND (sequential) | `;` |
| **G3.3** | AT7 | AND | `-` |
| **G4** | – | – | `-` |
| **G5** | G5.1, G5.2, G5.3 | AND (sequential) | `;` |
| **G5.1** | G5.1.1, G5.1.2, G5.1.3 | OR (fallback) | `FALLBACK(G5.1.1,G5.1.2,G5.1.3)` |
| **G5.1.1** | AT10 | AND | `-` |
| **G5.1.2** | AT11 | AND | `-` |
| **G5.1.3** | AT12 | AND | `-` |
| **G5.2** | AT9 | AND | `-` |
| **G5.3** | AT14 | AND | `-` |

*All leaf tasks have no further children, so their relation is “-” and runtime is “-”.*
