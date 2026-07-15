# [[AGENCY_NAME]] CJIS Control Item Templates

This document provides one fill-in item for each CJIS control and enhancement in the current policy inventory. Each item includes a plain-language explanation and a recommended approach in addition to the agency-specific placeholders.

## Shared Placeholders

- `[[CONTROL_OWNER]]`
- `[[IMPLEMENTATION_NOTES]]`
- `[[EVIDENCE_ARTIFACTS]]`
- `[[REVIEW_FREQUENCY]]`
- `[[CONTROL_NOTES]]`
- `[[RISK_LEVEL]]`
- `[[EXCEPTION_REFERENCE]]`

## How To Use

- Replace the placeholders with agency-specific values.
- Use the explanation field as a quick training and review reference.
- Use the recommendation field as the starting point for local procedures and standards.
- Keep evidence current and tie it to the review cadence you choose.
- If you cannot implement a control as written, document the exception and compensating controls.

## Access Control (AC)

### AC-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AC-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [IA-1](#ia-1-policy-and-procedures), [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-2 - Account Management

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-2` |
| Control title | Account Management |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-5](#ac-5-separation-of-duties), [AC-6](#ac-6-least-privilege), [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AC-20](#ac-20-use-of-external-systems), [AU-2](#au-2-event-logging), [AU-12](#au-12-audit-record-generation), [CM-5](#cm-5-access-restrictions-for-change), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-4](#ia-4-identifier-management), [IA-5](#ia-5-authenticator-management), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-3](#ma-3-maintenance-tools), [MA-5](#ma-5-maintenance-personnel), [PE-2](#pe-2-physical-access-authorizations), [PL-4](#pl-4-rules-of-behavior), [PS-2](#ps-2-position-risk-designation), [PS-4](#ps-4-personnel-termination), [PS-5](#ps-5-personnel-transfer), [SC-7](#sc-7-boundary-protection), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection) |
| Related enhancements | [AC-2(1)](#ac-21-automated-system-account-management), [AC-2(2)](#ac-22-automated-temporary-and-emergency-account-management), [AC-2(3)](#ac-23-disable-accounts), [AC-2(4)](#ac-24-automated-audit-actions), [AC-2(5)](#ac-25-inactivity-logout), [AC-2(13)](#ac-213-disable-accounts-for-high-risk-individuals) |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable accounts for high-risk individuals requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-2(13)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-2(1) - Automated System Account Management

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-2(1)` |
| Control title | Automated System Account Management |
| Parent control | `AC-2` |
| Related controls | See parent control ([AC-2](#ac-2-account-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated system account management requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-2(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-2(2) - Automated Temporary and Emergency Account Management

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-2(2)` |
| Control title | Automated Temporary and Emergency Account Management |
| Parent control | `AC-2` |
| Related controls | See parent control ([AC-2](#ac-2-account-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated temporary and emergency account management requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-2(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-2(3) - Disable Accounts

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-2(3)` |
| Control title | Disable Accounts |
| Parent control | `AC-2` |
| Related controls | See parent control ([AC-2](#ac-2-account-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable accounts requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-2(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-2(4) - Automated Audit Actions

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-2(4)` |
| Control title | Automated Audit Actions |
| Parent control | `AC-2` |
| Related controls | See parent control ([AC-2](#ac-2-account-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated audit actions requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-2(4)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-2(5) - Inactivity Logout

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-2(5)` |
| Control title | Inactivity Logout |
| Parent control | `AC-2` |
| Related controls | See parent control ([AC-2](#ac-2-account-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific inactivity logout requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-2(5)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-2(13) - Disable Accounts for High-risk Individuals

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-2(13)` |
| Control title | Disable Accounts for High-risk Individuals |
| Parent control | `AC-2` |
| Related controls | See parent control ([AC-2](#ac-2-account-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable accounts for high-risk individuals requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-2(13)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-3 - Access Enforcement

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-3` |
| Control title | Access Enforcement |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-4](#ac-4-information-flow-enforcement), [AC-5](#ac-5-separation-of-duties), [AC-6](#ac-6-least-privilege), [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AC-19](#ac-19-access-control-for-mobile-devices), [AC-20](#ac-20-use-of-external-systems), [AC-21](#ac-21-information-sharing), [AC-22](#ac-22-publicly-accessible-content), [AT-2](#at-2-literacy-training-and-awareness), [AT-3](#at-3-role-based-training), [AU-9](#au-9-protection-of-audit-information), [CA-9](#ca-9-internal-system-connections), [CM-5](#cm-5-access-restrictions-for-change), [CM-11](#cm-11-user-installed-software), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-5](#ia-5-authenticator-management), [IA-6](#ia-6-authentication-feedback), [IA-7](#ia-7-cryptographic-module-authenticationf), [IA-11](#ia-11-re-authentication), [MA-3](#ma-3-maintenance-tools), [MA-4](#ma-4-nonlocal-maintenance), [MA-5](#ma-5-maintenance-personnel), [MP-4](#mp-4-media-storage), [PS-3](#ps-3-personnel-screening), [SC-2](#sc-2-separation-of-system-and-user-functionality), [SC-4](#sc-4-information-in-shared-system-resources), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SC-28](#sc-28-protection-of-information-at-rest), [SI-4](#si-4-system-monitoring), [SI-8](#si-8-spam-protection) |
| Related enhancements | [AC-3(14)](#ac-314-individual-access) |
| What it is | This control addresses access enforcement for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-3(14) - Individual Access

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-3(14)` |
| Control title | Individual Access |
| Parent control | `AC-3` |
| Related controls | See parent control ([AC-3](#ac-3-access-enforcement)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-3 (Access Enforcement) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific individual access requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-3(14)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-4 - Information Flow Enforcement

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-4` |
| Control title | Information Flow Enforcement |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-6](#ac-6-least-privilege), [AC-17](#ac-17-remote-access), [AC-19](#ac-19-access-control-for-mobile-devices), [AC-21](#ac-21-information-sharing), [CA-3](#ca-3-information-exchange), [CA-9](#ca-9-internal-system-connections), [CM-7](#cm-7-least-functionality), [SC-4](#sc-4-information-in-shared-system-resources), [SC-7](#sc-7-boundary-protection) |
| Related enhancements | None |
| What it is | This control addresses information flow enforcement for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-5 - Separation of Duties

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-5` |
| Control title | Separation of Duties |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-6](#ac-6-least-privilege), [AU-9](#au-9-protection-of-audit-information), [CM-5](#cm-5-access-restrictions-for-change), [CM-11](#cm-11-user-installed-software), [CP-9](#cp-9-system-backup), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-4](#ia-4-identifier-management), [IA-5](#ia-5-authenticator-management), [IA-12](#ia-12-identity-proofing), [MA-3](#ma-3-maintenance-tools), [MA-5](#ma-5-maintenance-personnel), [PS-2](#ps-2-position-risk-designation), [SA-8](#sa-8-security-and-privacy-engineering-principles) |
| Related enhancements | None |
| What it is | This control addresses separation of duties for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-6 - Least Privilege

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-6` |
| Control title | Least Privilege |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-5](#ac-5-separation-of-duties), [CM-5](#cm-5-access-restrictions-for-change), [CM-11](#cm-11-user-installed-software), [PL-2](#pl-2-system-security-and-privacy-plans), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-15](#sa-15-development-process-standards-and-tools) |
| Related enhancements | [AC-6(1)](#ac-61-authorize-access-to-security-functions), [AC-6(2)](#ac-62-non-privileged-access-for-nonsecurity-functions), [AC-6(5)](#ac-65-privileged-accounts), [AC-6(7)](#ac-67-review-of-user-privileges), [AC-6(9)](#ac-69-log-use-of-privileged-functions), [AC-6(10)](#ac-610-prohibit-non-privileged-users-from-executing-privileged-functions) |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prohibit non-privileged users from executing privileged functions requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-6(10)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-6(1) - Authorize Access to Security Functions

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-6(1)` |
| Control title | Authorize Access to Security Functions |
| Parent control | `AC-6` |
| Related controls | See parent control ([AC-6](#ac-6-least-privilege)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific authorize access to security functions requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-6(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-6(2) - Non-privileged Access for Nonsecurity Functions

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-6(2)` |
| Control title | Non-privileged Access for Nonsecurity Functions |
| Parent control | `AC-6` |
| Related controls | See parent control ([AC-6](#ac-6-least-privilege)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific non-privileged access for nonsecurity functions requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-6(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-6(5) - Privileged Accounts

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-6(5)` |
| Control title | Privileged Accounts |
| Parent control | `AC-6` |
| Related controls | See parent control ([AC-6](#ac-6-least-privilege)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific privileged accounts requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-6(5)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-6(7) - Review of User Privileges

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-6(7)` |
| Control title | Review of User Privileges |
| Parent control | `AC-6` |
| Related controls | See parent control ([AC-6](#ac-6-least-privilege)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific review of user privileges requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-6(7)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-6(9) - Log Use of Privileged Functions

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-6(9)` |
| Control title | Log Use of Privileged Functions |
| Parent control | `AC-6` |
| Related controls | See parent control ([AC-6](#ac-6-least-privilege)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific log use of privileged functions requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-6(9)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-6(10) - Prohibit Non-privileged Users from Executing Privileged Functions

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-6(10)` |
| Control title | Prohibit Non-privileged Users from Executing Privileged Functions |
| Parent control | `AC-6` |
| Related controls | See parent control ([AC-6](#ac-6-least-privilege)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-6 (Least Privilege) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prohibit non-privileged users from executing privileged functions requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-6(10)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-7 - Unsuccessful Logon Attempts

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-7` |
| Control title | Unsuccessful Logon Attempts |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AU-2](#au-2-event-logging), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [IA-5](#ia-5-authenticator-management) |
| Related enhancements | None |
| What it is | This control addresses unsuccessful logon attempts for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-8 - System Use Notification

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-8` |
| Control title | System Use Notification |
| Parent control | `N/A` |
| Related controls | [AC-14](#ac-14-permitted-actions-without-identification-or-authentication), [PL-4](#pl-4-rules-of-behavior), [SI-4](#si-4-system-monitoring) |
| Related enhancements | None |
| What it is | This control addresses system use notification for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-11 - Device Lock

Tags: #priority/p4 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-11` |
| Control title | Device Lock |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-7](#ac-7-unsuccessful-logon-attempts), [IA-11](#ia-11-re-authentication), [PL-4](#pl-4-rules-of-behavior) |
| Related enhancements | [AC-11(1)](#ac-111-pattern-hiding-displays) |
| What it is | Enhancement to AC-11 (Device Lock) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific pattern-hiding displays requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-11(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-11(1) - Pattern-hiding Displays

Tags: #priority/p4 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-11(1)` |
| Control title | Pattern-hiding Displays |
| Parent control | `AC-11` |
| Related controls | See parent control ([AC-11](#ac-11-device-lock)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-11 (Device Lock) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific pattern-hiding displays requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-11(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-12 - Session Termination

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AC-12` |
| Control title | Session Termination |
| Parent control | `N/A` |
| Related controls | [MA-4](#ma-4-nonlocal-maintenance), [SC-10](#sc-10-network-disconnect), [SC-23](#sc-23-session-authenticity) |
| Related enhancements | None |
| What it is | This control addresses session termination for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-14 - Permitted Actions without Identification or Authentication

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AC-14` |
| Control title | Permitted Actions without Identification or Authentication |
| Parent control | `N/A` |
| Related controls | [AC-8](#ac-8-system-use-notification), [IA-2](#ia-2-identification-and-authentication-organizational-users), [PL-2](#pl-2-system-security-and-privacy-plans) |
| Related enhancements | None |
| What it is | This control addresses permitted actions without identification or authentication for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-17 - Remote Access

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-17` |
| Control title | Remote Access |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [AC-18](#ac-18-wireless-access), [AC-19](#ac-19-access-control-for-mobile-devices), [AC-20](#ac-20-use-of-external-systems), [CA-3](#ca-3-information-exchange), [CM-10](#cm-10-software-usage-restrictions), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-3](#ia-3-device-identification-and-authentication), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-4](#ma-4-nonlocal-maintenance), [PE-17](#pe-17-alternate-work-site), [PL-2](#pl-2-system-security-and-privacy-plans), [PL-4](#pl-4-rules-of-behavior), [SC-10](#sc-10-network-disconnect), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SI-4](#si-4-system-monitoring) |
| Related enhancements | [AC-17(1)](#ac-171-monitoring-and-control), [AC-17(2)](#ac-172-protection-of-confidentiality-and-integrity-using-encryption), [AC-17(3)](#ac-173-managed-access-control-points), [AC-17(4)](#ac-174-privileged-commands-and-access) |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific privileged commands and access requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-17(4)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-17(1) - Monitoring and Control

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-17(1)` |
| Control title | Monitoring and Control |
| Parent control | `AC-17` |
| Related controls | See parent control ([AC-17](#ac-17-remote-access)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific monitoring and control requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-17(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-17(2) - Protection of Confidentiality and Integrity Using Encryption

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-17(2)` |
| Control title | Protection of Confidentiality and Integrity Using Encryption |
| Parent control | `AC-17` |
| Related controls | See parent control ([AC-17](#ac-17-remote-access)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific protection of confidentiality and integrity using encryption requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-17(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-17(3) - Managed Access Control Points

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-17(3)` |
| Control title | Managed Access Control Points |
| Parent control | `AC-17` |
| Related controls | See parent control ([AC-17](#ac-17-remote-access)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific managed access control points requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-17(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-17(4) - Privileged Commands and Access

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-17(4)` |
| Control title | Privileged Commands and Access |
| Parent control | `AC-17` |
| Related controls | See parent control ([AC-17](#ac-17-remote-access)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-17 (Remote Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific privileged commands and access requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-17(4)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-18 - Wireless Access

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-18` |
| Control title | Wireless Access |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-17](#ac-17-remote-access), [AC-19](#ac-19-access-control-for-mobile-devices), [CA-9](#ca-9-internal-system-connections), [CM-7](#cm-7-least-functionality), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-3](#ia-3-device-identification-and-authentication), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [PL-4](#pl-4-rules-of-behavior), [SI-4](#si-4-system-monitoring) |
| Related enhancements | [AC-18(1)](#ac-181-authentication-and-encryption), [AC-18(3)](#ac-183-disable-wireless-networking-32-vii-12272024-cjissecpol-v60) |
| What it is | Enhancement to AC-18 (Wireless Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable wireless networking ..........................................................32 vii 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-18(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-18(1) - Authentication and Encryption

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-18(1)` |
| Control title | Authentication and Encryption |
| Parent control | `AC-18` |
| Related controls | See parent control ([AC-18](#ac-18-wireless-access)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-18 (Wireless Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific authentication and encryption requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-18(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-18(3) - Disable Wireless Networking ..........................................................32 Vii 12/27/2024 CJISSECPOL V6.0

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-18(3)` |
| Control title | Disable Wireless Networking ..........................................................32 Vii 12/27/2024 CJISSECPOL V6.0 |
| Parent control | `AC-18` |
| Related controls | See parent control ([AC-18](#ac-18-wireless-access)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-18 (Wireless Access) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific disable wireless networking ..........................................................32 vii 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-18(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-19 - Access Control for Mobile Devices

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-19` |
| Control title | Access Control for Mobile Devices |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [AC-7](#ac-7-unsuccessful-logon-attempts), [AC-11](#ac-11-device-lock), [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AC-20](#ac-20-use-of-external-systems), [CA-9](#ca-9-internal-system-connections), [CM-2](#cm-2-baseline-configuration), [CM-6](#cm-6-configuration-settings), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-3](#ia-3-device-identification-and-authentication), [MP-2](#mp-2-media-access), [MP-4](#mp-4-media-storage), [MP-5](#mp-5-media-transport), [MP-7](#mp-7-media-use), [PL-4](#pl-4-rules-of-behavior), [SC-7](#sc-7-boundary-protection), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring) |
| Related enhancements | [AC-19(5)](#ac-195-full-device-or-container-based-encryption) |
| What it is | Enhancement to AC-19 (Access Control for Mobile Devices) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific full device or container-based encryption requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-19(5)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-19(5) - Full Device or Container-based Encryption

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-19(5)` |
| Control title | Full Device or Container-based Encryption |
| Parent control | `AC-19` |
| Related controls | See parent control ([AC-19](#ac-19-access-control-for-mobile-devices)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-19 (Access Control for Mobile Devices) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific full device or container-based encryption requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-19(5)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-20 - Use of External Systems

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-20` |
| Control title | Use of External Systems |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-17](#ac-17-remote-access), [AC-19](#ac-19-access-control-for-mobile-devices), [CA-3](#ca-3-information-exchange), [PL-2](#pl-2-system-security-and-privacy-plans), [PL-4](#pl-4-rules-of-behavior), [SA-9](#sa-9-external-system-services), [SC-7](#sc-7-boundary-protection) |
| Related enhancements | [AC-20(1)](#ac-201-limits-on-authorized-use), [AC-20(2)](#ac-202-portable-storage-devices-227-restricted-use) |
| What it is | Enhancement to AC-20 (Use of External Systems) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limits on authorized use requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-20(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-20(1) - Limits on Authorized Use

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-20(1)` |
| Control title | Limits on Authorized Use |
| Parent control | `AC-20` |
| Related controls | See parent control ([AC-20](#ac-20-use-of-external-systems)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-20 (Use of External Systems) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limits on authorized use requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-20(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AC-20(2) - Portable Storage Devices \227 Restricted Use

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AC-20(2)` |
| Control title | Portable Storage Devices \227 Restricted Use |
| Parent control | `AC-20` |
| Related controls | See parent control ([AC-20](#ac-20-use-of-external-systems)) |
| Related enhancements | N/A |
| What it is | Enhancement to AC-20 (Use of External Systems) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific portable storage devices \227 restricted use requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AC-20(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-21 - Information Sharing

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AC-21` |
| Control title | Information Sharing |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [RA-3](#ra-3-risk-assessment), [SC-15](#sc-15-collaborative-computing-devices-and-applications) |
| Related enhancements | None |
| What it is | This control addresses information sharing for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-22 - Publicly Accessible Content

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AC-22` |
| Control title | Publicly Accessible Content |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AT-2](#at-2-literacy-training-and-awareness), [AT-3](#at-3-role-based-training) |
| Related enhancements | None |
| What it is | This control addresses publicly accessible content for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AC-23 - Ac-23

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `AC-23` |
| Control title | Ac-23 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses ac-23 for CJIS systems, users, or data. |
| Recommended approach | Use centralized identity and access management, unique user accounts, and periodic reviews. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Awareness and Training (AT)

### AT-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AT-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Require completion before access and renew at least annually. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AT-2 - Literacy Training and Awareness

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AT-2` |
| Control title | Literacy Training and Awareness |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-17](#ac-17-remote-access), [AC-22](#ac-22-publicly-accessible-content), [AT-3](#at-3-role-based-training), [AT-4](#at-4-training-records), [CP-3](#cp-3-contingency-training), [IA-4](#ia-4-identifier-management), [IR-2](#ir-2-incident-response-training), [IR-7](#ir-7-incident-response-assistance), [PL-4](#pl-4-rules-of-behavior), [PS-7](#ps-7-external-personnel-security), [SA-8](#sa-8-security-and-privacy-engineering-principles) |
| Related enhancements | None |
| What it is | This control addresses at-2 for CJIS systems, users, or data. |
| Recommended approach | Require completion before access and renew at least annually. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AT-3 - Role-based Training

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AT-3` |
| Control title | Role-based Training |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-17](#ac-17-remote-access), [AC-22](#ac-22-publicly-accessible-content), [AT-2](#at-2-literacy-training-and-awareness), [AT-4](#at-4-training-records), [CP-3](#cp-3-contingency-training), [IR-2](#ir-2-incident-response-training), [IR-4](#ir-4-incident-handling), [IR-7](#ir-7-incident-response-assistance), [PL-4](#pl-4-rules-of-behavior), [PS-7](#ps-7-external-personnel-security), [PS-9](#ps-9-position-descriptions), [SA-3](#sa-3-system-development-life-cycle), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-11](#sa-11-developer-testing-and-evaluation), [SR-5](#sr-5-acquisition-strategies-tools-and-methods), [SR-6](#sr-6-supplier-assessments-and-reviews), [SR-11](#sr-11-sr-11) |
| Related enhancements | None |
| What it is | This control addresses at-3 for CJIS systems, users, or data. |
| Recommended approach | Require completion before access and renew at least annually. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AT-4 - Training Records

Tags: #priority/p4 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AT-4` |
| Control title | Training Records |
| Parent control | `N/A` |
| Related controls | [AT-2](#at-2-literacy-training-and-awareness), [AT-3](#at-3-role-based-training), [CP-3](#cp-3-contingency-training), [IR-2](#ir-2-incident-response-training), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses training records for CJIS systems, users, or data. |
| Recommended approach | Require completion before access and renew at least annually. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Audit and Accountability (AU)

### AU-1 - Policy and Procedures

Tags: #priority/p2 #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `AU-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-2 - Event Logging

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AU-2` |
| Control title | Event Logging |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-6](#ac-6-least-privilege), [AC-7](#ac-7-unsuccessful-logon-attempts), [AC-8](#ac-8-system-use-notification), [AC-17](#ac-17-remote-access), [AU-3](#au-3-content-of-audit-records), [AU-4](#au-4-audit-log-storage-capacity), [AU-5](#au-5-response-to-audit-logging-process-failures), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-7](#au-7-audit-record-reduction-and-report-generation), [AU-11](#au-11-audit-record-retention), [AU-12](#au-12-audit-record-generation), [CM-3](#cm-3-configuration-change-control), [CM-5](#cm-5-access-restrictions-for-change), [CM-6](#cm-6-configuration-settings), [IA-3](#ia-3-device-identification-and-authentication), [MA-4](#ma-4-nonlocal-maintenance), [MP-4](#mp-4-media-storage), [PE-3](#pe-3-physical-access-control), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-7](#sc-7-boundary-protection), [SC-18](#sc-18-mobile-code), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity), [SI-10](#si-10-information-input-validation), [SI-11](#si-11-error-handling) |
| Related enhancements | None |
| What it is | This control addresses event logging for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-3 - Content of Audit Records

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AU-3` |
| Control title | Content of Audit Records |
| Parent control | `N/A` |
| Related controls | [AU-2](#au-2-event-logging), [AU-8](#au-8-time-stamps), [AU-12](#au-12-audit-record-generation), [MA-4](#ma-4-nonlocal-maintenance), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SI-7](#si-7-software-firmware-and-information-integrity), [SI-11](#si-11-error-handling) |
| Related enhancements | [AU-3(1)](#au-31-additional-audit-information), [AU-3(3)](#au-33-limit-personally-identifiable-information-elements) |
| What it is | Enhancement to AU-3 (Content of Audit Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AU-3(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AU-3(1) - Additional Audit Information

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AU-3(1)` |
| Control title | Additional Audit Information |
| Parent control | `AU-3` |
| Related controls | See parent control ([AU-3](#au-3-content-of-audit-records)) |
| Related enhancements | N/A |
| What it is | Enhancement to AU-3 (Content of Audit Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific additional audit information requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AU-3(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AU-3(3) - Limit Personally Identifiable Information Elements

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AU-3(3)` |
| Control title | Limit Personally Identifiable Information Elements |
| Parent control | `AU-3` |
| Related controls | See parent control ([AU-3](#au-3-content-of-audit-records)) |
| Related enhancements | N/A |
| What it is | Enhancement to AU-3 (Content of Audit Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AU-3(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-4 - Audit Log Storage Capacity

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AU-4` |
| Control title | Audit Log Storage Capacity |
| Parent control | `N/A` |
| Related controls | [AU-2](#au-2-event-logging), [AU-5](#au-5-response-to-audit-logging-process-failures), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-7](#au-7-audit-record-reduction-and-report-generation), [AU-9](#au-9-protection-of-audit-information), [AU-11](#au-11-audit-record-retention), [AU-12](#au-12-audit-record-generation), [SI-4](#si-4-system-monitoring) |
| Related enhancements | None |
| What it is | This control addresses audit log storage capacity for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-5 - Response to Audit Logging Process Failures

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AU-5` |
| Control title | Response to Audit Logging Process Failures |
| Parent control | `N/A` |
| Related controls | [AU-2](#au-2-event-logging), [AU-4](#au-4-audit-log-storage-capacity), [AU-7](#au-7-audit-record-reduction-and-report-generation), [AU-9](#au-9-protection-of-audit-information), [AU-11](#au-11-audit-record-retention), [AU-12](#au-12-audit-record-generation), [SI-4](#si-4-system-monitoring), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses response to audit logging process failures for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-6 - Audit Record Review, Analysis, and Reporting

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AU-6` |
| Control title | Audit Record Review, Analysis, and Reporting |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-5](#ac-5-separation-of-duties), [AC-6](#ac-6-least-privilege), [AC-7](#ac-7-unsuccessful-logon-attempts), [AC-17](#ac-17-remote-access), [AU-7](#au-7-audit-record-reduction-and-report-generation), [CA-2](#ca-2-control-assessments), [CA-7](#ca-7-continuous-monitoring), [CM-2](#cm-2-baseline-configuration), [CM-5](#cm-5-access-restrictions-for-change), [CM-6](#cm-6-configuration-settings), [CM-10](#cm-10-software-usage-restrictions), [CM-11](#cm-11-user-installed-software), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-3](#ia-3-device-identification-and-authentication), [IA-5](#ia-5-authenticator-management), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [IR-5](#ir-5-incident-monitoring), [MA-4](#ma-4-nonlocal-maintenance), [MP-4](#mp-4-media-storage), [PE-3](#pe-3-physical-access-control), [PE-6](#pe-6-monitoring-physical-access), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-7](#sc-7-boundary-protection), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity) |
| Related enhancements | [AU-6(1)](#au-61-automated-process-integration), [AU-6(3)](#au-63-correlate-audit-record-repositories) |
| What it is | Enhancement to AU-6 (Audit Record Review, Analysis, and Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific correlate audit record repositories requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AU-6(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AU-6(1) - Automated Process Integration

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AU-6(1)` |
| Control title | Automated Process Integration |
| Parent control | `AU-6` |
| Related controls | See parent control ([AU-6](#au-6-audit-record-review-analysis-and-reporting)) |
| Related enhancements | N/A |
| What it is | Enhancement to AU-6 (Audit Record Review, Analysis, and Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated process integration requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AU-6(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AU-6(3) - Correlate Audit Record Repositories

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AU-6(3)` |
| Control title | Correlate Audit Record Repositories |
| Parent control | `AU-6` |
| Related controls | See parent control ([AU-6](#au-6-audit-record-review-analysis-and-reporting)) |
| Related enhancements | N/A |
| What it is | Enhancement to AU-6 (Audit Record Review, Analysis, and Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific correlate audit record repositories requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AU-6(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-7 - Audit Record Reduction and Report Generation

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AU-7` |
| Control title | Audit Record Reduction and Report Generation |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AU-2](#au-2-event-logging), [AU-3](#au-3-content-of-audit-records), [AU-4](#au-4-audit-log-storage-capacity), [AU-5](#au-5-response-to-audit-logging-process-failures), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-12](#au-12-audit-record-generation), [CM-5](#cm-5-access-restrictions-for-change), [IA-5](#ia-5-authenticator-management), [IR-4](#ir-4-incident-handling), [SI-4](#si-4-system-monitoring) |
| Related enhancements | [AU-7(1)](#au-71-automatic-processing) |
| What it is | Enhancement to AU-7 (Audit Record Reduction and Report Generation) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automatic processing requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AU-7(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### AU-7(1) - Automatic Processing

Tags: #priority/p3 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `AU-7(1)` |
| Control title | Automatic Processing |
| Parent control | `AU-7` |
| Related controls | See parent control ([AU-7](#au-7-audit-record-reduction-and-report-generation)) |
| Related enhancements | N/A |
| What it is | Enhancement to AU-7 (Audit Record Reduction and Report Generation) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automatic processing requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `AU-7(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-8 - Time Stamps

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AU-8` |
| Control title | Time Stamps |
| Parent control | `N/A` |
| Related controls | [AU-3](#au-3-content-of-audit-records), [AU-12](#au-12-audit-record-generation) |
| Related enhancements | None |
| What it is | This control addresses time stamps for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-9 - Protection of Audit Information

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AU-9` |
| Control title | Protection of Audit Information |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-6](#ac-6-least-privilege), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-11](#au-11-audit-record-retention), [MP-2](#mp-2-media-access), [MP-4](#mp-4-media-storage), [PE-2](#pe-2-physical-access-authorizations), [PE-3](#pe-3-physical-access-control), [PE-6](#pe-6-monitoring-physical-access), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-8](#sc-8-transmission-confidentiality-and-integrity), [SI-4](#si-4-system-monitoring) |
| Related enhancements | None |
| What it is | This control addresses au-9 for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-11 - Audit Record Retention

Tags: #priority/p4 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `AU-11` |
| Control title | Audit Record Retention |
| Parent control | `N/A` |
| Related controls | [AU-2](#au-2-event-logging), [AU-4](#au-4-audit-log-storage-capacity), [AU-5](#au-5-response-to-audit-logging-process-failures), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-9](#au-9-protection-of-audit-information), [MP-6](#mp-6-media-sanitization), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses audit record retention for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-12 - Audit Record Generation

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `AU-12` |
| Control title | Audit Record Generation |
| Parent control | `N/A` |
| Related controls | [AC-6](#ac-6-least-privilege), [AC-17](#ac-17-remote-access), [AU-2](#au-2-event-logging), [AU-3](#au-3-content-of-audit-records), [AU-4](#au-4-audit-log-storage-capacity), [AU-5](#au-5-response-to-audit-logging-process-failures), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-7](#au-7-audit-record-reduction-and-report-generation), [CM-5](#cm-5-access-restrictions-for-change), [MA-4](#ma-4-nonlocal-maintenance), [MP-4](#mp-4-media-storage), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-18](#sc-18-mobile-code), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity), [SI-10](#si-10-information-input-validation) |
| Related enhancements | None |
| What it is | This control addresses audit record generation for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-13 - Au-13

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `AU-13` |
| Control title | Au-13 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses au-13 for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### AU-16 - Au-16

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `AU-16` |
| Control title | Au-16 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses au-16 for CJIS systems, users, or data. |
| Recommended approach | Send logs to a central platform and review them on a schedule. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Assessment, Authorization, and Monitoring (CA)

### CA-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CA-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CA-2 - Control Assessments

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CA-2` |
| Control title | Control Assessments |
| Parent control | `N/A` |
| Related controls | [AC-20](#ac-20-use-of-external-systems), [CA-5](#ca-5-plan-of-action-and-milestones), [CA-6](#ca-6-authorization), [CA-7](#ca-7-continuous-monitoring), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SA-11](#sa-11-developer-testing-and-evaluation), [SI-3](#si-3-malicious-code-protection), [SI-12](#si-12-information-management-and-retention), [SR-2](#sr-2-supply-chain-risk-management-plan), [SR-3](#sr-3-supply-chain-controls-and-processes) |
| Related enhancements | [CA-2(1)](#ca-21-independent-assessors) |
| What it is | Enhancement to CA-2 (Control Assessments) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific independent assessors requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CA-2(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CA-2(1) - Independent Assessors

Tags: #priority/p3 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CA-2(1)` |
| Control title | Independent Assessors |
| Parent control | `CA-2` |
| Related controls | See parent control ([CA-2](#ca-2-control-assessments)) |
| Related enhancements | N/A |
| What it is | Enhancement to CA-2 (Control Assessments) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific independent assessors requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CA-2(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CA-3 - Information Exchange

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `CA-3` |
| Control title | Information Exchange |
| Parent control | `N/A` |
| Related controls | [AC-4](#ac-4-information-flow-enforcement), [AC-20](#ac-20-use-of-external-systems), [CA-6](#ca-6-authorization), [IA-3](#ia-3-device-identification-and-authentication), [IR-4](#ir-4-incident-handling), [PL-2](#pl-2-system-security-and-privacy-plans), [RA-3](#ra-3-risk-assessment), [SA-9](#sa-9-external-system-services), [SC-7](#sc-7-boundary-protection), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses information exchange for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CA-5 - Plan of Action and Milestones

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CA-5` |
| Control title | Plan of Action and Milestones |
| Parent control | `N/A` |
| Related controls | [CA-2](#ca-2-control-assessments), [CA-7](#ca-7-continuous-monitoring), [RA-7](#ra-7-risk-response), [SI-2](#si-2-flaw-remediation), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses plan of action and milestones for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CA-6 - Authorization

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CA-6` |
| Control title | Authorization |
| Parent control | `N/A` |
| Related controls | [CA-2](#ca-2-control-assessments), [CA-3](#ca-3-information-exchange), [CA-7](#ca-7-continuous-monitoring), [RA-3](#ra-3-risk-assessment), [SA-10](#sa-10-developer-configuration-management), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses authorization for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CA-7 - Continuous Monitoring

Tags: #priority/p1 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CA-7` |
| Control title | Continuous Monitoring |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-6](#ac-6-least-privilege), [AC-17](#ac-17-remote-access), [AT-4](#at-4-training-records), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [CA-2](#ca-2-control-assessments), [CA-5](#ca-5-plan-of-action-and-milestones), [CA-6](#ca-6-authorization), [CM-3](#cm-3-configuration-change-control), [CM-4](#cm-4-impact-analyses), [CM-6](#cm-6-configuration-settings), [CM-11](#cm-11-user-installed-software), [IA-5](#ia-5-authenticator-management), [IR-5](#ir-5-incident-monitoring), [MA-2](#ma-2-controlled-maintenance), [MA-3](#ma-3-maintenance-tools), [MA-4](#ma-4-nonlocal-maintenance), [PE-3](#pe-3-physical-access-control), [PE-6](#pe-6-monitoring-physical-access), [PE-14](#pe-14-environmental-controls), [PE-16](#pe-16-delivery-and-removal), [PL-2](#pl-2-system-security-and-privacy-plans), [PS-7](#ps-7-external-personnel-security), [RA-3](#ra-3-risk-assessment), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [RA-7](#ra-7-risk-response), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SA-11](#sa-11-developer-testing-and-evaluation), [SC-5](#sc-5-denial-of-service-protection), [SC-7](#sc-7-boundary-protection), [SC-18](#sc-18-mobile-code), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring), [SI-12](#si-12-information-management-and-retention), [SR-6](#sr-6-supplier-assessments-and-reviews) |
| Related enhancements | [CA-7(1)](#ca-71-independent-assessment), [CA-7(4)](#ca-74-risk-monitoring) |
| What it is | Enhancement to CA-7 (Continuous Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific risk monitoring requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CA-7(4)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CA-7(1) - Independent Assessment

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CA-7(1)` |
| Control title | Independent Assessment |
| Parent control | `CA-7` |
| Related controls | See parent control ([CA-7](#ca-7-continuous-monitoring)) |
| Related enhancements | N/A |
| What it is | Enhancement to CA-7 (Continuous Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific independent assessment requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CA-7(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CA-7(4) - Risk Monitoring

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CA-7(4)` |
| Control title | Risk Monitoring |
| Parent control | `CA-7` |
| Related controls | See parent control ([CA-7](#ca-7-continuous-monitoring)) |
| Related enhancements | N/A |
| What it is | Enhancement to CA-7 (Continuous Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific risk monitoring requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CA-7(4)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CA-9 - Internal System Connections

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CA-9` |
| Control title | Internal System Connections |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [AC-18](#ac-18-wireless-access), [AC-19](#ac-19-access-control-for-mobile-devices), [CM-2](#cm-2-baseline-configuration), [IA-3](#ia-3-device-identification-and-authentication), [SC-7](#sc-7-boundary-protection), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses internal system connections for CJIS systems, users, or data. |
| Recommended approach | Tie approvals to documented assessments and recurring monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Configuration Management (CM)

### CM-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-2 - Baseline Configuration

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `CM-2` |
| Control title | Baseline Configuration |
| Parent control | `N/A` |
| Related controls | [AC-19](#ac-19-access-control-for-mobile-devices), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [CA-9](#ca-9-internal-system-connections), [CM-1](#cm-1-policy-and-procedures), [CM-3](#cm-3-configuration-change-control), [CM-5](#cm-5-access-restrictions-for-change), [CM-6](#cm-6-configuration-settings), [CM-8](#cm-8-system-component-inventory), [CM-9](#cm-9-configuration-management-plan), [CP-9](#cp-9-system-backup), [CP-10](#cp-10-system-recovery-and-reconstitution), [MA-2](#ma-2-controlled-maintenance), [PL-8](#pl-8-security-and-privacy-architectures), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-10](#sa-10-developer-configuration-management), [SA-15](#sa-15-development-process-standards-and-tools), [SC-18](#sc-18-mobile-code) |
| Related enhancements | [CM-2(2)](#cm-22-automation-support-for-accuracy-and-currency), [CM-2(3)](#cm-23-retention-of-previous-configurations), [CM-2(7)](#cm-27-configure-systems-and-components-for-high-risk-areas) |
| What it is | Enhancement to CM-2 (Baseline Configuration) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific retention of previous configurations requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-2(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-2(2) - Automation Support for Accuracy and Currency

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-2(2)` |
| Control title | Automation Support for Accuracy and Currency |
| Parent control | `CM-2` |
| Related controls | See parent control ([CM-2](#cm-2-baseline-configuration)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-2 (Baseline Configuration) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automation support for accuracy and currency requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-2(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-2(3) - Retention of Previous Configurations

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-2(3)` |
| Control title | Retention of Previous Configurations |
| Parent control | `CM-2` |
| Related controls | See parent control ([CM-2](#cm-2-baseline-configuration)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-2 (Baseline Configuration) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific retention of previous configurations requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-2(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-2(7) - Configure Systems and Components for High-risk Areas

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-2(7)` |
| Control title | Configure Systems and Components for High-risk Areas |
| Parent control | `CM-2` |
| Related controls | See parent control ([CM-2](#cm-2-baseline-configuration)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-2 (Baseline Configuration) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific configure systems and components for high-risk areas requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-2(7)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-3 - Configuration Change Control

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-3` |
| Control title | Configuration Change Control |
| Parent control | `N/A` |
| Related controls | [CA-7](#ca-7-continuous-monitoring), [CM-2](#cm-2-baseline-configuration), [CM-4](#cm-4-impact-analyses), [CM-5](#cm-5-access-restrictions-for-change), [CM-6](#cm-6-configuration-settings), [CM-9](#cm-9-configuration-management-plan), [CM-11](#cm-11-user-installed-software), [IA-3](#ia-3-device-identification-and-authentication), [MA-2](#ma-2-controlled-maintenance), [PE-16](#pe-16-delivery-and-removal), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-10](#sa-10-developer-configuration-management), [SC-28](#sc-28-protection-of-information-at-rest), [SI-2](#si-2-flaw-remediation), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity), [SI-10](#si-10-information-input-validation), [SR-11](#sr-11-sr-11) |
| Related enhancements | [CM-3(2)](#cm-32-testing-validation-and-documentation-of-changes), [CM-3(4)](#cm-34-security-and-privacy-representatives) |
| What it is | Enhancement to CM-3 (Configuration Change Control) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific security and privacy representatives requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-3(4)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-3(2) - Testing, Validation, and Documentation of Changes

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-3(2)` |
| Control title | Testing, Validation, and Documentation of Changes |
| Parent control | `CM-3` |
| Related controls | See parent control ([CM-3](#cm-3-configuration-change-control)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-3 (Configuration Change Control) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific testing, validation, and documentation of changes requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-3(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-3(4) - Security and Privacy Representatives

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-3(4)` |
| Control title | Security and Privacy Representatives |
| Parent control | `CM-3` |
| Related controls | See parent control ([CM-3](#cm-3-configuration-change-control)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-3 (Configuration Change Control) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific security and privacy representatives requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-3(4)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-4 - Impact Analyses

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-4` |
| Control title | Impact Analyses |
| Parent control | `N/A` |
| Related controls | [CA-7](#ca-7-continuous-monitoring), [CM-3](#cm-3-configuration-change-control), [CM-8](#cm-8-system-component-inventory), [CM-9](#cm-9-configuration-management-plan), [MA-2](#ma-2-controlled-maintenance), [RA-3](#ra-3-risk-assessment), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-10](#sa-10-developer-configuration-management), [SI-2](#si-2-flaw-remediation) |
| Related enhancements | [CM-4(2)](#cm-42-verification-of-controls) |
| What it is | Enhancement to CM-4 (Impact Analyses) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific verification of controls requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-4(2)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-4(2) - Verification of Controls

Tags: #priority/p3 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-4(2)` |
| Control title | Verification of Controls |
| Parent control | `CM-4` |
| Related controls | See parent control ([CM-4](#cm-4-impact-analyses)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-4 (Impact Analyses) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific verification of controls requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-4(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-5 - Access Restrictions for Change

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `CM-5` |
| Control title | Access Restrictions for Change |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-5](#ac-5-separation-of-duties), [AC-6](#ac-6-least-privilege), [CM-9](#cm-9-configuration-management-plan), [PE-3](#pe-3-physical-access-control), [SC-28](#sc-28-protection-of-information-at-rest), [SI-2](#si-2-flaw-remediation), [SI-10](#si-10-information-input-validation) |
| Related enhancements | None |
| What it is | This control addresses access restrictions for change for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-6 - Configuration Settings

Tags: #priority/p1 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-6` |
| Control title | Configuration Settings |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-19](#ac-19-access-control-for-mobile-devices), [AU-2](#au-2-event-logging), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [CA-9](#ca-9-internal-system-connections), [CM-2](#cm-2-baseline-configuration), [CM-3](#cm-3-configuration-change-control), [CM-5](#cm-5-access-restrictions-for-change), [CM-7](#cm-7-least-functionality), [CM-11](#cm-11-user-installed-software), [CP-7](#cp-7-alternate-processing-site), [CP-9](#cp-9-system-backup), [CP-10](#cp-10-system-recovery-and-reconstitution), [IA-3](#ia-3-device-identification-and-authentication), [IA-5](#ia-5-authenticator-management), [PL-8](#pl-8-security-and-privacy-architectures), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SA-4](#sa-4-acquisition-process), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SC-18](#sc-18-mobile-code), [SC-28](#sc-28-protection-of-information-at-rest), [SI-2](#si-2-flaw-remediation), [SI-4](#si-4-system-monitoring) |
| Related enhancements | None |
| What it is | This control addresses configuration settings for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-7 - Least Functionality

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `CM-7` |
| Control title | Least Functionality |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [CM-2](#cm-2-baseline-configuration), [CM-5](#cm-5-access-restrictions-for-change), [CM-6](#cm-6-configuration-settings), [CM-11](#cm-11-user-installed-software), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SA-4](#sa-4-acquisition-process), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SA-15](#sa-15-development-process-standards-and-tools), [SC-2](#sc-2-separation-of-system-and-user-functionality), [SC-7](#sc-7-boundary-protection), [SI-4](#si-4-system-monitoring) |
| Related enhancements | [CM-7(1)](#cm-71-periodic-review), [CM-7(2)](#cm-72-prevent-program-execution), [CM-7(5)](#cm-75-authorized-software-227-allow-by-exception) |
| What it is | Enhancement to CM-7 (Least Functionality) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prevent program execution requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-7(2)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-7(1) - Periodic Review

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-7(1)` |
| Control title | Periodic Review |
| Parent control | `CM-7` |
| Related controls | See parent control ([CM-7](#cm-7-least-functionality)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-7 (Least Functionality) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific periodic review requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-7(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-7(2) - Prevent Program Execution

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-7(2)` |
| Control title | Prevent Program Execution |
| Parent control | `CM-7` |
| Related controls | See parent control ([CM-7](#cm-7-least-functionality)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-7 (Least Functionality) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prevent program execution requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-7(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-7(5) - Authorized Software \227 Allow-by-exception

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-7(5)` |
| Control title | Authorized Software \227 Allow-by-exception |
| Parent control | `CM-7` |
| Related controls | See parent control ([CM-7](#cm-7-least-functionality)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-7 (Least Functionality) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific authorized software \227 allow-by-exception requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-7(5)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-8 - System Component Inventory

Tags: #priority/p1 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-8` |
| Control title | System Component Inventory |
| Parent control | `N/A` |
| Related controls | [CM-2](#cm-2-baseline-configuration), [CM-7](#cm-7-least-functionality), [CM-9](#cm-9-configuration-management-plan), [CM-10](#cm-10-software-usage-restrictions), [CM-11](#cm-11-user-installed-software), [CP-2](#cp-2-contingency-plan), [CP-9](#cp-9-system-backup), [MA-2](#ma-2-controlled-maintenance), [MA-6](#ma-6-timely-maintenance), [SA-4](#sa-4-acquisition-process), [SA-5](#sa-5-system-documentation), [SI-2](#si-2-flaw-remediation) |
| Related enhancements | [CM-8(1)](#cm-81-updates-during-installation-and-removal), [CM-8(3)](#cm-83-automated-unauthorized-component-detection) |
| What it is | Enhancement to CM-8 (System Component Inventory) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated unauthorized component detection requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-8(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-8(1) - Updates During Installation and Removal

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-8(1)` |
| Control title | Updates During Installation and Removal |
| Parent control | `CM-8` |
| Related controls | See parent control ([CM-8](#cm-8-system-component-inventory)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-8 (System Component Inventory) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific updates during installation and removal requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-8(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-8(3) - Automated Unauthorized Component Detection

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-8(3)` |
| Control title | Automated Unauthorized Component Detection |
| Parent control | `CM-8` |
| Related controls | See parent control ([CM-8](#cm-8-system-component-inventory)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-8 (System Component Inventory) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated unauthorized component detection requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-8(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-9 - Configuration Management Plan

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-9` |
| Control title | Configuration Management Plan |
| Parent control | `N/A` |
| Related controls | [CM-2](#cm-2-baseline-configuration), [CM-3](#cm-3-configuration-change-control), [CM-4](#cm-4-impact-analyses), [CM-5](#cm-5-access-restrictions-for-change), [CM-8](#cm-8-system-component-inventory), [PL-2](#pl-2-system-security-and-privacy-plans), [SA-10](#sa-10-developer-configuration-management), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses configuration management plan for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-10 - Software Usage Restrictions

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-10` |
| Control title | Software Usage Restrictions |
| Parent control | `N/A` |
| Related controls | [AC-17](#ac-17-remote-access), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [CM-7](#cm-7-least-functionality), [CM-8](#cm-8-system-component-inventory), [SC-7](#sc-7-boundary-protection) |
| Related enhancements | None |
| What it is | This control addresses software usage restrictions for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-11 - User-installed Software

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-11` |
| Control title | User-installed Software |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [CM-2](#cm-2-baseline-configuration), [CM-3](#cm-3-configuration-change-control), [CM-5](#cm-5-access-restrictions-for-change), [CM-6](#cm-6-configuration-settings), [CM-7](#cm-7-least-functionality), [CM-8](#cm-8-system-component-inventory), [PL-4](#pl-4-rules-of-behavior), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity) |
| Related enhancements | None |
| What it is | This control addresses user-installed software for CJIS systems, users, or data. |
| Recommended approach | Control baselines, changes, and inventories through a documented workflow. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CM-12 - Information Location

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CM-12` |
| Control title | Information Location |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [AC-6](#ac-6-least-privilege), [CM-8](#cm-8-system-component-inventory), [RA-2](#ra-2-security-categorization), [SA-4](#sa-4-acquisition-process), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-4](#sc-4-information-in-shared-system-resources), [SC-28](#sc-28-protection-of-information-at-rest), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity) |
| Related enhancements | [CM-12(1)](#cm-121-automated-tools-to-support-information-location-79-contingency-planning-cp) |
| What it is | Enhancement to CM-12 (Information Location) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated tools to support information location ................79 contingency planning (cp) requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-12(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CM-12(1) - Automated Tools to Support Information Location ................79 CONTINGENCY PLANNING (Cp)

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CM-12(1)` |
| Control title | Automated Tools to Support Information Location ................79 CONTINGENCY PLANNING (Cp) |
| Parent control | `CM-12` |
| Related controls | See parent control ([CM-12](#cm-12-information-location)) |
| Related enhancements | N/A |
| What it is | Enhancement to CM-12 (Information Location) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated tools to support information location ................79 contingency planning (cp) requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CM-12(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Contingency Planning (CP)

### CP-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Keep backups, recovery procedures, and restoration testing current. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CP-2 - Contingency Plan

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-2` |
| Control title | Contingency Plan |
| Parent control | `N/A` |
| Related controls | [CP-3](#cp-3-contingency-training), [CP-4](#cp-4-contingency-plan-testing), [CP-6](#cp-6-alternate-storage-site), [CP-7](#cp-7-alternate-processing-site), [CP-8](#cp-8-telecommunications-services), [CP-9](#cp-9-system-backup), [CP-10](#cp-10-system-recovery-and-reconstitution), [IR-4](#ir-4-incident-handling), [IR-6](#ir-6-incident-reporting), [IR-8](#ir-8-incident-response-plan), [MA-6](#ma-6-timely-maintenance), [MP-2](#mp-2-media-access), [MP-4](#mp-4-media-storage), [MP-5](#mp-5-media-transport), [PL-2](#pl-2-system-security-and-privacy-plans), [SA-15](#sa-15-development-process-standards-and-tools), [SC-7](#sc-7-boundary-protection), [SC-23](#sc-23-session-authenticity), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | [CP-2(1)](#cp-21-coordinate-with-related-plans), [CP-2(3)](#cp-23-resume-mission-and-business-functions), [CP-2(8)](#cp-28-identify-critical-assets) |
| What it is | Enhancement to CP-2 (Contingency Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identify critical assets requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-2(8)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-2(1) - Coordinate with Related Plans

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-2(1)` |
| Control title | Coordinate with Related Plans |
| Parent control | `CP-2` |
| Related controls | See parent control ([CP-2](#cp-2-contingency-plan)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-2 (Contingency Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordinate with related plans requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-2(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-2(3) - Resume Mission and Business Functions

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-2(3)` |
| Control title | Resume Mission and Business Functions |
| Parent control | `CP-2` |
| Related controls | See parent control ([CP-2](#cp-2-contingency-plan)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-2 (Contingency Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific resume mission and business functions requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-2(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-2(8) - Identify Critical Assets

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-2(8)` |
| Control title | Identify Critical Assets |
| Parent control | `CP-2` |
| Related controls | See parent control ([CP-2](#cp-2-contingency-plan)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-2 (Contingency Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identify critical assets requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-2(8)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CP-3 - Contingency Training

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-3` |
| Control title | Contingency Training |
| Parent control | `N/A` |
| Related controls | [AT-2](#at-2-literacy-training-and-awareness), [AT-3](#at-3-role-based-training), [AT-4](#at-4-training-records), [CP-2](#cp-2-contingency-plan), [CP-4](#cp-4-contingency-plan-testing), [CP-8](#cp-8-telecommunications-services), [IR-2](#ir-2-incident-response-training), [IR-4](#ir-4-incident-handling) |
| Related enhancements | None |
| What it is | This control addresses contingency training for CJIS systems, users, or data. |
| Recommended approach | Keep backups, recovery procedures, and restoration testing current. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CP-4 - Contingency Plan Testing

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-4` |
| Control title | Contingency Plan Testing |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [CP-2](#cp-2-contingency-plan), [CP-3](#cp-3-contingency-training), [CP-8](#cp-8-telecommunications-services), [CP-9](#cp-9-system-backup), [IR-3](#ir-3-incident-response-testing), [IR-4](#ir-4-incident-handling), [PL-2](#pl-2-system-security-and-privacy-plans), [SR-2](#sr-2-supply-chain-risk-management-plan) |
| Related enhancements | [CP-4(1)](#cp-41-coordinate-with-related-plans) |
| What it is | Enhancement to CP-4 (Contingency Plan Testing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordinate with related plans requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-4(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-4(1) - Coordinate with Related Plans

Tags: #priority/p3 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-4(1)` |
| Control title | Coordinate with Related Plans |
| Parent control | `CP-4` |
| Related controls | See parent control ([CP-4](#cp-4-contingency-plan-testing)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-4 (Contingency Plan Testing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordinate with related plans requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-4(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CP-6 - Alternate Storage Site

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-6` |
| Control title | Alternate Storage Site |
| Parent control | `N/A` |
| Related controls | [CP-2](#cp-2-contingency-plan), [CP-7](#cp-7-alternate-processing-site), [CP-8](#cp-8-telecommunications-services), [CP-9](#cp-9-system-backup), [CP-10](#cp-10-system-recovery-and-reconstitution), [MP-4](#mp-4-media-storage), [MP-5](#mp-5-media-transport), [PE-3](#pe-3-physical-access-control) |
| Related enhancements | [CP-6(1)](#cp-61-separation-from-primary-site), [CP-6(3)](#cp-63-accessibility) |
| What it is | Enhancement to CP-6 (Alternate Storage Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific accessibility requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-6(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-6(1) - Separation from Primary Site

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-6(1)` |
| Control title | Separation from Primary Site |
| Parent control | `CP-6` |
| Related controls | See parent control ([CP-6](#cp-6-alternate-storage-site)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-6 (Alternate Storage Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific separation from primary site requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-6(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-6(3) - Accessibility

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-6(3)` |
| Control title | Accessibility |
| Parent control | `CP-6` |
| Related controls | See parent control ([CP-6](#cp-6-alternate-storage-site)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-6 (Alternate Storage Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific accessibility requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-6(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CP-7 - Alternate Processing Site

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-7` |
| Control title | Alternate Processing Site |
| Parent control | `N/A` |
| Related controls | [CP-2](#cp-2-contingency-plan), [CP-6](#cp-6-alternate-storage-site), [CP-8](#cp-8-telecommunications-services), [CP-9](#cp-9-system-backup), [CP-10](#cp-10-system-recovery-and-reconstitution), [MA-6](#ma-6-timely-maintenance), [PE-3](#pe-3-physical-access-control), [PE-11](#pe-11-emergency-power), [PE-12](#pe-12-emergency-lighting), [PE-17](#pe-17-alternate-work-site) |
| Related enhancements | [CP-7(1)](#cp-71-separation-from-primary-site), [CP-7(2)](#cp-72-accessibility), [CP-7(3)](#cp-73-priority-of-service) |
| What it is | Enhancement to CP-7 (Alternate Processing Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific priority of service requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-7(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-7(1) - Separation from Primary Site

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-7(1)` |
| Control title | Separation from Primary Site |
| Parent control | `CP-7` |
| Related controls | See parent control ([CP-7](#cp-7-alternate-processing-site)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-7 (Alternate Processing Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific separation from primary site requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-7(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-7(2) - Accessibility

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-7(2)` |
| Control title | Accessibility |
| Parent control | `CP-7` |
| Related controls | See parent control ([CP-7](#cp-7-alternate-processing-site)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-7 (Alternate Processing Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific accessibility requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-7(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-7(3) - Priority of Service

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-7(3)` |
| Control title | Priority of Service |
| Parent control | `CP-7` |
| Related controls | See parent control ([CP-7](#cp-7-alternate-processing-site)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-7 (Alternate Processing Site) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific priority of service requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-7(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CP-8 - Telecommunications Services

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-8` |
| Control title | Telecommunications Services |
| Parent control | `N/A` |
| Related controls | [CP-2](#cp-2-contingency-plan), [CP-6](#cp-6-alternate-storage-site), [CP-7](#cp-7-alternate-processing-site), [SC-7](#sc-7-boundary-protection) |
| Related enhancements | [CP-8(1)](#cp-81-priority-of-service-provisions), [CP-8(2)](#cp-82-single-points-of-failure) |
| What it is | Enhancement to CP-8 (Telecommunications Services) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific single points of failure requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-8(2)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-8(1) - Priority of Service Provisions

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-8(1)` |
| Control title | Priority of Service Provisions |
| Parent control | `CP-8` |
| Related controls | See parent control ([CP-8](#cp-8-telecommunications-services)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-8 (Telecommunications Services) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific priority of service provisions requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-8(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-8(2) - Single Points of Failure

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-8(2)` |
| Control title | Single Points of Failure |
| Parent control | `CP-8` |
| Related controls | See parent control ([CP-8](#cp-8-telecommunications-services)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-8 (Telecommunications Services) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific single points of failure requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-8(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CP-9 - System Backup

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-9` |
| Control title | System Backup |
| Parent control | `N/A` |
| Related controls | [CP-2](#cp-2-contingency-plan), [CP-6](#cp-6-alternate-storage-site), [CP-10](#cp-10-system-recovery-and-reconstitution), [MP-4](#mp-4-media-storage), [MP-5](#mp-5-media-transport), [SC-8](#sc-8-transmission-confidentiality-and-integrity), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SI-4](#si-4-system-monitoring) |
| Related enhancements | [CP-9(1)](#cp-91-testing-for-reliability-and-integrity-89-ix-12272024-cjissecpol-v60), [CP-9(8)](#cp-98-cryptographic-protection) |
| What it is | Enhancement to CP-9 (System Backup) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-9(8)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-9(1) - Testing for Reliability and Integrity .................................................89 Ix 12/27/2024 CJISSECPOL V6.0

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-9(1)` |
| Control title | Testing for Reliability and Integrity .................................................89 Ix 12/27/2024 CJISSECPOL V6.0 |
| Parent control | `CP-9` |
| Related controls | See parent control ([CP-9](#cp-9-system-backup)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-9 (System Backup) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific testing for reliability and integrity .................................................89 ix 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-9(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-9(8) - Cryptographic Protection

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-9(8)` |
| Control title | Cryptographic Protection |
| Parent control | `CP-9` |
| Related controls | See parent control ([CP-9](#cp-9-system-backup)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-9 (System Backup) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-9(8)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### CP-10 - System Recovery and Reconstitution

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `CP-10` |
| Control title | System Recovery and Reconstitution |
| Parent control | `N/A` |
| Related controls | [CP-2](#cp-2-contingency-plan), [CP-4](#cp-4-contingency-plan-testing), [CP-6](#cp-6-alternate-storage-site), [CP-7](#cp-7-alternate-processing-site), [CP-9](#cp-9-system-backup), [IR-4](#ir-4-incident-handling), [SA-8](#sa-8-security-and-privacy-engineering-principles) |
| Related enhancements | [CP-10(2)](#cp-102-transaction-recovery-90-identification-and-authentication-ia) |
| What it is | Enhancement to CP-10 (System Recovery and Reconstitution) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific transaction recovery .....................................90 identification and authentication (ia) requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-10(2)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### CP-10(2) - Transaction Recovery .....................................90 IDENTIFICATION AND AUTHENTICATION (Ia)

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `CP-10(2)` |
| Control title | Transaction Recovery .....................................90 IDENTIFICATION AND AUTHENTICATION (Ia) |
| Parent control | `CP-10` |
| Related controls | See parent control ([CP-10](#cp-10-system-recovery-and-reconstitution)) |
| Related enhancements | N/A |
| What it is | Enhancement to CP-10 (System Recovery and Reconstitution) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific transaction recovery .....................................90 identification and authentication (ia) requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `CP-10(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Identification and Authentication (IA)

### IA-0 - Use of Originating Agency Identifiers in Transactions and Information Exchanges

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `IA-0` |
| Control title | Use of Originating Agency Identifiers in Transactions and Information Exchanges |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses use of originating agency identifiers in transactions and information exchanges for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IA-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [AC-1](#ac-1-policy-and-procedures), [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-2 - Identification and Authentication (Organizational Users)

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IA-2` |
| Control title | Identification and Authentication (Organizational Users) |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [AC-14](#ac-14-permitted-actions-without-identification-or-authentication), [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AU-1](#au-1-policy-and-procedures), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [IA-4](#ia-4-identifier-management), [IA-5](#ia-5-authenticator-management), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-4](#ma-4-nonlocal-maintenance), [MA-5](#ma-5-maintenance-personnel), [PE-2](#pe-2-physical-access-authorizations), [PL-4](#pl-4-rules-of-behavior), [SA-4](#sa-4-acquisition-process), [SA-8](#sa-8-security-and-privacy-engineering-principles) |
| Related enhancements | None |
| What it is | This control addresses identification and authentication \(organizational users\) for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-3 - Device Identification and Authentication

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IA-3` |
| Control title | Device Identification and Authentication |
| Parent control | `N/A` |
| Related controls | [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AC-19](#ac-19-access-control-for-mobile-devices), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [CA-3](#ca-3-information-exchange), [CA-9](#ca-9-internal-system-connections), [IA-4](#ia-4-identifier-management), [IA-5](#ia-5-authenticator-management), [IA-11](#ia-11-re-authentication), [SI-4](#si-4-system-monitoring) |
| Related enhancements | None |
| What it is | This control addresses device identification and authentication for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-4 - Identifier Management

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IA-4` |
| Control title | Identifier Management |
| Parent control | `N/A` |
| Related controls | [AC-5](#ac-5-separation-of-duties), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-3](#ia-3-device-identification-and-authentication), [IA-5](#ia-5-authenticator-management), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [IA-12](#ia-12-identity-proofing), [MA-4](#ma-4-nonlocal-maintenance), [PE-2](#pe-2-physical-access-authorizations), [PE-3](#pe-3-physical-access-control), [PE-4](#pe-4-access-control-for-transmission), [PL-4](#pl-4-rules-of-behavior), [PS-3](#ps-3-personnel-screening), [PS-4](#ps-4-personnel-termination), [PS-5](#ps-5-personnel-transfer) |
| Related enhancements | [IA-4(4)](#ia-44-identify-user-status) |
| What it is | Enhancement to IA-4 (Identifier Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identify user status requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-4(4)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IA-4(4) - Identify User Status

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IA-4(4)` |
| Control title | Identify User Status |
| Parent control | `IA-4` |
| Related controls | See parent control ([IA-4](#ia-4-identifier-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to IA-4 (Identifier Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identify user status requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-4(4)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-5 - Authenticator Management

Tags: #priority/p1 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IA-5` |
| Control title | Authenticator Management |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-6](#ac-6-least-privilege), [CM-6](#cm-6-configuration-settings), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-4](#ia-4-identifier-management), [IA-7](#ia-7-cryptographic-module-authenticationf), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-4](#ma-4-nonlocal-maintenance), [PE-2](#pe-2-physical-access-authorizations), [PL-4](#pl-4-rules-of-behavior), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection) |
| Related enhancements | [IA-5(1)](#ia-51-authenticator-types-118-a-memorized-secret-authenticators-and-verifiers-118-b-look-up-secret-authenticators-and-verifiers-123-c-out-of-band-authenticators-and-verifiers-125-d-otp-authenticators-and-verifiers-130-e-cryptographic-authenticators-and-verifiers-including-single-and-multi-factor-cryptographic-authenticators-both-hardware-and-software-based), [IA-5(2)](#ia-52-public-key-based-authentication), [IA-5(6)](#ia-56-protection-of-authenticators) |
| What it is | Enhancement to IA-5 (Authenticator Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific protection of authenticators requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-5(6)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IA-5(1) - Authenticator Types ....................................................118 (A) Memorized Secret Authenticators and Verifiers: .................................................. 118 (B) Look-up Secret Authenticators and Verifiers ...................................................... 123 (C) Out-of-band Authenticators and Verifiers ............................................................ 125 (D) OTP Authenticators and Verifiers ......................................................................... 130 (E) Cryptographic Authenticators and Verifiers (Including Single- and Multi-factor Cryptographic Authenticators, Both Hardware- and Software-based) ......................

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IA-5(1)` |
| Control title | Authenticator Types ....................................................118 (A) Memorized Secret Authenticators and Verifiers: .................................................. 118 (B) Look-up Secret Authenticators and Verifiers ...................................................... 123 (C) Out-of-band Authenticators and Verifiers ............................................................ 125 (D) OTP Authenticators and Verifiers ......................................................................... 130 (E) Cryptographic Authenticators and Verifiers (Including Single- and Multi-factor Cryptographic Authenticators, Both Hardware- and Software-based) ...................... |
| Parent control | `IA-5` |
| Related controls | See parent control ([IA-5](#ia-5-authenticator-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to IA-5 (Authenticator Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific authenticator types ....................................................118 (a) memorized secret authenticators and verifiers: .................................................. 118 (b) look-up secret authenticators and verifiers ...................................................... 123 (c) out-of-band authenticators and verifiers ............................................................ 125 (d) otp authenticators and verifiers ......................................................................... 130 (e) cryptographic authenticators and verifiers (including single- and multi-factor cryptographic authenticators, both hardware- and software-based) ...................... requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-5(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IA-5(2) - Public Key Based Authentication

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IA-5(2)` |
| Control title | Public Key Based Authentication |
| Parent control | `IA-5` |
| Related controls | See parent control ([IA-5](#ia-5-authenticator-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to IA-5 (Authenticator Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific public key based authentication requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-5(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IA-5(6) - Protection of Authenticators

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IA-5(6)` |
| Control title | Protection of Authenticators |
| Parent control | `IA-5` |
| Related controls | See parent control ([IA-5](#ia-5-authenticator-management)) |
| Related enhancements | N/A |
| What it is | Enhancement to IA-5 (Authenticator Management) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific protection of authenticators requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-5(6)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-6 - Authentication Feedback

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IA-6` |
| Control title | Authentication Feedback |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement) |
| Related enhancements | None |
| What it is | This control addresses authentication feedback for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-7 - Cryptographic Module Authenticationf

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IA-7` |
| Control title | Cryptographic Module Authenticationf |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [IA-5](#ia-5-authenticator-management), [SA-4](#sa-4-acquisition-process), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection) |
| Related enhancements | None |
| What it is | This control addresses ia-7 for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-8 - Identification and Authentication (Non-organizational Users)

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IA-8` |
| Control title | Identification and Authentication (Non-organizational Users) |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-6](#ac-6-least-privilege), [AC-14](#ac-14-permitted-actions-without-identification-or-authentication), [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-4](#ia-4-identifier-management), [IA-5](#ia-5-authenticator-management), [IA-11](#ia-11-re-authentication), [MA-4](#ma-4-nonlocal-maintenance), [RA-3](#ra-3-risk-assessment), [SA-4](#sa-4-acquisition-process), [SC-8](#sc-8-transmission-confidentiality-and-integrity) |
| Related enhancements | None |
| What it is | This control addresses identification and authentication \(non-organizational users\) for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-11 - Re-authentication

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IA-11` |
| Control title | Re-authentication |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-11](#ac-11-device-lock), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-3](#ia-3-device-identification-and-authentication), [IA-4](#ia-4-identifier-management), [IA-8](#ia-8-identification-and-authentication-non-organizational-users) |
| Related enhancements | None |
| What it is | This control addresses re-authentication for CJIS systems, users, or data. |
| Recommended approach | Use unique identities, strong authenticators, and controlled lifecycle management. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IA-12 - Identity Proofing

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IA-12` |
| Control title | Identity Proofing |
| Parent control | `N/A` |
| Related controls | [AC-5](#ac-5-separation-of-duties), [IA-1](#ia-1-policy-and-procedures), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-3](#ia-3-device-identification-and-authentication), [IA-4](#ia-4-identifier-management), [IA-5](#ia-5-authenticator-management), [IA-6](#ia-6-authentication-feedback), [IA-8](#ia-8-identification-and-authentication-non-organizational-users) |
| Related enhancements | [IA-12(2)](#ia-122-identity-evidence), [IA-12(3)](#ia-123-identity-evidence-validation-and-verification), [IA-12(5)](#ia-125-address-confirmation-164-incident-response-ir) |
| What it is | Enhancement to IA-12 (Identity Proofing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific address confirmation ..................................................................164 incident response (ir) requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-12(5)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IA-12(2) - Identity Evidence

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IA-12(2)` |
| Control title | Identity Evidence |
| Parent control | `IA-12` |
| Related controls | See parent control ([IA-12](#ia-12-identity-proofing)) |
| Related enhancements | N/A |
| What it is | Enhancement to IA-12 (Identity Proofing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identity evidence requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-12(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IA-12(3) - Identity Evidence Validation and Verification

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IA-12(3)` |
| Control title | Identity Evidence Validation and Verification |
| Parent control | `IA-12` |
| Related controls | See parent control ([IA-12](#ia-12-identity-proofing)) |
| Related enhancements | N/A |
| What it is | Enhancement to IA-12 (Identity Proofing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific identity evidence validation and verification requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-12(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IA-12(5) - Address Confirmation ..................................................................164 INCIDENT RESPONSE (Ir)

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IA-12(5)` |
| Control title | Address Confirmation ..................................................................164 INCIDENT RESPONSE (Ir) |
| Parent control | `IA-12` |
| Related controls | See parent control ([IA-12](#ia-12-identity-proofing)) |
| Related enhancements | N/A |
| What it is | Enhancement to IA-12 (Identity Proofing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific address confirmation ..................................................................164 incident response (ir) requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IA-12(5)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Incident Response (IR)

### IR-1 - Policy and Procedures

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IR-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses ir-1 for CJIS systems, users, or data. |
| Recommended approach | Use a clear reporting path and preserve evidence during every incident. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IR-2 - Incident Response Training

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IR-2` |
| Control title | Incident Response Training |
| Parent control | `N/A` |
| Related controls | [AT-2](#at-2-literacy-training-and-awareness), [AT-3](#at-3-role-based-training), [AT-4](#at-4-training-records), [CP-3](#cp-3-contingency-training), [IR-3](#ir-3-incident-response-testing), [IR-4](#ir-4-incident-handling), [IR-8](#ir-8-incident-response-plan) |
| Related enhancements | [IR-2(3)](#ir-23-breach-168-x-12272024-cjissecpol-v60) |
| What it is | Enhancement to IR-2 (Incident Response Training) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific breach ..........................................................................168 x 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-2(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IR-2(3) - Breach ..........................................................................168 X 12/27/2024 CJISSECPOL V6.0

Tags: #priority/p3 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IR-2(3)` |
| Control title | Breach ..........................................................................168 X 12/27/2024 CJISSECPOL V6.0 |
| Parent control | `IR-2` |
| Related controls | See parent control ([IR-2](#ir-2-incident-response-training)) |
| Related enhancements | N/A |
| What it is | Enhancement to IR-2 (Incident Response Training) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific breach ..........................................................................168 x 12/27/2024 cjissecpol v6.0 requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-2(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IR-3 - Incident Response Testing

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IR-3` |
| Control title | Incident Response Testing |
| Parent control | `N/A` |
| Related controls | [CP-3](#cp-3-contingency-training), [CP-4](#cp-4-contingency-plan-testing), [IR-2](#ir-2-incident-response-training), [IR-4](#ir-4-incident-handling), [IR-8](#ir-8-incident-response-plan) |
| Related enhancements | [IR-3(2)](#ir-32-coordination-with-related-plans) |
| What it is | Enhancement to IR-3 (Incident Response Testing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordination with related plans requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-3(2)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IR-3(2) - Coordination with Related Plans

Tags: #priority/p3 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IR-3(2)` |
| Control title | Coordination with Related Plans |
| Parent control | `IR-3` |
| Related controls | See parent control ([IR-3](#ir-3-incident-response-testing)) |
| Related enhancements | N/A |
| What it is | Enhancement to IR-3 (Incident Response Testing) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific coordination with related plans requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-3(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IR-4 - Incident Handling

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IR-4` |
| Control title | Incident Handling |
| Parent control | `N/A` |
| Related controls | [AC-19](#ac-19-access-control-for-mobile-devices), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-7](#au-7-audit-record-reduction-and-report-generation), [CM-6](#cm-6-configuration-settings), [CP-2](#cp-2-contingency-plan), [CP-3](#cp-3-contingency-training), [CP-4](#cp-4-contingency-plan-testing), [IR-2](#ir-2-incident-response-training), [IR-3](#ir-3-incident-response-testing), [IR-5](#ir-5-incident-monitoring), [IR-6](#ir-6-incident-reporting), [IR-8](#ir-8-incident-response-plan), [PE-6](#pe-6-monitoring-physical-access), [PL-2](#pl-2-system-security-and-privacy-plans), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-5](#sc-5-denial-of-service-protection), [SC-7](#sc-7-boundary-protection), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity) |
| Related enhancements | [IR-4(1)](#ir-41-automated-incident-handling-processes) |
| What it is | Enhancement to IR-4 (Incident Handling) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated incident handling processes requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-4(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IR-4(1) - Automated Incident Handling Processes

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IR-4(1)` |
| Control title | Automated Incident Handling Processes |
| Parent control | `IR-4` |
| Related controls | See parent control ([IR-4](#ir-4-incident-handling)) |
| Related enhancements | N/A |
| What it is | Enhancement to IR-4 (Incident Handling) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated incident handling processes requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-4(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IR-5 - Incident Monitoring

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IR-5` |
| Control title | Incident Monitoring |
| Parent control | `N/A` |
| Related controls | [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-7](#au-7-audit-record-reduction-and-report-generation), [IR-4](#ir-4-incident-handling), [IR-6](#ir-6-incident-reporting), [IR-8](#ir-8-incident-response-plan), [PE-6](#pe-6-monitoring-physical-access), [SC-5](#sc-5-denial-of-service-protection), [SC-7](#sc-7-boundary-protection), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity) |
| Related enhancements | None |
| What it is | This control addresses incident monitoring for CJIS systems, users, or data. |
| Recommended approach | Use a clear reporting path and preserve evidence during every incident. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IR-6 - Incident Reporting

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `IR-6` |
| Control title | Incident Reporting |
| Parent control | `N/A` |
| Related controls | [CM-6](#cm-6-configuration-settings), [CP-2](#cp-2-contingency-plan), [IR-4](#ir-4-incident-handling), [IR-5](#ir-5-incident-monitoring), [IR-8](#ir-8-incident-response-plan) |
| Related enhancements | [IR-6(1)](#ir-61-automated-reporting), [IR-6(3)](#ir-63-supply-chain-coordination) |
| What it is | Enhancement to IR-6 (Incident Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific supply chain coordination requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-6(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IR-6(1) - Automated Reporting

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IR-6(1)` |
| Control title | Automated Reporting |
| Parent control | `IR-6` |
| Related controls | See parent control ([IR-6](#ir-6-incident-reporting)) |
| Related enhancements | N/A |
| What it is | Enhancement to IR-6 (Incident Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated reporting requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-6(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IR-6(3) - Supply Chain Coordination

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IR-6(3)` |
| Control title | Supply Chain Coordination |
| Parent control | `IR-6` |
| Related controls | See parent control ([IR-6](#ir-6-incident-reporting)) |
| Related enhancements | N/A |
| What it is | Enhancement to IR-6 (Incident Reporting) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific supply chain coordination requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-6(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IR-7 - Incident Response Assistance

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IR-7` |
| Control title | Incident Response Assistance |
| Parent control | `N/A` |
| Related controls | [AT-2](#at-2-literacy-training-and-awareness), [AT-3](#at-3-role-based-training), [IR-4](#ir-4-incident-handling), [IR-6](#ir-6-incident-reporting), [IR-8](#ir-8-incident-response-plan), [SA-9](#sa-9-external-system-services) |
| Related enhancements | [IR-7(1)](#ir-71-automation-support-for-availability-of-information-and-support10f) |
| What it is | Enhancement to IR-7 (Incident Response Assistance) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automation support for availability of information and support10f requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-7(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IR-7(1) - Automation Support for Availability of Information and Support10f

Tags: #priority/p3 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IR-7(1)` |
| Control title | Automation Support for Availability of Information and Support10f |
| Parent control | `IR-7` |
| Related controls | See parent control ([IR-7](#ir-7-incident-response-assistance)) |
| Related enhancements | N/A |
| What it is | Enhancement to IR-7 (Incident Response Assistance) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automation support for availability of information and support10f requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-7(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### IR-8 - Incident Response Plan

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `IR-8` |
| Control title | Incident Response Plan |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [CP-2](#cp-2-contingency-plan), [CP-4](#cp-4-contingency-plan-testing), [IR-4](#ir-4-incident-handling), [IR-7](#ir-7-incident-response-assistance), [PE-6](#pe-6-monitoring-physical-access), [PL-2](#pl-2-system-security-and-privacy-plans), [SA-15](#sa-15-development-process-standards-and-tools), [SI-12](#si-12-information-management-and-retention), [SR-8](#sr-8-notification-agreements) |
| Related enhancements | [IR-8(1)](#ir-81-breaches-173-maintenance-ma) |
| What it is | Enhancement to IR-8 (Incident Response Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific breaches .............................................................................173 maintenance (ma) requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-8(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### IR-8(1) - Breaches .............................................................................173 MAINTENANCE (Ma)

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `IR-8(1)` |
| Control title | Breaches .............................................................................173 MAINTENANCE (Ma) |
| Parent control | `IR-8` |
| Related controls | See parent control ([IR-8](#ir-8-incident-response-plan)) |
| Related enhancements | N/A |
| What it is | Enhancement to IR-8 (Incident Response Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific breaches .............................................................................173 maintenance (ma) requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `IR-8(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Maintenance (MA)

### MA-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `MA-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MA-2 - Controlled Maintenance

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `MA-2` |
| Control title | Controlled Maintenance |
| Parent control | `N/A` |
| Related controls | [CM-2](#cm-2-baseline-configuration), [CM-3](#cm-3-configuration-change-control), [CM-4](#cm-4-impact-analyses), [CM-5](#cm-5-access-restrictions-for-change), [CM-8](#cm-8-system-component-inventory), [MA-4](#ma-4-nonlocal-maintenance), [MP-6](#mp-6-media-sanitization), [PE-16](#pe-16-delivery-and-removal), [SI-2](#si-2-flaw-remediation), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-11](#sr-11-sr-11) |
| Related enhancements | None |
| What it is | This control addresses controlled maintenance for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MA-3 - Maintenance Tools

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `MA-3` |
| Control title | Maintenance Tools |
| Parent control | `N/A` |
| Related controls | [MA-2](#ma-2-controlled-maintenance), [PE-16](#pe-16-delivery-and-removal) |
| Related enhancements | [MA-3(1)](#ma-31-inspect-tools), [MA-3(2)](#ma-32-inspect-media), [MA-3(3)](#ma-33-prevent-unauthorized-removal) |
| What it is | Enhancement to MA-3 (Maintenance Tools) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prevent unauthorized removal requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `MA-3(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### MA-3(1) - Inspect Tools

Tags: #priority/p4 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `MA-3(1)` |
| Control title | Inspect Tools |
| Parent control | `MA-3` |
| Related controls | See parent control ([MA-3](#ma-3-maintenance-tools)) |
| Related enhancements | N/A |
| What it is | Enhancement to MA-3 (Maintenance Tools) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific inspect tools requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `MA-3(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### MA-3(2) - Inspect Media

Tags: #priority/p4 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `MA-3(2)` |
| Control title | Inspect Media |
| Parent control | `MA-3` |
| Related controls | See parent control ([MA-3](#ma-3-maintenance-tools)) |
| Related enhancements | N/A |
| What it is | Enhancement to MA-3 (Maintenance Tools) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific inspect media requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `MA-3(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### MA-3(3) - Prevent Unauthorized Removal

Tags: #priority/p4 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `MA-3(3)` |
| Control title | Prevent Unauthorized Removal |
| Parent control | `MA-3` |
| Related controls | See parent control ([MA-3](#ma-3-maintenance-tools)) |
| Related enhancements | N/A |
| What it is | Enhancement to MA-3 (Maintenance Tools) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific prevent unauthorized removal requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `MA-3(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MA-4 - Nonlocal Maintenance

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `MA-4` |
| Control title | Nonlocal Maintenance |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-6](#ac-6-least-privilege), [AC-17](#ac-17-remote-access), [AU-2](#au-2-event-logging), [AU-3](#au-3-content-of-audit-records), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-4](#ia-4-identifier-management), [IA-5](#ia-5-authenticator-management), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-2](#ma-2-controlled-maintenance), [MA-5](#ma-5-maintenance-personnel), [PL-2](#pl-2-system-security-and-privacy-plans), [SC-7](#sc-7-boundary-protection), [SC-10](#sc-10-network-disconnect) |
| Related enhancements | None |
| What it is | This control addresses ma-4 for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MA-5 - Maintenance Personnel

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `MA-5` |
| Control title | Maintenance Personnel |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-5](#ac-5-separation-of-duties), [AC-6](#ac-6-least-privilege), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-4](#ma-4-nonlocal-maintenance), [MP-2](#mp-2-media-access), [PE-2](#pe-2-physical-access-authorizations), [PE-3](#pe-3-physical-access-control), [PS-7](#ps-7-external-personnel-security), [RA-3](#ra-3-risk-assessment) |
| Related enhancements | None |
| What it is | This control addresses maintenance personnel for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MA-6 - Timely Maintenance

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `MA-6` |
| Control title | Timely Maintenance |
| Parent control | `N/A` |
| Related controls | [CM-8](#cm-8-system-component-inventory), [CP-2](#cp-2-contingency-plan), [CP-7](#cp-7-alternate-processing-site), [RA-7](#ra-7-risk-response), [SA-15](#sa-15-development-process-standards-and-tools), [SR-2](#sr-2-supply-chain-risk-management-plan), [SR-3](#sr-3-supply-chain-controls-and-processes) |
| Related enhancements | None |
| What it is | This control addresses timely maintenance for CJIS systems, users, or data. |
| Recommended approach | Approve maintenance work, log it, and limit access to the minimum necessary. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Media Protection (MP)

### MP-1 - Policy and Procedures

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `MP-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MP-2 - Media Access

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `MP-2` |
| Control title | Media Access |
| Parent control | `N/A` |
| Related controls | [AC-19](#ac-19-access-control-for-mobile-devices), [AU-9](#au-9-protection-of-audit-information), [CP-2](#cp-2-contingency-plan), [CP-9](#cp-9-system-backup), [CP-10](#cp-10-system-recovery-and-reconstitution), [MA-5](#ma-5-maintenance-personnel), [MP-4](#mp-4-media-storage), [MP-6](#mp-6-media-sanitization), [PE-2](#pe-2-physical-access-authorizations), [PE-3](#pe-3-physical-access-control), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses media access for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MP-3 - Media Marking

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `MP-3` |
| Control title | Media Marking |
| Parent control | `N/A` |
| Related controls | [CP-9](#cp-9-system-backup), [MP-5](#mp-5-media-transport), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses media marking for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MP-4 - Media Storage

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `MP-4` |
| Control title | Media Storage |
| Parent control | `N/A` |
| Related controls | [AC-19](#ac-19-access-control-for-mobile-devices), [CP-2](#cp-2-contingency-plan), [CP-6](#cp-6-alternate-storage-site), [CP-9](#cp-9-system-backup), [CP-10](#cp-10-system-recovery-and-reconstitution), [MP-2](#mp-2-media-access), [MP-7](#mp-7-media-use), [PE-3](#pe-3-physical-access-control), [PL-2](#pl-2-system-security-and-privacy-plans), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SC-28](#sc-28-protection-of-information-at-rest), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses media storage for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MP-5 - Media Transport

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `MP-5` |
| Control title | Media Transport |
| Parent control | `N/A` |
| Related controls | [AC-7](#ac-7-unsuccessful-logon-attempts), [AC-19](#ac-19-access-control-for-mobile-devices), [CP-2](#cp-2-contingency-plan), [CP-9](#cp-9-system-backup), [MP-3](#mp-3-media-marking), [MP-4](#mp-4-media-storage), [PE-16](#pe-16-delivery-and-removal), [PL-2](#pl-2-system-security-and-privacy-plans), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SC-28](#sc-28-protection-of-information-at-rest) |
| Related enhancements | None |
| What it is | This control addresses media transport for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MP-6 - Media Sanitization

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `MP-6` |
| Control title | Media Sanitization |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-7](#ac-7-unsuccessful-logon-attempts), [AU-11](#au-11-audit-record-retention), [MA-2](#ma-2-controlled-maintenance), [MA-3](#ma-3-maintenance-tools), [MA-4](#ma-4-nonlocal-maintenance), [MA-5](#ma-5-maintenance-personnel), [SI-12](#si-12-information-management-and-retention), [SR-11](#sr-11-sr-11) |
| Related enhancements | None |
| What it is | This control addresses media sanitization for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### MP-7 - Media Use

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `MP-7` |
| Control title | Media Use |
| Parent control | `N/A` |
| Related controls | [AC-19](#ac-19-access-control-for-mobile-devices), [AC-20](#ac-20-use-of-external-systems), [PL-4](#pl-4-rules-of-behavior) |
| Related enhancements | None |
| What it is | This control addresses media use for CJIS systems, users, or data. |
| Recommended approach | Track media from creation through disposal. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Physical and Environmental Protection (PE)

### PE-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-2 - Physical Access Authorizations

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PE-2` |
| Control title | Physical Access Authorizations |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [AU-9](#au-9-protection-of-audit-information), [IA-4](#ia-4-identifier-management), [MA-5](#ma-5-maintenance-personnel), [MP-2](#mp-2-media-access), [PE-3](#pe-3-physical-access-control), [PE-4](#pe-4-access-control-for-transmission), [PE-5](#pe-5-access-control-for-output-devices), [PE-8](#pe-8-visitor-access-records), [PS-3](#ps-3-personnel-screening), [PS-4](#ps-4-personnel-termination), [PS-5](#ps-5-personnel-transfer), [PS-6](#ps-6-access-agreements) |
| Related enhancements | None |
| What it is | This control addresses physical access authorizations for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-3 - Physical Access Control

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PE-3` |
| Control title | Physical Access Control |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [AU-2](#au-2-event-logging), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-9](#au-9-protection-of-audit-information), [CP-10](#cp-10-system-recovery-and-reconstitution), [IA-3](#ia-3-device-identification-and-authentication), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-5](#ma-5-maintenance-personnel), [MP-2](#mp-2-media-access), [MP-4](#mp-4-media-storage), [PE-2](#pe-2-physical-access-authorizations), [PE-4](#pe-4-access-control-for-transmission), [PE-5](#pe-5-access-control-for-output-devices), [PE-8](#pe-8-visitor-access-records), [PS-2](#ps-2-position-risk-designation), [PS-3](#ps-3-personnel-screening), [PS-6](#ps-6-access-agreements), [PS-7](#ps-7-external-personnel-security), [RA-3](#ra-3-risk-assessment), [SC-28](#sc-28-protection-of-information-at-rest), [SI-4](#si-4-system-monitoring), [SR-3](#sr-3-supply-chain-controls-and-processes) |
| Related enhancements | None |
| What it is | This control addresses pe-3 for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-4 - Access Control for Transmission

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PE-4` |
| Control title | Access Control for Transmission |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [IA-4](#ia-4-identifier-management), [MP-2](#mp-2-media-access), [MP-4](#mp-4-media-storage), [PE-2](#pe-2-physical-access-authorizations), [PE-3](#pe-3-physical-access-control), [PE-5](#pe-5-access-control-for-output-devices), [PE-9](#pe-9-power-equipment-and-cabling), [SC-7](#sc-7-boundary-protection), [SC-8](#sc-8-transmission-confidentiality-and-integrity) |
| Related enhancements | None |
| What it is | This control addresses access control for transmission for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-5 - Access Control for Output Devices

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PE-5` |
| Control title | Access Control for Output Devices |
| Parent control | `N/A` |
| Related controls | [PE-2](#pe-2-physical-access-authorizations), [PE-3](#pe-3-physical-access-control), [PE-4](#pe-4-access-control-for-transmission) |
| Related enhancements | None |
| What it is | This control addresses access control for output devices for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-6 - Monitoring Physical Access

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PE-6` |
| Control title | Monitoring Physical Access |
| Parent control | `N/A` |
| Related controls | [AU-2](#au-2-event-logging), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-9](#au-9-protection-of-audit-information), [AU-12](#au-12-audit-record-generation), [CA-7](#ca-7-continuous-monitoring), [CP-10](#cp-10-system-recovery-and-reconstitution), [IR-4](#ir-4-incident-handling), [IR-8](#ir-8-incident-response-plan) |
| Related enhancements | None |
| What it is | This control addresses pe-6 for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-8 - Visitor Access Records

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-8` |
| Control title | Visitor Access Records |
| Parent control | `N/A` |
| Related controls | [PE-2](#pe-2-physical-access-authorizations), [PE-3](#pe-3-physical-access-control), [PE-6](#pe-6-monitoring-physical-access) |
| Related enhancements | [PE-8(3)](#pe-83-limit-personally-identifiable-information-elements) |
| What it is | Enhancement to PE-8 (Visitor Access Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `PE-8(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### PE-8(3) - Limit Personally Identifiable Information Elements

Tags: #priority/p4 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `PE-8(3)` |
| Control title | Limit Personally Identifiable Information Elements |
| Parent control | `PE-8` |
| Related controls | See parent control ([PE-8](#pe-8-visitor-access-records)) |
| Related enhancements | N/A |
| What it is | Enhancement to PE-8 (Visitor Access Records) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `PE-8(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-9 - Power Equipment and Cabling

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-9` |
| Control title | Power Equipment and Cabling |
| Parent control | `N/A` |
| Related controls | [PE-4](#pe-4-access-control-for-transmission) |
| Related enhancements | None |
| What it is | This control addresses power equipment and cabling for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-10 - Emergency Shutoff

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-10` |
| Control title | Emergency Shutoff |
| Parent control | `N/A` |
| Related controls | [PE-15](#pe-15-water-damage-protection) |
| Related enhancements | None |
| What it is | This control addresses emergency shutoff for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-11 - Emergency Power

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-11` |
| Control title | Emergency Power |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [CP-2](#cp-2-contingency-plan), [CP-7](#cp-7-alternate-processing-site) |
| Related enhancements | None |
| What it is | This control addresses emergency power for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-12 - Emergency Lighting

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-12` |
| Control title | Emergency Lighting |
| Parent control | `N/A` |
| Related controls | [CP-2](#cp-2-contingency-plan), [CP-7](#cp-7-alternate-processing-site) |
| Related enhancements | None |
| What it is | This control addresses emergency lighting for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-13 - Fire Protection

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-13` |
| Control title | Fire Protection |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training) |
| Related enhancements | [PE-13(1)](#pe-131-detection-systems-227-automatic-activation-and-notification) |
| What it is | This control addresses fire protection for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### PE-13(1) - Detection Systems \227 Automatic Activation and Notification

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `PE-13(1)` |
| Control title | Detection Systems \227 Automatic Activation and Notification |
| Parent control | `PE-13` |
| Related controls | See parent control ([PE-13](#pe-13-fire-protection)) |
| Related enhancements | N/A |
| What it is | Enhancement to PE-13 (Fire Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific detection systems \227 automatic activation and notification requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `PE-13(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-14 - Environmental Controls

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-14` |
| Control title | Environmental Controls |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [CP-2](#cp-2-contingency-plan) |
| Related enhancements | None |
| What it is | This control addresses environmental controls for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-15 - Water Damage Protection

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PE-15` |
| Control title | Water Damage Protection |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [PE-10](#pe-10-emergency-shutoff) |
| Related enhancements | None |
| What it is | This control addresses water damage protection for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-16 - Delivery and Removal

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PE-16` |
| Control title | Delivery and Removal |
| Parent control | `N/A` |
| Related controls | [CM-3](#cm-3-configuration-change-control), [CM-8](#cm-8-system-component-inventory), [MA-2](#ma-2-controlled-maintenance), [MA-3](#ma-3-maintenance-tools), [MP-5](#mp-5-media-transport), [SR-2](#sr-2-supply-chain-risk-management-plan), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-6](#sr-6-supplier-assessments-and-reviews) |
| Related enhancements | None |
| What it is | This control addresses delivery and removal for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PE-17 - Alternate Work Site

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PE-17` |
| Control title | Alternate Work Site |
| Parent control | `N/A` |
| Related controls | [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [CP-7](#cp-7-alternate-processing-site) |
| Related enhancements | None |
| What it is | This control addresses alternate work site for CJIS systems, users, or data. |
| Recommended approach | Use layered physical safeguards appropriate to the site. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Planning (PL)

### PL-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PL-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PL-2 - System Security and Privacy Plans

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PL-2` |
| Control title | System Security and Privacy Plans |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-6](#ac-6-least-privilege), [AC-14](#ac-14-permitted-actions-without-identification-or-authentication), [AC-17](#ac-17-remote-access), [AC-20](#ac-20-use-of-external-systems), [CA-2](#ca-2-control-assessments), [CA-3](#ca-3-information-exchange), [CA-7](#ca-7-continuous-monitoring), [CM-9](#cm-9-configuration-management-plan), [CP-2](#cp-2-contingency-plan), [CP-4](#cp-4-contingency-plan-testing), [IR-4](#ir-4-incident-handling), [IR-8](#ir-8-incident-response-plan), [MA-4](#ma-4-nonlocal-maintenance), [MA-5](#ma-5-maintenance-personnel), [MP-4](#mp-4-media-storage), [MP-5](#mp-5-media-transport), [PL-8](#pl-8-security-and-privacy-architectures), [PL-10](#pl-10-baseline-selection), [PL-11](#pl-11-baseline-tailoring), [RA-3](#ra-3-risk-assessment), [RA-9](#ra-9-criticality-analysis), [SA-5](#sa-5-system-documentation), [SA-22](#sa-22-unsupported-system-components), [SI-12](#si-12-information-management-and-retention), [SR-2](#sr-2-supply-chain-risk-management-plan) |
| Related enhancements | None |
| What it is | This control addresses system security and privacy plans for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PL-4 - Rules of Behavior

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PL-4` |
| Control title | Rules of Behavior |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-6](#ac-6-least-privilege), [AC-8](#ac-8-system-use-notification), [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AC-19](#ac-19-access-control-for-mobile-devices), [AC-20](#ac-20-use-of-external-systems), [AT-2](#at-2-literacy-training-and-awareness), [AT-3](#at-3-role-based-training), [CM-11](#cm-11-user-installed-software), [IA-2](#ia-2-identification-and-authentication-organizational-users), [IA-4](#ia-4-identifier-management), [IA-5](#ia-5-authenticator-management), [MP-7](#mp-7-media-use), [PS-6](#ps-6-access-agreements), [PS-8](#ps-8-personnel-sanctions), [SA-5](#sa-5-system-documentation), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses pl-4 for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PL-8 - Security and Privacy Architectures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PL-8` |
| Control title | Security and Privacy Architectures |
| Parent control | `N/A` |
| Related controls | [CM-2](#cm-2-baseline-configuration), [CM-6](#cm-6-configuration-settings), [PL-2](#pl-2-system-security-and-privacy-plans), [PL-7](#pl-7-pl-7), [PL-9](#pl-9-central-management), PM-5, [RA-9](#ra-9-criticality-analysis), [SA-3](#sa-3-system-development-life-cycle), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-7](#sc-7-boundary-protection) |
| Related enhancements | None |
| What it is | This control addresses security and privacy architectures for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PL-9 - Central Management

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PL-9` |
| Control title | Central Management |
| Parent control | `N/A` |
| Related controls | [PL-8](#pl-8-security-and-privacy-architectures) |
| Related enhancements | None |
| What it is | This control addresses central management for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PL-10 - Baseline Selection

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PL-10` |
| Control title | Baseline Selection |
| Parent control | `N/A` |
| Related controls | [PL-2](#pl-2-system-security-and-privacy-plans), [PL-11](#pl-11-baseline-tailoring), [RA-2](#ra-2-security-categorization), [RA-3](#ra-3-risk-assessment), [SA-8](#sa-8-security-and-privacy-engineering-principles) |
| Related enhancements | None |
| What it is | This control addresses baseline selection for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PL-11 - Baseline Tailoring

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PL-11` |
| Control title | Baseline Tailoring |
| Parent control | `N/A` |
| Related controls | [PL-10](#pl-10-baseline-selection), [RA-2](#ra-2-security-categorization), [RA-3](#ra-3-risk-assessment), [RA-9](#ra-9-criticality-analysis), [SA-8](#sa-8-security-and-privacy-engineering-principles) |
| Related enhancements | None |
| What it is | This control addresses baseline tailoring for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PL-7 - Pl-7

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `PL-7` |
| Control title | Pl-7 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses pl-7 for CJIS systems, users, or data. |
| Recommended approach | Keep planning docs aligned to the actual environment and controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Personnel Security (PS)

### PS-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PS-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PS-2 - Position Risk Designation

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PS-2` |
| Control title | Position Risk Designation |
| Parent control | `N/A` |
| Related controls | [AC-5](#ac-5-separation-of-duties), [AT-3](#at-3-role-based-training), [PE-2](#pe-2-physical-access-authorizations), [PE-3](#pe-3-physical-access-control), [PL-2](#pl-2-system-security-and-privacy-plans), [PS-3](#ps-3-personnel-screening), [PS-6](#ps-6-access-agreements), [SA-5](#sa-5-system-documentation), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses position risk designation for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PS-3 - Personnel Screening

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PS-3` |
| Control title | Personnel Screening |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [IA-4](#ia-4-identifier-management), [MA-5](#ma-5-maintenance-personnel), [PE-2](#pe-2-physical-access-authorizations), [PS-2](#ps-2-position-risk-designation), [PS-6](#ps-6-access-agreements), [PS-7](#ps-7-external-personnel-security) |
| Related enhancements | None |
| What it is | This control addresses personnel screening for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PS-4 - Personnel Termination

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PS-4` |
| Control title | Personnel Termination |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [IA-4](#ia-4-identifier-management), [PE-2](#pe-2-physical-access-authorizations), [PS-6](#ps-6-access-agreements), [PS-7](#ps-7-external-personnel-security) |
| Related enhancements | None |
| What it is | This control addresses personnel termination for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PS-5 - Personnel Transfer

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PS-5` |
| Control title | Personnel Transfer |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [IA-4](#ia-4-identifier-management), [PE-2](#pe-2-physical-access-authorizations), [PS-4](#ps-4-personnel-termination), [PS-7](#ps-7-external-personnel-security) |
| Related enhancements | None |
| What it is | This control addresses personnel transfer for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PS-6 - Access Agreements

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PS-6` |
| Control title | Access Agreements |
| Parent control | `N/A` |
| Related controls | [AC-17](#ac-17-remote-access), [PE-2](#pe-2-physical-access-authorizations), [PL-4](#pl-4-rules-of-behavior), [PS-2](#ps-2-position-risk-designation), [PS-3](#ps-3-personnel-screening), [PS-6](#ps-6-access-agreements), [PS-7](#ps-7-external-personnel-security), [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses access agreements for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PS-7 - External Personnel Security

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `PS-7` |
| Control title | External Personnel Security |
| Parent control | `N/A` |
| Related controls | [AT-2](#at-2-literacy-training-and-awareness), [AT-3](#at-3-role-based-training), [MA-5](#ma-5-maintenance-personnel), [PE-3](#pe-3-physical-access-control), [PS-2](#ps-2-position-risk-designation), [PS-3](#ps-3-personnel-screening), [PS-4](#ps-4-personnel-termination), [PS-5](#ps-5-personnel-transfer), [PS-6](#ps-6-access-agreements), [SA-5](#sa-5-system-documentation), [SA-9](#sa-9-external-system-services) |
| Related enhancements | None |
| What it is | This control addresses external personnel security for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PS-8 - Personnel Sanctions

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PS-8` |
| Control title | Personnel Sanctions |
| Parent control | `N/A` |
| Related controls | All XX-1 Controls, [PL-4](#pl-4-rules-of-behavior), [PS-6](#ps-6-access-agreements) |
| Related enhancements | None |
| What it is | This control addresses personnel sanctions for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### PS-9 - Position Descriptions

Tags: #priority/p4 #existing/no

| Field | Value |
| --- | --- |
| Control code | `PS-9` |
| Control title | Position Descriptions |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses position descriptions for CJIS systems, users, or data. |
| Recommended approach | Screen people before access and remove access promptly when status changes. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Risk Assessment (RA)

### RA-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `RA-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### RA-2 - Security Categorization

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `RA-2` |
| Control title | Security Categorization |
| Parent control | `N/A` |
| Related controls | [CM-8](#cm-8-system-component-inventory), [MP-4](#mp-4-media-storage), [PL-2](#pl-2-system-security-and-privacy-plans), [PL-10](#pl-10-baseline-selection), [PL-11](#pl-11-baseline-tailoring), [RA-3](#ra-3-risk-assessment), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [RA-7](#ra-7-risk-response), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-7](#sc-7-boundary-protection), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses security categorization for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### RA-3 - Risk Assessment

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `RA-3` |
| Control title | Risk Assessment |
| Parent control | `N/A` |
| Related controls | [CA-3](#ca-3-information-exchange), [CA-6](#ca-6-authorization), [CM-4](#cm-4-impact-analyses), [CP-6](#cp-6-alternate-storage-site), [CP-7](#cp-7-alternate-processing-site), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-5](#ma-5-maintenance-personnel), [PE-3](#pe-3-physical-access-control), [PE-8](#pe-8-visitor-access-records), [PL-2](#pl-2-system-security-and-privacy-plans), [PL-10](#pl-10-baseline-selection), [PL-11](#pl-11-baseline-tailoring), [RA-2](#ra-2-security-categorization), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [RA-7](#ra-7-risk-response), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses ra-3 for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### RA-5 - Vulnerability Monitoring and Scanning

Tags: #priority/p1 #existing/no

| Field | Value |
| --- | --- |
| Control code | `RA-5` |
| Control title | Vulnerability Monitoring and Scanning |
| Parent control | `N/A` |
| Related controls | [CA-2](#ca-2-control-assessments), [CA-7](#ca-7-continuous-monitoring), [CM-2](#cm-2-baseline-configuration), [CM-4](#cm-4-impact-analyses), [CM-6](#cm-6-configuration-settings), [CM-8](#cm-8-system-component-inventory), [RA-2](#ra-2-security-categorization), [RA-3](#ra-3-risk-assessment), [SA-11](#sa-11-developer-testing-and-evaluation), [SA-15](#sa-15-development-process-standards-and-tools), [SI-2](#si-2-flaw-remediation), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity), [SR-11](#sr-11-sr-11) |
| Related enhancements | [RA-5(2)](#ra-52-update-vulnerabilities-to-be-scanned), [RA-5(5)](#ra-55-privileged-access), [RA-5(11)](#ra-511-public-disclosure-program) |
| What it is | Enhancement to RA-5 (Vulnerability Monitoring and Scanning) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific public disclosure program requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `RA-5(11)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### RA-5(2) - Update Vulnerabilities to Be Scanned

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `RA-5(2)` |
| Control title | Update Vulnerabilities to Be Scanned |
| Parent control | `RA-5` |
| Related controls | See parent control ([RA-5](#ra-5-vulnerability-monitoring-and-scanning)) |
| Related enhancements | N/A |
| What it is | Enhancement to RA-5 (Vulnerability Monitoring and Scanning) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific update vulnerabilities to be scanned requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `RA-5(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### RA-5(5) - Privileged Access

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `RA-5(5)` |
| Control title | Privileged Access |
| Parent control | `RA-5` |
| Related controls | See parent control ([RA-5](#ra-5-vulnerability-monitoring-and-scanning)) |
| Related enhancements | N/A |
| What it is | Enhancement to RA-5 (Vulnerability Monitoring and Scanning) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific privileged access requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `RA-5(5)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### RA-5(11) - Public Disclosure Program

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `RA-5(11)` |
| Control title | Public Disclosure Program |
| Parent control | `RA-5` |
| Related controls | See parent control ([RA-5](#ra-5-vulnerability-monitoring-and-scanning)) |
| Related enhancements | N/A |
| What it is | Enhancement to RA-5 (Vulnerability Monitoring and Scanning) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific public disclosure program requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `RA-5(11)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### RA-7 - Risk Response

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `RA-7` |
| Control title | Risk Response |
| Parent control | `N/A` |
| Related controls | [CA-5](#ca-5-plan-of-action-and-milestones), [RA-2](#ra-2-security-categorization), [RA-3](#ra-3-risk-assessment), [SR-2](#sr-2-supply-chain-risk-management-plan) |
| Related enhancements | None |
| What it is | This control addresses risk response for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### RA-9 - Criticality Analysis

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `RA-9` |
| Control title | Criticality Analysis |
| Parent control | `N/A` |
| Related controls | [CP-2](#cp-2-contingency-plan), [PL-2](#pl-2-system-security-and-privacy-plans), [PL-8](#pl-8-security-and-privacy-architectures), [PL-11](#pl-11-baseline-tailoring), [RA-2](#ra-2-security-categorization), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-15](#sa-15-development-process-standards-and-tools), [SR-5](#sr-5-acquisition-strategies-tools-and-methods) |
| Related enhancements | None |
| What it is | This control addresses ra-9 for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### RA-8 - Ra-8

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `RA-8` |
| Control title | Ra-8 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses ra-8 for CJIS systems, users, or data. |
| Recommended approach | Reassess risks regularly and close findings based on priority. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## System and Services Acquisition / Development (SA)

### SA-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-2 - Allocation of Resources

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-2` |
| Control title | Allocation of Resources |
| Parent control | `N/A` |
| Related controls | [SA-9](#sa-9-external-system-services), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-5](#sr-5-acquisition-strategies-tools-and-methods) |
| Related enhancements | None |
| What it is | This control addresses allocation of resources for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-3 - System Development Life Cycle

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-3` |
| Control title | System Development Life Cycle |
| Parent control | `N/A` |
| Related controls | [PL-8](#pl-8-security-and-privacy-architectures), [SA-4](#sa-4-acquisition-process), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-11](#sa-11-developer-testing-and-evaluation), [SA-15](#sa-15-development-process-standards-and-tools), [SA-22](#sa-22-unsupported-system-components), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-5](#sr-5-acquisition-strategies-tools-and-methods),  |
| Related enhancements | None |
| What it is | This control addresses system development life cycle for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-4 - Acquisition Process

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-4` |
| Control title | Acquisition Process |
| Parent control | `N/A` |
| Related controls | [CM-6](#cm-6-configuration-settings), [CM-8](#cm-8-system-component-inventory), [PS-7](#ps-7-external-personnel-security), [SA-3](#sa-3-system-development-life-cycle), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-11](#sa-11-developer-testing-and-evaluation), [SA-15](#sa-15-development-process-standards-and-tools), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-5](#sr-5-acquisition-strategies-tools-and-methods) |
| Related enhancements | [SA-4(1)](#sa-41-functional-properties-of-controls), [SA-4(2)](#sa-42-design-and-implementation-information-for-controls), [SA-4(9)](#sa-49-functions-ports-protocols-and-services-in-use), [SA-4(10)](#sa-410-use-of-approved-piv-products) |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific use of approved piv products requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SA-4(10)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SA-4(1) - Functional Properties of Controls

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SA-4(1)` |
| Control title | Functional Properties of Controls |
| Parent control | `SA-4` |
| Related controls | See parent control ([SA-4](#sa-4-acquisition-process)) |
| Related enhancements | N/A |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific functional properties of controls requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SA-4(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SA-4(2) - Design and Implementation Information for Controls

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SA-4(2)` |
| Control title | Design and Implementation Information for Controls |
| Parent control | `SA-4` |
| Related controls | See parent control ([SA-4](#sa-4-acquisition-process)) |
| Related enhancements | N/A |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific design and implementation information for controls requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SA-4(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SA-4(9) - Functions, Ports, Protocols, and Services in Use

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SA-4(9)` |
| Control title | Functions, Ports, Protocols, and Services in Use |
| Parent control | `SA-4` |
| Related controls | See parent control ([SA-4](#sa-4-acquisition-process)) |
| Related enhancements | N/A |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific functions, ports, protocols, and services in use requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SA-4(9)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SA-4(10) - Use of Approved Piv Products

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SA-4(10)` |
| Control title | Use of Approved Piv Products |
| Parent control | `SA-4` |
| Related controls | See parent control ([SA-4](#sa-4-acquisition-process)) |
| Related enhancements | N/A |
| What it is | Enhancement to SA-4 (Acquisition Process) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific use of approved piv products requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SA-4(10)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-5 - System Documentation

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-5` |
| Control title | System Documentation |
| Parent control | `N/A` |
| Related controls | [CM-4](#cm-4-impact-analyses), [CM-6](#cm-6-configuration-settings), [CM-7](#cm-7-least-functionality), [CM-8](#cm-8-system-component-inventory), [PL-2](#pl-2-system-security-and-privacy-plans), [PL-4](#pl-4-rules-of-behavior), [PL-8](#pl-8-security-and-privacy-architectures), [PS-2](#ps-2-position-risk-designation), [SA-3](#sa-3-system-development-life-cycle), [SA-4](#sa-4-acquisition-process), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SA-10](#sa-10-developer-configuration-management), [SA-11](#sa-11-developer-testing-and-evaluation), [SA-15](#sa-15-development-process-standards-and-tools), [SI-12](#si-12-information-management-and-retention), [SR-3](#sr-3-supply-chain-controls-and-processes) |
| Related enhancements | None |
| What it is | This control addresses system documentation for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-8 - Security and Privacy Engineering Principles

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-8` |
| Control title | Security and Privacy Engineering Principles |
| Parent control | `N/A` |
| Related controls | [PL-8](#pl-8-security-and-privacy-architectures), [RA-2](#ra-2-security-categorization), [RA-3](#ra-3-risk-assessment), [RA-9](#ra-9-criticality-analysis), [SA-3](#sa-3-system-development-life-cycle), [SA-4](#sa-4-acquisition-process), [SA-15](#sa-15-development-process-standards-and-tools), [SC-2](#sc-2-separation-of-system-and-user-functionality), [SC-39](#sc-39-process-isolation), [SR-2](#sr-2-supply-chain-risk-management-plan), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-5](#sr-5-acquisition-strategies-tools-and-methods) |
| Related enhancements | [SA-8(33)](#sa-833-minimization) |
| What it is | Enhancement to SA-8 (Security and Privacy Engineering Principles) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific minimization requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SA-8(33)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SA-8(33) - Minimization

Tags: #priority/p2 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SA-8(33)` |
| Control title | Minimization |
| Parent control | `SA-8` |
| Related controls | See parent control ([SA-8](#sa-8-security-and-privacy-engineering-principles)) |
| Related enhancements | N/A |
| What it is | Enhancement to SA-8 (Security and Privacy Engineering Principles) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific minimization requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SA-8(33)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-9 - External System Services

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-9` |
| Control title | External System Services |
| Parent control | `N/A` |
| Related controls | [AC-20](#ac-20-use-of-external-systems), [CA-3](#ca-3-information-exchange), [CP-2](#cp-2-contingency-plan), [IR-4](#ir-4-incident-handling), [IR-7](#ir-7-incident-response-assistance), [PL-10](#pl-10-baseline-selection), [PL-11](#pl-11-baseline-tailoring), [PS-7](#ps-7-external-personnel-security), [SA-2](#sa-2-allocation-of-resources), [SA-4](#sa-4-acquisition-process), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-5](#sr-5-acquisition-strategies-tools-and-methods) |
| Related enhancements | None |
| What it is | This control addresses sa-9 for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-10 - Developer Configuration Management

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-10` |
| Control title | Developer Configuration Management |
| Parent control | `N/A` |
| Related controls | [CM-2](#cm-2-baseline-configuration), [CM-3](#cm-3-configuration-change-control), [CM-4](#cm-4-impact-analyses), [CM-7](#cm-7-least-functionality), [CM-9](#cm-9-configuration-management-plan), [SA-4](#sa-4-acquisition-process), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-15](#sa-15-development-process-standards-and-tools), [SI-2](#si-2-flaw-remediation), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-5](#sr-5-acquisition-strategies-tools-and-methods), [SR-6](#sr-6-supplier-assessments-and-reviews) |
| Related enhancements | None |
| What it is | This control addresses developer configuration management for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-11 - Developer Testing and Evaluation

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-11` |
| Control title | Developer Testing and Evaluation |
| Parent control | `N/A` |
| Related controls | [CA-2](#ca-2-control-assessments), [CA-7](#ca-7-continuous-monitoring), [CM-4](#cm-4-impact-analyses), [SA-3](#sa-3-system-development-life-cycle), [SA-4](#sa-4-acquisition-process), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-15](#sa-15-development-process-standards-and-tools), [SI-2](#si-2-flaw-remediation), [SR-5](#sr-5-acquisition-strategies-tools-and-methods), [SR-6](#sr-6-supplier-assessments-and-reviews) |
| Related enhancements | None |
| What it is | This control addresses developer testing and evaluation for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-15 - Development Process, Standards, and Tools

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-15` |
| Control title | Development Process, Standards, and Tools |
| Parent control | `N/A` |
| Related controls | [RA-9](#ra-9-criticality-analysis) |
| Related enhancements | None |
| What it is | This control addresses development process, standards, and tools for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SA-22 - Unsupported System Components

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SA-22` |
| Control title | Unsupported System Components |
| Parent control | `N/A` |
| Related controls | [PL-2](#pl-2-system-security-and-privacy-plans), [SA-3](#sa-3-system-development-life-cycle) |
| Related enhancements | None |
| What it is | This control addresses unsupported system components for CJIS systems, users, or data. |
| Recommended approach | Build CJIS requirements into procurement, development, and testing. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## System and Communications Protection (SC)

### SC-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-2 - Separation of System and User Functionality

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-2` |
| Control title | Separation of System and User Functionality |
| Parent control | `N/A` |
| Related controls | [AC-6](#ac-6-least-privilege), [SA-4](#sa-4-acquisition-process), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-7](#sc-7-boundary-protection), [SC-22](#sc-22-architecture-and-provisioning-for-nameaddress-resolution-service), [SC-39](#sc-39-process-isolation) |
| Related enhancements | None |
| What it is | This control addresses sc-2 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-4 - Information in Shared System Resources

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-4` |
| Control title | Information in Shared System Resources |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [SA-8](#sa-8-security-and-privacy-engineering-principles) |
| Related enhancements | None |
| What it is | This control addresses information in shared system resources for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-5 - Denial-of-service Protection

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-5` |
| Control title | Denial-of-service Protection |
| Parent control | `N/A` |
| Related controls | [CP-2](#cp-2-contingency-plan), [IR-4](#ir-4-incident-handling), [SC-7](#sc-7-boundary-protection) |
| Related enhancements | None |
| What it is | This control addresses denial-of-service protection for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-7 - Boundary Protection

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-7` |
| Control title | Boundary Protection |
| Parent control | `N/A` |
| Related controls | [AC-4](#ac-4-information-flow-enforcement), [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AC-19](#ac-19-access-control-for-mobile-devices), [AC-20](#ac-20-use-of-external-systems), [CA-3](#ca-3-information-exchange), [CM-2](#cm-2-baseline-configuration), [CM-4](#cm-4-impact-analyses), [CM-7](#cm-7-least-functionality), [CM-10](#cm-10-software-usage-restrictions), [CP-8](#cp-8-telecommunications-services), [CP-10](#cp-10-system-recovery-and-reconstitution), [IR-4](#ir-4-incident-handling), [MA-4](#ma-4-nonlocal-maintenance), [PE-3](#pe-3-physical-access-control), [PL-8](#pl-8-security-and-privacy-architectures), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-5](#sc-5-denial-of-service-protection) |
| Related enhancements | [SC-7(3)](#sc-73-access-points), [SC-7(4)](#sc-74-external-telecommunications-services), [SC-7(5)](#sc-75-deny-by-default-227-allow-by-exception), [SC-7(7)](#sc-77-split-tunneling-for-remote-devices), [SC-7(8)](#sc-78-route-traffic-to-authenticated-proxy-servers), [SC-7(24)](#sc-724-personally-identifiable-information) |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific personally identifiable information requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-7(24)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SC-7(3) - Access Points

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SC-7(3)` |
| Control title | Access Points |
| Parent control | `SC-7` |
| Related controls | See parent control ([SC-7](#sc-7-boundary-protection)) |
| Related enhancements | N/A |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific access points requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-7(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SC-7(4) - External Telecommunications Services

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SC-7(4)` |
| Control title | External Telecommunications Services |
| Parent control | `SC-7` |
| Related controls | See parent control ([SC-7](#sc-7-boundary-protection)) |
| Related enhancements | N/A |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific external telecommunications services requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-7(4)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SC-7(5) - Deny By Default \227 Allow By Exception

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SC-7(5)` |
| Control title | Deny By Default \227 Allow By Exception |
| Parent control | `SC-7` |
| Related controls | See parent control ([SC-7](#sc-7-boundary-protection)) |
| Related enhancements | N/A |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific deny by default \227 allow by exception requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-7(5)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SC-7(7) - Split Tunneling for Remote Devices

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SC-7(7)` |
| Control title | Split Tunneling for Remote Devices |
| Parent control | `SC-7` |
| Related controls | See parent control ([SC-7](#sc-7-boundary-protection)) |
| Related enhancements | N/A |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific split tunneling for remote devices requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-7(7)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SC-7(8) - Route Traffic to Authenticated Proxy Servers

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SC-7(8)` |
| Control title | Route Traffic to Authenticated Proxy Servers |
| Parent control | `SC-7` |
| Related controls | See parent control ([SC-7](#sc-7-boundary-protection)) |
| Related enhancements | N/A |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific route traffic to authenticated proxy servers requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-7(8)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SC-7(24) - Personally Identifiable Information

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SC-7(24)` |
| Control title | Personally Identifiable Information |
| Parent control | `SC-7` |
| Related controls | See parent control ([SC-7](#sc-7-boundary-protection)) |
| Related enhancements | N/A |
| What it is | Enhancement to SC-7 (Boundary Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific personally identifiable information requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-7(24)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-8 - Transmission Confidentiality and Integrity

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-8` |
| Control title | Transmission Confidentiality and Integrity |
| Parent control | `N/A` |
| Related controls | [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [IA-3](#ia-3-device-identification-and-authentication), [IA-8](#ia-8-identification-and-authentication-non-organizational-users), [MA-4](#ma-4-nonlocal-maintenance), [PE-4](#pe-4-access-control-for-transmission), [SA-4](#sa-4-acquisition-process), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-7](#sc-7-boundary-protection), [SC-20](#sc-20-secure-nameaddress-resolution-service-authoritative-source), [SC-23](#sc-23-session-authenticity), [SC-28](#sc-28-protection-of-information-at-rest) |
| Related enhancements | [SC-8(1)](#sc-81-cryptographic-protection) |
| What it is | Enhancement to SC-8 (Transmission Confidentiality and Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-8(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SC-8(1) - Cryptographic Protection

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SC-8(1)` |
| Control title | Cryptographic Protection |
| Parent control | `SC-8` |
| Related controls | See parent control ([SC-8](#sc-8-transmission-confidentiality-and-integrity)) |
| Related enhancements | N/A |
| What it is | Enhancement to SC-8 (Transmission Confidentiality and Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-8(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-10 - Network Disconnect

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-10` |
| Control title | Network Disconnect |
| Parent control | `N/A` |
| Related controls | [AC-17](#ac-17-remote-access), [SC-23](#sc-23-session-authenticity) |
| Related enhancements | None |
| What it is | This control addresses network disconnect for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-12 - Cryptographic Key Establishment and Management

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-12` |
| Control title | Cryptographic Key Establishment and Management |
| Parent control | `N/A` |
| Related controls | [AC-17](#ac-17-remote-access), [AU-9](#au-9-protection-of-audit-information), [CM-3](#cm-3-configuration-change-control), [IA-3](#ia-3-device-identification-and-authentication), [IA-7](#ia-7-cryptographic-module-authenticationf), [SA-4](#sa-4-acquisition-process), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SC-8](#sc-8-transmission-confidentiality-and-integrity), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SC-17](#sc-17-public-key-infrastructure-certificates), [SC-20](#sc-20-secure-nameaddress-resolution-service-authoritative-source), [SI-3](#si-3-malicious-code-protection), [SI-7](#si-7-software-firmware-and-information-integrity) |
| Related enhancements | None |
| What it is | This control addresses cryptographic key establishment and management for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-13 - Cryptographic Protection

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-13` |
| Control title | Cryptographic Protection |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-7](#ac-7-unsuccessful-logon-attempts), [AC-17](#ac-17-remote-access), [AC-18](#ac-18-wireless-access), [AC-19](#ac-19-access-control-for-mobile-devices), [AU-9](#au-9-protection-of-audit-information), [CM-11](#cm-11-user-installed-software), [CP-9](#cp-9-system-backup), [IA-3](#ia-3-device-identification-and-authentication), [IA-5](#ia-5-authenticator-management), [IA-7](#ia-7-cryptographic-module-authenticationf), [MA-4](#ma-4-nonlocal-maintenance), [MP-2](#mp-2-media-access), [MP-4](#mp-4-media-storage), [MP-5](#mp-5-media-transport), [SA-4](#sa-4-acquisition-process), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SC-8](#sc-8-transmission-confidentiality-and-integrity), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-20](#sc-20-secure-nameaddress-resolution-service-authoritative-source), [SC-23](#sc-23-session-authenticity), [SC-28](#sc-28-protection-of-information-at-rest), [SI-3](#si-3-malicious-code-protection), [SI-7](#si-7-software-firmware-and-information-integrity) |
| Related enhancements | None |
| What it is | This control addresses cryptographic protection for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-15 - Collaborative Computing Devices and Applications

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-15` |
| Control title | Collaborative Computing Devices and Applications |
| Parent control | `N/A` |
| Related controls | [AC-21](#ac-21-information-sharing) |
| Related enhancements | None |
| What it is | This control addresses collaborative computing devices and applications for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-17 - Public Key Infrastructure Certificates

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-17` |
| Control title | Public Key Infrastructure Certificates |
| Parent control | `N/A` |
| Related controls | [IA-5](#ia-5-authenticator-management), [SC-12](#sc-12-cryptographic-key-establishment-and-management) |
| Related enhancements | None |
| What it is | This control addresses public key infrastructure certificates for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-18 - Mobile Code

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-18` |
| Control title | Mobile Code |
| Parent control | `N/A` |
| Related controls | [AU-2](#au-2-event-logging), [AU-12](#au-12-audit-record-generation), [CM-2](#cm-2-baseline-configuration), [CM-6](#cm-6-configuration-settings), [SI-3](#si-3-malicious-code-protection) |
| Related enhancements | None |
| What it is | This control addresses mobile code for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-20 - Secure Name/address Resolution Service (Authoritative Source)

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-20` |
| Control title | Secure Name/address Resolution Service (Authoritative Source) |
| Parent control | `N/A` |
| Related controls | [SC-8](#sc-8-transmission-confidentiality-and-integrity), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SC-21](#sc-21-secure-nameaddress-resolution-service-recursive-or-caching-resolver), [SC-22](#sc-22-architecture-and-provisioning-for-nameaddress-resolution-service) |
| Related enhancements | None |
| What it is | This control addresses secure name/address resolution service \(authoritative source\) for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-21 - Secure Name/address Resolution Service (Recursive or Caching Resolver)

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-21` |
| Control title | Secure Name/address Resolution Service (Recursive or Caching Resolver) |
| Parent control | `N/A` |
| Related controls | [SC-20](#sc-20-secure-nameaddress-resolution-service-authoritative-source), [SC-22](#sc-22-architecture-and-provisioning-for-nameaddress-resolution-service) |
| Related enhancements | None |
| What it is | This control addresses secure name/address resolution service \(recursive or caching resolver\) for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-22 - Architecture and Provisioning for Name/address Resolution Service

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-22` |
| Control title | Architecture and Provisioning for Name/address Resolution Service |
| Parent control | `N/A` |
| Related controls | [SC-2](#sc-2-separation-of-system-and-user-functionality), [SC-20](#sc-20-secure-nameaddress-resolution-service-authoritative-source), [SC-21](#sc-21-secure-nameaddress-resolution-service-recursive-or-caching-resolver) |
| Related enhancements | None |
| What it is | This control addresses architecture and provisioning for name/address resolution service for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-23 - Session Authenticity

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SC-23` |
| Control title | Session Authenticity |
| Parent control | `N/A` |
| Related controls | [SC-8](#sc-8-transmission-confidentiality-and-integrity), [SC-10](#sc-10-network-disconnect) |
| Related enhancements | None |
| What it is | This control addresses session authenticity for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-28 - Protection of Information at Rest

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-28` |
| Control title | Protection of Information at Rest |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [AC-6](#ac-6-least-privilege), [AC-19](#ac-19-access-control-for-mobile-devices), [CA-7](#ca-7-continuous-monitoring), [CM-3](#cm-3-configuration-change-control), [CM-5](#cm-5-access-restrictions-for-change), [CM-6](#cm-6-configuration-settings), [CP-9](#cp-9-system-backup), [MP-4](#mp-4-media-storage), [MP-5](#mp-5-media-transport), [PE-3](#pe-3-physical-access-control), [SC-8](#sc-8-transmission-confidentiality-and-integrity), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SI-3](#si-3-malicious-code-protection), [SI-7](#si-7-software-firmware-and-information-integrity), [SI-16](#si-16-memory-protection) |
| Related enhancements | [SC-28(1)](#sc-281-cryptographic-protection) |
| What it is | Enhancement to SC-28 (Protection of Information at Rest) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-28(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SC-28(1) - Cryptographic Protection

Tags: #priority/p2 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SC-28(1)` |
| Control title | Cryptographic Protection |
| Parent control | `SC-28` |
| Related controls | See parent control ([SC-28](#sc-28-protection-of-information-at-rest)) |
| Related enhancements | N/A |
| What it is | Enhancement to SC-28 (Protection of Information at Rest) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific cryptographic protection requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SC-28(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-39 - Process Isolation

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SC-39` |
| Control title | Process Isolation |
| Parent control | `N/A` |
| Related controls | [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [AC-6](#ac-6-least-privilege), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SC-2](#sc-2-separation-of-system-and-user-functionality), [SI-16](#si-16-memory-protection) |
| Related enhancements | None |
| What it is | This control addresses process isolation for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-3 - Sc-3

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SC-3` |
| Control title | Sc-3 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses sc-3 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-43 - Sc-43

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SC-43` |
| Control title | Sc-43 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses sc-43 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-30 - Sc-30

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SC-30` |
| Control title | Sc-30 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses sc-30 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SC-32 - Sc-32

Tags: #priority/unlisted #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SC-32` |
| Control title | Sc-32 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses sc-32 for CJIS systems, users, or data. |
| Recommended approach | Protect traffic, boundaries, and stored data with approved technical controls. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## System and Information Integrity (SI)

### SI-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SI-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-2 - Flaw Remediation

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SI-2` |
| Control title | Flaw Remediation |
| Parent control | `N/A` |
| Related controls | [CA-5](#ca-5-plan-of-action-and-milestones), [CM-3](#cm-3-configuration-change-control), [CM-4](#cm-4-impact-analyses), [CM-5](#cm-5-access-restrictions-for-change), [CM-6](#cm-6-configuration-settings), [CM-8](#cm-8-system-component-inventory), [MA-2](#ma-2-controlled-maintenance), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-10](#sa-10-developer-configuration-management), [SA-11](#sa-11-developer-testing-and-evaluation), [SI-3](#si-3-malicious-code-protection), [SI-5](#si-5-security-alerts-advisories-and-directives), [SI-7](#si-7-software-firmware-and-information-integrity), [SI-11](#si-11-error-handling) |
| Related enhancements | [SI-2(2)](#si-22-automated-flaw-remediation-status) |
| What it is | Enhancement to SI-2 (Flaw Remediation) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated flaw remediation status requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-2(2)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-2(2) - Automated Flaw Remediation Status

Tags: #priority/p1 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-2(2)` |
| Control title | Automated Flaw Remediation Status |
| Parent control | `SI-2` |
| Related controls | See parent control ([SI-2](#si-2-flaw-remediation)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-2 (Flaw Remediation) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated flaw remediation status requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-2(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-3 - Malicious Code Protection

Tags: #priority/p1 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SI-3` |
| Control title | Malicious Code Protection |
| Parent control | `N/A` |
| Related controls | [AC-4](#ac-4-information-flow-enforcement), [AC-19](#ac-19-access-control-for-mobile-devices), [CM-3](#cm-3-configuration-change-control), [CM-8](#cm-8-system-component-inventory), [IR-4](#ir-4-incident-handling), [MA-3](#ma-3-maintenance-tools), [MA-4](#ma-4-nonlocal-maintenance), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SC-7](#sc-7-boundary-protection), [SC-23](#sc-23-session-authenticity), [SC-28](#sc-28-protection-of-information-at-rest), [SI-2](#si-2-flaw-remediation), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity), [SI-8](#si-8-spam-protection) |
| Related enhancements | None |
| What it is | This control addresses malicious code protection for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-4 - System Monitoring

Tags: #priority/p1 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SI-4` |
| Control title | System Monitoring |
| Parent control | `N/A` |
| Related controls | [AC-2](#ac-2-account-management), [AC-3](#ac-3-access-enforcement), [AC-4](#ac-4-information-flow-enforcement), [AC-8](#ac-8-system-use-notification), [AC-17](#ac-17-remote-access), [AU-2](#au-2-event-logging), [AU-6](#au-6-audit-record-review-analysis-and-reporting), [AU-7](#au-7-audit-record-reduction-and-report-generation), [AU-9](#au-9-protection-of-audit-information), [AU-12](#au-12-audit-record-generation), [CA-7](#ca-7-continuous-monitoring), [CM-3](#cm-3-configuration-change-control), [CM-6](#cm-6-configuration-settings), [CM-8](#cm-8-system-component-inventory), [CM-11](#cm-11-user-installed-software), [IR-4](#ir-4-incident-handling), [MA-3](#ma-3-maintenance-tools), [MA-4](#ma-4-nonlocal-maintenance), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SC-5](#sc-5-denial-of-service-protection), [SC-7](#sc-7-boundary-protection), [SC-18](#sc-18-mobile-code), [SI-3](#si-3-malicious-code-protection), [SI-7](#si-7-software-firmware-and-information-integrity), [SR-10](#sr-10-inspection-of-systems-or-components) |
| Related enhancements | [SI-4(2)](#si-42-automated-tools-and-mechanisms-for-real-time-analysis), [SI-4(4)](#si-44-inbound-and-outbound-communications-traffic), [SI-4(5)](#si-45-system-generated-alerts) |
| What it is | Enhancement to SI-4 (System Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific system-generated alerts requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-4(5)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-4(2) - Automated Tools and Mechanisms for Real-time Analysis

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-4(2)` |
| Control title | Automated Tools and Mechanisms for Real-time Analysis |
| Parent control | `SI-4` |
| Related controls | See parent control ([SI-4](#si-4-system-monitoring)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-4 (System Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automated tools and mechanisms for real-time analysis requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-4(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-4(4) - Inbound and Outbound Communications Traffic

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-4(4)` |
| Control title | Inbound and Outbound Communications Traffic |
| Parent control | `SI-4` |
| Related controls | See parent control ([SI-4](#si-4-system-monitoring)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-4 (System Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific inbound and outbound communications traffic requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-4(4)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-4(5) - System-generated Alerts

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-4(5)` |
| Control title | System-generated Alerts |
| Parent control | `SI-4` |
| Related controls | See parent control ([SI-4](#si-4-system-monitoring)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-4 (System Monitoring) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific system-generated alerts requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-4(5)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-5 - Security Alerts, Advisories, and Directives

Tags: #priority/p2 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SI-5` |
| Control title | Security Alerts, Advisories, and Directives |
| Parent control | `N/A` |
| Related controls | [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SI-2](#si-2-flaw-remediation) |
| Related enhancements | None |
| What it is | This control addresses security alerts, advisories, and directives for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-7 - Software, Firmware, and Information Integrity

Tags: #priority/p1 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SI-7` |
| Control title | Software, Firmware, and Information Integrity |
| Parent control | `N/A` |
| Related controls | [AC-4](#ac-4-information-flow-enforcement), [CM-3](#cm-3-configuration-change-control), [CM-7](#cm-7-least-functionality), [CM-8](#cm-8-system-component-inventory), [MA-3](#ma-3-maintenance-tools), [MA-4](#ma-4-nonlocal-maintenance), [RA-5](#ra-5-vulnerability-monitoring-and-scanning), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SA-10](#sa-10-developer-configuration-management), [SC-8](#sc-8-transmission-confidentiality-and-integrity), [SC-12](#sc-12-cryptographic-key-establishment-and-management), [SC-13](#sc-13-cryptographic-protection), [SC-28](#sc-28-protection-of-information-at-rest), [SI-3](#si-3-malicious-code-protection), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-5](#sr-5-acquisition-strategies-tools-and-methods), [SR-6](#sr-6-supplier-assessments-and-reviews), [SR-10](#sr-10-inspection-of-systems-or-components), [SR-11](#sr-11-sr-11) |
| Related enhancements | [SI-7(1)](#si-71-integrity-checks), [SI-7(7)](#si-77-integration-of-detection-and-response) |
| What it is | Enhancement to SI-7 (Software, Firmware, and Information Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific integration of detection and response requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-7(7)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-7(1) - Integrity Checks

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-7(1)` |
| Control title | Integrity Checks |
| Parent control | `SI-7` |
| Related controls | See parent control ([SI-7](#si-7-software-firmware-and-information-integrity)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-7 (Software, Firmware, and Information Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific integrity checks requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-7(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-7(7) - Integration of Detection and Response

Tags: #priority/p1 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-7(7)` |
| Control title | Integration of Detection and Response |
| Parent control | `SI-7` |
| Related controls | See parent control ([SI-7](#si-7-software-firmware-and-information-integrity)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-7 (Software, Firmware, and Information Integrity) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific integration of detection and response requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-7(7)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-8 - Spam Protection

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SI-8` |
| Control title | Spam Protection |
| Parent control | `N/A` |
| Related controls | [SC-5](#sc-5-denial-of-service-protection), [SC-7](#sc-7-boundary-protection), [SI-3](#si-3-malicious-code-protection), [SI-4](#si-4-system-monitoring) |
| Related enhancements | [SI-8(2)](#si-82-automatic-updates) |
| What it is | Enhancement to SI-8 (Spam Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automatic updates requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-8(2)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-8(2) - Automatic Updates

Tags: #priority/p3 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-8(2)` |
| Control title | Automatic Updates |
| Parent control | `SI-8` |
| Related controls | See parent control ([SI-8](#si-8-spam-protection)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-8 (Spam Protection) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific automatic updates requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-8(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-10 - Information Input Validation

Tags: #priority/p1 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SI-10` |
| Control title | Information Input Validation |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses information input validation for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-11 - Error Handling

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SI-11` |
| Control title | Error Handling |
| Parent control | `N/A` |
| Related controls | [AU-2](#au-2-event-logging), [AU-3](#au-3-content-of-audit-records), [SI-2](#si-2-flaw-remediation) |
| Related enhancements | None |
| What it is | This control addresses error handling for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-12 - Information Management and Retention

Tags: #priority/p3 #existing/yes

| Field | Value |
| --- | --- |
| Control code | `SI-12` |
| Control title | Information Management and Retention |
| Parent control | `N/A` |
| Related controls | [AU-5](#au-5-response-to-audit-logging-process-failures), [AU-11](#au-11-audit-record-retention), [CA-2](#ca-2-control-assessments), [CA-3](#ca-3-information-exchange), [CA-5](#ca-5-plan-of-action-and-milestones), [CA-6](#ca-6-authorization), [CA-7](#ca-7-continuous-monitoring), [CA-9](#ca-9-internal-system-connections), [CM-5](#cm-5-access-restrictions-for-change), [CM-9](#cm-9-configuration-management-plan), [CP-2](#cp-2-contingency-plan), [IR-8](#ir-8-incident-response-plan), [MP-2](#mp-2-media-access), [MP-3](#mp-3-media-marking), [MP-4](#mp-4-media-storage), [MP-6](#mp-6-media-sanitization), [PL-2](#pl-2-system-security-and-privacy-plans), [PL-4](#pl-4-rules-of-behavior), [PS-2](#ps-2-position-risk-designation), [PS-6](#ps-6-access-agreements), [RA-2](#ra-2-security-categorization), [RA-3](#ra-3-risk-assessment), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SR-2](#sr-2-supply-chain-risk-management-plan) |
| Related enhancements | [SI-12(1)](#si-121-limit-personally-identifiable-information-elements), [SI-12(2)](#si-122-minimize-personally-identifiable-information-in-testing-training-and-research), [SI-12(3)](#si-123-information-disposal) |
| What it is | Enhancement to SI-12 (Information Management and Retention) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific information disposal requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-12(3)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-12(1) - Limit Personally Identifiable Information Elements

Tags: #priority/p3 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-12(1)` |
| Control title | Limit Personally Identifiable Information Elements |
| Parent control | `SI-12` |
| Related controls | See parent control ([SI-12](#si-12-information-management-and-retention)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-12 (Information Management and Retention) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific limit personally identifiable information elements requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-12(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-12(2) - Minimize Personally Identifiable Information in Testing, Training, and Research

Tags: #priority/p3 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-12(2)` |
| Control title | Minimize Personally Identifiable Information in Testing, Training, and Research |
| Parent control | `SI-12` |
| Related controls | See parent control ([SI-12](#si-12-information-management-and-retention)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-12 (Information Management and Retention) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific minimize personally identifiable information in testing, training, and research requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-12(2)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SI-12(3) - Information Disposal

Tags: #priority/p3 #existing/yes #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SI-12(3)` |
| Control title | Information Disposal |
| Parent control | `SI-12` |
| Related controls | See parent control ([SI-12](#si-12-information-management-and-retention)) |
| Related enhancements | N/A |
| What it is | Enhancement to SI-12 (Information Management and Retention) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific information disposal requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SI-12(3)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-16 - Memory Protection

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SI-16` |
| Control title | Memory Protection |
| Parent control | `N/A` |
| Related controls | [SI-7](#si-7-software-firmware-and-information-integrity) |
| Related enhancements | None |
| What it is | This control addresses si-16 for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-18 - Si-18

Tags: #priority/p4 #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SI-18` |
| Control title | Si-18 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses si-18 for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SI-19 - De-identification

Tags: #priority/p4 #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SI-19` |
| Control title | De-identification |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses si-19 for CJIS systems, users, or data. |
| Recommended approach | Patch quickly and monitor for malicious or unexpected activity. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

## Supply Chain Risk Management (SR)

### SR-1 - Policy and Procedures

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SR-1` |
| Control title | Policy and Procedures |
| Parent control | `N/A` |
| Related controls | [PS-8](#ps-8-personnel-sanctions), [SI-12](#si-12-information-management-and-retention) |
| Related enhancements | None |
| What it is | This control addresses policy and procedures for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SR-2 - Supply Chain Risk Management Plan

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SR-2` |
| Control title | Supply Chain Risk Management Plan |
| Parent control | `N/A` |
| Related controls | [CA-2](#ca-2-control-assessments), [CP-4](#cp-4-contingency-plan-testing), [IR-4](#ir-4-incident-handling), [MA-2](#ma-2-controlled-maintenance), [MA-6](#ma-6-timely-maintenance), [PE-16](#pe-16-delivery-and-removal), [PL-2](#pl-2-system-security-and-privacy-plans), [RA-3](#ra-3-risk-assessment), [RA-7](#ra-7-risk-response), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SI-4](#si-4-system-monitoring) |
| Related enhancements | [SR-2(1)](#sr-21-establish-scrm-team) |
| What it is | Enhancement to SR-2 (Supply Chain Risk Management Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific establish scrm team requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SR-2(1)`. |
| Review frequency | Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

#### SR-2(1) - Establish SCRM Team

Tags: #priority/p3 #existing/no #enhancement/yes

| Field | Value |
| --- | --- |
| Control code | `SR-2(1)` |
| Control title | Establish SCRM Team |
| Parent control | `SR-2` |
| Related controls | See parent control ([SR-2](#sr-2-supply-chain-risk-management-plan)) |
| Related enhancements | N/A |
| What it is | Enhancement to SR-2 (Supply Chain Risk Management Plan) that strengthens, automates, or narrows the base requirement. |
| Recommended approach | Implement this enhancement after the base control is stable. Apply the specific establish scrm team requirement and verify it through testing, review, or monitoring. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | Proof of enhancement configuration, test result, or review evidence tied to `SR-2(1)`. |
| Review frequency | Align with the parent control cadence: Align with the parent control cadence: `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SR-5 - Acquisition Strategies, Tools, and Methods

Tags: #priority/p2 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SR-5` |
| Control title | Acquisition Strategies, Tools, and Methods |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [SA-2](#sa-2-allocation-of-resources), [SA-3](#sa-3-system-development-life-cycle), [SA-4](#sa-4-acquisition-process), [SA-5](#sa-5-system-documentation), [SA-8](#sa-8-security-and-privacy-engineering-principles), [SA-9](#sa-9-external-system-services), [SA-10](#sa-10-developer-configuration-management), [SA-15](#sa-15-development-process-standards-and-tools), [SR-6](#sr-6-supplier-assessments-and-reviews), [SR-10](#sr-10-inspection-of-systems-or-components), [SR-11](#sr-11-sr-11) |
| Related enhancements | None |
| What it is | This control addresses acquisition strategies, tools, and methods for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SR-8 - Notification Agreements

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SR-8` |
| Control title | Notification Agreements |
| Parent control | `N/A` |
| Related controls | [IR-4](#ir-4-incident-handling), [IR-6](#ir-6-incident-reporting), [IR-8](#ir-8-incident-response-plan) |
| Related enhancements | None |
| What it is | This control addresses notification agreements for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SR-10 - Inspection of Systems or Components

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SR-10` |
| Control title | Inspection of Systems or Components |
| Parent control | `N/A` |
| Related controls | [AT-3](#at-3-role-based-training), [SI-4](#si-4-system-monitoring), [SI-7](#si-7-software-firmware-and-information-integrity), [SR-3](#sr-3-supply-chain-controls-and-processes), [SR-5](#sr-5-acquisition-strategies-tools-and-methods), [SR-11](#sr-11-sr-11) |
| Related enhancements | None |
| What it is | This control addresses inspection of systems or components for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SR-12 - Component Disposal

Tags: #priority/p3 #existing/no

| Field | Value |
| --- | --- |
| Control code | `SR-12` |
| Control title | Component Disposal |
| Parent control | `N/A` |
| Related controls | [MP-6](#mp-6-media-sanitization) |
| Related enhancements | None |
| What it is | This control addresses component disposal for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SR-3 - Supply Chain Controls and Processes

Tags: #priority/p3 #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SR-3` |
| Control title | Supply Chain Controls and Processes |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses sr-3 for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SR-6 - Supplier Assessments and Reviews

Tags: #priority/p2 #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SR-6` |
| Control title | Supplier Assessments and Reviews |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses sr-6 for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |

### SR-11 - Sr-11

Tags: #priority/p2 #existing/unlisted

| Field | Value |
| --- | --- |
| Control code | `SR-11` |
| Control title | Sr-11 |
| Parent control | `N/A` |
| Related controls | None |
| Related enhancements | None |
| What it is | This control addresses sr-11 for CJIS systems, users, or data. |
| Recommended approach | Vet vendors and track component risk throughout the lifecycle. |
| Owner | `[[CONTROL_OWNER]]` |
| Implementation notes | `[[IMPLEMENTATION_NOTES]]` |
| Evidence artifacts | `[[EVIDENCE_ARTIFACTS]]` |
| Review frequency | `[[REVIEW_FREQUENCY]]` |
| Risk level | `[[RISK_LEVEL]]` |
| Exception reference | `[[EXCEPTION_REFERENCE]]` |
| Control notes | `[[CONTROL_NOTES]]` |
