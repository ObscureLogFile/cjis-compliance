<a id="control-ma-4"></a>
# MA-4 — Nonlocal Maintenance

**Control family:** Maintenance (MA)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-MA-4` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Each maintenance event; annual review |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **MA-4 — Nonlocal Maintenance** for systems, personnel, services, and data within the CJIS scope.

This control addresses ma-4 for CJIS systems, users, or data.

**Implementation objective:** Approve maintenance work, log it, and limit access to the minimum necessary.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **MA-4** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

**Procedure**

1. Approve maintenance work before it starts and define the scope.
2. Monitor or escort the activity as required and log the session.
3. Verify the system is stable and secure before it returns to service.
4. Retain the maintenance record and follow up on open issues.
5. Record the result, evidence location, reviewer, date, and any exception or remediation reference.
6. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.

**Workflow output**

An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.

## Organizational action items

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for MA-4.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by MA-4.
- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.
- [ ] Record the current implementation state, gap, risk level, and target completion date.
- [ ] Test the control and attach the result to the evidence repository.
- [ ] Schedule the recurring review and assign an accountable reviewer.
- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.

## Audit evidence and continuous compliance artifacts

**Expected evidence:** Maintenance log, vendor approval, escort record, return-to-service note.

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

- **Source title:** NONLOCAL MAINTENANCE
- **Source marking:** `[Priority 3]`

**Control**

> a. Approve and monitor nonlocal maintenance and diagnostic activities; b. Allow the use of nonlocal maintenance and diagnostic tools only as consistent with organizational policy and documented in the security plan for the system; c. Employ strong authentication in the establishment of nonlocal maintenance and diagnostic sessions; d. Maintain records for nonlocal maintenance and diagnostic activities; and e. Terminate session and network connections when nonlocal maintenance is completed.

**Discussion**

> Nonlocal maintenance and diagnostic activities are conducted by individuals who communicate through either an external or internal network. Local maintenance and diagnostic activities are carried out by individuals who are physically present at the system location and not communicating across a network connection. Authentication techniques used to establish nonlocal maintenance and diagnostic sessions reflect the network access requirements in IA-2. Strong authentication requires authenticators that are resistant to replay attacks and employ multi-factor authentication. Strong authenticators include PKI where certificates are stored on a token protected by a password, passphrase, or biometric. Enforcing requirements in MA-4 is accomplished, in part, by other controls.

**Related Controls in the source**

> AC-2, AC-3, AC-6, AC-17, AU-2, AU-3, IA-2, IA-4, IA-5, IA-8, MA-2, MA-5, PL-2, SC-7, SC-10.

## Related controls

[AC-2](../control_documents/AC-2.md), [AC-3](../control_documents/AC-3.md), [AC-6](../control_documents/AC-6.md), [AC-17](../control_documents/AC-17.md), [AU-2](../control_documents/AU-2.md), [AU-3](../control_documents/AU-3.md), [IA-2](../control_documents/IA-2.md), [IA-4](../control_documents/IA-4.md), [IA-5](../control_documents/IA-5.md), [IA-8](../control_documents/IA-8.md), [MA-2](../control_documents/MA-2.md), [MA-5](../control_documents/MA-5.md), [PL-2](../control_documents/PL-2.md), [SC-7](../control_documents/SC-7.md), [SC-10](../control_documents/SC-10.md)

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
