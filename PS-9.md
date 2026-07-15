<a id="control-ps-9"></a>
# PS-9 — Position Descriptions

**Control family:** Personnel Security (PS)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-PS-9` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Each hire/exit; annual audit |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **PS-9 — Position Descriptions** for systems, personnel, services, and data within the CJIS scope.

This control addresses position descriptions for CJIS systems, users, or data.

**Implementation objective:** Screen people before access and remove access promptly when status changes.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **PS-9** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

**Procedure**

1. Complete screening and access agreements before CJIS access is granted.
2. Assign access only to the role and remove unnecessary privileges promptly.
3. Process transfers, terminations, and sanctions through the documented workflow.
4. Keep screening and agreement records current and retrievable.
5. Record the result, evidence location, reviewer, date, and any exception or remediation reference.
6. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.

**Workflow output**

An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.

## Organizational action items

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for PS-9.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by PS-9.
- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.
- [ ] Record the current implementation state, gap, risk level, and target completion date.
- [ ] Test the control and attach the result to the evidence repository.
- [ ] Schedule the recurring review and assign an accountable reviewer.
- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.

## Audit evidence and continuous compliance artifacts

**Expected evidence:** Background clearance, signed agreements, offboarding checklist.

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

- **Source title:** POSITION DESCRIPTIONS
- **Source marking:** `[Priority 4]`

**Control**

> Incorporate security and privacy roles and responsibilities into organizational position descriptions.

**Discussion**

> Specification of security and privacy roles in individual organizational position descriptions facilitates clarity in understanding the security or privacy responsibilities associated with the roles and the role-based security and privacy training requirements for the roles. Figure 13 – Personnel Security Use Cases Use Case 1 – A Local Police Department\222s Personnel Security Controls A local police department implemented a replacement CAD system that integrated to their state\222s CSA and was authorized to process CJI. In addition to the physical and technical controls already in place, the police department implemented a variety of personnel security controls to reduce the insider threat. The police department used background screening consistent with the FBI CJIS Security Policy to vet those with unescorted access to areas in which CJI is processed, including the IT administrators employed by a contractor and all janitorial staff. The police department established sanctions against any vetted person found to be in violation of stated policies. The police department re-evaluated each person\222s suitability for access to CJI every five years. Use Case 2 – Infrastructure as a Service (IaaS) Cloud Service Implementation This model provides the consumer the capability to provision processing, storage, networks, and other fundamental computing resources where the consumer is able to deploy and run arbitrary software, including operating systems and applications. When using the IaaS service model the consumer may have control over operating systems, storage, and deployed applications; and possibly limited control of select networking components (e.g., host firewalls), but does not manage or control the underlying cloud infrastructure – as defined in Appendix G.3. A local agency implements an IaaS solution in a cloud environment leveraging an agency-implemented secure virtual private cloud which has been identified to meet the appropriate security controls in the CJIS Security Policy. The agency maintains sole access to the encryption keys. In this scenario, cloud service provider personnel have no logical or physical access to any information system resulting in the ability, right, or privilege to view, modify, or make use of unencrypted CJI; therefore, no fingerprint-based background checks are required to comply with the CJIS Security Policy. Refer to Appendix G.3 Cloud Computing for additional implementation guidance. Use Case 3 – Platform as a Service (PaaS) Cloud Service Implementation This model provides the consumer the capability to deploy consumer-created or acquired applications* created using programming languages, libraries, services, and tools supported by the provider onto the cloud infrastructure. * This capability does not necessarily preclude the use of compatible programming languages, libraries, services, and tools from other sources. When using the PaaS service model, the consumer may have control over the deployed applications and possibly configuration settings for the application-hosting environment, but does not manage or control the underlying cloud infrastructure including network, servers, operating systems, or storage – as defined in Appendix G.3. An agency utilizes a cloud service solution involving PaaS to write code, build, or develop a new application. There is no CJI associated with the code development. Although cloud service personnel provide support for the platform (i.e., hardware and software maintenance), no CJI is being accessed during development. The cloud service provider has no unescorted logical or physical access to any information system and no ability, right, or privilege to view, modify, or make use of unencrypted CJI. Refer to Appendix G.3 Cloud Computing for additional implementation guidance. Use Case 4 – Software as a Service (SaaS) Cloud Service Implementation The SaaS service model is often referred to as "Software deployed as a hosted service and accessed over the Internet." The applications are accessible from various client devices through either a thin client interface, such as a web browser (e.g., web-based email), or a program interface. When using the SaaS service model, it should be understood that the consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, storage, or even individual application capabilities, with the possible exception of limited user-specific application configuration settings – as defined in Appendix G.3 An agency utilizes a SaaS provider for their records management system (RMS). The SaaS provider hosts their solution on a cloud provider. The SaaS provider directly supports the agency for updates and management of the solution and has unescorted logical or physical access to the information system resulting in the ability, right, or privilege to view, modify, or make use of unencrypted CJI within the RMS. The cloud provider, however, does not have unescorted logical or physical access to any information system resulting in the ability, right, or privilege to view, modify, or make use of unencrypted CJI as the SaaS provider maintains the encryption keys. In this scenario, the agency would be required to comply with Section 5.12 for employees of the SaaS provider with access to CJI but would not need to do so for employees of the cloud provider used by the SaaS provider. Refer to Appendix G.3 Cloud Computing for additional implementation guidance. RISK ASSESSMENT (RA)

**Related Controls in the source**

> None listed.

## Related controls

None listed in the supplied control inventory.

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
