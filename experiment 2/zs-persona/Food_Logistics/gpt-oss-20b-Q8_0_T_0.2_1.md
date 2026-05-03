**Goal Model – Multi‑Robot Food Delivery**

| **Name** | **Text**                                                     | **Runtime**                                          | **Goal Type** | **Target Condition / Enquired Information**                                             | **Relation** | **New Ground Truth I** | **New Ground Truth G** | **Consensus** |
| -------- | ------------------------------------------------------------ | ---------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------- | ------------ | ------------------ | ------------------ | ------------- |
| G1       | Deliver food from the kitchen to an inpatient room           | G2;G3;G4;G5;G6                                       | Achieve       | Food is on the patient’s table or has been retrieved by the patient / nurse / companion | – (root)     | Achieve                   |  Achieve                  |               |
| G2       | Receive delivery request from the kitchen                    | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G3       | Determine who can retrieve the food                          | –                                                    | Query         | *Patient retrieval capability* and *presence of a companion*                            | AND          | OK                   |                    |               |
| G4       | Execute the delivery (choose the appropriate retrieval mode) | FALLBACK(FALLBACK(FALLBACK(G4.1, G4.2), G4.3), G4.4) | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G4.1     | Patient retrieves the food                                   | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G4.2     | Nurse retrieves the food                                     | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G4.3     | Companion retrieves the food                                 | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G4.4     | Deliver the food to the patient’s table                      | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G5       | Retrieve dirty dishes from the room                          | FALLBACK(G5.1, FALLBACK(G5.2, G5.3))                 | Perform       | –                                                                                       | AND          | Achieve. Target condition: all dishes were retrieved.                   |                    |               |
| G5.1     | Unassisted dish retrieval                                    | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G5.2     | Robot-robot dish retrieval                                   | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G5.3     | Robot-human dish retrieval                                   | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G6       | Open the room door (if required)                             | FALLBACK(G6.1, FALLBACK(G6.2, G6.3))                 | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G6.1     | Robot opens the door alone                                   | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G6.2     | Robot-human door opening                                     | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |
| G6.3     | Robot-robot door opening                                     | –                                                    | Perform       | –                                                                                       | AND          | OK                   |                    |               |

---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| AT1 | Receive request from kitchen | AND | Kitchen | 1 |
| AT2 | Query patient record & companion presence | AND | Hospital Database | 1 |
| AT3 | Indicate meal to patient | AND | Patient room | 1 |
| AT4 | Wait for patient to retrieve meal | AND | Patient room | 1 |
| AT5 | Confirm patient retrieval & verify meal | AND | Patient room | 1 |
| AT6 | Indicate meal to nurse | AND | Patient room | 1 |
| AT7 | Wait for nurse to retrieve meal | AND | Patient room | 1 |
| AT8 | Confirm nurse retrieval & verify meal | AND | Patient room | 1 |
| AT9 | Indicate meal to companion | AND | Patient room | 1 |
| AT10 | Wait for companion to retrieve meal | AND | Patient room | 1 |
| AT11 | Confirm companion retrieval & verify meal | AND | Patient room | 1 |
| AT12 | Deliver food to patient’s table | AND | Patient room table | 1 |
| AT13 | Confirm table delivery | AND | Patient room table | 1 |
| AT14 | Retrieve dishes unassisted | AND | Patient room | 1 |
| AT15 | Confirm dish retrieval | AND | Patient room | 1 |
| AT16 | Coordinate with Robot B for dish retrieval | AND | Patient room | 2 |
| AT17 | Retrieve dishes together | AND | Patient room | 2 |
| AT18 | Confirm joint dish retrieval | AND | Patient room | 2 |
| AT19 | Request human assistance for dish retrieval | AND | Patient room | 1 |
| AT20 | Retrieve dishes with human | AND | Patient room | 1 |
| AT21 | Confirm human‑assisted dish retrieval | AND | Patient room | 1 |
| AT22 | Open the door | AND | Room door | 1 |
| AT23 | Request human to open door | AND | Room door | 1 |
| AT24 | Human opens the door | AND | Room door | 1 |
| AT25 | Coordinate with Robot B to open door | AND | Room door | 2 |
| AT26 | Open door together | AND | Room door | 2 |

---

### Logical Relationships Summary

```
G1  -> G2, G3, G4, G5, G6 [AND][sequential]
G2  -> AT1 [AND][-]
G3  -> AT2 [AND][-]
G4  -> G4.1, G4.2, G4.3, G4.4 [AND][FALLBACK(FALLBACK(FALLBACK(G4.1, G4.2), G4.3), G4.4)]
G4.1 -> AT3, AT4, AT5 [AND][AND]
G4.2 -> AT6, AT7, AT8 [AND][AND]
G4.3 -> AT9, AT10, AT11 [AND][AND]
G4.4 -> AT12, AT13 [AND][AND]
G5  -> G5.1, G5.2, G5.3 [AND][FALLBACK(G5.1, FALLBACK(G5.2, G5.3))]
G5.1 -> AT14, AT15 [AND][AND]
G5.2 -> AT16, AT17, AT18 [AND][AND]
G5.3 -> AT19, AT20, AT21 [AND][AND]
G6  -> G6.1, G6.2, G6.3 [AND][FALLBACK(G6.1, FALLBACK(G6.2, G6.3))]
G6.1 -> AT22 [AND][-]
G6.2 -> AT23, AT24 [AND][AND]
G6.3 -> AT25, AT26 [AND][AND]
```

This goal‑task tree captures the full multi‑robot food delivery mission, including decision points, fallback strategies, and cooperation with humans or other robots.
