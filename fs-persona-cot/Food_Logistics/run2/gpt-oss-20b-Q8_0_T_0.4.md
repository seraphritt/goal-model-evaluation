## 1. Goal Model – Tables  

| **Name**                                    | **Text**                                                                                 | **Runtime**                                            | **Goal Type** | **Target / Enquired**                         | **Relation** | **Justification**                                                                                                                                                                         | **Ground truth I**                                    | **Ground truth C** | **Ground truth E** |
| ------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------- | --------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------ | ------------------ |
| **G1 – Deliver Food & Clean Dishes**        | Bring the kitchen’s meals to the inpatient room and ensure all dirty dishes are removed. | `; (G2 # (G3 # G4))`                                   | Achieve       | food delivered to room **and** dishes cleaned | AND          | All three sub-goals must be satisfied. The door must be opened first; after that, food delivery and dish retrieval can proceed in parallel.                                               | Perform                                               |  Perform                  |                    |
| **G2 – Open Door**                          | Make the room door passable for the robot.                                               | `FALLBACK(G2.1, G2.2)`                                 | Perform       | –                                             | OR           | Either the robot opens the door itself or a human does; the robot first attempts, and if it fails a human can help.                                                                       | OK                                                    |  Ok                  |                    |
| **G2.1 – Robot Opens Door**                 | Robot physically opens the room door.                                                    | `-`                                                    | Perform       | –                                             | –            | Robot action.                                                                                                                                                                             | OK                                                    |  Ok                  |                    |
| **G2.2 – Human Opens Door**                 | Human (nurse, companion, etc.) opens the room door.                                      | `-`                                                    | Perform       | –                                             | –            | Human action.                                                                                                                                                                             | OK                                                    |  Ok                  |                    |
| **G3 – Deliver Food**                       | Execute all actions required to get a meal from the kitchen to the patient.              | `; (G3.0 # G3.1 # FALLBACK(G3.2, G3.3) # G3.4 # G3.5)` | Perform       | –                                             | AND          | The robot must acquire the meal, check if the patient can fetch it, then either deliver it to the table or coordinate a fetch, track the retrieval, and alert if the wrong meal is taken. | Achieve. Target condition: all food was delivered     |  Ok                  |                    |
| **G3.0 – Acquire Meal**                     | Pick up the meal from the kitchen.                                                       | `-`                                                    | Perform       | –                                             | –            | Robot action.                                                                                                                                                                             | OK                                                    |  Ok                  |                    |
| **G3.1 – Determine Retrieval Capability**   | Query the patient record and room occupancy to decide if the patient can fetch the meal. | `-`                                                    | Query         | “Can patient fetch?”                          | –            | Information-seeking step.                                                                                                                                                                 | OK                                                    |  Ok                  |                    |
| **G3.2 – Deliver to Table**                 | Place the meal on the patient’s table.                                                   | `-`                                                    | Perform       | –                                             | –            | Requires special manipulation skill.                                                                                                                                                      | OK                                                    |  Ok                  |                    |
| **G3.3 – Coordinate Fetch**                 | Tell the patient (or companion) which meal to retrieve from the robot’s tray.            | `-`                                                    | Perform       | –                                             | –            | Human-robot interaction.                                                                                                                                                                  | OK                                                    |  Ok                  |                    |
| **G3.4 – Track Meal Retrieval**             | Record when and where each meal was retrieved.                                           | `-`                                                    | Perform       | –                                             | –            | Logging.                                                                                                                                                                                  | OK                                                    |  Ok                  |                    |
| **G3.5 – Alert Wrong Meal**                 | Notify staff if the patient picks up the wrong meal.                                     | `-`                                                    | Perform       | –                                             | –            | Safety check.                                                                                                                                                                             | OK                                                    |  Ok                  |                    |
| **G4 – Retrieve Dishes**                    | Remove dirty dishes from the room.                                                       | `FALLBACK(G4.1, G4.2)`                                 | Perform       | –                                             | OR           | The robot can do it alone or with help.                                                                                                                                                   | Achieve. Target condition: all dishes were retrieved. |  Ok                  |                    |
| **G4.1 – Retrieve Dishes Unassisted**       | Robot picks up dishes by itself.                                                         | `-`                                                    | Perform       | –                                             | –            | Robot action.                                                                                                                                                                             | OK                                                    |  Ok                  |                    |
| **G4.2 – Retrieve Dishes with Cooperation** | Robot works with another robot or a human to clear dishes.                               | `-`                                                    | Perform       | –                                             | –            | Cooperative action.                                                                                                                                                                       | OK                                                    |  Ok                  |                    |

---

## 2. Task Model – Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|---|---|---|---|---|---|
| **AT1 – Pick up Meal** | Robot picks up the meal from the kitchen. | AND (with G3.0) | kitchen | 1 | Robot must navigate to the kitchen and lift the meal. |
| **AT2 – Deliver Meal to Table** | Robot places the meal on the patient’s table. | AND (with G3.2) | inpatient room table | 1 | Requires the robot’s manipulation skill. |
| **AT3 – Indicate Meal to Inpatient** | Robot informs the patient which meal to retrieve from its tray. | AND (with G3.3) | inpatient room | 1 | Robot must communicate the correct meal ID. |
| **AT4 – Robot Opens Door** | Robot opens the room door. | AND (with G2.1) | room door | 1 | Robot’s door‑opening mechanism. |
| **AT6a – Retrieve Dishes Unassisted** | Robot picks up dirty dishes alone. | AND (with G4.1) | room | 1 | Robot can lift dishes by itself. |
| **AT6b – Retrieve Dishes with Cooperation** | Robot coordinates with another robot or a human to clear dishes. | AND (with G4.2) | room | [1,2] | If a single robot cannot lift all dishes, a second robot or a human can help. |
| **AT7 – Track Meal Retrieval** | Robot logs the time and location of each meal retrieval. | AND (with G3.4) | robot internal | 1 | Internal state update. |
| **AT8 – Alert Wrong Meal** | Robot raises an alarm if the wrong meal is taken. | AND (with G3.5) | robot internal | 1 | Safety alert. |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Title** | **Type** | **Runtime / Relation** |
|---|---|---|---|
| **G1** | Deliver Food & Clean Dishes | Achieve | `; (G2 # (G3 # G4))` |
| **G2** | Open Door | Perform | `FALLBACK(G2.1, G2.2)` |
| **G2.1** | Robot Opens Door | Perform | `-` |
| **G2.2** | Human Opens Door | Perform | `-` |
| **G3** | Deliver Food | Perform | `; (G3.0 # G3.1 # FALLBACK(G3.2, G3.3) # G3.4 # G3.5)` |
| **G3.0** | Acquire Meal | Perform | `-` |
| **G3.1** | Determine Retrieval Capability | Query | `-` |
| **G3.2** | Deliver to Table | Perform | `-` |
| **G3.3** | Coordinate Fetch | Perform | `-` |
| **G3.4** | Track Meal Retrieval | Perform | `-` |
| **G3.5** | Alert Wrong Meal | Perform | `-` |
| **G4** | Retrieve Dishes | Perform | `FALLBACK(G4.1, G4.2)` |
| **G4.1** | Retrieve Dishes Unassisted | Perform | `-` |
| **G4.2** | Retrieve Dishes with Cooperation | Perform | `-` |
| **AT1** | Pick up Meal | – | – |
| **AT2** | Deliver Meal to Table | – | – |
| **AT3** | Indicate Meal to Inpatient | – | – |
| **AT4** | Robot Opens Door | – | – |
| **AT6a** | Retrieve Dishes Unassisted | – | – |
| **AT6b** | Retrieve Dishes with Cooperation | – | – |
| **AT7** | Track Meal Retrieval | – | – |
| **AT8** | Alert Wrong Meal | – | – |

---

## 4. Logical Relationships (Tree‑Structure)

```
G1 -> G2, G3, G4 [AND][; (G2 # (G3 # G4))]
  - Justification: Door must be opened first; after that, food delivery and dish retrieval can happen in parallel.

G2 -> G2.1, G2.2 [OR][FALLBACK(G2.1, G2.2)]
  - Justification: Robot attempts to open the door; if it fails, a human can help.

G3 -> G3.0, G3.1, G3.2, G3.3, G3.4, G3.5 [AND][; (G3.0 # G3.1 # FALLBACK(G3.2, G3.3) # G3.4 # G3.5)]
  - Justification: All sub‑goals must be satisfied; the robot first acquires the meal, checks if the patient can fetch it, then either delivers to the table or coordinates a fetch, tracks the retrieval, and alerts if the wrong meal is taken.

G3.0 -> AT1 [AND][-]
  - Justification: Picking up the meal is the only action needed to acquire it.

G3.1 -> (no task – query)

G3.2 -> AT2 [AND][-]
  - Justification: Delivering to the table is a single action.

G3.3 -> AT3 [AND][-]
  - Justification: The robot must inform the patient which meal to retrieve.

G3.4 -> AT7 [AND][-]
  - Justification: Tracking is a single logging action.

G3.5 -> AT8 [AND][-]
  - Justification: Alerting is a single action.

G4 -> G4.1, G4.2 [OR][FALLBACK(G4.1, G4.2)]
  - Justification: The robot can clear dishes alone or with help.

G4.1 -> AT6a [AND][-]
  - Justification: Unassisted dish retrieval is a single action.

G4.2 -> AT6b [AND][-]
  - Justification: Cooperative dish retrieval may involve another robot or a human.

G2.1 -> AT4 [AND][-]
  - Justification: Robot opening the door is a single action.
```

---

### 5. Remarks & Justifications

* **Goal Types**  
  * *Achieve* (G1) – the mission’s ultimate state (food delivered & dishes cleaned).  
  * *Perform* – all other goals require concrete robot actions.  
  * *Query* (G3.1) – the robot must obtain information from the patient record.  

* **Runtime Annotations**  
  * `;` (sequential) is used when a sub‑goal must finish before the next one starts (e.g., door opening before delivery).  
  * `#` (parallel) is used when two sub‑goals can proceed concurrently (e.g., delivery and dish retrieval after the door is open).  
  * `FALLBACK(exp1,exp2)` is used for alternatives where one succeeds if the other fails (e.g., robot vs. human door opening, deliver to table vs. fetch).  

* **Relations**  
  * `AND` is chosen when *all* children must be satisfied for the parent to succeed.  
  * `OR` is chosen when *any* child suffices for the parent to succeed.  

* **Task Properties**  
  * *Location* is set to the physical place where the action occurs (kitchen, room table, door, etc.).  
  * *Number of Robots* reflects the minimum or required number of robots for the task; ranges are used when cooperation may be needed.  

This goal‑task model captures the entire mission flow, clarifies the dependencies, and provides a clear blueprint for multi‑robot coordination in a hospital setting.
