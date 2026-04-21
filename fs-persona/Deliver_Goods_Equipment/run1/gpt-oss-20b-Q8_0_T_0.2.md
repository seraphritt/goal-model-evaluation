**Goal‑Model Tables**

| **Name**   | **Text**                          | **Runtime** | **Goal Type** | **Enquired / Target** | **Relation** | **Ground truth I**                                       | **Ground truth C** | **Ground truth E** |
| ---------- | --------------------------------- | ----------- | ------------- | --------------------- | ------------ | -------------------------------------------------------- | ------------------ | ------------------ |
| **G1**     | Collect and Deliver Resources     | `;`         | Perform       | –                     | –            | OK                                                       | OK                   |                    |
| **G1.1**   | Collection Phase                  | `#`         | Perform       | –                     | –            | Achieve. Target condition: all resources were collected. | OK                   |                    |
| **G1.1.1** | Determine Order of Storage Visits | `-`         | Query         | *Storage visit order* | AND          | OK                                                       | Perform                   |                    |
| **G1.1.2** | Request Resources from Storage    | `;`         | Perform       | –                     | AND          | Query. Enqueried information: resources to be collected  | OK                   |                    |
| **G1.1.3** | Battery-Low Handling (Collection) | `-`         | Perform       | –                     | AND          | OK                                                       | OK                   |                    |
| **G1.2**   | Delivery Phase                    | `#`         | Perform       | –                     | –            | Achieve. Target condition: all resources were delivered. | OK                   |                    |
| **G1.2.1** | Deliver Resources to Destination  | `;`         | Perform       | –                     | AND          | OK                                                       | OK                   |                    |
| **G1.2.2** | Battery-Low Handling (Delivery)   | `-`         | Perform       | –                     | AND          | OK                                                       | OK                   |                    |
| **G1.3**   | Failure Handling                  | `;`         | Perform       | –                     | AND          | OK                                                       | OK                   |                    |
| **G1.3.1** | Trigger Alert & Report            | `-`         | Perform       | –                     | AND          | OK                                                       | OK                   |                    |


---

**Task‑Model Tables**

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Compute Storage Visit Order | AND | *Planning Module* | 1 |
| **AT2** | Send Request to Storage | AND | *Storage Location* | [1,5] |
| **AT3** | Wait for Resources Retrieval | AND | *Storage Location* | 1 |
| **AT4** | Transport Resources to Destination | AND | *Delivery Destination* | 1 |
| **AT5** | (Optional) Return to Checkpoint | AND | *Checkpoint* | 1 |
| **AT6** | Go to Recharge Station | AND | *Recharge Station* | 1 |
| **AT7** | Assign Mission to Another Robot | AND | *Current Location* | 1 |
| **AT8** | Return Resource to Checkpoint | AND | *Checkpoint* | 1 |
| **AT9** | Alert Sector Manager | AND | *Sector Manager* | 1 |
| **AT10** | Send Failure Report | AND | *Sector Manager* | 1 |

---

**Summary Table (Goals + Tasks)**

| **ID** | **Title** | **Type** | **Text / Role** | **Runtime / Location** | **Relation** | **Other Attributes** |
|--------|-----------|----------|-----------------|------------------------|--------------|----------------------|
| G1 | Collect & Deliver Resources | Goal | Main mission objective | `;` | – | – |
| G1.1 | Collection Phase | Goal | Gather all required items | `#` | – | – |
| AT1 | Compute Storage Order | Task | Planning step | – | AND | Location: Planning Module, Robots: 1 |
| G1.1.1 | Determine Order | Goal | Query storage visit order | `-` | AND | – |
| G1.1.2 | Request Resources | Goal | Request & wait | `;` | AND | – |
| AT2 | Send Request | Task | Send message to storage | – | AND | Location: Storage, Robots: [1,5] |
| AT3 | Wait for Retrieval | Task | Block until resources arrive | – | AND | Location: Storage, Robots: 1 |
| G1.1.3 | Battery‑Low Handling | Goal | Low‑battery fallback | `-` | AND | – |
| AT6 | Go to Recharge | Task | Move to recharge station | – | AND | Location: Recharge Station, Robots: 1 |
| AT7 | Assign to Another Robot | Task | Re‑assign mission | – | AND | Location: Current, Robots: 1 |
| G1.2 | Delivery Phase | Goal | Deliver items to destination | `#` | – | – |
| G1.2.1 | Deliver to Destination | Goal | Transport resources | `;` | AND | – |
| AT4 | Transport to Destination | Task | Move items | – | AND | Location: Destination, Robots: 1 |
| G1.2.2 | Battery‑Low Handling | Goal | Low‑battery fallback | `-` | AND | – |
| AT8 | Return to Checkpoint | Task | Return resource | – | AND | Location: Checkpoint, Robots: 1 |
| G1.3 | Failure Handling | Goal | Handle delivery failure | `;` | AND | – |
| G1.3.1 | Trigger Alert & Report | Goal | Notify sector manager | `-` | AND | – |
| AT9 | Alert Sector Manager | Task | Send alert | – | AND | Location: Sector Manager, Robots: 1 |
| AT10 | Send Failure Report | Task | Send report | – | AND | Location: Sector Manager, Robots: 1 |

---

**Logical Relationships**

- **G1 → G1.1, G1.2, G1.3** [AND][;]  
- **G1.1 → G1.1.1, G1.1.2, G1.1.3** [AND][#]  
- **G1.1.2 → AT2, AT3** [AND][;]  
- **G1.1.3 → AT6, AT7** [AND][;]  
- **G1.2 → G1.2.1, G1.2.2** [AND][#]  
- **G1.2.1 → AT4** [AND][-]  
- **G1.2.2 → AT8** [AND][-]  
- **G1.3 → G1.3.1** [AND][;]  
- **G1.3.1 → AT9, AT10** [AND][;]  

These relations capture the hierarchical AND/OR structure, the execution order (parallel vs sequential), and the fallback behaviour as required by the mission description.
