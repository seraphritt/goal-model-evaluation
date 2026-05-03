**Goal Model – Multi‑Robot Food Delivery**

| **Name** | **Text**                           | **Runtime**                           | **Goal Type** | **Target Condition / Enquired Information**                        | **Relation** | **Ground Truth I** | **Ground Truth G** | **Consensus** |
| -------- | ---------------------------------- | ------------------------------------- | ------------- | ------------------------------------------------------------------ | ------------ | ------------------ | ------------------ | ------------- |
| G1       | Deliver food to inpatient room     | G2;G3;G4;G5;G6                        | Achieve       | Food delivered to the room table **or** patient retrieves the meal | AND          |  Perform                  |                    |               |
| G2       | Query delivery request             | –                                     | Query         | Order details (meal type, quantity, patient ID)                    | AND          |  OK                  |                    |               |
| G3       | Transport food to room             | –                                     | Perform       | –                                                                  | AND          |  OK                  |                    |               |
| G4       | Deliver food to patient            | FALLBACK(G4.1, G4.2)                  | Perform       | –                                                                  | AND          |  Achieve. Target condition: all food was delivered.                  |                    |               |
| G4.1     | Deliver to table                   | –                                     | Perform       | –                                                                  | AND          |  OK                  |                    |               |
| G4.2     | Provide tray for retrieval         | AND(G4.2.1, FALLBACK(G4.2.3, G4.2.2)) | Perform       | –                                                                  | AND          |  OK                  |                    |               |
| G4.2.1   | Query patient retrieval capability | –                                     | Query         | Patient’s ability to fetch from tray (yes/no)                      | AND          |  OK                  |                    |               |
| G4.2.3   | Place food on tray                 | –                                     | Perform       | –                                                                  | AND          |  OK                  |                    |               |
| G4.2.2   | Request assistance                 | –                                     | Perform       | –                                                                  | AND          |  OK                  |                    |               |
| G5       | Track meal retrieval               | –                                     | Achieve       | Retrieval events logged (who, when, which meal)                    | AND          |  OK                  |                    |               |
| G6       | Alert wrong meal retrieval         | –                                     | Perform       | –                                                                  | AND          |  OK                  |                    |               |
| G7       | Retrieve dirty dishes              | FALLBACK(G7.1, FALLBACK(G7.2, G7.3))  | Perform       | –                                                                  | AND          |  Achieve. Target condition: all dishes were retrieved                  |                    |               |
| G7.1     | Unassisted retrieval               | –                                     | Perform       | –                                                                  | AND          | OK                   |                    |               |
| G7.2     | Cooperation with two robots        | –                                     | Perform       | –                                                                  | AND          | OK                   |                    |               |
| G7.3     | Cooperation with human             | –                                     | Perform       | –                                                                  | AND          | OK                   |                    |               |
| G8       | Open room door                     | FALLBACK(G8.1, G8.2)                  | Perform       | –                                                                  | AND          | OK                   |                    |               |
| G8.1     | Open door alone                    | –                                     | Perform       | –                                                                  | AND          | OK                   |                    |               |
| G8.2     | Open door with assistance          | –                                     | Perform       | –                                                                  | AND          | OK                   |                    |               |
| G9       | Respond to call for dish pickup    | AND(AT13, AT14)                       | Perform       | –                                                                  | AND          | OK                   |                    |               |


---

**Task Model**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| AT1 | Query kitchen for order | AND | kitchen | 1 |
| AT2 | Move to room | AND | from kitchen to room | 1 |
| AT3 | Place food on table | AND | room table | 1 |
| AT4 | Query patient record | AND | patient record system | 1 |
| AT5 | Request assistance | AND | room | 1 |
| AT6 | Monitor retrieval events | AND | room | 1 |
| AT7 | Alert wrong meal retrieval | AND | room | 1 |
| AT8 | Pick up dishes | AND | room | 1 |
| AT9 | Coordinate with another robot | AND | room | 2 |
| AT10 | Request human | AND | room | 1 |
| AT11 | Open door | AND | room door | 1 |
| AT12 | Request assistance to open door | AND | room door | 1 |
| AT13 | Wait for call | AND | room | 1 |
| AT14 | Pick up dishes after call | AND | room | 1 |
| AT15 | Place food on tray | AND | room | 1 |

---

### Logical Relationships (Tree Structure)

```
G1 -> G2, G3, G4, G5, G6 [AND] (sequential)
G4 -> G4.1, G4.2 [AND] (fallback)
G4.2 -> G4.2.1, G4.2.3, G4.2.2 [AND] (fallback between 3 and 2)
G4.1 -> AT3 [AND]
G4.2.1 -> AT4 [AND]
G4.2.3 -> AT15 [AND]
G4.2.2 -> AT5 [AND]
G5 -> AT6 [AND]
G6 -> AT7 [AND]
G7 -> G7.1, G7.2, G7.3 [AND] (fallback)
G7.1 -> AT8 [AND]
G7.2 -> AT9 [AND]
G7.3 -> AT10 [AND]
G8 -> G8.1, G8.2 [AND] (fallback)
G8.1 -> AT11 [AND]
G8.2 -> AT12 [AND]
G9 -> AT13, AT14 [AND]
```

This goal‑task decomposition captures the full multi‑robot food delivery mission, including uncertainty handling, fallback strategies, and coordination with humans or other robots.
