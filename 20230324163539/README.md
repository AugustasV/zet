# Authentication and Authorization
### Authentication

Authentication is the process of verifying the identity of a user or entity attempting to access a system or resource. Here are a few key points:

1. Central authentication example: One common example is Active Directory, which uses the Lightweight Directory Access Protocol (LDAP) to store and manage user credentials centrally. LDAP allows organizations to maintain a single source of truth for user authentication across multiple systems.

2. Multi-factor authentication (MFA): MFA enhances security by requiring users to provide multiple pieces of evidence to prove their identity. Common factors include something you know (e.g., a password), something you have (e.g., a mobile device), and something you are (e.g., biometrics like fingerprint or facial recognition). It is important to note that using a combination of a PIN and a password does not qualify as true multi-factor authentication.

3. Biometric authentication: Biometric factors, such as iris, retina, or fingerprint scans, can be used for authentication purposes. However, certain biometric methods may have limitations. For example, retina scans might be impractical for pregnant individuals due to potential changes in their retina during pregnancy.

### Authorization

Authorization decides what permissions you have what to do with those permissions.


1. Permission-based authorization: This approach involves granting permissions or privileges to users based on their roles, groups, or other organizational units. Access control lists (ACLs) and role-based access control (RBAC) are common methods used for permission management.

2. Attribute-based access control (ABAC): ABAC is a more flexible and granular authorization model. It considers various attributes associated with users, resources, and the environment to make access control decisions. Attributes could include user roles, location, time, and other contextual information. ABAC provides a more dynamic and adaptable approach to access control.

* Open Policy Agent used for real time driven software

* OPAL is layer on top of OPA, open source one

Source: [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html) and het_tanis twitch

[OPAL policies](https://github.com/permitio/opal
)
