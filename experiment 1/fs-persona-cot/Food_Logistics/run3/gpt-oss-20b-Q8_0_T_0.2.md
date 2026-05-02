**Goal Model – Multi‑Robot Food Delivery**

| **Name** | **Text**                                                | **Runtime**                            | **Goal Type** | **Target Condition / Enquired Information**       | **Relation**   | **Justification**                                                                                                         | **Ground truth I**                                   | **Ground truth C** | **Consensus**                                        |
| -------- | ------------------------------------------------------- | -------------------------------------- | ------------- | ------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ---------------------------------------------------- |
| **G1**   | Deliver food from the kitchen to an inpatient room.     | `;`                                    | Perform       | –                                                 | –              | The overall mission is a sequence of sub-tasks: request reception, transport, delivery, dish retrieval, and coordination. | Ok                                                   | Ok                 | Ok                                                   |
| **G2**   | Receive kitchen delivery request.                       | `-`                                    | Perform       | –                                                 | AND (under G1) | The robot must first know what to deliver; otherwise no further action is possible.                                       | Query. Enqueried information: food to be delivered   | Ok                 | Query. Enqueried information: food to be delivered   |
| **G3**   | Transport food to the room.                             | `;`                                    | Perform       | –                                                 | AND (under G1) | Transport is a prerequisite for delivery; it must be completed before the food can be handed over or placed.              | OK                                                   | Ok                 | OK                                                   |
| **G6**   | Open the room door.                                     | `-`                                    | Perform       | –                                                 | AND (under G3) | The robot cannot enter the room until the door is open.                                                                   | Ok                                                   | Ok                 | Ok                                                   |
| **G3.1** | Move to the room with the food.                         | `-`                                    | Perform       | –                                                 | AND (under G3) | Physical movement is the core of the transport action.                                                                    | OK                                                   | Ok                 | OK                                                   |
| **G4**   | Deliver food to the patient or to the table.            | `;`                                    | Perform       | –                                                 | AND (under G1) | Delivery is the final step of the mission; it must succeed for the goal to be achieved.                                   | Ok                                                   | Ok                 | Ok                                                   |
| **G7**   | Query patient’s ability to retrieve food from the tray. | `-`                                    | Query         | “Can the patient or companion retrieve the meal?” | AND (under G4) | The robot needs this information to decide whether to hand over or place the meal.                                        | OK                                                   | Ok                 | OK                                                   |
| **G4.1** | Hand over the meal to the patient.                      | `-`                                    | Perform       | –                                                 | AND (under G4) | Direct hand-over is possible only if the patient can retrieve the meal.                                                   | Ok                                                   | Ok                 | Ok                                                   |
| **G4.2** | Place the meal on the room table.                       | `-`                                    | Perform       | –                                                 | AND (under G4) | Table placement is the fallback when hand-over is not feasible.                                                           | OK                                                   | Ok                 | OK                                                   |
| **G5**   | Retrieve dirty dishes from the room.                    | `FALLBACK(G5.1, FALLBACK(G5.2, G5.3))` | Perform       | –                                                 | AND (under G1) | Dish retrieval can be attempted in priority order: unassisted → two robots → human assistance.                            | Achieve. Target condition: all dishes were retrieved | Ok                 | Achieve. Target condition: all dishes were retrieved |
| **G5.1** | Retrieve dishes unassisted.                             | `-`                                    | Perform       | –                                                 | AND (under G5) | If the robot can lift the dishes alone, this is the simplest solution.                                                    | OK                                                   | Ok                 | OK                                                   |
| **G5.2** | Retrieve dishes with two robots.                        | `-`                                    | Perform       | –                                                 | AND (under G5) | Heavy or bulky dishes may require a second robot.                                                                         | OK                                                   | Ok                 | OK                                                   |
| **G5.3** | Retrieve dishes with a human.                           | `-`                                    | Perform       | –                                                 | AND (under G5) | If no second robot is available, a human can help.                                                                        | OK                                                   | Ok                 | OK                                                   |
| **G8**   | Track when and where each meal was retrieved.           | `-`                                    | Perform       | –                                                 | AND (under G1) | The system must maintain a record for accountability and error detection.                                                 | OK                                                   | Ok                 | OK                                                   |
| **G9**   | Alert if the wrong meal is retrieved.                   | `-`                                    | Perform       | –                                                 | AND (under G1) | Ensures patient safety and correct meal delivery.                                                                         | OK                                                   | Ok                 | OK                                                   |
| **G10**  | Indicate which meal should be retrieved by the patient. | `-`                                    | Perform       | –                                                 | AND (under G1) | Needed when the patient is fetching from the tray.                                                                        | OK                                                   | Ok                 | OK                                                   |
| **G12**  | Call the robot to pick up dishes.                       | `-`                                    | Perform       | –                                                 | AND (under G1) | Allows a patient or staff to request dish retrieval on demand.                                                            | Ok                                                   | Ok                 | Ok                                                   |
| **G13**  | Wait for the patient to retrieve the meal.              | `-`                                    | Perform       | –                                                 | AND (under G1) | The robot must monitor the patient’s action before proceeding.                                                            | OK                                                   | Ok                 | OK                                                   |
| **G14**  | Coordinate with another robot for joint tasks.          | `-`                                    | Perform       | –                                                 | AND (under G1) | Some actions (e.g., door opening, heavy dish lifting) may require a second robot.                                         | OK                                                   | Ok                 | OK                                                   |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Receive kitchen delivery request. | AND (under G2) | Kitchen | 1 | Robot must be in the kitchen to receive the request. |
| **AT2** | Pick up meals from the kitchen. | AND (under G3.1) | Kitchen | 1 | Robot must physically collect the meals. |
| **AT3** | Open the room door with the robot. | OR (under G6) | Room door | 1 | Robot can open the door autonomously. |
| **AT4** | Wait for a human to open the door. | OR (under G6) | Room door | 1 | Human may be present and open the door. |
| **AT5** | Deliver the meal to the room table. | AND (under G4.2) | Room table | 1 | Requires the robot’s manipulation skill to place the meal. |
| **AT6** | Hand over the meal to the patient. | AND (under G4.1) | Room | 1 | Direct hand‑over requires the robot’s manipulation skill. |
| **AT7** | Indicate which meal the patient should retrieve. | AND (under G10) | Room | 1 | Robot must communicate the correct meal to the patient. |
| **AT8** | Track meal retrieval (time & location). | AND (under G8) | Room | 1 | Robot must log the event for accountability. |
| **AT9** | Alert if the wrong meal is retrieved. | AND (under G9) | Room | 1 | Robot must detect and notify the patient or staff. |
| **AT10** | Retrieve dishes unassisted. | AND (under G5.1) | Room | 1 | Robot can lift dishes alone if they are light enough. |
| **AT11** | Retrieve dishes with two robots. | AND (under G5.2) | Room | 2 | Heavy dishes may require two robots. |
| **AT12** | Retrieve dishes with a human. | AND (under G5.3) | Room | 1 | Human assistance may be needed if the robot cannot lift alone. |
| **AT13** | Call the robot to pick up dishes. | AND (under G12) | Room | 1 | Robot initiates the dish‑retrieval process on request. |
| **AT14** | Wait for door opening signal. | AND (under G11) | Room | 1 | Robot must pause until the door is opened. |
| **AT15** | Wait for patient to retrieve the meal. | AND (under G13) | Room | 1 | Robot must monitor the patient’s action. |
| **AT16** | Coordinate with another robot for joint tasks. | AND (under G14) | Room | 2 | Joint tasks (e.g., door opening, heavy lifting) require coordination. |

---

### Summary Table (Goals + Tasks)

| **ID** | **Type** | **Text** | **Runtime / Relation** | **Location / Robots** | **Justification** |
|--------|----------|----------|------------------------|-----------------------|-------------------|
| G1 | Goal | Deliver food from kitchen to inpatient room | `;` (sequential) | – | Overall mission is a sequence of sub‑tasks. |
| G2 | Goal | Receive kitchen delivery request | `-` | – | Must know what to deliver first. |
| AT1 | Task | Receive kitchen delivery request | AND (under G2) | Kitchen, 1 | Robot must be in kitchen. |
| G3 | Goal | Transport food to the room | `;` | – | Transport precedes delivery. |
| G6 | Goal | Open the room door | `-` | – | Door must be open before entering. |
| AT3 | Task | Open door with robot | OR (under G6) | Room door, 1 | Robot can open door. |
| AT4 | Task | Wait for human to open door | OR (under G6) | Room door, 1 | Human may open door. |
| G3.1 | Goal | Move to the room with the food | `-` | – | Physical movement. |
| AT2 | Task | Pick up meals from kitchen | AND (under G3.1) | Kitchen, 1 | Robot must collect meals. |
| G4 | Goal | Deliver food to patient or table | `;` | – | Final step of mission. |
| G7 | Goal | Query patient’s ability to retrieve food | `-` | – | Needed to decide delivery mode. |
| AT7 | Task | Indicate which meal to retrieve | AND (under G10) | Room, 1 | Robot must communicate. |
| G4.1 | Goal | Hand over the meal to patient | `-` | – | Requires patient to retrieve. |
| AT6 | Task | Hand over meal to patient | AND (under G4.1) | Room, 1 | Direct hand‑over. |
| G4.2 | Goal | Place meal on table | `-` | – | Fallback when hand‑over not possible. |
| AT5 | Task | Deliver meal to table | AND (under G4.2) | Room table, 1 | Manipulation skill needed. |
| G5 | Goal | Retrieve dirty dishes | `FALLBACK(G5.1, FALLBACK(G5.2, G5.3))` | – | Priority order of assistance. |
| AT10 | Task | Retrieve dishes unassisted | AND (under G5.1) | Room, 1 | Robot can lift alone. |
| AT11 | Task | Retrieve dishes with two robots | AND (under G5.2) | Room, 2 | Heavy dishes need two robots. |
| AT12 | Task | Retrieve dishes with human | AND (under G5.3) | Room, 1 | Human assistance required. |
| G8 | Goal | Track meal retrieval | `-` | – | Accountability. |
| AT8 | Task | Track meal retrieval | AND (under G8) | Room, 1 | Robot logs event. |
| G9 | Goal | Alert wrong meal retrieval | `-` | – | Safety. |
| AT9 | Task | Alert wrong meal | AND (under G9) | Room, 1 | Robot notifies. |
| G10 | Goal | Indicate meal to patient | `-` | – | Needed for patient retrieval. |
| G12 | Goal | Call robot to pick up dishes | `-` | – | On‑demand dish retrieval. |
| AT13 | Task | Call robot to pick up dishes | AND (under G12) | Room, 1 | Robot initiates process. |
| G13 | Goal | Wait for patient to retrieve | `-` | – | Robot must monitor. |
| AT15 | Task | Wait for patient to retrieve | AND (under G13) | Room, 1 | Robot pauses. |
| G14 | Goal | Coordinate with another robot | `-` | – | Joint tasks. |
| AT16 | Task | Coordinate with another robot | AND (under G14) | Room, 2 | Coordination needed. |

---

### Logical Relationships

| **Parent → Children** | **Relation** | **Runtime** | **Justification** |
|-----------------------|--------------|-------------|-------------------|
| **G1 → G2, G3, G4, G5, G8, G9, G10, G12, G13, G14** | AND | `;` | All sub‑goals must be satisfied sequentially for the overall delivery to be considered complete. |
| **G3 → G6, G3.1** | AND | `;` | The robot must open the door before it can move into the room. |
| **G4 → G7, G4.1, G4.2** | AND | `;` | The robot must know the patient’s capability before deciding between hand‑over or table placement. |
| **G5 → G5.1, G5.2, G5.3** | AND | `FALLBACK(G5.1, FALLBACK(G5.2, G5.3))` | Dish retrieval is attempted in priority order: unassisted → two robots → human assistance. |
| **G6 → AT3, AT4** | OR | `#` | Either the robot opens the door itself or a human does it. |
| **G4.1 → AT6** | AND | `-` | Hand‑over requires the specific task. |
| **G4.2 → AT5** | AND | `-` | Table placement requires the specific task. |
| **G7 → (none)** | – | – | Query goal has no tasks; its result informs G4. |
| **G10 → AT7** | AND | `-` | Indicating the meal is a separate task. |
| **G8 → AT8** | AND | `-` | Tracking is a separate task. |
| **G9 → AT9** | AND | `-` | Alerting is a separate task. |
| **G5.1 → AT10** | AND | `-` | Unassisted retrieval is a separate task. |
| **G5.2 → AT11** | AND | `-` | Two‑robot retrieval is a separate task. |
| **G5.3 → AT12** | AND | `-` | Human‑assisted retrieval is a separate task. |
| **G12 → AT13** | AND | `-` | Calling the robot is a separate task. |
| **G13 → AT15** | AND | `-` | Waiting for patient is a separate task. |
| **G14 → AT16** | AND | `-` | Coordination is a separate task. |

---

**Key Design Decisions**

1. **Sequential vs. Parallel** – The top‑level goal is sequential because the robot must finish each phase before moving to the next (e.g., it cannot deliver before it has the food).  
2. **Fallbacks** – Dish retrieval and delivery mode use fallback to reflect priority and uncertainty.  
3. **OR Decompositions** – Door opening and delivery mode are OR because either the robot or a human can perform the action.  
4. **Query Goal** – Patient retrieval capability is a query; its result influences the delivery mode but does not itself require an action.  
5. **Task Locations & Robot Numbers** – Each task’s location and robot count are chosen to reflect the physical constraints described (e.g., two robots needed for heavy dishes).  

This goal and task model captures the mission’s structure, decision points, and uncertainty, providing a clear blueprint for multi‑robot coordination.
