## 1. Goal & Task Tables

| **Name**                                   | **Text**                                                                                                                       | **Runtime**            | **Goal Type** | **Target / Enquired Info** | **Relation**             | **Ground truth I**                                       | **Ground truth C** | **Ground truth E** |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------- | ------------- | -------------------------- | ------------------------ | -------------------------------------------------------- | ------------------ | ------------------ |
| **G1 – Execute Resource Delivery Mission** | Complete the mission of collecting the required resources from storage and delivering them to the requesting agent’s location. | `;` (sequential)       | Perform       | –                          | AND (to G2 & G3)         | OK                                                       | OK                   |                    |
| **G2 – Collection Phase**                  | Gather the requested resources from the appropriate storage locations.                                                         | `FALLBACK(G2.1, G2.2)` | Perform       | –                          | OR (between G2.1 & G2.2) | Achieve. Target condition: all resources were collected. | OK                   |                    |
| **G2.1 – Normal Collection**               | Perform the standard collection steps: navigate to storage, request the resource and wait for retrieval.                       | `-`                    | Perform       | –                          | AND (to AT1-AT3)         | OK                                                       | OK                   |                    |
| **G2.2 – Low-Battery Collection Handling** | Handle the situation where the robot’s battery drops below 10 % during collection.                                             | `-`                    | Perform       | –                          | AND (to AT6 & AT9)       | OK                                                       | OK                   |                    |
| **G3 – Delivery Phase**                    | Deliver the gathered resources to the specified location.                                                                      | `FALLBACK(G3.1, G3.2)` | Perform       | –                          | OR (between G3.1 & G3.2) | Achieve. Target condition: all resources were delivered. | OK                   |                    |
| **G3.1 – Normal Delivery**                 | Perform the standard delivery steps: navigate to the delivery point and hand over the resources.                               | `-`                    | Perform       | –                          | AND (to AT4 & AT5)       | OK                                                       | OK                   |                    |
| **G3.2 – Low-Battery Delivery Handling**   | Handle the situation where the robot’s battery drops below 30 % during delivery.                                               | `-`                    | Perform       | –                          | AND (to AT7, AT9 & AT8)  | OK                                                       | OK                   |                    |


---

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1 – Navigate to Storage** | Robot moves to the storage location where the requested resource is located. | AND (to G2.1) | storage | 1 |
| **AT2 – Request Resource** | Robot sends a precise request to the storage for the needed resource and waits for confirmation. | AND (to G2.1) | storage | 1 |
| **AT3 – Wait for Retrieval** | Robot remains at the storage until the resource is physically retrieved. | AND (to G2.1) | storage | 1 |
| **AT4 – Navigate to Delivery Location** | Robot travels from the storage to the destination where the resource must be delivered. | AND (to G3.1) | delivery location | 1 |
| **AT5 – Deliver Resource** | Robot hands over the resource to the requesting agent or place. | AND (to G3.1) | delivery location | 1 |
| **AT6 – Return to Recharging Station** | Robot returns to the charging station because its battery fell below 10 % during collection. | AND (to G2.2) | recharging station | 1 |
| **AT7 – Return Resource to Checkpoint** | Robot brings the resource back to a checkpoint because its battery fell below 30 % during delivery. | AND (to G3.2) | checkpoint | 1 |
| **AT8 – Trigger Alert & Report** | If the resource cannot be returned to the checkpoint, an alert is sent to the sector manager. | AND (to G3.2) | sector manager | 1 |
| **AT9 – Assign Mission to Another Robot** | The remaining tasks (either collection or delivery) are handed over to a spare robot. | AND (to G2.2 & G3.2) | central command | 1 |

---

## 2. Summary Table (Goals + Tasks)

| **ID** | **Title** | **Type** | **Relation to Parent** | **Runtime** |
|--------|-----------|----------|------------------------|-------------|
| G1 | Execute Resource Delivery Mission | Perform | – | `;` |
| G2 | Collection Phase | Perform | AND (to G1) | `FALLBACK(G2.1, G2.2)` |
| G2.1 | Normal Collection | Perform | OR (to G2) | `-` |
| G2.2 | Low‑Battery Collection Handling | Perform | OR (to G2) | `-` |
| G3 | Delivery Phase | Perform | AND (to G1) | `FALLBACK(G3.1, G3.2)` |
| G3.1 | Normal Delivery | Perform | OR (to G3) | `-` |
| G3.2 | Low‑Battery Delivery Handling | Perform | OR (to G3) | `-` |
| AT1 | Navigate to Storage | Task | AND (to G2.1) | – |
| AT2 | Request Resource | Task | AND (to G2.1) | – |
| AT3 | Wait for Retrieval | Task | AND (to G2.1) | – |
| AT4 | Navigate to Delivery Location | Task | AND (to G3.1) | – |
| AT5 | Deliver Resource | Task | AND (to G3.1) | – |
| AT6 | Return to Recharging Station | Task | AND (to G2.2) | – |
| AT7 | Return Resource to Checkpoint | Task | AND (to G3.2) | – |
| AT8 | Trigger Alert & Report | Task | AND (to G3.2) | – |
| AT9 | Assign Mission to Another Robot | Task | AND (to G2.2 & G3.2) | – |

---

## 3. Logical Relationships (Tree View)

```
G1 -> G2, G3 [AND][;]
   G2 -> G2.1, G2.2 [OR][FALLBACK(G2.1, G2.2)]
      G2.1 -> AT1, AT2, AT3 [AND][#]
      G2.2 -> AT6, AT9 [AND][#]
   G3 -> G3.1, G3.2 [OR][FALLBACK(G3.1, G3.2)]
      G3.1 -> AT4, AT5 [AND][#]
      G3.2 -> AT7, AT9, AT8 [AND][#]
```

- **`[AND]`** means all children must be satisfied for the parent to succeed.  
- **`[OR]`** (fallback) means the parent succeeds if at least one child succeeds; the second child is used only if the first fails.  
- **`[#]`** indicates that the child tasks can be executed in parallel (though in this concrete mission the robot executes them sequentially, the annotation reflects the potential parallelism of the overall system).  

This tree captures the full multi‑robot mission logic, including normal operation, low‑battery contingencies, and the possibility of parallel assignment when multiple items are requested.
