**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

| **Name**                                | **Text**                                                                                                      | **Runtime**                            | **Goal Type** | **Target Condition / Enquired Information**                   | **Relation** | **Ground Truth I** | **Ground Truth G** | **Consensus** |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------- | ------------------------------------------------------------- | ------------ | ------------------ | ------------------ | ------------- |
| **G1 – Deliver Food to Inpatient Room** | Deliver a meal from the kitchen to the patient’s room and retrieve any dirty dishes.                          | G2#G3                                  | Achieve       | Food delivered to patient and all dirty dishes retrieved      | AND          |   Perform                 |                    |               |
| **G2 – Deliver Meal**                   | Execute the meal delivery sequence (door opening, pickup, delivery, patient retrieval).                       | G2.5; G2.4; FALLBACK(G2.1,(G2.2;G2.3)) | Perform       | –                                                             | AND          |  Achieve. Target condition: all food was delivered                  |                    |               |
| **G2.5 – Manage Door Opening**          | Open the patient room door (may involve another robot or a human).                                            | –                                      | Perform       | –                                                             | AND          | OK                   |                    |               |
| **G2.4 – Query Patient Capabilities**   | Obtain information on whether the patient can retrieve the meal, and whether a companion or nurse is present. | –                                      | Query         | Patient retrieval ability, companion presence, nurse presence | AND          |   OK                 |                    |               |
| **G2.1 – Deliver to Table**             | Place the meal directly on the patient’s table.                                                               | –                                      | Perform       | –                                                             | AND          |  OK                  |                    |               |
| **G2.2 – Deliver to Tray**              | Place the meal on the patient’s tray for later retrieval.                                                     | –                                      | Perform       | –                                                             | AND          |  OK                  |                    |               |
| **G2.3 – Patient Retrieval**            | Coordinate the patient’s retrieval of the meal from the tray.                                                 | G2.3.1;G2.3.2;G2.3.3;G2.3.4            | Perform       | –                                                             | AND          |  OK                  |                    |               |
| **G2.3.1 – Indicate Meal to Patient**   | Inform the patient which meal to pick up.                                                                     | –                                      | Perform       | –                                                             | AND          |  OK                  |                    |               |
| **G2.3.2 – Wait for Retrieval**         | Wait until the patient has taken the meal.                                                                    | –                                      | Perform       | –                                                             | AND          |  OK                  |                    |               |
| **G2.3.3 – Track Retrieval**            | Record the time and location of the meal retrieval.                                                           | –                                      | Perform       | –                                                             | AND          |  OK                  |                    |               |
| **G2.3.4 – Alert Wrong Meal**           | Notify staff if the patient retrieves the wrong meal.                                                         | –                                      | Perform       | –                                                             | AND          |  OK                  |                    |               |
| **G3 – Retrieve Dirty Dishes**          | Collect all dirty dishes from the patient’s room.                                                             | G3.1;G3.2;G3.3;G3.4                    | Perform       | –                                                             | AND          |  Achieve. Target condition: all dishes were retrieved.                  |                    |               |
| **G3.1 – Identify Dirty Dishes**        | Detect which dishes are dirty in the room.                                                                    | –                                      | Query         | List of dirty dishes in patient room                          | AND          |  OK                  |                    |               |
| **G3.2 – Retrieve Dishes**              | Pick up the dirty dishes.                                                                                     | –                                      | Perform       | –                                                             | AND          | OK                   |                    |               |
| **G3.3 – Coordinate with Human/Robot**  | Arrange assistance for dish retrieval.                                                                        | AT12;AT13                              | Perform       | –                                                             | AND          | OK                   |                    |               |
| **G3.3.1 – Coordinate with Human**      | Ask a human to help pick up dishes.                                                                           | –                                      | Perform       | –                                                             | AND          | OK                   |                    |               |
| **G3.3.2 – Coordinate with Robot**      | Ask another robot to help pick up dishes.                                                                     | –                                      | Perform       | –                                                             | AND          | OK                   |                    |               |
| **G3.4 – Open Door if Needed**          | Open the room door if it is closed.                                                                           | –                                      | Perform       | –                                                             | AND          | OK                   |                    |               |


---

**Task Model**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1 – Go to Kitchen** | Robot moves from its current location to the kitchen. | AND | kitchen | 1 |
| **AT2 – Pick up Meal** | Robot picks up a meal from the kitchen counter. | AND | kitchen | 1 |
| **AT3 – Open Door** | Robot opens the patient room door (may require a second robot or a human). | AND | patient room | [1,2] |
| **AT4 – Deliver to Table** | Robot places the meal on the patient’s table. | AND | patient room table | 1 |
| **AT5 – Deliver to Tray** | Robot places the meal on the patient’s tray. | AND | patient room tray | 1 |
| **AT6 – Indicate Meal to Patient** | Robot informs the patient which meal to retrieve. | AND | patient room | 1 |
| **AT7 – Wait for Retrieval** | Robot waits until the patient has taken the meal. | AND | patient room | 1 |
| **AT8 – Track Retrieval** | Robot records the time and location of the meal retrieval. | AND | patient room | 1 |
| **AT9 – Alert Wrong Meal** | Robot alerts staff if the patient retrieves the wrong meal. | AND | patient room | 1 |
| **AT10 – Identify Dirty Dishes** | Robot identifies dirty dishes in the patient’s room. | AND | patient room | 1 |
| **AT11 – Retrieve Dishes** | Robot picks up the dirty dishes (may involve a second robot). | AND | patient room | [1,2] |
| **AT12 – Coordinate with Human** | Robot coordinates with a human to retrieve dishes. | AND | patient room | 1 |
| **AT13 – Coordinate with Robot** | Robot coordinates with another robot to retrieve dishes. | AND | patient room | 2 |
| **AT14 – Go to Patient Room** | Robot moves to the patient’s room. | AND | patient room | 1 |

---

### Summary of Logical Relationships

| **Parent** | **Children** | **Relation** |
|------------|--------------|--------------|
| **G1** | G2, G3 | AND |
| **G2** | G2.5, G2.4, G2.1, G2.2, G2.3 | AND |
| **G2.5** | AT3 | AND |
| **G2.4** | – (query goal) | – |
| **G2.1** | AT1, AT2, AT4 | AND |
| **G2.2** | AT1, AT2, AT5 | AND |
| **G2.3** | G2.3.1, G2.3.2, G2.3.3, G2.3.4 | AND |
| **G2.3.1** | AT6 | AND |
| **G2.3.2** | AT7 | AND |
| **G2.3.3** | AT8 | AND |
| **G2.3.4** | AT9 | AND |
| **G3** | G3.1, G3.2, G3.3, G3.4 | AND |
| **G3.1** | AT10 | AND |
| **G3.2** | AT11 | AND |
| **G3.3** | AT12, AT13 | AND |
| **G3.4** | AT3 | AND |
| **AT3** | – (used by G2.5 and G3.4) | – |
| **AT14** | – (used by G2.5 and G3.4 if door opening requires movement) | – |

This goal‑task model captures the hierarchical decomposition of the multi‑robot food delivery and dish retrieval mission, explicitly representing the decision points (fallbacks), parallelism, and required cooperation with humans or other robots.
