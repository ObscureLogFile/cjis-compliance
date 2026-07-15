<a id="control-ca-7"></a>
# CA-7 — Continuous Monitoring

**Control family:** Assessment, Authorization, and Monitoring (CA)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-CA-7` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Before go-live and annual review |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **CA-7 — Continuous Monitoring** for systems, personnel, services, and data within the CJIS scope.

Enhancement to CA-7 (Continuous Monitoring) that strengthens, automates, or narrows the base requirement.

**Implementation objective:** Implement this enhancement after the base control is stable. Apply the specific risk monitoring requirement and verify it through testing, review, or monitoring.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **CA-7** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

**Procedure**

1. Assess the control design and operating effectiveness before production use.
2. Document findings, remediation actions, and the approval decision.
3. Monitor the control on a recurring basis and after major changes.
4. Update the authorization record if risk or scope changes materially.
5. Record the result, evidence location, reviewer, date, and any exception or remediation reference.
6. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.

**Workflow output**

An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.

## Organizational action items

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for CA-7.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by CA-7.
- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.
- [ ] Record the current implementation state, gap, risk level, and target completion date.
- [ ] Test the control and attach the result to the evidence repository.
- [ ] Schedule the recurring review and assign an accountable reviewer.
- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.

## Audit evidence and continuous compliance artifacts

**Expected evidence:** Assessment report, POA&M, authorization memo, monitoring dashboard.

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

- **Source title:** CONTINUOUS MONITORING
- **Source marking:** `[Priority 1]`

**Control**

> Develop a system-level continuous monitoring strategy and implement continuous monitoring in accordance with the organization-level continuous monitoring strategy that includes: a. Establishing the following system-level metrics to be monitored: 1. AC-2(g) Account Management 2. AC-17(1) Remote Access | Monitoring and Control 3. AT-4(a) Training Records 4. CM-3(f) Configuration Change Control 5. CM-6(d) Configuration Settings 6. CM-11(c) User-Installed Software 7. IR-5 Incident Monitoring 8. MA-2(b) Controlled Maintenance 9. MA-3(a) Maintenance Tool 10. MA-4(a) Nonlocal Maintenance 11. PE-3(d) Physical Access Control 12. PE-6 Monitoring Physical Access 13. PE-14(b) Environmental Controls 14. PE-16 Delivery and Removal 15. PS-7(e) External Personnel Security 16. SA-9(c) External System Services 17. SC-7(a) Boundary Protection 18. SC-7(24)(b) Boundary Protection | Personally Identifiable Information 19. SC-18(b) Mobile Code 20. SI-4 System Monitoring b. Establishing an ongoing frequency for monitoring and an ongoing frequency for assessment of control effectiveness; c. Ongoing control assessments in accordance with the continuous monitoring strategy; d. Ongoing monitoring of system and organization-defined metrics in accordance with the continuous monitoring strategy; e. Correlation and analysis of information generated by control assessments and monitoring; f. Response actions to address results of the analysis of control assessment and monitoring information; and g. Reporting the security and privacy status of the system to organizational personnel with information security, privacy responsibilities, and system/network administrators annually, when security events/incidents occur, and when requested.

**Discussion**

> Continuous monitoring at the system level facilitates ongoing awareness of the system security and privacy posture to support organizational risk management decisions. The terms "continuous" and "ongoing" imply that organizations assess and monitor their controls and risks at a frequency sufficient to support risk-based decisions. Different types of controls may require different monitoring frequencies. The results of continuous monitoring generate risk response actions by organizations. When monitoring the effectiveness of multiple controls that have been grouped into capabilities, a root-cause analysis may be needed to determine the specific control that has failed. Continuous monitoring programs allow organizations to maintain the authorizations of systems and common controls in highly dynamic environments of operation with changing mission and business needs, threats, vulnerabilities, and technologies. Having access to security and privacy information on a continuing basis through reports and dashboards gives organizational officials the ability to make effective and timely risk management decisions, including ongoing authorization decisions. Automation supports more frequent updates to hardware, software, and firmware inventories, authorization packages, and other system information. Effectiveness is further enhanced when continuous monitoring outputs are formatted to provide information that is specific, measurable, actionable, relevant, and timely. Continuous monitoring activities are scaled in accordance with the security categories of systems. Monitoring requirements, including the need for specific monitoring, may be referenced in other controls and control enhancements.

**Related Controls in the source**

> AC-2, AC-6, AC-17, AT-4, AU-6, CA-2, CA-5, CA-6, CM-3, CM-4, CM-6, CM-11, IA-5, IR-5, MA-2, MA-3, MA-4, PE-3, PE-6, PE-14, PE-16, PL-2, PS-7, RA-3, RA-5, RA-7, SA-8, SA-9, SA-11, SC-5, SC-7, SC-18, SI-3, SI-4, SI-12, SR-6.

## Related controls

[AC-2](../control_documents/AC-2.md), [AC-6](../control_documents/AC-6.md), [AC-17](../control_documents/AC-17.md), [AT-4](../control_documents/AT-4.md), [AU-6](../control_documents/AU-6.md), [CA-2](../control_documents/CA-2.md), [CA-5](../control_documents/CA-5.md), [CA-6](../control_documents/CA-6.md), [CM-3](../control_documents/CM-3.md), [CM-4](../control_documents/CM-4.md), [CM-6](../control_documents/CM-6.md), [CM-11](../control_documents/CM-11.md), [IA-5](../control_documents/IA-5.md), [IR-5](../control_documents/IR-5.md), [MA-2](../control_documents/MA-2.md), [MA-3](../control_documents/MA-3.md), [MA-4](../control_documents/MA-4.md), [PE-3](../control_documents/PE-3.md), [PE-6](../control_documents/PE-6.md), [PE-14](../control_documents/PE-14.md), [PE-16](../control_documents/PE-16.md), [PL-2](../control_documents/PL-2.md), [PS-7](../control_documents/PS-7.md), [RA-3](../control_documents/RA-3.md), [RA-5](../control_documents/RA-5.md), [RA-7](../control_documents/RA-7.md), [SA-8](../control_documents/SA-8.md), [SA-9](../control_documents/SA-9.md), [SA-11](../control_documents/SA-11.md), [SC-5](../control_documents/SC-5.md), [SC-7](../control_documents/SC-7.md), [SC-18](../control_documents/SC-18.md), [SI-3](../control_documents/SI-3.md), [SI-4](../control_documents/SI-4.md), [SI-12](../control_documents/SI-12.md), [SR-6](../control_documents/SR-6.md)

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
