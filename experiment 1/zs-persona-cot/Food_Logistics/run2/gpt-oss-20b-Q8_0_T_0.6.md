**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

---

## 1. Goal Decomposition Tables  

| **Name**     | **Title**                      | **Text**                                                                        | **Runtime**                                | **Goal Type** | **Target / Enquired Info**                                  | **Relation** | **Justification**                                                                  | Ground truth I | Ground truth C | Consensus |
| ------------ | ------------------------------ | ------------------------------------------------------------------------------- | ------------------------------------------ | ------------- | ----------------------------------------------------------- | ------------ | ---------------------------------------------------------------------------------- | -------------- | -------------- | --------- |
| **G1**       | Deliver food & retrieve dishes | Bring all ordered meals to the inpatient room and remove all dirty dishes.      | `;`                                        | Achieve       | `All meals delivered to room AND all dirty dishes removed.` | N/A (root)   | Must finish both delivery and dish retrieval for mission success.                  | Perform.       | Perform        | Perform.  |
| **G1.1**     | Deliver food                   | Bring the requested meals to the patient, either onto the table or onto a tray. | `FALLBACK(G1.1.1,G1.1.2)`                  | Achieve       | `Food delivered to patient (table or tray).`                | OR           | Two delivery modes; one success suffices.                                          | OK.            | Perform        | OK.       |
| **G1.1.1**   | Deliver to table               | Robot places the meal directly onto the patient’s table.                        | `-`                                        | Perform       | –                                                           | –            | Simple action, no further decomposition.                                           | OK.            | OK             | OK.       |
| **G1.1.2**   | Deliver to tray                | Robot places the meal on a tray for the patient to fetch.                       | `;`                                        | Perform       | –                                                           | AND          | Must query patient ability, companion presence, then perform the actions in order. | OK.            | OK             | OK.       |
| **G1.1.2.1** | Query patient ability          | Ask whether the patient can retrieve the meal from the tray.                    | `-`                                        | Query         | `Can patient retrieve from tray?`                           | –            | Uncertain patient capability must be known before proceeding.                      | OK             | OK             | OK        |
| **G1.1.2.2** | Query companion presence       | Ask whether a companion is present in the room.                                 | `-`                                        | Query         | `Is a companion present?`                                   | –            | Companion may assist if patient cannot fetch.                                      | OK             | OK             | OK        |
| **G1.1.2.3** | Place food on tray             | Robot puts the meal on the patient’s tray.                                      | `-`                                        | Perform       | –                                                           | –            | Required step after confirming fetch possibility.                                  | OK             | OK             | OK        |
| **G1.1.2.4** | Signal meal                    | Robot informs the patient which meal is on the tray.                            | `-`                                        | Perform       | –                                                           | –            | Enables correct retrieval.                                                         | OK             | OK             | OK        |
| **G1.1.2.5** | Track retrieval                | Record when and where the patient takes the meal.                               | `-`                                        | Perform       | –                                                           | –            | Needed for later auditing and error detection.                                     | OK             | OK             | OK        |
| **G1.1.2.6** | Alert wrong meal               | Notify if a meal that is not the patient’s was retrieved.                       | `-`                                        | Perform       | –                                                           | –            | Prevents mis-delivery.                                                             | OK             | OK             | OK        |
| **G1.2**     | Retrieve dishes                | Remove all dirty dishes from the patient room.                                  | `FALLBACK(FALLBACK(G1.2.1,G1.2.2),G1.2.3)` | Achieve       | `All dirty dishes removed.`                                 | OR           | Three cooperation options; any one suffices.                                       | OK             | OK             | OK        |
| **G1.2.1**   | Unassisted retrieval           | Robot fetches the dishes alone.                                                 | `-`                                        | Perform       | –                                                           | –            | Robot can handle light loads.                                                      | OK             | Perform        | OK        |
| **G1.2.2**   | Retrieval with two robots      | Two robots cooperate to fetch the dishes.                                       | `-`                                        | Perform       | –                                                           | –            | Needed for heavier or bulky dishes.                                                | OK             | OK             | OK        |
| **G1.2.3**   | Retrieval with human           | Robot works with a human to fetch the dishes.                                   | `-`                                        | Perform       | –                                                           | –            | Human assistance may be required.                                                  | OK             | OK             | OK        |

---

## 2. Task Decomposition Tables  

| **Name** | **Title** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|-----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Pick up food (table) | Robot picks up the meal in the kitchen. | AND | kitchen | 1 | Robot must collect the food before transport. |
| **AT2** | Transport to room (table) | Robot carries the meal through the hallway to the patient room. | AND | hallway | 1 | Physical movement required. |
| **AT3** | Open door (table) | Robot opens the patient room door. | AND | room door | 1 | Door must be opened for access. |
| **AT4** | Deliver to table | Robot places the meal on the patient’s table. | AND | patient room table | 1 | Final delivery step. |
| **AT5** | Pick up food (tray) | Robot picks up the meal in the kitchen. | AND | kitchen | 1 | Same initial step as table delivery. |
| **AT6** | Transport to room (tray) | Robot carries the meal to the patient room. | AND | hallway | 1 | Same transport step. |
| **AT7** | Open door (tray) | Robot opens the patient room door. | AND | room door | 1 | Needed before tray placement. |
| **AT8** | Place on tray | Robot places the meal onto the patient’s tray. | AND | patient room tray | 1 | Enables patient to fetch. |
| **AT9** | Signal meal | Robot signals the patient which meal is on the tray. | AND | patient room | 1 | Ensures correct retrieval. |
| **AT10** | Track retrieval | Robot logs the time and location of meal pickup. | AND | patient room | 1 | For audit and error handling. |
| **AT11** | Alert wrong meal | Robot alerts staff if the wrong meal is taken. | AND | patient room | 1 | Prevents mis‑delivery. |
| **AT12** | Retrieve dish (unassisted) | Robot picks up dirty dishes alone. | AND | patient room | 1 | Robot can handle light dishes. |
| **AT13** | Retrieve dish (two robots) | Two robots cooperate to fetch dishes. | AND | patient room | 2 | Needed for heavier loads. |
| **AT14** | Retrieve dish (human) | Robot works with a human to fetch dishes. | AND | patient room | 1 | Human assistance may be required. |
| **AT15** | Open door for dish retrieval | Robot opens the room door for dish fetching. | AND | room door | 1 | Required for access. |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Type** | **Title** | **Runtime / Relation** | **Justification** |
|--------|----------|-----------|------------------------|-------------------|
| G1 | Goal | Deliver food & retrieve dishes | `;` (sequential) | Must finish delivery before dish retrieval. |
| G1.1 | Goal | Deliver food | `FALLBACK(G1.1.1,G1.1.2)` | Table vs tray. |
| G1.1.1 | Goal | Deliver to table | `-` | Simple action. |
| G1.1.2 | Goal | Deliver to tray | `;` | Query + actions. |
| G1.1.2.1 | Goal | Query patient ability | `-` | Needed before tray. |
| G1.1.2.2 | Goal | Query companion presence | `-` | Needed before tray. |
| G1.1.2.3 | Goal | Place food on tray | `-` | Action. |
| G1.1.2.4 | Goal | Signal meal | `-` | Action. |
| G1.1.2.5 | Goal | Track retrieval | `-` | Action. |
| G1.1.2.6 | Goal | Alert wrong meal | `-` | Action. |
| G1.2 | Goal | Retrieve dishes | `FALLBACK(FALLBACK(G1.2.1,G1.2.2),G1.2.3)` | Multiple options. |
| G1.2.1 | Goal | Unassisted retrieval | `-` | Action. |
| G1.2.2 | Goal | Retrieval with two robots | `-` | Action. |
| G1.2.3 | Goal | Retrieval with human | `-` | Action. |
| AT1 | Task | Pick up food (table) | AND | Kitchen. |
| AT2 | Task | Transport to room (table) | AND | Hallway. |
| AT3 | Task | Open door (table) | AND | Door. |
| AT4 | Task | Deliver to table | AND | Table. |
| AT5 | Task | Pick up food (tray) | AND | Kitchen. |
| AT6 | Task | Transport to room (tray) | AND | Hallway. |
| AT7 | Task | Open door (tray) | AND | Door. |
| AT8 | Task | Place on tray | AND | Tray. |
| AT9 | Task | Signal meal | AND | Room. |
| AT10 | Task | Track retrieval | AND | Room. |
| AT11 | Task | Alert wrong meal | AND | Room. |
| AT12 | Task | Retrieve dish (unassisted) | AND | Room. |
| AT13 | Task | Retrieve dish (two robots) | AND | Room. |
| AT14 | Task | Retrieve dish (human) | AND | Room. |
| AT15 | Task | Open door for dish retrieval | AND | Door. |

---

## 4. Logical Relationships (Arrows)

```
G1  ->  G1.1, G1.2  [AND][;]
     Justification: Both food delivery and dish retrieval must succeed in sequence.

G1.1  ->  G1.1.1, G1.1.2  [OR][FALLBACK(G1.1.1,G1.1.2)]
     Justification: Attempt table delivery first; fallback to tray if table delivery fails.

G1.1.2  ->  G1.1.2.1, G1.1.2.2, G1.1.2.3, G1.1.2.4, G1.1.2.5, G1.1.2.6  [AND][;]
     Justification: Must query patient ability and companion presence before performing the tray actions in order.

G1.2  ->  G1.2.1, G1.2.2, G1.2.3  [OR][FALLBACK(FALLBACK(G1.2.1,G1.2.2),G1.2.3)]
     Justification: Try unassisted first; if not possible, try two robots; else human assistance.

G1.1.1  ->  AT1, AT2, AT3, AT4  [AND][#]
     Justification: All four actions must be executed in parallel (pick, transport, open, deliver).

G1.1.2  ->  AT5, AT6, AT7, AT8, AT9, AT10, AT11  [AND][#]
     Justification: All actions must be performed together (pick, transport, open, place, signal, track, alert).

G1.2.1  ->  AT12, AT15  [AND][#]
     Justification: Retrieve dish and open door.

G1.2.2  ->  AT13, AT15  [AND][#]
     Justification: Two robots retrieve dish and open door.

G1.2.3  ->  AT14, AT15  [AND][#]
     Justification: Robot retrieves dish with human and opens door.
```

---

### Remarks on the Design Choices

1. **Sequential vs Parallel** – The top‑level goal (`G1`) is sequential because the system must finish delivering food before it can start dish retrieval. Inside each delivery mode, the robot’s physical actions (pick‑up, transport, door‑open, placement) can be executed in parallel (denoted by `#`) because they are independent sub‑tasks that can run simultaneously on the same robot (e.g., the robot can open the door while carrying the meal).  

2. **Fallbacks** – The use of `FALLBACK` reflects the uncertainty in the environment: the robot should try the simplest option (table delivery) first, and if it is not feasible (e.g., patient cannot fetch, no companion), it falls back to the next option (tray). Similarly for dish retrieval, the robot prefers to act alone, then tries two‑robot cooperation, and finally human help.  

3. **Queries** – The `Query` goals capture the need to obtain uncertain information (patient capability, companion presence). These are pure information‑gathering steps that do not involve physical actions.  

4. **Goal Types** –  
   * `Perform` goals describe concrete actions the robot must execute.  
   * `Query` goals are purely informational.  
   * `Achieve` goals describe a desired world state (food delivered, dishes removed).  

5. **Task Locations & Robot Count** – All tasks are tied to realistic locations (kitchen, hallway, door, patient room) and specify the number of robots needed. For dish retrieval, the two‑robot option explicitly requires two robots.  

This goal model provides a clear, hierarchical decomposition that can be directly mapped to a multi‑robot planning and execution framework.
