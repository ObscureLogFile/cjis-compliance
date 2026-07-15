<a id="control-ia-8"></a>
# IA-8 — Identification and Authentication (Non-organizational Users)

**Control family:** Identification and Authentication (IA)

## Document control and cadence

| Field | Value |
| --- | --- |
| Document ID | `CJIS-CTRL-IA-8` |
| Agency | `[[AGENCY_NAME]]` |
| Version | `[[DOCUMENT_VERSION]]` |
| Owner | `[[CONTROL_OWNER]]` |
| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |
| Effective date | `[[EFFECTIVE_DATE]]` |
| Next review date | `[[NEXT_REVIEW_DATE]]` |
| Operating cadence | Annual review and on change |
| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |

## Policy & Purpose

This control document defines how `[[AGENCY_NAME]]` implements **IA-8 — Identification and Authentication (Non-organizational Users)** for systems, personnel, services, and data within the CJIS scope.

This control addresses identification and authentication (non-organizational users) for CJIS systems, users, or data.

**Implementation objective:** Use unique identities, strong authenticators, and controlled lifecycle management.

## Operational roles and responsibilities

- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.
- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.
- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.
- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.
- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.
- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.

## Step-by-step procedures workflow

**Trigger / inputs**

A new system, user, vendor, change, incident, assessment finding, or scheduled review places **IA-8** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.

**Procedure**

1. Verify the identity of the user, device, or service before granting access.
2. Issue the approved authenticator and record the issuance details.
3. Enforce authentication strength, renewal, and re-authentication rules.
4. Revoke or reset credentials promptly when compromise or separation occurs.
5. Record the result, evidence location, reviewer, date, and any exception or remediation reference.
6. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.

**Workflow output**

An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.

## Organizational action items

- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for IA-8.
- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by IA-8.
- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.
- [ ] Record the current implementation state, gap, risk level, and target completion date.
- [ ] Test the control and attach the result to the evidence repository.
- [ ] Schedule the recurring review and assign an accountable reviewer.
- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.

## Audit evidence and continuous compliance artifacts

**Expected evidence:** MFA enrollment evidence, account provisioning records, reset tickets.

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

- **Source title:** IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS)
- **Source marking:** `[Priority 2]`

**Control**

> Uniquely identify and authenticate non-organizational users or processes acting on behalf of non-organizational users. DISCUSSION: Non-organizational users include system users other than organizational users explicitly covered by IA-2. Non-organizational users are uniquely identified and authenticated for accesses other than those explicitly identified and documented in AC-14. Identification and authentication of non-organizational users accessing federal systems may be required to protect federal, proprietary, or privacy-related information (with exceptions noted for national security systems). Organizations consider many factors—including security, privacy, scalability, and practicality—when balancing the need to ensure ease of use for access to federal information and systems with the need to protect and adequately mitigate risk. Related Controls: AC-2, AC-6, AC-14, AC-17, AC-18, AU-6, IA-2, IA-4, IA-5, IA-11, MA-4, RA-3, SA-4, SC-8. Control Enhancements: (1) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | ACCEPTANCE OF PIV CREDENTIALS FROM OTHER AGENCIES [Priority 2] Control: Accept and electronically verify Personal Identity Verification-compliant credentials from other federal, state, local, tribal, or territorial (SLTT) agencies. DISCUSSION: Acceptance of Personal Identity Verification (PIV) credentials from other federal or SLTT agencies applies to both logical and physical access control systems. PIV credentials are those credentials issued by federal or SLTT agencies that conform to FIPS Publication 201 and supporting guidelines. Related Controls: PE-3. (2) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | ACCEPTANCE OF EXTERNAL AUTHENTICATORS [Priority 2] Control: (a) Accept only external authenticators that are NIST-compliant; and (b) Document and maintain a list of accepted external authenticators. DISCUSSION: Acceptance of only NIST-compliant external authenticators applies to organizational systems that are accessible to the public (e.g., public-facing websites). External authenticators are issued by nonfederal government entities and are compliant with the CJISSECPOL. Approved external authenticators meet or exceed the minimum Federal Government-wide technical, security, privacy, and organizational maturity requirements. Meeting or exceeding Federal requirements allows Federal Government relying parties to trust external authenticators in connection with an authentication transaction at a specified authenticator assurance level. Related Controls: None. (4) IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS) | USE OF DEFINED PROFILES [Priority 2] Control: Conform to the following profiles for identity management: Security Assertion Markup Language (SAML) or OpenID Connect. DISCUSSION: Organizations define profiles for identity management based on open identity management standards. To ensure that open identity management standards are viable, robust, reliable, sustainable, and interoperable as documented, the Federal Government assesses and scopes the standards and technology implementations against applicable laws, executive orders, directives, policies, regulations, standards, and guidelines. Related Controls: None.

**Discussion**

> No discussion text was extracted.

**Related Controls in the source**

> None listed.

## Related controls

[AC-2](../control_documents/AC-2.md), [AC-6](../control_documents/AC-6.md), [AC-14](../control_documents/AC-14.md), [AC-17](../control_documents/AC-17.md), [AC-18](../control_documents/AC-18.md), [AU-6](../control_documents/AU-6.md), [IA-2](../control_documents/IA-2.md), [IA-4](../control_documents/IA-4.md), [IA-5](../control_documents/IA-5.md), [IA-11](../control_documents/IA-11.md), [MA-4](../control_documents/MA-4.md), [RA-3](../control_documents/RA-3.md), [SA-4](../control_documents/SA-4.md), [SC-8](../control_documents/SC-8.md)

**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.
