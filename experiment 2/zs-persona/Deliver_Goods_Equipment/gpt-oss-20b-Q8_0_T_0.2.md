**Goal Table**

| Name                                             | Text                                                                                                   | Runtime                             | Goal Type | Target Condition / Enquired Information                                                        | Relation | Ground Truth I | Ground Truth G | Consensus |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ----------------------------------- | --------- | ---------------------------------------------------------------------------------------------- | -------- | -------------- | -------------- | --------- |
| **G1: Complete Resource Delivery Mission**       | Ensure all requested resources are delivered to the requesting agent at the specified location.        | `G1.1;G1.2`                         | Achieve   | All requested resources have been delivered to the requesting agent at the specified location. | AND      | Perform               |                |           |
| **G1.1: Collect Resources**                      | Collect required resources from storage.                                                               | `FALLBACK((G1.1.1;G1.1.2), G1.1.3)` | Perform   | –                                                                                              | AND      | Achieve, Target conditon. All resources were collected               |                |           |
| **G1.1.1: Navigate to Storage**                  | Navigate to the storage location to collect resources.                                                 | `-`                                 | Perform   | –                                                                                              | AND      | OK               |                |           |
| **G1.1.2: Send Request and Wait for Retrieval**  | Send request to storage and wait until resources are retrieved.                                        | `-`                                 | Perform   | –                                                                                              | AND      | OK               |                |           |
| **G1.1.3: Handle Low Battery during Collection** | Handle low battery by recharging and assigning mission to another robot.                               | `-`                                 | Perform   | –                                                                                              | AND      |  OK              |                |           |
| **G1.2: Deliver Resources**                      | Deliver collected resources to the requesting location.                                                | `FALLBACK((G1.2.1;G1.2.2), G1.2.3)` | Perform   | –                                                                                              | AND      |   Achieve. Target condition: all resources were delivered             |                |           |
| **G1.2.1: Navigate to Delivery Location**        | Navigate to the delivery location.                                                                     | `-`                                 | Perform   | –                                                                                              | AND      | OK               |                |           |
| **G1.2.2: Transport Resources**                  | Transport resources to the delivery location.                                                          | `-`                                 | Perform   | –                                                                                              | AND      |  OK              |                |           |
| **G1.2.3: Handle Low Battery during Delivery**   | Handle low battery by returning resource to checkpoint, assigning remaining task, or triggering alert. | `-`                                 | Perform   | –                                                                                              | AND      | OK               |                |           |


---

**Task Table**

| Name | Text | Relation | Location | Number of Robots |
|------|------|----------|----------|------------------|
| **AT1: Navigate to Storage** | Robot navigates to the storage location to collect resources. | AND | storage location | 1 |
| **AT2: Send Request and Wait for Retrieval** | Robot sends request to storage and waits until resources are retrieved. | AND | storage location | 1 |
| **AT3: Recharge Battery** | Robot recharges battery at recharging station. | AND | recharging station | 1 |
| **AT4: Navigate to Delivery Location** | Robot navigates to the delivery location. | AND | delivery location | 1 |
| **AT5: Transport Resources** | Robot transports resources to the delivery location. | AND | delivery location | 1 |
| **AT6: Return Resource to Checkpoint** | Robot returns resource to checkpoint. | AND | checkpoint | 1 |
| **AT7: Assign Remaining Task to Another Robot** | Robot assigns remaining task to another robot. | AND | current location | 1 |
| **AT8: Trigger Alert and Report to Sector Manager** | Robot triggers alert and reports to sector manager. | AND | current location | 1 |
| **AT9: Assign Mission to Another Robot** | Robot assigns mission to another robot. | AND | current location | 1 |

---

**Summary Table (Goals + Tasks)**

| ID | Title | Type | Description | Runtime/Relation | Location/Target Condition | Number of Robots |
|----|-------|------|-------------|------------------|---------------------------|------------------|
| G1 | Complete Resource Delivery Mission | Goal | Ensure all requested resources are delivered to the requesting agent at the specified location. | `G1.1;G1.2` | All requested resources have been delivered to the requesting agent at the specified location. | N/A |
| G1.1 | Collect Resources | Goal | Collect required resources from storage. | `FALLBACK((G1.1.1;G1.1.2), G1.1.3)` | – | N/A |
| G1.1.1 | Navigate to Storage | Goal | Navigate to the storage location to collect resources. | – | – | N/A |
| G1.1.2 | Send Request and Wait for Retrieval | Goal | Send request to storage and wait until resources are retrieved. | – | – | N/A |
| G1.1.3 | Handle Low Battery during Collection | Goal | Handle low battery by recharging and assigning mission to another robot. | – | – | N/A |
| G1.2 | Deliver Resources | Goal | Deliver collected resources to the requesting location. | `FALLBACK((G1.2.1;G1.2.2), G1.2.3)` | – | N/A |
| G1.2.1 | Navigate to Delivery Location | Goal | Navigate to the delivery location. | – | – | N/A |
| G1.2.2 | Transport Resources | Goal | Transport resources to the delivery location. | – | – | N/A |
| G1.2.3 | Handle Low Battery during Delivery | Goal | Handle low battery by returning resource to checkpoint, assigning remaining task, or triggering alert. | – | – | N/A |
| AT1 | Navigate to Storage | Task | Robot navigates to the storage location to collect resources. | – | storage location | 1 |
| AT2 | Send Request and Wait for Retrieval | Task | Robot sends request to storage and waits until resources are retrieved. | – | storage location | 1 |
| AT3 | Recharge Battery | Task | Robot recharges battery at recharging station. | – | recharging station | 1 |
| AT4 | Navigate to Delivery Location | Task | Robot navigates to the delivery location. | – | delivery location | 1 |
| AT5 | Transport Resources | Task | Robot transports resources to the delivery location. | – | delivery location | 1 |
| AT6 | Return Resource to Checkpoint | Task | Robot returns resource to checkpoint. | – | checkpoint | 1 |
| AT7 | Assign Remaining Task to Another Robot | Task | Robot assigns remaining task to another robot. | – | current location | 1 |
| AT8 | Trigger Alert and Report to Sector Manager | Task | Robot triggers alert and reports to sector manager. | – | current location | 1 |
| AT9 | Assign Mission to Another Robot | Task | Robot assigns mission to another robot. | – | current location | 1 |

---

**Logical Relationships**

- **G1 → G1.1, G1.2** [AND][sequential]  
- **G1.1 → G1.1.1, G1.1.2, G1.1.3** [AND][FALLBACK((G1.1.1;G1.1.2), G1.1.3)]  
- **G1.2 → G1.2.1, G1.2.2, G1.2.3** [AND][FALLBACK((G1.2.1;G1.2.2), G1.2.3)]  
- **G1.1.1 → AT1** [AND]  
- **G1.1.2 → AT2** [AND]  
- **G1.1.3 → AT3, AT9** [AND]  
- **G1.2.1 → AT4** [AND]  
- **G1.2.2 → AT5** [AND]  
- **G1.2.3 → AT6, AT7, AT8** [AND]  

These relationships capture the hierarchical, sequential, parallel, and fallback structure of the mission in a multi‑robot system.
