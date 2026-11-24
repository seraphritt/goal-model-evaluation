Below are the exact passages **removed or modified in the 12 previously generated variants**, together with their corresponding ground-truth goals.

Omission removes information, contradiction introduces a conflicting requirement, and ambiguity introduces wording with multiple interpretations. In the generated variants, contradiction means conflict with the ground-truth model. Your example uses a different definition, retaining two conflicting requirements within the same description.

**1. Omission variants**

| Mission | What was removed | Resulting passage | Related ground-truth goal |
|---|---|---|---|
| **Vital Signs** | “In case of non-response, an alert should be sent to the responsible nurse/doctor.” | The sentence was deleted entirely. | **G15 — Send Alert** |
| **Deliver Goods/Equipment** | The requirement to trigger an alert when returning the resource to a checkpoint fails. | “In case of failure to return the resource to a checkpoint, the report must be sent to the sector manager.” | **G15 — Trigger Alert** |
| **Lab Samples** | The robotic arm as a recipient during sample unloading. The later phrase “picks up samples” was also removed. | “In the laboratory, the sample can be picked by laboratory personnel.” Later, “The robotic arm scans the barcode in each sample, sorts, and loads the samples into the entry-module of the analysis machines.” | **G9 — Approach Arm and Unload Sample**, **G13 — Unload the Sample** |
| **Food Logistics** | The option to deliver food onto the room table, including its manipulation-skill requirement. | “The food can be fetched from the robot’s tray.” | **Delivery G11 — Deliver Food To Room Table** |

**2. Contradiction variants**

Each passage below replaced the corresponding original requirement.

| Mission | What was introduced | Conflict with the ground truth |
|---|---|---|
| **Vital Signs** | “In case of non-response, the robot must leave the responsible nurse/doctor unalerted.” | **G15 — Send Alert** provides an alert as the fallback when assessing the patient fails. The replacement prohibits that alert. |
| **Deliver Goods/Equipment** | “In case of failure to return the resource to a checkpoint, the alert must be suppressed and the report sent to the sector manager.” | **G15 — Trigger Alert** provides the alert fallback after checkpoint return fails. The replacement requires suppression. |
| **Lab Samples** | “In the laboratory, only laboratory personnel may unload the sample from the transport drawer. The robotic arm must never receive a sample directly from the transport robot.” | **G9 — Approach Arm and Unload Sample** and **G13 — Unload the Sample** describe unloading at the arm. The replacement prohibits the direct handoff. |
| **Food Logistics** | “Dirty dishes must be collected in the corridor outside the inpatient room. The robot must never pick them up inside the room.” | **Pickup G7 — Pickup Dishes in Patient Room** explicitly places collection inside the patient room. |

**3. Ambiguity variants**

Each passage below replaced the corresponding original requirement.

| Mission | What was introduced | Intended alternative interpretations | Related ground-truth goal |
|---|---|---|---|
| **Vital Signs ** | “When a robot 
comes out of a room where a patient subject to infectious disease is being treated, sterilization must be performed” | The room needs to be sterilized, or the robot needs to be sterilized, or both. | **G16 — Sanitize Robot if Needed** |
| **Deliver Goods/Equipment** | “In case of failure to return the resource to a checkpoint, the robot must send the report to the sector manager with an alert when delivery resumes.” | “When delivery resumes” specifies the timing of **the alert alone**, or of **both the report and the alert**. | **G13 — Return Objects To Checkpoint**, **G15 — Trigger Alert** |
| **Lab Samples** | “In the laboratory, a technician positions the transport robot beside the robotic arm so that it can unload the sample.” | “It” refers to **the transport robot** or **the robotic arm**, leaving the unloading responsibility unclear. | **G9 — Approach Arm and Unload Sample**, **G13 — Unload the Sample** |
| **Food Logistics** | “At pickup, the patient places the dirty dishes on a cart beside the room door for the robot to retrieve.” | The cart is **inside the patient room** or **outside in the corridor**, leaving the pickup location unclear. | **Pickup G6 — Fetch Pickup Room**, **G7 — Pickup Dishes in Patient Room** |

The Vital Signs ambiguity is a weaker experimental manipulation because the original expression “non-response” already leaves partial responses unspecified. The Food Logistics ambiguity also introduces patient participation and a cart, so it changes more than the pickup-location wording alone.