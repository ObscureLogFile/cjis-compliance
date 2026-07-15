<a id="control-mp-5"></a>
# MP-5 — Media Transport

**Control family:** Media Protection (MP)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-MP-5` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Monthly inventory; per disposal event |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **MP-5 — Media Transport** for systems, personnel, services, and data within the CJIS scope.

This control addresses media transport for CJIS systems, users, or data.

**Implementation objective:** Track media from creation through disposal.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **MP-5** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

**Procedure**

1. Classify and label media based on the CJIS content it contains.
2. Store and transport the media using approved chain-of-custody controls.
3. Track use, movement, and storage in a log or inventory.
4. Sanitize or destroy media when it is no longer needed and retain proof.
5. Record the result, evidence location, reviewer, date, and any exception or remediation reference.
6. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.

**Workflow output**

An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.

## Organizational action items

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for MP-5.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by MP-5.
- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.
- [ ] Record the current implementation state, gap, risk level, and target completion date.
- [ ] Test the control and attach the result to the evidence repository.
- [ ] Schedule the recurring review and assign an accountable reviewer.
- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.

## Audit evidence and continuous compliance artifacts

**Expected evidence:** Media inventory, checkout log, destruction certificate.

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

- **Source title:** MEDIA TRANSPORT
- **Source marking:** `[Existing] [Priority 2]`

**Control**

> a. Protect and control digital and non-digital media to help prevent compromise of the data during transport outside of the physically secure locations or controlled areas using encryption, as defined in SC-13 and SC-28 of this Policy. Physical media will be protected at the same level as the information would be protected in electronic form. Restrict the activities associated with transport of electronic and physical media to authorized personnel; b. Maintain accountability for system media during transport outside of the physically secure location or controlled areas; c. Document activities associated with the transport of system media; and d. Restrict the activities associated with the transport of system media to authorized personnel.

**Discussion**

> System media includes digital and non-digital media. Digital media includes flash drives, diskettes, magnetic tapes, external or removable hard disk drives (e.g., solid state and magnetic), compact discs, and digital versatile discs. Non-digital media includes microfilm and paper. Controlled areas are spaces for which agencies provide physical or procedural controls to meet requirements established for protecting information and systems. Controls to protect media during transport include cryptography and locked containers. Cryptographic mechanisms can provide confidentiality and integrity protections depending on the mechanisms implemented. Activities associated with media transport include releasing media for transport, ensuring that media enters the appropriate transport processes, and the actual transport. Authorized transport and courier personnel may include individuals external to the agency. Maintaining accountability of media during transport includes restricting transport activities to authorized personnel and tracking and/or obtaining records of transport activities as the media moves through the transportation system to prevent and detect loss, destruction, or tampering. Agencies establish documentation requirements for activities associated with the transport of system media in accordance with agency assessments of risk. Agencies maintain the flexibility to define record-keeping methods for the different types of media transport as part of a system of transport-related records.

**Related Controls in the source**

> AC-7, AC-19, CP-2, CP-9, MP-3, MP-4, PE-16, PL-2, SC-12, SC-13, SC-28.

## Related controls

[AC-7](../control_documents/AC-7.md), [AC-19](../control_documents/AC-19.md), [CP-2](../control_documents/CP-2.md), [CP-9](../control_documents/CP-9.md), [MP-3](../control_documents/MP-3.md), [MP-4](../control_documents/MP-4.md), [PE-16](../control_documents/PE-16.md), [PL-2](../control_documents/PL-2.md), [SC-12](../control_documents/SC-12.md), [SC-13](../control_documents/SC-13.md), [SC-28](../control_documents/SC-28.md)

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
