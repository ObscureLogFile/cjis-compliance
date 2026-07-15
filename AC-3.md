<a id="control-ac-3"></a>
# AC-3 — Access Enforcement

**Control family:** Access Control (AC)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-AC-3` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Quarterly or [[ACCESS_REVIEW_INTERVAL_DAYS]] days |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **AC-3 — Access Enforcement** for systems, personnel, services, and data within the CJIS scope.

This control addresses access enforcement for CJIS systems, users, or data.

**Implementation objective:** Use centralized identity and access management, unique user accounts, and periodic reviews.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **AC-3** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

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

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for AC-3.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by AC-3.
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

- **Source title:** ACCESS ENFORCEMENT
- **Source marking:** `[Existing] [Priority 1]`

**Control**

> Enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Discussion**

> Access control policies control access between active entities or subjects (i.e., users or processes acting on behalf of users) and passive entities or objects (i.e., devices, files, records, domains) in organizational systems. In addition to enforcing authorized access at the system level and recognizing that systems can host many applications and services in support of mission and business functions, access enforcement mechanisms can also be employed at the application and service level to provide increased information security and privacy. In contrast to logical access controls that are implemented within the system, physical access controls are addressed by the controls in the Physical and Environmental Protection (PE) family.

**Related Controls in the source**

> AC-2, AC-4, AC-5, AC-6, AC-17, AC-18, AC-19, AC-20, AC-21, AC-22, AT-2, AT-3, AU-9, CA-9, CM-5, CM-11, IA-2, IA-5, IA-6, IA-7, IA-11, MA-3, MA-4, MA-5, MP-4, PS-3, SC-2, SC-4, SC-12, SC-13, SC-28, SI-4, SI-8.

## Related controls

[AC-2](../control_documents/AC-2.md), [AC-4](../control_documents/AC-4.md), [AC-5](../control_documents/AC-5.md), [AC-6](../control_documents/AC-6.md), [AC-17](../control_documents/AC-17.md), [AC-18](../control_documents/AC-18.md), [AC-19](../control_documents/AC-19.md), [AC-20](../control_documents/AC-20.md), [AC-21](../control_documents/AC-21.md), [AC-22](../control_documents/AC-22.md), [AT-2](../control_documents/AT-2.md), [AT-3](../control_documents/AT-3.md), [AU-9](../control_documents/AU-9.md), [CA-9](../control_documents/CA-9.md), [CM-5](../control_documents/CM-5.md), [CM-11](../control_documents/CM-11.md), [IA-2](../control_documents/IA-2.md), [IA-5](../control_documents/IA-5.md), [IA-6](../control_documents/IA-6.md), [IA-7](../control_documents/IA-7.md), [IA-11](../control_documents/IA-11.md), [MA-3](../control_documents/MA-3.md), [MA-4](../control_documents/MA-4.md), [MA-5](../control_documents/MA-5.md), [MP-4](../control_documents/MP-4.md), [PS-3](../control_documents/PS-3.md), [SC-2](../control_documents/SC-2.md), [SC-4](../control_documents/SC-4.md), [SC-12](../control_documents/SC-12.md), [SC-13](../control_documents/SC-13.md), [SC-28](../control_documents/SC-28.md), [SI-4](../control_documents/SI-4.md), [SI-8](../control_documents/SI-8.md)

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
