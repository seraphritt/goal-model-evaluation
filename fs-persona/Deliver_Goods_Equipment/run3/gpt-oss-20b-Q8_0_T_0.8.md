**Goal Model – Multi‑Robot Resource Delivery Mission**

---

### 1.  Goal Tables  

| **Name**                                         | **Text**                                                                                                                                  | **Runtime**        | **Goal Type** | **Target Condition / Enquired Info** | **Relation** | **Ground truth I**                                       | **Ground truth C** | **Ground truth E** |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------- | ------------------------------------ | ------------ | -------------------------------------------------------- | ------------------ | ------------------ |
| G1: Execute Resource Delivery Mission            | The overall mission to collect required resources from storage and deliver them to the requesting agent at the specified location.        | [;]                | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| G2: Collect Resources                            | The robot gathers the specified resources from the storage locations.                                                                     | [#]                | Perform       | –                                    | AND          | Achieve. Target condition: all resources were collected. |  OK                  |                    |
| AT1: Navigate to Storage and Request Resource    | Robot travels to the storage location, sends a request for the specified resources, and waits for acknowledgment.                         | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| AT2: Wait for Resource Retrieval                 | Robot waits until the requested resources are retrieved from storage.                                                                     | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| AT3: Return to Recharge Station if Battery <10%  | If the robot’s battery drops below 10 % during collection, it returns to the recharge station and transfers the mission to another robot. | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| G3: Deliver Resources                            | The robot transports the collected resources to the specified delivery location.                                                          | FALLBACK(G3.1, G4) | Perform       | –                                    | OR           | Achieve. Target condition: all resources were delivered. |  OK                  |                    |
| G3.1: Normal Delivery                            | The robot delivers resources to the destination following the standard delivery procedure.                                                | [#]                | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| AT4: Navigate to Delivery Location with Resource | Robot travels to the delivery location carrying the resources.                                                                            | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| AT5: Deliver Resource                            | Robot transfers the resources to the requesting agent at the delivery location.                                                           | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| AT6: Return to Checkpoint if Battery <30%        | If the robot’s battery drops below 30 % during delivery, it returns the resource to a checkpoint.                                         | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| AT7: Assign Remaining Task to Another Robot      | After returning to the checkpoint, the robot assigns the remaining delivery task to another robot.                                        | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| G4: Handle Failure to Return to Checkpoint       | If the robot fails to return the resource to the checkpoint, an alert is triggered and a report is sent to the sector manager.            | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |
| AT8: Trigger Alert and Send Report               | The robot triggers an alert and sends a report to the sector manager.                                                                     | –                  | Perform       | –                                    | AND          | OK                                                       |  OK                  |                    |


> **Notes**  
> *All leaf goals/tasks use “–” for Runtime.*  
> *The runtime annotation for G3 uses the **FALLBACK** operator to model the failure‑handling branch.*

---

### 2.  Task Tables  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| AT1 | Navigate to storage, request resources | AND | Storage | 1 |
| AT2 | Wait for resource retrieval | AND | Storage | 1 |
| AT3 | Return to recharge station if battery <10 % | AND | Recharge Station | 1 |
| AT4 | Navigate to delivery location with resource | AND | Delivery Location | 1 |
| AT5 | Deliver resource to requesting agent | AND | Delivery Location | 1 |
| AT6 | Return to checkpoint if battery <30 % | AND | Checkpoint | 1 |
| AT7 | Assign remaining delivery task to another robot | AND | Current Location | 1 |
| AT8 | Trigger alert and send report to sector manager | AND | Sector Manager | 1 |

---

### 3.  Summary Table (Goals + Tasks)  

| **ID** | **Title** | **Type** | **Runtime / Relation** |
|--------|-----------|----------|------------------------|
| G1 | Execute Resource Delivery Mission | Goal (Perform) | [;] – AND |
| G2 | Collect Resources | Goal (Perform) | [#] – AND |
| AT1 | Navigate to Storage and Request Resource | Task | AND |
| AT2 | Wait for Resource Retrieval | Task | AND |
| AT3 | Return to Recharge Station if Battery <10% | Task | AND |
| G3 | Deliver Resources | Goal (Perform) | FALLBACK(G3.1, G4) – OR |
| G3.1 | Normal Delivery | Goal (Perform) | [#] – AND |
| AT4 | Navigate to Delivery Location with Resource | Task | AND |
| AT5 | Deliver Resource | Task | AND |
| AT6 | Return to Checkpoint if Battery <30% | Task | AND |
| AT7 | Assign Remaining Task to Another Robot | Task | AND |
| G4 | Handle Failure to Return to Checkpoint | Goal (Perform) | – – AND |
| AT8 | Trigger Alert and Send Report | Task | AND |

---

### 4.  Logical Relationships  

```
G1 -> G2, G3 [AND][;]
G2 -> AT1, AT2, AT3 [AND][#]
G3 -> G3.1, G4 [OR][FALLBACK(G3.1,G4)]
G3.1 -> AT4, AT5, AT6, AT7 [AND][#]
G4 -> AT8 [AND][ - ]
```

These relationships capture the hierarchical structure and execution semantics of the mission, ensuring that the multi‑robot system can collect resources, deliver them, and handle battery‑related contingencies and failure alerts in a coordinated manner.
