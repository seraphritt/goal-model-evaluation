**Goal Model – Multi‑Robot Food Delivery & Dish Retrieval**

---

## 1. Goal Tables  

| **Name** | **Text**                                | **Runtime**          | **Goal Type** | **Target Condition / Enquired Information**                                     | **Relation**     | **Justification**                                                                                                   | **Ground truth I**                                   | **Ground truth C** | **Ground truth E** |
| -------- | --------------------------------------- | -------------------- | ------------- | ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ------------------ |
| **G1**   | *All Food Delivery and Dish Management* | `#`                  | Achieve       | `All orders delivered, all dishes cleared, door closed, meal tracking correct.` | –                | Root goal – delivery, dish retrieval and door management can proceed in parallel.                                   | Perform.                                             | Perform                   |                    |
| **G2**   | *Deliver Food*                          | `;`                  | Achieve       | `Food successfully delivered to patient.`                                       | AND (G3, G4, G9) | Delivery has three sequential phases: transport, placement/fetch, and tracking.                                     | OK.                                                  | Perform                   |                    |
| **G3**   | *Transport Food*                        | `-`                  | Perform       | –                                                                               | AND (AT1)        | Simple navigation action.                                                                                           | OK                                                   | Ok                   |                    |
| **G4**   | *Deliver to Table or Fetch from Tray*   | `FALLBACK(G6, G5)`   | Perform       | –                                                                               | OR (G5, G6)      | System first tries to fetch from tray; if that fails (e.g., patient cannot fetch), it falls back to table delivery. | OK                                                   | Ok                   |                    |
| **G5**   | *Deliver to Table*                      | `-`                  | Perform       | –                                                                               | AND (AT2)        | Physical placement on the table.                                                                                    | OK                                                   | Ok                   |                    |
| **G6**   | *Fetch from Tray*                       | `;`                  | Perform       | –                                                                               | AND (G7, G8)     | Requires patient-capability check and coordination.                                                                 | OK                                                   | Ok                   |                    |
| **G7**   | *Query Patient Capability*              | `-`                  | Query         | `Can patient fetch from tray? Companion present? Nurse present?`                | AND (AT3)        | Must know whether the patient can fetch the tray.                                                                   | OK                                                   | Ok                   |                    |
| **G8**   | *Coordinate Retrieval*                  | `-`                  | Perform       | –                                                                               | AND (AT4)        | Robot must coordinate with the appropriate human/robot.                                                             | OK                                                   | Ok                   |                    |
| **G9**   | *Track Meal Retrieval*                  | `-`                  | Perform       | –                                                                               | AND (AT5, AT10)  | Record events and raise alerts if wrong meal is taken.                                                              | OK                                                   | Ok                   |                    |
| **G10**  | *Retrieve Dishes*                       | `FALLBACK(G12, G11)` | Perform       | –                                                                               | OR (G11, G12)    | Attempt unassisted retrieval first; if that fails, use cooperation.                                                 | Achieve. Target condition: all dishes were retrieved | Ok                   |                    |
| **G11**  | *Determine Retrieval Method*            | `-`                  | Query         | `Is dish retrieval unassisted, robot-cooperative, or human-assisted?`           | AND (AT6)        | Decision point for dish retrieval.                                                                                  | OK                                                   | Ok                   |                    |
| **G12**  | *Execute Dish Retrieval*                | `-`                  | Perform       | –                                                                               | AND (AT7)        | Physical act of picking up dishes.                                                                                  | OK                                                   | Ok                   |                    |
| **G13**  | *Manage Door Access*                    | `;`                  | Perform       | –                                                                               | AND (G14, G15)   | Door opening requires capability check then coordination.                                                           | OK                                                   | Ok                   |                    |
| **G14**  | *Check Door Opening Capability*         | `-`                  | Query         | `Can robot open door alone?`                                                    | AND (AT8)        | Determines if robot can act solo.                                                                                   | OK                                                   | Ok                   |                    |
| **G15**  | *Coordinate Door Opening*               | `-`                  | Perform       | –                                                                               | AND (AT9)        | If robot cannot open alone, it must coordinate.                                                                     | OK                                                   | Ok                   |                    |


---

## 2. Task Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** | *Navigate from Kitchen to Room* | AND (G3) | Hospital – kitchen to room | 1 | Single robot performs navigation. |
| **AT2** | *Place Food on Table* | AND (G5) | Inpatient room – table | 1 | Requires special manipulation skill. |
| **AT3** | *Query Patient Record* | AND (G7) | Hospital – patient record system | 1 | Robot accesses electronic record. |
| **AT4** | *Coordinate Retrieval* | AND (G8) | Inpatient room – patient/companion/nurse area | 1–2 | May involve a second robot for hand‑off. |
| **AT5** | *Record Meal Events* | AND (G9) | Hospital – system database | 1 | Logs delivery and retrieval timestamps. |
| **AT6** | *Determine Dish Retrieval Method* | AND (G11) | Inpatient room – door area | 1 | Decision logic based on room state. |
| **AT7** | *Retrieve Dishes* | AND (G12) | Inpatient room – table/closet | 1–2 | May need cooperation for heavy dishes. |
| **AT8** | *Assess Door Opening Capability* | AND (G14) | Room door | 1 | Robot checks mechanical capability. |
| **AT9** | *Coordinate Door Opening* | AND (G15) | Room door | 1–2 | Requires human or robot partner if needed. |
| **AT10** | *Alert Wrong Meal* | AND (G9) | Hospital – communication channel | 1 | Notifies staff if mismatch detected. |

---

## 3. Summary Table (Goals & Tasks)  

| **ID** | **Type** | **Title** | **Runtime / Relation** | **Justification** |
|--------|----------|-----------|------------------------|-------------------|
| G1 | Goal | All Food Delivery & Dish Management | `#` (parallel) | Root goal – delivery, dish clearance, and door access can happen concurrently. |
| G2 | Goal | Deliver Food | `;` (sequential) | Transport, placement/fetch, and tracking are sequential steps. |
| G3 | Goal | Transport Food | `-` | Simple navigation task. |
| G4 | Goal | Deliver to Table or Fetch from Tray | `FALLBACK(G6,G5)` | Prefer tray fetch; fallback to table if fetch fails. |
| G5 | Goal | Deliver to Table | `-` | Physical placement. |
| G6 | Goal | Fetch from Tray | `;` | Requires capability query + coordination. |
| G7 | Goal | Query Patient Capability | `-` | Must know if patient can fetch. |
| G8 | Goal | Coordinate Retrieval | `-` | Robot must coordinate with appropriate agent. |
| G9 | Goal | Track Meal Retrieval | `-` | Record events & alert wrong meal. |
| G10 | Goal | Retrieve Dishes | `FALLBACK(G12,G11)` | Attempt unassisted; fallback to cooperation. |
| G11 | Goal | Determine Retrieval Method | `-` | Decision point for dish retrieval. |
| G12 | Goal | Execute Dish Retrieval | `-` | Physical act of picking up dishes. |
| G13 | Goal | Manage Door Access | `;` | Door opening requires check + coordination. |
| G14 | Goal | Check Door Opening Capability | `-` | Robot must know if it can open door alone. |
| G15 | Goal | Coordinate Door Opening | `-` | If robot cannot open alone, coordinate with others. |
| AT1 | Task | Navigate from Kitchen to Room | AND (G3) | Robot navigation. |
| AT2 | Task | Place Food on Table | AND (G5) | Manipulation skill. |
| AT3 | Task | Query Patient Record | AND (G7) | Access patient data. |
| AT4 | Task | Coordinate Retrieval | AND (G8) | Human/robot coordination. |
| AT5 | Task | Record Meal Events | AND (G9) | Logging. |
| AT6 | Task | Determine Dish Retrieval Method | AND (G11) | Decision logic. |
| AT7 | Task | Retrieve Dishes | AND (G12) | Physical retrieval. |
| AT8 | Task | Assess Door Opening Capability | AND (G14) | Capability check. |
| AT9 | Task | Coordinate Door Opening | AND (G15) | Human/robot coordination. |
| AT10 | Task | Alert Wrong Meal | AND (G9) | Notification. |

---

## 4. Logical Relationships  

- **G1 → G2, G10, G13**  
  - **Relation:** `AND` (parallel)  
  - **Justification:** Root goal requires simultaneous completion of food delivery, dish retrieval, and door management.

- **G2 → G3, G4, G9**  
  - **Relation:** `AND` (sequential)  
  - **Justification:** Delivery consists of transporting food, delivering it, and tracking the process.

- **G3 → AT1**  
  - **Relation:** `AND`  
  - **Justification:** Transport goal is realized by navigation task.

- **G4 → G5, G6**  
  - **Relation:** `OR` (fallback)  
  - **Justification:** System first attempts tray fetch; if not possible, it falls back to table delivery.

- **G5 → AT2**  
  - **Relation:** `AND`  
  - **Justification:** Table delivery is performed by placing food on the table.

- **G6 → G7, G8**  
  - **Relation:** `AND` (sequential)  
  - **Justification:** Fetching requires checking patient capability and then coordinating retrieval.

- **G7 → AT3**  
  - **Relation:** `AND`  
  - **Justification:** Query task obtains necessary information.

- **G8 → AT4**  
  - **Relation:** `AND`  
  - **Justification:** Coordination task actualizes the goal.

- **G9 → AT5, AT10**  
  - **Relation:** `AND`  
  - **Justification:** Tracking involves recording events and alerting on wrong meals.

- **G10 → G11, G12**  
  - **Relation:** `OR` (fallback)  
  - **Justification:** Attempt unassisted retrieval first; if fails, use cooperation.

- **G11 → AT6**  
  - **Relation:** `AND`  
  - **Justification:** Decision task.

- **G12 → AT7**  
  - **Relation:** `AND`  
  - **Justification:** Physical dish retrieval.

- **G13 → G14, G15**  
  - **Relation:** `AND` (sequential)  
  - **Justification:** Door access requires capability check then coordination.

- **G14 → AT8**  
  - **Relation:** `AND`  
  - **Justification:** Capability check task.

- **G15 → AT9**  
  - **Relation:** `AND`  
  - **Justification:** Coordination task.

---

### 5. Remarks on Uncertainty & Fallbacks  

* **Patient Capability Uncertainty** – Captured by **G7 (Query Patient Capability)**. If the patient cannot fetch the tray, the fallback in **G4** routes to table delivery.  
* **Dish Retrieval Uncertainty** – Captured by **G11 (Determine Retrieval Method)**. If unassisted retrieval fails, **G10** falls back to cooperative retrieval.  
* **Door Opening Uncertainty** – Captured by **G14 (Check Door Opening Capability)**. If the robot cannot open the door alone, **G15** coordinates with a human or another robot.  

All fallback mechanisms are expressed using the **FALLBACK** runtime annotation, reflecting the mission’s need to gracefully handle failure or lack of cooperation.  

---
