<a id="control-pe-4"></a>
# PE-4 — Access Control for Transmission

**Control family:** Physical and Environmental Protection (PE)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-PE-4` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Quarterly and after facility changes |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **PE-4 — Access Control for Transmission** for systems, personnel, services, and data within the CJIS scope.

This control addresses access control for transmission for CJIS systems, users, or data.

**Implementation objective:** Use layered physical safeguards appropriate to the site.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **PE-4** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

**Procedure**

1. Restrict access to approved physical spaces and devices.
2. Maintain monitoring, visitor control, and environmental safeguards.
3. Inspect doors, badges, cameras, power, and cabling on schedule.
4. Document exceptions, maintenance, and corrective actions.
5. Record the result, evidence location, reviewer, date, and any exception or remediation reference.
6. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.

**Workflow output**

An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.

## Organizational action items

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for PE-4.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by PE-4.
- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.
- [ ] Record the current implementation state, gap, risk level, and target completion date.
- [ ] Test the control and attach the result to the evidence repository.
- [ ] Schedule the recurring review and assign an accountable reviewer.
- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.

## Audit evidence and continuous compliance artifacts

**Expected evidence:** Badge report, visitor log, inspection checklist, camera log.

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

- **Source title:** ACCESS CONTROL FOR TRANSMISSION
- **Source marking:** `[Existing] [Priority 2]`

**Control**

> Control physical access to information system distribution and transmission lines and devices within organizational facilities using agency-implemented procedures and controls.

**Discussion**

> Security controls applied to system distribution and transmission lines prevent accidental damage, disruption, and physical tampering. Such controls may also be necessary to prevent eavesdropping or modification of unencrypted transmissions. Security controls used to control physical access to system distribution and transmission lines include disconnected or locked spare jacks, locked wiring closets, protection of cabling by conduit or cable trays, and wiretapping sensors.

**Related Controls in the source**

> AT-3, IA-4, MP-2, MP-4, PE-2, PE-3, PE-5, PE-9, SC-7, SC-8.

## Related controls

[AT-3](../control_documents/AT-3.md), [IA-4](../control_documents/IA-4.md), [MP-2](../control_documents/MP-2.md), [MP-4](../control_documents/MP-4.md), [PE-2](../control_documents/PE-2.md), [PE-3](../control_documents/PE-3.md), [PE-5](../control_documents/PE-5.md), [PE-9](../control_documents/PE-9.md), [SC-7](../control_documents/SC-7.md), [SC-8](../control_documents/SC-8.md)

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
