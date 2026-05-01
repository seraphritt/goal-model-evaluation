## 1. Goal Model – Detailed Tables  

| **Name** | **Text**                                                          | **Runtime**                         | **Goal Type** | **Target Condition / Enquired Info**                                                | **Relation**  | **Justification**                                                                                                                                                                                          | **Ground truth I**                                 | **Ground truth C** | **Consensus**                                      |
| -------- | ----------------------------------------------------------------- | ----------------------------------- | ------------- | ----------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------ | -------------------------------------------------- |
| **G1**   | Deliver food to the inpatient room                                | `FALLBACK(G3, G2)`                  | Achieve       | *Food is delivered to the room and the patient has received the meal*               | OR            | The system prefers tray-delivery (G3) because it allows the patient to retrieve the meal themselves. If tray-delivery fails (e.g., patient cannot retrieve), the system falls back to table-delivery (G2). | OK.                                                | OK                 | OK.                                                |
| **G2**   | Deliver food to the inpatient table                               | `;`                                 | Perform       | –                                                                                   | AND           | Navigation, manipulation and verification are all necessary and must occur in sequence.                                                                                                                    | OK                                                 | OK                 | OK                                                 |
| **G3**   | Deliver food to the patient’s tray                                | `;`                                 | Perform       | –                                                                                   | AND           | The tray-delivery path requires (i) knowing whether the patient can retrieve the food (G6), (ii) placing the tray (G7) and (iii) monitoring the retrieval (G8).                                            | OK                                                 | OK                 | OK                                                 |
| **G4**   | Retrieve dirty dishes from the room                               | `;`                                 | Perform       | –                                                                                   | AND           | Dish retrieval requires (i) identifying dishes and opening the door (G10), (ii) picking them up (G11) and (iii) transporting them to the kitchen (G12).                                                    | Achieve. Target condition: all food was retrieved. | OK                 | Achieve. Target condition: all food was retrieved. |
| **G6**   | Query whether the patient/companion can retrieve food from a tray | `-`                                 | Query         | *Whether the patient or an available companion can retrieve the food from the tray* | –             | The robot needs this information to decide whether tray-delivery is feasible.                                                                                                                              | OK                                                 | OK                 | OK                                                 |
| **G7**   | Place the tray at the patient and indicate the meal               | `;`                                 | Perform       | –                                                                                   | AND           | The robot must (i) navigate to the patient, (ii) place the tray, and (iii) inform the patient which meal is on the tray.                                                                                   | OK                                                 | OK                 | OK                                                 |
| **G8**   | Monitor the patient’s retrieval of the meal                       | `;`                                 | Perform       | –                                                                                   | AND           | The robot must (i) detect that the patient has taken a meal, (ii) verify that it is the correct meal, and (iii) alert staff if the wrong meal was taken.                                                   | OK                                                 | OK                 | OK                                                 |
| **G10**  | Identify dirty dishes and open the room door                      | `;`                                 | Perform       | –                                                                                   | AND           | The robot must (i) detect dirty dishes, (ii) open the door unassisted or with human help, before it can pick up the dishes.                                                                                | OK                                                 | OK                 | OK                                                 |
| **G11**  | Pick up the dishes                                                | `FALLBACK(G14, FALLBACK(G15, G16))` | Perform       | –                                                                                   | OR (fallback) | The robot first tries to pick up dishes alone (G14). If that fails (e.g., too many dishes), it tries two-robot cooperation (G15), and finally robot-human cooperation (G16).                               | OK                                                 | OK                 | OK                                                 |
| **G12**  | Transport the dishes to the kitchen                               | `-`                                 | Perform       | –                                                                                   | –             | A single task – the robot carries the dishes to the kitchen.                                                                                                                                               | OK                                                 | OK                 | OK                                                 |
| **G14**  | Pick up dishes unassisted                                         | `-`                                 | Perform       | –                                                                                   | –             | The robot alone can handle a small number of dishes.                                                                                                                                                       | OK                                                 | OK                 | OK                                                 |
| **G15**  | Pick up dishes with two robots                                    | `-`                                 | Perform       | –                                                                                   | –             | Two robots cooperate when the load is too heavy for one robot.                                                                                                                                             | OK                                                 | OK                 | OK                                                 |
| **G16**  | Pick up dishes with a human helper                                | `-`                                 | Perform       | –                                                                                   | –             | The robot assists a human when the patient or a staff member is present.                                                                                                                                   | OK                                                 | OK                 | OK                                                 |

---

## 2. Task Model – Detailed Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT6** | Navigate to the patient | AND | room | 1 | The robot must reach the patient’s location. |
| **AT7** | Place the tray at the patient | AND | room | 1 | The robot manipulates the tray onto the patient’s hand or table. |
| **AT8** | Indicate which meal the patient should retrieve | AND | room | 1 | The robot informs the patient of the correct meal. |
| **AT9** | Detect that the patient has taken a meal | AND | room | 1 | Sensor monitoring is needed to know when the patient has grabbed a meal. |
| **AT10** | Verify the retrieved meal matches the indicated meal | AND | room | 1 | The robot checks the meal ID to detect mistakes. |
| **AT11** | Alert staff if a wrong meal was retrieved | AND | room | 1 | Immediate notification is required to correct the error. |
| **AT13** | Navigate to the table | AND | room | 1 | The robot must reach the table to deliver the meal. |
| **AT14** | Manipulate the tray onto the table | AND | room | 1 | The robot places the tray onto the table. |
| **AT12** | Verify that the meal is on the table | AND | room | 1 | Confirmation that delivery succeeded. |
| **AT16** | Identify dirty dishes in the room | AND | room | 1 | Scanning is required to locate dishes. |
| **AT21** | Open the room door unassisted | AND | door | 1 | The robot can open the door if no human is present. |
| **AT22** | Open the room door with human assistance | AND | door | 1 | The robot can open the door if a human is available to help. |
| **AT17** | Pick up dishes unassisted | AND | room | 1 | The robot can handle a small load alone. |
| **AT18** | Pick up dishes with two robots | AND | room | [2,2] | Two robots cooperate for heavier loads. |
| **AT19** | Pick up dishes with a human helper | AND | room | 1 | Human assistance is used when the patient or staff is present. |
| **AT20** | Transport dishes to the kitchen | AND | room → kitchen | 1 | The robot carries dishes back to the kitchen for washing. |

---

## 3. Summary Table (All Goals & Tasks)

| **ID** | **Type** | **Title** | **Key Description** |
|--------|----------|-----------|---------------------|
| **G1** | Goal | Deliver food to inpatient room | Achieve successful delivery via tray or table |
| **G2** | Goal | Deliver food to table | Perform navigation, manipulation, verification |
| **G3** | Goal | Deliver food to tray | Query, place, monitor |
| **G4** | Goal | Retrieve dirty dishes | Identify, pick up, transport |
| **G6** | Goal | Query patient retrieval capability | Query information |
| **G7** | Goal | Place tray at patient | Navigate, place, indicate |
| **G8** | Goal | Monitor retrieval | Detect, verify, alert |
| **G10** | Goal | Identify dirty dishes & open door | Scan, open door |
| **G11** | Goal | Pick up dishes | Unassisted → two robots → human |
| **G12** | Goal | Transport dishes to kitchen | Single task |
| **G14** | Goal | Unassisted dish pickup | Single robot |
| **G15** | Goal | Two-robot dish pickup | Two robots cooperate |
| **G16** | Goal | Human-assisted dish pickup | Robot assists human |
| **AT6** | Task | Navigate to patient | Robot navigation |
| **AT7** | Task | Place tray at patient | Manipulation |
| **AT8** | Task | Indicate meal | Inform patient |
| **AT9** | Task | Detect meal retrieval | Sensor monitoring |
| **AT10** | Task | Verify meal correctness | ID check |
| **AT11** | Task | Alert wrong meal | Notification |
| **AT13** | Task | Navigate to table | Robot navigation |
| **AT14** | Task | Manipulate tray onto table | Placement |
| **AT12** | Task | Verify delivery | Confirmation |
| **AT16** | Task | Identify dirty dishes | Scanning |
| **AT21** | Task | Open door unassisted | Door operation |
| **AT22** | Task | Open door with human | Door operation |
| **AT17** | Task | Pick up dishes unassisted | Pickup |
| **AT18** | Task | Pick up dishes with two robots | Cooperative pickup |
| **AT19** | Task | Pick up dishes with human | Cooperative pickup |
| **AT20** | Task | Transport dishes to kitchen | Transport |

---

## 4. Logical Relationships (Parent → Children)

| **Parent** | **Children** | **Relation** | **Runtime** | **Justification** |
|------------|--------------|--------------|-------------|-------------------|
| **G1** | G3, G2 | OR (fallback) | `FALLBACK(G3, G2)` | Prefer tray delivery; fallback to table if tray fails. |
| **G3** | G6, G7, G8 | AND | `;` | All three steps are required for tray delivery. |
| **G6** | – | – | `-` | Leaf query. |
| **G7** | AT6, AT7, AT8 | AND | `;` | Navigation, placement, and indication must all happen. |
| **AT6** | – | – | `-` | Leaf task. |
| **AT7** | – | – | `-` | Leaf task. |
| **AT8** | – | – | `-` | Leaf task. |
| **G8** | AT9, AT10, AT11 | AND | `;` | Detection, verification, and alert are all needed. |
| **AT9** | – | – | `-` | Leaf task. |
| **AT10** | – | – | `-` | Leaf task. |
| **AT11** | – | – | `-` | Leaf task. |
| **G2** | AT13, AT14, AT12 | AND | `;` | Navigation, manipulation, verification. |
| **AT13** | – | – | `-` | Leaf task. |
| **AT14** | – | – | `-` | Leaf task. |
| **AT12** | – | – | `-` | Leaf task. |
| **G4** | G10, G11, G12 | AND | `;` | Identification, pickup, transport. |
| **G10** | AT16, AT21, AT22 | AND | `;` | Scan, open door unassisted, open door with human. |
| **AT16** | – | – | `-` | Leaf task. |
| **AT21** | – | – | `-` | Leaf task. |
| **AT22** | – | – | `-` | Leaf task. |
| **G11** | G14, G15, G16 | OR (fallback) | `FALLBACK(G14, FALLBACK(G15, G16))` | Try unassisted first, then two-robot, then human-assisted. |
| **G14** | – | – | `-` | Leaf task. |
| **G15** | – | – | `-` | Leaf task. |
| **G16** | – | – | `-` | Leaf task. |
| **G12** | AT20 | AND | `;` | Single transport task. |
| **AT20** | – | – | `-` | Leaf task. |

---

### Notes on Justifications

1. **Fallbacks** are used where the mission explicitly states a preference or contingency (tray‑delivery vs. table‑delivery; unassisted pickup vs. cooperative pickup).  
2. **AND decompositions** capture the fact that multiple sub‑tasks must all succeed for the parent goal to be satisfied (e.g., navigation + manipulation + verification).  
3. **Sequential runtime (`;`)** is applied when the order of actions matters (robot must navigate before manipulating).  
4. **Parallel runtime (`#`)** is not needed here because the mission does not describe independent concurrent sub‑tasks that can be executed in parallel.  
5. **Query goals** (G6) provide necessary information that influences subsequent decisions; they are leaf goals.  
6. **Perform goals** represent concrete actions that the robot must carry out; they are decomposed into tasks.  
7. **Achieve goal** (G1) sets the overall mission objective of successful food delivery.  

This goal model captures all major functional requirements of the multi‑robot system, respects the uncertainty in patient capabilities, and explicitly models cooperation scenarios (human‑robot, robot‑robot) as fallback alternatives.
