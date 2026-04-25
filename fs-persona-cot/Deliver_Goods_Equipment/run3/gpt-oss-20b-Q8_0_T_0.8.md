**Goal Model – Multi‑Robot Resource Delivery Mission**

| Name                                      | Text                                                                                                                                | Runtime                                 | Goal Type | Target Condition / Enquired Info | Relation                                  | Justification                                                                                                                | Ground truth I                                          | Ground truth C | Ground truth E |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | --------- | -------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------- | -------------- |
| **G1: Execute Resource Delivery Mission** | The robot must collect required resources from storage and deliver them to the requesting agent at the specified location.          | `;` (sequential)                        | Perform   | –                                | AND (between G2 & G3)                     | The mission is naturally split into a collection phase followed by a delivery phase; both must succeed in order.             | OK                                                      | Ok               |                |
| **G2: Collect Resources**                 | The robot navigates to storage, requests, and waits for resources.                                                                  | `FALLBACK(AND(G2.1, G2.2, G2.3), G2.4)` | Perform   | –                                | AND between G2.1-G2.3, fallback to G2.4   | All collection sub-steps must succeed; if battery drops below 10 % the fallback branch handles re-charging and reassignment. | Achieve. Target condition: all resources were collected | Ok               |                |
| G2.1                                      | **Navigate to Storage**                                                                                                             | –                                       | Perform   | –                                | AND                                       | Navigation must occur before a request can be made.                                                                          | OK                                                      | Ok               |                |
| G2.2                                      | **Request Resource**                                                                                                                | –                                       | Perform   | –                                | AND                                       | The robot must request the exact resources before they can be retrieved.                                                     | Query. Enquired information: resources to be collected  | Ok               |                |
| G2.3                                      | **Wait for Retrieval**                                                                                                              | –                                       | Perform   | –                                | AND                                       | The robot must wait until the storage confirms that the resources have been fetched.                                         | OK                                                      | Ok               |                |
| G2.4                                      | **Handle Low Battery During Collection**                                                                                            | –                                       | Perform   | –                                | AND                                       | If battery < 10 % the robot must recharge and hand off the mission to another robot.                                         | OK                                                      | Ok               |                |
| **G3: Deliver Resources**                 | The robot transports resources to the destination, handling low battery by returning to a checkpoint and assigning remaining tasks. | `FALLBACK(AND(G3.1, G3.3), G3.2)`       | Perform   | –                                | AND between G3.1 & G3.3, fallback to G3.2 | Successful delivery requires transport and task reassignment; a low-battery failure triggers the checkpoint branch.          | Achieve. Target condition: all resources were delivered | Ok               |                |
| G3.1                                      | **Transport to Destination**                                                                                                        | –                                       | Perform   | –                                | AND                                       | Core action of carrying the resources.                                                                                       | OK                                                      | Ok               |                |
| G3.3                                      | **Assign Remaining Task**                                                                                                           | –                                       | Perform   | –                                | AND                                       | After a partial delivery the robot must hand over the rest to another robot.                                                 | OK                                                      | Ok               |                |
| G3.2                                      | **Return to Checkpoint Due to Low Battery**                                                                                         | –                                       | Perform   | –                                | AND                                       | If battery < 30 % the robot must safely return the resource to a checkpoint before re-assignment.                            | OK                                                      | Ok               |                |
| **G4: Parallel Task Assignment**          | Identify items, allocate robots, schedule tasks, and execute them concurrently to reduce mission time.                              | `;` (sequential)                        | Perform   | –                                | AND between G4.1-G4.4                     | Each preparatory step must occur before the next; only after scheduling can parallel execution begin.                        | OK                                                      | Ok               |                |
| G4.1                                      | **Identify Required Items**                                                                                                         | –                                       | Perform   | –                                | AND                                       | The system must know which items and storages are needed before allocation.                                                  | OK                                                      | Ok               |                |
| G4.2                                      | **Allocate Robots**                                                                                                                 | –                                       | Perform   | –                                | AND                                       | Robots must be assigned to each collection-delivery pair before scheduling.                                                  | Ok                                                      | Ok               |                |
| G4.3                                      | **Schedule Tasks**                                                                                                                  | –                                       | Perform   | –                                | AND                                       | A schedule is required to orchestrate parallelism.                                                                           | OK                                                      | Ok               |                |
| G4.4                                      | **Execute Parallel Tasks**                                                                                                          | –                                       | Perform   | –                                | AND                                       | Robots concurrently perform their assigned tasks.                                                                            | Ok                                                      | Ok               |                |
| **G5: Handle Failure**                    | Trigger an alert and report to the sector manager if a robot fails to return a resource to a checkpoint.                            | `;` (sequential)                        | Perform   | –                                | AND between G5.1 & G5.2                   | Alert must be raised before a report is sent.                                                                                | OK                                                      | Ok               |                |
| G5.1                                      | **Trigger Alert**                                                                                                                   | –                                       | Perform   | –                                | AND                                       | Immediate notification of the failure.                                                                                       | OK                                                      | Ok               |                |
| G5.2                                      | **Send Report to Sector Manager**                                                                                                   | –                                       | Perform   | –                                | AND                                       | Documentation of the failure for higher-level oversight.                                                                     | OK                                                      | Ok               |                |


---

### Task Model

| Name | Text | Relation | Location | Number of Robots | Justification |
|------|------|----------|----------|------------------|---------------|
| **AT1: Navigate to Storage** | Robot moves to the storage location where the resources are located. | AND (under G2.1) | Storage | 1 | A single robot must physically reach the storage. |
| **AT2: Request Resource** | Robot sends a message to the storage specifying the required resources. | AND (under G2.2) | Storage | 1 | Direct communication is performed by the same robot. |
| **AT3: Wait for Retrieval** | Robot waits until the storage confirms that the resources have been fetched. | AND (under G2.3) | Storage | 1 | The robot must remain until confirmation. |
| **AT4: Recharge at Station** | Robot returns to the charging station to recharge its battery. | AND (under G2.4) | Charging Station | 1 | Re‑charging is a single‑robot action. |
| **AT5: Transport to Destination** | Robot carries the resources to the specified destination location. | AND (under G3.1) | Destination | 1 | The robot physically moves the load. |
| **AT6: Return to Checkpoint** | Robot returns the resource to a checkpoint due to low battery. | AND (under G3.2) | Checkpoint | 1 | Safe return is handled by the same robot. |
| **AT7: Assign Remaining Task** | Robot assigns the remaining resources to another robot. | AND (under G3.3) | Current location / Command Center | 1 | Coordination is performed by the robot that still holds the resource. |
| **AT8: Identify Required Items** | System identifies items and storages needed for the mission. | AND (under G4.1) | Command Center | 1 | Manager agent performs the identification. |
| **AT9: Allocate Robots** | System assigns specific robots to each collection‑delivery pair. | AND (under G4.2) | Command Center | 1 | Allocation logic is centralized. |
| **AT10: Schedule Tasks** | System creates an execution schedule for all robots. | AND (under G4.3) | Command Center | 1 | Scheduling is a shared planning step. |
| **AT11: Execute Parallel Tasks** | Multiple robots concurrently execute their assigned collection‑delivery tasks. | AND (under G4.4) | Various storages/destinations | [1,n] | Parallel execution reduces overall mission time. |
| **AT12: Trigger Alert** | Robot triggers an alert upon failure to return a resource to the checkpoint. | AND (under G5.1) | Current location | 1 | Immediate notification is required. |
| **AT13: Send Report to Sector Manager** | Robot sends a failure report to the sector manager. | AND (under G5.2) | Command Center | 1 | Reporting is handled by the robot that detected the failure. |

---

## Summary Table – Goals & Tasks

| Goal ID | Goal Name | Task ID | Task Name |
|---------|------------|---------|-----------|
| G1 | Execute Resource Delivery Mission | – | – |
| G2 | Collect Resources | AT1 | Navigate to Storage |
|  |  | AT2 | Request Resource |
|  |  | AT3 | Wait for Retrieval |
|  |  | AT4 | Recharge at Station |
| G3 | Deliver Resources | AT5 | Transport to Destination |
|  |  | AT6 | Return to Checkpoint |
|  |  | AT7 | Assign Remaining Task |
| G4 | Parallel Task Assignment | AT8 | Identify Required Items |
|  |  | AT9 | Allocate Robots |
|  |  | AT10 | Schedule Tasks |
|  |  | AT11 | Execute Parallel Tasks |
| G5 | Handle Failure | AT12 | Trigger Alert |
|  |  | AT13 | Send Report to Sector Manager |

---

## Logical Relationships

| Parent Goal | Children | Relation & Runtime | Justification |
|-------------|----------|--------------------|---------------|
| **G1** | G2, G3 | **AND** `[;]` (sequential) | Collection must complete before delivery; both are required for mission success. |
| **G2** | G2.1, G2.2, G2.3, G2.4 | **AND** `[FALLBACK(AND(G2.1,G2.2,G2.3), G2.4)]` | All collection sub‑steps are mandatory; if battery < 10 % the fallback branch handles re‑charging and reassignment. |
| **G2.1** | AT1 | **AND** `[-]` | Single navigation task. |
| **G2.2** | AT2 | **AND** `[-]` | Single request task. |
| **G2.3** | AT3 | **AND** `[-]` | Single wait task. |
| **G2.4** | AT4 | **AND** `[-]` | Single recharge task. |
| **G3** | G3.1, G3.3, G3.2 | **AND** `[FALLBACK(AND(G3.1,G3.3), G3.2)]` | Transport and reassignment are needed; low‑battery fallback returns to checkpoint. |
| **G3.1** | AT5 | **AND** `[-]` | Single transport task. |
| **G3.3** | AT7 | **AND** `[-]` | Single assignment task. |
| **G3.2** | AT6 | **AND** `[-]` | Single checkpoint return task. |
| **G4** | G4.1, G4.2, G4.3, G4.4 | **AND** `[;]` (sequential) | Each preparatory step must finish before the next; only after scheduling can parallel execution commence. |
| **G4.1** | AT8 | **AND** `[-]` | Single identification task. |
| **G4.2** | AT9 | **AND** `[-]` | Single allocation task. |
| **G4.3** | AT10 | **AND** `[-]` | Single scheduling task. |
| **G4.4** | AT11 | **AND** `[-]` | Single parallel execution task. |
| **G5** | G5.1, G5.2 | **AND** `[;]` (sequential) | Alert must precede report. |
| **G5.1** | AT12 | **AND** `[-]` | Single alert task. |
| **G5.2** | AT13 | **AND** `[-]` | Single reporting task. |

---

### Overall Rationale

1. **Sequential vs. Parallel** – The mission naturally decomposes into a *collection* phase followed by a *delivery* phase; thus G1 uses a sequential runtime (`;`). Within each phase, the necessary sub‑steps must occur in order (navigation → request → wait → possibly recharge). Parallelism is only introduced at the *task‑assignment* level (G4) where multiple robots can operate concurrently, captured by a sequential ordering of the preparatory sub‑goals but a single parallel execution task (AT11) that actually runs robots in parallel.

2. **Fallback Mechanisms** – Battery thresholds are explicit failure points. We model them as *fallback* branches: if the normal path fails (e.g., battery < 10 % during collection), the fallback sub‑goal (G2.4) takes over. Similarly, low battery during delivery triggers G3.2. This mirrors the mission’s description of re‑assignment and safe return.

3. **Task Granularity** – Each leaf goal has one concrete task. This keeps the model simple while still capturing the operational steps. Tasks are linked to their parent goal with an AND relation because a goal is satisfied only when its task succeeds.

4. **Robot Allocation** – The parallel assignment goal (G4) and its tasks (AT8‑AT11) explicitly capture the requirement that *multiple robots can be assigned to parallel collect‑deliver tasks* to reduce overall mission time.

5. **Failure Handling** – G5 and its tasks represent the *alert* and *report* sequence mandated when a robot cannot return a resource to a checkpoint.

This goal‑task structure provides a clear, hierarchical, and executable plan for a multi‑robot system to fulfill the described resource delivery mission.
