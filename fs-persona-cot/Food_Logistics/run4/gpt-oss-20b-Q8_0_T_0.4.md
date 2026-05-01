**Goal‑Model – Multi‑Robot Food Delivery & Dish Retrieval**

| **Name**   | **Text**                       | **Runtime**                                  | **Goal Type** | **Target Condition / Enquired Info**                                                         | **Relation**              | **Justification**                                                                                                               | **Ground truth I**                                   | **Ground truth C** | **Consensus**                                        |
| ---------- | ------------------------------ | -------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ---------------------------------------------------- |
| **G0**     | Hospital Service               | **#**                                        | **Achieve**   | “All required services (food delivery and dish retrieval) have been successfully completed.” | – (root)                  | Root of the mission – both food delivery and dish retrieval are required for the hospital service to be considered complete.    | Perform.                                             | Perform            | Perform.                                             |
| **G1**     | Deliver food to inpatient room | **;**                                        | **Achieve**   | “Food has been delivered to the inpatient room.”                                             | AND (G5, FALLBACK(G2,G3)) | Delivery must occur after the door is opened (G5). The delivery itself can be either table-delivery (G2) or patient-fetch (G3). | OK                                                   | Perform            | OK                                                   |
| **G5**     | Open room door                 | **FALLBACK(G5.1,G5.2)**                      | **Perform**   | –                                                                                            | AND (G1)                  | Door opening is a prerequisite for any delivery. Either the robot or a human can open it.                                       | OK                                                   | Ok                 | OK                                                   |
| **G5.1**   | Robot opens door               | **-**                                        | **Perform**   | –                                                                                            | OR (G5.2)                 | Robot can physically open the door.                                                                                             | OK                                                   | Ok                 | OK                                                   |
| **G5.2**   | Human opens door               | **-**                                        | **Perform**   | –                                                                                            | OR (G5.1)                 | Human can open the door if the robot cannot.                                                                                    | OK                                                   | Ok                 | OK                                                   |
| **G2**     | Deliver into room table        | **;**                                        | **Perform**   | –                                                                                            | FALLBACK(G3) (within G1)  | Table-delivery is one valid delivery mode.                                                                                      | OK                                                   | Ok                 | OK                                                   |
| **G2.1**   | Transport food to room         | **-**                                        | **Perform**   | –                                                                                            | AND (G2.2,G2.3,G2.4)      | Robot must move the food from kitchen to the room.                                                                              | OK                                                   | Ok                 | OK                                                   |
| **G2.2**   | Deliver into table             | **-**                                        | **Perform**   | –                                                                                            | AND (G2.3,G2.4)           | Robot places the food on the table.                                                                                             | OK                                                   | Ok                 | OK                                                   |
| **G2.3**   | Track delivery                 | **-**                                        | **Perform**   | –                                                                                            | AND (G2.4)                | Robot verifies that the food is on the table.                                                                                   | OK                                                   | Ok                 | OK                                                   |
| **G2.4**   | Alert wrong meal               | **-**                                        | **Perform**   | –                                                                                            | –                         | Robot notifies staff if the wrong meal was delivered.                                                                           | OK                                                   | Ok                 | OK                                                   |
| **G3**     | Patient fetch from tray        | **FALLBACK(G3.1,G3.2)**                      | **Perform**   | –                                                                                            | FALLBACK(G2) (within G1)  | Patient-fetch is the alternative delivery mode.                                                                                 | OK                                                   | Ok                 | OK                                                   |
| **G3.1**   | Query & deliver to patient     | **;**                                        | **Perform**   | –                                                                                            | AND (G3.2)                | First determine if patient can fetch, then hand over.                                                                           | OK                                                   | Ok                 | OK                                                   |
| **G3.1.1** | Query patient fetch capability | **-**                                        | **Query**     | “patient fetch capability”                                                                   | AND (G3.1.2)              | Information is uncertain; must be queried from patient record.                                                                  | OK                                                   | Ok                 | OK                                                   |
| **G3.1.2** | Deliver to patient             | **-**                                        | **Perform**   | –                                                                                            | AND (G3.1.3)              | Robot hands the food to the patient.                                                                                            | OK                                                   | Ok                 | OK                                                   |
| **G3.1.3** | Track retrieval                | **-**                                        | **Perform**   | –                                                                                            | AND (G3.1.4)              | Robot monitors that the patient actually takes the food.                                                                        | OK                                                   | Ok                 | OK                                                   |
| **G3.1.4** | Alert wrong meal               | **-**                                        | **Perform**   | –                                                                                            | –                         | Robot notifies staff if the patient takes the wrong meal.                                                                       | OK                                                   | Ok                 | OK                                                   |
| **G3.2**   | Cooperation for fetching       | **FALLBACK(FALLBACK(G3.2.1,G3.2.2),G3.2.3)** | **Perform**   | –                                                                                            | –                         | If patient cannot fetch, robot seeks assistance from a companion, nurse, or another robot.                                      | OK                                                   | Ok                 | OK                                                   |
| **G3.2.1** | Companion fetch                | **-**                                        | **Perform**   | –                                                                                            | OR (G3.2.2)               | Companion can hand the food to the patient.                                                                                     | OK                                                   | Ok                 | OK                                                   |
| **G3.2.2** | Nurse fetch                    | **-**                                        | **Perform**   | –                                                                                            | OR (G3.2.3)               | Nurse can hand the food to the patient.                                                                                         | OK                                                   | Ok                 | OK                                                   |
| **G3.2.3** | Robot fetch                    | **-**                                        | **Perform**   | –                                                                                            | OR (G3.2.1)               | Robot can fetch the food itself if needed.                                                                                      | OK                                                   | Ok                 | OK                                                   |
| **G4**     | Retrieve dirty dishes          | **;**                                        | **Perform**   | –                                                                                            | AND (G0)                  | Dish retrieval is a separate service that runs concurrently with food delivery.                                                 | Achieve. Target condition: all dishes were retrieved | Ok                 | Achieve. Target condition: all dishes were retrieved |
| **G4.1**   | Identify dishes                | **-**                                        | **Perform**   | –                                                                                            | AND (G4.2)                | Robot scans the room for dirty dishes.                                                                                          | OK                                                   | Ok                 | OK                                                   |
| **G4.2**   | Retrieve dishes                | **FALLBACK(FALLBACK(G4.2.1,G4.2.2),G4.2.3)** | **Perform**   | –                                                                                            | AND (G4.3)                | Dishes can be retrieved alone, by two robots, or with a human.                                                                  | OK                                                   | Ok                 | OK                                                   |
| **G4.2.1** | Unassisted retrieval           | **-**                                        | **Perform**   | –                                                                                            | OR (G4.2.2)               | Robot can pick up small dishes alone.                                                                                           | OK                                                   | Ok                 | OK                                                   |
| **G4.2.2** | Two-robot retrieval            | **-**                                        | **Perform**   | –                                                                                            | OR (G4.2.3)               | Two robots cooperate for large or heavy dishes.                                                                                 | OK                                                   | Ok                 | OK                                                   |
| **G4.2.3** | Robot-human retrieval          | **-**                                        | **Perform**   | –                                                                                            | OR (G4.2.1)               | Robot assists a human in picking up dishes.                                                                                     | OK                                                   | Ok                 | OK                                                   |
| **G4.3**   | Transport dishes to kitchen    | **-**                                        | **Perform**   | –                                                                                            | AND (G4.4)                | Robot carries dishes back to the kitchen.                                                                                       | OK                                                   | Ok                 | OK                                                   |
| **G4.4**   | Dispose dishes                 | **-**                                        | **Perform**   | –                                                                                            | –                         | Robot disposes of the dishes in the kitchen sink.                                                                               | OK                                                   | Ok                 | OK                                                   |


---

### Task‑Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Pick up food from kitchen | AND (G2.1) | kitchen | 1 | Robot must acquire the meal before transport. |
| **AT2** | Transport food to room | AND (G2.1) | hospital corridor | 1 | Robot moves the meal to the patient’s room. |
| **AT3** | Deliver into table | AND (G2.2) | inpatient room | 1 | Robot places the meal on the table (special manipulation skill). |
| **AT4** | Track delivery on table | AND (G2.3) | inpatient room | 1 | Robot confirms the meal is on the table. |
| **AT5** | Alert wrong meal (table) | AND (G2.4) | inpatient room | 1 | Robot notifies staff if the wrong meal was placed. |
| **AT6** | Robot opens door | AND (G5.1) | room door | 1 | Robot can physically open the door. |
| **AT7** | Human opens door | AND (G5.2) | room door | 0 | Human action – no robot required. |
| **AT8** | Query patient fetch capability | AND (G3.1.1) | hospital server | 0 | Information is retrieved from patient record. |
| **AT9** | Deliver to patient | AND (G3.1.2) | inpatient room | 1 | Robot hands the meal to the patient. |
| **AT10** | Track patient retrieval | AND (G3.1.3) | inpatient room | 1 | Robot monitors that the patient takes the meal. |
| **AT11** | Alert wrong meal (patient) | AND (G3.1.4) | inpatient room | 1 | Robot notifies staff if the wrong meal was taken. |
| **AT12** | Companion fetch | AND (G3.2.1) | inpatient room | 0 | Companion physically fetches the meal. |
| **AT13** | Nurse fetch | AND (G3.2.2) | inpatient room | 0 | Nurse physically fetches the meal. |
| **AT14** | Robot fetch | AND (G3.2.3) | inpatient room | 1 | Robot fetches the meal itself. |
| **AT15** | Identify dishes | AND (G4.1) | inpatient room | 1 | Robot scans for dirty dishes. |
| **AT16** | Unassisted dish retrieval | AND (G4.2.1) | inpatient room | 1 | Robot picks up small dishes alone. |
| **AT17** | Two‑robot dish retrieval | AND (G4.2.2) | inpatient room | 2 | Two robots cooperate for large dishes. |
| **AT18** | Robot‑human dish retrieval | AND (G4.2.3) | inpatient room | 1 | Robot assists a human. |
| **AT19** | Transport dishes to kitchen | AND (G4.3) | hospital corridor | 1 | Robot carries dishes back to kitchen. |
| **AT20** | Dispose dishes | AND (G4.4) | kitchen | 1 | Robot disposes of dishes. |

---

### Summary Table (Goals & Tasks)

| **ID** | **Type** | **Description** | **Relation** | **Runtime** | **Justification** |
|--------|----------|-----------------|--------------|-------------|-------------------|
| G0 | Goal | Hospital Service | – (root) | # | Both food delivery and dish retrieval are required. |
| G1 | Goal | Deliver food to inpatient room | AND (G5, FALLBACK(G2,G3)) | ; | Door must be opened first; delivery can be table or patient‑fetch. |
| G5 | Goal | Open room door | FALLBACK(G5.1,G5.2) | – | Either robot or human can open. |
| G5.1 | Goal | Robot opens door | – | – | Robot can physically open. |
| G5.2 | Goal | Human opens door | – | – | Human can open. |
| G2 | Goal | Deliver into room table | ; | – | Table‑delivery is one delivery mode. |
| G2.1 | Goal | Transport food to room | – | – | Robot moves food. |
| G2.2 | Goal | Deliver into table | – | – | Robot places food. |
| G2.3 | Goal | Track delivery | – | – | Verify placement. |
| G2.4 | Goal | Alert wrong meal | – | – | Notify if wrong meal. |
| G3 | Goal | Patient fetch from tray | FALLBACK(G3.1,G3.2) | – | Patient‑fetch is alternative. |
| G3.1 | Goal | Query & deliver to patient | ; | – | Query capability then hand over. |
| G3.1.1 | Goal | Query patient fetch capability | – | – | Information uncertain. |
| G3.1.2 | Goal | Deliver to patient | – | – | Hand over. |
| G3.1.3 | Goal | Track retrieval | – | – | Monitor. |
| G3.1.4 | Goal | Alert wrong meal | – | – | Notify if wrong meal. |
| G3.2 | Goal | Cooperation for fetching | FALLBACK(FALLBACK(G3.2.1,G3.2.2),G3.2.3) | – | Seek assistance. |
| G3.2.1 | Goal | Companion fetch | – | – | Companion fetches. |
| G3.2.2 | Goal | Nurse fetch | – | – | Nurse fetches. |
| G3.2.3 | Goal | Robot fetch | – | – | Robot fetches. |
| G4 | Goal | Retrieve dirty dishes | ; | – | Concurrent with food delivery. |
| G4.1 | Goal | Identify dishes | – | – | Scan for dishes. |
| G4.2 | Goal | Retrieve dishes | FALLBACK(FALLBACK(G4.2.1,G4.2.2),G4.2.3) | – | Multiple retrieval modes. |
| G4.2.1 | Goal | Unassisted retrieval | – | – | Robot alone. |
| G4.2.2 | Goal | Two‑robot retrieval | – | – | Two robots cooperate. |
| G4.2.3 | Goal | Robot‑human retrieval | – | – | Robot assists human. |
| G4.3 | Goal | Transport dishes to kitchen | – | – | Carry back. |
| G4.4 | Goal | Dispose dishes | – | – | Dispose. |

---

### Logical Relationships (with Justifications)

| **Parent → Children** | **Relation** | **Runtime** | **Justification** |
|-----------------------|--------------|-------------|-------------------|
| **G0 → G1, G4** | AND | **#** | Food delivery and dish retrieval can occur in parallel; both must finish for the hospital service to be complete. |
| **G1 → G5, FALLBACK(G2,G3)** | AND | **;** | Door must be opened before any delivery; delivery can be table or patient‑fetch. |
| **G5 → G5.1, G5.2** | OR | **FALLBACK(G5.1,G5.2)** | Either the robot or a human can open the door. |
| **G2 → G2.1, G2.2, G2.3, G2.4** | AND | **;** | Transport, placement, verification, and error alert must all occur sequentially. |
| **G3 → G3.1, G3.2** | Fallback | **FALLBACK(G3.1,G3.2)** | First try patient‑fetch; if not possible, fall back to cooperation. |
| **G3.1 → G3.1.1, G3.1.2, G3.1.3, G3.1.4** | AND | **;** | Query, hand‑over, track, and alert must happen in order. |
| **G3.2 → G3.2.1, G3.2.2, G3.2.3** | Fallback | **FALLBACK(FALLBACK(G3.2.1,G3.2.2),G3.2.3)** | Try companion, then nurse, then robot if needed. |
| **G4 → G4.1, G4.2, G4.3, G4.4** | AND | **;** | Identification, retrieval, transport, and disposal must all happen sequentially. |
| **G4.2 → G4.2.1, G4.2.2, G4.2.3** | Fallback | **FALLBACK(FALLBACK(G4.2.1,G4.2.2),G4.2.3)** | Try unassisted, then two‑robot, then robot‑human. |

---

### Mapping of Tasks to Goals

| **Task** | **Goal(s) it fulfills** | **Relation** |
|----------|------------------------|--------------|
| AT1 | G2.1 | AND |
| AT2 | G2.1 | AND |
| AT3 | G2.2 | AND |
| AT4 | G2.3 | AND |
| AT5 | G2.4 | AND |
| AT6 | G5.1 | AND |
| AT7 | G5.2 | AND |
| AT8 | G3.1.1 | AND |
| AT9 | G3.1.2 | AND |
| AT10 | G3.1.3 | AND |
| AT11 | G3.1.4 | AND |
| AT12 | G3.2.1 | AND |
| AT13 | G3.2.2 | AND |
| AT14 | G3.2.3 | AND |
| AT15 | G4.1 | AND |
| AT16 | G4.2.1 | AND |
| AT17 | G4.2.2 | AND |
| AT18 | G4.2.3 | AND |
| AT19 | G4.3 | AND |
| AT20 | G4.4 | AND |

---

**Key Design Decisions & Justifications**

1. **Fallback vs OR** – The mission explicitly states that if one delivery mode fails, the other should be attempted. This is captured by `FALLBACK` operators.  
2. **Sequential vs Parallel** – Within each delivery mode, the steps must occur in a specific order (transport → place → verify → alert). Therefore, `;` is used.  
3. **Uncertainty Handling** – Query goals (`G3.1.1`) are used to obtain uncertain information (patient fetch capability, companion presence).  
4. **Cooperation** – Multiple cooperation options are represented by nested `FALLBACK` (or OR) to allow any one to succeed.  
5. **Parallel Root** – Food delivery and dish retrieval are independent services that can run concurrently, so the root uses `#`.  
6. **Task Mapping** – Every leaf goal is associated with a concrete task that specifies location and robot count, ensuring that the model is actionable.  

This goal‑model decomposes the multi‑robot mission into a clear, hierarchical structure that captures all operational, informational, and cooperative aspects described in the mission brief.
