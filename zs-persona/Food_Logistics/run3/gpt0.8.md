**Goal Model – Multi‑Robot Food Delivery System**

| **Name**                  | **Text**                                                                  | **Runtime**                                                                  | **Goal Type** | **Target Condition / Enquired Information**        | **Relation** | **Ground truth I**                                    | **Ground truth C** | **Ground truth E** |
| ------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------- | -------------------------------------------------- | ------------ | ----------------------------------------------------- | ------------------ | ------------------ |
| G1: Root                  | Ensure timely delivery of food meals to inpatient rooms                   | `#` (parallel)                                                               | Perform       | –                                                  | N/A          | OK                                                    |  OK                  |                    |
| G2: Receive order         | Receive delivery request from the kitchen                                 | `-`                                                                          | Perform       | –                                                  | AND          | OK                                                    |  OK                  |                    |
| G3: Transport food        | Transport food to the inpatient room                                      | `;` (sequential)                                                             | Perform       | –                                                  | AND          | OK                                                    |  OK                  |                    |
| G4: Deliver food          | Deliver food to the patient (table or hand-over)                          | `FALLBACK(FALLBACK(G4.1,G4.2),G4.3)`                                         | Perform       | –                                                  | AND          | Achieve. Target condition: all food was delivered.    |  OK                  |                    |
| G4.1: Place on table      | Place the meal on the patient’s table (special manipulation)              | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G4.2: Hand over           | Hand over the meal to a human (patient, companion, nurse, or robot)       | `FALLBACK(FALLBACK(FALLBACK(FALLBACK(G4.2.1,G4.2.2),G4.2.3),G4.2.4),G4.2.5)` | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G4.3: Track & alert       | Track meal retrieval and alert if wrong meal is taken                     | `;`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G4.2.1: Query ability     | Query patient record for ability to retrieve meal & presence of companion | `-`                                                                          | Query         | “Can patient retrieve meal? Is companion present?” | OR           | OK                                                    |  OK                  |                  |
| G4.2.2: Hand to patient   | Hand the meal to the patient                                              | `-`                                                                          | Perform       | –                                                  | OR           | Ok                                                    |  OK                  |                    |
| G4.2.3: Hand to companion | Hand the meal to a companion visitor                                      | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G4.2.4: Hand to nurse     | Hand the meal to a nurse                                                  | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G4.2.5: Robot fetch       | Robot fetches the meal cooperatively (two robots)                         | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G5: Retrieve dishes       | Retrieve dirty dishes from the patient room                               | `FALLBACK(FALLBACK(G5.1,G5.2),G5.3)`                                         | Perform       | –                                                  | AND          | Achieve. Target condition: all dishes were retrieved. |  OK                  |                    |
| G5.1: Unassisted          | Retrieve dishes without assistance                                        | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G5.2: Robot-robot         | Two robots cooperate to retrieve dishes                                   | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G5.3: Robot-human         | Robot retrieves dishes with human assistance                              | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G6: Open door             | Open the patient-room door                                                | `FALLBACK(FALLBACK(G6.1,G6.2),G6.3)`                                         | Perform       | –                                                  | AND          | OK                                                    |  OK                  |                    |
| G6.1: Robot alone         | Robot opens the door by itself                                            | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G6.2: Robot-human         | Robot opens the door with a human                                         | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |
| G6.3: Robot-robot         | Two robots cooperate to open the door                                     | `-`                                                                          | Perform       | –                                                  | OR           | OK                                                    |  OK                  |                    |


---

### Tasks

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| AT1 | Receive order from kitchen | AND | kitchen | 1 |
| AT2 | Pick up food from kitchen | AND | kitchen | 1 |
| AT3 | Move to patient room | AND | hallway → room | 1 |
| AT4 | Manipulate robot to place meal on table | AND | patient‑room table | 1 |
| AT5 | Robot handover to patient | AND | patient‑room | 1 |
| AT6 | Robot handover to companion | AND | patient‑room | 1 |
| AT7 | Robot handover to nurse | AND | patient‑room | 1 |
| AT8 | Robot fetch meal cooperatively | AND | patient‑room | 2 |
| AT9 | Track meal retrieval | AND | patient‑room | 1 |
| AT10 | Alert wrong meal | AND | patient‑room | 1 |
| AT11 | Robot picks up dish | AND | patient‑room | 1 |
| AT12 | Two robots pick up dish cooperatively | AND | patient‑room | 2 |
| AT13 | Robot fetch dish with human assistance | AND | patient‑room | 1 |
| AT14 | Robot opens door | AND | room door | 1 |
| AT15 | Robot opens door with human | AND | room door | 1 |
| AT16 | Two robots open door | AND | room door | 2 |

---

### Summary Table (Goals + Tasks)

| **ID** | **Title** | **Type** | **Runtime / Relation** | **Location / Robots** |
|--------|-----------|----------|------------------------|-----------------------|
| G1 | Root | Perform | `#` (parallel) | – |
| G2 | Receive order | Perform | AND | – |
| AT1 | Receive order | – | AND | kitchen, 1 |
| G3 | Transport food | Perform | `;` (sequential) | – |
| AT2 | Pick up food | – | AND | kitchen, 1 |
| AT3 | Move to room | – | AND | hallway→room, 1 |
| G4 | Deliver food | Perform | `FALLBACK(FALLBACK(G4.1,G4.2),G4.3)` | – |
| G4.1 | Place on table | Perform | OR | – |
| AT4 | Place meal on table | – | AND | patient‑room table, 1 |
| G4.2 | Hand over | Perform | `FALLBACK(FALLBACK(FALLBACK(FALLBACK(G4.2.1,G4.2.2),G4.2.3),G4.2.4),G4.2.5)` | – |
| G4.2.1 | Query ability | Query | OR | – |
| AT5 | Hand to patient | – | AND | patient‑room, 1 |
| AT6 | Hand to companion | – | AND | patient‑room, 1 |
| AT7 | Hand to nurse | – | AND | patient‑room, 1 |
| AT8 | Robot fetch meal | – | AND | patient‑room, 2 |
| G4.3 | Track & alert | Perform | `;` | – |
| AT9 | Track retrieval | – | AND | patient‑room, 1 |
| AT10 | Alert wrong meal | – | AND | patient‑room, 1 |
| G5 | Retrieve dishes | Perform | `FALLBACK(FALLBACK(G5.1,G5.2),G5.3)` | – |
| G5.1 | Unassisted | Perform | OR | – |
| AT11 | Pick up dish | – | AND | patient‑room, 1 |
| G5.2 | Robot‑robot | Perform | OR | – |
| AT12 | Two robots pick dish | – | AND | patient‑room, 2 |
| G5.3 | Robot‑human | Perform | OR | – |
| AT13 | Robot fetch dish with human | – | AND | patient‑room, 1 |
| G6 | Open door | Perform | `FALLBACK(FALLBACK(G6.1,G6.2),G6.3)` | – |
| G6.1 | Robot alone | Perform | OR | – |
| AT14 | Robot opens door | – | AND | room door, 1 |
| G6.2 | Robot‑human | Perform | OR | – |
| AT15 | Robot opens door with human | – | AND | room door, 1 |
| G6.3 | Robot‑robot | Perform | OR | – |
| AT16 | Two robots open door | – | AND | room door, 2 |

---

### Logical Relationships (Tree Structure)

```
G1 -> G2, G3, G4, G5, G6 [AND][#]

G2 -> AT1 [AND]
G3 -> AT2, AT3 [AND][;]
G4 -> G4.1, G4.2, G4.3 [OR][FALLBACK(FALLBACK(G4.1,G4.2),G4.3)]
G4.1 -> AT4 [AND]
G4.2 -> G4.2.1, G4.2.2, G4.2.3, G4.2.4, G4.2.5 [OR][FALLBACK(FALLBACK(FALLBACK(FALLBACK(G4.2.1,G4.2.2),G4.2.3),G4.2.4),G4.2.5)]
G4.2.1 -> (query) [AND]
G4.2.2 -> AT5 [AND]
G4.2.3 -> AT6 [AND]
G4.2.4 -> AT7 [AND]
G4.2.5 -> AT8 [AND]
G4.3 -> AT9, AT10 [AND][;]

G5 -> G5.1, G5.2, G5.3 [OR][FALLBACK(FALLBACK(G5.1,G5.2),G5.3)]
G5.1 -> AT11 [AND]
G5.2 -> AT12 [AND]
G5.3 -> AT13 [AND]

G6 -> G6.1, G6.2, G6.3 [OR][FALLBACK(FALLBACK(G6.1,G6.2),G6.3)]
G6.1 -> AT14 [AND]
G6.2 -> AT15 [AND]
G6.3 -> AT16 [AND]
```

This model captures all intentional objectives, decomposes them into actionable tasks, and explicitly defines the execution semantics (parallel, sequential, fallback) and the logical relations among goals and tasks for the multi‑robot food delivery system.
