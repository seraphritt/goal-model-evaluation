**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

Below is a complete goal model that decomposes the mission description into a hierarchical tree of goals and tasks.  
All goals are numbered in depth‑first order (G1, G1.1, G1.2, …).  
All tasks are numbered in depth‑first order (AT1, AT2, …).  
The tables contain the required columns, runtime annotations, goal types, relations, and justifications.

---

## 1. Goal Table

| Name         | Text                               | Runtime                                                             | Goal Type | Enquired Information / Target Condition                                                  | Relation | Justification                                                                                                                                                                      | Ground truth I                                        | Ground truth C | Consensus                                             |
| ------------ | ---------------------------------- | ------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------- | ----------------------------------------------------- |
| **G1**       | Deliver food to inpatient room     | `;`                                                                 | Perform   | –                                                                                        | AND      | All sub-steps (collect, query, decide, deliver, dish-cleanup, door-open, call-wait, indicate, check, track, alert) must happen in sequence before the overall mission is finished. | OK                                                    | Ok             | OK                                                    |
| **G1.1**     | Collect meals                      | `-`                                                                 | Perform   | –                                                                                        | –        | Robot must pick up meals before any delivery can occur.                                                                                                                            | Achieve. Target condition: all meals were collected   | Ok             | Achieve. Target condition: all meals were collected   |
| **G1.2**     | Query patient retrieval capability | `-`                                                                 | Query     | patient retrieval capability (patient ability, presence of companion, presence of nurse) | –        | Needed to decide whether the patient can fetch the meal from the robot’s tray.                                                                                                     | OK                                                    | Ok             | OK                                                    |
| **G1.3**     | Decide delivery method             | `FALLBACK(G1.3.1,G1.3.2)`                                           | Perform   | –                                                                                        | OR       | If the patient can retrieve the meal, the robot will deliver to the tray; otherwise it delivers to the table.                                                                      | OK                                                    | Ok             | OK                                                    |
| **G1.3.1**   | Deliver to table                   | `-`                                                                 | Perform   | –                                                                                        | –        | Robot can place the meal directly on the patient’s table using its manipulation skill.                                                                                             | OK                                                    | Ok             | OK                                                    |
| **G1.3.2**   | Deliver to tray                    | `FALLBACK(FALLBACK(FALLBACK(G1.3.2.1,G1.3.2.2),G1.3.2.3),G1.3.2.4)` | Perform   | –                                                                                        | OR       | The tray delivery requires cooperation with one of the following agents: patient, companion, nurse, or another robot.                                                              | OK                                                    | Ok             | OK                                                    |
| **G1.3.2.1** | Cooperate with patient             | `-`                                                                 | Perform   | –                                                                                        | –        | Patient can fetch the meal directly from the robot’s tray.                                                                                                                         | OK                                                    | Ok             | OK                                                    |
| **G1.3.2.2** | Cooperate with companion           | `-`                                                                 | Perform   | –                                                                                        | –        | Companion can fetch the meal from the robot’s tray.                                                                                                                                | OK                                                    | Ok             | OK                                                    |
| **G1.3.2.3** | Cooperate with nurse               | `-`                                                                 | Perform   | –                                                                                        | –        | Nurse can fetch the meal from the robot’s tray.                                                                                                                                    | OK                                                    | Ok             | OK                                                    |
| **G1.3.2.4** | Cooperate with robot               | `-`                                                                 | Perform   | –                                                                                        | –        | Another robot can transfer the meal to the patient.                                                                                                                                | OK                                                    | Ok             | OK                                                    |
| **G1.4**     | Retrieve dirty dishes              | `FALLBACK(FALLBACK(G1.4.1,G1.4.2),G1.4.3)`                          | Perform   | –                                                                                        | OR       | Dish retrieval can be unassisted, with two robots, or with a human.                                                                                                                | Achieve. Target condition: all dishes were retrieved. | Ok             | Achieve. Target condition: all dishes were retrieved. |
| **G1.4.1**   | Retrieve dishes unassisted         | `-`                                                                 | Perform   | –                                                                                        | –        | Robot can pick up dishes by itself.                                                                                                                                                | OK                                                    | Ok             | OK                                                    |
| **G1.4.2**   | Retrieve dishes with two robots    | `-`                                                                 | Perform   | –                                                                                        | –        | Two robots coordinate to lift heavier loads.                                                                                                                                       | Ok                                                    | Ok             | Ok                                                    |
| **G1.4.3**   | Retrieve dishes with human         | `-`                                                                 | Perform   | –                                                                                        | –        | A human can pick up dishes on the robot’s request.                                                                                                                                 | OK                                                    | Ok             | OK                                                    |
| **G1.5**     | Open room door                     | `FALLBACK(FALLBACK(G1.5.1,G1.5.2),G1.5.3)`                          | Perform   | –                                                                                        | OR       | Door opening can be unassisted, with a robot, or with a human.                                                                                                                     | OK                                                    | Ok             | OK                                                    |
| **G1.5.1**   | Open door unassisted               | `-`                                                                 | Perform   | –                                                                                        | –        | Robot can push the door by itself.                                                                                                                                                 | OK                                                    | Ok             | OK                                                    |
| **G1.5.2**   | Open door with robot               | `-`                                                                 | Perform   | –                                                                                        | –        | A robot can push the door for another robot.                                                                                                                                       | OK                                                    | Ok             | OK                                                    |
| **G1.5.3**   | Open door with human               | `-`                                                                 | Perform   | –                                                                                        | –        | Human can open the door when the robot arrives.                                                                                                                                    | OK                                                    | Ok             | OK                                                    |
| **G1.6**     | Wait for call                      | `-`                                                                 | Perform   | –                                                                                        | –        | Robot must listen for a patient’s call to pick up dishes.                                                                                                                          | OK                                                    | Ok             | OK                                                    |
| **G1.7**     | Indicate meal to patient           | `-`                                                                 | Perform   | –                                                                                        | –        | Robot announces which meal the patient should retrieve.                                                                                                                            | OK                                                    | Ok             | OK                                                    |
| **G1.8**     | Check meal correctness             | `-`                                                                 | Perform   | –                                                                                        | –        | Robot verifies that the retrieved meal matches the order.                                                                                                                          | OK                                                    | Ok             | OK                                                    |
| **G1.9**     | Track meal retrieval               | `-`                                                                 | Perform   | –                                                                                        | –        | Robot logs when and where each meal was retrieved.                                                                                                                                 | OK                                                    | Ok             | OK                                                    |
| **G1.10**    | Alert wrong meal                   | `-`                                                                 | Perform   | –                                                                                        | –        | Robot sends an alert if the patient retrieves the wrong meal.                                                                                                                      | OK                                                    | Ok             | OK                                                    |


---

## 2. Task Table

| Name | Text | Relation | Location | Number of Robots | Justification |
|------|------|----------|----------|------------------|---------------|
| **AT1** | Move to kitchen | AND | kitchen | 1 | Robot must be in the kitchen to pick up meals. |
| **AT2** | Pick up meals | AND | kitchen | 1 | Robot must physically grab meals before delivery. |
| **AT3** | Move to room | AND | patient room | 1 | Robot needs to reach the patient’s room. |
| **AT4** | Place meal on table | AND | patient room | 1 | Requires the robot’s manipulation skill. |
| **AT5** | Wait for patient | AND | patient room | 1 | Patient must be present to receive the meal. |
| **AT6** | Hand over meal | AND | patient room | 1 | Robot hands the tray to the patient. |
| **AT7** | Wait for companion | AND | patient room | 1 | Companion must be present to receive the meal. |
| **AT8** | Hand over meal | AND | patient room | 1 | Companion receives the tray. |
| **AT9** | Wait for nurse | AND | patient room | 1 | Nurse must be present to receive the meal. |
| **AT10** | Hand over meal | AND | patient room | 1 | Nurse receives the tray. |
| **AT11** | Robot A passes meal to Robot B | AND | patient room | 2 | Two robots coordinate to transfer the meal. |
| **AT12** | Robot B delivers to patient | AND | patient room | 1 | Robot B hands the meal to the patient. |
| **AT13** | Move to room | AND | patient room | 1 | Robot must reach the room to pick up dishes. |
| **AT14** | Pick up dishes | AND | patient room | 1 | Robot lifts dishes. |
| **AT15** | Robot A and Robot B coordinate | AND | patient room | 2 | Two robots lift heavier dishes together. |
| **AT16** | Pick up dishes | AND | patient room | 2 | Both robots share the load. |
| **AT17** | Wait for human | AND | patient room | 1 | Human must be present to pick up dishes. |
| **AT18** | Human picks up dishes | AND | patient room | 1 | Human removes dishes on robot’s request. |
| **AT19** | Push door | AND | door | 1 | Robot can push the door by itself. |
| **AT20** | Robot pushes door | AND | door | 1 | Robot pushes the door for another robot. |
| **AT21** | Human opens door | AND | door | 1 | Human opens the door when the robot arrives. |
| **AT22** | Listen for call | AND | patient room | 1 | Robot must detect a patient’s call. |
| **AT23** | Respond to call | AND | patient room | 1 | Robot acknowledges the call. |
| **AT24** | Announce meal number | AND | patient room | 1 | Robot informs the patient which meal to retrieve. |
| **AT25** | Verify meal | AND | patient room | 1 | Robot checks that the retrieved meal matches the order. |
| **AT26** | Confirm with patient | AND | patient room | 1 | Patient confirms the meal. |
| **AT27** | Monitor patient retrieval | AND | patient room | 1 | Robot observes the patient’s action. |
| **AT28** | Log retrieval time and location | AND | patient room | 1 | Robot records when and where the meal was taken. |
| **AT29** | Compare retrieved meal with expected | AND | patient room | 1 | Robot checks for mismatch. |
| **AT30** | Send alert | AND | patient room | 1 | Robot notifies staff if the wrong meal is taken. |

---

## 3. Summary Table (Goals & Tasks)

| ID | Type | Text | Runtime / Relation | Location / Robots | Justification |
|----|------|------|--------------------|-------------------|---------------|
| **G1** | Goal | Deliver food to inpatient room | `;` (AND) | – | All sub‑steps must occur in sequence. |
| **G1.1** | Goal | Collect meals | `-` | – | Robot must pick up meals first. |
| **AT1** | Task | Move to kitchen | AND | kitchen, 1 | Robot must be in kitchen. |
| **AT2** | Task | Pick up meals | AND | kitchen, 1 | Robot grabs meals. |
| **G1.2** | Goal | Query patient retrieval capability | `-` | – | Needed to decide delivery method. |
| **G1.3** | Goal | Decide delivery method | `FALLBACK(G1.3.1,G1.3.2)` (OR) | – | Choose between table or tray delivery. |
| **G1.3.1** | Goal | Deliver to table | `-` | – | Robot can place meal directly. |
| **AT3** | Task | Move to room | AND | patient room, 1 | Robot must reach room. |
| **AT4** | Task | Place meal on table | AND | patient room, 1 | Requires manipulation skill. |
| **G1.3.2** | Goal | Deliver to tray | `FALLBACK(FALLBACK(FALLBACK(G1.3.2.1,G1.3.2.2),G1.3.2.3),G1.3.2.4)` (OR) | – | Requires cooperation. |
| **G1.3.2.1** | Goal | Cooperate with patient | `-` | – | Patient can fetch meal. |
| **AT5** | Task | Wait for patient | AND | patient room, 1 | Patient must be present. |
| **AT6** | Task | Hand over meal | AND | patient room, 1 | Transfer to patient. |
| **G1.3.2.2** | Goal | Cooperate with companion | `-` | – | Companion can fetch meal. |
| **AT7** | Task | Wait for companion | AND | patient room, 1 | Companion must be present. |
| **AT8** | Task | Hand over meal | AND | patient room, 1 | Transfer to companion. |
| **G1.3.2.3** | Goal | Cooperate with nurse | `-` | – | Nurse can fetch meal. |
| **AT9** | Task | Wait for nurse | AND | patient room, 1 | Nurse must be present. |
| **AT10** | Task | Hand over meal | AND | patient room, 1 | Transfer to nurse. |
| **G1.3.2.4** | Goal | Cooperate with robot | `-` | – | Another robot can transfer meal. |
| **AT11** | Task | Robot A passes meal to Robot B | AND | patient room, 2 | Two robots coordinate. |
| **AT12** | Task | Robot B delivers to patient | AND | patient room, 1 | Final hand‑over. |
| **G1.4** | Goal | Retrieve dirty dishes | `FALLBACK(FALLBACK(G1.4.1,G1.4.2),G1.4.3)` (OR) | – | Three possible retrieval modes. |
| **G1.4.1** | Goal | Retrieve dishes unassisted | `-` | – | Robot can lift dishes alone. |
| **AT13** | Task | Move to room | AND | patient room, 1 | Robot must reach room. |
| **AT14** | Task | Pick up dishes | AND | patient room, 1 | Robot lifts dishes. |
| **G1.4.2** | Goal | Retrieve dishes with two robots | `-` | – | Two robots share load. |
| **AT15** | Task | Robot A and Robot B coordinate | AND | patient room, 2 | Coordination needed. |
| **AT16** | Task | Pick up dishes | AND | patient room, 2 | Both lift together. |
| **G1.4.3** | Goal | Retrieve dishes with human | `-` | – | Human assists. |
| **AT17** | Task | Wait for human | AND | patient room, 1 | Human must be present. |
| **AT18** | Task | Human picks up dishes | AND | patient room, 1 | Human removes dishes. |
| **G1.5** | Goal | Open room door | `FALLBACK(FALLBACK(G1.5.1,G1.5.2),G1.5.3)` (OR) | – | Three possible opening modes. |
| **G1.5.1** | Goal | Open door unassisted | `-` | – | Robot can push door alone. |
| **AT19** | Task | Push door | AND | door, 1 | Robot pushes. |
| **G1.5.2** | Goal | Open door with robot | `-` | – | Robot pushes for another robot. |
| **AT20** | Task | Robot pushes door | AND | door, 1 | Robot pushes. |
| **G1.5.3** | Goal | Open door with human | `-` | – | Human opens door. |
| **AT21** | Task | Human opens door | AND | door, 1 | Human action. |
| **G1.6** | Goal | Wait for call | `-` | – | Robot listens for patient call. |
| **AT22** | Task | Listen for call | AND | patient room, 1 | Detection. |
| **AT23** | Task | Respond to call | AND | patient room, 1 | Acknowledgement. |
| **G1.7** | Goal | Indicate meal to patient | `-` | – | Robot announces meal number. |
| **AT24** | Task | Announce meal number | AND | patient room, 1 | Communication. |
| **G1.8** | Goal | Check meal correctness | `-` | – | Robot verifies meal. |
| **AT25** | Task | Verify meal | AND | patient room, 1 | Check. |
| **AT26** | Task | Confirm with patient | AND | patient room, 1 | Confirmation. |
| **G1.9** | Goal | Track meal retrieval | `-` | – | Robot logs retrieval. |
| **AT27** | Task | Monitor patient retrieval | AND | patient room, 1 | Observation. |
| **AT28** | Task | Log retrieval time and location | AND | patient room, 1 | Logging. |
| **G1.10** | Goal | Alert wrong meal | `-` | – | Robot alerts if mismatch. |
| **AT29** | Task | Compare retrieved meal with expected | AND | patient room, 1 | Check. |
| **AT30** | Task | Send alert | AND | patient room, 1 | Notification. |

---

## 4. Logical Relationships

| Relation | Description | Justification |
|----------|-------------|---------------|
| **G1 → G1.1, G1.2, G1.3, G1.4, G1.5, G1.6, G1.7, G1.8, G1.9, G1.10**<br>**[AND][;]** | All sub‑goals must be executed in order before the overall mission is complete. | The mission requires meal collection, capability query, delivery decision, dish retrieval, door opening, call waiting, meal indication, correctness check, tracking, and alerting. |
| **G1.3 → G1.3.1, G1.3.2**<br>**[OR][FALLBACK(G1.3.1,G1.3.2)]** | Choose between table delivery or tray delivery. | If the patient can retrieve from the tray, tray delivery is preferred; otherwise table delivery is used. |
| **G1.3.2 → G1.3.2.1, G1.3.2.2, G1.3.2.3, G1.3.2.4**<br>**[OR][FALLBACK(FALLBACK(FALLBACK(G1.3.2.1,G1.3.2.2),G1.3.2.3),G1.3.2.4)]** | Any of the four agents can cooperate to transfer the meal. | The mission allows patient, companion, nurse, or robot to fetch the meal; the first available agent is used. |
| **G1.4 → G1.4.1, G1.4.2, G1.4.3**<br>**[OR][FALLBACK(FALLBACK(G1.4.1,G1.4.2),G1.4.3)]** | Dish retrieval can be unassisted, with two robots, or with a human. | The robot chooses the most feasible retrieval method based on context. |
| **G1.5 → G1.5.1, G1.5.2, G1.5.3**<br>**[OR][FALLBACK(FALLBACK(G1.5.1,G1.5.2),G1.5.3)]** | Door opening can be unassisted, with a robot, or with a human. | The robot selects the appropriate opening method depending on availability. |
| **Each goal → its tasks**<br>**[AND][#]** | All tasks under a goal must be performed. | The robot must complete all operational steps to satisfy the goal. |

---

### Final Remarks

- **Parallel vs. Sequential**: Most sub‑goals are executed sequentially (`;`) because the mission has a clear order (collect → query → decide → deliver → cleanup).  
- **Fallback**: Used wherever the mission allows alternative agents or methods; the robot will try the first alternative and fall back to the next if the first fails.  
- **OR/AND**: OR is used for alternative methods; AND is used when all child tasks must be satisfied for the parent goal.  
- **Justifications**: Every relation and runtime annotation is explicitly justified based on the mission description, ensuring that the goal model faithfully represents the operational constraints and uncertainties.
