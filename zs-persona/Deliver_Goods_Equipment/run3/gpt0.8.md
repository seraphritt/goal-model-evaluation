**Goal Model – Multi‑Robot Resource Delivery Mission**

| **Name**     | **Text**                                              | **Runtime**                | **Goal Type** | **Target / Enquired Info** | **Relation** | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| ------------ | ----------------------------------------------------- | -------------------------- | ------------- | -------------------------- | ------------ | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1**       | Deliver requested resources                           | `;`                        | Perform       | –                          | –            | OK                                                       | OK                 | OK                                                       |
| **G2**       | Collection phase                                      | `FALLBACK(G2.0, G2.4)`     | Perform       | –                          | AND          | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G2.0**     | Normal collection                                     | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G2.0.1**   | Go to storage                                         | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G2.0.2**   | Request resource                                      | `;`                        | Perform       | –                          | AND          | Query. enquired information: resources to be collected   | OK                 | Query. enquired information: resources to be collected   |
| **G2.0.3**   | Wait for retrieval                                    | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G2.4**     | Battery-low handling (collection)                     | `;`                        | Perform       | –                          | AND          | Ok                                                       | Ok                 | Ok                                                       |
| **G2.4.1**   | Go to recharge station                                | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G2.4.2**   | Assign mission to another robot                       | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3**       | Delivery phase                                        | `FALLBACK(G3.0, G3.4)`     | Perform       | –                          | AND          | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G3.0**     | Normal delivery                                       | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.0.1**   | Deliver resources to destination                      | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.4**     | Battery-low handling (delivery)                       | `FALLBACK(G3.4.1, G3.4.3)` | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.4.1**   | Return resource to checkpoint & assign remaining task | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.4.1.1** | Return resource to checkpoint                         | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.4.1.2** | Assign remaining task to another robot                | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.4**     | Failure handling (battery-low in delivery)            | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.4.3**   | Failure handling                                      | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.4.3.1** | Trigger alert                                         | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |
| **G3.4.3.2** | Send report to sector manager                         | `;`                        | Perform       | –                          | AND          | OK                                                       | OK                 | OK                                                       |

---

### Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Go to storage location | AND | storage | 1 |
| **AT2** | Send request to storage | AND | storage | 1 |
| **AT3** | Wait for retrieval | AND | storage | 1 |
| **AT4** | Deliver resources to destination | AND | destination | 1 |
| **AT5** | Go to recharge station | AND | recharge station | 1 |
| **AT6** | Assign mission to another robot | AND | current location | 1 |
| **AT7** | Return resource to checkpoint | AND | checkpoint | 1 |
| **AT8** | Trigger alert | AND | current location | 1 |
| **AT9** | Assign remaining task to another robot | AND | current location | 1 |
| **AT10** | Send report to sector manager | AND | sector manager | 1 |

---

### Summary Table (Goals + Tasks)

| **ID** | **Type** | **Text** | **Runtime / Relation** |
|--------|----------|----------|------------------------|
| G1 | Goal | Deliver requested resources | `;` |
| G2 | Goal | Collection phase | `FALLBACK(G2.0, G2.4)` |
| G2.0 | Goal | Normal collection | `;` |
| G2.0.1 | Goal | Go to storage | `;` |
| AT1 | Task | Go to storage location | AND |
| G2.0.2 | Goal | Request resource | `;` |
| AT2 | Task | Send request to storage | AND |
| G2.0.3 | Goal | Wait for retrieval | `;` |
| AT3 | Task | Wait for retrieval | AND |
| G2.4 | Goal | Battery‑low handling (collection) | `;` |
| G2.4.1 | Goal | Go to recharge station | `;` |
| AT5 | Task | Go to recharge station | AND |
| G2.4.2 | Goal | Assign mission to another robot | `;` |
| AT6 | Task | Assign mission to another robot | AND |
| G3 | Goal | Delivery phase | `FALLBACK(G3.0, G3.4)` |
| G3.0 | Goal | Normal delivery | `;` |
| G3.0.1 | Goal | Deliver resources to destination | `;` |
| AT4 | Task | Deliver resources to destination | AND |
| G3.4 | Goal | Battery‑low handling (delivery) | `FALLBACK(G3.4.1, G3.4.3)` |
| G3.4.1 | Goal | Return resource to checkpoint & assign remaining task | `;` |
| G3.4.1.1 | Goal | Return resource to checkpoint | `;` |
| AT7 | Task | Return resource to checkpoint | AND |
| G3.4.1.2 | Goal | Assign remaining task to another robot | `;` |
| AT9 | Task | Assign remaining task to another robot | AND |
| G3.4.3 | Goal | Failure handling | `;` |
| G3.4.3.1 | Goal | Trigger alert | `;` |
| AT8 | Task | Trigger alert | AND |
| G3.4.3.2 | Goal | Send report to sector manager | `;` |
| AT10 | Task | Send report to sector manager | AND |

---

### Logical Relationships

```
G1 -> G2, G3 [AND][;]

G2 -> G2.0, G2.4 [AND][FALLBACK(G2.0, G2.4)]

G2.0 -> G2.0.1, G2.0.2, G2.0.3 [AND][;]

G2.0.1 -> AT1 [AND]
G2.0.2 -> AT2 [AND]
G2.0.3 -> AT3 [AND]

G2.4 -> G2.4.1, G2.4.2 [AND][;]
G2.4.1 -> AT5 [AND]
G2.4.2 -> AT6 [AND]

G3 -> G3.0, G3.4 [AND][FALLBACK(G3.0, G3.4)]

G3.0 -> G3.0.1 [AND][;]
G3.0.1 -> AT4 [AND]

G3.4 -> G3.4.1, G3.4.3 [AND][FALLBACK(G3.4.1, G3.4.3)]

G3.4.1 -> G3.4.1.1, G3.4.1.2 [AND][;]
G3.4.1.1 -> AT7 [AND]
G3.4.1.2 -> AT9 [AND]

G3.4.3 -> G3.4.3.1, G3.4.3.2 [AND][;]
G3.4.3.1 -> AT8 [AND]
G3.4.3.2 -> AT10 [AND]
```

This goal‑task decomposition captures the multi‑robot resource delivery mission, explicitly modeling collection, delivery, battery management, failure handling, and parallelism where appropriate.
