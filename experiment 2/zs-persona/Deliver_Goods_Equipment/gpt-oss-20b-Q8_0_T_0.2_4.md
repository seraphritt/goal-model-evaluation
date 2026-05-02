## 1. Goal Model – Tables

| **Name** | **Text** | **Runtime** | **Goal Type** | **Target Condition / Enquired Information** | **Relation** |
|----------|----------|-------------|---------------|-------------------------------------------|--------------|
| **G1** | Complete Resource Delivery Mission | G2;G6;G9;G12;G15 | Achieve | All requested resources delivered to the specified destination. | AND |
| **G2** | Collect Resources | G3;G4;G5 | Perform | – | AND |
| **G3** | Plan Collection Route | – | Query | List of storage locations with waiting times and path distances. | AND |
| **G4** | Request Resources | – | Perform | – | AND |
| **G5** | Retrieve Resources | – | Perform | – | AND |
| **G6** | Deliver Resources | G7;G8 | Perform | – | AND |
| **G7** | Transport Resources to Destination | – | Perform | – | AND |
| **G8** | Coordinate Parallel Delivery | – | Perform | – | AND |
| **G9** | Handle Low Battery during Collection | G10;G11 | Perform | – | AND |
| **G10** | Return to Recharge Station | – | Perform | – | AND |
| **G11** | Assign Mission to Another Robot | – | Perform | – | AND |
| **G12** | Handle Low Battery during Delivery | G13;G14 | Perform | – | AND |
| **G13** | Return Resource to Checkpoint | – | Perform | – | AND |
| **G14** | Assign Remaining Task to Another Robot | – | Perform | – | AND |
| **G15** | Handle Failure to Return Resource to Checkpoint | G16 | Perform | – | AND |
| **G16** | Trigger Alert and Report to Sector Manager | – | Perform | – | AND |

---

## 2. Task Model – Tables

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Compute optimal collection route based on storage availability and path cost. | AND | Robot’s current location (planning module) | 1 |
| **AT2** | Send resource request message to the selected storage. | AND | Robot’s current location | 1 |
| **AT3** | Wait for the storage to retrieve the requested resources. | AND | Robot’s current location | 1 |
| **AT4** | Transport the retrieved resources to the destination location. | AND | Destination (e.g., sterile facility or linen storage) | 1 |
| **AT5** | Coordinate parallel delivery among multiple robots (assign next storage, update schedule). | AND | Robot’s current location | [1,3] |
| **AT6** | Navigate back to the nearest recharge station. | AND | Recharge station | 1 |
| **AT7** | Notify the central scheduler that the robot’s battery is low and the mission is reassigned. | AND | Robot’s current location | 1 |
| **AT8** | Navigate to the nearest checkpoint to deposit the resource. | AND | Checkpoint | 1 |
| **AT9** | Notify the central scheduler that the robot’s battery is low during delivery and the remaining task is reassigned. | AND | Robot’s current location | 1 |
| **AT10** | Send an alert and report to the sector manager about the failure to return the resource to a checkpoint. | AND | Robot’s current location | 1 |

---

## 3. Summary Table (Goals + Tasks)

| **ID** | **Type** | **Title** | **Description** | **Relation** |
|--------|----------|-----------|-----------------|--------------|
| G1 | Goal | Complete Resource Delivery Mission | Achieve delivery of all requested resources to the destination. | AND |
| G2 | Goal | Collect Resources | Perform collection of resources from storages. | AND |
| G3 | Goal | Plan Collection Route | Query for optimal route. | AND |
| AT1 | Task | Compute Optimal Collection Route | Planning task. | AND |
| G4 | Goal | Request Resources | Perform request to storage. | AND |
| AT2 | Task | Send Resource Request Message | Messaging task. | AND |
| G5 | Goal | Retrieve Resources | Perform waiting for retrieval. | AND |
| AT3 | Task | Wait for Resource Retrieval | Waiting task. | AND |
| G6 | Goal | Deliver Resources | Perform delivery of resources. | AND |
| G7 | Goal | Transport Resources to Destination | Perform transport. | AND |
| AT4 | Task | Transport Resources to Destination | Transport task. | AND |
| G8 | Goal | Coordinate Parallel Delivery | Perform coordination. | AND |
| AT5 | Task | Coordinate Parallel Delivery | Coordination task. | AND |
| G9 | Goal | Handle Low Battery during Collection | Perform low‑battery handling. | AND |
| G10 | Goal | Return to Recharge Station | Perform recharge. | AND |
| AT6 | Task | Navigate to Recharge Station | Navigation task. | AND |
| G11 | Goal | Assign Mission to Another Robot | Perform reassignment. | AND |
| AT7 | Task | Notify Central Scheduler of Low Battery | Notification task. | AND |
| G12 | Goal | Handle Low Battery during Delivery | Perform low‑battery handling. | AND |
| G13 | Goal | Return Resource to Checkpoint | Perform checkpoint return. | AND |
| AT8 | Task | Navigate to Checkpoint | Navigation task. | AND |
| G14 | Goal | Assign Remaining Task to Another Robot | Perform reassignment. | AND |
| AT9 | Task | Notify Central Scheduler of Low Battery during Delivery | Notification task. | AND |
| G15 | Goal | Handle Failure to Return Resource to Checkpoint | Perform failure handling. | AND |
| G16 | Goal | Trigger Alert and Report to Sector Manager | Perform alert. | AND |
| AT10 | Task | Send Alert to Sector Manager | Alert task. | AND |

---

## 4. Logical Relationships

- **G1 → G2, G6, G9, G12, G15** [AND]  
- **G2 → G3, G4, G5** [AND]  
- **G3 → AT1** [AND]  
- **G4 → AT2** [AND]  
- **G5 → AT3** [AND]  
- **G6 → G7, G8** [AND]  
- **G7 → AT4** [AND]  
- **G8 → AT5** [AND]  
- **G9 → G10, G11** [AND]  
- **G10 → AT6** [AND]  
- **G11 → AT7** [AND]  
- **G12 → G13, G14** [AND]  
- **G13 → AT8** [AND]  
- **G14 → AT9** [AND]  
- **G15 → G16** [AND]  
- **G16 → AT10** [AND]  

These relationships capture the hierarchical, sequential, and parallel execution structure of the mission, ensuring that each sub‑goal and task is properly linked and that the overall mission can be monitored and executed by a fleet of multi‑robot agents.
