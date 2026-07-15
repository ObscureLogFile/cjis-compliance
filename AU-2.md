<a id="control-au-2"></a>
# AU-2 — Event Logging

**Control family:** Audit and Accountability (AU)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-AU-2` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Daily review for alerts; monthly formal review |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **AU-2 — Event Logging** for systems, personnel, services, and data within the CJIS scope.

This control addresses event logging for CJIS systems, users, or data.

**Implementation objective:** Send logs to a central platform and review them on a schedule.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **AU-2** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

**Procedure**

1. Enable the required audit events for the control and its supporting systems.
2. Send logs to the approved collection or review location.
3. Review the logs or alerts on the defined cadence and investigate anomalies.
4. Retain and protect the records for the required period.
5. Record the result, evidence location, reviewer, date, and any exception or remediation reference.
6. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.

**Workflow output**

An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.

## Organizational action items

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for AU-2.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by AU-2.
- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.
- [ ] Record the current implementation state, gap, risk level, and target completion date.
- [ ] Test the control and attach the result to the evidence repository.
- [ ] Schedule the recurring review and assign an accountable reviewer.
- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.

## Audit evidence and continuous compliance artifacts

**Expected evidence:** Audit logs, SIEM alerts, review signoff, exception tickets.

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

- **Source title:** EVENT LOGGING
- **Source marking:** `[Priority 2]`

**Control**

> a. Identify the types of events that the system is capable of logging in support of the audit function: authentication, file use, user/group management, events sufficient to establish what occurred, the sources of events, outcomes of events, and operational transactions (e.g., NCIC, III); b. Coordinate the event logging function with other organizational entities requiring audit- related information to guide and inform the selection criteria for events to be logged; c. Specify the following event types for logging within the system: All successful and unsuccessful: 1. System log-on attempts 2. Attempts to use: a. Access permission on a user account, file, directory, or other system resource; b. Create permission on a user account, file, directory, or other system resource; c. Write permission on a user account, file, directory, or other system resource; d. Delete permission on a user account, file, directory, or other system resource; e. Change permission on a user account, file, directory, or other system resource. 3. Attempts to change account passwords 4. Actions by privileged accounts (i.e., root, Oracle, DBA, admin, etc.) 5. Attempts for users to: a. Access the audit log file; b. Modify the audit log file; c. Destroy the audit log file. d. Provide a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents; and e. Review and update the event types selected for logging annually.

**Discussion**

> An event is an observable occurrence in a system. The types of events that require logging are those events that are significant and relevant to the security of systems and the privacy of individuals. Event logging also supports specific monitoring and auditing needs. Event types include password changes, failed logons or failed accesses related to systems, security or privacy attribute changes, administrative privilege usage, PIV credential usage, data action changes, query parameters, or external credential usage. In determining the set of event types that require logging, organizations consider the monitoring and auditing appropriate for each of the controls to be implemented. For completeness, event logging includes all protocols that are operational and supported by the system. To balance monitoring and auditing requirements with other system needs, event logging requires identifying the subset of event types that are logged at a given point in time. For example, organizations may determine that systems need the capability to log every file access successful and unsuccessful, but not activate that capability except for specific circumstances due to the potential burden on system performance. The types of events that organizations desire to be logged may change. Reviewing and updating the set of logged events is necessary to help ensure that the events remain relevant and continue to support the needs of the organization. Organizations consider how the types of logging events can reveal information about individuals that may give rise to privacy risk and how best to mitigate such risks. For example, there is the potential to reveal personally identifiable information in the audit trail, especially if the logging event is based on patterns or time of usage. Event logging requirements, including the need to log specific event types, may be referenced in other controls and control enhancements. These include AC-2(4), AC-3(10), AC-6(9), AC-17(1), CM-3f, CM-5(1), IA-3(3.b), MA-4(1), MP-4(2), PE-3, PM-21, PT-7, RA-8, SC-7(9), SC-7(15), SI-3(8), SI-4(22), SI-7(8), and SI-10(1). Organizations include event types that are required by applicable laws, executive orders, directives, policies, regulations, standards, and guidelines. Audit records can be generated at various levels, including at the packet level as information traverses the network. Selecting the appropriate level of event logging is an important part of a monitoring and auditing capability and can identify the root causes of problems. When defining event types, organizations consider the logging necessary to cover related event types, such as the steps in distributed, transaction-based processes and the actions that occur in service-oriented architectures.

**Related Controls in the source**

> AC-2, AC-3, AC-6, AC-7, AC-8, AC-17, AU-3, AU-4, AU-5, AU-6, AU-7, AU-11, AU-12, CM-3, CM-5, CM-6, IA-3, MA-4, MP-4, PE-3, SA-8, SC-7, SC-18, SI-3, SI-4, SI-7, SI-10, SI-11.

## Related controls

[AC-2](../control_documents/AC-2.md), [AC-3](../control_documents/AC-3.md), [AC-6](../control_documents/AC-6.md), [AC-7](../control_documents/AC-7.md), [AC-8](../control_documents/AC-8.md), [AC-17](../control_documents/AC-17.md), [AU-3](../control_documents/AU-3.md), [AU-4](../control_documents/AU-4.md), [AU-5](../control_documents/AU-5.md), [AU-6](../control_documents/AU-6.md), [AU-7](../control_documents/AU-7.md), [AU-11](../control_documents/AU-11.md), [AU-12](../control_documents/AU-12.md), [CM-3](../control_documents/CM-3.md), [CM-5](../control_documents/CM-5.md), [CM-6](../control_documents/CM-6.md), [IA-3](../control_documents/IA-3.md), [MA-4](../control_documents/MA-4.md), [MP-4](../control_documents/MP-4.md), [PE-3](../control_documents/PE-3.md), [SA-8](../control_documents/SA-8.md), [SC-7](../control_documents/SC-7.md), [SC-18](../control_documents/SC-18.md), [SI-3](../control_documents/SI-3.md), [SI-4](../control_documents/SI-4.md), [SI-7](../control_documents/SI-7.md), [SI-10](../control_documents/SI-10.md), [SI-11](../control_documents/SI-11.md)

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
