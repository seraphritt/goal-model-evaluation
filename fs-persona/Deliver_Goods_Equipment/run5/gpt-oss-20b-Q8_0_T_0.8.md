**Goal Model – Multi‑Robot Resource Delivery Mission**  

---

### 1. Goals

| **Name**                         | **Text**                                                                                | **Runtime**      | **Goal Type** | **Target Condition / Enquired Info**                                                | **Relation**             | **Ground truth I**                                       | **Ground truth C** | **Ground truth E** |
| -------------------------------- | --------------------------------------------------------------------------------------- | ---------------- | ------------- | ----------------------------------------------------------------------------------- | ------------------------ | -------------------------------------------------------- | ------------------ | ------------------ |
| **G1: Complete Mission**         | Ensure all requested resources are delivered to the specified location(s) successfully. | `;` (sequential) | Achieve       | “All requested resources delivered to destination and mission marked as completed.” | AND – G2, G3             | Perform.                                                 |  Perform                  |                    |
| **G2: Collect Resources**        | Gather all required resources from their respective storage locations.                  | `#` (parallel)   | Perform       | –                                                                                   | OR – G2.1, G2.2          | Achieve. Target condition: all resources were collected  |  Ok                  |                    |
| **G2.1: Normal Collection**      | Collect resources under normal battery conditions.                                      | `;` (sequential) | Perform       | –                                                                                   | AND – AT1, AT2, AT3      | OK                                                       |  Ok                  |                    |
| **G2.2: Battery Low Collection** | Handle collection when battery is low.                                                  | `;` (sequential) | Perform       | –                                                                                   | AND – G4                 | OK                                                       |  Ok                  |                    |
| **G3: Deliver Resources**        | Transport collected resources to the specified delivery location.                       | `#` (parallel)   | Perform       | –                                                                                   | OR – G3.1, G3.2          | Achieve. Target condition: all resources were delivered. |  Ok                  |                    |
| **G3.1: Normal Delivery**        | Deliver resources under normal battery conditions.                                      | `;` (sequential) | Perform       | –                                                                                   | AND – AT4                | OK                                                       |  Ok                  |                    |
| **G3.2: Battery Low Delivery**   | Handle delivery when battery is low.                                                    | `;` (sequential) | Perform       | –                                                                                   | AND – G4                 | OK                                                       |  Ok                  |                    |
| **G4: Handle Battery Low**       | Manage low-battery scenarios during collection or delivery.                             | `;` (sequential) | Perform       | –                                                                                   | AND – AT5, AT6, AT7, AT8 | OK                                                       |  Ok                  |                    |


---

### 2. Tasks

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1: Navigate to Storage** | Robot moves to the storage location containing the requested resources. | AND (child of G2.1) | Storage | [1, n] |
| **AT2: Request Resource** | Robot sends a request message to the storage specifying the required resources. | AND (child of G2.1) | Storage | [1, n] |
| **AT3: Wait for Retrieval** | Robot waits until the resources are retrieved from the storage. | AND (child of G2.1) | Storage | [1, n] |
| **AT4: Deliver Resource** | Robot transports the retrieved resources to the specified delivery location. | AND (child of G3.1) | Delivery Location | [1, n] |
| **AT5: Return to Recharging Station** | Robot returns to the recharging station due to low battery in collection phase. | AND (child of G4) | Recharging Station | [1, n] |
| **AT6: Return to Checkpoint** | Robot returns the resource to a checkpoint due to low battery in delivery phase. | AND (child of G4) | Checkpoint | [1, n] |
| **AT7: Assign Mission to Another Robot** | Robot assigns the remaining task to another robot after returning to recharging or checkpoint. | AND (child of G4) | Current location | [1, n] |
| **AT8: Trigger Alert and Report** | If failure to return resource to checkpoint, trigger alert and send report to sector manager. | AND (child of G4) | Current location | [1, n] |

---

### 3. Summary Table (All Goals & Tasks)

| **ID** | **Title** | **Type** | **Runtime** | **Relation** | **Location / Condition** |
|--------|-----------|----------|-------------|--------------|--------------------------|
| G1 | Complete Mission | Achieve | `;` | AND – G2, G3 | – |
| G2 | Collect Resources | Perform | `#` | OR – G2.1, G2.2 | – |
| G2.1 | Normal Collection | Perform | `;` | AND – AT1, AT2, AT3 | – |
| G2.2 | Battery Low Collection | Perform | `;` | AND – G4 | – |
| G3 | Deliver Resources | Perform | `#` | OR – G3.1, G3.2 | – |
| G3.1 | Normal Delivery | Perform | `;` | AND – AT4 | – |
| G3.2 | Battery Low Delivery | Perform | `;` | AND – G4 | – |
| G4 | Handle Battery Low | Perform | `;` | AND – AT5, AT6, AT7, AT8 | – |
| AT1 | Navigate to Storage | Task | – | AND – G2.1 | Storage |
| AT2 | Request Resource | Task | – | AND – G2.1 | Storage |
| AT3 | Wait for Retrieval | Task | – | AND – G2.1 | Storage |
| AT4 | Deliver Resource | Task | – | AND – G3.1 | Delivery Location |
| AT5 | Return to Recharging Station | Task | – | AND – G4 | Recharging Station |
| AT6 | Return to Checkpoint | Task | – | AND – G4 | Checkpoint |
| AT7 | Assign Mission to Another Robot | Task | – | AND – G4 | Current location |
| AT8 | Trigger Alert and Report | Task | – | AND – G4 | Current location |

---

### 4. Logical Relationships

```
G1 -> G2, G3 [AND][;]
G2 -> G2.1, G2.2 [OR][#]
G2.1 -> AT1, AT2, AT3 [AND][;]
G2.2 -> G4 [AND][;]
G3 -> G3.1, G3.2 [OR][#]
G3.1 -> AT4 [AND][;]
G3.2 -> G4 [AND][;]
G4 -> AT5, AT6, AT7, AT8 [AND][;]
```

These tables and relationships fully decompose the mission description into a structured goal model suitable for multi‑robot coordination, capturing the sequential, parallel, and fallback execution patterns required for efficient resource collection and delivery while managing battery constraints.
