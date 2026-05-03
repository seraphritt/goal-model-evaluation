## Goal Model – Multi‑Robot Resource Delivery Mission  

| **Name**                                      | **Text**                                                                        | **Runtime**              | **Goal Type** | **Target Condition / Enquired Information**                  | **Relation** | **Ground Truth I** | **Ground Truth G** | **Consensus** |
| --------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------ | ------------- | ------------------------------------------------------------ | ------------ | ------------------ | ------------------ | ------------- |
| **G1: Complete Resource Delivery Mission**    | Ensure all requested resources are delivered to the specified location.         | G2;G3                    | Achieve       | All requested resources delivered to the specified location. | AND          |   Perform                 |                    |               |
| **G2: Collect Resources**                     | Collect all required resources from storage locations.                          | G2.1;G2.2;G2.3;G2.4;G2.5 | Perform       | –                                                            | AND          |   Achieve. target condition: all resources were collected                 |                    |               |
| **G2.1: Plan Collection Route**               | Retrieve waiting-time estimation and path to each storage.                      | AT1                      | Query         | waiting time estimation, path                                | AND          |  OK                  |                    |               |
| **G2.2: Navigate to Storage**                 | Move robot to the designated storage location.                                  | AT2                      | Perform       | –                                                            | AND          |  OK                  |                    |               |
| **G2.3: Send Resource Request**               | Send request to storage for specified resources.                                | AT3                      | Perform       | –                                                            | AND          |  OK                  |                    |               |
| **G2.4: Wait for Resource Retrieval**         | Wait until resources are retrieved from storage.                                | AT4                      | Perform       | –                                                            | AND          |  OK                  |                    |               |
| **G2.5: Monitor Battery During Collection**   | Monitor battery level and handle low battery during collection.                 | FALLBACK(G2.5.1, G2.5.2) | Perform       | –                                                            | AND          |   OK                 |                    |               |
| **G2.5.1: Continue Collecting**               | Continue collection if battery is sufficient.                                   | AT5                      | Perform       | –                                                            | AND          |    OK                |                    |               |
| **G2.5.2: Battery Low Fallback**              | Handle low battery: return to recharging and re-assign mission.                 | AT6;AT7                  | Perform       | –                                                            | AND          |  OK                  |                    |               |
| **G3: Deliver Resources**                     | Deliver collected resources to the requesting agent’s location.                 | G3.1;G3.2;G3.3           | Perform       | –                                                            | AND          |    Achieve. Target condition: all resources were delivered.                |                    |               |
| **G3.1: Navigate to Delivery Location**       | Move robot to the delivery location.                                            | AT8                      | Perform       | –                                                            | AND          |  OK                  |                    |               |
| **G3.2: Transport Resource**                  | Carry resources to the delivery location.                                       | AT9                      | Perform       | –                                                            | AND          |  OK                  |                    |               |
| **G3.3: Monitor Battery During Delivery**     | Monitor battery level and handle low battery during delivery.                   | FALLBACK(G3.3.1, G3.3.2) | Perform       | –                                                            | AND          |   OK                 |                    |               |
| **G3.3.1: Continue Delivery**                 | Continue delivery if battery is sufficient.                                     | AT10                     | Perform       | –                                                            | AND          |    OK                |                    |               |
| **G3.3.2: Battery Low Fallback**              | Handle low battery: return resource to checkpoint and re-assign remaining task. | AT11;AT12                | Perform       | –                                                            | AND          |   OK                 |                    |               |
| **G4: Assign Parallel Collect-Deliver Tasks** | Assign parallel collect-deliver tasks to multiple robots for multiple items.    | AT14                     | Perform       | –                                                            | AND          |   OK                 |                    |               |

---

## Task Model – Concrete Operations  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1: Retrieve waiting time and path estimation** | Retrieve waiting‑time estimation and path to each storage location. | AND | Planning Module | 1 |
| **AT2: Navigate to Storage** | Navigate robot to the specified storage location. | AND | Storage location | 1 |
| **AT3: Send Resource Request** | Send request to storage for specified resources. | AND | Storage location | 1 |
| **AT4: Wait for Resource Retrieval** | Wait until resources are retrieved from storage. | AND | Storage location | 1 |
| **AT5: Monitor Battery Level During Collection** | Monitor battery level during collection phase. | AND | Robot | 1 |
| **AT6: Return to Recharging Station** | Return robot to recharging station due to low battery. | AND | Recharging Station | 1 |
| **AT7: Assign Mission to Another Robot** | Assign the remaining collection mission to another robot. | AND | Robot | 1 |
| **AT8: Navigate to Delivery Location** | Navigate robot to the delivery location. | AND | Delivery location | 1 |
| **AT9: Transport Resource** | Transport resources to the delivery location. | AND | Delivery location | 1 |
| **AT10: Monitor Battery Level During Delivery** | Monitor battery level during delivery phase. | AND | Robot | 1 |
| **AT11: Return Resource to Checkpoint** | Return resource to checkpoint due to low battery. | AND | Checkpoint | 1 |
| **AT12: Assign Remaining Delivery Task to Another Robot** | Assign remaining delivery task to another robot. | AND | Robot | 1 |
| **AT13: Trigger Alert and Report to Sector Manager** | Trigger alert and send report to sector manager if resource cannot be returned to checkpoint. | AND | Robot | 1 |
| **AT14: Assign Parallel Collect‑Deliver Tasks to Multiple Robots** | Assign parallel collect‑deliver tasks to multiple robots for multiple items. | AND | Robot | [2,5] |

---

## Summary Table (Goals + Tasks)

| **ID** | **Type** | **Title** | **Description** | **Relation** | **Runtime / Location** | **Target / Enquired Info** | **Robots** |
|--------|----------|-----------|-----------------|--------------|------------------------|---------------------------|------------|
| G1 | Goal | Complete Resource Delivery Mission | Ensure all requested resources are delivered to the specified location. | AND | G2;G3 | All requested resources delivered to the specified location. | – |
| G2 | Goal | Collect Resources | Collect all required resources from storage locations. | AND | G2.1;G2.2;G2.3;G2.4;G2.5 | – | – |
| G2.1 | Goal | Plan Collection Route | Retrieve waiting‑time estimation and path to each storage. | AND | AT1 | waiting time estimation, path | – |
| G2.2 | Goal | Navigate to Storage | Move robot to the designated storage location. | AND | AT2 | – | – |
| G2.3 | Goal | Send Resource Request | Send request to storage for specified resources. | AND | AT3 | – | – |
| G2.4 | Goal | Wait for Resource Retrieval | Wait until resources are retrieved from storage. | AND | AT4 | – | – |
| G2.5 | Goal | Monitor Battery During Collection | Monitor battery level and handle low battery during collection. | AND | FALLBACK(G2.5.1, G2.5.2) | – | – |
| G2.5.1 | Goal | Continue Collecting | Continue collection if battery is sufficient. | AND | AT5 | – | – |
| G2.5.2 | Goal | Battery Low Fallback | Handle low battery: return to recharging and re‑assign mission. | AND | AT6;AT7 | – | – |
| G3 | Goal | Deliver Resources | Deliver collected resources to the requesting agent’s location. | AND | G3.1;G3.2;G3.3 | – | – |
| G3.1 | Goal | Navigate to Delivery Location | Move robot to the delivery location. | AND | AT8 | – | – |
| G3.2 | Goal | Transport Resource | Carry resources to the delivery location. | AND | AT9 | – | – |
| G3.3 | Goal | Monitor Battery During Delivery | Monitor battery level and handle low battery during delivery. | AND | FALLBACK(G3.3.1, G3.3.2) | – | – |
| G3.3.1 | Goal | Continue Delivery | Continue delivery if battery is sufficient. | AND | AT10 | – | – |
| G3.3.2 | Goal | Battery Low Fallback | Handle low battery: return resource to checkpoint and re‑assign remaining task. | AND | AT11;AT12 | – | – |
| G4 | Goal | Assign Parallel Collect‑Deliver Tasks | Assign parallel collect‑deliver tasks to multiple robots for multiple items. | AND | AT14 | – | – |
| AT1 | Task | Retrieve waiting time and path estimation | Retrieve waiting‑time estimation and path to each storage location. | AND | Planning Module | – | 1 |
| AT2 | Task | Navigate to Storage | Navigate robot to the specified storage location. | AND | Storage location | – | 1 |
| AT3 | Task | Send Resource Request | Send request to storage for specified resources. | AND | Storage location | – | 1 |
| AT4 | Task | Wait for Resource Retrieval | Wait until resources are retrieved from storage. | AND | Storage location | – | 1 |
| AT5 | Task | Monitor Battery Level During Collection | Monitor battery level during collection phase. | AND | Robot | – | 1 |
| AT6 | Task | Return to Recharging Station | Return robot to recharging station due to low battery. | AND | Recharging Station | – | 1 |
| AT7 | Task | Assign Mission to Another Robot | Assign the remaining collection mission to another robot. | AND | Robot | – | 1 |
| AT8 | Task | Navigate to Delivery Location | Navigate robot to the delivery location. | AND | Delivery location | – | 1 |
| AT9 | Task | Transport Resource | Transport resources to the delivery location. | AND | Delivery location | – | 1 |
| AT10 | Task | Monitor Battery Level During Delivery | Monitor battery level during delivery phase. | AND | Robot | – | 1 |
| AT11 | Task | Return Resource to Checkpoint | Return resource to checkpoint due to low battery. | AND | Checkpoint | – | 1 |
| AT12 | Task | Assign Remaining Delivery Task to Another Robot | Assign remaining delivery task to another robot. | AND | Robot | – | 1 |
| AT13 | Task | Trigger Alert and Report to Sector Manager | Trigger alert and send report to sector manager if resource cannot be returned to checkpoint. | AND | Robot | – | 1 |
| AT14 | Task | Assign Parallel Collect‑Deliver Tasks to Multiple Robots | Assign parallel collect‑deliver tasks to multiple robots for multiple items. | AND | Robot | – | [2,5] |

---

## Logical Relationships (Goal ↔ Goal / Task)

```
G1  -> G2, G3 [AND][sequential]
G2  -> G2.1, G2.2, G2.3, G2.4, G2.5 [AND][sequential]
G2.5 -> G2.5.1, G2.5.2 [AND][FALLBACK]
G2.5.1 -> AT5 [AND]
G2.5.2 -> AT6, AT7 [AND]

G3  -> G3.1, G3.2, G3.3 [AND][sequential]
G3.3 -> G3.3.1, G3.3.2 [AND][FALLBACK]
G3.3.1 -> AT10 [AND]
G3.3.2 -> AT11, AT12 [AND]

G4  -> AT14 [AND]

AT1 -> G2.1
AT2 -> G2.2
AT3 -> G2.3
AT4 -> G2.4
AT5 -> G2.5.1
AT6 -> G2.5.2
AT7 -> G2.5.2
AT8 -> G3.1
AT9 -> G3.2
AT10 -> G3.3.1
AT11 -> G3.3.2
AT12 -> G3.3.2
AT13 -> (failure case of AT11)
AT14 -> G4
```

This goal model captures the hierarchical decomposition of the mission into high‑level objectives, sub‑goals, and concrete tasks, while explicitly encoding execution order, parallelism, and fallback behavior for battery‑related contingencies.
