**Goal Table**
| **Name** | **Text**                                                                                                                                          | **Runtime**            | **Goal Type** | **Target Condition / Enquired Info**                                | **Relation**    | **Ground truth I**                                    | **Ground truth C** | **Consensus**                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------- | ------------------------------------------------------------------- | --------------- | ----------------------------------------------------- | ------------------ | ----------------------------------------------------- |
| **G1**   | Deliver food from the kitchen to an inpatient room, either by placing it on the table or by having the patient retrieve it from the robot’s tray. | `FALLBACK(G1.2, G1.1)` | Perform       | –                                                                   | –               | Ok                                                    | OK                 | Ok                                                    |
| **G1.1** | Deliver the meal directly onto the inpatient’s table.                                                                                             | `-`                    | Perform       | –                                                                   | OR (from G1)    | OK                                                    | OK                 | OK                                                    |
| **G1.2** | Deliver the meal onto the robot’s tray and coordinate with the patient to retrieve it.                                                            | `;`                    | Perform       | –                                                                   | OR (from G1)    | OK                                                    | OK                 | OK                                                    |
| **G5**   | Query whether the patient is able to retrieve the meal from the robot’s tray.                                                                     | `-`                    | Query         | “Patient retrieval capability”                                      | AND (from G1.2) | OK                                                    | OK                 | OK                                                    |
| **G3**   | Ensure that the meal retrieved by the patient corresponds to the correct inpatient and that no wrong meal is taken.                               | `;`                    | Achieve       | “All meals retrieved by correct inpatient; no wrong meal retrieved” | AND (from G1.2) | OK                                                    | OK                 | OK                                                    |
| **G2**   | Retrieve dirty dishes from the inpatient room.                                                                                                    | `;`                    | Perform       | –                                                                   | –               | Achieve. Target condition: all dishes were retrieved. | OK                 | Achieve. Target condition: all dishes were retrieved. |
| **G2.1** | Open the room door so that the robot can access the room.                                                                                         | `-`                    | Perform       | –                                                                   | AND (from G2)   | OK                                                    | OK                 | OK                                                    |
| **G2.2** | Retrieve the dirty dishes from the room.                                                                                                          | `-`                    | Perform       | –                                                                   | AND (from G2)   | OK                                                    | OK                 | OK                                                    |

---

**Task Table**

| Name | Text | Relation | Location | Number of Robots |
|------|------|----------|----------|------------------|
| **AT1** | Robot uses its manipulation skill to place the meal on the inpatient’s table. | AND (from G1.1) | Inpatient room | 1 |
| **AT2** | Robot places the meal onto its tray after kitchen preparation. | AND (from G3) | Kitchen | 1 |
| **AT3** | Robot communicates to the patient which meal they should retrieve. | AND (from G3) | Inpatient room | 1 |
| **AT4** | Robot tracks when and where each meal is retrieved and alerts if a wrong meal is taken. | AND (from G3) | Inpatient room | 1 |
| **AT5** | Robot picks up dirty dishes from the room without assistance. | OR (from G2.2) | Inpatient room | 1 |
| **AT6** | Two robots cooperate to gather dirty dishes from the room. | OR (from G2.2) | Inpatient room | 2 |
| **AT7** | Robot assists a human in gathering dirty dishes from the room. | OR (from G2.2) | Inpatient room | 1 |
| **AT8** | Robot opens the room door by itself. | OR (from G2.1) | Room door | 1 |
| **AT9** | Robot cooperates with a human to open the room door. | OR (from G2.1) | Room door | 1 |
| **AT10** | Two robots cooperate to open the room door. | OR (from G2.1) | Room door | 2 |

---

### Summary Table (Goals + Tasks)

| ID | Type | Title | Text | Runtime / Goal‑Type | Target / Enquired | Relation | Location | Robots |
|----|------|-------|------|---------------------|-------------------|----------|----------|--------|
| G1 | Goal | Deliver food to inpatient room | Deliver food from kitchen to an inpatient room, either on the table or via the tray. | `FALLBACK(G1.2, G1.1)` / Perform | – | – | – | – |
| G1.1 | Goal | Deliver to table | Place meal directly on the table. | `-` / Perform | – | OR | – | – |
| AT1 | Task | Deliver meal to table | Manipulate meal onto table. | – | – | AND | Inpatient room | 1 |
| G1.2 | Goal | Deliver to tray & patient retrieval | Place meal on tray and coordinate patient retrieval. | `;` / Perform | – | OR | – | – |
| G5 | Goal | Query patient retrieval | Check if patient can retrieve from tray. | `-` / Query | “Patient retrieval capability” | AND | – | – |
| G3 | Goal | Ensure correct meal retrieval | Confirm meal matches patient and no wrong meal is taken. | `;` / Achieve | “All meals retrieved by correct inpatient; no wrong meal retrieved” | AND | – | – |
| AT2 | Task | Place meal on tray | Place meal on robot tray. | – | – | AND | Kitchen | 1 |
| AT3 | Task | Indicate meal to patient | Communicate which meal to retrieve. | – | – | AND | Inpatient room | 1 |
| AT4 | Task | Monitor meal retrieval | Track retrieval and alert on wrong meal. | – | – | AND | Inpatient room | 1 |
| G2 | Goal | Retrieve dirty dishes | Gather dirty dishes from the room. | `;` / Perform | – | – | – | – |
| G2.1 | Goal | Open door | Open the room door for access. | `-` / Perform | – | AND | – | – |
| AT8 | Task | Open door robot‑only | Robot opens door by itself. | – | – | OR | Room door | 1 |
| AT9 | Task | Open door with human | Robot cooperates with human to open door. | – | – | OR | Room door | 1 |
| AT10 | Task | Open door with another robot | Two robots open door together. | – | – | OR | Room door | 2 |
| G2.2 | Goal | Retrieve dishes | Retrieve dishes from room. | `-` / Perform | – | AND | – | – |
| AT5 | Task | Retrieve dishes unassisted | Robot picks up dishes alone. | – | – | OR | Inpatient room | 1 |
| AT6 | Task | Retrieve dishes with two robots | Two robots gather dishes together. | – | – | OR | Inpatient room | 2 |
| AT7 | Task | Retrieve dishes with human | Robot assists human in gathering dishes. | – | – | OR | Inpatient room | 1 |

---

### Logical Relationships

- **G1 → G1.1, G1.2** [OR] `FALLBACK(G1.2, G1.1)`
- **G1.2 → G5, G3** [AND] `;`
- **G5 → (leaf)** [AND] `-`
- **G3 → AT2, AT3, AT4** [AND] `;`
- **G1.1 → AT1** [AND] `-`
- **G2 → G2.1, G2.2** [AND] `;`
- **G2.1 → AT8, AT9, AT10** [OR] `-`
- **G2.2 → AT5, AT6, AT7** [OR] `-`

This goal model captures the decision‑making (fallback between table delivery and tray‑based delivery), the necessary queries (patient retrieval capability), the coordination required for door opening and dish retrieval, and the monitoring needed to ensure correct meal handling. All tasks are annotated with location and the number of robots required.
