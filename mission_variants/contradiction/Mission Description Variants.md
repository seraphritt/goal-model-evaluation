# Mission Description Variants: Omission, Contradiction, and Ambiguity

Below are **12 mission description variants**, based on the four original robotic missions: Vital Signs, Deliver Goods/Equipment, Lab Samples, and Food Logistics.

Each mission has three variations:

1. **Omission:** A relevant requirement is deliberately removed, making the mission description incomplete.
2. **Contradiction:** A requirement is introduced that directly conflicts with another requirement in the same description.
3. **Ambiguity:** A requirement is modified to permit multiple interpretations, making its intended meaning unclear.

### Variation Design

To support controlled experiments in LLM-assisted goal-model generation, I followed three principles:

- **Minimal modification:** Preserve the original mission description as much as possible.
- **Single targeted defect:** Introduce one deliberate omission, contradiction, or ambiguity per variant.
- **Consistent target:** Whenever possible, modify the same requirement across the three variants of a mission, allowing direct comparison of how each defect affects goal-model generation.

The variations retain the original mission objectives, operational conditions, and multi-robot coordination mechanisms, except where deliberately modified.

---

# 1. Omission Variants

In these variants, an existing requirement is removed without replacing it. The resulting descriptions lack information necessary to fully specify some aspect of mission execution.

## 1.1. Vital Signs — Omission

Every two hours, all patient's vital signs should be checked. Therefore, the assigned robot should visit every occupied room.

Before entering the room, the robot must check if the patient is available for vital signs checking, and if there is enough battery to perform all the tasks inside the room. Hospital rooms may have one or more beds. So the robot has to identify the correct patient either by asking or by scanning the patients barcode.

If there is not enough battery, the robot should recharge and the tasks need to be reassigned. Once inside the room, the robot should approach the patient, announce the procedure to be performed, and provide instructions to the patient.

The failure of collecting any necessary vital signs should trigger a set of questions to assess the patient status for those signs that were failed to be collected. In case of non-response, an alert should be sent to the responsible nurse/doctor.

Once the patient is checked, the robot should mark it as done and proceed to the next room.

Patients subject to infectious diseases must be checked for heart rate, blood pressure, body temperature, and blood oxygenation. Patients subject to post-surgical conditions must be checked for heart rate and blood oxygenation. Patients with a history of diabetes must be checked for glucose levels in the blood.

When a robot comes out of a room where a patient subject to infectious disease is being treated, it must be sterilized. All the patients in high risk must be checked in the first 15 minutes of the mission.

If the robot is performing any duties with patient contact (touching the patient) it should disinfect its actuators afterwards.

Additional robots can be assigned to help in case of impossibility of performing the mission in the required time. The responsible manager for the site must be alerted if no combination of robots can complete the mission.

## 1.2. Deliver Goods/Equipment — Omission

When required, a robot must collect the required resources in the storage and deliver them to the requesting agent in a specified location.

In the collection phase, the robot must go to the storage places where the resources can be found. The order to be followed is defined by the estimation of waiting time summed up with the path to be run by the robot.

Once the robot reaches one storage and it is time to request the resource, the robot sends a message to the storage with the precise specification of the requested resources and waits until the resources have been retrieved.

Once retrieved, the delivery phase begins. In this phase, the robot will make as many runs as necessary to take all the resources to the specified location.

If the battery of the assigned robot runs low (10%) in the collection phase, the robot goes back to the recharging station and assigns the mission to another robot.

In case of failure to return the resource to a checkpoint, an alert must be triggered and the report sent to the sector manager.

When multiple items are required from different storages, multiple robots can be assigned to parallel collect-deliver tasks to reduce the time to finish the mission.

Examples of goods/equipments are: (i) sterile medical equipment Logistics, which should be transported from sterile facilities to use destinations, and (ii) clean linens, which should periodically be moved from the laundry to storage rooms close to where it should be used.

## 1.3. Lab Samples — Omission

Lab samples should be transported from patient floors to the laboratory. A nurse responsible for collecting a sample can request a delivery to the laboratory.

Each sample before collection is identified with a barcode. The nurse inserts data about the sample in a track system.

Samples are transported in secure locked drawers. In the laboratory, the sample can be picked by a robotic arm or laboratory personnel.

The robotic arm picks up samples, scans the barcode in each sample, sorts, and loads the samples into the entry-module of the analysis machines.

Information about where and when a given sample was picked should be logged securely.

The time between sample collection and laboratory delivery should be tracked to be sure that it goes according to laboratory protocols.

## 1.4. Food Logistics — Omission

The system should deliver food from the kitchen to an inpatient room. The delivery is made on an order-by-order basis in response to kitchen delivery requests.

The food can be delivered into a room table by the robot (requires a special manipulation robot skill) or the food can be fetched from the robot's tray.

Fetching from the robot tray requires cooperation with the inpatient, a companion, a nurse, or another robot.

Some inpatients could be unable to fetch the food from the tray, and a companion visitor or nurse could not be available at the moment of the delivery.

The information about if the inpatient, a companion visitor or nurse can be able to retrieve the food from the tray can be obtained based on the inpatient record according to information about the patient and the presence of a companion into the room.

This information is subject to uncertainty.

The robot can carry multiple meals, in the case of a person retrieving the meal the robot should indicate which meal should be retrieved by a given inpatient.

It should track when and where each meal was retrieved.

Dirty dishes should be retrieved from the room. As with delivery, the dish retrieve can occur unassisted, with the cooperation of two robots or with the cooperation of robots and a human.

Opening the room door can involve cooperation with another robot or a human.

Someone in the room can call a robot to pick up the dishes. In that case, that person can signal if they can open the door when the robot comes to it.

**Omissions introduced:**

| Mission | Deliberately omitted requirement |
|---|---|
| Vital Signs | The robot must return after 5 minutes if the patient is unavailable. |
| Deliver Goods/Equipment | The robot must return resources to a checkpoint and reassign the remaining delivery task when its battery reaches 30%. |
| Lab Samples | Only authorized personnel or designated robots at specific locations may open the locked drawers. |
| Food Logistics | The robot must generate an alert when the wrong meal is retrieved. |

These omissions target exception handling, battery-related adaptation, access control, and error detection, respectively.

---

# 2. Contradiction Variants

In these variants, a new requirement is inserted that conflicts with an existing requirement. Both statements are retained so that the description contains an explicit inconsistency.

## 2.1. Vital Signs — Contradiction

Every two hours, all patient's vital signs should be checked. Therefore, the assigned robot should visit every occupied room.

Before entering the room, the robot must check if the patient is available for vital signs checking, and if there is enough battery to perform all the tasks inside the room. Hospital rooms may have one or more beds. So the robot has to identify the correct patient either by asking or by scanning the patients barcode.

If the patient is not available, the robot should come back in 5 minutes. However, if the patient is unavailable, the robot must wait at least 20 minutes before returning to the room.

If there is not enough battery, the robot should recharge and the tasks need to be reassigned. Once inside the room, the robot should approach the patient, announce the procedure to be performed, and provide instructions to the patient.

The failure of collecting any necessary vital signs should trigger a set of questions to assess the patient status for those signs that were failed to be collected. In case of non-response, an alert should be sent to the responsible nurse/doctor.

Once the patient is checked, the robot should mark it as done and proceed to the next room.

Patients subject to infectious diseases must be checked for heart rate, blood pressure, body temperature, and blood oxygenation. Patients subject to post-surgical conditions must be checked for heart rate and blood oxygenation. Patients with a history of diabetes must be checked for glucose levels in the blood.

When a robot comes out of a room where a patient subject to infectious disease is being treated, it must be sterilized. All the patients in high risk must be checked in the first 15 minutes of the mission.

If the robot is performing any duties with patient contact (touching the patient) it should disinfect its actuators afterwards.

Additional robots can be assigned to help in case of impossibility of performing the mission in the required time. The responsible manager for the site must be alerted if no combination of robots can complete the mission.

## 2.2. Deliver Goods/Equipment — Contradiction

When required, a robot must collect the required resources in the storage and deliver them to the requesting agent in a specified location.

In the collection phase, the robot must go to the storage places where the resources can be found. The order to be followed is defined by the estimation of waiting time summed up with the path to be run by the robot.

Once the robot reaches one storage and it is time to request the resource, the robot sends a message to the storage with the precise specification of the requested resources and waits until the resources have been retrieved.

Once retrieved, the delivery phase begins. In this phase, the robot will make as many runs as necessary to take all the resources to the specified location.

If the battery of the assigned robot runs low (10%) in the collection phase, the robot goes back to the recharging station and assigns the mission to another robot.

If the battery of the assigned robot runs low (30%) in the delivery phase, the robot must return the resource to a checkpoint and assign the remaining task to another robot, which will know where the resource is positioned.

However, when the battery reaches 30% during the delivery phase, the robot must continue delivering the resources without returning them to a checkpoint or reassigning the task to another robot.

In case of failure to return the resource to a checkpoint, an alert must be triggered and the report sent to the sector manager.

When multiple items are required from different storages, multiple robots can be assigned to parallel collect-deliver tasks to reduce the time to finish the mission.

Examples of goods/equipments are: (i) sterile medical equipment Logistics, which should be transported from sterile facilities to use destinations, and (ii) clean linens, which should periodically be moved from the laundry to storage rooms close to where it should be used.

## 2.3. Lab Samples — Contradiction

Lab samples should be transported from patient floors to the laboratory. A nurse responsible for collecting a sample can request a delivery to the laboratory.

Each sample before collection is identified with a barcode. The nurse inserts data about the sample in a track system.

Samples are transported in secure locked drawers. In the laboratory, the sample can be picked by a robotic arm or laboratory personnel.

Only authorized personnel or specific robots in specific locations should be able to open the locked drawers. However, any person or robot must be allowed to open the locked drawers at any location, regardless of authorization.

The robotic arm picks up samples, scans the barcode in each sample, sorts, and loads the samples into the entry-module of the analysis machines.

Information about where and when a given sample was picked should be logged securely.

The time between sample collection and laboratory delivery should be tracked to be sure that it goes according to laboratory protocols.

## 2.4. Food Logistics — Contradiction

The system should deliver food from the kitchen to an inpatient room. The delivery is made on an order-by-order basis in response to kitchen delivery requests.

The food can be delivered into a room table by the robot (requires a special manipulation robot skill) or the food can be fetched from the robot's tray.

Fetching from the robot tray requires cooperation with the inpatient, a companion, a nurse, or another robot.

Some inpatients could be unable to fetch the food from the tray, and a companion visitor or nurse could not be available at the moment of the delivery.

The information about if the inpatient, a companion visitor or nurse can be able to retrieve the food from the tray can be obtained based on the inpatient record according to information about the patient and the presence of a companion into the room.

This information is subject to uncertainty.

The robot can carry multiple meals, in the case of a person retrieving the meal the robot should indicate which meal should be retrieved by a given inpatient.

It should track when and where each meal was retrieved.

The robot should alert if a wrong meal is retrieved. However, if the wrong meal is retrieved, the robot must not generate an alert.

Dirty dishes should be retrieved from the room. As with delivery, the dish retrieve can occur unassisted, with the cooperation of two robots or with the cooperation of robots and a human.

Opening the room door can involve cooperation with another robot or a human.

Someone in the room can call a robot to pick up the dishes. In that case, that person can signal if they can open the door when the robot comes to it.

**Contradictions introduced:**

| Mission | Existing requirement | Contradictory requirement |
|---|---|---|
| Vital Signs | Return after 5 minutes. | Wait at least 20 minutes before returning. |
| Deliver Goods/Equipment | At 30% battery, return resources to a checkpoint and reassign the task. | At 30% battery, continue delivering without returning resources or reassigning the task. |
| Lab Samples | Only authorized personnel or designated robots can open the drawers. | Anyone or any robot must be allowed to open the drawers. |
| Food Logistics | Generate an alert when the wrong meal is retrieved. | Do not generate an alert when the wrong meal is retrieved. |

Each pair of contradictory requirements refers to the same condition, making the conflict identifiable without requiring assumptions about the environment.

---

# 3. Ambiguity Variants

In these variants, an existing requirement is modified to introduce uncertainty about its meaning, conditions, or execution constraints. The resulting description permits multiple reasonable interpretations.

## 3.1. Vital Signs — Ambiguity

Every two hours, all patient's vital signs should be checked. Therefore, the assigned robot should visit every occupied room.

Before entering the room, the robot must check if the patient is available for vital signs checking, and if there is enough battery to perform all the tasks inside the room. Hospital rooms may have one or more beds. So the robot has to identify the correct patient either by asking or by scanning the patients barcode.

If the patient is not available, the robot should come back after a short period of time.

If there is not enough battery, the robot should recharge and the tasks need to be reassigned. Once inside the room, the robot should approach the patient, announce the procedure to be performed, and provide instructions to the patient.

The failure of collecting any necessary vital signs should trigger a set of questions to assess the patient status for those signs that were failed to be collected. In case of non-response, an alert should be sent to the responsible nurse/doctor.

Once the patient is checked, the robot should mark it as done and proceed to the next room.

Patients subject to infectious diseases must be checked for heart rate, blood pressure, body temperature, and blood oxygenation. Patients subject to post-surgical conditions must be checked for heart rate and blood oxygenation. Patients with a history of diabetes must be checked for glucose levels in the blood.

When a robot comes out of a room where a patient subject to infectious disease is being treated, it must be sterilized. All the patients in high risk must be checked in the first 15 minutes of the mission.

If the robot is performing any duties with patient contact (touching the patient) it should disinfect its actuators afterwards.

Additional robots can be assigned to help in case of impossibility of performing the mission in the required time. The responsible manager for the site must be alerted if no combination of robots can complete the mission.

## 3.2. Deliver Goods/Equipment — Ambiguity

When required, a robot must collect the required resources in the storage and deliver them to the requesting agent in a specified location.

In the collection phase, the robot must go to the storage places where the resources can be found. The order to be followed is defined by the estimation of waiting time summed up with the path to be run by the robot.

Once the robot reaches one storage and it is time to request the resource, the robot sends a message to the storage with the precise specification of the requested resources and waits until the resources have been retrieved.

Once retrieved, the delivery phase begins. In this phase, the robot will make as many runs as necessary to take all the resources to the specified location.

If the battery of the assigned robot runs low (10%) in the collection phase, the robot goes back to the recharging station and assigns the mission to another robot.

If the battery of the assigned robot becomes low during the delivery phase, the robot must return the resource to a checkpoint and assign the remaining task to another robot, which will know where the resource is positioned.

In case of failure to return the resource to a checkpoint, an alert must be triggered and the report sent to the sector manager.

When multiple items are required from different storages, multiple robots can be assigned to parallel collect-deliver tasks to reduce the time to finish the mission.

Examples of goods/equipments are: (i) sterile medical equipment Logistics, which should be transported from sterile facilities to use destinations, and (ii) clean linens, which should periodically be moved from the laundry to storage rooms close to where it should be used.

## 3.3. Lab Samples — Ambiguity

Lab samples should be transported from patient floors to the laboratory. A nurse responsible for collecting a sample can request a delivery to the laboratory.

Each sample before collection is identified with a barcode. The nurse inserts data about the sample in a track system.

Samples are transported in secure locked drawers. In the laboratory, the sample can be picked by a robotic arm or laboratory personnel.

Only personnel or robots considered suitable at the time should be able to open the locked drawers.

The robotic arm picks up samples, scans the barcode in each sample, sorts, and loads the samples into the entry-module of the analysis machines.

Information about where and when a given sample was picked should be logged securely.

The time between sample collection and laboratory delivery should be tracked to be sure that it goes according to laboratory protocols.

## 3.4. Food Logistics — Ambiguity

The system should deliver food from the kitchen to an inpatient room. The delivery is made on an order-by-order basis in response to kitchen delivery requests.

The food can be delivered into a room table by the robot (requires a special manipulation robot skill) or the food can be fetched from the robot's tray.

Fetching from the robot tray requires cooperation with the inpatient, a companion, a nurse, or another robot.

Some inpatients could be unable to fetch the food from the tray, and a companion visitor or nurse could not be available at the moment of the delivery.

The information about if the inpatient, a companion visitor or nurse can be able to retrieve the food from the tray can be obtained based on the inpatient record according to information about the patient and the presence of a companion into the room.

This information is subject to uncertainty.

The robot can carry multiple meals, in the case of a person retrieving the meal the robot should indicate which meal should be retrieved by a given inpatient.

It should track when and where each meal was retrieved.

The robot should generate an alert if the meal retrieval is not performed correctly.

Dirty dishes should be retrieved from the room. As with delivery, the dish retrieve can occur unassisted, with the cooperation of two robots or with the cooperation of robots and a human.

Opening the room door can involve cooperation with another robot or a human.

Someone in the room can call a robot to pick up the dishes. In that case, that person can signal if they can open the door when the robot comes to it.

**Ambiguities introduced:**

| Mission | Modified expression | Source of ambiguity |
|---|---|---|
| Vital Signs | "After a short period of time" | The required waiting time is unspecified. Different interpretations may produce different scheduling constraints. |
| Deliver Goods/Equipment | "Becomes low during the delivery phase" | The battery threshold is unspecified, allowing different interpretations of when task reassignment must occur. |
| Lab Samples | "Personnel or robots considered suitable at the time" | The criteria for determining which agents are permitted to access the drawers are unclear. |
| Food Logistics | "If the meal retrieval is not performed correctly" | The conditions constituting incorrect retrieval are unspecified. This could refer to retrieving the wrong meal, incorrect handling, or another type of error. |

---

# 4. Summary of the 12 Variants

| Mission | Omission | Contradiction | Ambiguity |
|---|---|---|---|
| **Vital Signs** | Missing waiting time and retry behavior for unavailable patients | Conflicting waiting times: 5 versus at least 20 minutes | Unspecified waiting period |
| **Deliver Goods/Equipment** | Missing low-battery delivery-phase recovery behavior | Conflicting instructions at 30% battery | Unspecified battery threshold |
| **Lab Samples** | Missing authorization requirements | Restricted versus unrestricted drawer access | Unclear access eligibility criteria |
| **Food Logistics** | Missing wrong-meal alert requirement | Alert required versus alert prohibited | Unclear conditions triggering alerts |

**Total: 12 variants (4 missions × 3 defect types).**

## 5. Recommendation for Your Experimental Evaluation

Given your research on LLM-assisted goal-model generation from natural-language robotic mission descriptions, these variants could support an experiment evaluating the ability of an LLM to identify defects in mission specifications.

I recommend distinguishing between two evaluation objectives:

**1. Defect identification**

Evaluate whether the LLM correctly identifies the deliberately introduced problem and its location in the mission description.

For example, in the contradictory Vital Signs variant, the expected observation would be that the description specifies two incompatible waiting times for the same condition.

**2. Defect resolution**

Evaluate whether the LLM can propose an appropriate correction without introducing unsupported assumptions.

For example, in the ambiguous Deliver Goods/Equipment variant, the LLM should identify that the delivery-phase battery threshold is unspecified rather than arbitrarily deciding that the threshold must be 30%.

An important methodological consideration is that **identifying a defect does not necessarily mean that the LLM can correctly resolve it**. For omissions and ambiguities, the original requirement can serve as a reference, but the modified description alone may not contain enough information to recover that requirement.

Therefore, you could evaluate defect identification separately from the correctness of the proposed correction.

This distinction is particularly relevant to your research question concerning the extent to which LLM-generated goal models can help improve the clarity, completeness, and consistency of natural-language mission descriptions.
