**Goal Model – Multi‑Robot Resource Delivery Mission**

| **Name** | **Text** | **Runtime** | **Goal Type** | **Target Condition / Enquired Information** | **Relation** |
|----------|----------|-------------|---------------|-------------------------------------------|--------------|
| **G1 – Complete Resource Delivery Mission** | Ensure that all requested resources are delivered to the specified destination. | `G2;G3` | Achieve | *All requested resources have been delivered to the specified location.* | AND |
| **G2 – Collect Resources** | Gather the required items from the designated storage locations. | `G2.1;G2.2;G2.3;G2.4;G2.5` | Perform |  | AND |
| **G2.1 – Plan Collection Route** | Determine the optimal sequence of storages based on waiting time and path length. | `-` | Query | *Optimal sequence of storages based on waiting time and path.* | AND |
| **G2.2 – Navigate to Storage** | Move the robot to the next storage location. | `-` | Perform |  | AND |
| **G2.3 – Request Resources** | Send a request message to the storage for the needed items. | `-` | Perform |  | AND |
| **G2.4 – Wait for Retrieval** | Wait until the storage has supplied the requested resources. | `-` | Perform |  | AND |
| **G2.5 – Handle Low Battery in Collection** | If battery < 10 % return to the recharging station and hand over the mission to another robot. | `-` | Perform |  | AND |
| **G3 – Deliver Resources** | Transport the collected items to the destination. | `G3.1;G3.2;G3.3` | Perform |  | AND |
| **G3.1 – Navigate to Delivery Location** | Move the robot to the delivery point. | `-` | Perform |  | AND |
| **G3.2 – Transport Resources** | Carry the items from the storage to the delivery location. | `-` | Perform |  | AND |
| **G3.3 – Handle Low Battery in Delivery** | If battery < 30 % return the resource to a checkpoint and re‑assign the remaining task. | `FALLBACK(G3.3.1, G4)` | Perform |  | AND |
| **G3.3.1 – Return Resource to Checkpoint and Re‑assign** | Return the resource to a checkpoint and inform another robot of its location. | `-` | Perform |  | AND |
| **G4 – Failure Management** | Manage the situation when the robot cannot return the resource to the checkpoint. | `G4.1;G4.2` | Perform |  | AND |
| **G4.1 – Trigger Alert** | Raise an alert to the sector manager. | `-` | Perform |  | AND |
| **G4.2 – Send Report to Sector Manager** | Send a detailed report of the failure. | `-` | Perform |  | AND |

---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1 – Navigate to Storage** | Move the robot to the specified storage location. | AND | Storage (variable) | 1 |
| **AT2 – Send Request Message** | Transmit the resource request to the storage. | AND | Storage | 1 |
| **AT3 – Wait for Retrieval** | Remain at the storage until the items are ready. | AND | Storage | 1 |
| **AT4 – Navigate to Delivery Location** | Move the robot to the delivery point. | AND | Delivery Location | 1 |
| **AT5 – Transport Resources** | Carry the items from storage to delivery location. | AND | Delivery Location | 1 |
| **AT6 – Return to Recharging Station** | Go to the recharging station when battery < 10 %. | AND | Recharging Station | 1 |
| **AT7 – Assign Mission to Another Robot** | Inform another robot of the remaining task. | AND | Central Command | 1 |
| **AT8 – Return Resource to Checkpoint** | Bring the resource to a checkpoint when battery < 30 %. | AND | Checkpoint | 1 |
| **AT9 – Trigger Alert** | Raise an alert to the sector manager. | AND | Central Command | 1 |
| **AT10 – Send Report to Sector Manager** | Deliver a failure report. | AND | Central Command | 1 |

---

### Logical Relationships Summary

| **Parent Goal / Task** | **Children** | **Relation** | **Runtime** |
|------------------------|--------------|--------------|-------------|
| **G1** | G2, G3 | AND | sequential (`;`) |
| **G2** | G2.1, G2.2, G2.3, G2.4, G2.5 | AND | sequential (`;`) |
| **G3** | G3.1, G3.2, G3.3 | AND | sequential (`;`) |
| **G3.3** | G3.3.1, G4 | AND | fallback (`FALLBACK(G3.3.1, G4)`) |
| **G4** | G4.1, G4.2 | AND | sequential (`;`) |
| **G2.2** | AT1 | AND | - |
| **G2.3** | AT2 | AND | - |
| **G2.4** | AT3 | AND | - |
| **G2.5** | AT6, AT7 | AND | - |
| **G3.1** | AT4 | AND | - |
| **G3.2** | AT5 | AND | - |
| **G3.3.1** | AT8 | AND | - |
| **G4.1** | AT9 | AND | - |
| **G4.2** | AT10 | AND | - |

This goal‑task decomposition captures the full multi‑robot mission, including planning, execution, battery‑aware contingencies, and failure handling, with clear execution order, parallelism, and fallback mechanisms.
