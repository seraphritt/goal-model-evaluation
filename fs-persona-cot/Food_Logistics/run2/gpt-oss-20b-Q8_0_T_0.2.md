## 1. Goal Model – Tables

| **Name**   | **Text**                                                                             | **Runtime**                          | **Goal Type** | **Target Condition / Enquired Information** | **Relation** | **Justification**                                                                                                                                                   | **Ground truth I**                                   | **Ground truth C** | **Consensus**                                        |
| ---------- | ------------------------------------------------------------------------------------ | ------------------------------------ | ------------- | ------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ---------------------------------------------------- |
| **G1**     | Deliver food from the kitchen to an inpatient room in response to a kitchen request. | `FALLBACK(G2, G3)`                   | Perform       | –                                           | OR           | The robot can satisfy the delivery either by placing the food on the table or by placing it on the patient’s tray. Either option is sufficient for the parent goal. | Achieve. Target condition: all food was delivered    | Ok                 | Achieve. Target condition: all food was delivered    |
| **G2**     | Deliver food onto the room table.                                                    | `;`                                  | Perform       | –                                           | AND          | The table delivery requires two sequential steps: opening the door and placing the food on the table.                                                               | ok                                                   | Ok                 | ok                                                   |
| **G2.1**   | Open the room door to allow the robot to enter.                                      | `FALLBACK(AT1, AT2)`                 | Perform       | –                                           | OR           | The door can be opened by the robot itself or by a human; the robot only needs one of these to succeed.                                                             | ok                                                   | Ok                 | ok                                                   |
| **G2.2**   | Place food onto the room table.                                                      | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot simply manipulates the food onto the table.                                                                                                   | ok                                                   | Ok                 | ok                                                   |
| **G3**     | Deliver food onto the patient’s tray.                                                | `;`                                  | Perform       | –                                           | AND          | The tray delivery requires first checking whether the patient can retrieve the food, then actually placing it on the tray.                                          | ok                                                   | Ok                 | ok                                                   |
| **G3.1**   | Check whether the patient (or a companion/nurse) can retrieve food from the tray.    | `-`                                  | Query         | `canRetrieveFromTray`                       | AND          | The robot must know whether the patient can retrieve the food; this is a pure information-retrieval goal.                                                           | ok                                                   | Ok                 | ok                                                   |
| **G3.2**   | Deliver food to the tray **and** indicate which meal the patient should retrieve.    | `;`                                  | Perform       | –                                           | AND          | The robot must first place the food on the tray and then inform the patient which meal to take.                                                                     | ok                                                   | Ok                 | ok                                                   |
| **G3.2.1** | Place food onto the patient’s tray.                                                  | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot manipulates the food onto the tray.                                                                                                           | ok                                                   | Ok                 | ok                                                   |
| **G3.2.2** | Indicate to the patient which meal should be retrieved.                              | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot communicates the meal identity to the patient.                                                                                                | ok                                                   | Ok                 | ok                                                   |
| **G4**     | Record when and where each meal was retrieved.                                       | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot logs retrieval data.                                                                                                                          | ok                                                   | Ok                 | ok                                                   |
| **G5**     | Alert if the wrong meal is retrieved.                                                | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot monitors the retrieval and raises an alarm if a mismatch occurs.                                                                              | ok                                                   | Ok                 | ok                                                   |
| **G6**     | Retrieve dirty dishes from the room.                                                 | `FALLBACK(FALLBACK(AT8, AT9), AT10)` | Perform       | –                                           | OR           | Dish retrieval can be done unassisted, with two robots, or with a robot and a human; any one of these suffices.                                                     | Achieve. Target condition: all dishes were delivered | Ok                 | Achieve. Target condition: all dishes were delivered |
| **G6.1**   | Retrieve dishes unassisted.                                                          | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot alone picks up the dishes.                                                                                                                    | ok                                                   | Ok                 | ok                                                   |
| **G6.2**   | Retrieve dishes with two robots cooperating.                                         | `-`                                  | Perform       | –                                           | AND          | Leaf goal – two robots share the load.                                                                                                                              | ok                                                   | Ok                 | ok                                                   |
| **G6.3**   | Retrieve dishes with a robot and a human cooperating.                                | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot works with a human.                                                                                                                           | ok                                                   | Ok                 | ok                                                   |
| **G7**     | Open the room door to allow dish retrieval.                                          | `FALLBACK(AT1, AT2)`                 | Perform       | –                                           | OR           | The door can be opened by the robot or by a human; the robot only needs one of these.                                                                               | ok                                                   | Ok                 | ok                                                   |
| **G8**     | Wait for a call from a person in the room to pick up dishes.                         | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot simply waits for a call signal.                                                                                                               | ok                                                   | Ok                 | ok                                                   |
| **G8.1**   | Wait for the call signal.                                                            | `-`                                  | Perform       | –                                           | AND          | Leaf goal – the robot monitors the call channel.                                                                                                                    | ok                                                   | Ok                 | ok                                                   |

---

## 2. Task Model – Tables

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Robot opens the room door. | AND | room door | 1 | The robot has the necessary manipulation skill to open the door. |
| **AT2** | Robot waits for a human to open the door. | AND | room door | 1 | The robot can idle while a human performs the action. |
| **AT3** | Robot places food onto the room table. | AND | room table | 1 | The robot must manipulate the food onto the table. |
| **AT4** | Robot places food onto the patient’s tray. | AND | room tray | 1 | The robot must manipulate the food onto the tray. |
| **AT5** | Robot indicates which meal the patient should retrieve. | AND | room | 1 | The robot communicates the meal identity to the patient. |
| **AT6** | Robot records retrieval time and location. | AND | robot memory | 1 | The robot logs data for later audit. |
| **AT7** | Robot detects if the wrong meal was retrieved. | AND | room | 1 | The robot monitors the patient’s action and compares it to the logged meal. |
| **AT8** | Robot picks up dishes alone. | AND | room | 1 | The robot can handle the dishes by itself. |
| **AT9** | Two robots cooperate to pick up dishes. | AND | room | 2 | Two robots can share the load and coordinate. |
| **AT10** | Robot cooperates with a human to pick up dishes. | AND | room | 1 | The robot can assist a human in lifting dishes. |
| **AT11** | Robot waits for a call signal from a person in the room. | AND | room | 1 | The robot monitors the call channel. |
| **AT12** | Robot queries patient record and companion presence. | AND | robot memory | 1 | The robot accesses the patient database to determine retrieval capability. |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Type** | **Title** | **Runtime / Relation** | **Justification** |
|--------|----------|-----------|------------------------|-------------------|
| **G1** | Goal | Deliver Food to Room | `FALLBACK(G2, G3)` | Either table or tray delivery satisfies the parent. |
| **G2** | Goal | Deliver Food to Table | `;` | Must open door then deliver. |
| **G2.1** | Goal | Open Door for Table | `FALLBACK(AT1, AT2)` | Robot or human can open. |
| **G2.2** | Goal | Deliver Food to Table | `-` | Leaf. |
| **G3** | Goal | Deliver Food to Tray | `;` | Check capability then deliver. |
| **G3.1** | Goal | Check Retrieval Capability | `-` | Query. |
| **G3.2** | Goal | Deliver Food to Tray Sequence | `;` | Deliver then indicate. |
| **G3.2.1** | Goal | Deliver Food to Tray | `-` | Leaf. |
| **G3.2.2** | Goal | Indicate Meal | `-` | Leaf. |
| **G4** | Goal | Track Retrieval | `-` | Leaf. |
| **G5** | Goal | Alert Wrong Meal | `-` | Leaf. |
| **G6** | Goal | Retrieve Dishes | `FALLBACK(FALLBACK(AT8, AT9), AT10)` | Any cooperation mode works. |
| **G6.1** | Goal | Retrieve Dishes Unassisted | `-` | Leaf. |
| **G6.2** | Goal | Retrieve Dishes with Two Robots | `-` | Leaf. |
| **G6.3** | Goal | Retrieve Dishes with Robot+Human | `-` | Leaf. |
| **G7** | Goal | Open Door for Dishes | `FALLBACK(AT1, AT2)` | Robot or human can open. |
| **G8** | Goal | Call Robot | `-` | Leaf. |
| **G8.1** | Goal | Wait for Call | `-` | Leaf. |
| **AT1** | Task | Open Door by Robot | AND | Robot can open. |
| **AT2** | Task | Wait for Human to Open Door | AND | Robot can wait. |
| **AT3** | Task | Deliver Food to Table | AND | Robot manipulates food. |
| **AT4** | Task | Deliver Food to Tray | AND | Robot manipulates food. |
| **AT5** | Task | Indicate Meal | AND | Robot communicates. |
| **AT6** | Task | Record Retrieval | AND | Robot logs. |
| **AT7** | Task | Detect Wrong Meal | AND | Robot monitors. |
| **AT8** | Task | Retrieve Dishes Unassisted | AND | Robot can lift. |
| **AT9** | Task | Retrieve Dishes with Two Robots | AND | Two robots cooperate. |
| **AT10** | Task | Retrieve Dishes with Robot+Human | AND | Robot assists human. |
| **AT11** | Task | Wait for Call | AND | Robot monitors call. |
| **AT12** | Task | Query Retrieval Capability | AND | Robot accesses records. |

---

## 4. Logical Relationships (Tree Structure)

| **Parent → Children** | **Relation** | **Runtime** | **Justification** |
|------------------------|--------------|-------------|-------------------|
| **G1 → G2, G3** | OR | `FALLBACK(G2, G3)` | Either table or tray delivery satisfies the parent. |
| **G2 → G2.1, G2.2** | AND | `;` | Must open door *and* deliver to table. |
| **G2.1 → AT1, AT2** | OR | `FALLBACK(AT1, AT2)` | Robot can open door *or* wait for human. |
| **G2.2 → AT3** | AND | `-` | Leaf. |
| **G3 → G3.1, G3.2** | AND | `;` | Must check capability *and* deliver to tray. |
| **G3.1 → AT12** | AND | `-` | Query patient record. |
| **G3.2 → G3.2.1, G3.2.2** | AND | `;` | Must deliver to tray *and* indicate meal. |
| **G3.2.1 → AT4** | AND | `-` | Leaf. |
| **G3.2.2 → AT5** | AND | `-` | Leaf. |
| **G4 → AT6** | AND | `-` | Leaf. |
| **G5 → AT7** | AND | `-` | Leaf. |
| **G6 → G6.1, G6.2, G6.3** | OR | `FALLBACK(FALLBACK(AT8, AT9), AT10)` | Any cooperation mode works. |
| **G6.1 → AT8** | AND | `-` | Leaf. |
| **G6.2 → AT9** | AND | `-` | Leaf. |
| **G6.3 → AT10** | AND | `-` | Leaf. |
| **G7 → AT1, AT2** | OR | `FALLBACK(AT1, AT2)` | Robot or human can open door. |
| **G8 → AT11** | AND | `-` | Leaf. |
| **G8.1 → AT11** | AND | `-` | Leaf. |

---

### Why the chosen decomposition?

1. **OR vs AND** – The mission explicitly states that the robot can deliver food either onto the table or onto the tray. This is a classic *choice* scenario, so the top‑level goal uses an OR (fallback) decomposition.  
2. **Sequential steps** – Opening the door must happen *before* the robot can place food on the table or tray. Hence the use of a sequential (`;`) operator for the sub‑goals that involve both opening and placing.  
3. **Uncertainty in retrieval** – Whether the patient can retrieve from the tray is uncertain and depends on external information. This is captured as a *query* goal (`G3.1`) that feeds into the decision to deliver to the tray.  
4. **Cooperation modes** – Dish retrieval can be performed in several ways. An OR decomposition with a fallback chain models the fact that the robot will try the simplest mode first (unassisted) and fall back to more complex cooperation if needed.  
5. **Human‑robot interaction** – Opening the door or waiting for a call can be done by a human or the robot. These are represented as OR decompositions between a robot task and a waiting task.  
6. **Tracking and alerting** – These are straightforward perform goals that are leaf nodes because they involve only a single action (recording or detecting).  

All runtime annotations, goal types, and task properties are justified by the mission description and the functional requirements of a multi‑robot system.
