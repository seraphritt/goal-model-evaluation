**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

| **Name**                           | **Text**                                                                                          | **Runtime**                        | **Goal Type** | **Target / Enquired Info**                      | **Relation** | **Ground truth I**                                    | **Ground truth C** | **Consensus**                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------- | ----------------------------------------------- | ------------ | ----------------------------------------------------- | ------------------ | ----------------------------------------------------- |
| G1: Respond to Delivery Request    | Respond to kitchen delivery requests by delivering food to inpatient rooms *and* cleaning dishes. | `;`                                | Achieve       | food delivered and dishes cleaned               | AND          | Perform.                                              | Perform            | Perform.                                              |
| G2: Deliver Food to Inpatient Room | Deliver food from kitchen to inpatient room.                                                      | `FALLBACK(G2.1, G2.2)`             | Achieve       | food delivered to table or retrieved by patient | OR           | OK                                                    | Ok                 | OK                                                    |
| G2.1: Deliver to Table             | Robot delivers food onto inpatient table.                                                         | `;`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G2.1.1: Open Door                  | Robot or human opens the room door.                                                               | `FALLBACK(AT1, AT2)`               | Perform       | door opened                                     | OR           | OK                                                    | Ok                 | OK                                                    |
| G2.1.2: Move to Room               | Robot moves to the room.                                                                          | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G2.1.3: Pick Meal                  | Robot picks up meal from tray.                                                                    | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G2.1.4: Deliver to Table           | Robot manipulates food onto table.                                                                | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G2.2: Hand Over to Patient         | Robot hands over meal to patient for retrieval from tray.                                         | `;`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G2.2.1: Query Retrieval Ability    | Query if patient can retrieve meal.                                                               | `-`                                | Query         | can patient retrieve meal?                      | AND          | OK                                                    | Ok                 | OK                                                    |
| G2.2.2: Indicate Meal to Retrieve  | Robot indicates which meal patient should retrieve.                                               | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G2.2.3: Wait and Track Retrieval   | Robot waits & tracks patient retrieval.                                                           | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G2.2.4: Alert Wrong Meal           | Robot alerts if wrong meal is retrieved.                                                          | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G3: Retrieve Dirty Dishes          | Robot retrieves dirty dishes from inpatient room.                                                 | `;`                                | Perform       | –                                               | AND          | Achieve. Target condition: all dishes were retrieved. | Ok                 | Achieve. Target condition: all dishes were retrieved. |
| G3.1: Open Door                    | Robot or human opens room door for dish retrieval.                                                | `FALLBACK(AT10, AT11)`             | Perform       | door opened                                     | OR           | OK                                                    | Ok                 | OK                                                    |
| G3.2: Retrieve Dishes              | Robot retrieves dishes, possibly with assistance.                                                 | `FALLBACK(G3.2.1, G3.2.2, G3.2.3)` | Perform       | –                                               | OR           | OK                                                    | Ok                 | OK                                                    |
| G3.2.1: Retrieve Unassisted        | Robot retrieves dish unassisted.                                                                  | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G3.2.2: Retrieve with Two Robots   | Two robots retrieve dish together.                                                                | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |
| G3.2.3: Retrieve with Human        | Robot retrieves dish with human assistance.                                                       | `-`                                | Perform       | –                                               | AND          | OK                                                    | Ok                 | OK                                                    |

---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **# Robots** |
|----------|----------|--------------|--------------|--------------|
| AT1: Robot Open Door | Robot opens the room door. | OR | room door | 1 |
| AT2: Human Open Door | Human opens the room door. | OR | room door | 0 |
| AT3: Move to Room | Robot moves to inpatient room. | AND | room | 1 |
| AT4: Pick Meal from Tray | Robot picks up meal from tray. | AND | tray | 1 |
| AT5: Manipulate Food onto Table | Robot manipulates food onto table. | AND | table | 1 |
| AT6: Query Retrieval Ability | Robot queries inpatient record & companion presence. | AND | system | 0 |
| AT7: Indicate Meal | Robot indicates which meal patient should retrieve. | AND | room | 1 |
| AT8: Monitor Retrieval | Robot monitors patient retrieving meal. | AND | room | 1 |
| AT9: Alert Wrong Meal | Robot alerts if wrong meal is retrieved. | AND | room | 1 |
| AT10: Robot Open Door (Dish) | Robot opens the room door for dish retrieval. | OR | room door | 1 |
| AT11: Human Open Door (Dish) | Human opens the room door for dish retrieval. | OR | room door | 0 |
| AT12: Pick Up Dish Unassisted | Robot picks up dirty dish unassisted. | AND | room | 1 |
| AT13: Pick Up Dish with Two Robots | Two robots cooperate to pick up dirty dish. | AND | room | 2 |
| AT14: Pick Up Dish with Human | Robot cooperates with human to pick up dirty dish. | AND | room | 1 |

---

## Logical Relationships (Tree Structure)

```
G1 -> G2, G3 [AND][;]
G2 -> G2.1, G2.2 [OR][FALLBACK(G2.1, G2.2)]
G2.1 -> G2.1.1, G2.1.2, G2.1.3, G2.1.4 [AND][;]
G2.1.1 -> AT1, AT2 [OR][FALLBACK(AT1, AT2)]
G2.1.2 -> AT3 [AND]
G2.1.3 -> AT4 [AND]
G2.1.4 -> AT5 [AND]
G2.2 -> G2.2.1, G2.2.2, G2.2.3, G2.2.4 [AND][;]
G2.2.1 -> AT6 [AND]
G2.2.2 -> AT7 [AND]
G2.2.3 -> AT8 [AND]
G2.2.4 -> AT9 [AND]
G3 -> G3.1, G3.2 [AND][;]
G3.1 -> AT10, AT11 [OR][FALLBACK(AT10, AT11)]
G3.2 -> G3.2.1, G3.2.2, G3.2.3 [OR][FALLBACK(G3.2.1, G3.2.2, G3.2.3)]
G3.2.1 -> AT12 [AND]
G3.2.2 -> AT13 [AND]
G3.2.3 -> AT14 [AND]
```

---

### Summary Table (Goals + Tasks)

| **ID** | **Type** | **Title** | **Runtime / Relation** |
|--------|----------|-----------|------------------------|
| G1 | Goal | Respond to Delivery Request | `;` AND |
| G2 | Goal | Deliver Food to Inpatient Room | `FALLBACK(G2.1, G2.2)` OR |
| G2.1 | Goal | Deliver to Table | `;` AND |
| G2.1.1 | Goal | Open Door | `FALLBACK(AT1, AT2)` OR |
| G2.1.2 | Goal | Move to Room | `-` AND |
| G2.1.3 | Goal | Pick Meal | `-` AND |
| G2.1.4 | Goal | Deliver to Table | `-` AND |
| G2.2 | Goal | Hand Over to Patient | `;` AND |
| G2.2.1 | Goal | Query Retrieval Ability | `-` AND |
| G2.2.2 | Goal | Indicate Meal to Retrieve | `-` AND |
| G2.2.3 | Goal | Wait and Track Retrieval | `-` AND |
| G2.2.4 | Goal | Alert Wrong Meal | `-` AND |
| G3 | Goal | Retrieve Dirty Dishes | `;` AND |
| G3.1 | Goal | Open Door | `FALLBACK(AT10, AT11)` OR |
| G3.2 | Goal | Retrieve Dishes | `FALLBACK(G3.2.1, G3.2.2, G3.2.3)` OR |
| G3.2.1 | Goal | Retrieve Unassisted | `-` AND |
| G3.2.2 | Goal | Retrieve with Two Robots | `-` AND |
| G3.2.3 | Goal | Retrieve with Human | `-` AND |
| AT1 | Task | Robot Open Door | OR |
| AT2 | Task | Human Open Door | OR |
| AT3 | Task | Move to Room | AND |
| AT4 | Task | Pick Meal from Tray | AND |
| AT5 | Task | Manipulate Food onto Table | AND |
| AT6 | Task | Query Retrieval Ability | AND |
| AT7 | Task | Indicate Meal | AND |
| AT8 | Task | Monitor Retrieval | AND |
| AT9 | Task | Alert Wrong Meal | AND |
| AT10 | Task | Robot Open Door (Dish) | OR |
| AT11 | Task | Human Open Door (Dish) | OR |
| AT12 | Task | Pick Up Dish Unassisted | AND |
| AT13 | Task | Pick Up Dish with Two Robots | AND |
| AT14 | Task | Pick Up Dish with Human | AND |

This goal‑task tree captures the full multi‑robot mission: delivering food to inpatient rooms (either directly onto the table or by handing it over for patient retrieval) while handling uncertainties about patient retrieval capability, and cleaning dirty dishes with or without human/robot assistance. The runtime annotations and decomposition operators define the execution flow, and the task attributes (location, robot count) make the model actionable for a multi‑robot system.
