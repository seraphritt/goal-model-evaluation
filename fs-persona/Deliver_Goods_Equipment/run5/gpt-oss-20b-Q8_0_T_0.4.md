**Goal Model – Multi‑Robot Resource Delivery Mission**

| **Name** | **Text**                                                                | **Runtime**            | **Goal Type** | **Target / Enquired** | **Relation** | **Ground truth I**                                       | **Ground truth C** | **Ground truth E** |
| -------- | ----------------------------------------------------------------------- | ---------------------- | ------------- | --------------------- | ------------ | -------------------------------------------------------- | ------------------ | ------------------ |
| **G1**   | Deliver the requested resources to the specified destination            | `#`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G2**   | Collection Phase                                                        | `;`                    | Perform       | –                     | AND          | Achieve. Target condition: all resources were collected. |  OK                  |                    |
| **G2.1** | Determine optimal storage order (waiting + path)                        | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G2.2** | Navigate to the selected storage                                        | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G2.3** | Request the specified resources                                         | `-`                    | Perform       | –                     | AND          | Query. Enqueried information: resources to be collected  |  OK                  |                    |
| **G2.4** | Wait until the resources are retrieved                                  | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G2.5** | Handle low battery (10 %) during collection                             | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G3**   | Delivery Phase                                                          | `;`                    | Perform       | –                     | AND          | Achieve. Target condition: all resources were delivered. |  OK                  |                    |
| **G3.1** | Navigate to the destination                                             | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G3.2** | Deliver the resources (multiple runs if needed)                         | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G3.3** | Handle low battery (30 %) during delivery                               | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G4**   | Battery-Management Sub-system                                           | `FALLBACK(G4.1, G4.2)` | Perform       | –                     | OR           | OK                                                       |  OK                  |                    |
| **G4.1** | Recharge robot when battery < 10 % (collection phase)                   | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G4.2** | Return resource to checkpoint when battery < 30 % (delivery phase)      | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G5**   | Failure-Handling Sub-system                                             | `;`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G5.1** | Trigger alert if the robot fails to return the resource to a checkpoint | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G5.2** | Send a report to the sector manager                                     | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G6**   | Parallel-Task Assignment                                                | `;`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G6.1** | Assign multiple robots to parallel collect-deliver tasks                | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |
| **G6.2** | Reduce overall mission time by parallelisation                          | `-`                    | Perform       | –                     | AND          | OK                                                       |  OK                  |                    |


---

### Task Nodes

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Navigate to the selected storage location | AND | Storage | 1 |
| **AT2** | Send a request message to the storage with the exact resource specification | AND | Storage | 1 |
| **AT3** | Wait until the storage confirms that the resources have been retrieved | AND | Storage | 1 |
| **AT4** | Navigate to the destination location where the resources are required | AND | Destination | 1 |
| **AT5** | Deliver the retrieved resources to the destination (may involve multiple runs) | AND | Destination | 1 |
| **AT6** | Return to the recharging station and recharge the robot’s battery | AND | RechargeStation | 1 |
| **AT7** | Return the partially delivered resource to a checkpoint when battery < 30 % | AND | Checkpoint | 1 |
| **AT8** | Assign the remaining mission portion to another robot (robot hand‑over) | AND | CurrentLocation | 1 |
| **AT9** | Trigger an alert when the robot fails to return a resource to a checkpoint | AND | System | 1 |
| **AT10** | Send a detailed report to the sector manager after a failure event | AND | SectorManager | 1 |
| **AT11** | Distribute parallel collect‑deliver tasks among available robots to minimise total mission time | AND | System | [2, 5] |

---

### Logical Relationships (Tree Summary)

```
G1 -> G2, G3, G4, G5, G6 [AND][#]

G2 -> G2.1, G2.2, G2.3, G2.4, G2.5 [AND][;]
G2.2 -> AT1 [AND]
G2.3 -> AT2 [AND]
G2.4 -> AT3 [AND]
G2.5 -> AT6, AT8 [AND]

G3 -> G3.1, G3.2, G3.3 [AND][;]
G3.1 -> AT4 [AND]
G3.2 -> AT5 [AND]
G3.3 -> AT7, AT8 [AND]

G4 -> G4.1, G4.2 [OR][FALLBACK(G4.1,G4.2)]
G4.1 -> AT6 [AND]
G4.2 -> AT7 [AND]

G5 -> G5.1, G5.2 [AND][;]
G5.1 -> AT9 [AND]
G5.2 -> AT10 [AND]

G6 -> G6.1, G6.2 [AND][;]
G6.1 -> AT11 [AND]
```

> **Explanation**  
> * **G1** is the top‑level perform goal that must be achieved by executing all five sub‑goals.  
> * **G2** and **G3** are sequential sub‑goals (runtime `;`) that contain the concrete tasks for collection and delivery respectively.  
> * **G4** uses a **fallback** to decide whether to recharge (10 %) or return the resource to a checkpoint (30 %) based on the robot’s battery level.  
> * **G5** handles failure situations; both tasks must succeed.  
> * **G6** enables parallel assignment of robots to reduce total mission time.  

All tasks are simple, concrete actions that can be directly assigned to a single robot or a small group, and each is linked to the appropriate goal via an **AND** relation. This goal model captures the mission’s operational flow, fault tolerance, and parallelisation strategies for a multi‑robot system.
