## 1. Goal Model – Tables  

| **Name**                               | **Text**                                                                                                                           | **Runtime**                       | **Goal Type** | **Target Condition / Enquired Information**           | **Relation**           | **Ground truth I**                                    | **Ground truth C** | **Ground truth E** |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------- | ----------------------------------------------------- | ---------------------- | ----------------------------------------------------- | ------------------ | ------------------ |
| **G1**: Deliver Food to Inpatient Room | Achieve that a meal is delivered to the patient’s room (either on the table or on the tray) and all ancillary tasks are completed. | (G2 ; FALLBACK(G3, G4) ; G5 ; G6) | Achieve       | Food delivered to room table or retrieved by patient. | – (root)               | OK                                                    | Perform                   |                    |
| **G2**: Determine Retrieval Capability | Query whether the patient (or companion/nurse) can retrieve the meal from the robot’s tray.                                        | –                                 | Query         | Patient retrieval capability (boolean).               | AND                    | OK                                                    | OK                   |                    |
| **G3**: Deliver Meal to Table          | Perform the delivery of the meal onto the patient’s table.                                                                         | –                                 | Perform       | –                                                     | OR (alternative to G4) | OK                                                    | OK                   |                    |
| **G4**: Deliver Meal to Tray           | Place the meal on the robot’s tray for patient-initiated retrieval.                                                                | –                                 | Perform       | –                                                     | OR (alternative to G3) | OK                                                    | OK                   |                    |
| **G5**: Retrieve Dirty Dishes          | Pick up dirty dishes from the patient’s room.                                                                                      | –                                 | Perform       | –                                                     | AND                    | Achieve. Target condition: all dishes were retrieved. | OK                   |                    |
| **G6**: Open Room Door                 | Open the patient room door for robot entry.                                                                                        | –                                 | Perform       | –                                                     | AND                    | OK                                                    | OK                   |                    |


> **Note**  
> *The “OR” relation between **G3** and **G4** is expressed by the `FALLBACK(G3, G4)` in the runtime of **G1**.*

---

## 2. Task Model – Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1**: Fetch Meal from Kitchen | Retrieve the ordered meal from the kitchen storage. | AND | Kitchen | 1 |
| **AT2**: Query Retrieval Capability | Query the hospital database for the patient’s retrieval capability. | AND | Hospital Database | 1 |
| **AT3**: Deliver Meal to Table | Place the meal onto the patient’s table. | AND | Inpatient Room | 1 |
| **AT4**: Place Meal on Tray | Put the meal onto the robot’s tray. | AND | Inpatient Room | 1 |
| **AT5**: Indicate Meal for Retrieval | Notify the patient which meal to retrieve. | AND | Inpatient Room | 1 |
| **AT6**: Track Retrieval | Record the time and location of the patient’s meal retrieval. | AND | Inpatient Room | 1 |
| **AT7**: Alert Wrong Retrieval | Alert the system if a wrong meal is retrieved. | AND | Inpatient Room | 1 |
| **AT8**: Confirm Retrieval Success | Confirm that the patient has successfully retrieved the meal. | AND | Inpatient Room | 1 |
| **AT9**: Retrieve Dirty Dishes | Pick up dirty dishes from the patient’s room. | AND | Inpatient Room | 1 |
| **AT10**: Open Door Unassisted | Open the room door without assistance. | OR | Inpatient Room Door | 1 |
| **AT11**: Open Door with Human | Open the room door with human assistance. | OR | Inpatient Room Door | 1 |
| **AT12**: Open Door with Robot | Open the room door with another robot. | OR | Inpatient Room Door | 2 |
| **AT13**: Fetch Meal from Tray | Robot fetches the meal from the tray (cooperating with patient, companion, nurse, or another robot). | AND | Inpatient Room | 1 |

---

## 3. Summary Table (Goals + Tasks)  

| **Type** | **ID** | **Title** | **Description** | **Relation** | **Runtime / Goal Type** | **Target / Enquired** | **Location** | **# Robots** |
|----------|--------|-----------|-----------------|--------------|------------------------|-----------------------|--------------|--------------|
| Goal | G1 | Deliver Food to Inpatient Room | Achieve that a meal is delivered to the patient’s room (table or tray) and all ancillary tasks are completed. | – | (G2 ; FALLBACK(G3, G4) ; G5 ; G6) / Achieve | Food delivered to room table or retrieved by patient | – | – |
| Goal | G2 | Determine Retrieval Capability | Query whether the patient can retrieve the meal from the tray. | AND | – / Query | Patient retrieval capability | – | – |
| Goal | G3 | Deliver Meal to Table | Perform the delivery of the meal onto the patient’s table. | OR (with G4) | – / Perform | – | – | – |
| Goal | G4 | Deliver Meal to Tray | Place the meal on the robot’s tray for patient‑initiated retrieval. | OR (with G3) | – / Perform | – | – | – |
| Goal | G5 | Retrieve Dirty Dishes | Pick up dirty dishes from the patient’s room. | AND | – / Perform | – | – | – |
| Goal | G6 | Open Room Door | Open the patient room door for robot entry. | AND | – / Perform | – | – | – |
| Task | AT1 | Fetch Meal from Kitchen | Retrieve the ordered meal from the kitchen storage. | AND | – | – | Kitchen | 1 |
| Task | AT2 | Query Retrieval Capability | Query hospital database for patient retrieval capability. | AND | – | – | Hospital Database | 1 |
| Task | AT3 | Deliver Meal to Table | Place the meal onto patient’s table. | AND | – | – | Inpatient Room | 1 |
| Task | AT4 | Place Meal on Tray | Put the meal onto the robot’s tray. | AND | – | – | Inpatient Room | 1 |
| Task | AT5 | Indicate Meal for Retrieval | Notify patient which meal to retrieve. | AND | – | – | Inpatient Room | 1 |
| Task | AT6 | Track Retrieval | Record time and location of meal retrieval. | AND | – | – | Inpatient Room | 1 |
| Task | AT7 | Alert Wrong Retrieval | Alert if wrong meal is retrieved. | AND | – | – | Inpatient Room | 1 |
| Task | AT8 | Confirm Retrieval Success | Confirm that patient has successfully retrieved the meal. | AND | – | – | Inpatient Room | 1 |
| Task | AT9 | Retrieve Dirty Dishes | Pick up dirty dishes from patient’s room. | AND | – | – | Inpatient Room | 1 |
| Task | AT10 | Open Door Unassisted | Open the room door without assistance. | OR | – | – | Inpatient Room Door | 1 |
| Task | AT11 | Open Door with Human | Open the room door with human assistance. | OR | – | – | Inpatient Room Door | 1 |
| Task | AT12 | Open Door with Robot | Open the room door with another robot. | OR | – | – | Inpatient Room Door | 2 |
| Task | AT13 | Fetch Meal from Tray | Robot fetches the meal from the tray (cooperating with patient, companion, nurse, or another robot). | AND | – | – | Inpatient Room | 1 |

---

## 4. Logical Relationships (Tree‑Style)  

```
G1 -> G2, G3, G4, G5, G6 [AND][(sequential)]

G1 -> G3, G4 [OR][FALLBACK(G3, G4)]

G2 -> AT2 [AND]

G3 -> AT1, AT3 [AND][(sequential)]

G4 -> AT4, AT5, AT6, AT7, AT8, AT13 [AND][(sequential)]

G5 -> AT9 [AND]

G6 -> AT10, AT11, AT12 [OR][(parallel)]
```

*Each arrow indicates the parent‑child relationship; the brackets show the decomposition type (AND/OR) and the execution semantics (sequential, parallel, or fallback).*

---
