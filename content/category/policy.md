Title: Policy system
Author: Kristoffer Paulsson
Date: 2021-01-18
Category: Developer
url: policy-system.html
sort: 3

Policies are needed to guarantee safety within the Angelos network and for each user. Because each user is an entity with a private domain of nodes, every data transaction between two Facades in different domains must enforce policy checks to discover discrepancies.

In all circumstances must user safety be guaranteed or, they may be at risk of falling victim to EAVESDROPPING, SECURITY BREACHES, INFORMATION LOSS, INFILTRATION, EXPOSURE TO ROGUE ENTITIES, PERSECUTION, and LOSS OF LIFE AND WEALTH.

Policies apply in several layers and sections of the Angelos program and server, made to protect at multiple levels. Policies have a tag with a number, letter, and chronological serial number. The policy tag has a determined format for implementation reference and description.

Example: 1A-0001 Policy description and purpose.

## Layers and sections

* 1: Field level policies
    * A: Standard field checks
    * B: Specific field type validation
* 2: Document level policies
    * C: Standard document checks
    * D: Custom document checks
    * E: Arbitrary document checks
* 3: Portfolio level policies
    * F: Portfolio related checks
    * G: Collection related checks
    * H: Operation related checks
    * J: ...
* 4: Facade level policies
    * K: ...
    * L: ...
    * M: ...
    * N: ...
* 5: Node level policies
    * P: ...
    * Q: ...
    * R: ...
    * S: ...
* 6: Domain level policies
    * T: ...
    * U: ...
    * V: ...
    * X: ...
* 7: Network level policies
    * Y: ...
    * Z: ...
  
## Implented policies
 
0I-0000: Null policy. This policy should never happen, it indicates an implementation failure or different error.
 
1A-0001: Check that a field marked as required isn't empty. Required fields are mandatory.

1A-0002: Check that multifield isn't assigned non-list items directly, this goes both ways. A multifield must have a list.

1A-0003: Check that a field is assigned an item of a specified type only. The specified item types are required

