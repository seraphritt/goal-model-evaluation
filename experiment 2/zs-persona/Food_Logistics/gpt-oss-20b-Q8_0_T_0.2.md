## Goal Model – Multi‑Robot Food Delivery

| **Name**      | **Text**                                                                                                               | **Runtime**                                                                                                    | **Goal Type** | **Target Condition / Enquired Information**                                                 | **Relation** | **Ground Truth I** | **Ground Truth G** | **Consensus** |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------- | ------------ | ------------------ | ------------------ | ------------- |
| **G1**        | Deliver food from the kitchen to an inpatient room, ensuring the correct meal is retrieved and all dishes are cleaned. | G1.1; G1.2; G1.3; G1.4; G1.5; G1.6                                                                             | Achieve       | Food delivered to the correct room, meal retrieved by patient or staff, all dishes cleaned. | AND          | Perform                   |                    |               |
| **G1.1**      | Receive an order-by-order delivery request from the kitchen.                                                           | AT1                                                                                                            | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.2**      | Transport the requested meals from the kitchen to the inpatient room.                                                  | AT2; AT3; AT23                                                                                                 | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3**      | Deliver the food to the patient, either directly to the table or to the tray for later retrieval.                      | FALLBACK(G1.3.1, G1.3.2)                                                                                       | Perform       | –                                                                                           | OR           | OK                   |                    |               |
| **G1.3.1**    | Deliver the meal directly onto the patient’s table using the robot’s manipulation skill.                               | AT4                                                                                                            | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2**    | Deliver the meal onto the tray and coordinate its retrieval by patient or staff.                                       | G1.3.2.1; G1.3.2.2; G1.3.2.3; G1.3.2.4; G1.3.2.5; G1.3.2.6; G1.3.2.7; G1.3.2.8; G1.3.2.9; G1.3.2.10; G1.3.2.11 | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2.1**  | Query whether the patient can retrieve the meal from the tray.                                                         | AT6                                                                                                            | Query         | “Can patient retrieve meal from tray?”                                                      | AND          | OK                   |                    |               |
| **G1.3.2.2**  | Query whether a companion is present in the room.                                                                      | AT7                                                                                                            | Query         | “Is companion present?”                                                                     | AND          | OK                   |                    |               |
| **G1.3.2.3**  | Query whether a nurse is available to assist.                                                                          | AT8                                                                                                            | Query         | “Is nurse available?”                                                                       | AND          | OK                   |                    |               |
| **G1.3.2.4**  | Coordinate with the patient to retrieve the meal.                                                                      | AT9                                                                                                            | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2.5**  | Coordinate with the companion to retrieve the meal.                                                                    | AT10                                                                                                           | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2.6**  | Coordinate with the nurse to retrieve the meal.                                                                        | AT11                                                                                                           | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2.7**  | Robot fetches the meal from the tray when no human can retrieve it.                                                    | AT12                                                                                                           | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2.8**  | Wait until the meal is retrieved by patient or staff.                                                                  | AT13                                                                                                           | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2.9**  | Log the time and location of the meal retrieval.                                                                       | AT14                                                                                                           | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2.10** | Alert if the wrong meal is retrieved.                                                                                  | AT15                                                                                                           | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.3.2.11** | Indicate which meal should be retrieved by the patient.                                                                | AT22                                                                                                           | Perform       | –                                                                                           | AND          | OK                   |                    |               |
| **G1.4**      | Retrieve dirty dishes from the room.                                                                                   | FALLBACK(FALLBACK(G1.4.1, G1.4.2), G1.4.3)                                                                     | Perform       | –                                                                                           | OR           | Achieve. Target condition: all dishes were retrieved.                   |                    |               |
| **G1.4.1**    | Retrieve dishes without assistance.                                                                                    | AT16                                                                                                           | Perform       | –                                                                                           | AND          |  OK                  |                    |               |
| **G1.4.2**    | Retrieve dishes with human assistance.                                                                                 | AT17                                                                                                           | Perform       | –                                                                                           | AND          |  OK                  |                    |               |
| **G1.4.3**    | Retrieve dishes with another robot.                                                                                    | AT18                                                                                                           | Perform       | –                                                                                           | AND          |  OK                  |                    |               |
| **G1.5**      | Manage opening of the room door.                                                                                       | FALLBACK(G1.5.1, G1.5.2)                                                                                       | Perform       | –                                                                                           | OR           |  OK                  |                    |               |
| **G1.5.1**    | Robot opens the door alone.                                                                                            | AT19                                                                                                           | Perform       | –                                                                                           | AND          |  OK                  |                    |               |
| **G1.5.2**    | Robot requests a human to open the door.                                                                               | AT20                                                                                                           | Perform       | –                                                                                           | AND          |  OK                  |                    |               |
| **G1.6**      | Update system records after the delivery.                                                                              | AT21                                                                                                           | Perform       | –                                                                                           | AND          |  OK                  |                    |               |


---

## Task Model

| **Name** | **Text** | **Relation** | **Location** | **Number of Robots** |
|----------|----------|--------------|--------------|----------------------|
| **AT1** | Receive the order‑by‑order delivery request from the kitchen. | AND | kitchen | 1 |
| **AT2** | Plan the navigation path from the kitchen to the inpatient room. | AND | hospital corridor | 1 |
| **AT3** | Execute navigation to the inpatient room. | AND | hospital corridor | 1 |
| **AT4** | Place the meal on the patient’s table using the robot’s manipulation skill. | AND | inpatient room table | 1 |
| **AT5** | Place the meal on the tray in the patient room. | AND | inpatient room | 1 |
| **AT6** | Query whether the patient can retrieve the meal from the tray. | AND | inpatient room | 1 |
| **AT7** | Query whether a companion is present in the room. | AND | inpatient room | 1 |
| **AT8** | Query whether a nurse is available to assist. | AND | hospital | 1 |
| **AT9** | Coordinate with the patient to retrieve the meal. | AND | inpatient room | 1 |
| **AT10** | Coordinate with the companion to retrieve the meal. | AND | inpatient room | 1 |
| **AT11** | Coordinate with the nurse to retrieve the meal. | AND | inpatient room | 1 |
| **AT12** | Robot fetches the meal from the tray. | AND | inpatient room | 1 |
| **AT13** | Wait until the meal is retrieved by patient or staff. | AND | inpatient room | 1 |
| **AT14** | Log the time and location of the meal retrieval. | AND | inpatient room | 1 |
| **AT15** | Alert if the wrong meal is retrieved. | AND | inpatient room | 1 |
| **AT16** | Retrieve dishes without assistance. | AND | inpatient room | 1 |
| **AT17** | Retrieve dishes with human assistance. | AND | inpatient room | 2 |
| **AT18** | Retrieve dishes with another robot. | AND | inpatient room | 2 |
| **AT19** | Robot opens the door alone. | AND | inpatient room door | 1 |
| **AT20** | Robot requests a human to open the door. | AND | inpatient room door | 1 |
| **AT21** | Update system records after the delivery. | AND | hospital | 1 |
| **AT22** | Indicate which meal should be retrieved by the patient. | AND | inpatient room | 1 |
| **AT23** | Carry multiple meals from the kitchen to the room. | AND | kitchen | 1 |

---

## Logical Relationships (Summary)

```
G1  -> G1.1, G1.2, G1.3, G1.4, G1.5, G1.6   [AND]
G1.3 -> G1.3.1, G1.3.2                        [OR]
G1.3.2 -> G1.3.2.1, G1.3.2.2, G1.3.2.3, G1.3.2.4, G1.3.2.5, G1.3.2.6, G1.3.2.7, G1.3.2.8, G1.3.2.9, G1.3.2.10, G1.3.2.11   [AND]
G1.4 -> G1.4.1, G1.4.2, G1.4.3               [OR]
G1.5 -> G1.5.1, G1.5.2                       [OR]
G1.1 -> AT1                                   [AND]
G1.2 -> AT2, AT3, AT23                        [AND]
G1.3.1 -> AT4                                 [AND]
G1.3.2 -> AT5, AT6, AT7, AT8, AT9, AT10, AT11, AT12, AT13, AT14, AT15, AT22   [AND]
G1.4.1 -> AT16                                 [AND]
G1.4.2 -> AT17                                 [AND]
G1.4.3 -> AT18                                 [AND]
G1.5.1 -> AT19                                 [AND]
G1.5.2 -> AT20                                 [AND]
G1.6 -> AT21                                   [AND]
```

This goal‑task hierarchy captures the full multi‑robot delivery mission, including decision points (fallbacks), uncertainty handling (queries), coordination with humans, and record‑keeping.
