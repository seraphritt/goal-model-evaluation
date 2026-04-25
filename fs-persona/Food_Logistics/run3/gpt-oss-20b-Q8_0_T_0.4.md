**Goal Model – Multi‑Robot Food & Dish Delivery**

| **Name**     | **Text**                                                                                 | **Runtime**                          | **Goal Type** | **Enquired Information / Target Condition** | **Relation** | **Ground truth I**                                    | **Ground truth C** | **Ground truth E** |
| ------------ | ---------------------------------------------------------------------------------------- | ------------------------------------ | ------------- | ------------------------------------------- | ------------ | ----------------------------------------------------- | ------------------ | ------------------ |
| **G1**       | Deliver food to an inpatient room (order-by-order)                                       | FALLBACK(G1.1, G1.2)                 | Perform       |                                             | Root         | Achieve. Target condition: all food was delivered.    |  Ok                  |                    |
| **G1.1**     | Direct delivery to the patient’s table (robot uses special manipulation)                 | AND                                  | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.1.1**   | Navigate to the room & open the door                                                     | AND                                  | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.1.2**   | Manipulate the meal onto the table                                                       | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2**     | Deliver the meal to the robot tray and let the patient (or assistance) fetch it          | AND                                  | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.1**   | Place the meal on the robot tray                                                         | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.2**   | Query if the patient can fetch the meal from the tray                                    | –                                    | Query         | can_patient_fetch                           | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.3**   | Fetch the meal from the tray (patient or assisted)                                       | FALLBACK(G1.2.3a, G1.2.3b)           | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.3a**  | Patient fetches the meal                                                                 | AND                                  | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.3a1** | Indicate which meal the patient should take                                              | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.3a2** | Track the meal retrieval                                                                 | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.3a3** | Alert if the wrong meal is retrieved                                                     | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.3b**  | Assistance fetch (nurse / visitor / robot)                                               | AND                                  | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.3b1** | Request assistance                                                                       | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G1.2.3b2** | Robot fetches the meal from the tray                                                     | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G2**       | Retrieve dirty dishes from the room (unassisted, robot cooperation or human cooperation) | FALLBACK(FALLBACK(G2.1, G2.2), G2.3) | Perform       |                                             | Root         | Achieve. Target condition: all dishes were retrieved. |  Ok                  |                    |
| **G2.1**     | Unassisted dish retrieval                                                                | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G2.2**     | Robot cooperation (door opening + dish pickup)                                           | AND                                  | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G2.2.1**   | Open the door with another robot                                                         | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G2.2.2**   | Pick up dishes                                                                           | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G2.3**     | Human cooperation (door opening + dish pickup)                                           | AND                                  | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G2.3.1**   | Request human to open the door                                                           | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |
| **G2.3.2**   | Log that dishes have been retrieved                                                      | –                                    | Perform       |                                             | AND          | OK                                                    |  Ok                  |                    |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Navigate to the inpatient room | AND | room | 1 |
| **AT14** | Open the room door | AND | door | 1 |
| **AT2** | Place the meal onto the patient’s table | AND | room | 1 |
| **AT3** | Place the meal onto the robot’s tray | AND | kitchen | 1 |
| **AT5** | Announce which meal the patient should take | AND | room | 1 |
| **AT6** | Log the retrieval of the meal | AND | room | 1 |
| **AT13** | Alert if the retrieved meal is incorrect | AND | room | 1 |
| **AT7** | Request assistance from nurse/visitor/robot | AND | room | 1 |
| **AT8** | Robot fetches the meal from the tray for the patient | AND | room | 1 |
| **AT9** | Pick up dirty dishes from the room | AND | room | 1 |
| **AT10** | Open the door with help of another robot | AND | door | 2 |
| **AT11** | Request human to open the door | AND | room | 1 |
| **AT12** | Log that dishes have been retrieved | AND | room | 1 |

---

### Logical Relationships (Parent → Children)

```
G1  -> G1.1, G1.2 [OR][FALLBACK(G1.1,G1.2)]
G1.1 -> G1.1.1, G1.1.2 [AND][AND]
G1.1.1 -> AT1, AT14 [AND][AND]
G1.1.2 -> AT2 [AND][AND]

G1.2 -> G1.2.1, G1.2.2, G1.2.3 [AND][AND]
G1.2.1 -> AT3 [AND][AND]
G1.2.2 -> (query) [AND][-]
G1.2.3 -> G1.2.3a, G1.2.3b [OR][FALLBACK(G1.2.3a,G1.2.3b)]

G1.2.3a -> G1.2.3a1, G1.2.3a2, G1.2.3a3 [AND][AND]
G1.2.3a1 -> AT5 [AND][AND]
G1.2.3a2 -> AT6 [AND][AND]
G1.2.3a3 -> AT13 [AND][AND]

G1.2.3b -> G1.2.3b1, G1.2.3b2 [AND][AND]
G1.2.3b1 -> AT7 [AND][AND]
G1.2.3b2 -> AT8 [AND][AND]

G2  -> G2.1, G2.2, G2.3 [OR][FALLBACK(FALLBACK(G2.1,G2.2),G2.3)]
G2.1 -> AT9 [AND][AND]
G2.2 -> G2.2.1, G2.2.2 [AND][AND]
G2.2.1 -> AT10 [AND][AND]
G2.2.2 -> AT9 [AND][AND]
G2.3 -> G2.3.1, G2.3.2 [AND][AND]
G2.3.1 -> AT11 [AND][AND]
G2.3.2 -> AT12 [AND][AND]
```

---

### Summary Table (Goals & Tasks)

| **ID** | **Type** | **Description** |
|--------|----------|-----------------|
| G1 | Goal – Perform | Deliver food to an inpatient room (direct or tray) |
| G1.1 | Goal – Perform | Direct delivery to the patient’s table |
| G1.1.1 | Goal – Perform | Navigate & open door |
| G1.1.2 | Goal – Perform | Manipulate meal onto table |
| G1.2 | Goal – Perform | Tray delivery + patient fetch |
| G1.2.1 | Goal – Perform | Place meal on robot tray |
| G1.2.2 | Goal – Query | Query patient fetch capability |
| G1.2.3 | Goal – Perform | Fetch meal (patient or assisted) |
| G1.2.3a | Goal – Perform | Patient fetch |
| G1.2.3a1 | Goal – Perform | Indicate meal to patient |
| G1.2.3a2 | Goal – Perform | Track meal retrieval |
| G1.2.3a3 | Goal – Perform | Alert wrong meal |
| G1.2.3b | Goal – Perform | Assistance fetch |
| G1.2.3b1 | Goal – Perform | Request assistance |
| G1.2.3b2 | Goal – Perform | Assist fetch |
| G2 | Goal – Perform | Retrieve dirty dishes |
| G2.1 | Goal – Perform | Unassisted retrieval |
| G2.2 | Goal – Perform | Robot cooperation |
| G2.2.1 | Goal – Perform | Open door with another robot |
| G2.2.2 | Goal – Perform | Pick up dishes |
| G2.3 | Goal – Perform | Human cooperation |
| G2.3.1 | Goal – Perform | Request human to open door |
| G2.3.2 | Goal – Perform | Log dish retrieval |
| AT1 | Task | Navigate to the inpatient room |
| AT14 | Task | Open the room door |
| AT2 | Task | Place the meal onto the patient’s table |
| AT3 | Task | Place the meal onto the robot’s tray |
| AT5 | Task | Announce which meal the patient should take |
| AT6 | Task | Log the retrieval of the meal |
| AT13 | Task | Alert if the retrieved meal is incorrect |
| AT7 | Task | Request assistance from nurse/visitor/robot |
| AT8 | Task | Robot fetches the meal from the tray for the patient |
| AT9 | Task | Pick up dirty dishes from the room |
| AT10 | Task | Open the door with help of another robot |
| AT11 | Task | Request human to open the door |
| AT12 | Task | Log that dishes have been retrieved |

This goal‑task decomposition captures the full multi‑robot system behaviour for food delivery and dish retrieval, including handling of uncertainty, cooperation, and monitoring.
