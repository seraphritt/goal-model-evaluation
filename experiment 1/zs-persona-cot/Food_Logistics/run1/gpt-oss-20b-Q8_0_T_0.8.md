**Mission‑Level Goal Model – “Food Delivery in a Hospital”**  
*(Multi‑Robot System – depth‑first numbering, explicit runtime operators, goal‑type classification, and task decomposition)*  

---

## 1. Goal‑Level Tables

| **Name**                                    | **Text**                                                                                                                                                    | **Runtime**                          | **Goal Type** | **Target Condition / Enquired Info**                      | **Relation**                    | **Justification**                                                                                                                           | **Ground truth I**                                    | **Ground truth C** | **Consensus**                                         |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------- | --------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------ | ----------------------------------------------------- |
| **G1 – Deliver Food to Inpatient Room**     | Achieve that a meal is delivered to the inpatient’s room and the inpatient (or companion) has successfully retrieved it or it has been placed on the table. | `;` (sequential)                     | **Achieve**   | *Food delivered to room & meal retrieved/placed on table* | – (root)                        | The overall mission must finish only after the food is delivered, the meal is retrieved (or placed), and any required cleanup is performed. | Achieve. Target condition: all food was delivered.    | Ok                 | Achieve. Target condition: all food was delivered.    |
| **G2 – Query Patient Retrieval Capability** | Enquire whether the patient can retrieve the meal from the robot’s tray.                                                                                    | `-` (leaf)                           | **Query**     | *Patient can retrieve from tray? (true/false)*            | **AND** (with G7)               | The decision of the delivery mode depends on this information.                                                                              | OK                                                    | Ok                 | OK                                                    |
| **G3 – Deliver Food to Table**              | Perform the manipulation skill to place the meal directly on the inpatient’s table.                                                                         | `-`                                  | **Perform**   | –                                                         | **OR** (inside G7)              | One of the two delivery modes must be executed.                                                                                             | OK                                                    | Ok                 | OK                                                    |
| **G4 – Deliver Food to Tray**               | Place the meal on the robot’s tray in the inpatient’s room for the patient (or companion) to fetch.                                                         | `-`                                  | **Perform**   | –                                                         | **OR** (inside G7)              | Alternative to G3 when the patient can retrieve from the tray.                                                                              | OK                                                    | Ok                 | OK                                                    |
| **G5 – Retrieve Dirty Dishes**              | Retrieve dirty dishes from the room, using the most feasible cooperation strategy.                                                                          | `FALLBACK(FALLBACK(G5.1,G5.2),G5.3)` | **Perform**   | –                                                         | **OR** (inside G5)              | Dish retrieval can be unassisted, robot-robot, or robot-human; the fallback captures the priority order.                                    | Achieve. target condition: all dishes were retrieved. | Ok                 | Achieve. target condition: all dishes were retrieved. |
| **G5.1 – Unassisted Dish Retrieval**        | Robot alone picks up all dishes.                                                                                                                            | `-`                                  | **Perform**   | –                                                         | **AND** (with AT10, AT11)       | Minimal cooperation, highest priority when possible.                                                                                        | OK                                                    | Ok                 | OK                                                    |
| **G5.2 – Robot-Robot Dish Retrieval**       | Two robots cooperate to pick up dishes.                                                                                                                     | `-`                                  | **Perform**   | –                                                         | **AND** (with AT12, AT13)       | Used when one robot is insufficient or when a second robot is available.                                                                    | OK                                                    | Ok                 | OK                                                    |
| **G5.3 – Human-Assisted Dish Retrieval**    | Human assists robot in picking up dishes.                                                                                                                   | `-`                                  | **Perform**   | –                                                         | **AND** (with AT14, AT15, AT16) | Fallback when no robot-robot pair is available.                                                                                             | OK                                                    | Ok                 | OK                                                    |
| **G6 – Open Room Door**                     | Open the room door, possibly requiring cooperation.                                                                                                         | `FALLBACK(FALLBACK(G6.1,G6.2),G6.3)` | **Perform**   | –                                                         | **OR** (inside G6)              | The door may be opened by robot-human, robot-robot, or human alone.                                                                         | OK                                                    | Ok                 | OK                                                    |
| **G6.1 – Robot-Human Door Opening**         | Robot signals; human opens the door.                                                                                                                        | `-`                                  | **Perform**   | –                                                         | **AND** (with AT17, AT18)       | Preferred when a human is present and can cooperate.                                                                                        | OK                                                    | Ok                 | OK                                                    |
| **G6.2 – Robot-Robot Door Opening**         | Two robots cooperate to open the door.                                                                                                                      | `-`                                  | **Perform**   | –                                                         | **AND** (with AT19, AT20)       | Used when no human is available.                                                                                                            | OK                                                    | Ok                 | OK                                                    |
| **G6.3 – Human-Only Door Opening**          | Human opens the door alone.                                                                                                                                 | `-`                                  | **Perform**   | –                                                         | **AND** (with AT21)             | Fallback if robots cannot cooperate.                                                                                                        | OK                                                    | Ok                 | OK                                                    |
| **G7 – Choose Delivery Mode**               | Decide whether to deliver to table (G3) or to tray (G4) based on G2.                                                                                        | `FALLBACK(G4,G3)`                    | **Perform**   | –                                                         | **AND** (with G2)               | The fallback captures the conditional choice: if G2 succeeds → G4, otherwise → G3.                                                          | OK                                                    | Ok                 | OK                                                    |
| **G8 – Monitor Meal Retrieval**             | Observe the patient (or companion) retrieving the meal and verify correctness.                                                                              | `-`                                  | **Perform**   | –                                                         | **AND** (with AT7, AT8, AT9)    | Needed to detect wrong meal and maintain accountability.                                                                                    | OK                                                    | Ok                 | OK                                                    |
| **G9 – Alert Wrong Meal Retrieval**         | Notify staff if a meal different from the one assigned is retrieved.                                                                                        | `-`                                  | **Perform**   | –                                                         | **AND** (with AT9)              | Sub-goal of G8, but expressed separately for clarity.                                                                                       | OK                                                    | Ok                 | OK                                                    |

---

## 2. Task‑Level Tables

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1 – Move to Kitchen & Pick Meal** | Robot travels to the kitchen, grabs the meal from the counter. | **AND** (under G4) | Kitchen | 1 | Only the robot is required to pick up the meal. |
| **AT2 – Deliver to Tray** | Robot transports meal to the inpatient’s room and places it on its tray. | **AND** (under G4) | Inpatient Room | 1 | Robot alone can deliver to the tray. |
| **AT3 – Indicate Meal to Patient** | Robot displays the meal ID (e.g., via screen or voice) so the patient knows which meal to pick. | **AND** (under G4) | Inpatient Room | 1 | Communication is part of the delivery routine. |
| **AT4 – Move to Kitchen & Pick Meal (Table)** | Robot travels to the kitchen and grabs the meal. | **AND** (under G3) | Kitchen | 1 | Same as AT1 but for table delivery. |
| **AT5 – Deliver to Table** | Robot places the meal on the patient’s table. | **AND** (under G3) | Inpatient Room | 1 | Requires manipulation skill. |
| **AT6 – Wait for Patient Retrieval** | Robot waits until the patient (or companion) picks the meal from the tray. | **AND** (under G8) | Inpatient Room | 1 | Monitoring phase. |
| **AT7 – Verify Meal Identity** | Robot scans or reads the meal ID and compares it to the assigned ID. | **AND** (under G8) | Inpatient Room | 1 | Ensures correct meal is retrieved. |
| **AT8 – Alert Wrong Meal** | If mismatch detected, robot raises an alarm to staff. | **AND** (under G9) | Inpatient Room | 1 | Safety & accountability. |
| **AT9 – Log Retrieval Time & Location** | Robot records timestamp and room number when meal is retrieved. | **AND** (under G8) | Inpatient Room | 1 | Tracking requirement. |
| **AT10 – Move to Room & Pick Dishes (Unassisted)** | Robot goes to the room and collects all dishes. | **AND** (under G5.1) | Inpatient Room | 1 | Single robot can handle simple cleanup. |
| **AT11 – Secure Dishes in Trash Bin** | Robot places dishes in the designated trash bin. | **AND** (under G5.1) | Trash Bin | 1 | Completion of cleanup. |
| **AT12 – Robot A Signals Robot B** | First robot initiates coordination handshake. | **AND** (under G5.2) | Inpatient Room | 2 | Two robots need to coordinate. |
| **AT13 – Joint Dish Pickup** | Both robots collaborate to lift and transport dishes. | **AND** (under G5.2) | Inpatient Room | 2 | Handles heavier loads. |
| **AT14 – Request Human Assistance** | Robot asks a human (patient, companion, or nurse) to help. | **AND** (under G5.3) | Inpatient Room | 1 | Human cooperation required. |
| **AT15 – Human Picks Dishes** | Human collects dishes while robot assists. | **AND** (under G5.3) | Inpatient Room | 1 | Human performs main action. |
| **AT16 – Robot Secures Dishes** | Robot holds dishes while human moves them to trash. | **AND** (under G5.3) | Inpatient Room | 1 | Robot’s support role. |
| **AT17 – Robot Signals Door Opening** | Robot indicates to human that the door can be opened. | **AND** (under G6.1) | Inpatient Room | 1 | Communication step. |
| **AT18 – Human Opens Door** | Human opens the room door. | **AND** (under G6.1) | Inpatient Room | 1 | Human action. |
| **AT19 – Robot A Signals Robot B** | First robot initiates door‑opening coordination. | **AND** (under G6.2) | Inpatient Room | 2 | Two robots coordinate. |
| **AT20 – Robot B Opens Door** | Second robot opens the door (e.g., with a door‑handle attachment). | **AND** (under G6.2) | Inpatient Room | 1 | Robot performs mechanical action. |
| **AT21 – Human Opens Door Alone** | Human opens the door without robot assistance. | **AND** (under G6.3) | Inpatient Room | 1 | Fallback. |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Type** | **Title** | **Relation** | **Runtime / Decomposition** |
|--------|----------|-----------|--------------|-----------------------------|
| G1 | Goal (Achieve) | Deliver Food to Inpatient Room | Root | `;` (sequential) |
| G2 | Goal (Query) | Query Patient Retrieval Capability | AND (with G7) | `-` |
| G7 | Goal (Perform) | Choose Delivery Mode | AND (with G2) | `FALLBACK(G4,G3)` |
| G3 | Goal (Perform) | Deliver Food to Table | OR (inside G7) | `-` |
| G4 | Goal (Perform) | Deliver Food to Tray | OR (inside G7) | `-` |
| G8 | Goal (Perform) | Monitor Meal Retrieval | AND (with AT6, AT7, AT9) | `-` |
| G9 | Goal (Perform) | Alert Wrong Meal Retrieval | AND (with AT9) | `-` |
| G5 | Goal (Perform) | Retrieve Dirty Dishes | OR (inside G5) | `FALLBACK(FALLBACK(G5.1,G5.2),G5.3)` |
| G5.1 | Goal (Perform) | Unassisted Dish Retrieval | AND (with AT10, AT11) | `-` |
| G5.2 | Goal (Perform) | Robot‑Robot Dish Retrieval | AND (with AT12, AT13) | `-` |
| G5.3 | Goal (Perform) | Human‑Assisted Dish Retrieval | AND (with AT14, AT15, AT16) | `-` |
| G6 | Goal (Perform) | Open Room Door | OR (inside G6) | `FALLBACK(FALLBACK(G6.1,G6.2),G6.3)` |
| G6.1 | Goal (Perform) | Robot‑Human Door Opening | AND (with AT17, AT18) | `-` |
| G6.2 | Goal (Perform) | Robot‑Robot Door Opening | AND (with AT19, AT20) | `-` |
| G6.3 | Goal (Perform) | Human‑Only Door Opening | AND (with AT21) | `-` |
| AT1 | Task | Move to Kitchen & Pick Meal (Tray) | AND (under G4) | Kitchen, 1 robot |
| AT2 | Task | Deliver to Tray | AND (under G4) | Inpatient Room, 1 robot |
| AT3 | Task | Indicate Meal to Patient | AND (under G4) | Inpatient Room, 1 robot |
| AT4 | Task | Move to Kitchen & Pick Meal (Table) | AND (under G3) | Kitchen, 1 robot |
| AT5 | Task | Deliver to Table | AND (under G3) | Inpatient Room, 1 robot |
| AT6 | Task | Wait for Patient Retrieval | AND (under G8) | Inpatient Room, 1 robot |
| AT7 | Task | Verify Meal Identity | AND (under G8) | Inpatient Room, 1 robot |
| AT8 | Task | Alert Wrong Meal | AND (under G9) | Inpatient Room, 1 robot |
| AT9 | Task | Log Retrieval Time & Location | AND (under G8) | Inpatient Room, 1 robot |
| AT10 | Task | Move to Room & Pick Dishes (Unassisted) | AND (under G5.1) | Inpatient Room, 1 robot |
| AT11 | Task | Secure Dishes in Trash Bin | AND (under G5.1) | Trash Bin, 1 robot |
| AT12 | Task | Robot A Signals Robot B | AND (under G5.2) | Inpatient Room, 2 robots |
| AT13 | Task | Joint Dish Pickup | AND (under G5.2) | Inpatient Room, 2 robots |
| AT14 | Task | Request Human Assistance | AND (under G5.3) | Inpatient Room, 1 robot |
| AT15 | Task | Human Picks Dishes | AND (under G5.3) | Inpatient Room, 1 human |
| AT16 | Task | Robot Secures Dishes | AND (under G5.3) | Inpatient Room, 1 robot |
| AT17 | Task | Robot Signals Door Opening | AND (under G6.1) | Inpatient Room, 1 robot |
| AT18 | Task | Human Opens Door | AND (under G6.1) | Inpatient Room, 1 human |
| AT19 | Task | Robot A Signals Robot B | AND (under G6.2) | Inpatient Room, 2 robots |
| AT20 | Task | Robot B Opens Door | AND (under G6.2) | Inpatient Room, 1 robot |
| AT21 | Task | Human Opens Door Alone | AND (under G6.3) | Inpatient Room, 1 human |

---

## 4. Logical Relationships (with Justifications)

| **Parent → Children** | **Relation / Runtime** | **Justification** |
|------------------------|------------------------|-------------------|
| **G1 → G2** | **AND** | G1 requires the result of the query before deciding the delivery mode. |
| **G1 → G7** | **AND** | G7 implements the conditional choice; it cannot finish until G2 has provided the information. |
| **G1 → G8** | **AND** | Monitoring retrieval must happen after the meal is delivered. |
| **G1 → G5** | **AND** | Dish retrieval is part of the overall delivery cycle (cleanup). |
| **G1 → G6** | **AND** | Opening the door is necessary for both delivery and dish retrieval. |
| **G7 → G4** | **OR** | If the patient can retrieve, the tray delivery is chosen. |
| **G7 → G3** | **OR** | If the patient cannot retrieve, the table delivery is chosen. |
| **G5 → G5.1** | **OR** | Unassisted retrieval is preferred if possible. |
| **G5 → G5.2** | **OR** | Robot‑robot retrieval is the next fallback. |
| **G5 → G5.3** | **OR** | Human‑assisted retrieval is the last resort. |
| **G6 → G6.1** | **OR** | Robot‑human door opening is the preferred method. |
| **G6 → G6.2** | **OR** | Robot‑robot door opening is the second option. |
| **G6 → G6.3** | **OR** | Human‑only door opening is the fallback. |
| **G5.1 → AT10** | **AND** | Moving to the room is needed before picking dishes. |
| **G5.1 → AT11** | **AND** | Secure dishes after picking. |
| **G5.2 → AT12** | **AND** | Coordination handshake before joint pickup. |
| **G5.2 → AT13** | **AND** | Joint pickup action. |
| **G5.3 → AT14** | **AND** | Robot requests assistance before human acts. |
| **G5.3 → AT15** | **AND** | Human picks dishes. |
| **G5.3 → AT16** | **AND** | Robot secures dishes. |
| **G6.1 → AT17** | **AND** | Robot signals before human opens. |
| **G6.1 → AT18** | **AND** | Human opens door. |
| **G6.2 → AT19** | **AND** | Robot A signals before B opens. |
| **G6.2 → AT20** | **AND** | Robot B opens door. |
| **G6.3 → AT21** | **AND** | Human opens door alone. |
| **G4 → AT1** | **AND** | Robot must pick meal before delivering to tray. |
| **G4 → AT2** | **AND** | Robot must deliver meal to tray. |
| **G4 → AT3** | **AND** | Robot must indicate meal to patient. |
| **G3 → AT4** | **AND** | Robot must pick meal before table delivery. |
| **G3 → AT5** | **AND** | Robot must place meal on table. |
| **G8 → AT6** | **AND** | Wait for patient retrieval. |
| **G8 → AT7** | **AND** | Verify meal identity. |
| **G8 → AT9** | **AND** | Log retrieval. |
| **G9 → AT8** | **AND** | Alert wrong meal. |

---

### Rationale for Runtime Choices

* **Sequential (`;`)** – The overall mission (G1) must finish in a logical order: first determine capability (G2), decide delivery mode (G7), perform delivery (G3/G4), monitor retrieval (G8), then perform cleanup (G5) and open the door (G6).  
* **Parallel (`#`)** – Not used in this model because the tasks are tightly coupled; each step depends on the previous one (e.g., you cannot retrieve dishes before the meal is delivered and the room is accessible).  
* **Fallback (`FALLBACK`)** – Used for decisions with uncertainty or multiple cooperation strategies:  
  * Delivery mode (G7).  
  * Dish retrieval (G5).  
  * Door opening (G6).  
  The nesting of `FALLBACK` preserves binary structure while allowing more than two alternatives.

---

## 5. Final Remarks

This goal model captures the full spectrum of the hospital food‑delivery scenario:

* **Decision making** under uncertainty (patient retrieval capability).  
* **Multiple cooperation modes** (robot‑human, robot‑robot, human‑only).  
* **Safety and accountability** (meal identity verification, wrong meal alert).  
* **Cleanup and room access** (dish retrieval, door opening).  

All goals and tasks are explicitly typed, justified, and linked with clear logical relations, making the model suitable for implementation in a multi‑robot system planner or a hierarchical task network (HTN) framework.
