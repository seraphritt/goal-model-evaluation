**Goal Model – Multi‑Robot Resource Collection & Delivery**

| **Name**                                       | **Text**                                                                                                                                             | **Runtime**                                 | **Goal Type** | **Target Condition / Enquired Info**                      | **Relation** | **Ground Truth I** | **Ground Truth G** | **Consensus** |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ------------- | --------------------------------------------------------- | ------------ | ------------------ | ------------------ | ------------- |
| **G1 – Complete Resource Delivery Mission**    | Ensure that all requested resources are collected from storages and delivered to the specified destination.                                          | `G1.1; G1.2`                                | Achieve       | All requested resources are delivered to the destination. | –            | Perform                   |                    |               |
| **G1.1 – Collect Resources**                   | Gather all required items from the designated storage locations.                                                                                     | `(G1.1.1; FALLBACK(G1.1.2, G1.1.4))#G1.1.3` | Achieve       | All requested resources are collected.                    | AND          | OK                   |                    |               |
| **G1.1.1 – Plan Collection Route**             | Compute the optimal path to the storages, taking into account waiting times and travel distance.                                                     | `-`                                         | Perform       | –                                                         | AND          | Query. Enqueried info: optimal path                   |                    |               |
| **G1.1.2 – Execute Collection**                | Perform the actual collection sequence: navigate, request, and wait for the resource.                                                                | `-`                                         | Perform       | –                                                         | AND          | OK                  |                    |               |
| **G1.1.3 – Monitor Battery During Collection** | Continuously check the robot’s battery level while collecting.                                                                                       | `-`                                         | Query         | Current battery level during collection.                  | AND          |  OK                  |                    |               |
| **G1.1.4 – Recharge & Re-assign Mission**      | If battery < 10 % during collection, return to the charging station and hand over the task to another robot.                                         | `-`                                         | Perform       | –                                                         | AND          | OK                   |                    |               |
| **G1.2 – Deliver Resources**                   | Transport the collected items to the requesting agent’s location.                                                                                    | `(G1.2.1; FALLBACK(G1.2.2, G1.2.4))#G1.2.3` | Achieve       | All collected resources are delivered to the destination. | AND          |OK                    |                    |               |
| **G1.2.1 – Navigate to Delivery Location**     | Move the robot from the storage to the delivery point.                                                                                               | `-`                                         | Perform       | –                                                         | AND          |     OK               |                    |               |
| **G1.2.2 – Transport Resource**                | Physically carry the resource to the delivery location.                                                                                              | `-`                                         | Perform       | –                                                         | AND          |   OK                 |                    |               |
| **G1.2.3 – Monitor Battery During Delivery**   | Continuously check the robot’s battery level while delivering.                                                                                       | `-`                                         | Query         | Current battery level during delivery.                    | AND          |  OK                  |                    |               |
| **G1.2.4 – Return to Checkpoint & Re-assign**  | If battery < 30 % during delivery, return the resource to a checkpoint, alert the sector manager, and hand over the remaining task to another robot. | `-`                                         | Perform       | –                                                         | AND          |  OK                  |                    |               |



---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1 – Navigate to Storage A** | Robot moves to Storage A to collect the resource. | AND | Storage A | 1 |
| **AT2 – Request Resource at Storage A** | Robot sends a request for the needed item. | AND | Storage A | 1 |
| **AT3 – Wait for Retrieval at Storage A** | Robot waits until the resource is retrieved. | AND | Storage A | 1 |
| **AT4 – Navigate to Delivery Location B** | Robot moves to Delivery Location B to deliver the resource. | AND | Delivery Location B | 1 |
| **AT5 – Transport Resource to Delivery Location** | Robot carries the resource to the delivery point. | AND | Delivery Location B | 1 |
| **AT6 – Navigate to Recharging Station** | Robot moves to the charging station to recharge. | AND | Recharging Station | 1 |
| **AT7 – Navigate to Checkpoint** | Robot moves to a checkpoint to deposit the resource. | AND | Checkpoint | 1 |
| **AT8 – Send Alert to Sector Manager** | Robot notifies the sector manager of a failure to return the resource. | AND | Robot’s current location | 1 |
| **AT9 – Assign Remaining Task to Another Robot** | Robot hands over the remaining delivery task to a spare robot. | AND | Robot’s current location | 1 |
| **AT10 – Check Battery Level** | Robot queries its own battery level. | AND | Robot’s current location | 1 |
| **AT11 – Compute Optimal Collection Route** | Robot calculates the best path to the storages. | AND | Robot’s current location | 1 |
| **AT12 – Compute Optimal Delivery Route** | Robot calculates the best path to the delivery location. | AND | Robot’s current location | 1 |

---

### Summary Table (Goals & Tasks)

| **ID** | **Title** | **Type** | **Runtime / Relation** |
|--------|-----------|----------|------------------------|
| G1 | Complete Resource Delivery Mission | Achieve | `G1.1; G1.2` |
| G1.1 | Collect Resources | Achieve | `(G1.1.1; FALLBACK(G1.1.2, G1.1.4))#G1.1.3` |
| G1.1.1 | Plan Collection Route | Perform | – |
| G1.1.2 | Execute Collection | Perform | – |
| G1.1.3 | Monitor Battery During Collection | Query | – |
| G1.1.4 | Recharge & Re‑assign Mission | Perform | – |
| G1.2 | Deliver Resources | Achieve | `(G1.2.1; FALLBACK(G1.2.2, G1.2.4))#G1.2.3` |
| G1.2.1 | Navigate to Delivery Location | Perform | – |
| G1.2.2 | Transport Resource | Perform | – |
| G1.2.3 | Monitor Battery During Delivery | Query | – |
| G1.2.4 | Return to Checkpoint & Re‑assign | Perform | – |
| AT1 | Navigate to Storage A | – | – |
| AT2 | Request Resource at Storage A | – | – |
| AT3 | Wait for Retrieval at Storage A | – | – |
| AT4 | Navigate to Delivery Location B | – | – |
| AT5 | Transport Resource to Delivery Location | – | – |
| AT6 | Navigate to Recharging Station | – | – |
| AT7 | Navigate to Checkpoint | – | – |
| AT8 | Send Alert to Sector Manager | – | – |
| AT9 | Assign Remaining Task to Another Robot | – | – |
| AT10 | Check Battery Level | – | – |
| AT11 | Compute Optimal Collection Route | – | – |
| AT12 | Compute Optimal Delivery Route | – | – |

---

### Logical Relationships

- **G1 → G1.1, G1.2** [AND][sequential]  
- **G1.1 → G1.1.1, G1.1.2, G1.1.3, G1.1.4** [AND][parallel]  
- **G1.1.1 → AT11** [AND]  
- **G1.1.2 → AT1, AT2, AT3** [AND][parallel]  
- **G1.1.3 → AT10** [AND]  
- **G1.1.4 → AT6** [AND]  
- **G1.2 → G1.2.1, G1.2.2, G1.2.3, G1.2.4** [AND][parallel]  
- **G1.2.1 → AT4, AT12** [AND][parallel]  
- **G1.2.2 → AT5** [AND]  
- **G1.2.3 → AT10** [AND]  
- **G1.2.4 → AT7, AT8, AT9** [AND][parallel]  

This goal‑task decomposition captures the multi‑robot mission’s logical structure, execution flow, and operational details, ready for implementation in a multi‑robot planning and coordination framework.
