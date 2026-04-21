**Goal Model – Multi‑Robot Food Delivery**

| **Name**                                    | **Text**                                                                                                                                 | **Runtime**                          | **Goal Type** | **Target Condition / Enquired Information**   | **Relation** | **Ground truth I**                                    | **Ground truth C** | **Ground truth E** |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------- | --------------------------------------------- | ------------ | ----------------------------------------------------- | ------------------ | ------------------ |
| **G1: Deliver Food to Inpatient Room**      | Achieve delivery of food from the kitchen to the inpatient’s room, ensuring the meal is placed on the table or retrieved by the patient. | `;`                                  | Achieve       | `food delivered to room and patient has meal` | AND          | Perform                                               | Perform                   |                    |
| **G2: Obtain Order and Meals from Kitchen** | Retrieve the meal order and fetch the meals from the kitchen.                                                                            | `#`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G4: Deliver Food**                        | Deliver food to the inpatient, either by placing it on the table or by providing a tray for the patient to fetch.                        | `FALLBACK(G4.2, G4.1)`               | Perform       | –                                             | OR           | Achieve. Target condition: all food was delivered     | Ok                   |                    |
| **G4.2: Provide Tray for Inpatient**        | Place a tray for the patient to fetch the meal, requiring a check of the patient’s retrieval capability.                                 | `;`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G4.2.1: Check Retrieval Capability**      | Query the inpatient record to determine whether the patient can retrieve the meal from the tray.                                         | `-`                                  | Query         | `can_inpatient_retrieve`                      | AND          | OK                                                    | Ok                   |                    |
| **G4.2.2: Place Tray and Await Retrieval**  | Place the tray, wait for the patient to retrieve the meal, then log the retrieval and alert if the wrong meal is taken.                  | `#`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G4.1: Deliver to Table**                  | Deliver the meal directly onto the patient’s table using a special manipulation skill.                                                   | `;`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G5: Retrieve Dishes**                     | Retrieve dirty dishes from the room, using unassisted, two-robot, or human-assisted methods.                                             | `FALLBACK(FALLBACK(G5.1,G5.2),G5.3)` | Perform       | –                                             | OR           | Achieve. Target condition: all dishes were retrieved. | Ok                   |                    |
| **G5.1: Unassisted Retrieval**              | Robot retrieves dishes alone.                                                                                                            | `-`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G5.2: Two Robots Retrieval**              | Two robots coordinate to retrieve dishes.                                                                                                | `#`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G5.3: Human-Assisted Retrieval**          | Robot assists a human in retrieving dishes.                                                                                              | `#`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G6: Manage Door**                         | Open the room door to allow robot entry/exit, possibly with human or another robot.                                                      | `FALLBACK(FALLBACK(G6.1,G6.2),G6.3)` | Perform       | –                                             | OR           | OK                                                    | Ok                   |                    |
| **G6.1: Robot Alone**                       | Robot opens the door alone.                                                                                                              | `-`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G6.2: Robot + Human**                     | Robot and human collaborate to open the door.                                                                                            | `#`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |
| **G6.3: Robot + Robot**                     | Two robots coordinate to open the door.                                                                                                  | `#`                                  | Perform       | –                                             | AND          | OK                                                    | Ok                   |                    |


---

**Task Model**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1: Retrieve Order from Kitchen** | Robot obtains the meal order from the kitchen station. | AND | kitchen | 1 |
| **AT2: Fetch Meals from Kitchen** | Robot picks up the meals for the order. | AND | kitchen | 1 |
| **AT5: Place Tray at Table** | Robot places a tray on the patient’s table. | AND | room table | 1 |
| **AT6: Signal Inpatient** | Robot signals the patient that the tray is ready. | AND | room | 1 |
| **AT7: Wait for Retrieval** | Robot waits for the patient to retrieve the meal from the tray. | AND | room | 1 |
| **AT25: Indicate Meal to Inpatient** | Robot indicates which meal should be retrieved. | AND | room | 1 |
| **AT26: Log Retrieval** | Robot logs the time and location of meal retrieval. | AND | robot | 1 |
| **AT27: Alert Wrong Meal** | Robot alerts if the retrieved meal does not match the order. | AND | robot | 1 |
| **AT8: Approach Table** | Robot approaches the patient’s table to deliver meal. | AND | room table | 1 |
| **AT9: Manipulate and Place Meal** | Robot manipulates the meal and places it on the table. | AND | room table | 1 |
| **AT10: Approach Dish** | Robot approaches a dirty dish in the room. | AND | room | 1 |
| **AT11: Pick Up Dish** | Robot picks up the dirty dish. | AND | room | 1 |
| **AT12: Robot1 Approach Dish** | First robot approaches the dish. | AND | room | 1 |
| **AT13: Robot2 Assist** | Second robot assists in picking up the dish. | AND | room | 1 |
| **AT14: Pick Up Dish** | Two robots coordinate to pick up the dish. | AND | room | 2 |
| **AT15: Approach Dish** | Robot approaches dish for human assistance. | AND | room | 1 |
| **AT16: Await Human Assistance** | Robot waits for human to pick up dish. | AND | room | 1 |
| **AT17: Human Picks Up Dish** | Human picks up the dish with robot’s assistance. | AND | room | 1 |
| **AT18: Approach Door** | Robot approaches the room door. | AND | door | 1 |
| **AT19: Open Door** | Robot opens the door. | AND | door | 1 |
| **AT20: Robot Approach Door** | Robot approaches the door while human opens it. | AND | door | 1 |
| **AT21: Human Opens Door** | Human opens the door with robot’s help. | AND | door | 1 |
| **AT22: Robot1 Approach Door** | First robot approaches the door. | AND | door | 1 |
| **AT23: Robot2 Assist** | Second robot assists in opening the door. | AND | door | 1 |
| **AT24: Open Door** | Two robots coordinate to open the door. | AND | door | 2 |

---

### Summary Table (Goals & Tasks)

| **ID** | **Title** | **Type** | **Parent** |
|--------|-----------|----------|------------|
| G1 | Deliver Food to Inpatient Room | Goal (Achieve) | Root |
| G2 | Obtain Order and Meals from Kitchen | Goal (Perform) | G1 |
| AT1 | Retrieve Order from Kitchen | Task | G2 |
| AT2 | Fetch Meals from Kitchen | Task | G2 |
| G4 | Deliver Food | Goal (Perform) | G1 |
| G4.2 | Provide Tray for Inpatient | Goal (Perform) | G4 |
| G4.2.1 | Check Retrieval Capability | Goal (Query) | G4.2 |
| G4.2.2 | Place Tray and Await Retrieval | Goal (Perform) | G4.2 |
| AT5 | Place Tray at Table | Task | G4.2.2 |
| AT6 | Signal Inpatient | Task | G4.2.2 |
| AT7 | Wait for Retrieval | Task | G4.2.2 |
| AT25 | Indicate Meal to Inpatient | Task | G4.2.2 |
| AT26 | Log Retrieval | Task | G4.2.2 |
| AT27 | Alert Wrong Meal | Task | G4.2.2 |
| G4.1 | Deliver to Table | Goal (Perform) | G4 |
| AT8 | Approach Table | Task | G4.1 |
| AT9 | Manipulate and Place Meal | Task | G4.1 |
| G5 | Retrieve Dishes | Goal (Perform) | G1 |
| G5.1 | Unassisted Retrieval | Goal (Perform) | G5 |
| AT10 | Approach Dish | Task | G5.1 |
| AT11 | Pick Up Dish | Task | G5.1 |
| G5.2 | Two Robots Retrieval | Goal (Perform) | G5 |
| AT12 | Robot1 Approach Dish | Task | G5.2 |
| AT13 | Robot2 Assist | Task | G5.2 |
| AT14 | Pick Up Dish | Task | G5.2 |
| G5.3 | Human‑Assisted Retrieval | Goal (Perform) | G5 |
| AT15 | Approach Dish | Task | G5.3 |
| AT16 | Await Human Assistance | Task | G5.3 |
| AT17 | Human Picks Up Dish | Task | G5.3 |
| G6 | Manage Door | Goal (Perform) | G1 |
| G6.1 | Robot Alone | Goal (Perform) | G6 |
| AT18 | Approach Door | Task | G6.1 |
| AT19 | Open Door | Task | G6.1 |
| G6.2 | Robot + Human | Goal (Perform) | G6 |
| AT20 | Robot Approach Door | Task | G6.2 |
| AT21 | Human Opens Door | Task | G6.2 |
| G6.3 | Robot + Robot | Goal (Perform) | G6 |
| AT22 | Robot1 Approach Door | Task | G6.3 |
| AT23 | Robot2 Assist | Task | G6.3 |
| AT24 | Open Door | Task | G6.3 |

---

### Logical Relationships

```
G1 -> G2, G4, G5, G6 [AND][;]
G2 -> AT1, AT2 [AND][#]
G4 -> G4.2, G4.1 [OR][FALLBACK(G4.2, G4.1)]
G4.2 -> G4.2.1, G4.2.2 [AND][;]
G4.2.2 -> AT5, AT6, AT7, AT25, AT26, AT27 [AND][#]
G4.1 -> AT8, AT9 [AND][;]
G5 -> G5.1, G5.2, G5.3 [OR][FALLBACK(FALLBACK(G5.1, G5.2), G5.3)]
G5.1 -> AT10, AT11 [AND][#]
G5.2 -> AT12, AT13, AT14 [AND][#]
G5.3 -> AT15, AT16, AT17 [AND][#]
G6 -> G6.1, G6.2, G6.3 [OR][FALLBACK(FALLBACK(G6.1, G6.2), G6.3)]
G6.1 -> AT18, AT19 [AND][#]
G6.2 -> AT20, AT21 [AND][#]
G6.3 -> AT22, AT23, AT24 [AND][#]
```

This goal‑task model captures the multi‑robot food‑delivery mission, including decision points for patient retrieval capability, cooperation with humans or other robots, and handling of dirty dishes and door opening.
