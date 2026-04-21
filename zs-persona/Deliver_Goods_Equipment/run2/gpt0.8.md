**Goal Model – Multi‑Robot Resource Transfer Mission**

| **Name**                                   | **Text**                                                                                                                   | **Runtime**                          | **Goal Type** | **Target Condition / Enquired Information**      | **Relation** | **Ground truth I** | **Ground truth C** | **Ground truth E** |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------- | ------------------------------------------------ | ------------ | ------------------ | ------------------ | ------------------ |
| **G1: Complete Resource Transfer Mission** | Ensure that required resources are collected from storage and delivered to the requesting agent at the specified location. | `;`                                  | Perform       | –                                                | AND          | OK                   |OK                    |                    |
| **G2: Collect Resources**                  | Collect the required resources from storage locations.                                                                     | `FALLBACK((G2.1; G2.2; G2.3), G2.4)` | Perform       | –                                                | AND          | Achieve. Target condition: all resources were collected.                   | OK                   |                    |
| G2.1                                       | Navigate to the designated storage location.                                                                               | `-`                                  | Perform       | –                                                | AND          | OK                   |OK                    |                    |
| G2.2                                       | Send a request to the storage for the specified resources.                                                                 | `-`                                  | Perform       | –                                                | AND          | Query. Enqueried information: resources to be collected                   |   OK                 |                    |
| G2.3                                       | Wait until the requested resources are retrieved from the storage.                                                         | `-`                                  | Perform       | –                                                | AND          |                    |   OK                 |                    |
| G2.4                                       | Handle low-battery situation during collection phase.                                                                      | `;`                                  | Perform       | –                                                | AND          |                    |  OK                  |                    |
| G2.4.1                                     | Return to the recharging station to recharge the battery.                                                                  | `-`                                  | Perform       | –                                                | AND          |                    |  OK                  |                    |
| G2.4.2                                     | Assign the remaining collection mission to another robot.                                                                  | `-`                                  | Perform       | –                                                | AND          |                    |  OK                  |                    |
| **G3: Deliver Resources**                  | Deliver the collected resources to the specified destination.                                                              | `FALLBACK((G3.1; G3.2), G3.3)`       | Achieve       | *Resources are at the destination location.*     | AND          |                    |  OK                  |                    |
| G3.1                                       | Navigate to the delivery destination.                                                                                      | `-`                                  | Perform       | –                                                | AND          |                    |  OK                  |                    |
| G3.2                                       | Carry the resources from storage to destination.                                                                           | `-`                                  | Perform       | –                                                | AND          |                    |   OK                 |                    |
| G3.3                                       | Handle low-battery situation during delivery phase.                                                                        | `;`                                  | Perform       | –                                                | AND          |                    |  OK                  |                    |
| G3.3.1                                     | Return the resource to a checkpoint before re-assigning.                                                                   | `;`                                  | Perform       | –                                                | AND          |                    |  OK                  |                    |
| G3.3.1.1                                   | Trigger an alert in case of failure to return resource to checkpoint.                                                      | `-`                                  | Perform       | –                                                | AND          |                    |  OK                  |                    |
| G3.3.1.2                                   | Send a report to the sector manager after alert.                                                                           | `-`                                  | Perform       | –                                                | AND          |                    |  OK                  |                    |
| G3.3.2                                     | Assign remaining delivery tasks to another robot.                                                                          | `-`                                  | Perform       | –                                                | AND          |                    | OK                   |                    |
| **G5: Check Battery Level**                | Query the current battery level of the robot.                                                                              | `-`                                  | Query         | *Current battery percentage of the robot.*       | AND          | Perform.                   | Perform                   |                    |
| **G6: Check Resource Availability**        | Query the availability of the requested resources at the storage.                                                          | `-`                                  | Query         | *Whether the requested resources are available.* | AND          |  OK                  |  OK                  |                    |
| **G7: Check Resource Position**            | Query the position/location of the requested resources.                                                                    | `-`                                  | Query         | *Storage location of the requested resources.*   | AND          | OK                   | OK                   |                    |


---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1: Navigate to Storage** | Navigate to the designated storage location. | AND | Storage | 1 |
| AT2: Request Resource | Send request to storage for specified resources. | AND | Storage | 1 |
| AT3: Wait for Retrieval | Wait until resources are retrieved from storage. | AND | Storage | 1 |
| AT4: Return to Recharging Station | Return to recharging station to recharge battery. | AND | Recharging Station | 1 |
| AT5: Assign Mission to Another Robot | Assign remaining collection mission to another robot. | AND | Current / Coordination Center | 1 |
| AT6: Navigate to Destination | Navigate to delivery destination. | AND | Destination | 1 |
| AT7: Carry Resource | Carry resources to destination. | AND | Destination | 1 |
| AT8: Return Resource to Checkpoint | Return resource to checkpoint. | AND | Checkpoint | 1 |
| AT9: Assign Remaining Task to Another Robot | Assign remaining delivery tasks to another robot. | AND | Checkpoint | 1 |
| AT10: Trigger Alert | Trigger alert for failure to return resource. | AND | Current | 1 |
| AT11: Send Report to Sector Manager | Send report to sector manager. | AND | Current | 1 |
| AT12: Check Battery Level | Check current battery level. | AND | Current | 1 |
| AT13: Check Resource Availability | Check availability of requested resources. | AND | Storage | 1 |
| AT14: Check Resource Position | Check position of requested resources. | AND | Storage | 1 |

---

### Summary Table (Goals & Tasks)

| **ID** | **Type** | **Title** |
|--------|----------|-----------|
| G1 | Goal | Complete Resource Transfer Mission |
| G2 | Goal | Collect Resources |
| G2.1 | Goal | Navigate to Storage |
| G2.2 | Goal | Request Resource |
| G2.3 | Goal | Wait for Retrieval |
| G2.4 | Goal | Handle Low Battery in Collection |
| G2.4.1 | Goal | Return to Recharging Station |
| G2.4.2 | Goal | Assign Mission to Another Robot |
| G3 | Goal | Deliver Resources |
| G3.1 | Goal | Navigate to Destination |
| G3.2 | Goal | Carry Resource |
| G3.3 | Goal | Handle Low Battery in Delivery |
| G3.3.1 | Goal | Return Resource to Checkpoint |
| G3.3.1.1 | Goal | Trigger Alert |
| G3.3.1.2 | Goal | Send Report to Sector Manager |
| G3.3.2 | Goal | Assign Remaining Task to Another Robot |
| G5 | Goal | Check Battery Level |
| G6 | Goal | Check Resource Availability |
| G7 | Goal | Check Resource Position |
| AT1 | Task | Navigate to Storage |
| AT2 | Task | Request Resource |
| AT3 | Task | Wait for Retrieval |
| AT4 | Task | Return to Recharging Station |
| AT5 | Task | Assign Mission to Another Robot |
| AT6 | Task | Navigate to Destination |
| AT7 | Task | Carry Resource |
| AT8 | Task | Return Resource to Checkpoint |
| AT9 | Task | Assign Remaining Task to Another Robot |
| AT10 | Task | Trigger Alert |
| AT11 | Task | Send Report to Sector Manager |
| AT12 | Task | Check Battery Level |
| AT13 | Task | Check Resource Availability |
| AT14 | Task | Check Resource Position |

---

### Logical Relationships

```
G1  -> G2, G3  [AND][;]
G2  -> G2.1, G2.2, G2.3, G2.4  [AND][FALLBACK((G2.1; G2.2; G2.3), G2.4)]
G2.1 -> AT1  [AND][-]
G2.2 -> AT2  [AND][-]
G2.3 -> AT3  [AND][-]
G2.4 -> G2.4.1, G2.4.2  [AND][;]
G2.4.1 -> AT4  [AND][-]
G2.4.2 -> AT5  [AND][-]

G3  -> G3.1, G3.2, G3.3  [AND][FALLBACK((G3.1; G3.2), G3.3)]
G3.1 -> AT6  [AND][-]
G3.2 -> AT7  [AND][-]
G3.3 -> G3.3.1, G3.3.2  [AND][;]
G3.3.1 -> G3.3.1.1, G3.3.1.2  [AND][;]
G3.3.1.1 -> AT10  [AND][-]
G3.3.1.2 -> AT11  [AND][-]
G3.3.2 -> AT9  [AND][-]

G5  -> AT12  [AND][-]
G6  -> AT13  [AND][-]
G7  -> AT14  [AND][-]
```

This decomposition provides a clear, hierarchical goal model suitable for planning and execution in a multi‑robot system, capturing all operational, query, and achievement aspects of the described mission.
