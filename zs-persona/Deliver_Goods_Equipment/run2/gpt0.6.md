**Goal‑Model Tables**

| **Name**                                          | **Text**                                                                                                                 | **Runtime**    | **Goal Type** | **Target Condition / Enquired Info** | **Relation** | **Ground truth I**                                            | **Ground truth C** | **Consensus**                                            |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------- | ------------- | ------------------------------------ | ------------ | ------------------------------------------------------------- | ------------------ | ------------------------------------------------------------- |
| **G1** – *Complete Resource Delivery Mission*     | Deliver requested resources from storage to the specified destination while ensuring battery safety and fault tolerance. | # (parallel)   | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G2** – *Perform Collection of Resources*        | Gather all required items from the designated storage locations.                                                         | ; (sequential) | Perform       | –                                    | AND          | Achieve. Target condition: all required items were collected  | perform            | Achieve. Target condition: all required items were collected  |
| **G2.1** – *Navigate to Storage*                  | Move to the storage location that holds the requested item.                                                              | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G2.2** – *Request Resource*                     | Send a request message to the storage system specifying the needed items.                                                | -              | Perform       | –                                    | AND          | Query. Enqueried information: resources to be collected.      | OK                 | Query. Enqueried information: resources to be collected.      |
| **G2.3** – *Wait for Retrieval*                   | Remain at the storage until the items are physically retrieved.                                                          | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G3** – *Perform Delivery of Resources*          | Transport the collected items to the destination point and hand them over to the requesting agent.                       | ; (sequential) | Perform       | –                                    | AND          | Achieve. Target condition: all required items were delivered. | OK                 | Achieve. Target condition: all required items were delivered. |
| **G3.1** – *Navigate to Delivery Location*        | Move from the storage to the delivery destination.                                                                       | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G3.2** – *Transport Resource*                   | Carry the items during the transit between storage and destination.                                                      | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G3.3** – *Deliver Resource*                     | Drop the items at the destination and confirm receipt.                                                                   | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G4** – *Monitor Battery Levels*                 | Continuously check the robot’s battery and react when thresholds are crossed.                                            | # (parallel)   | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G4.1** – *Handle Battery Low during Collection* | If battery < 10 % during collection, return to recharge and re-assign the mission.                                       | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G4.2** – *Handle Battery Low during Delivery*   | If battery < 30 % during delivery, return the resource to a checkpoint and re-assign remaining tasks.                    | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G5** – *Handle Failures*                        | Manage exceptional situations such as checkpoint return failure.                                                         | # (parallel)   | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G5.1** – *Send Alert to Sector Manager*         | Trigger an alert and report when a resource cannot be returned to a checkpoint.                                          | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G6** – *Parallel Assignment of Robots*          | Allocate multiple robots to simultaneous collect-deliver sub-missions to reduce overall mission time.                    | # (parallel)   | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |
| **G6.1** – *Assign Robots to Parallel Tasks*      | Dispatch additional robots to other storages and destinations as needed.                                                 | -              | Perform       | –                                    | AND          | OK                                                            | OK                 | OK                                                            |


---

**Task‑Model Tables**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** – *Navigate to Storage* | Robot moves from its current position to the designated storage location. | AND | Storage | 1 |
| **AT2** – *Request Resource* | Robot sends a request message to the storage system. | AND | Storage | 1 |
| **AT3** – *Wait for Retrieval* | Robot remains at the storage until the items are physically retrieved. | AND | Storage | 1 |
| **AT4** – *Navigate to Delivery Location* | Robot moves from the storage to the specified delivery point. | AND | Delivery Destination | 1 |
| **AT5** – *Transport Resource* | Robot carries the items during transit. | AND | Between Storage and Destination | 1 |
| **AT6** – *Deliver Resource* | Robot deposits the items at the destination and confirms receipt. | AND | Delivery Destination | 1 |
| **AT7** – *Recharge Battery* | Robot returns to the recharging station to replenish its battery. | AND | Recharging Station | 1 |
| **AT8** – *Return Resource to Checkpoint* | Robot brings the resource back to a checkpoint when battery is low during delivery. | AND | Checkpoint | 1 |
| **AT9** – *Send Alert to Sector Manager* | Robot sends an alert and report to the sector manager when checkpoint return fails. | AND | N/A | 1 |
| **AT10** – *Assign Robot to Parallel Tasks* | Control center dispatches additional robots to other storages/destinations. | AND | Control Center | 1 |

---

### Summary Table (Goals + Tasks)

| ID | Title | Type | Relation | Runtime | Location / Robots |
|----|-------|------|----------|---------|-------------------|
| **G1** | Complete Resource Delivery Mission | Perform | AND | # | – |
| **G2** | Perform Collection of Resources | Perform | AND | ; | – |
| **G2.1** | Navigate to Storage | Perform | AND | - | – |
| **AT1** | Navigate to Storage | – | AND | – | Storage, 1 |
| **G2.2** | Request Resource | Perform | AND | - | – |
| **AT2** | Request Resource | – | AND | – | Storage, 1 |
| **G2.3** | Wait for Retrieval | Perform | AND | - | – |
| **AT3** | Wait for Retrieval | – | AND | – | Storage, 1 |
| **G3** | Perform Delivery of Resources | Perform | AND | ; | – |
| **G3.1** | Navigate to Delivery Location | Perform | AND | - | – |
| **AT4** | Navigate to Delivery Location | – | AND | – | Delivery Destination, 1 |
| **G3.2** | Transport Resource | Perform | AND | - | – |
| **AT5** | Transport Resource | – | AND | – | Between Storage and Destination, 1 |
| **G3.3** | Deliver Resource | Perform | AND | - | – |
| **AT6** | Deliver Resource | – | AND | – | Delivery Destination, 1 |
| **G4** | Monitor Battery Levels | Perform | AND | # | – |
| **G4.1** | Handle Battery Low during Collection | Perform | AND | - | – |
| **AT7** | Recharge Battery | – | AND | – | Recharging Station, 1 |
| **G4.2** | Handle Battery Low during Delivery | Perform | AND | - | – |
| **AT8** | Return Resource to Checkpoint | – | AND | – | Checkpoint, 1 |
| **G5** | Handle Failures | Perform | AND | # | – |
| **G5.1** | Send Alert to Sector Manager | Perform | AND | - | – |
| **AT9** | Send Alert to Sector Manager | – | AND | – | N/A, 1 |
| **G6** | Parallel Assignment of Robots | Perform | AND | # | – |
| **G6.1** | Assign Robots to Parallel Tasks | Perform | AND | - | – |
| **AT10** | Assign Robot to Parallel Tasks | – | AND | – | Control Center, 1 |

---

### Logical Relationships (Tree View)

```
G1 -> G2, G3, G4, G5, G6  [AND][#]

G2 -> G2.1, G2.2, G2.3  [AND][;]
G2.1 -> AT1 [AND]
G2.2 -> AT2 [AND]
G2.3 -> AT3 [AND]

G3 -> G3.1, G3.2, G3.3  [AND][;]
G3.1 -> AT4 [AND]
G3.2 -> AT5 [AND]
G3.3 -> AT6 [AND]

G4 -> G4.1, G4.2  [AND][#]
G4.1 -> AT7 [AND]
G4.2 -> AT8 [AND]

G5 -> G5.1  [AND][#]
G5.1 -> AT9 [AND]

G6 -> G6.1  [AND][#]
G6.1 -> AT10 [AND]
```

*All goals and tasks are linked via **AND** relations, reflecting that each child must be satisfied for its parent to succeed. The runtime annotations (`#`, `;`, `-`) indicate parallel execution, sequential execution, and leaf nodes, respectively.*
