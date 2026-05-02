**Goal Model – Multi‑Robot Resource Collection & Delivery**
| Name       | Text                                              | Runtime                          | Goal Type | Target Condition / Enquired Info | Relation | Ground truth I                                           | Ground truth C | Consensus                                                |
| ---------- | ------------------------------------------------- | -------------------------------- | --------- | -------------------------------- | -------- | -------------------------------------------------------- | -------------- | -------------------------------------------------------- |
| **G1**     | Execute resource collection and delivery mission  | `;`                              | Perform   | –                                | AND      | OK                                                       | OK             | OK                                                       |
| **G2**     | Collection Phase                                  | `(G2.1 ; G2.3 ; FALLBACK(G2.2))` | Perform   | –                                | AND      | Achieve. Target condition: all resources were collected. | OK             | Achieve. Target condition: all resources were collected. |
| **G2.1**   | Navigate to storage, request & wait for resources | `;`                              | Perform   | –                                | AND      | OK                                                       | OK             | OK                                                       |
| **G2.2**   | Handle low battery during collection              | `;`                              | Perform   | –                                | AND      | OK                                                       | OK             | OK                                                       |
| **G2.3**   | Assign multiple robots to parallel storage visits | `#`                              | Perform   | –                                | AND      | OK                                                       | OK             | OK                                                       |
| **G3**     | Delivery Phase                                    | `(G3.1 ; G3.2)`                  | Perform   | –                                | AND      | Achieve. Target condition: all resources were delivered. | OK             | Achieve. Target condition: all resources were delivered. |
| **G3.1**   | Transport resources to destination                | `;`                              | Perform   | –                                | AND      | OK                                                       | OK             | OK                                                       |
| **G3.2**   | Handle low battery during delivery                | `;`                              | Perform   | –                                | AND      | OK                                                       | OK             | OK                                                       |
| **G3.2.1** | Return resource to checkpoint                     | `-`                              | Perform   | –                                | AND      | Ok                                                       | OK             | Ok                                                       |
| **G3.2.2** | Assign remaining task to another robot            | `-`                              | Perform   | –                                | AND      | OK                                                       | OK             | OK                                                       |
| **G3.2.3** | Send alert to sector manager if return fails      | `-`                              | Perform   | –                                | AND      | OK                                                       | OK             | OK                                                       |


---

**Task Model**

| Name | Text | Relation | Location | Number of Robots |
|------|------|----------|----------|------------------|
| **AT1** | Navigate to storage location | AND | *storage* | 1 |
| **AT2** | Send request for resources | AND | *storage* | 1 |
| **AT3** | Wait for resources to be retrieved | AND | *storage* | 1 |
| **AT4** | Navigate to delivery destination | AND | *delivery location* | 1 |
| **AT5** | Transport resources to delivery destination | AND | *delivery location* | 1 |
| **AT6** | Recharge battery at charging station | AND | *charging station* | 1 |
| **AT7** | Return resource to checkpoint | AND | *checkpoint* | 1 |
| **AT8** | Send alert to sector manager | AND | *command center* | 1 |
| **AT9** | Assign mission to another robot | AND | *command center* | 1 |

---

### Summary Table (Goals + Tasks)

| ID | Type | Text | Runtime / Relation | Location / Robots |
|----|------|------|--------------------|-------------------|
| G1 | Goal | Execute resource collection and delivery mission | `;` (sequential) | – |
| G2 | Goal | Collection Phase | `(G2.1 ; G2.3 ; FALLBACK(G2.2))` | – |
| G2.1 | Goal | Navigate to storage, request & wait | `;` | – |
| AT1 | Task | Navigate to storage | AND | storage – 1 robot |
| AT2 | Task | Send request | AND | storage – 1 robot |
| AT3 | Task | Wait for retrieval | AND | storage – 1 robot |
| G2.2 | Goal | Handle low battery during collection | `;` | – |
| AT6 | Task | Recharge battery | AND | charging station – 1 robot |
| AT9 | Task | Assign mission to another robot | AND | command center – 1 robot |
| G2.3 | Goal | Parallel assignment to multiple storages | `#` | – |
| AT9 | Task | Assign mission to another robot | AND | command center – 1 robot |
| G3 | Goal | Delivery Phase | `(G3.1 ; G3.2)` | – |
| G3.1 | Goal | Transport resources to destination | `;` | – |
| AT4 | Task | Navigate to delivery destination | AND | delivery location – 1 robot |
| AT5 | Task | Transport resources | AND | delivery location – 1 robot |
| G3.2 | Goal | Handle low battery during delivery | `;` | – |
| G3.2.1 | Goal | Return resource to checkpoint | `-` | – |
| AT7 | Task | Return resource to checkpoint | AND | checkpoint – 1 robot |
| G3.2.2 | Goal | Assign remaining task to another robot | `-` | – |
| AT9 | Task | Assign mission to another robot | AND | command center – 1 robot |
| G3.2.3 | Goal | Send alert if return fails | `-` | – |
| AT8 | Task | Send alert to sector manager | AND | command center – 1 robot |

---

### Logical Relationships

- **G1 → G2, G3** `[AND][;]`  
- **G2 → G2.1, G2.3, G2.2** `[AND][(G2.1 ; G2.3 ; FALLBACK(G2.2))]`  
- **G2.1 → AT1, AT2, AT3** `[AND][;]`  
- **G2.2 → AT6, AT9** `[AND][;]`  
- **G2.3 → AT9** `[AND][-]`  *(assigns robots to parallel storage visits)*  
- **G3 → G3.1, G3.2** `[AND][;]`  
- **G3.1 → AT4, AT5** `[AND][;]`  
- **G3.2 → G3.2.1, G3.2.2, G3.2.3** `[AND][;]`  
- **G3.2.1 → AT7** `[AND][-]`  
- **G3.2.2 → AT9** `[AND][-]`  
- **G3.2.3 → AT8** `[AND][-]`  

This goal‑task decomposition captures the full multi‑robot mission: sequential collection and delivery phases, battery‑aware fallback handling, parallel robot assignment for multiple storages, and alerting mechanisms for failures.
