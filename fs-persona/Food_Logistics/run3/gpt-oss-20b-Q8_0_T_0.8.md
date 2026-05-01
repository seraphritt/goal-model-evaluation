**Goal Tables**

| Name                               | Text                                                                                                                    | Runtime                              | Goal Type | Target Condition / Enquired Information                              | Relation | Ground truth I                                        | Ground truth C | Consensus                                             |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | --------- | -------------------------------------------------------------------- | -------- | ----------------------------------------------------- | -------------- | ----------------------------------------------------- |
| **G1: Deliver Food to Patient**    | Deliver food from the kitchen to an inpatient room and ensure the correct meal is retrieved and all dishes are cleared. | `;`                                  | Achieve   | *Food delivered to patient, correct meal retrieved, dishes cleared.* | AND      | Perform.                                              | Perform        | Perform.                                              |
| **G2: Execute Delivery**           | Execute the delivery of food to the patient.                                                                            | `;`                                  | Perform   | –                                                                    | AND      | Achieve. Target condition: all food was delivered     | Ok             | Achieve. Target condition: all food was delivered     |
| **G2.3: Query Retrieval Ability**  | Query the patient record for retrieval capability and companion presence.                                               | `-`                                  | Query     | *Patient retrieval capability, companion presence.*                  | AND      | OK                                                    | Ok             | OK                                                    |
| **G2.4: Choose Delivery Method**   | Choose between direct delivery or tray hand-over based on the query result.                                             | `FALLBACK(G2.1,G2.2)`                | Perform   | –                                                                    | OR       | OK                                                    | Ok             | OK                                                    |
| **G2.1: Direct Delivery**          | Deliver the food directly into the patient’s room table.                                                                | `-`                                  | Perform   | –                                                                    | AND      | OK                                                    | Ok             | OK                                                    |
| **G2.2: Tray Handover**            | Hand over the food to the patient via the robot’s tray.                                                                 | `-`                                  | Perform   | –                                                                    | AND      | OK                                                    | Ok             | OK                                                    |
| **G3: Retrieve Dishes**            | Retrieve dirty dishes from the patient’s room.                                                                          | `FALLBACK(FALLBACK(G3.1,G3.2),G3.3)` | Perform   | –                                                                    | OR       | Achieve. Target condition: all dishes were retrieved. | Ok             | Achieve. Target condition: all dishes were retrieved. |
| **G3.1: Unassisted Retrieval**     | Retrieve dishes unassisted by the robot.                                                                                | `-`                                  | Perform   | –                                                                    | AND      | OK                                                    | Ok             | OK                                                    |
| **G3.2: Cooperative Retrieval**    | Retrieve dishes with cooperation of two robots.                                                                         | `-`                                  | Perform   | –                                                                    | AND      | OK                                                    | Ok             | OK                                                    |
| **G3.3: Human-Assisted Retrieval** | Retrieve dishes with assistance from a human.                                                                           | `-`                                  | Perform   | –                                                                    | AND      | OK                                                    | Ok             | OK                                                    |


---

**Task Tables**

| Name | Text | Relation | Location | Number of Robots |
|------|------|----------|----------|------------------|
| **AT1: Query Retrieval Context** | Query patient record for retrieval capability and companion presence. | AND | Hospital Database | 1 |
| **AT2: Move to Kitchen** | Navigate robot to kitchen. | AND | Kitchen | 1 |
| **AT3: Pick Up Meals** | Robot picks up meals from kitchen. | AND | Kitchen | 1 |
| **AT4: Carry to Room** | Robot carries meals to patient room. | AND | Patient Room | 1 |
| **AT5: Open Room Door** | Robot opens room door. | AND | Patient Room Door | 1 |
| **AT6: Deliver to Table** | Robot delivers meals into patient room table. | AND | Patient Room Table | 1 |
| **AT7: Confirm Delivery** | Robot confirms delivery to patient. | AND | Patient Room | 1 |
| **AT8: Move to Kitchen (Tray)** | Robot moves to kitchen. | AND | Kitchen | 1 |
| **AT9: Pick Up Meals (Tray)** | Robot picks up meals from kitchen. | AND | Kitchen | 1 |
| **AT10: Carry to Room (Tray)** | Robot carries meals to patient room. | AND | Patient Room | 1 |
| **AT11: Open Room Door (Tray)** | Robot opens room door. | AND | Patient Room Door | 1 |
| **AT12: Hand Over Tray** | Robot hands over tray to patient. | AND | Patient Room | 1 |
| **AT13: Signal Meal Number** | Robot signals which meal to retrieve to patient. | AND | Patient Room | 1 |
| **AT14: Track Retrieval** | Robot tracks when and where each meal is retrieved. | AND | Patient Room | 1 |
| **AT15: Alert Wrong Meal** | Robot alerts if wrong meal is retrieved. | AND | Patient Room | 1 |
| **AT16: Open Door for Dishes** | Robot opens door for dish retrieval. | AND | Patient Room Door | 1 |
| **AT17: Retrieve Dishes** | Robot retrieves dirty dishes unassisted. | AND | Patient Room | 1 |
| **AT18: Open Door with Two Robots** | Two robots open door cooperatively. | AND | Patient Room Door | [2,2] |
| **AT19: Retrieve Dishes with Two Robots** | Two robots retrieve dishes together. | AND | Patient Room | [2,2] |
| **AT20: Open Door with Human** | Robot opens door with human assistance. | AND | Patient Room Door | 1 |
| **AT21: Retrieve Dishes with Human** | Robot retrieves dishes with human assistance. | AND | Patient Room | 1 |

---

**Summary Table (Goals & Tasks)**

| ID | Type | Title | Relation |
|----|------|-------|----------|
| **G1** | Goal | Deliver Food to Patient | AND |
| **G2** | Goal | Execute Delivery | AND |
| **G2.3** | Goal | Query Retrieval Ability | AND |
| **G2.4** | Goal | Choose Delivery Method | OR |
| **G2.1** | Goal | Direct Delivery | AND |
| **G2.2** | Goal | Tray Handover | AND |
| **G3** | Goal | Retrieve Dishes | OR |
| **G3.1** | Goal | Unassisted Retrieval | AND |
| **G3.2** | Goal | Cooperative Retrieval | AND |
| **G3.3** | Goal | Human‑Assisted Retrieval | AND |
| **AT1** | Task | Query Retrieval Context | AND |
| **AT2** | Task | Move to Kitchen | AND |
| **AT3** | Task | Pick Up Meals | AND |
| **AT4** | Task | Carry to Room | AND |
| **AT5** | Task | Open Room Door | AND |
| **AT6** | Task | Deliver to Table | AND |
| **AT7** | Task | Confirm Delivery | AND |
| **AT8** | Task | Move to Kitchen (Tray) | AND |
| **AT9** | Task | Pick Up Meals (Tray) | AND |
| **AT10** | Task | Carry to Room (Tray) | AND |
| **AT11** | Task | Open Room Door (Tray) | AND |
| **AT12** | Task | Hand Over Tray | AND |
| **AT13** | Task | Signal Meal Number | AND |
| **AT14** | Task | Track Retrieval | AND |
| **AT15** | Task | Alert Wrong Meal | AND |
| **AT16** | Task | Open Door for Dishes | AND |
| **AT17** | Task | Retrieve Dishes | AND |
| **AT18** | Task | Open Door with Two Robots | AND |
| **AT19** | Task | Retrieve Dishes with Two Robots | AND |
| **AT20** | Task | Open Door with Human | AND |
| **AT21** | Task | Retrieve Dishes with Human | AND |

---

**Logical Relationships**

- **G1 → G2, G3** [AND][;]  
- **G2 → G2.3, G2.4** [AND][;]  
- **G2.4 → G2.1, G2.2** [OR][FALLBACK(G2.1,G2.2)]  
- **G2.3 → AT1** [AND]  
- **G2.1 → AT2, AT3, AT4, AT5, AT6, AT7** [AND]  
- **G2.2 → AT8, AT9, AT10, AT11, AT12, AT13, AT14, AT15** [AND]  
- **G3 → G3.1, G3.2, G3.3** [OR][FALLBACK(FALLBACK(G3.1,G3.2),G3.3)]  
- **G3.1 → AT16, AT17** [AND]  
- **G3.2 → AT18, AT19** [AND]  
- **G3.3 → AT20, AT21** [AND]
