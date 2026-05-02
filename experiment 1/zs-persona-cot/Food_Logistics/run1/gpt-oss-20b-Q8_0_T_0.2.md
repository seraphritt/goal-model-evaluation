## 1. Goal Model – Tables

| **Name**     | **Text**                                                                  | **Runtime**                                | **Goal Type** | **Target Condition / Enquired Information**                                                                               | **Relation**                                                                                                         | **Justification**                                                                                                                                                                                                                 | **Ground truth I** | **Ground truth C** | **Consensus** |
| ------------ | ------------------------------------------------------------------------- | ------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------ | ------------- |
| **G1**       | Deliver food to inpatient rooms and retrieve all dirty dishes             | #                                          | **Achieve**   | *All ordered meals are delivered to the correct inpatient rooms and all dirty dishes have been removed from those rooms.* | –                                                                                                                    | Top-level mission: both food delivery and dish retrieval must finish. Parallel execution is possible because the two activities are independent.                                                                                  | Perform            | Perform            | Perform       |
| **G2**       | Food delivery sub-mission                                                 | ;                                          | **Achieve**   | *All requested meals are correctly delivered to the patient’s room.*                                                      | AND (with G3)                                                                                                        | Food delivery is a distinct sub-mission that must succeed before the overall mission can be considered complete. Sequential order is chosen because the next sub-goal (dish retrieval) can start only after delivery is finished. | OK                 | Perform            | OK            |
| **G2.1**     | Determine if patient can fetch food from tray                             | -                                          | **Query**     | *Can the patient, a companion, or a nurse fetch food from the robot’s tray?*                                              | AND (with G2.2)                                                                                                      | The robot must know the patient’s ability before deciding the delivery method.                                                                                                                                                    | OK                 | OK                 | OK            |
| **G2.2**     | Choose delivery method (table or tray)                                    | FALLBACK(G2.2.1, G2.2.2)                   | **Perform**   | –                                                                                                                         | The robot has two mutually exclusive ways to deliver. If the tray-fetch plan fails, it falls back to table delivery. |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G2.2.1**   | Deliver food to the patient’s table                                       | -                                          | **Perform**   | –                                                                                                                         | Simple manipulation task that places food on the table.                                                              |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G2.2.2**   | Fetch food from the robot’s tray                                          | ;                                          | **Perform**   | –                                                                                                                         | Consists of a sequence of sub-tasks that must be executed in order.                                                  |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G2.2.2.1** | Bring tray to patient’s room                                              | -                                          | **Perform**   | –                                                                                                                         | Robot must carry the tray to the room before the patient can fetch.                                                  |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G2.2.2.2** | Open the room door for tray delivery                                      | -                                          | **Perform**   | –                                                                                                                         | Door opening may involve another robot or a human; the robot must perform the action.                                |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G2.2.2.3** | Indicate which meal the patient should take                               | -                                          | **Perform**   | –                                                                                                                         | Prevents the patient from taking the wrong meal.                                                                     |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G2.2.2.4** | Monitor the patient’s retrieval of the meal                               | -                                          | **Perform**   | –                                                                                                                         | Ensures the patient actually takes the indicated meal.                                                               |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G2.2.2.5** | Alert if the wrong meal is retrieved                                      | -                                          | **Perform**   | –                                                                                                                         | Immediate notification is required to correct errors.                                                                |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G3**       | Dish retrieval sub-mission                                                | ;                                          | **Achieve**   | *All dirty dishes have been removed from the patient’s room.*                                                             | AND (with G2)                                                                                                        | Must finish after food delivery; sequentially after G2.                                                                                                                                                                           | OK                 | Perform            | OK            |
| **G3.1**     | Identify dirty dishes in the room                                         | -                                          | **Perform**   | –                                                                                                                         | Robot must detect dishes before attempting removal.                                                                  |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G3.2**     | Choose dish retrieval method (unassisted, robot-assisted, human-assisted) | FALLBACK(FALLBACK(G3.2.1, G3.2.2), G3.2.3) | **Perform**   | –                                                                                                                         | Three mutually exclusive options; fallback is used if a method fails.                                                |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G3.2.1**   | Retrieve dishes unassisted                                                | -                                          | **Perform**   | –                                                                                                                         | Robot picks up dishes by itself.                                                                                     |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G3.2.2**   | Retrieve dishes with another robot                                        | -                                          | **Perform**   | –                                                                                                                         | Robot cooperates with a second robot to lift heavier loads.                                                          |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G3.2.3**   | Retrieve dishes with a human                                              | -                                          | **Perform**   | –                                                                                                                         | Human assists the robot in lifting or carrying dishes.                                                               |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |
| **G3.3**     | Open the room door for dish retrieval                                     | -                                          | **Perform**   | –                                                                                                                         | Robot must open the door before any dish can be taken.                                                               |                                                                                                                                                                                                                                   | OK                 | OK                 | OK            |


---

## 2. Task Model – Tables

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | Deliver food to the patient’s table | AND (under G2.2.1) | Inpatient room | 1 | Single robot performs the manipulation skill to place food on the table. |
| **AT2** | Bring tray to the patient’s room | AND (under G2.2.2.1) | Inpatient room | 1 | Robot must transport the tray; no cooperation required. |
| **AT3** | Open the room door for tray delivery | AND (under G2.2.2.2) | Room door | 1 | Robot can open the door; may involve a human, but the robot’s action is independent. |
| **AT4** | Indicate which meal the patient should take | AND (under G2.2.2.3) | Inpatient room | 1 | Robot communicates the correct meal to the patient. |
| **AT5** | Monitor the patient’s retrieval of the meal | AND (under G2.2.2.4) | Inpatient room | 1 | Robot observes the patient to confirm correct retrieval. |
| **AT6** | Alert if the wrong meal is retrieved | AND (under G2.2.2.5) | Inpatient room | 1 | Robot triggers an alarm or notification when a mismatch occurs. |
| **AT7** | Scan the room for dirty dishes | AND (under G3.1) | Inpatient room | 1 | Robot uses sensors to detect dishes. |
| **AT8** | Pick up a dish unassisted | AND (under G3.2.1) | Inpatient room | 1 | Robot lifts a dish by itself. |
| **AT9** | Robot cooperatively pick up a dish | AND (under G3.2.2) | Inpatient room | 2 | Two robots coordinate to lift heavier dishes. |
| **AT10** | Human assists the robot in picking up a dish | AND (under G3.2.3) | Inpatient room | 1 | Robot performs the action while a human helps. |
| **AT11** | Open the room door for dish retrieval | AND (under G3.3) | Room door | 1 | Robot opens the door, possibly with human assistance. |

---

## 3. Summary Table

| **Goal / Task** | **ID** | **Type** | **Runtime** | **Relation** | **Justification** |
|------------------|--------|----------|-------------|--------------|-------------------|
| Deliver food to inpatient rooms and retrieve all dirty dishes | G1 | Goal – Achieve | # | – | Both sub‑missions must finish; can run in parallel. |
| Food delivery sub‑mission | G2 | Goal – Achieve | ; | AND (with G3) | Must finish before overall mission; sequential. |
| Determine if patient can fetch food from tray | G2.1 | Goal – Query | - | AND (with G2.2) | Must know before choosing method. |
| Choose delivery method | G2.2 | Goal – Perform | FALLBACK(G2.2.1, G2.2.2) | – | Two exclusive options; fallback if first fails. |
| Deliver food to the table | G2.2.1 | Goal – Perform | - | – | Direct manipulation. |
| Fetch food from tray | G2.2.2 | Goal – Perform | ; | – | Sequence of sub‑tasks. |
| Bring tray to room | AT2 | Task | – | – | Robot transports tray. |
| Open door for tray delivery | AT3 | Task | – | – | Robot opens door. |
| Indicate meal | AT4 | Task | – | – | Robot informs patient. |
| Monitor retrieval | AT5 | Task | – | – | Robot observes patient. |
| Alert wrong meal | AT6 | Task | – | – | Robot notifies error. |
| Deliver food to table | AT1 | Task | – | – | Robot places food. |
| Dish retrieval sub‑mission | G3 | Goal – Achieve | ; | AND (with G2) | Must finish after food delivery. |
| Identify dirty dishes | G3.1 | Goal – Perform | - | – | Robot scans for dishes. |
| Choose dish retrieval method | G3.2 | Goal – Perform | FALLBACK(FALLBACK(G3.2.1, G3.2.2), G3.2.3) | – | Three options; fallback. |
| Retrieve dishes unassisted | G3.2.1 | Goal – Perform | - | – | Robot lifts alone. |
| Retrieve dishes with robot | G3.2.2 | Goal – Perform | - | – | Two robots cooperate. |
| Retrieve dishes with human | G3.2.3 | Goal – Perform | - | – | Human assists. |
| Open door for dish retrieval | G3.3 | Goal – Perform | - | – | Robot opens door. |
| Scan for dishes | AT7 | Task | – | – | Robot detects dishes. |
| Pick up dish unassisted | AT8 | Task | – | – | Robot lifts. |
| Robot cooperatively pick up dish | AT9 | Task | – | – | Two robots lift. |
| Human assists pick up dish | AT10 | Task | – | – | Human helps. |
| Open door for dish retrieval | AT11 | Task | – | – | Robot opens door. |

---

## 4. Logical Relationships

| **Parent** | **Children** | **Relation** | **Runtime** | **Justification** |
|------------|--------------|--------------|-------------|-------------------|
| **G1** | G2, G3 | AND | # | Both food delivery and dish retrieval must succeed; they can run in parallel. |
| **G2** | G2.1, G2.2 | AND | ; | Delivery method decision must precede the actual delivery. |
| **G2.1** | – | – | – | Query goal; no children. |
| **G2.2** | G2.2.1, G2.2.2 | OR (FALLBACK) | FALLBACK(G2.2.1, G2.2.2) | Two mutually exclusive delivery modes; fallback if first fails. |
| **G2.2.1** | AT1 | AND | – | Single task to deliver to table. |
| **G2.2.2** | AT2, AT3, AT4, AT5, AT6 | AND | ; | Sequence of tasks required for tray‑fetch. |
| **G3** | G3.1, G3.2, G3.3 | AND | ; | Dish retrieval steps must all be completed. |
| **G3.1** | AT7 | AND | – | Task to detect dishes. |
| **G3.2** | G3.2.1, G3.2.2, G3.2.3 | OR (FALLBACK) | FALLBACK(FALLBACK(G3.2.1, G3.2.2), G3.2.3) | Three mutually exclusive retrieval methods; fallback if one fails. |
| **G3.2.1** | AT8 | AND | – | Unassisted pick‑up. |
| **G3.2.2** | AT9 | AND | – | Robot‑robot cooperation. |
| **G3.2.3** | AT10 | AND | – | Human assistance. |
| **G3.3** | AT11 | AND | – | Door opening for dish retrieval. |

---

### Key Design Decisions & Justifications

1. **Parallel vs Sequential**  
   * **G1** uses parallel (`#`) because food delivery and dish retrieval are independent and can be performed simultaneously.  
   * **G2** and **G3** use sequential (`;`) because each sub‑mission must finish before the overall mission can be considered complete (e.g., dish retrieval only after food delivery to avoid interference).  

2. **Fallback for OR Decompositions**  
   * **G2.2** and **G3.2** use `FALLBACK` because the robot has alternative methods; if the first fails (e.g., patient cannot fetch from tray), it automatically falls back to the next method.  

3. **Task Granularity**  
   * Tasks are kept fine‑grained (e.g., opening door, indicating meal) to allow clear assignment of robot capabilities and to reflect the actual robot actions described.  

4. **Number of Robots**  
   * Most tasks involve a single robot; cooperative tasks (`AT9`) explicitly require two robots. Human participation is acknowledged in the task description but not counted as a robot.  

5. **Query Goals**  
   * `G2.1` is a query goal because it only retrieves information from the patient record; no action is performed.  

6. **Perform Goals**  
   * All actions that the robot must execute are classified as Perform goals, with target conditions implicitly defined by the success of the corresponding tasks.  

7. **Achieve Goals**  
   * `G1`, `G2`, and `G3` are Achieve goals because they specify a desired world state (food delivered, dishes removed).  

8. **Leaf Goals**  
   * Goals with no children (e.g., `G2.2.1`, `G2.2.2.1`, etc.) are marked with `-` runtime annotation.  

This model faithfully captures the mission’s requirements, uncertainties, and the multi‑robot coordination needed to deliver food and clean rooms in a hospital setting.
