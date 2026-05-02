## Goal Model – Multi‑Robot Resource‑Collection & Delivery Mission  

| **Name**     | **Text**                                                                              | **Runtime**                   | **Goal Type** | **Target Condition / Enquired Info**                           | **Relation** | **Ground truth I**                                       | **Ground truth C** | **Consensus**                                            |
| ------------ | ------------------------------------------------------------------------------------- | ----------------------------- | ------------- | -------------------------------------------------------------- | ------------ | -------------------------------------------------------- | ------------------ | -------------------------------------------------------- |
| **G1**       | Achieve mission completion – all requested resources are delivered to the destination | `;` (sequential)              | Achieve       | *All requested resources delivered to the specified location.* | –            | Perform                                                  | Perform            | Perform                                                  |
| **G1.1**     | Perform collection of all requested resources                                         | `#` (parallel)                | Perform       | –                                                              | AND          | Achieve. Target condition: all resources were collected. | OK                 | Achieve. Target condition: all resources were collected. |
| **G1.2**     | Perform delivery of all collected resources                                           | `#` (parallel)                | Perform       | –                                                              | AND          | Achieve. Target condition: all resources were delivered. | OK                 | Achieve. Target condition: all resources were delivered. |
| **G1.1.1**   | Collect resource from **Storage A**                                                   | `FALLBACK(G1.1.1.1,G1.1.1.2)` | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.1.1.1** | Normal collection sequence for Storage A                                              | `;` (sequential)              | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.1.1.2** | Low-battery handling during collection for Storage A                                  | `;` (sequential)              | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.1.2**   | Collect resource from **Storage B**                                                   | `FALLBACK(G1.1.2.1,G1.1.2.2)` | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.1.2.1** | Normal collection sequence for Storage B                                              | `;` (sequential)              | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.1.2.2** | Low-battery handling during collection for Storage B                                  | `;` (sequential)              | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.2.1**   | Deliver resource from Storage A                                                       | `FALLBACK(G1.2.1.1,G1.2.1.2)` | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.2.1.1** | Normal delivery sequence for resource from Storage A                                  | `;` (sequential)              | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.2.1.2** | Low-battery handling during delivery for resource from Storage A                      | `;` (sequential)              | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.2.2**   | Deliver resource from Storage B                                                       | `FALLBACK(G1.2.2.1,G1.2.2.2)` | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.2.2.1** | Normal delivery sequence for resource from Storage B                                  | `;` (sequential)              | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |
| **G1.2.2.2** | Low-battery handling during delivery for resource from Storage B                      | `;` (sequential)              | Perform       | –                                                              | AND          | OK                                                       | OK                 | OK                                                       |

---

## Task Model – Concrete Robot Actions  

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Navigate to **Storage A** | AND | Storage A | 1 |
| **AT2** | Send request to **Storage A** | AND | Storage A | 1 |
| **AT3** | Wait for retrieval from **Storage A** | AND | Storage A | 1 |
| **AT4** | Navigate to **Recharge Station** (battery low during collection from A) | AND | Recharge Station | 1 |
| **AT5** | Recharge battery at **Recharge Station** | AND | Recharge Station | 1 |
| **AT6** | Assign mission to another robot (after recharging at A) | AND | Recharge Station | 1 |
| **AT7** | Navigate to **Storage B** | AND | Storage B | 1 |
| **AT8** | Send request to **Storage B** | AND | Storage B | 1 |
| **AT9** | Wait for retrieval from **Storage B** | AND | Storage B | 1 |
| **AT10** | Navigate to **Recharge Station** (battery low during collection from B) | AND | Recharge Station | 1 |
| **AT11** | Recharge battery at **Recharge Station** | AND | Recharge Station | 1 |
| **AT12** | Assign mission to another robot (after recharging at B) | AND | Recharge Station | 1 |
| **AT13** | Navigate to **Destination** (deliver resource from A) | AND | Destination | 1 |
| **AT14** | Transport resources to **Destination** (from A) | AND | Destination | 1 |
| **AT15** | Navigate to **Destination** (deliver resource from B) | AND | Destination | 1 |
| **AT16** | Transport resources to **Destination** (from B) | AND | Destination | 1 |
| **AT17** | Return resource to **Checkpoint** (battery low during delivery from A) | AND | Checkpoint | 1 |
| **AT18** | Assign remaining delivery task to another robot (from A) | AND | Checkpoint | 1 |
| **AT19** | Trigger alert to **Sector Manager** (failed checkpoint return from A) | AND | Checkpoint | 1 |
| **AT20** | Return resource to **Checkpoint** (battery low during delivery from B) | AND | Checkpoint | 1 |
| **AT21** | Assign remaining delivery task to another robot (from B) | AND | Checkpoint | 1 |
| **AT22** | Trigger alert to **Sector Manager** (failed checkpoint return from B) | AND | Checkpoint | 1 |

---

## Summary Table – Goals & Tasks  

| **ID** | **Type** | **Description** | **Relation to Parent** | **Runtime** |
|--------|----------|-----------------|------------------------|-------------|
| G1 | Goal – Achieve | Mission completion | – | `;` |
| G1.1 | Goal – Perform | Collection | AND | `#` |
| G1.2 | Goal – Perform | Delivery | AND | `#` |
| G1.1.1 | Goal – Perform | Collect from Storage A | AND | `FALLBACK(G1.1.1.1,G1.1.1.2)` |
| G1.1.1.1 | Goal – Perform | Normal collection A | AND | `;` |
| G1.1.1.2 | Goal – Perform | Low‑battery collection A | AND | `;` |
| G1.1.2 | Goal – Perform | Collect from Storage B | AND | `FALLBACK(G1.1.2.1,G1.1.2.2)` |
| G1.1.2.1 | Goal – Perform | Normal collection B | AND | `;` |
| G1.1.2.2 | Goal – Perform | Low‑battery collection B | AND | `;` |
| G1.2.1 | Goal – Perform | Deliver from Storage A | AND | `FALLBACK(G1.2.1.1,G1.2.1.2)` |
| G1.2.1.1 | Goal – Perform | Normal delivery A | AND | `;` |
| G1.2.1.2 | Goal – Perform | Low‑battery delivery A | AND | `;` |
| G1.2.2 | Goal – Perform | Deliver from Storage B | AND | `FALLBACK(G1.2.2.1,G1.2.2.2)` |
| G1.2.2.1 | Goal – Perform | Normal delivery B | AND | `;` |
| G1.2.2.2 | Goal – Perform | Low‑battery delivery B | AND | `;` |
| AT1‑AT22 | Tasks | Concrete robot actions | AND | – |

---

## Logical Relationships (Illustrative)

```
G1  ->  G1.1, G1.2          [AND][;]
G1.1 ->  G1.1.1, G1.1.2     [AND][#]
G1.1.1 ->  G1.1.1.1, G1.1.1.2   [AND][FALLBACK(G1.1.1.1,G1.1.1.2)]
G1.1.1.1 ->  AT1, AT2, AT3    [AND][;]
G1.1.1.2 ->  AT4, AT5, AT6    [AND][;]
G1.1.2 ->  G1.1.2.1, G1.1.2.2   [AND][FALLBACK(G1.1.2.1,G1.1.2.2)]
G1.1.2.1 ->  AT7, AT8, AT9    [AND][;]
G1.1.2.2 ->  AT10, AT11, AT12 [AND][;]
G1.2  ->  G1.2.1, G1.2.2     [AND][#]
G1.2.1 ->  G1.2.1.1, G1.2.1.2   [AND][FALLBACK(G1.2.1.1,G1.2.1.2)]
G1.2.1.1 ->  AT13, AT14     [AND][;]
G1.2.1.2 ->  AT17, AT18, AT19 [AND][;]
G1.2.2 ->  G1.2.2.1, G1.2.2.2   [AND][FALLBACK(G1.2.2.1,G1.2.2.2)]
G1.2.2.1 ->  AT15, AT16     [AND][;]
G1.2.2.2 ->  AT20, AT21, AT22 [AND][;]
```

This model captures:

* **Sequential phases** (collection → delivery).  
* **Parallelism** (multiple storages or deliveries executed concurrently).  
* **Fallbacks** for low‑battery handling.  
* **Explicit tasks** with location and robot count for each robot to execute.  
* **Goal‑type annotations** (Achieve for overall mission, Perform for all operational sub‑goals).  

Feel free to extend the model with additional storages, checkpoints, or robot counts as required by the deployment environment.
