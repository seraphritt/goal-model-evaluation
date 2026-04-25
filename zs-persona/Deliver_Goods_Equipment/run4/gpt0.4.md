**Goal‑Model Tables**

| **Name**                                        | **Text**                                                                                        | **Runtime**               | **Goal Type** | **Target Condition / Enquired Information**              | **Relation** | **Ground truth I** | **Ground truth C** | **Ground truth E** |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------- | ------------- | -------------------------------------------------------- | ------------ | ------------------ | ------------------ | ------------------ |
| G1 – Deliver All Requested Resources            | Ensure that every item requested by the agent is delivered to the specified location.           | `;` (sequential)          | Achieve       | All requested resources are at the destination location. | AND          | OK                   | OK                   |                    |
| G2 – Collect Resources                          | Perform the collection phase for the requested items.                                           | `;`                       | Perform       | –                                                        | AND          | Achieve. Target condition: all resources were collected.                   | OK                   |                    |
| G2.1 – Navigate to Storage                      | Move the robot to the storage location containing the required resources.                       | `-`                       | Perform       | –                                                        | AND          | OK                   |OK                    |                    |
| G2.2 – Request Resource                         | Send a request message to the storage specifying the exact resources needed.                    | `-`                       | Perform       | –                                                        | AND          | Query. Enqueried information: resources to be collected.                   |OK                    |                    |
| G2.3 – Wait for Retrieval                       | Wait until the storage confirms that the resources have been retrieved.                         | `-`                       | Perform       | –                                                        | AND          |  OK                  |OK                    |                    |
| G2.4 – Handle Low Battery During Collection     | If the battery falls below 10 % during collection, take corrective action.                      | `FALLBACK(G2.4.1,G2.4.2)` | Perform       | –                                                        | OR           |  OK                  | OK                   |                    |
| G2.4.1 – Return to Recharge Station             | Go to the nearest recharge station to replenish battery.                                        | `-`                       | Perform       | –                                                        | AND          |  OK                  | OK                   |                    |
| G2.4.2 – Assign Mission to Another Robot        | Notify the fleet manager to re-assign the remaining collection task to another robot.           | `-`                       | Perform       | –                                                        | AND          |  OK                  | OK                   |                    |
| G3 – Deliver Resources                          | Perform the delivery phase for the retrieved items.                                             | `;`                       | Perform       | –                                                        | AND          |  Achieve. Target condition: all resources were delivered.                  | OK                   |                    |
| G3.1 – Transport Resource to Destination        | Carry the resources from the storage to the requested destination.                              | `-`                       | Perform       | –                                                        | AND          |  OK                  | OK                   |                    |
| G3.2 – Handle Low Battery During Delivery       | If the battery falls below 30 % during delivery, take corrective action.                        | `FALLBACK(G3.2.1,G3.2.2)` | Perform       | –                                                        | OR           |  OK                  |  OK                  |                    |
| G3.2.1 – Return Resource to Checkpoint          | Return the partially delivered resource to the nearest checkpoint.                              | `-`                       | Perform       | –                                                        | AND          |  OK                  | OK                   |                    |
| G3.2.2 – Assign Remaining Task to Another Robot | Notify the fleet manager to re-assign the remaining delivery task to another robot.             | `-`                       | Perform       | –                                                        | AND          |  OK                  | OK                   |                    |
| G3.3 – Trigger Alert to Sector Manager          | If the robot fails to return the resource to a checkpoint, send an alert to the sector manager. | `-`                       | Perform       | –                                                        | AND          |  OK                  | OK                   |                    |


---

**Task‑Model Tables**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| AT1 – Navigate to Storage | Move the robot to the storage location where the resources are stored. | AND | Storage | 1 |
| AT2 – Send Request Message | Transmit a request containing the precise specification of the needed resources to the storage. | AND | Storage | 1 |
| AT3 – Wait for Retrieval | Remain idle at the storage until the resources have been physically retrieved and confirmed. | AND | Storage | 1 |
| AT4 – Navigate to Recharge Station | Travel to the nearest recharge station to replenish the battery. | AND | Recharge Station | 1 |
| AT5 – Notify Mission Assignment | Communicate to the fleet manager that the current robot’s task has been aborted and another robot must take over. | AND | Communication Hub | 1 |
| AT6 – Transport Resource to Destination | Move the retrieved resources from the storage to the specified destination location. | AND | Destination | 1 |
| AT7 – Return Resource to Checkpoint | Carry the partially delivered resource back to the nearest checkpoint. | AND | Checkpoint | 1 |
| AT8 – Assign Remaining Task | Inform the fleet manager to re‑assign the remaining part of the delivery task to another robot. | AND | Checkpoint | 1 |
| AT9 – Trigger Alert to Sector Manager | Send an alert to the sector manager indicating that the robot failed to return the resource to a checkpoint. | AND | Communication Hub | 1 |

---

**Summary Table (Combined Goals & Tasks)**

| **Node ID** | **Title** | **Type** | **Parent** | **Runtime / Relation** |
|-------------|-----------|----------|------------|------------------------|
| G1 | Deliver All Requested Resources | Goal (Achieve) | – | `;` (sequential) |
| G2 | Collect Resources | Goal (Perform) | G1 | `;` |
| G2.1 | Navigate to Storage | Goal (Perform) | G2 | `-` |
| AT1 | Navigate to Storage | Task | G2.1 | AND |
| G2.2 | Request Resource | Goal (Perform) | G2 | `-` |
| AT2 | Send Request Message | Task | G2.2 | AND |
| G2.3 | Wait for Retrieval | Goal (Perform) | G2 | `-` |
| AT3 | Wait for Retrieval | Task | G2.3 | AND |
| G2.4 | Handle Low Battery During Collection | Goal (Perform) | G2 | `FALLBACK(G2.4.1,G2.4.2)` |
| G2.4.1 | Return to Recharge Station | Goal (Perform) | G2.4 | `-` |
| AT4 | Navigate to Recharge Station | Task | G2.4.1 | AND |
| G2.4.2 | Assign Mission to Another Robot | Goal (Perform) | G2.4 | `-` |
| AT5 | Notify Mission Assignment | Task | G2.4.2 | AND |
| G3 | Deliver Resources | Goal (Perform) | G1 | `;` |
| G3.1 | Transport Resource to Destination | Goal (Perform) | G3 | `-` |
| AT6 | Transport Resource to Destination | Task | G3.1 | AND |
| G3.2 | Handle Low Battery During Delivery | Goal (Perform) | G3 | `FALLBACK(G3.2.1,G3.2.2)` |
| G3.2.1 | Return Resource to Checkpoint | Goal (Perform) | G3.2 | `-` |
| AT7 | Return Resource to Checkpoint | Task | G3.2.1 | AND |
| G3.2.2 | Assign Remaining Task to Another Robot | Goal (Perform) | G3.2 | `-` |
| AT8 | Assign Remaining Task | Task | G3.2.2 | AND |
| G3.3 | Trigger Alert to Sector Manager | Goal (Perform) | G3 | `-` |
| AT9 | Trigger Alert to Sector Manager | Task | G3.3 | AND |

---

**Logical Relationships**

- **G1** → **G2**, **G3** [AND][sequential `;`]
- **G2** → **G2.1**, **G2.2**, **G2.3**, **G2.4** [AND][sequential `;`]
- **G2.4** → **G2.4.1**, **G2.4.2** [OR][fallback `FALLBACK(G2.4.1,G2.4.2)`]
- **G3** → **G3.1**, **G3.2**, **G3.3** [AND][sequential `;`]
- **G3.2** → **G3.2.1**, **G3.2.2** [OR][fallback `FALLBACK(G3.2.1,G3.2.2)`]
- **G2.1** → **AT1** [AND]
- **G2.2** → **AT2** [AND]
- **G2.3** → **AT3** [AND]
- **G2.4.1** → **AT4** [AND]
- **G2.4.2** → **AT5** [AND]
- **G3.1** → **AT6** [AND]
- **G3.2.1** → **AT7** [AND]
- **G3.2.2** → **AT8** [AND]
- **G3.3** → **AT9** [AND]
