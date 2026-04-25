**Goal Model – Multi‑Robot Food Delivery**

| **Name**   | **Text**                                                                                              | **Runtime**                          | **Goal Type** | **Target Condition / Enquired Information**                  | **Relation**        | **Ground truth I**                                    | **Ground truth C** | **Ground truth E** |
| ---------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------- | ------------------------------------------------------------ | ------------------- | ----------------------------------------------------- | ------------------ | ------------------ |
| **G1**     | Deliver food from kitchen to inpatient room (pickup, transport, delivery, door opening, dish cleanup) | `;`                                  | Perform       | Food delivered to patient/table, door opened, dishes cleaned | – (root)            | OK                                                    | OK                 |                    |
| **G1.1**   | Receive delivery request                                                                              | `-`                                  | Perform       | Request received                                             | AND (child of G1)   | OK                                                    | OK                 |                    |
| **G2**     | Acquire and transport meal(s)                                                                         | `;`                                  | Perform       | Meal(s) in robot’s tray and at room                          | AND (child of G1)   | OK                                                    | OK                 |                    |
| **G2.1**   | Pick up meal(s) from kitchen                                                                          | `-`                                  | Perform       | Meal(s) in robot’s tray                                      | AND (child of G2)   | Achieve. Target condition: all meals were picked up   | OK                 |                    |
| **G2.2**   | Transport meal(s) to room                                                                             | `-`                                  | Perform       | Meal(s) at room                                              | AND (child of G2)   | OK                                                    | OK                 |                    |
| **G6**     | Open room door                                                                                        | `FALLBACK(FALLBACK(G6.1,G6.2),G6.3)` | Perform       | Door open                                                    | AND (child of G2)   | OK                                                    | OK                 |                    |
| **G6.1**   | Open door alone                                                                                       | `-`                                  | Perform       | Door open                                                    | OR (child of G6)    | OK                                                    | OK                 |                    |
| **G6.2**   | Open door with human                                                                                  | `-`                                  | Perform       | Door open                                                    | OR (child of G6)    | OK                                                    | OK                 |                    |
| **G6.3**   | Open door with robot                                                                                  | `-`                                  | Perform       | Door open                                                    | OR (child of G6)    | OK                                                    | OK                 |                    |
| **G3**     | Query patient retrieval capability                                                                    | `-`                                  | Query         | Patient can retrieve meal from tray?                         | AND (child of G2)   | OK                                                    | OK                 |                    |
| **G4**     | Deliver meal                                                                                          | `FALLBACK(G4.1,G4.2)`                | Perform       | Meal delivered to patient/table                              | AND (child of G2)   | OK                                                    | OK                 |                    |
| **G4.1**   | Deliver to table                                                                                      | `-`                                  | Perform       | Meal on table                                                | OR (child of G4)    | OK                                                    | OK                 |                    |
| **G4.2**   | Hand over to patient                                                                                  | `;`                                  | Perform       | Patient has meal                                             | OR (child of G4)    | OK                                                    | OK                 |                    |
| **G4.2.1** | Hand over meal                                                                                        | `-`                                  | Perform       | Patient receives meal                                        | AND (child of G4.2) | OK                                                    | OK                 |                    |
| **G4.2.2** | Indicate meal                                                                                         | `-`                                  | Perform       | Patient knows which meal                                     | AND (child of G4.2) | OK                                                    | OK                 |                    |
| **G4.2.3** | Track retrieval                                                                                       | `-`                                  | Perform       | Retrieval logged                                             | AND (child of G4.2) | OK                                                    | OK                 |                    |
| **G4.2.4** | Alert wrong meal                                                                                      | `-`                                  | Perform       | Wrong meal detected                                          | AND (child of G4.2) | OK                                                    | OK                 |                    |
| **G5**     | Dish retrieval                                                                                        | `;`                                  | Perform       | Dishes cleaned                                               | AND (child of G1)   | Achieve. Target condition: all dishes were retrieved. | OK                 |                    |
| **G5.1**   | Identify dirty dishes                                                                                 | `-`                                  | Perform       | Dishes identified                                            | AND (child of G5)   | OK                                                    | OK                 |                    |
| **G5.2**   | Retrieve dishes                                                                                       | `-`                                  | Perform       | Dishes removed                                               | AND (child of G5)   | OK                                                    | OK                 |                    |
| **G5.3**   | Dispose dishes                                                                                        | `-`                                  | Perform       | Dishes disposed                                              | AND (child of G5)   | OK                                                    | OK                 |                    |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Receive delivery request from kitchen | AND (child of G1.1) | kitchen | 1 |
| **AT2** | Query whether patient can retrieve meal from robot tray | AND (child of G3) | room | 1 |
| **AT3** | Pick up meal(s) from kitchen | AND (child of G2.1) | kitchen | 1 |
| **AT4** | Transport meal(s) from kitchen to inpatient room | AND (child of G2.2) | hallway → room | 1 |
| **AT5** | Deliver meal onto patient’s table | AND (child of G4.1) | room | 1 |
| **AT6** | Hand over meal to patient | AND (child of G4.2.1) | room | 1 |
| **AT7** | Indicate which meal to retrieve | AND (child of G4.2.2) | room | 1 |
| **AT8** | Track when and where meal was retrieved | AND (child of G4.2.3) | room | 1 |
| **AT9** | Alert if wrong meal retrieved | AND (child of G4.2.4) | room | 1 |
| **AT10** | Identify dirty dishes in room | AND (child of G5.1) | room | 1 |
| **AT11** | Retrieve dirty dishes from room | AND (child of G5.2) | room | 1–2 |
| **AT12** | Dispose dishes in kitchen | AND (child of G5.3) | kitchen | 1 |
| **AT13** | Robot opens door alone | AND (child of G6.1) | door | 1 |
| **AT14** | Robot cooperates with human to open door | AND (child of G6.2) | door | 1 |
| **AT15** | Two robots cooperate to open door | AND (child of G6.3) | door | 2 |

---

### Logical Relationships (Tree)

```
G1 -> G1.1, G2, G5 [AND][;]
G1.1 -> AT1 [AND]
G2 -> G2.1, G2.2, G6, G3, G4 [AND][;]
G2.1 -> AT3 [AND]
G2.2 -> AT4 [AND]
G6 -> G6.1, G6.2, G6.3 [OR][FALLBACK(FALLBACK(G6.1,G6.2),G6.3)]
G6.1 -> AT13 [AND]
G6.2 -> AT14 [AND]
G6.3 -> AT15 [AND]
G3 -> AT2 [AND]
G4 -> G4.1, G4.2 [OR][FALLBACK(G4.1,G4.2)]
G4.1 -> AT5 [AND]
G4.2 -> G4.2.1, G4.2.2, G4.2.3, G4.2.4 [AND][;]
G4.2.1 -> AT6 [AND]
G4.2.2 -> AT7 [AND]
G4.2.3 -> AT8 [AND]
G4.2.4 -> AT9 [AND]
G5 -> G5.1, G5.2, G5.3 [AND][;]
G5.1 -> AT10 [AND]
G5.2 -> AT11 [AND]
G5.3 -> AT12 [AND]
```

---

**Summary**

The model decomposes the high‑level mission “deliver food from kitchen to inpatient room” into a hierarchy of **perform**, **query**, and **achieve** goals, each mapped to concrete, executable **tasks**. The runtime annotations (`;`, `#`, `FALLBACK`) capture the required sequencing, parallelism, and fallback strategies (e.g., door opening, delivery method selection). The logical relationships table shows the exact parent‑child links and the execution semantics for each branch of the mission.
