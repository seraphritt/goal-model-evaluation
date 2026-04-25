**Goal Model – Multi‑Robot Resource Delivery**

| **Name**                         | **Text**                                                                                    | **Runtime**            | **Goal Type** | **Target Condition / Enquired Info** | **Relation** | **Ground truth I** | **Ground truth C** | **Ground truth E** |
| -------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------- | ------------- | ------------------------------------ | ------------ | ------------------ | ------------------ | ------------------ |
| **G1: Complete Mission**         | Complete the resource delivery mission by collecting and delivering all required resources. | `;`                    | Perform       | –                                    | AND          |  OK                  | OK                   |                    |
| **G2: Collect Resources**        | Collect all required resources from storages.                                               | `FALLBACK(G2.1, G2.2)` | Perform       | –                                    | OR           |  Achieve. Target condition: all resources were collected.                   | OK                   |                    |
| **G2.1: Standard Collection**    | Perform the standard collection process.                                                    | `;`                    | Perform       | –                                    | AND          |  OK                  | OK                   |                    |
| **G2.2: Low-Battery Collection** | Handle low battery during collection by recharging and re-assigning.                        | `;`                    | Perform       | –                                    | AND          |  OK                  | OK                   |                    |
| **G3: Deliver Resources**        | Deliver collected resources to the destination.                                             | `FALLBACK(G3.1, G3.2)` | Perform       | –                                    | OR           |  Achieve. Target condition: all resources were delivered.                   | OK                   |                    |
| **G3.1: Standard Delivery**      | Perform the standard delivery process.                                                      | `-`                    | Perform       | –                                    | AND          |  OK                  |  OK                  |                    |
| **G3.2: Low-Battery Delivery**   | Handle low battery during delivery by returning to checkpoint and re-assigning.             | `FALLBACK(G3.2.1, G6)` | Perform       | –                                    | OR           |  OK                  |  OK                  |                    |
| **G3.2.1: Return & Re-assign**   | Return resource to checkpoint and assign remaining task to another robot.                   | `;`                    | Perform       | –                                    | AND          |  OK                  |  OK                  |                    |
| **G6: Handle Return Failure**    | Trigger alert and report if resource cannot be returned to checkpoint.                      | `-`                    | Perform       | –                                    | AND          |  OK                  |  OK                  |                    |


---

**Task Model**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1: Navigate to Storage** | Navigate the robot to the storage location where the resource is located. | AND | storage | 1 |
| **AT2: Request Resource** | Send a request message to the storage specifying the required resource. | AND | storage | 1 |
| **AT3: Wait for Retrieval** | Wait until the storage retrieves the requested resource. | AND | storage | 1 |
| **AT4: Navigate to Delivery** | Navigate the robot to the destination location to deliver the resource. | AND | delivery location | 1 |
| **AT5: Return to Checkpoint** | Return the resource to the checkpoint location. | AND | checkpoint | 1 |
| **AT6: Recharge Battery** | Recharge the robot's battery at the charging station. | AND | recharging station | 1 |
| **AT7: Assign Mission** | Assign the remaining collection task to another robot. | AND | – | 1 |
| **AT8: Trigger Alert** | Trigger an alert indicating failure to return to checkpoint. | AND | – | 1 |
| **AT9: Send Report** | Send a report to the sector manager about the failure. | AND | – | 1 |
| **AT10: Navigate to Recharge** | Navigate the robot to the recharging station. | AND | recharging station | 1 |
| **AT12: Assign Remaining Task** | Assign the remaining delivery task to another robot. | AND | – | 1 |

---

### Logical Relationships (Tree Structure)

```
G1 -> G2, G3 [AND][;]
G2 -> G2.1, G2.2 [OR][FALLBACK(G2.1,G2.2)]
G3 -> G3.1, G3.2 [OR][FALLBACK(G3.1,G3.2)]
G3.2 -> G3.2.1, G6 [OR][FALLBACK(G3.2.1,G6)]

G2.1 -> AT1, AT2, AT3 [AND][;]
G2.2 -> AT10, AT6, AT7 [AND][;]
G3.1 -> AT4 [AND][-]
G3.2.1 -> AT5, AT12 [AND][;]
G6 -> AT8, AT9 [AND][-]
```

The model captures the sequential flow of collection then delivery, the fallback handling for low‑battery scenarios, and the failure handling when a robot cannot return to the checkpoint. Parallel execution is represented by the `#` operator where appropriate (e.g., multiple collection/delivery tasks can run concurrently when multiple items are requested).
