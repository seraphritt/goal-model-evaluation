**Goal Model – Multi‑Robot Resource Delivery**


| **Name**                                                 | **Text**                                                                                                           | **Runtime**                         | **Goal Type** | **Target Condition / Enquired Info**                                                             | **Relation**                               | **Justification**                                                                 | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------ | --------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1** – Deliver Requested Resources to Requesting Agent | Bring the requested resources to the location specified by the requesting agent and mark the request as fulfilled. | `;`                                 | Achieve       | *All requested resources are present at the destination and the request is marked as satisfied.* | AND (to G2 & G3)                           | Collection must finish before delivery – strictly sequential.                     | perform                                                  | OK                 | perform                                                  |
| **G2** – Collect Resources                               | Execute the collection phase.                                                                                      | `FALLBACK(;(G2.1;G2.2;G2.3), G2.4)` | Perform       | –                                                                                                | OR (normal collection vs battery-fallback) | Normal collection can fail because of low battery; fallback handles reassignment. | Achive. Target condition: all resources were collected.  | OK                 | Achive. Target condition: all resources were collected.  |
| **G2.1** – Navigate to Storage                           | Robot moves to the storage where the needed resources are located.                                                 | `-`                                 | Perform       | –                                                                                                | AND (within normal collection)             | Robot must reach storage before requesting.                                       | OK                                                       | OK                 | OK                                                       |
| **G2.2** – Request Resource                              | Robot sends a message to the storage specifying the exact resources needed.                                        | `-`                                 | Perform       | –                                                                                                | AND                                        | The request is the only way to trigger retrieval.                                 | Query. enquired information: resources to be collected.  | OK                 | Query. enquired information: resources to be collected.  |
| **G2.3** – Wait for Retrieval                            | Robot waits until the resources are retrieved and ready for pickup.                                                | `-`                                 | Perform       | –                                                                                                | AND                                        | Waiting is required until the storage confirms availability.                      | OK                                                       | OK                 | OK                                                       |
| **G2.4** – Handle Low Battery during Collection          | Robot returns to the recharge station (battery < 10 %) and assigns the mission to another robot.                   | `-`                                 | Perform       | –                                                                                                | AND                                        | Battery threshold triggers immediate reassignment.                                | OK                                                       | OK                 | OK                                                       |
| **G3** – Deliver Resources                               | Execute the delivery phase.                                                                                        | `FALLBACK(;(G3.1;G3.2;G3.3), G3.4)` | Perform       | –                                                                                                | OR (normal delivery vs battery-fallback)   | Low battery in delivery forces checkpointing and reassignment.                    | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G3.1** – Navigate to Destination                       | Robot moves to the destination location where resources must be delivered.                                         | `-`                                 | Perform       | –                                                                                                | AND                                        | Delivery can only start once the robot reaches the destination.                   | OK                                                       | OK                 | OK                                                       |
| **G3.2** – Deliver Items                                 | Robot unloads the retrieved resources at the destination.                                                          | `-`                                 | Perform       | –                                                                                                | AND                                        | Unloading is the core of the delivery.                                            | OK                                                       | OK                 | OK                                                       |
| **G3.3** – Perform Multiple Runs to Transfer All Items   | Robot makes successive trips between storage and destination until all resources are delivered.                    | `-`                                 | Perform       | –                                                                                                | AND                                        | Multiple loads may be necessary for large payloads.                               | OK                                                       | OK                 | OK                                                       |
| **G3.4** – Handle Low Battery during Delivery            | Robot returns the resource to a checkpoint (battery < 30 %) and assigns remaining items to another robot.          | `-`                                 | Perform       | –                                                                                                | AND                                        | Battery threshold triggers checkpointing and reassignment.                        | OK                                                       | OK                 | OK                                                       |
| **G4** – Trigger Alert and Report to Sector Manager      | Send an alert and report if the robot fails to return the resource to a checkpoint.                                | `-`                                 | Perform       | –                                                                                                | AND                                        | Alerting is mandatory when checkpointing fails.                                   | OK                                                       | OK                 | OK                                                       |

---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** | **Justification** |
|----------|----------|--------------|--------------|----------------------|-------------------|
| **AT1** – Navigate to Storage | Robot moves from its current location to the storage where requested resources are located. | AND | *storage* | 1 | Only one robot is needed to perform the navigation. |
| **AT2** – Send Request to Storage | Robot sends a message to the storage specifying the exact resources needed. | AND | *storage* | 1 | The robot at the storage is the sole requester. |
| **AT3** – Wait for Resource Retrieval | Robot remains at the storage until the resources are retrieved and ready for pickup. | AND | *storage* | 1 | Waiting is a passive action performed by the same robot. |
| **AT4** – Return to Recharge Station & Reassign Mission | Robot returns to the recharge station because battery is below 10 % and assigns the mission to another robot. | AND | *recharge station* | 1 | The robot must recharge and hand over the task. |
| **AT5** – Navigate to Destination | Robot moves to the destination location where the resources must be delivered. | AND | *destination* | 1 | One robot travels to the delivery point. |
| **AT6** – Deliver Items to Destination | Robot unloads the retrieved resources at the destination location. | AND | *destination* | 1 | Unloading is performed by the delivering robot. |
| **AT7** – Perform Multiple Runs to Transfer All Items | Robot makes successive trips between storage and destination until all resources are delivered. | AND | *between storage and destination* | 1 | Multiple trips are required for large payloads. |
| **AT8** – Return Resource to Checkpoint & Reassign Remaining Task | Robot returns the resource to a checkpoint due to low battery (30 %) in delivery phase and assigns the remaining items to another robot. | AND | *checkpoint* | 1 | The robot must secure the resource before reassigning. |
| **AT9** – Send Alert & Report to Sector Manager | If the robot fails to return the resource to a checkpoint, it sends an alert and reports the incident to the sector manager. | AND | *sector manager* | 1 | Alerting is mandatory when checkpointing fails. |

---

### Summary Table (Goals & Tasks)

| **ID** | **Title** | **Type** | **Relation to Parent** | **Runtime / Location** | **Justification** |
|--------|-----------|----------|------------------------|------------------------|-------------------|
| G1 | Deliver Requested Resources to Requesting Agent | Achieve | – | `;` | Sequential: collect → deliver |
| G2 | Collect Resources | Perform | AND (to G1) | `FALLBACK(;(G2.1;G2.2;G2.3), G2.4)` | Battery‑fallback |
| G2.1 | Navigate to Storage | Perform | AND (to G2) | – | Reach storage |
| G2.2 | Request Resource | Perform | AND | – | Send request |
| G2.3 | Wait for Retrieval | Perform | AND | – | Wait for pickup |
| G2.4 | Handle Low Battery during Collection | Perform | AND | – | Recharge & reassign |
| G3 | Deliver Resources | Perform | AND (to G1) | `FALLBACK(;(G3.1;G3.2;G3.3), G3.4)` | Battery‑fallback |
| G3.1 | Navigate to Destination | Perform | AND | – | Reach destination |
| G3.2 | Deliver Items | Perform | AND | – | Unload resources |
| G3.3 | Perform Multiple Runs to Transfer All Items | Perform | AND | – | Multiple trips |
| G3.4 | Handle Low Battery during Delivery | Perform | AND | – | Checkpoint & reassign |
| G4 | Trigger Alert and Report to Sector Manager | Perform | AND (to G3.4) | – | Alert on failure |
| AT1 | Navigate to Storage | Task | AND (to G2.1) | *storage* | One robot |
| AT2 | Send Request to Storage | Task | AND | *storage* | One robot |
| AT3 | Wait for Resource Retrieval | Task | AND | *storage* | One robot |
| AT4 | Return to Recharge Station & Reassign Mission | Task | AND | *recharge station* | Recharge |
| AT5 | Navigate to Destination | Task | AND | *destination* | One robot |
| AT6 | Deliver Items to Destination | Task | AND | *destination* | One robot |
| AT7 | Perform Multiple Runs to Transfer All Items | Task | AND | *between storage & destination* | One robot |
| AT8 | Return Resource to Checkpoint & Reassign Remaining Task | Task | AND | *checkpoint* | Battery low |
| AT9 | Send Alert & Report to Sector Manager | Task | AND | *sector manager* | Alerting |

---

### Logical Relationships

| **Parent** | **Children** | **Relation** | **Runtime** | **Justification** |
|------------|--------------|--------------|-------------|-------------------|
| **G1** | G2, G3 | AND | `;` | Collection must finish before delivery. |
| **G2** | G2.1, G2.2, G2.3, G2.4 | OR (via FALLBACK) | `FALLBACK(;(G2.1;G2.2;G2.3), G2.4)` | Normal collection may fail due to low battery. |
| **G3** | G3.1, G3.2, G3.3, G3.4 | OR (via FALLBACK) | `FALLBACK(;(G3.1;G3.2;G3.3), G3.4)` | Low battery in delivery triggers checkpointing. |
| **G4** | AT9 | AND | `-` | Alert must be sent if checkpointing fails. |
| **AT1** | – | – | – | – |
| **AT2** | – | – | – | – |
| **AT3** | – | – | – | – |
| **AT4** | – | – | – | – |
| **AT5** | – | – | – | – |
| **AT6** | – | – | – | – |
| **AT7** | – | – | – | – |
| **AT8** | – | – | – | – |
| **AT9** | – | – | – | – |

*All task relations are **AND** because each task must be completed for its parent goal to succeed.*
