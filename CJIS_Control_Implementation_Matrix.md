# [[AGENCY_NAME]] CJIS Control Implementation Matrix

This expanded matrix gives each CJIS control its own implementation entry so owners can assign work, collect evidence, and review the control on a defined cadence.

## Shared Placeholders

- `[[CONTROL_OWNER]]`
- `[[IMPLEMENTATION_NOTES]]`
- `[[EVIDENCE_ARTIFACTS]]`
- `[[REVIEW_FREQUENCY]]`
- `[[ACCESS_REVIEW_INTERVAL_DAYS]]`
- `[[RISK_LEVEL]]`

## How To Use

- Replace placeholders with agency-specific values.
- Use one owner per control and keep evidence current.
- Mark exceptions separately and tie them to a review date.

## Access Control (AC)

### AC-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `AC-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-2 - Account Management

| Field | Value |
| --- | --- |
| Control code | `AC-2` |
| Control title | Account Management |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable accounts for high-risk individuals requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-2(1) - Automated System Account Management

| Field | Value |
| --- | --- |
| Control code | `AC-2(1)` |
| Control title | Automated System Account Management |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated system account management requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-2(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-2(2) - Automated Temporary and Emergency Account Management

| Field | Value |
| --- | --- |
| Control code | `AC-2(2)` |
| Control title | Automated Temporary and Emergency Account Management |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated temporary and emergency account management requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-2(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-2(3) - Disable Accounts

| Field | Value |
| --- | --- |
| Control code | `AC-2(3)` |
| Control title | Disable Accounts |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable accounts requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-2(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-2(4) - Automated Audit Actions

| Field | Value |
| --- | --- |
| Control code | `AC-2(4)` |
| Control title | Automated Audit Actions |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated audit actions requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-2(4) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-2(5) - Inactivity Logout

| Field | Value |
| --- | --- |
| Control code | `AC-2(5)` |
| Control title | Inactivity Logout |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific inactivity logout requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-2(5) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-2(13) - Disable Accounts for High-risk Individuals

| Field | Value |
| --- | --- |
| Control code | `AC-2(13)` |
| Control title | Disable Accounts for High-risk Individuals |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable accounts for high-risk individuals requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-2(13) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-3 - Access Enforcement

| Field | Value |
| --- | --- |
| Control code | `AC-3` |
| Control title | Access Enforcement |
| What it is | This control addresses access enforcement for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-3(14) - Individual Access

| Field | Value |
| --- | --- |
| Control code | `AC-3(14)` |
| Control title | Individual Access |
| What it is | Enhancement to AC-3 (Access Enforcement) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific individual access requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-3(14) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-4 - Information Flow Enforcement

| Field | Value |
| --- | --- |
| Control code | `AC-4` |
| Control title | Information Flow Enforcement |
| What it is | This control addresses information flow enforcement for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-5 - Separation of Duties

| Field | Value |
| --- | --- |
| Control code | `AC-5` |
| Control title | Separation of Duties |
| What it is | This control addresses separation of duties for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-6 - Least Privilege

| Field | Value |
| --- | --- |
| Control code | `AC-6` |
| Control title | Least Privilege |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prohibit non-privileged users from executing privileged functions requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-6(1) - Authorize Access to Security Functions

| Field | Value |
| --- | --- |
| Control code | `AC-6(1)` |
| Control title | Authorize Access to Security Functions |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific authorize access to security functions requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-6(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-6(2) - Non-privileged Access for Nonsecurity Functions

| Field | Value |
| --- | --- |
| Control code | `AC-6(2)` |
| Control title | Non-privileged Access for Nonsecurity Functions |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific non-privileged access for nonsecurity functions requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-6(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-6(5) - Privileged Accounts

| Field | Value |
| --- | --- |
| Control code | `AC-6(5)` |
| Control title | Privileged Accounts |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific privileged accounts requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-6(5) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-6(7) - Review of User Privileges

| Field | Value |
| --- | --- |
| Control code | `AC-6(7)` |
| Control title | Review of User Privileges |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific review of user privileges requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-6(7) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-6(9) - Log Use of Privileged Functions

| Field | Value |
| --- | --- |
| Control code | `AC-6(9)` |
| Control title | Log Use of Privileged Functions |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific log use of privileged functions requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-6(9) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-6(10) - Prohibit Non-privileged Users from Executing Privileged Functions

| Field | Value |
| --- | --- |
| Control code | `AC-6(10)` |
| Control title | Prohibit Non-privileged Users from Executing Privileged Functions |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prohibit non-privileged users from executing privileged functions requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-6(10) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-7 - Unsuccessful Logon Attempts

| Field | Value |
| --- | --- |
| Control code | `AC-7` |
| Control title | Unsuccessful Logon Attempts |
| What it is | This control addresses unsuccessful logon attempts for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-8 - System Use Notification

| Field | Value |
| --- | --- |
| Control code | `AC-8` |
| Control title | System Use Notification |
| What it is | This control addresses system use notification for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-11 - Device Lock

| Field | Value |
| --- | --- |
| Control code | `AC-11` |
| Control title | Device Lock |
| What it is | Enhancement to AC-11 (Device Lock) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific pattern-hiding displays requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-11(1) - Pattern-hiding Displays

| Field | Value |
| --- | --- |
| Control code | `AC-11(1)` |
| Control title | Pattern-hiding Displays |
| What it is | Enhancement to AC-11 (Device Lock) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific pattern-hiding displays requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-11(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-12 - Session Termination

| Field | Value |
| --- | --- |
| Control code | `AC-12` |
| Control title | Session Termination |
| What it is | This control addresses session termination for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-14 - Permitted Actions without Identification or Authentication

| Field | Value |
| --- | --- |
| Control code | `AC-14` |
| Control title | Permitted Actions without Identification or Authentication |
| What it is | This control addresses permitted actions without identification or authentication for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-17 - Remote Access

| Field | Value |
| --- | --- |
| Control code | `AC-17` |
| Control title | Remote Access |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific privileged commands and access requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-17(1) - Monitoring and Control

| Field | Value |
| --- | --- |
| Control code | `AC-17(1)` |
| Control title | Monitoring and Control |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific monitoring and control requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-17(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-17(2) - Protection of Confidentiality and Integrity Using Encryption

| Field | Value |
| --- | --- |
| Control code | `AC-17(2)` |
| Control title | Protection of Confidentiality and Integrity Using Encryption |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific protection of confidentiality and integrity using encryption requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-17(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-17(3) - Managed Access Control Points

| Field | Value |
| --- | --- |
| Control code | `AC-17(3)` |
| Control title | Managed Access Control Points |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific managed access control points requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-17(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-17(4) - Privileged Commands and Access

| Field | Value |
| --- | --- |
| Control code | `AC-17(4)` |
| Control title | Privileged Commands and Access |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific privileged commands and access requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-17(4) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-18 - Wireless Access

| Field | Value |
| --- | --- |
| Control code | `AC-18` |
| Control title | Wireless Access |
| What it is | Enhancement to AC-18 (Wireless Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable wireless networking ..........................................................32 vii 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-18(1) - Authentication and Encryption

| Field | Value |
| --- | --- |
| Control code | `AC-18(1)` |
| Control title | Authentication and Encryption |
| What it is | Enhancement to AC-18 (Wireless Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific authentication and encryption requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-18(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-18(3) - Disable Wireless Networking

| Field | Value |
| --- | --- |
| Control code | `AC-18(3)` |
| Control title | Disable Wireless Networking |
| What it is | Enhancement to AC-18 (Wireless Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable wireless networking ..........................................................32 vii 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-18(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-19 - Access Control for Mobile Devices

| Field | Value |
| --- | --- |
| Control code | `AC-19` |
| Control title | Access Control for Mobile Devices |
| What it is | Enhancement to AC-19 (Access Control for Mobile Devices) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific full device or container-based encryption requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-19(5) - Full Device or Container-based Encryption

| Field | Value |
| --- | --- |
| Control code | `AC-19(5)` |
| Control title | Full Device or Container-based Encryption |
| What it is | Enhancement to AC-19 (Access Control for Mobile Devices) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific full device or container-based encryption requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-19(5) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-20 - Use of External Systems

| Field | Value |
| --- | --- |
| Control code | `AC-20` |
| Control title | Use of External Systems |
| What it is | Enhancement to AC-20 (Use of External Systems) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limits on authorized use requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-20(1) - Limits on Authorized Use

| Field | Value |
| --- | --- |
| Control code | `AC-20(1)` |
| Control title | Limits on Authorized Use |
| What it is | Enhancement to AC-20 (Use of External Systems) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limits on authorized use requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-20(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-20(2) - Portable Storage Devices \227 Restricted Use

| Field | Value |
| --- | --- |
| Control code | `AC-20(2)` |
| Control title | Portable Storage Devices \227 Restricted Use |
| What it is | Enhancement to AC-20 (Use of External Systems) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific portable storage devices \227 restricted use requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AC-20(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AC-21 - Information Sharing

| Field | Value |
| --- | --- |
| Control code | `AC-21` |
| Control title | Information Sharing |
| What it is | This control addresses information sharing for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-22 - Publicly Accessible Content

| Field | Value |
| --- | --- |
| Control code | `AC-22` |
| Control title | Publicly Accessible Content |
| What it is | This control addresses publicly accessible content for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

### AC-23 - Ac-23

| Field | Value |
| --- | --- |
| Control code | `AC-23` |
| Control title | Ac-23 |
| What it is | This control addresses ac-23 for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Implement role-based access, MFA, account lifecycle controls, and periodic access review. |
| Evidence / artifact | Access request forms, approvals, MFA status, access review report |
| Review frequency | Quarterly or `[[ACCESS_REVIEW_INTERVAL_DAYS]]` days |

## Awareness and Training (AT)

### AT-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `AT-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Require completion before access and renew at least annually. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assign CJIS awareness training at onboarding and annually, then record completion. |
| Evidence / artifact | Training completion records, signed acknowledgments, roster export |
| Review frequency | Annual and upon hire or role change |

### AT-2 - Literacy Training and Awareness

| Field | Value |
| --- | --- |
| Control code | `AT-2` |
| Control title | Literacy Training and Awareness |
| What it is | This control addresses at-2 for CJIS systems, users, or data. |
| Recommended approach | Require completion before access and renew at least annually. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assign CJIS awareness training at onboarding and annually, then record completion. |
| Evidence / artifact | Training completion records, signed acknowledgments, roster export |
| Review frequency | Annual and upon hire or role change |

### AT-3 - Role-based Training

| Field | Value |
| --- | --- |
| Control code | `AT-3` |
| Control title | Role-based Training |
| What it is | This control addresses at-3 for CJIS systems, users, or data. |
| Recommended approach | Require completion before access and renew at least annually. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assign CJIS awareness training at onboarding and annually, then record completion. |
| Evidence / artifact | Training completion records, signed acknowledgments, roster export |
| Review frequency | Annual and upon hire or role change |

### AT-4 - Training Records

| Field | Value |
| --- | --- |
| Control code | `AT-4` |
| Control title | Training Records |
| What it is | This control addresses training records for CJIS systems, users, or data. |
| Recommended approach | Require completion before access and renew at least annually. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assign CJIS awareness training at onboarding and annually, then record completion. |
| Evidence / artifact | Training completion records, signed acknowledgments, roster export |
| Review frequency | Annual and upon hire or role change |

## Audit and Accountability (AU)

### AU-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `AU-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-2 - Event Logging

| Field | Value |
| --- | --- |
| Control code | `AU-2` |
| Control title | Event Logging |
| What it is | This control addresses event logging for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-3 - Content of Audit Records

| Field | Value |
| --- | --- |
| Control code | `AU-3` |
| Control title | Content of Audit Records |
| What it is | Enhancement to AU-3 (Content of Audit Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-3(1) - Additional Audit Information

| Field | Value |
| --- | --- |
| Control code | `AU-3(1)` |
| Control title | Additional Audit Information |
| What it is | Enhancement to AU-3 (Content of Audit Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific additional audit information requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AU-3(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AU-3(3) - Limit Personally Identifiable Information Elements

| Field | Value |
| --- | --- |
| Control code | `AU-3(3)` |
| Control title | Limit Personally Identifiable Information Elements |
| What it is | Enhancement to AU-3 (Content of Audit Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AU-3(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AU-4 - Audit Log Storage Capacity

| Field | Value |
| --- | --- |
| Control code | `AU-4` |
| Control title | Audit Log Storage Capacity |
| What it is | This control addresses audit log storage capacity for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-5 - Response to Audit Logging Process Failures

| Field | Value |
| --- | --- |
| Control code | `AU-5` |
| Control title | Response to Audit Logging Process Failures |
| What it is | This control addresses response to audit logging process failures for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-6 - Audit Record Review, Analysis, and Reporting

| Field | Value |
| --- | --- |
| Control code | `AU-6` |
| Control title | Audit Record Review, Analysis, and Reporting |
| What it is | Enhancement to AU-6 (Audit Record Review, Analysis, and Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific correlate audit record repositories requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-6(1) - Automated Process Integration

| Field | Value |
| --- | --- |
| Control code | `AU-6(1)` |
| Control title | Automated Process Integration |
| What it is | Enhancement to AU-6 (Audit Record Review, Analysis, and Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated process integration requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AU-6(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AU-6(3) - Correlate Audit Record Repositories

| Field | Value |
| --- | --- |
| Control code | `AU-6(3)` |
| Control title | Correlate Audit Record Repositories |
| What it is | Enhancement to AU-6 (Audit Record Review, Analysis, and Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific correlate audit record repositories requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AU-6(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AU-7 - Audit Record Reduction and Report Generation

| Field | Value |
| --- | --- |
| Control code | `AU-7` |
| Control title | Audit Record Reduction and Report Generation |
| What it is | Enhancement to AU-7 (Audit Record Reduction and Report Generation) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automatic processing requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-7(1) - Automatic Processing

| Field | Value |
| --- | --- |
| Control code | `AU-7(1)` |
| Control title | Automatic Processing |
| What it is | Enhancement to AU-7 (Audit Record Reduction and Report Generation) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automatic processing requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to AU-7(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### AU-8 - Time Stamps

| Field | Value |
| --- | --- |
| Control code | `AU-8` |
| Control title | Time Stamps |
| What it is | This control addresses time stamps for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-9 - Protection of Audit Information

| Field | Value |
| --- | --- |
| Control code | `AU-9` |
| Control title | Protection of Audit Information |
| What it is | This control addresses au-9 for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-11 - Audit Record Retention

| Field | Value |
| --- | --- |
| Control code | `AU-11` |
| Control title | Audit Record Retention |
| What it is | This control addresses audit record retention for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-12 - Audit Record Generation

| Field | Value |
| --- | --- |
| Control code | `AU-12` |
| Control title | Audit Record Generation |
| What it is | This control addresses audit record generation for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-13 - Au-13

| Field | Value |
| --- | --- |
| Control code | `AU-13` |
| Control title | Au-13 |
| What it is | This control addresses au-13 for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

### AU-16 - Au-16

| Field | Value |
| --- | --- |
| Control code | `AU-16` |
| Control title | Au-16 |
| What it is | This control addresses au-16 for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Centralize logs, protect them from tampering, and review them on a recurring schedule. |
| Evidence / artifact | Audit logs, SIEM alerts, review signoff, exception tickets |
| Review frequency | Daily review for alerts; monthly formal review |

## Assessment, Authorization, and Monitoring (CA)

### CA-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `CA-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assess the control before use, track findings, and re-evaluate after changes. |
| Evidence / artifact | Assessment report, POA&M, authorization memo, monitoring dashboard |
| Review frequency | Before go-live and annual review |

### CA-2 - Control Assessments

| Field | Value |
| --- | --- |
| Control code | `CA-2` |
| Control title | Control Assessments |
| What it is | Enhancement to CA-2 (Control Assessments) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific independent assessors requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assess the control before use, track findings, and re-evaluate after changes. |
| Evidence / artifact | Assessment report, POA&M, authorization memo, monitoring dashboard |
| Review frequency | Before go-live and annual review |

### CA-2(1) - Independent Assessors

| Field | Value |
| --- | --- |
| Control code | `CA-2(1)` |
| Control title | Independent Assessors |
| What it is | Enhancement to CA-2 (Control Assessments) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific independent assessors requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CA-2(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CA-3 - Information Exchange

| Field | Value |
| --- | --- |
| Control code | `CA-3` |
| Control title | Information Exchange |
| What it is | This control addresses information exchange for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assess the control before use, track findings, and re-evaluate after changes. |
| Evidence / artifact | Assessment report, POA&M, authorization memo, monitoring dashboard |
| Review frequency | Before go-live and annual review |

### CA-5 - Plan of Action and Milestones

| Field | Value |
| --- | --- |
| Control code | `CA-5` |
| Control title | Plan of Action and Milestones |
| What it is | This control addresses plan of action and milestones for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assess the control before use, track findings, and re-evaluate after changes. |
| Evidence / artifact | Assessment report, POA&M, authorization memo, monitoring dashboard |
| Review frequency | Before go-live and annual review |

### CA-6 - Authorization

| Field | Value |
| --- | --- |
| Control code | `CA-6` |
| Control title | Authorization |
| What it is | This control addresses authorization for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assess the control before use, track findings, and re-evaluate after changes. |
| Evidence / artifact | Assessment report, POA&M, authorization memo, monitoring dashboard |
| Review frequency | Before go-live and annual review |

### CA-7 - Continuous Monitoring

| Field | Value |
| --- | --- |
| Control code | `CA-7` |
| Control title | Continuous Monitoring |
| What it is | Enhancement to CA-7 (Continuous Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific risk monitoring requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assess the control before use, track findings, and re-evaluate after changes. |
| Evidence / artifact | Assessment report, POA&M, authorization memo, monitoring dashboard |
| Review frequency | Before go-live and annual review |

### CA-7(1) - Independent Assessment

| Field | Value |
| --- | --- |
| Control code | `CA-7(1)` |
| Control title | Independent Assessment |
| What it is | Enhancement to CA-7 (Continuous Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific independent assessment requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CA-7(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CA-7(4) - Risk Monitoring

| Field | Value |
| --- | --- |
| Control code | `CA-7(4)` |
| Control title | Risk Monitoring |
| What it is | Enhancement to CA-7 (Continuous Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific risk monitoring requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CA-7(4) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CA-9 - Internal System Connections

| Field | Value |
| --- | --- |
| Control code | `CA-9` |
| Control title | Internal System Connections |
| What it is | This control addresses internal system connections for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Assess the control before use, track findings, and re-evaluate after changes. |
| Evidence / artifact | Assessment report, POA&M, authorization memo, monitoring dashboard |
| Review frequency | Before go-live and annual review |

## Configuration Management (CM)

### CM-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `CM-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-2 - Baseline Configuration

| Field | Value |
| --- | --- |
| Control code | `CM-2` |
| Control title | Baseline Configuration |
| What it is | Enhancement to CM-2 (Baseline Configuration) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific retention of previous configurations requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-2(2) - Automation Support for Accuracy and Currency

| Field | Value |
| --- | --- |
| Control code | `CM-2(2)` |
| Control title | Automation Support for Accuracy and Currency |
| What it is | Enhancement to CM-2 (Baseline Configuration) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automation support for accuracy and currency requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-2(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-2(3) - Retention of Previous Configurations

| Field | Value |
| --- | --- |
| Control code | `CM-2(3)` |
| Control title | Retention of Previous Configurations |
| What it is | Enhancement to CM-2 (Baseline Configuration) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific retention of previous configurations requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-2(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-2(7) - Configure Systems and Components for High-risk Areas

| Field | Value |
| --- | --- |
| Control code | `CM-2(7)` |
| Control title | Configure Systems and Components for High-risk Areas |
| What it is | Enhancement to CM-2 (Baseline Configuration) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific configure systems and components for high-risk areas requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-2(7) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-3 - Configuration Change Control

| Field | Value |
| --- | --- |
| Control code | `CM-3` |
| Control title | Configuration Change Control |
| What it is | Enhancement to CM-3 (Configuration Change Control) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific security and privacy representatives requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-3(2) - Testing, Validation, and Documentation of Changes

| Field | Value |
| --- | --- |
| Control code | `CM-3(2)` |
| Control title | Testing, Validation, and Documentation of Changes |
| What it is | Enhancement to CM-3 (Configuration Change Control) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific testing, validation, and documentation of changes requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-3(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-3(4) - Security and Privacy Representatives

| Field | Value |
| --- | --- |
| Control code | `CM-3(4)` |
| Control title | Security and Privacy Representatives |
| What it is | Enhancement to CM-3 (Configuration Change Control) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific security and privacy representatives requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-3(4) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-4 - Impact Analyses

| Field | Value |
| --- | --- |
| Control code | `CM-4` |
| Control title | Impact Analyses |
| What it is | Enhancement to CM-4 (Impact Analyses) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific verification of controls requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-4(2) - Verification of Controls

| Field | Value |
| --- | --- |
| Control code | `CM-4(2)` |
| Control title | Verification of Controls |
| What it is | Enhancement to CM-4 (Impact Analyses) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific verification of controls requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-4(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-5 - Access Restrictions for Change

| Field | Value |
| --- | --- |
| Control code | `CM-5` |
| Control title | Access Restrictions for Change |
| What it is | This control addresses access restrictions for change for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-6 - Configuration Settings

| Field | Value |
| --- | --- |
| Control code | `CM-6` |
| Control title | Configuration Settings |
| What it is | This control addresses configuration settings for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-7 - Least Functionality

| Field | Value |
| --- | --- |
| Control code | `CM-7` |
| Control title | Least Functionality |
| What it is | Enhancement to CM-7 (Least Functionality) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prevent program execution requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-7(1) - Periodic Review

| Field | Value |
| --- | --- |
| Control code | `CM-7(1)` |
| Control title | Periodic Review |
| What it is | Enhancement to CM-7 (Least Functionality) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific periodic review requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-7(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-7(2) - Prevent Program Execution

| Field | Value |
| --- | --- |
| Control code | `CM-7(2)` |
| Control title | Prevent Program Execution |
| What it is | Enhancement to CM-7 (Least Functionality) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prevent program execution requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-7(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-7(5) - Authorized Software \227 Allow-by-exception

| Field | Value |
| --- | --- |
| Control code | `CM-7(5)` |
| Control title | Authorized Software \227 Allow-by-exception |
| What it is | Enhancement to CM-7 (Least Functionality) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific authorized software \227 allow-by-exception requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-7(5) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-8 - System Component Inventory

| Field | Value |
| --- | --- |
| Control code | `CM-8` |
| Control title | System Component Inventory |
| What it is | Enhancement to CM-8 (System Component Inventory) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated unauthorized component detection requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-8(1) - Updates During Installation and Removal

| Field | Value |
| --- | --- |
| Control code | `CM-8(1)` |
| Control title | Updates During Installation and Removal |
| What it is | Enhancement to CM-8 (System Component Inventory) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific updates during installation and removal requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-8(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-8(3) - Automated Unauthorized Component Detection

| Field | Value |
| --- | --- |
| Control code | `CM-8(3)` |
| Control title | Automated Unauthorized Component Detection |
| What it is | Enhancement to CM-8 (System Component Inventory) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated unauthorized component detection requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-8(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CM-9 - Configuration Management Plan

| Field | Value |
| --- | --- |
| Control code | `CM-9` |
| Control title | Configuration Management Plan |
| What it is | This control addresses configuration management plan for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-10 - Software Usage Restrictions

| Field | Value |
| --- | --- |
| Control code | `CM-10` |
| Control title | Software Usage Restrictions |
| What it is | This control addresses software usage restrictions for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-11 - User-installed Software

| Field | Value |
| --- | --- |
| Control code | `CM-11` |
| Control title | User-installed Software |
| What it is | This control addresses user-installed software for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-12 - Information Location

| Field | Value |
| --- | --- |
| Control code | `CM-12` |
| Control title | Information Location |
| What it is | Enhancement to CM-12 (Information Location) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated tools to support information location ................79 contingency planning (cp) requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use hardened baselines, change approval, and current asset inventory. |
| Evidence / artifact | Baseline standards, change tickets, inventory export, rollback record |
| Review frequency | Quarterly and after changes |

### CM-12(1) - Automated Tools to Support Information Location

| Field | Value |
| --- | --- |
| Control code | `CM-12(1)` |
| Control title | Automated Tools to Support Information Location |
| What it is | Enhancement to CM-12 (Information Location) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated tools to support information location ................79 contingency planning (cp) requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CM-12(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

## Contingency Planning (CP)

### CP-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `CP-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Keep backups, recovery procedures, and restoration testing current. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-2 - Contingency Plan

| Field | Value |
| --- | --- |
| Control code | `CP-2` |
| Control title | Contingency Plan |
| What it is | Enhancement to CP-2 (Contingency Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identify critical assets requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-2(1) - Coordinate with Related Plans

| Field | Value |
| --- | --- |
| Control code | `CP-2(1)` |
| Control title | Coordinate with Related Plans |
| What it is | Enhancement to CP-2 (Contingency Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordinate with related plans requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-2(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-2(3) - Resume Mission and Business Functions

| Field | Value |
| --- | --- |
| Control code | `CP-2(3)` |
| Control title | Resume Mission and Business Functions |
| What it is | Enhancement to CP-2 (Contingency Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific resume mission and business functions requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-2(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-2(8) - Identify Critical Assets

| Field | Value |
| --- | --- |
| Control code | `CP-2(8)` |
| Control title | Identify Critical Assets |
| What it is | Enhancement to CP-2 (Contingency Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identify critical assets requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-2(8) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-3 - Contingency Training

| Field | Value |
| --- | --- |
| Control code | `CP-3` |
| Control title | Contingency Training |
| What it is | This control addresses contingency training for CJIS systems, users, or data. |
| Recommended approach | Keep backups, recovery procedures, and restoration testing current. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-4 - Contingency Plan Testing

| Field | Value |
| --- | --- |
| Control code | `CP-4` |
| Control title | Contingency Plan Testing |
| What it is | Enhancement to CP-4 (Contingency Plan Testing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordinate with related plans requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-4(1) - Coordinate with Related Plans

| Field | Value |
| --- | --- |
| Control code | `CP-4(1)` |
| Control title | Coordinate with Related Plans |
| What it is | Enhancement to CP-4 (Contingency Plan Testing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordinate with related plans requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-4(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-6 - Alternate Storage Site

| Field | Value |
| --- | --- |
| Control code | `CP-6` |
| Control title | Alternate Storage Site |
| What it is | Enhancement to CP-6 (Alternate Storage Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific accessibility requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-6(1) - Separation from Primary Site

| Field | Value |
| --- | --- |
| Control code | `CP-6(1)` |
| Control title | Separation from Primary Site |
| What it is | Enhancement to CP-6 (Alternate Storage Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific separation from primary site requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-6(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-6(3) - Accessibility

| Field | Value |
| --- | --- |
| Control code | `CP-6(3)` |
| Control title | Accessibility |
| What it is | Enhancement to CP-6 (Alternate Storage Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific accessibility requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-6(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-7 - Alternate Processing Site

| Field | Value |
| --- | --- |
| Control code | `CP-7` |
| Control title | Alternate Processing Site |
| What it is | Enhancement to CP-7 (Alternate Processing Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific priority of service requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-7(1) - Separation from Primary Site

| Field | Value |
| --- | --- |
| Control code | `CP-7(1)` |
| Control title | Separation from Primary Site |
| What it is | Enhancement to CP-7 (Alternate Processing Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific separation from primary site requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-7(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-7(2) - Accessibility

| Field | Value |
| --- | --- |
| Control code | `CP-7(2)` |
| Control title | Accessibility |
| What it is | Enhancement to CP-7 (Alternate Processing Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific accessibility requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-7(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-7(3) - Priority of Service

| Field | Value |
| --- | --- |
| Control code | `CP-7(3)` |
| Control title | Priority of Service |
| What it is | Enhancement to CP-7 (Alternate Processing Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific priority of service requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-7(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-8 - Telecommunications Services

| Field | Value |
| --- | --- |
| Control code | `CP-8` |
| Control title | Telecommunications Services |
| What it is | Enhancement to CP-8 (Telecommunications Services) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific single points of failure requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-8(1) - Priority of Service Provisions

| Field | Value |
| --- | --- |
| Control code | `CP-8(1)` |
| Control title | Priority of Service Provisions |
| What it is | Enhancement to CP-8 (Telecommunications Services) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific priority of service provisions requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-8(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-8(2) - Single Points of Failure

| Field | Value |
| --- | --- |
| Control code | `CP-8(2)` |
| Control title | Single Points of Failure |
| What it is | Enhancement to CP-8 (Telecommunications Services) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific single points of failure requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-8(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-9 - System Backup

| Field | Value |
| --- | --- |
| Control code | `CP-9` |
| Control title | System Backup |
| What it is | Enhancement to CP-9 (System Backup) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-9(1) - Testing for Reliability and Integrity

| Field | Value |
| --- | --- |
| Control code | `CP-9(1)` |
| Control title | Testing for Reliability and Integrity |
| What it is | Enhancement to CP-9 (System Backup) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific testing for reliability and integrity .................................................89 ix 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-9(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-9(8) - Cryptographic Protection

| Field | Value |
| --- | --- |
| Control code | `CP-9(8)` |
| Control title | Cryptographic Protection |
| What it is | Enhancement to CP-9 (System Backup) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-9(8) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### CP-10 - System Recovery and Reconstitution

| Field | Value |
| --- | --- |
| Control code | `CP-10` |
| Control title | System Recovery and Reconstitution |
| What it is | Enhancement to CP-10 (System Recovery and Reconstitution) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific transaction recovery .....................................90 identification and authentication (ia) requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Maintain recovery plans, backups, and restoration tests for CJIS systems. |
| Evidence / artifact | BCP/DR plan, backup reports, restore test results |
| Review frequency | Annual test and update |

### CP-10(2) - Transaction Recovery

| Field | Value |
| --- | --- |
| Control code | `CP-10(2)` |
| Control title | Transaction Recovery |
| What it is | Enhancement to CP-10 (System Recovery and Reconstitution) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific transaction recovery .....................................90 identification and authentication (ia) requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to CP-10(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

## Identification and Authentication (IA)

### IA-0 - Use of Originating Agency Identifiers in Transactions and Information Exchanges

| Field | Value |
| --- | --- |
| Control code | `IA-0` |
| Control title | Use of Originating Agency Identifiers in Transactions and Information Exchanges |
| What it is | This control addresses use of originating agency identifiers in transactions and information exchanges for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `IA-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-2 - Identification and Authentication (Organizational Users)

| Field | Value |
| --- | --- |
| Control code | `IA-2` |
| Control title | Identification and Authentication (Organizational Users) |
| What it is | This control addresses identification and authentication \(organizational users\) for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-3 - Device Identification and Authentication

| Field | Value |
| --- | --- |
| Control code | `IA-3` |
| Control title | Device Identification and Authentication |
| What it is | This control addresses device identification and authentication for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-4 - Identifier Management

| Field | Value |
| --- | --- |
| Control code | `IA-4` |
| Control title | Identifier Management |
| What it is | Enhancement to IA-4 (Identifier Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identify user status requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-4(4) - Identify User Status

| Field | Value |
| --- | --- |
| Control code | `IA-4(4)` |
| Control title | Identify User Status |
| What it is | Enhancement to IA-4 (Identifier Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identify user status requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IA-4(4) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IA-5 - Authenticator Management

| Field | Value |
| --- | --- |
| Control code | `IA-5` |
| Control title | Authenticator Management |
| What it is | Enhancement to IA-5 (Authenticator Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific protection of authenticators requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-5(1) - Authenticator Types

| Field | Value |
| --- | --- |
| Control code | `IA-5(1)` |
| Control title | Authenticator Types |
| What it is | Enhancement to IA-5 (Authenticator Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific authenticator types ....................................................118 (a) memorized secret authenticators and verifiers: .................................................. 118 (b) look-up secret authenticators and verifiers ...................................................... 123 (c) out-of-band authenticators and verifiers ............................................................ 125 (d) otp authenticators and verifiers ......................................................................... 130 (e) cryptographic authenticators and verifiers (including single- and multi-factor cryptographic authenticators, both hardware- and software-based) ...................... requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IA-5(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IA-5(2) - Public Key Based Authentication

| Field | Value |
| --- | --- |
| Control code | `IA-5(2)` |
| Control title | Public Key Based Authentication |
| What it is | Enhancement to IA-5 (Authenticator Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific public key based authentication requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IA-5(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IA-5(6) - Protection of Authenticators

| Field | Value |
| --- | --- |
| Control code | `IA-5(6)` |
| Control title | Protection of Authenticators |
| What it is | Enhancement to IA-5 (Authenticator Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific protection of authenticators requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IA-5(6) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IA-6 - Authentication Feedback

| Field | Value |
| --- | --- |
| Control code | `IA-6` |
| Control title | Authentication Feedback |
| What it is | This control addresses authentication feedback for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-7 - Cryptographic Module Authenticationf

| Field | Value |
| --- | --- |
| Control code | `IA-7` |
| Control title | Cryptographic Module Authenticationf |
| What it is | This control addresses ia-7 for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-8 - Identification and Authentication (Non-organizational Users)

| Field | Value |
| --- | --- |
| Control code | `IA-8` |
| Control title | Identification and Authentication (Non-organizational Users) |
| What it is | This control addresses identification and authentication \(non-organizational users\) for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-11 - Re-authentication

| Field | Value |
| --- | --- |
| Control code | `IA-11` |
| Control title | Re-authentication |
| What it is | This control addresses re-authentication for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-12 - Identity Proofing

| Field | Value |
| --- | --- |
| Control code | `IA-12` |
| Control title | Identity Proofing |
| What it is | Enhancement to IA-12 (Identity Proofing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific address confirmation ..................................................................164 incident response (ir) requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Issue unique identities, require strong authentication, and control credential lifecycle. |
| Evidence / artifact | MFA enrollment evidence, account provisioning records, reset tickets |
| Review frequency | Annual review and on change |

### IA-12(2) - Identity Evidence

| Field | Value |
| --- | --- |
| Control code | `IA-12(2)` |
| Control title | Identity Evidence |
| What it is | Enhancement to IA-12 (Identity Proofing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identity evidence requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IA-12(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IA-12(3) - Identity Evidence Validation and Verification

| Field | Value |
| --- | --- |
| Control code | `IA-12(3)` |
| Control title | Identity Evidence Validation and Verification |
| What it is | Enhancement to IA-12 (Identity Proofing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identity evidence validation and verification requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IA-12(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IA-12(5) - Address Confirmation

| Field | Value |
| --- | --- |
| Control code | `IA-12(5)` |
| Control title | Address Confirmation |
| What it is | Enhancement to IA-12 (Identity Proofing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific address confirmation ..................................................................164 incident response (ir) requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IA-12(5) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

## Incident Response (IR)

### IR-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `IR-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses ir-1 for CJIS systems, users, or data. |
| Recommended approach | Use a clear reporting path and preserve evidence during every incident. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use a documented intake, containment, notification, and recovery process. |
| Evidence / artifact | Incident tickets, timeline, evidence log, after-action report |
| Review frequency | After each incident; annual exercise |

### IR-2 - Incident Response Training

| Field | Value |
| --- | --- |
| Control code | `IR-2` |
| Control title | Incident Response Training |
| What it is | Enhancement to IR-2 (Incident Response Training) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific breach ..........................................................................168 x 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use a documented intake, containment, notification, and recovery process. |
| Evidence / artifact | Incident tickets, timeline, evidence log, after-action report |
| Review frequency | After each incident; annual exercise |

### IR-2(3) - Breach

| Field | Value |
| --- | --- |
| Control code | `IR-2(3)` |
| Control title | Breach |
| What it is | Enhancement to IR-2 (Incident Response Training) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific breach ..........................................................................168 x 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IR-2(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IR-3 - Incident Response Testing

| Field | Value |
| --- | --- |
| Control code | `IR-3` |
| Control title | Incident Response Testing |
| What it is | Enhancement to IR-3 (Incident Response Testing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordination with related plans requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use a documented intake, containment, notification, and recovery process. |
| Evidence / artifact | Incident tickets, timeline, evidence log, after-action report |
| Review frequency | After each incident; annual exercise |

### IR-3(2) - Coordination with Related Plans

| Field | Value |
| --- | --- |
| Control code | `IR-3(2)` |
| Control title | Coordination with Related Plans |
| What it is | Enhancement to IR-3 (Incident Response Testing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordination with related plans requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IR-3(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IR-4 - Incident Handling

| Field | Value |
| --- | --- |
| Control code | `IR-4` |
| Control title | Incident Handling |
| What it is | Enhancement to IR-4 (Incident Handling) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated incident handling processes requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use a documented intake, containment, notification, and recovery process. |
| Evidence / artifact | Incident tickets, timeline, evidence log, after-action report |
| Review frequency | After each incident; annual exercise |

### IR-4(1) - Automated Incident Handling Processes

| Field | Value |
| --- | --- |
| Control code | `IR-4(1)` |
| Control title | Automated Incident Handling Processes |
| What it is | Enhancement to IR-4 (Incident Handling) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated incident handling processes requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IR-4(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IR-5 - Incident Monitoring

| Field | Value |
| --- | --- |
| Control code | `IR-5` |
| Control title | Incident Monitoring |
| What it is | This control addresses incident monitoring for CJIS systems, users, or data. |
| Recommended approach | Use a clear reporting path and preserve evidence during every incident. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use a documented intake, containment, notification, and recovery process. |
| Evidence / artifact | Incident tickets, timeline, evidence log, after-action report |
| Review frequency | After each incident; annual exercise |

### IR-6 - Incident Reporting

| Field | Value |
| --- | --- |
| Control code | `IR-6` |
| Control title | Incident Reporting |
| What it is | Enhancement to IR-6 (Incident Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific supply chain coordination requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use a documented intake, containment, notification, and recovery process. |
| Evidence / artifact | Incident tickets, timeline, evidence log, after-action report |
| Review frequency | After each incident; annual exercise |

### IR-6(1) - Automated Reporting

| Field | Value |
| --- | --- |
| Control code | `IR-6(1)` |
| Control title | Automated Reporting |
| What it is | Enhancement to IR-6 (Incident Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated reporting requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IR-6(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IR-6(3) - Supply Chain Coordination

| Field | Value |
| --- | --- |
| Control code | `IR-6(3)` |
| Control title | Supply Chain Coordination |
| What it is | Enhancement to IR-6 (Incident Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific supply chain coordination requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IR-6(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IR-7 - Incident Response Assistance

| Field | Value |
| --- | --- |
| Control code | `IR-7` |
| Control title | Incident Response Assistance |
| What it is | Enhancement to IR-7 (Incident Response Assistance) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automation support for availability of information and support10f requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use a documented intake, containment, notification, and recovery process. |
| Evidence / artifact | Incident tickets, timeline, evidence log, after-action report |
| Review frequency | After each incident; annual exercise |

### IR-7(1) - Automation Support for Availability of Information and Support10f

| Field | Value |
| --- | --- |
| Control code | `IR-7(1)` |
| Control title | Automation Support for Availability of Information and Support10f |
| What it is | Enhancement to IR-7 (Incident Response Assistance) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automation support for availability of information and support10f requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IR-7(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### IR-8 - Incident Response Plan

| Field | Value |
| --- | --- |
| Control code | `IR-8` |
| Control title | Incident Response Plan |
| What it is | Enhancement to IR-8 (Incident Response Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific breaches .............................................................................173 maintenance (ma) requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Use a documented intake, containment, notification, and recovery process. |
| Evidence / artifact | Incident tickets, timeline, evidence log, after-action report |
| Review frequency | After each incident; annual exercise |

### IR-8(1) - Breaches

| Field | Value |
| --- | --- |
| Control code | `IR-8(1)` |
| Control title | Breaches |
| What it is | Enhancement to IR-8 (Incident Response Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific breaches .............................................................................173 maintenance (ma) requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to IR-8(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

## Maintenance (MA)

### MA-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `MA-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Approve maintenance, monitor work, and log results before returning to service. |
| Evidence / artifact | Maintenance log, vendor approval, escort record, return-to-service note |
| Review frequency | Each maintenance event; annual review |

### MA-2 - Controlled Maintenance

| Field | Value |
| --- | --- |
| Control code | `MA-2` |
| Control title | Controlled Maintenance |
| What it is | This control addresses controlled maintenance for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Approve maintenance, monitor work, and log results before returning to service. |
| Evidence / artifact | Maintenance log, vendor approval, escort record, return-to-service note |
| Review frequency | Each maintenance event; annual review |

### MA-3 - Maintenance Tools

| Field | Value |
| --- | --- |
| Control code | `MA-3` |
| Control title | Maintenance Tools |
| What it is | Enhancement to MA-3 (Maintenance Tools) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prevent unauthorized removal requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Approve maintenance, monitor work, and log results before returning to service. |
| Evidence / artifact | Maintenance log, vendor approval, escort record, return-to-service note |
| Review frequency | Each maintenance event; annual review |

### MA-3(1) - Inspect Tools

| Field | Value |
| --- | --- |
| Control code | `MA-3(1)` |
| Control title | Inspect Tools |
| What it is | Enhancement to MA-3 (Maintenance Tools) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific inspect tools requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to MA-3(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### MA-3(2) - Inspect Media

| Field | Value |
| --- | --- |
| Control code | `MA-3(2)` |
| Control title | Inspect Media |
| What it is | Enhancement to MA-3 (Maintenance Tools) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific inspect media requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to MA-3(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### MA-3(3) - Prevent Unauthorized Removal

| Field | Value |
| --- | --- |
| Control code | `MA-3(3)` |
| Control title | Prevent Unauthorized Removal |
| What it is | Enhancement to MA-3 (Maintenance Tools) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prevent unauthorized removal requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to MA-3(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### MA-4 - Nonlocal Maintenance

| Field | Value |
| --- | --- |
| Control code | `MA-4` |
| Control title | Nonlocal Maintenance |
| What it is | This control addresses ma-4 for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Approve maintenance, monitor work, and log results before returning to service. |
| Evidence / artifact | Maintenance log, vendor approval, escort record, return-to-service note |
| Review frequency | Each maintenance event; annual review |

### MA-5 - Maintenance Personnel

| Field | Value |
| --- | --- |
| Control code | `MA-5` |
| Control title | Maintenance Personnel |
| What it is | This control addresses maintenance personnel for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Approve maintenance, monitor work, and log results before returning to service. |
| Evidence / artifact | Maintenance log, vendor approval, escort record, return-to-service note |
| Review frequency | Each maintenance event; annual review |

### MA-6 - Timely Maintenance

| Field | Value |
| --- | --- |
| Control code | `MA-6` |
| Control title | Timely Maintenance |
| What it is | This control addresses timely maintenance for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Approve maintenance, monitor work, and log results before returning to service. |
| Evidence / artifact | Maintenance log, vendor approval, escort record, return-to-service note |
| Review frequency | Each maintenance event; annual review |

## Media Protection (MP)

### MP-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `MP-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Label, store, transport, and sanitize CJIS media under chain-of-custody controls. |
| Evidence / artifact | Media inventory, checkout log, destruction certificate |
| Review frequency | Monthly inventory; per disposal event |

### MP-2 - Media Access

| Field | Value |
| --- | --- |
| Control code | `MP-2` |
| Control title | Media Access |
| What it is | This control addresses media access for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Label, store, transport, and sanitize CJIS media under chain-of-custody controls. |
| Evidence / artifact | Media inventory, checkout log, destruction certificate |
| Review frequency | Monthly inventory; per disposal event |

### MP-3 - Media Marking

| Field | Value |
| --- | --- |
| Control code | `MP-3` |
| Control title | Media Marking |
| What it is | This control addresses media marking for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Label, store, transport, and sanitize CJIS media under chain-of-custody controls. |
| Evidence / artifact | Media inventory, checkout log, destruction certificate |
| Review frequency | Monthly inventory; per disposal event |

### MP-4 - Media Storage

| Field | Value |
| --- | --- |
| Control code | `MP-4` |
| Control title | Media Storage |
| What it is | This control addresses media storage for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Label, store, transport, and sanitize CJIS media under chain-of-custody controls. |
| Evidence / artifact | Media inventory, checkout log, destruction certificate |
| Review frequency | Monthly inventory; per disposal event |

### MP-5 - Media Transport

| Field | Value |
| --- | --- |
| Control code | `MP-5` |
| Control title | Media Transport |
| What it is | This control addresses media transport for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Label, store, transport, and sanitize CJIS media under chain-of-custody controls. |
| Evidence / artifact | Media inventory, checkout log, destruction certificate |
| Review frequency | Monthly inventory; per disposal event |

### MP-6 - Media Sanitization

| Field | Value |
| --- | --- |
| Control code | `MP-6` |
| Control title | Media Sanitization |
| What it is | This control addresses media sanitization for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Label, store, transport, and sanitize CJIS media under chain-of-custody controls. |
| Evidence / artifact | Media inventory, checkout log, destruction certificate |
| Review frequency | Monthly inventory; per disposal event |

### MP-7 - Media Use

| Field | Value |
| --- | --- |
| Control code | `MP-7` |
| Control title | Media Use |
| What it is | This control addresses media use for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Label, store, transport, and sanitize CJIS media under chain-of-custody controls. |
| Evidence / artifact | Media inventory, checkout log, destruction certificate |
| Review frequency | Monthly inventory; per disposal event |

## Physical and Environmental Protection (PE)

### PE-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `PE-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-2 - Physical Access Authorizations

| Field | Value |
| --- | --- |
| Control code | `PE-2` |
| Control title | Physical Access Authorizations |
| What it is | This control addresses physical access authorizations for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-3 - Physical Access Control

| Field | Value |
| --- | --- |
| Control code | `PE-3` |
| Control title | Physical Access Control |
| What it is | This control addresses pe-3 for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-4 - Access Control for Transmission

| Field | Value |
| --- | --- |
| Control code | `PE-4` |
| Control title | Access Control for Transmission |
| What it is | This control addresses access control for transmission for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-5 - Access Control for Output Devices

| Field | Value |
| --- | --- |
| Control code | `PE-5` |
| Control title | Access Control for Output Devices |
| What it is | This control addresses access control for output devices for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-6 - Monitoring Physical Access

| Field | Value |
| --- | --- |
| Control code | `PE-6` |
| Control title | Monitoring Physical Access |
| What it is | This control addresses pe-6 for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-8 - Visitor Access Records

| Field | Value |
| --- | --- |
| Control code | `PE-8` |
| Control title | Visitor Access Records |
| What it is | Enhancement to PE-8 (Visitor Access Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-8(3) - Limit Personally Identifiable Information Elements

| Field | Value |
| --- | --- |
| Control code | `PE-8(3)` |
| Control title | Limit Personally Identifiable Information Elements |
| What it is | Enhancement to PE-8 (Visitor Access Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to PE-8(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### PE-9 - Power Equipment and Cabling

| Field | Value |
| --- | --- |
| Control code | `PE-9` |
| Control title | Power Equipment and Cabling |
| What it is | This control addresses power equipment and cabling for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-10 - Emergency Shutoff

| Field | Value |
| --- | --- |
| Control code | `PE-10` |
| Control title | Emergency Shutoff |
| What it is | This control addresses emergency shutoff for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-11 - Emergency Power

| Field | Value |
| --- | --- |
| Control code | `PE-11` |
| Control title | Emergency Power |
| What it is | This control addresses emergency power for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-12 - Emergency Lighting

| Field | Value |
| --- | --- |
| Control code | `PE-12` |
| Control title | Emergency Lighting |
| What it is | This control addresses emergency lighting for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-13 - Fire Protection

| Field | Value |
| --- | --- |
| Control code | `PE-13` |
| Control title | Fire Protection |
| What it is | This control addresses fire protection for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-13(1) - Detection Systems \227 Automatic Activation and Notification

| Field | Value |
| --- | --- |
| Control code | `PE-13(1)` |
| Control title | Detection Systems \227 Automatic Activation and Notification |
| What it is | Enhancement to PE-13 (Fire Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific detection systems \227 automatic activation and notification requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to PE-13(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### PE-14 - Environmental Controls

| Field | Value |
| --- | --- |
| Control code | `PE-14` |
| Control title | Environmental Controls |
| What it is | This control addresses environmental controls for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-15 - Water Damage Protection

| Field | Value |
| --- | --- |
| Control code | `PE-15` |
| Control title | Water Damage Protection |
| What it is | This control addresses water damage protection for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-16 - Delivery and Removal

| Field | Value |
| --- | --- |
| Control code | `PE-16` |
| Control title | Delivery and Removal |
| What it is | This control addresses delivery and removal for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

### PE-17 - Alternate Work Site

| Field | Value |
| --- | --- |
| Control code | `PE-17` |
| Control title | Alternate Work Site |
| What it is | This control addresses alternate work site for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Restrict facility access and protect devices, cabling, and environmental conditions. |
| Evidence / artifact | Badge report, visitor log, inspection checklist, camera log |
| Review frequency | Quarterly and after facility changes |

## Planning (PL)

### PL-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `PL-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Document system security, privacy, and baseline decisions before changes go live. |
| Evidence / artifact | System security plan, architecture notes, baseline approvals |
| Review frequency | Annual review and after major change |

### PL-2 - System Security and Privacy Plans

| Field | Value |
| --- | --- |
| Control code | `PL-2` |
| Control title | System Security and Privacy Plans |
| What it is | This control addresses system security and privacy plans for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Document system security, privacy, and baseline decisions before changes go live. |
| Evidence / artifact | System security plan, architecture notes, baseline approvals |
| Review frequency | Annual review and after major change |

### PL-4 - Rules of Behavior

| Field | Value |
| --- | --- |
| Control code | `PL-4` |
| Control title | Rules of Behavior |
| What it is | This control addresses pl-4 for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Document system security, privacy, and baseline decisions before changes go live. |
| Evidence / artifact | System security plan, architecture notes, baseline approvals |
| Review frequency | Annual review and after major change |

### PL-8 - Security and Privacy Architectures

| Field | Value |
| --- | --- |
| Control code | `PL-8` |
| Control title | Security and Privacy Architectures |
| What it is | This control addresses security and privacy architectures for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Document system security, privacy, and baseline decisions before changes go live. |
| Evidence / artifact | System security plan, architecture notes, baseline approvals |
| Review frequency | Annual review and after major change |

### PL-9 - Central Management

| Field | Value |
| --- | --- |
| Control code | `PL-9` |
| Control title | Central Management |
| What it is | This control addresses central management for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Document system security, privacy, and baseline decisions before changes go live. |
| Evidence / artifact | System security plan, architecture notes, baseline approvals |
| Review frequency | Annual review and after major change |

### PL-10 - Baseline Selection

| Field | Value |
| --- | --- |
| Control code | `PL-10` |
| Control title | Baseline Selection |
| What it is | This control addresses baseline selection for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Document system security, privacy, and baseline decisions before changes go live. |
| Evidence / artifact | System security plan, architecture notes, baseline approvals |
| Review frequency | Annual review and after major change |

### PL-11 - Baseline Tailoring

| Field | Value |
| --- | --- |
| Control code | `PL-11` |
| Control title | Baseline Tailoring |
| What it is | This control addresses baseline tailoring for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Document system security, privacy, and baseline decisions before changes go live. |
| Evidence / artifact | System security plan, architecture notes, baseline approvals |
| Review frequency | Annual review and after major change |

### PL-7 - Pl-7

| Field | Value |
| --- | --- |
| Control code | `PL-7` |
| Control title | Pl-7 |
| What it is | This control addresses pl-7 for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Document system security, privacy, and baseline decisions before changes go live. |
| Evidence / artifact | System security plan, architecture notes, baseline approvals |
| Review frequency | Annual review and after major change |

## Personnel Security (PS)

### PS-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `PS-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

### PS-2 - Position Risk Designation

| Field | Value |
| --- | --- |
| Control code | `PS-2` |
| Control title | Position Risk Designation |
| What it is | This control addresses position risk designation for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

### PS-3 - Personnel Screening

| Field | Value |
| --- | --- |
| Control code | `PS-3` |
| Control title | Personnel Screening |
| What it is | This control addresses personnel screening for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

### PS-4 - Personnel Termination

| Field | Value |
| --- | --- |
| Control code | `PS-4` |
| Control title | Personnel Termination |
| What it is | This control addresses personnel termination for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

### PS-5 - Personnel Transfer

| Field | Value |
| --- | --- |
| Control code | `PS-5` |
| Control title | Personnel Transfer |
| What it is | This control addresses personnel transfer for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

### PS-6 - Access Agreements

| Field | Value |
| --- | --- |
| Control code | `PS-6` |
| Control title | Access Agreements |
| What it is | This control addresses access agreements for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

### PS-7 - External Personnel Security

| Field | Value |
| --- | --- |
| Control code | `PS-7` |
| Control title | External Personnel Security |
| What it is | This control addresses external personnel security for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

### PS-8 - Personnel Sanctions

| Field | Value |
| --- | --- |
| Control code | `PS-8` |
| Control title | Personnel Sanctions |
| What it is | This control addresses personnel sanctions for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

### PS-9 - Position Descriptions

| Field | Value |
| --- | --- |
| Control code | `PS-9` |
| Control title | Position Descriptions |
| What it is | This control addresses position descriptions for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Screen personnel, document access agreements, and remove access promptly on status changes. |
| Evidence / artifact | Background clearance, signed agreements, offboarding checklist |
| Review frequency | Each hire/exit; annual audit |

## Risk Assessment (RA)

### RA-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `RA-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Identify and prioritize risks, then track mitigation to closure. |
| Evidence / artifact | Risk register, scan results, mitigation plan, signoff |
| Review frequency | Annual and after material change |

### RA-2 - Security Categorization

| Field | Value |
| --- | --- |
| Control code | `RA-2` |
| Control title | Security Categorization |
| What it is | This control addresses security categorization for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Identify and prioritize risks, then track mitigation to closure. |
| Evidence / artifact | Risk register, scan results, mitigation plan, signoff |
| Review frequency | Annual and after material change |

### RA-3 - Risk Assessment

| Field | Value |
| --- | --- |
| Control code | `RA-3` |
| Control title | Risk Assessment |
| What it is | This control addresses ra-3 for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Identify and prioritize risks, then track mitigation to closure. |
| Evidence / artifact | Risk register, scan results, mitigation plan, signoff |
| Review frequency | Annual and after material change |

### RA-5 - Vulnerability Monitoring and Scanning

| Field | Value |
| --- | --- |
| Control code | `RA-5` |
| Control title | Vulnerability Monitoring and Scanning |
| What it is | Enhancement to RA-5 (Vulnerability Monitoring and Scanning) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific public disclosure program requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Identify and prioritize risks, then track mitigation to closure. |
| Evidence / artifact | Risk register, scan results, mitigation plan, signoff |
| Review frequency | Annual and after material change |

### RA-5(2) - Update Vulnerabilities to Be Scanned

| Field | Value |
| --- | --- |
| Control code | `RA-5(2)` |
| Control title | Update Vulnerabilities to Be Scanned |
| What it is | Enhancement to RA-5 (Vulnerability Monitoring and Scanning) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific update vulnerabilities to be scanned requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to RA-5(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### RA-5(5) - Privileged Access

| Field | Value |
| --- | --- |
| Control code | `RA-5(5)` |
| Control title | Privileged Access |
| What it is | Enhancement to RA-5 (Vulnerability Monitoring and Scanning) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific privileged access requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to RA-5(5) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### RA-5(11) - Public Disclosure Program

| Field | Value |
| --- | --- |
| Control code | `RA-5(11)` |
| Control title | Public Disclosure Program |
| What it is | Enhancement to RA-5 (Vulnerability Monitoring and Scanning) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific public disclosure program requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to RA-5(11) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### RA-7 - Risk Response

| Field | Value |
| --- | --- |
| Control code | `RA-7` |
| Control title | Risk Response |
| What it is | This control addresses risk response for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Identify and prioritize risks, then track mitigation to closure. |
| Evidence / artifact | Risk register, scan results, mitigation plan, signoff |
| Review frequency | Annual and after material change |

### RA-9 - Criticality Analysis

| Field | Value |
| --- | --- |
| Control code | `RA-9` |
| Control title | Criticality Analysis |
| What it is | This control addresses ra-9 for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Identify and prioritize risks, then track mitigation to closure. |
| Evidence / artifact | Risk register, scan results, mitigation plan, signoff |
| Review frequency | Annual and after material change |

### RA-8 - Ra-8

| Field | Value |
| --- | --- |
| Control code | `RA-8` |
| Control title | Ra-8 |
| What it is | This control addresses ra-8 for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Identify and prioritize risks, then track mitigation to closure. |
| Evidence / artifact | Risk register, scan results, mitigation plan, signoff |
| Review frequency | Annual and after material change |

## System and Services Acquisition / Development (SA)

### SA-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `SA-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-2 - Allocation of Resources

| Field | Value |
| --- | --- |
| Control code | `SA-2` |
| Control title | Allocation of Resources |
| What it is | This control addresses allocation of resources for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-3 - System Development Life Cycle

| Field | Value |
| --- | --- |
| Control code | `SA-3` |
| Control title | System Development Life Cycle |
| What it is | This control addresses system development life cycle for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-4 - Acquisition Process

| Field | Value |
| --- | --- |
| Control code | `SA-4` |
| Control title | Acquisition Process |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific use of approved piv products requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-4(1) - Functional Properties of Controls

| Field | Value |
| --- | --- |
| Control code | `SA-4(1)` |
| Control title | Functional Properties of Controls |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific functional properties of controls requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SA-4(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SA-4(2) - Design and Implementation Information for Controls

| Field | Value |
| --- | --- |
| Control code | `SA-4(2)` |
| Control title | Design and Implementation Information for Controls |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific design and implementation information for controls requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SA-4(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SA-4(9) - Functions, Ports, Protocols, and Services in Use

| Field | Value |
| --- | --- |
| Control code | `SA-4(9)` |
| Control title | Functions, Ports, Protocols, and Services in Use |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific functions, ports, protocols, and services in use requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SA-4(9) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SA-4(10) - Use of Approved Piv Products

| Field | Value |
| --- | --- |
| Control code | `SA-4(10)` |
| Control title | Use of Approved Piv Products |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific use of approved piv products requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SA-4(10) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SA-5 - System Documentation

| Field | Value |
| --- | --- |
| Control code | `SA-5` |
| Control title | System Documentation |
| What it is | This control addresses system documentation for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-8 - Security and Privacy Engineering Principles

| Field | Value |
| --- | --- |
| Control code | `SA-8` |
| Control title | Security and Privacy Engineering Principles |
| What it is | Enhancement to SA-8 (Security and Privacy Engineering Principles) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific minimization requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-8(33) - Minimization

| Field | Value |
| --- | --- |
| Control code | `SA-8(33)` |
| Control title | Minimization |
| What it is | Enhancement to SA-8 (Security and Privacy Engineering Principles) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific minimization requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SA-8(33) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SA-9 - External System Services

| Field | Value |
| --- | --- |
| Control code | `SA-9` |
| Control title | External System Services |
| What it is | This control addresses sa-9 for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-10 - Developer Configuration Management

| Field | Value |
| --- | --- |
| Control code | `SA-10` |
| Control title | Developer Configuration Management |
| What it is | This control addresses developer configuration management for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-11 - Developer Testing and Evaluation

| Field | Value |
| --- | --- |
| Control code | `SA-11` |
| Control title | Developer Testing and Evaluation |
| What it is | This control addresses developer testing and evaluation for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-15 - Development Process, Standards, and Tools

| Field | Value |
| --- | --- |
| Control code | `SA-15` |
| Control title | Development Process, Standards, and Tools |
| What it is | This control addresses development process, standards, and tools for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

### SA-22 - Unsupported System Components

| Field | Value |
| --- | --- |
| Control code | `SA-22` |
| Control title | Unsupported System Components |
| What it is | This control addresses unsupported system components for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Bake CJIS requirements into procurement, design, testing, and vendor acceptance. |
| Evidence / artifact | Security clauses, procurement checklist, test evidence, acceptance record |
| Review frequency | Per procurement/project |

## System and Communications Protection (SC)

### SC-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `SC-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-2 - Separation of System and User Functionality

| Field | Value |
| --- | --- |
| Control code | `SC-2` |
| Control title | Separation of System and User Functionality |
| What it is | This control addresses sc-2 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-4 - Information in Shared System Resources

| Field | Value |
| --- | --- |
| Control code | `SC-4` |
| Control title | Information in Shared System Resources |
| What it is | This control addresses information in shared system resources for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-5 - Denial-of-service Protection

| Field | Value |
| --- | --- |
| Control code | `SC-5` |
| Control title | Denial-of-service Protection |
| What it is | This control addresses denial-of-service protection for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-7 - Boundary Protection

| Field | Value |
| --- | --- |
| Control code | `SC-7` |
| Control title | Boundary Protection |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific personally identifiable information requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-7(3) - Access Points

| Field | Value |
| --- | --- |
| Control code | `SC-7(3)` |
| Control title | Access Points |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific access points requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SC-7(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SC-7(4) - External Telecommunications Services

| Field | Value |
| --- | --- |
| Control code | `SC-7(4)` |
| Control title | External Telecommunications Services |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific external telecommunications services requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SC-7(4) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SC-7(5) - Deny By Default \227 Allow By Exception

| Field | Value |
| --- | --- |
| Control code | `SC-7(5)` |
| Control title | Deny By Default \227 Allow By Exception |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific deny by default \227 allow by exception requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SC-7(5) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SC-7(7) - Split Tunneling for Remote Devices

| Field | Value |
| --- | --- |
| Control code | `SC-7(7)` |
| Control title | Split Tunneling for Remote Devices |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific split tunneling for remote devices requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SC-7(7) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SC-7(8) - Route Traffic to Authenticated Proxy Servers

| Field | Value |
| --- | --- |
| Control code | `SC-7(8)` |
| Control title | Route Traffic to Authenticated Proxy Servers |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific route traffic to authenticated proxy servers requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SC-7(8) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SC-7(24) - Personally Identifiable Information

| Field | Value |
| --- | --- |
| Control code | `SC-7(24)` |
| Control title | Personally Identifiable Information |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific personally identifiable information requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SC-7(24) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SC-8 - Transmission Confidentiality and Integrity

| Field | Value |
| --- | --- |
| Control code | `SC-8` |
| Control title | Transmission Confidentiality and Integrity |
| What it is | Enhancement to SC-8 (Transmission Confidentiality and Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-8(1) - Cryptographic Protection

| Field | Value |
| --- | --- |
| Control code | `SC-8(1)` |
| Control title | Cryptographic Protection |
| What it is | Enhancement to SC-8 (Transmission Confidentiality and Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SC-8(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SC-10 - Network Disconnect

| Field | Value |
| --- | --- |
| Control code | `SC-10` |
| Control title | Network Disconnect |
| What it is | This control addresses network disconnect for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-12 - Cryptographic Key Establishment and Management

| Field | Value |
| --- | --- |
| Control code | `SC-12` |
| Control title | Cryptographic Key Establishment and Management |
| What it is | This control addresses cryptographic key establishment and management for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-13 - Cryptographic Protection

| Field | Value |
| --- | --- |
| Control code | `SC-13` |
| Control title | Cryptographic Protection |
| What it is | This control addresses cryptographic protection for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-15 - Collaborative Computing Devices and Applications

| Field | Value |
| --- | --- |
| Control code | `SC-15` |
| Control title | Collaborative Computing Devices and Applications |
| What it is | This control addresses collaborative computing devices and applications for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-17 - Public Key Infrastructure Certificates

| Field | Value |
| --- | --- |
| Control code | `SC-17` |
| Control title | Public Key Infrastructure Certificates |
| What it is | This control addresses public key infrastructure certificates for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-18 - Mobile Code

| Field | Value |
| --- | --- |
| Control code | `SC-18` |
| Control title | Mobile Code |
| What it is | This control addresses mobile code for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-20 - Secure Name/address Resolution Service (Authoritative Source)

| Field | Value |
| --- | --- |
| Control code | `SC-20` |
| Control title | Secure Name/address Resolution Service (Authoritative Source) |
| What it is | This control addresses secure name/address resolution service \(authoritative source\) for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-21 - Secure Name/address Resolution Service (Recursive or Caching Resolver)

| Field | Value |
| --- | --- |
| Control code | `SC-21` |
| Control title | Secure Name/address Resolution Service (Recursive or Caching Resolver) |
| What it is | This control addresses secure name/address resolution service \(recursive or caching resolver\) for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-22 - Architecture and Provisioning for Name/address Resolution Service

| Field | Value |
| --- | --- |
| Control code | `SC-22` |
| Control title | Architecture and Provisioning for Name/address Resolution Service |
| What it is | This control addresses architecture and provisioning for name/address resolution service for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-23 - Session Authenticity

| Field | Value |
| --- | --- |
| Control code | `SC-23` |
| Control title | Session Authenticity |
| What it is | This control addresses session authenticity for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-28 - Protection of Information at Rest

| Field | Value |
| --- | --- |
| Control code | `SC-28` |
| Control title | Protection of Information at Rest |
| What it is | Enhancement to SC-28 (Protection of Information at Rest) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-28(1) - Cryptographic Protection

| Field | Value |
| --- | --- |
| Control code | `SC-28(1)` |
| Control title | Cryptographic Protection |
| What it is | Enhancement to SC-28 (Protection of Information at Rest) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SC-28(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SC-39 - Process Isolation

| Field | Value |
| --- | --- |
| Control code | `SC-39` |
| Control title | Process Isolation |
| What it is | This control addresses process isolation for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-3 - Sc-3

| Field | Value |
| --- | --- |
| Control code | `SC-3` |
| Control title | Sc-3 |
| What it is | This control addresses sc-3 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-43 - Sc-43

| Field | Value |
| --- | --- |
| Control code | `SC-43` |
| Control title | Sc-43 |
| What it is | This control addresses sc-43 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-30 - Sc-30

| Field | Value |
| --- | --- |
| Control code | `SC-30` |
| Control title | Sc-30 |
| What it is | This control addresses sc-30 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

### SC-32 - Sc-32

| Field | Value |
| --- | --- |
| Control code | `SC-32` |
| Control title | Sc-32 |
| What it is | This control addresses sc-32 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Protect data in transit and at rest, and control network boundaries and remote paths. |
| Evidence / artifact | Encryption standard, firewall rules, VPN config, architecture diagram |
| Review frequency | Quarterly and after changes |

## System and Information Integrity (SI)

### SI-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `SI-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-2 - Flaw Remediation

| Field | Value |
| --- | --- |
| Control code | `SI-2` |
| Control title | Flaw Remediation |
| What it is | Enhancement to SI-2 (Flaw Remediation) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated flaw remediation status requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-2(2) - Automated Flaw Remediation Status

| Field | Value |
| --- | --- |
| Control code | `SI-2(2)` |
| Control title | Automated Flaw Remediation Status |
| What it is | Enhancement to SI-2 (Flaw Remediation) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated flaw remediation status requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-2(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-3 - Malicious Code Protection

| Field | Value |
| --- | --- |
| Control code | `SI-3` |
| Control title | Malicious Code Protection |
| What it is | This control addresses malicious code protection for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-4 - System Monitoring

| Field | Value |
| --- | --- |
| Control code | `SI-4` |
| Control title | System Monitoring |
| What it is | Enhancement to SI-4 (System Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific system-generated alerts requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-4(2) - Automated Tools and Mechanisms for Real-time Analysis

| Field | Value |
| --- | --- |
| Control code | `SI-4(2)` |
| Control title | Automated Tools and Mechanisms for Real-time Analysis |
| What it is | Enhancement to SI-4 (System Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated tools and mechanisms for real-time analysis requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-4(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-4(4) - Inbound and Outbound Communications Traffic

| Field | Value |
| --- | --- |
| Control code | `SI-4(4)` |
| Control title | Inbound and Outbound Communications Traffic |
| What it is | Enhancement to SI-4 (System Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific inbound and outbound communications traffic requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-4(4) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-4(5) - System-generated Alerts

| Field | Value |
| --- | --- |
| Control code | `SI-4(5)` |
| Control title | System-generated Alerts |
| What it is | Enhancement to SI-4 (System Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific system-generated alerts requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-4(5) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-5 - Security Alerts, Advisories, and Directives

| Field | Value |
| --- | --- |
| Control code | `SI-5` |
| Control title | Security Alerts, Advisories, and Directives |
| What it is | This control addresses security alerts, advisories, and directives for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-7 - Software, Firmware, and Information Integrity

| Field | Value |
| --- | --- |
| Control code | `SI-7` |
| Control title | Software, Firmware, and Information Integrity |
| What it is | Enhancement to SI-7 (Software, Firmware, and Information Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific integration of detection and response requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-7(1) - Integrity Checks

| Field | Value |
| --- | --- |
| Control code | `SI-7(1)` |
| Control title | Integrity Checks |
| What it is | Enhancement to SI-7 (Software, Firmware, and Information Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific integrity checks requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-7(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-7(7) - Integration of Detection and Response

| Field | Value |
| --- | --- |
| Control code | `SI-7(7)` |
| Control title | Integration of Detection and Response |
| What it is | Enhancement to SI-7 (Software, Firmware, and Information Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific integration of detection and response requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-7(7) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-8 - Spam Protection

| Field | Value |
| --- | --- |
| Control code | `SI-8` |
| Control title | Spam Protection |
| What it is | Enhancement to SI-8 (Spam Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automatic updates requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-8(2) - Automatic Updates

| Field | Value |
| --- | --- |
| Control code | `SI-8(2)` |
| Control title | Automatic Updates |
| What it is | Enhancement to SI-8 (Spam Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automatic updates requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-8(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-10 - Information Input Validation

| Field | Value |
| --- | --- |
| Control code | `SI-10` |
| Control title | Information Input Validation |
| What it is | This control addresses information input validation for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-11 - Error Handling

| Field | Value |
| --- | --- |
| Control code | `SI-11` |
| Control title | Error Handling |
| What it is | This control addresses error handling for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-12 - Information Management and Retention

| Field | Value |
| --- | --- |
| Control code | `SI-12` |
| Control title | Information Management and Retention |
| What it is | Enhancement to SI-12 (Information Management and Retention) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific information disposal requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-12(1) - Limit Personally Identifiable Information Elements

| Field | Value |
| --- | --- |
| Control code | `SI-12(1)` |
| Control title | Limit Personally Identifiable Information Elements |
| What it is | Enhancement to SI-12 (Information Management and Retention) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-12(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-12(2) - Minimize Personally Identifiable Information in Testing, Training, and Research

| Field | Value |
| --- | --- |
| Control code | `SI-12(2)` |
| Control title | Minimize Personally Identifiable Information in Testing, Training, and Research |
| What it is | Enhancement to SI-12 (Information Management and Retention) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific minimize personally identifiable information in testing, training, and research requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-12(2) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-12(3) - Information Disposal

| Field | Value |
| --- | --- |
| Control code | `SI-12(3)` |
| Control title | Information Disposal |
| What it is | Enhancement to SI-12 (Information Management and Retention) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific information disposal requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SI-12(3) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SI-16 - Memory Protection

| Field | Value |
| --- | --- |
| Control code | `SI-16` |
| Control title | Memory Protection |
| What it is | This control addresses si-16 for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-18 - Si-18

| Field | Value |
| --- | --- |
| Control code | `SI-18` |
| Control title | Si-18 |
| What it is | This control addresses si-18 for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

### SI-19 - De-identification

| Field | Value |
| --- | --- |
| Control code | `SI-19` |
| Control title | De-identification |
| What it is | This control addresses si-19 for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Patch quickly, monitor for malicious activity, and validate integrity. |
| Evidence / artifact | Patch report, AV dashboard, alert tickets, integrity check results |
| Review frequency | Weekly patch review; continuous monitoring |

## Supply Chain Risk Management (SR)

### SR-1 - Policy and Procedures

| Field | Value |
| --- | --- |
| Control code | `SR-1` |
| Control title | Policy and Procedures |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |

### SR-2 - Supply Chain Risk Management Plan

| Field | Value |
| --- | --- |
| Control code | `SR-2` |
| Control title | Supply Chain Risk Management Plan |
| What it is | Enhancement to SR-2 (Supply Chain Risk Management Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific establish scrm team requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |

### SR-2(1) - Establish SCRM Team

| Field | Value |
| --- | --- |
| Control code | `SR-2(1)` |
| Control title | Establish SCRM Team |
| What it is | Enhancement to SR-2 (Supply Chain Risk Management Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific establish scrm team requirement and verify it through testing, review, or monitoring. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Apply the enhancement to the parent control configuration, then verify it in testing or monitoring. |
| Evidence / artifact | Proof of enhancement configuration, test result, or log review tied to SR-2(1) |
| Review frequency | After implementation and at the same recurring interval as the parent control |

### SR-5 - Acquisition Strategies, Tools, and Methods

| Field | Value |
| --- | --- |
| Control code | `SR-5` |
| Control title | Acquisition Strategies, Tools, and Methods |
| What it is | This control addresses acquisition strategies, tools, and methods for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |

### SR-8 - Notification Agreements

| Field | Value |
| --- | --- |
| Control code | `SR-8` |
| Control title | Notification Agreements |
| What it is | This control addresses notification agreements for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |

### SR-10 - Inspection of Systems or Components

| Field | Value |
| --- | --- |
| Control code | `SR-10` |
| Control title | Inspection of Systems or Components |
| What it is | This control addresses inspection of systems or components for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |

### SR-12 - Component Disposal

| Field | Value |
| --- | --- |
| Control code | `SR-12` |
| Control title | Component Disposal |
| What it is | This control addresses component disposal for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |

### SR-3 - Supply Chain Controls and Processes

| Field | Value |
| --- | --- |
| Control code | `SR-3` |
| Control title | Supply Chain Controls and Processes |
| What it is | This control addresses sr-3 for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |

### SR-6 - Supplier Assessments and Reviews

| Field | Value |
| --- | --- |
| Control code | `SR-6` |
| Control title | Supplier Assessments and Reviews |
| What it is | This control addresses sr-6 for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |

### SR-11 - Sr-11

| Field | Value |
| --- | --- |
| Control code | `SR-11` |
| Control title | Sr-11 |
| What it is | This control addresses sr-11 for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Primary owner | `[[CONTROL_OWNER]]` |
| Implementation method | Vet vendors and components, include security terms, and track lifecycle risk. |
| Evidence / artifact | Vendor questionnaire, contract clause record, risk review, lifecycle status |
| Review frequency | Annual and before purchase |
