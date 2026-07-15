<a id="control-ac-2"></a>
# AC-2 — Account Management

**Control family:** Access Control (AC)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-AC-2` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Quarterly or [[ACCESS_REVIEW_INTERVAL_DAYS]] days |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **AC-2 — Account Management** for systems, personnel, services, and data within the CJIS scope.

Enhancement to AC-2 (Account Management) that strengthens, automates, or narrows the base requirement.

**Implementation objective:** Implement this enhancement after the base control is stable. Apply the specific disable accounts for high-risk individuals requirement and verify it through testing, review, or monitoring.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **AC-2** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

**Procedure**

1. Identify the person, role, or system that needs access.
2. Obtain documented approval for the least privilege needed.
3. Provision the account, permissions, and MFA or other required controls.
4. Verify access works as intended and remove any extra privileges.
5. Record the result, evidence location, reviewer, date, and any exception or remediation reference.
6. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.

**Workflow output**

An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.

## Organizational action items

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for AC-2.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by AC-2.
- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.
- [ ] Record the current implementation state, gap, risk level, and target completion date.
- [ ] Test the control and attach the result to the evidence repository.
- [ ] Schedule the recurring review and assign an accountable reviewer.
- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.

## Audit evidence and continuous compliance artifacts

**Expected evidence:** Access request forms, approvals, MFA status, access review report.

Maintain, as applicable:

- Current policy, procedure, standard, or system security plan section.
- Owner approval, implementation ticket, configuration export, or signed operational record.
- Test, inspection, review, training, log, or monitoring evidence showing the control operated.
- Recurring review sign-off with sample period, reviewer, date, result, and follow-up.
- Exception, compensating-control, POA&M, incident, or risk-acceptance record.
- Evidence retention location: `[[EVIDENCE_REPOSITORY_URL]]`; retain according to agency records requirements.

**Continuous compliance measures**

- Control status: Implemented / Partially implemented / Planned / Not applicable.
- Evidence freshness: last collected date, next due date, and overdue indicator.
- Exceptions: open count, aging, owner, target date, and residual risk.
- Review result: pass, pass with findings, or fail, with a linked corrective action.

## Original CJIS 6.0 control information (reference)

**Reference source:** [FBI CJIS Security Policy v6.0 (12/27/2024)](../CJIS_Security_Policy_v6-0_20241227%20(1)-1.pdf), using the supplied local text extract for search and drafting. This section is a reference and does not replace the official policy or state CJIS authority direction.

- **Source title:** ACCOUNT MANAGEMENT
- **Source marking:** `[Existing] [Priority 1]`

**Control**

> a. Define and document the types of accounts allowed and specifically prohibited for use within the system; b. Assign account managers; c. Require conditions for group and role membership; d. Specify: 1. Authorized users of the system; 2. Group and role membership; and 3. Access authorizations (i.e., privileges) and attributes listed for each account; Attribute Name Email Address Text Employer Name Federation Id Given Name Identity Provider Id Sur Name Telephone Number Identity Provider Id Unique Subject Id Counter Terrorism Data Self Search Home Privilege Indicator Criminal History Data Self Search Home Privilege Indicator Criminal Intelligence Data Self Search Home Privilege Indicator Criminal Investigative Data Self Search Home Privilege Indicator Display Name Government Data Self Search Home Privilege Indicator Local Id NCIC Certification Indicator N-DEx Privilege Indicator PCII Certification Indicator 28 CFR Certification Indicator Employer ORI Employer Organization General Category Code Employer State Code Public Safety Officer Indicator Sworn Law Enforcement Officer Indicator Authenticator Assurance Level Federation Assurance Level Identity Assurance Level Intelligence Analyst Indicator e. Require approvals by organizational personnel with account management responsibilities for requests to create accounts; f. Create, enable, modify, disable, and remove accounts in accordance with agency policy; g. Monitor the use of accounts; h. Notify account managers and system/network administrators within: 1. One day when accounts are no longer required; 2. One day when users are terminated or transferred; and 3. One day when system usage or need-to-know changes for an individual; i. Authorize access to the system based on: 1. A valid access authorization; 2. Intended system usage; and 3. Attributes as listed in AC-2(d)(3); j. Review accounts for compliance with account management requirements at least annually; k. Establish and implement a process for changing shared or group account authenticators (if deployed) when individuals are removed from the group; and l. Align account management processes with personnel termination and transfer processes.

**Discussion**

> Examples of system account types include individual, shared, group, system, guest, anonymous, emergency, developer, temporary, and service. Identification of authorized system users and the specification of access privileges reflect the requirements in other controls in the security plan. Users requiring administrative privileges on system accounts receive additional scrutiny by organizational personnel responsible for approving such accounts and privileged access, including system owner, mission or business owner, senior agency information security officer, or senior agency official for privacy. Types of accounts that organizations may wish to prohibit due to increased risk include shared, group, emergency, anonymous, temporary, and guest accounts. Where access involves personally identifiable information, security programs collaborate with the senior agency official for privacy to establish the specific conditions for group and role membership; specify authorized users, group and role membership, and access authorizations for each account; and create, adjust, or remove system accounts in accordance with organizational policies. Policies can include such information as account expiration dates or other factors that trigger the disabling of accounts. Organizations may choose to define access privileges or other attributes by account, type of account, or a combination of the two. Examples of other attributes required for authorizing access include restrictions on time of day, day of week, and point of origin. In defining other system account attributes, organizations consider system-related requirements and mission/business requirements. Failure to consider these factors could affect system availability. Temporary and emergency accounts are intended for short-term use. Organizations establish temporary accounts as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. Organizations establish emergency accounts in response to crisis situations and with the need for rapid account activation. Therefore, emergency account activation may bypass normal account authorization processes. Emergency and temporary accounts are not to be confused with infrequently used accounts, including local logon accounts used for special tasks or when network resources are unavailable (may also be known as accounts of last resort). Such accounts remain available and are not subject to automatic disabling or removal dates. Conditions for disabling or deactivating accounts include when shared/group, emergency, or temporary accounts are no longer required and when individuals are transferred or terminated. Changing shared/group authenticators when members leave the group is intended to ensure that former group members do not retain access to the shared or group account. Some types of system accounts may require specialized training.

**Related Controls in the source**

> AC-3, AC-5, AC-6, AC-17, AC-18, AC-20, AU-2, AU-12, CM-5, IA-2, IA-4, IA-5, IA-8, MA-3, MA-5, PE-2, PL-4, PS-2, PS-4, PS-5, SC-7, SC-12, SC-13.

## Related controls

[AC-3](../control_documents/AC-3.md), [AC-5](../control_documents/AC-5.md), [AC-6](../control_documents/AC-6.md), [AC-17](../control_documents/AC-17.md), [AC-18](../control_documents/AC-18.md), [AC-20](../control_documents/AC-20.md), [AU-2](../control_documents/AU-2.md), [AU-12](../control_documents/AU-12.md), [CM-5](../control_documents/CM-5.md), [IA-2](../control_documents/IA-2.md), [IA-4](../control_documents/IA-4.md), [IA-5](../control_documents/IA-5.md), [IA-8](../control_documents/IA-8.md), [MA-3](../control_documents/MA-3.md), [MA-5](../control_documents/MA-5.md), [PE-2](../control_documents/PE-2.md), [PL-4](../control_documents/PL-4.md), [PS-2](../control_documents/PS-2.md), [PS-4](../control_documents/PS-4.md), [PS-5](../control_documents/PS-5.md), [SC-7](../control_documents/SC-7.md), [SC-12](../control_documents/SC-12.md), [SC-13](../control_documents/SC-13.md)

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
