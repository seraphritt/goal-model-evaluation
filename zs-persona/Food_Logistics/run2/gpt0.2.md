**Goal Model – Multi‑Robot Food Delivery**

---

## 1.  Goal Table  

| Name     | Text                                                                                    | Runtime                          | Goal Type | Target Condition / Enquired Information  | Relation | Ground truth I                                      | Ground truth C | Ground truth E |
| -------- | --------------------------------------------------------------------------------------- | -------------------------------- | --------- | ---------------------------------------- | -------- | --------------------------------------------------- | -------------- | -------------- |
| **G1**   | Deliver food from kitchen to inpatient room (including door opening and dish retrieval) | `;` (sequential) of G2, G1.1, G6 | Perform   | –                                        | –        | OK                                                  | OK             |                |
| **G2**   | Open the room door to allow robot entry                                                 | `FALLBACK(G19,G20)`              | Perform   | –                                        | AND      | OK                                                  | OK             |                |
| **G19**  | Robot opens the room door                                                               | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G20**  | Human opens the room door                                                               | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G1.1** | Deliver food to the inpatient room                                                      | `FALLBACK(G4,G5)`                | Perform   | –                                        | AND      | Achieve. Target condition: all food was delivered.  | OK             |                |
| **G4**   | Fetch meal from robot’s tray with cooperation                                           | `AND(G3,G7,G8,G10,G13)`          | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G3**   | Query if inpatient can retrieve meal from tray                                          | `-`                              | Query     | “Can inpatient retrieve meal from tray?” | AND      | OK                                                  | OK             |                |
| **G7**   | Obtain cooperation from human or robot                                                  | `FALLBACK(G14,G15)`              | Perform   | –                                        | AND      | OK                                                  | OK             |                |
| **G14**  | Human cooperates with robot                                                             | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G15**  | Robot cooperates with another robot                                                     | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G8**   | Robot indicates which meal to retrieve                                                  | `-`                              | Perform   | –                                        | AND      | OK                                                  | OK             |                |
| **G10**  | Retrieve meal from tray                                                                 | `FALLBACK(G11,G12)`              | Perform   | –                                        | AND      | OK                                                  | OK             |                |
| **G11**  | Human retrieves meal                                                                    | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G12**  | Robot retrieves meal                                                                    | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G13**  | Alert if wrong meal retrieved                                                           | `-`                              | Perform   | –                                        | AND      | OK                                                  | OK             |                |
| **G5**   | Deliver meal onto room table                                                            | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G6**   | Retrieve dirty dishes from room                                                         | `FALLBACK(G16,G17,G18)`          | Perform   | –                                        | AND      | Achive. Target conditon: all dishes were retrieved. | OK             |                |
| **G16**  | Retrieve dishes unassisted                                                              | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G17**  | Retrieve dishes with robot cooperation                                                  | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |
| **G18**  | Retrieve dishes with human cooperation                                                  | `-`                              | Perform   | –                                        | OR       | OK                                                  | OK             |                |


---

## 2.  Task Table  

| Name | Text | Relation | Location | Number of Robots |
|------|------|----------|----------|------------------|
| **AT1** | Robot opens the room door | AND | room door | 1 |
| **AT3** | Robot requests human cooperation | AND | room | 1 |
| **AT4** | Robot requests robot cooperation | AND | room | 1 |
| **AT5** | Robot indicates which meal to retrieve | AND | robot | 1 |
| **AT7** | Robot retrieves meal from tray | AND | room | 1 |
| **AT8** | Robot alerts if wrong meal retrieved | AND | room | 1 |
| **AT9** | Robot delivers meal onto room table | AND | room table | 1 |
| **AT10** | Robot retrieves dishes unassisted | AND | room | 1 |
| **AT11** | Robot retrieves dishes with another robot | AND | room | 2 |
| **AT12** | Robot retrieves dishes with human cooperation | AND | room | 1 |

---

## 3.  Summary Table (Goals + Tasks)

| ID | Type | Title | Text | Runtime / Relation | Location / Target / Enquired Info | # Robots |
|----|------|-------|------|--------------------|-----------------------------------|----------|
| G1 | Goal | Deliver food to inpatient room | Deliver food from kitchen to inpatient room (door opening & dish retrieval) | `;` (sequential) of G2, G1.1, G6 | – | – |
| G2 | Goal | Open door | Open the room door to allow robot entry | `FALLBACK(G19,G20)` | – | – |
| G19 | Goal | Robot open door | Robot opens the room door | `-` | – | – |
| AT1 | Task | Robot opens door | Robot opens the room door | AND | room door | 1 |
| G20 | Goal | Human open door | Human opens the room door | `-` | – | – |
| G1.1 | Goal | Delivery | Deliver food to the inpatient room | `FALLBACK(G4,G5)` | – | – |
| G4 | Goal | Fetch from tray | Fetch meal from robot’s tray with cooperation | `AND(G3,G7,G8,G10,G13)` | – | – |
| G3 | Goal | Query inpatient retrieval capability | Query if inpatient can retrieve meal from tray | `-` | “Can inpatient retrieve meal from tray?” | – |
| G7 | Goal | Get cooperation | Obtain cooperation from human or robot | `FALLBACK(G14,G15)` | – | – |
| G14 | Goal | Human cooperation | Human cooperates with robot | `-` | – | – |
| AT3 | Task | Robot requests human cooperation | Robot requests human cooperation | AND | room | 1 |
| G15 | Goal | Robot cooperation | Robot cooperates with another robot | `-` | – | – |
| AT4 | Task | Robot requests robot cooperation | Robot requests robot cooperation | AND | room | 1 |
| G8 | Goal | Indicate meal | Robot indicates which meal to retrieve | `-` | – | – |
| AT5 | Task | Robot indicates meal | Robot indicates which meal to retrieve | AND | robot | 1 |
| G10 | Goal | Retrieve meal | Retrieve meal from tray | `FALLBACK(G11,G12)` | – | – |
| G11 | Goal | Human retrieve meal | Human retrieves meal | `-` | – | – |
| AT7 | Task | Robot retrieves meal | Robot retrieves meal from tray | AND | room | 1 |
| G12 | Goal | Robot retrieve meal | Robot retrieves meal | `-` | – | – |
| G13 | Goal | Alert wrong meal | Alert if wrong meal retrieved | `-` | – | – |
| AT8 | Task | Robot alerts wrong meal | Robot alerts if wrong meal retrieved | AND | room | 1 |
| G5 | Goal | Deliver to table | Deliver meal onto room table | `-` | – | – |
| AT9 | Task | Robot delivers meal to table | Robot delivers meal onto room table | AND | room table | 1 |
| G6 | Goal | Retrieve dirty dishes | Retrieve dirty dishes from room | `FALLBACK(G16,G17,G18)` | – | – |
| G16 | Goal | Unassisted retrieval | Retrieve dishes unassisted | `-` | – | – |
| AT10 | Task | Robot retrieves dishes unassisted | Robot retrieves dishes unassisted | AND | room | 1 |
| G17 | Goal | Robot cooperation retrieval | Retrieve dishes with robot cooperation | `-` | – | – |
| AT11 | Task | Robot retrieves dishes with cooperation | Robot retrieves dishes with another robot | AND | room | 2 |
| G18 | Goal | Human cooperation retrieval | Retrieve dishes with human cooperation | `-` | – | – |
| AT12 | Task | Robot retrieves dishes with human | Robot retrieves dishes with human cooperation | AND | room | 1 |

---

## 4.  Logical Relationships  

```
G1  -> G2, G1.1, G6          [AND][sequential]
G2  -> G19, G20              [OR][FALLBACK]
G1.1 -> G4, G5              [OR][FALLBACK]
G4  -> G3, G7, G8, G10, G13 [AND][parallel]
G7  -> G14, G15              [OR][FALLBACK]
G10 -> G11, G12              [OR][FALLBACK]
G6  -> G16, G17, G18         [OR][FALLBACK]
```

Each arrow indicates the parent goal’s relation to its children.  
- **AND** means all children must be satisfied.  
- **OR** (used with `FALLBACK`) means the first child is attempted; if it fails, the next is tried.  
- **Sequential** (`;`) indicates the children are executed in order.  
- **Parallel** (`#`) indicates the children can be executed concurrently (used implicitly in AND decompositions where order is irrelevant).  

This goal model captures the decision logic (fetch vs. deliver), cooperation requirements, uncertainty handling, and the necessary robot actions for a complete multi‑robot food‑delivery mission.
