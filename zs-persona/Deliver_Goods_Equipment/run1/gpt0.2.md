**Goal Model – Multi‑Robot Resource Collection & Delivery**

| **Name**                                     | **Text**                                                                                                | **Runtime**           | **Goal Type** | **Relation** | **Ground truth I**                                                | **Ground Truth C**                                                | **Ground truth E** |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------- | ------------- | ------------ | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------ |
| **G1: Deliver resources to destination**     | Deliver the requested resources from storage to the specified location.                                 | (G2 ; G3) # (G4 ; G5) | Achieve       | AND          | PERFORM                                                           | perform                                                           |                    |
| **G2: Collect resources**                    | Collect the required resources from storage.                                                            | FALLBACK(G2.1, G2.2)  | Perform       | AND          | Achieve. Target condition: all required resources were collected. | ok |                    |
| **G2.1: Battery-low handling in collection** | Handle low battery during collection by recharging and re-assigning the mission.                        | ;                     | Perform       | AND          | OK                                                                | ok                                                                |                    |
| **G2.2: Normal collection**                  | Perform normal collection steps: navigate, request, wait.                                               | ;                     | Perform       | AND          | OK                                                                | ok                                                                |                    |
| **G3: Deliver resources**                    | Deliver the collected resources to the destination.                                                     | FALLBACK(G3.1, G3.2)  | Perform       | AND          | Achieve. Target condition: all resources were delivered.          | ok          |                    |
| **G3.1: Battery-low handling in delivery**   | Handle low battery during delivery by returning resource to checkpoint and re-assigning remaining task. | ;                     | Perform       | AND          | OK                                                                | ok                                                                |                    |
| **G3.2: Normal delivery**                    | Perform normal delivery steps: navigate to destination, deliver resources.                              | ;                     | Perform       | AND          | OK                                                                | ok                                                                |                    |
| **G4: Parallel collect-deliver tasks**       | Assign multiple robots to parallel collect-deliver tasks for multiple items.                            | –                     | Perform       | AND          | OK                                                                | ok                                                                |                    |
| **G5: Failure handling**                     | Handle failure to return resource to checkpoint by triggering alert and reporting.                      | –                     | Perform       | AND          | OK                                                                | ok                                                                |                    |

---

**Task Model**

| **Name**                           | **Text**                                                                     | **Relation** | **Location**     | **Number of Robots** |
| ---------------------------------- | ---------------------------------------------------------------------------- | ------------ | ---------------- | -------------------- |
| **AT1: Navigate to storage**       | Navigate to the storage location to collect resources.                       | AND          | storage          | 1                    |
| **AT2: Request resource**          | Send request to storage for the specified resources.                         | AND          | storage          | 1                    |
| **AT3: Wait for retrieval**        | Wait until the resources are retrieved from storage.                         | AND          | storage          | 1                    |
| **AT4: Check battery & recharge**  | Check battery level; if below 10 % go to charging station.                   | AND          | current location | 1                    |
| **AT5: Re‑assign mission**         | Assign the remaining collection task to another robot.                       | AND          | current location | 1                    |
| **AT6: Return to checkpoint**      | Return the resource to a checkpoint due to low battery.                      | AND          | checkpoint       | 1                    |
| **AT7: Re‑assign delivery**        | Assign the remaining delivery task to another robot.                         | AND          | current location | 1                    |
| **AT8: Navigate to destination**   | Navigate to the specified destination to deliver resources.                  | AND          | destination      | 1                    |
| **AT9: Deliver resources**         | Deliver the resources to the requesting agent at the destination.            | AND          | destination      | 1                    |
| **AT10: Parallel task assignment** | Assign multiple robots to parallel collect‑deliver tasks for multiple items. | AND          | current location | [2,5]                |
| **AT11: Trigger alert**            | Trigger an alert due to failure to return resource to checkpoint.            | AND          | current location | 1                    |
| **AT12: Send report**              | Send a report to the sector manager about the failure.                       | AND          | current location | 1                    |

---

### Summary of Goals & Tasks

| **Goal** | **Sub‑Goals / Tasks** |
| -------- | --------------------- |
| G1       | G2, G3, G4, G5        |
| G2       | G2.1, G2.2            |
| G2.1     | AT4, AT5              |
| G2.2     | AT1, AT2, AT3         |
| G3       | G3.1, G3.2            |
| G3.1     | AT6, AT7              |
| G3.2     | AT8, AT9              |
| G4       | AT10                  |
| G5       | AT11, AT12            |

---

### Logical Relationships

```
G1 -> G2, G3, G4, G5 [AND][(G2 ; G3) # (G4 ; G5)]

G2 -> G2.1, G2.2 [AND][FALLBACK(G2.1, G2.2)]

G2.1 -> AT4, AT5 [AND][;]

G2.2 -> AT1, AT2, AT3 [AND][;]

G3 -> G3.1, G3.2 [AND][FALLBACK(G3.1, G3.2)]

G3.1 -> AT6, AT7 [AND][;]

G3.2 -> AT8, AT9 [AND][;]

G4 -> AT10 [AND][-]

G5 -> AT11, AT12 [AND][;]
```

*All relations are **AND** unless a fallback is explicitly specified.*
