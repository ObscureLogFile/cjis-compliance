from pathlib import Path
import re


ROOT = Path(r"C:\Users\AbysmalChef\Desktop\Projects\Work\CJIS-compliance")
SOURCE_PATH = ROOT / "CJIS_Control_Item_Templates.md"
MATRIX_PATH = ROOT / "CJIS_Control_Implementation_Matrix.md"
PROCEDURES_PATH = ROOT / "CJIS_Operating_Procedures.md"
RAW_PATH = ROOT / "_cjis_raw_extract.txt"
CONTROL_DOCS_PATH = ROOT / "control_documents"
MASTER_PATH = ROOT / "CJIS_Control_Master_Manual.md"


FAMILY_ORDER = [
    "Access Control (AC)",
    "Awareness and Training (AT)",
    "Audit and Accountability (AU)",
    "Assessment, Authorization, and Monitoring (CA)",
    "Configuration Management (CM)",
    "Contingency Planning (CP)",
    "Identification and Authentication (IA)",
    "Incident Response (IR)",
    "Maintenance (MA)",
    "Media Protection (MP)",
    "Physical and Environmental Protection (PE)",
    "Planning (PL)",
    "Personnel Security (PS)",
    "Risk Assessment (RA)",
    "System and Services Acquisition / Development (SA)",
    "System and Communications Protection (SC)",
    "System and Information Integrity (SI)",
    "Supply Chain Risk Management (SR)",
]

FAMILY_PREFIX = {
    "Access Control (AC)": "AC",
    "Awareness and Training (AT)": "AT",
    "Audit and Accountability (AU)": "AU",
    "Assessment, Authorization, and Monitoring (CA)": "CA",
    "Configuration Management (CM)": "CM",
    "Contingency Planning (CP)": "CP",
    "Identification and Authentication (IA)": "IA",
    "Incident Response (IR)": "IR",
    "Maintenance (MA)": "MA",
    "Media Protection (MP)": "MP",
    "Physical and Environmental Protection (PE)": "PE",
    "Planning (PL)": "PL",
    "Personnel Security (PS)": "PS",
    "Risk Assessment (RA)": "RA",
    "System and Services Acquisition / Development (SA)": "SA",
    "System and Communications Protection (SC)": "SC",
    "System and Information Integrity (SI)": "SI",
    "Supply Chain Risk Management (SR)": "SR",
}

FAMILY_MATRIX = {
    "Access Control (AC)": ("[[CONTROL_OWNER]]", "Implement role-based access, MFA, account lifecycle controls, and periodic access review.", "Access request forms, approvals, MFA status, access review report", "Quarterly or [[ACCESS_REVIEW_INTERVAL_DAYS]] days"),
    "Awareness and Training (AT)": ("[[CONTROL_OWNER]]", "Assign CJIS awareness training at onboarding and annually, then record completion.", "Training completion records, signed acknowledgments, roster export", "Annual and upon hire or role change"),
    "Audit and Accountability (AU)": ("[[CONTROL_OWNER]]", "Centralize logs, protect them from tampering, and review them on a recurring schedule.", "Audit logs, SIEM alerts, review signoff, exception tickets", "Daily review for alerts; monthly formal review"),
    "Assessment, Authorization, and Monitoring (CA)": ("[[CONTROL_OWNER]]", "Assess the control before use, track findings, and re-evaluate after changes.", "Assessment report, POA&M, authorization memo, monitoring dashboard", "Before go-live and annual review"),
    "Configuration Management (CM)": ("[[CONTROL_OWNER]]", "Use hardened baselines, change approval, and current asset inventory.", "Baseline standards, change tickets, inventory export, rollback record", "Quarterly and after changes"),
    "Contingency Planning (CP)": ("[[CONTROL_OWNER]]", "Maintain recovery plans, backups, and restoration tests for CJIS systems.", "BCP/DR plan, backup reports, restore test results", "Annual test and update"),
    "Identification and Authentication (IA)": ("[[CONTROL_OWNER]]", "Issue unique identities, require strong authentication, and control credential lifecycle.", "MFA enrollment evidence, account provisioning records, reset tickets", "Annual review and on change"),
    "Incident Response (IR)": ("[[CONTROL_OWNER]]", "Use a documented intake, containment, notification, and recovery process.", "Incident tickets, timeline, evidence log, after-action report", "After each incident; annual exercise"),
    "Maintenance (MA)": ("[[CONTROL_OWNER]]", "Approve maintenance, monitor work, and log results before returning to service.", "Maintenance log, vendor approval, escort record, return-to-service note", "Each maintenance event; annual review"),
    "Media Protection (MP)": ("[[CONTROL_OWNER]]", "Label, store, transport, and sanitize CJIS media under chain-of-custody controls.", "Media inventory, checkout log, destruction certificate", "Monthly inventory; per disposal event"),
    "Physical and Environmental Protection (PE)": ("[[CONTROL_OWNER]]", "Restrict facility access and protect devices, cabling, and environmental conditions.", "Badge report, visitor log, inspection checklist, camera log", "Quarterly and after facility changes"),
    "Planning (PL)": ("[[CONTROL_OWNER]]", "Document system security, privacy, and baseline decisions before changes go live.", "System security plan, architecture notes, baseline approvals", "Annual review and after major change"),
    "Personnel Security (PS)": ("[[CONTROL_OWNER]]", "Screen personnel, document access agreements, and remove access promptly on status changes.", "Background clearance, signed agreements, offboarding checklist", "Each hire/exit; annual audit"),
    "Risk Assessment (RA)": ("[[CONTROL_OWNER]]", "Identify and prioritize risks, then track mitigation to closure.", "Risk register, scan results, mitigation plan, signoff", "Annual and after material change"),
    "System and Services Acquisition / Development (SA)": ("[[CONTROL_OWNER]]", "Bake CJIS requirements into procurement, design, testing, and vendor acceptance.", "Security clauses, procurement checklist, test evidence, acceptance record", "Per procurement/project"),
    "System and Communications Protection (SC)": ("[[CONTROL_OWNER]]", "Protect data in transit and at rest, and control network boundaries and remote paths.", "Encryption standard, firewall rules, VPN config, architecture diagram", "Quarterly and after changes"),
    "System and Information Integrity (SI)": ("[[CONTROL_OWNER]]", "Patch quickly, monitor for malicious activity, and validate integrity.", "Patch report, AV dashboard, alert tickets, integrity check results", "Weekly patch review; continuous monitoring"),
    "Supply Chain Risk Management (SR)": ("[[CONTROL_OWNER]]", "Vet vendors and components, include security terms, and track lifecycle risk.", "Vendor questionnaire, contract clause record, risk review, lifecycle status", "Annual and before purchase"),
}

FAMILY_PROCEDURES = {
    "Access Control (AC)": [
        "Identify the person, role, or system that needs access.",
        "Obtain documented approval for the least privilege needed.",
        "Provision the account, permissions, and MFA or other required controls.",
        "Verify access works as intended and remove any extra privileges.",
    ],
    "Awareness and Training (AT)": [
        "Assign the required CJIS training based on the person’s role.",
        "Confirm the person completes training before CJIS access is activated.",
        "Record the completion date, score or attestation, and refresher due date.",
        "Reassign training after role changes and on the annual cycle.",
    ],
    "Audit and Accountability (AU)": [
        "Enable the required audit events for the control and its supporting systems.",
        "Send logs to the approved collection or review location.",
        "Review the logs or alerts on the defined cadence and investigate anomalies.",
        "Retain and protect the records for the required period.",
    ],
    "Assessment, Authorization, and Monitoring (CA)": [
        "Assess the control design and operating effectiveness before production use.",
        "Document findings, remediation actions, and the approval decision.",
        "Monitor the control on a recurring basis and after major changes.",
        "Update the authorization record if risk or scope changes materially.",
    ],
    "Configuration Management (CM)": [
        "Establish the approved baseline for the system or component.",
        "Route changes through the documented approval and testing workflow.",
        "Deploy the change, then verify that the baseline and inventory are current.",
        "Review exceptions and drift against the approved configuration.",
    ],
    "Contingency Planning (CP)": [
        "Document recovery priorities, dependencies, and restoration steps.",
        "Ensure backups or alternate capabilities are created and protected.",
        "Test restoration or failover on the scheduled cadence.",
        "Revise the plan after tests, incidents, or major system changes.",
    ],
    "Identification and Authentication (IA)": [
        "Verify the identity of the user, device, or service before granting access.",
        "Issue the approved authenticator and record the issuance details.",
        "Enforce authentication strength, renewal, and re-authentication rules.",
        "Revoke or reset credentials promptly when compromise or separation occurs.",
    ],
    "Incident Response (IR)": [
        "Receive the incident report and open a tracked case immediately.",
        "Contain the event, preserve evidence, and notify required parties.",
        "Remediate the root cause and restore impacted services safely.",
        "Close the incident with lessons learned and any corrective actions.",
    ],
    "Maintenance (MA)": [
        "Approve maintenance work before it starts and define the scope.",
        "Monitor or escort the activity as required and log the session.",
        "Verify the system is stable and secure before it returns to service.",
        "Retain the maintenance record and follow up on open issues.",
    ],
    "Media Protection (MP)": [
        "Classify and label media based on the CJIS content it contains.",
        "Store and transport the media using approved chain-of-custody controls.",
        "Track use, movement, and storage in a log or inventory.",
        "Sanitize or destroy media when it is no longer needed and retain proof.",
    ],
    "Physical and Environmental Protection (PE)": [
        "Restrict access to approved physical spaces and devices.",
        "Maintain monitoring, visitor control, and environmental safeguards.",
        "Inspect doors, badges, cameras, power, and cabling on schedule.",
        "Document exceptions, maintenance, and corrective actions.",
    ],
    "Planning (PL)": [
        "Document the requirement, design decision, or plan element in the approved plan set.",
        "Review the documentation against current operations and risk.",
        "Update the plan when the architecture, scope, or control baseline changes.",
        "Retain approval and revision history.",
    ],
    "Personnel Security (PS)": [
        "Complete screening and access agreements before CJIS access is granted.",
        "Assign access only to the role and remove unnecessary privileges promptly.",
        "Process transfers, terminations, and sanctions through the documented workflow.",
        "Keep screening and agreement records current and retrievable.",
    ],
    "Risk Assessment (RA)": [
        "Identify the assets, threats, and vulnerabilities that affect the control area.",
        "Rate the risk and assign treatment or mitigation actions.",
        "Track remediation and residual risk to closure or acceptance.",
        "Reassess on the recurring schedule or after a significant change.",
    ],
    "System and Services Acquisition / Development (SA)": [
        "Define the CJIS security requirement before acquisition or development begins.",
        "Build the requirement into procurement, design, and testing artifacts.",
        "Validate the control before acceptance or release.",
        "Update vendor records and technical documentation after go-live.",
    ],
    "System and Communications Protection (SC)": [
        "Define the network boundary, data path, or protection method needed.",
        "Configure encryption, segmentation, routing, or session controls as required.",
        "Verify the control with testing, logs, or review evidence.",
        "Monitor for changes or failures and remediate quickly.",
    ],
    "System and Information Integrity (SI)": [
        "Enable monitoring, patching, or integrity checking for the control area.",
        "Review alerts or scan results and open remediation when needed.",
        "Deploy fixes or compensating safeguards promptly.",
        "Confirm the issue is resolved and retain the evidence.",
    ],
    "Supply Chain Risk Management (SR)": [
        "Review the vendor, component, or supplier before use.",
        "Include CJIS requirements in procurement, contract language, or acceptance criteria.",
        "Monitor the supplier lifecycle, vulnerabilities, and service changes.",
        "Retire or replace risky components according to the plan.",
    ],
}


def parse_records(text: str):
    records = []
    current_family = None
    current = None
    skip_families = {"Shared Placeholders", "How To Use"}
    for line in text.splitlines():
        if line.startswith("## "):
            name = line[3:].strip()
            if name in skip_families:
                current_family = None
                current = None
            else:
                current_family = name
        elif (line.startswith("### ") or line.startswith("#### ")) and current_family:
            heading = line[3:].strip() if line.startswith("### ") else line[4:].strip()
            match = re.match(r"(?P<code>[^ ]+)\s+-\s+(?P<title>.+)", heading)
            code = match.group("code") if match else heading
            title = match.group("title") if match else heading
            current = {
                "family": current_family,
                "code": code,
                "title": title,
                "what": "",
                "recommendation": "",
                "parent": "N/A",
                "related_controls": "None",
                "related_enhancements": "None",
                "tags": "",
            }
            records.append(current)
        elif current is not None and line.startswith("Tags:"):
            current["tags"] = line[5:].strip()
        elif current is not None and line.startswith("| Control code |"):
            current["code"] = line.split("| Control code |", 1)[1].strip().strip("|").strip().strip("`")
        elif current is not None and line.startswith("| Control title |"):
            title = line.split("| Control title |", 1)[1].strip().strip("|").strip()
            current["title"] = re.sub(r"\s+\.{5,}.*$", "", title).strip()
        elif current is not None and line.startswith("| What it is |"):
            current["what"] = line.split("| What it is |", 1)[1].strip().strip("|").strip()
        elif current is not None and line.startswith("| Recommended approach |"):
            current["recommendation"] = line.split("| Recommended approach |", 1)[1].strip().strip("|").strip()
        elif current is not None and line.startswith("| Parent control |"):
            current["parent"] = line.split("| Parent control |", 1)[1].strip().strip("|").strip().strip("`")
        elif current is not None and line.startswith("| Related controls |"):
            current["related_controls"] = line.split("| Related controls |", 1)[1].strip().strip("|").strip()
        elif current is not None and line.startswith("| Related enhancements |"):
            current["related_enhancements"] = line.split("| Related enhancements |", 1)[1].strip().strip("|").strip()
    return records


def group_records(records):
    family_order = []
    grouped = {}
    for rec in records:
        fam = rec["family"]
        if fam not in grouped:
            grouped[fam] = []
            family_order.append(fam)
        grouped[fam].append(rec)
    return family_order, grouped


def build_matrix(records, family_order, grouped):
    lines = []
    lines.append("# [[AGENCY_NAME]] CJIS Control Implementation Matrix")
    lines.append("")
    lines.append("This expanded matrix gives each CJIS control its own implementation entry so owners can assign work, collect evidence, and review the control on a defined cadence.")
    lines.append("")
    lines.append("## Shared Placeholders")
    lines.append("")
    lines.extend([
        "- `[[CONTROL_OWNER]]`",
        "- `[[IMPLEMENTATION_NOTES]]`",
        "- `[[EVIDENCE_ARTIFACTS]]`",
        "- `[[REVIEW_FREQUENCY]]`",
        "- `[[ACCESS_REVIEW_INTERVAL_DAYS]]`",
        "- `[[RISK_LEVEL]]`",
    ])
    lines.append("")
    lines.append("## How To Use")
    lines.append("")
    lines.extend([
        "- Replace placeholders with agency-specific values.",
        "- Use one owner per control and keep evidence current.",
        "- Mark exceptions separately and tie them to a review date.",
    ])
    lines.append("")

    for fam in family_order:
        lines.append(f"## {fam}")
        lines.append("")
        owner, impl, evidence, review = FAMILY_MATRIX.get(fam, ("[[CONTROL_OWNER]]", "Implement the control using the approved standard.", "Approval, configuration, and review evidence", "Annual review"))
        for rec in grouped[fam]:
            code = rec["code"]
            title = rec["title"]
            what = rec["what"]
            recommendation = rec["recommendation"]
            if "(" in code:
                impl_text = "Apply the enhancement to the parent control configuration, then verify it in testing or monitoring."
                evidence_text = f"Proof of enhancement configuration, test result, or log review tied to {code}"
                review_text = "After implementation and at the same recurring interval as the parent control"
            else:
                impl_text = impl
                evidence_text = evidence
                review_text = review
            lines.append(f"### {code} - {title}")
            lines.append("")
            lines.append("| Field | Value |")
            lines.append("| --- | --- |")
            lines.append(f"| Control code | `{code}` |")
            lines.append(f"| Control title | {title} |")
            lines.append(f"| What it is | {what} |")
            lines.append(f"| Recommended approach | {recommendation} |")
            lines.append(f"| Primary owner | `{owner}` |")
            lines.append(f"| Implementation method | {impl_text} |")
            lines.append(f"| Evidence / artifact | {evidence_text} |")
            lines.append(f"| Review frequency | {review_text.replace('[[ACCESS_REVIEW_INTERVAL_DAYS]]', '`[[ACCESS_REVIEW_INTERVAL_DAYS]]`')} |")
            lines.append("")
    return "\n".join(lines)


def build_procedures(records, family_order, grouped):
    lines = []
    lines.append("# [[AGENCY_NAME]] CJIS Operating Procedures")
    lines.append("")
    lines.append("This expanded procedure set gives each CJIS control a practical operating routine. Use it to train staff, run the control consistently, and collect evidence for review.")
    lines.append("")
    lines.append("## Shared Placeholders")
    lines.append("")
    lines.extend([
        "- `[[CONTROL_OWNER]]`",
        "- `[[REVIEW_FREQUENCY]]`",
        "- `[[IR_RESPONSE_PHONE]]`",
        "- `[[IR_RESPONSE_EMAIL]]`",
        "- `[[ACCESS_REVIEW_INTERVAL_DAYS]]`",
        "- `[[SESSION_LOCK_MINUTES]]`",
        "- `[[EVIDENCE_ARTIFACTS]]`",
    ])
    lines.append("")
    lines.append("## How To Use")
    lines.append("")
    lines.extend([
        "- Replace placeholders with agency-specific values.",
        "- Keep procedures short enough to follow during real operations.",
        "- Update the procedure when the control, vendor, or technology changes.",
    ])
    lines.append("")

    for fam in family_order:
        lines.append(f"## {fam}")
        lines.append("")
        family_steps = FAMILY_PROCEDURES.get(fam, [
            "Identify the control requirement and the system or process in scope.",
            "Perform the approved action to implement or maintain the control.",
            "Verify the result and record the evidence.",
            "Escalate exceptions and review the control on the required cadence.",
        ])
        for rec in grouped[fam]:
            code = rec["code"]
            title = rec["title"]
            what = rec["what"]
            recommendation = rec["recommendation"]
            if "(" in code:
                purpose = f"Enhancement to {title} that strengthens the parent control."
                steps = [
                    f"Confirm the parent control for {code.split('(')[0]} is already operating.",
                    "Enable the enhancement using the approved configuration or process.",
                    "Test or observe the enhancement to confirm it is functioning.",
                    "Record the result and update the parent control evidence set.",
                ]
            else:
                purpose = what
                steps = family_steps
            lines.append(f"### {code} - {title}")
            lines.append("")
            lines.append(f"**Purpose:** {purpose}")
            lines.append("")
            lines.append("**Procedure**")
            lines.append("")
            for idx, step in enumerate(steps, start=1):
                lines.append(f"{idx}. {step}")
            lines.append("")
            lines.append("**Recommended approach**")
            lines.append("")
            lines.append(recommendation)
            lines.append("")
            lines.append("**Records / outputs**")
            lines.append("")
            lines.extend([
                "- Control evidence, approval record, or log entry",
                "- Exception or escalation record if needed",
                "- Review note or attestation for the control cycle",
            ])
            lines.append("")
            lines.append("**Owner**")
            lines.append("")
            lines.append("- `[[CONTROL_OWNER]]`")
            lines.append("")
            lines.append("**Review cadence**")
            lines.append("")
            lines.append("- `[[REVIEW_FREQUENCY]]`")
            lines.append("")
    return "\n".join(lines)


def clean_text(value: str) -> str:
    """Make extracted PDF escape sequences readable without changing their meaning."""
    replacements = {
        "\\223": '"',
        "\\224": '"',
        "\\225": "'",
        "\\226": "–",
        "\\227": "—",
        "\\228": "…",
        "\\(": "(",
        "\\)": ")",
        "\\/": "/",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    value = re.sub(r"\b\d+F(?:\d+F)+\b", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def control_anchor(code: str) -> str:
    return "control-" + re.sub(r"[^a-z0-9]+", "-", code.lower()).strip("-")


def control_filename(code: str) -> str:
    return code.replace("(", "_").replace(")", "") + ".md"


def extract_original_fields(section: str):
    """Extract the Control, Discussion, and Related Controls portions of one source block."""
    control_marker = "Control:"
    discussion_marker = "Discussion:"
    related_marker = "Related Controls:"
    start = section.find(control_marker)
    if start < 0:
        return {"control": "", "discussion": "", "related_controls": ""}
    content = section[start + len(control_marker):]
    control, remainder = (content.split(discussion_marker, 1) + [""])[:2] if discussion_marker in content else (content, "")
    if remainder and related_marker in remainder:
        discussion, related = remainder.split(related_marker, 1)
    else:
        discussion, related = remainder, ""
    if "Control Enhancements:" in related:
        related = related.split("Control Enhancements:", 1)[0]
    return {
        "control": clean_text(control),
        "discussion": clean_text(discussion),
        "related_controls": clean_text(related),
    }


def parse_original_cjis(raw_text: str):
    """Parse the supplied CJIS v6.0 text extract into base and enhancement references."""
    raw_text = re.sub(r"\s+\d+\s+12/27/2024\s+CJISSECPOL v6\.0\s+", " ", raw_text)
    first = raw_text.find("AC-1 POLICY AND PROCEDURES")
    if first >= 0:
        second = raw_text.find("AC-1 POLICY AND PROCEDURES", first + 1)
        raw_text = raw_text[second if second >= 0 else first:]

    base_pattern = re.compile(
        r"(?P<code>[A-Z]{2}-\d+)\s+"
        r"(?P<title>[A-Z][A-Z0-9 /&(),|\\.\-]+?)\s+"
        r"(?P<markers>(?:\[(?:Existing|Priority \d)\]\s*)+)Control:\s*",
        re.S,
    )
    enhancement_pattern = re.compile(
        r"\\\((?P<number>\d+)\\\)\s+"
        r"(?P<title>[A-Z][A-Z0-9 /&(),|\\.\-]+?)\s+"
        r"(?P<markers>(?:\[(?:Existing|Priority \d)\]\s*)+)Control:\s*",
        re.S,
    )

    references = {}
    bases = list(base_pattern.finditer(raw_text))
    for index, base in enumerate(bases):
        end = bases[index + 1].start() if index + 1 < len(bases) else len(raw_text)
        block = raw_text[base.start():end]
        markers = base.group("markers").strip()
        reference = extract_original_fields(block)
        reference.update({
            "source_title": clean_text(base.group("title")),
            "markers": markers,
            "priority": re.search(r"Priority\s+(\d)", markers).group(1) if re.search(r"Priority\s+(\d)", markers) else "",
            "existing": "Existing" in markers,
        })
        references[base.group("code")] = reference

        enhancements = list(enhancement_pattern.finditer(block))
        for e_index, enhancement in enumerate(enhancements):
            e_end = enhancements[e_index + 1].start() if e_index + 1 < len(enhancements) else len(block)
            e_block = block[enhancement.start():e_end]
            e_markers = enhancement.group("markers").strip()
            e_reference = extract_original_fields(e_block)
            e_reference.update({
                "source_title": clean_text(enhancement.group("title")),
                "markers": e_markers,
                "priority": re.search(r"Priority\s+(\d)", e_markers).group(1) if re.search(r"Priority\s+(\d)", e_markers) else "",
                "existing": "Existing" in e_markers,
            })
            key = f"{base.group('code')}({enhancement.group('number')})"
            references[key] = e_reference
    return references


def related_codes(record, original):
    values = [record.get("related_controls", ""), original.get("related_controls", "")]
    found = []
    for value in values:
        for code in re.findall(r"\b[A-Z]{2}-\d+(?:\(\d+\))?\b", value):
            if code not in found and code != record["code"]:
                found.append(code)
    return found


def related_links(record, original, known_codes, master=False):
    links = []
    for code in related_codes(record, original):
        if code not in known_codes:
            links.append(f"`{code}`")
            continue
        if master:
            links.append(f"[{code}](#{control_anchor(code)})")
        else:
            links.append(f"[{code}](../control_documents/{control_filename(code)})")
    return ", ".join(links) if links else "None listed in the supplied control inventory."


def family_context(record):
    family = record["family"]
    owner, implementation, evidence, review = FAMILY_MATRIX.get(
        family,
        ("[[CONTROL_OWNER]]", "Implement the control using the approved standard.", "Approval, configuration, and review evidence", "Annual review"),
    )
    steps = FAMILY_PROCEDURES.get(family, [
        "Identify the requirement and the system or process in scope.",
        "Perform the approved action to implement or maintain the control.",
        "Verify the result and record the evidence.",
        "Escalate exceptions and review the control on the required cadence.",
    ])
    if "(" in record["code"]:
        parent = record["code"].split("(", 1)[0]
        steps = [
            f"Confirm that parent control {parent} is operating and identify the enhancement condition.",
            "Enable or perform the enhancement using the approved configuration or process.",
            "Test or observe the enhancement and document the result.",
            f"Update the {parent} evidence set and escalate any gap or exception.",
        ]
    return {"owner": owner, "implementation": implementation, "evidence": evidence, "review": review, "steps": steps}


def render_control(record, original, known_codes, master=False):
    code = clean_text(record["code"])
    title = clean_text(record["title"])
    family = clean_text(record["family"])
    context = family_context(record)
    source_found = bool(original)
    source_related = original.get("related_controls", "") if original else ""
    heading = "##" if master else "#"
    section_heading = "###" if master else "##"
    source_pdf_link = "CJIS_Security_Policy_v6-0_20241227%20(1)-1.pdf" if master else "../CJIS_Security_Policy_v6-0_20241227%20(1)-1.pdf"
    lines = [
        f'<a id="{control_anchor(code)}"></a>',
        f"{heading} {code} — {title}",
        "",
        f"**Control family:** {family}",
        "",
        f"{section_heading} Document control and cadence",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| Document ID | `CJIS-CTRL-{code}` |",
        "| Agency | `[[AGENCY_NAME]]` |",
        "| Version | `[[DOCUMENT_VERSION]]` |",
        "| Owner | `[[CONTROL_OWNER]]` |",
        "| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |",
        "| Effective date | `[[EFFECTIVE_DATE]]` |",
        "| Next review date | `[[NEXT_REVIEW_DATE]]` |",
        f"| Operating cadence | {clean_text(context['review'])} |",
        "| Policy review trigger | Annually and after a security incident, material change, assessment finding, or applicable legal/regulatory change. |",
        "",
        f"{section_heading} Policy & Purpose",
        "",
        f"This control document defines how `[[AGENCY_NAME]]` implements **{code} — {title}** for systems, personnel, services, and data within the CJIS scope.",
        "",
        f"{clean_text(record.get('what', ''))}",
        "",
        f"**Implementation objective:** {clean_text(record.get('recommendation', context['implementation']))}",
        "",
        f"{section_heading} Operational roles and responsibilities",
        "",
        "- **Control owner (`[[CONTROL_OWNER]]`):** Maintains the procedure, assigns work, reviews evidence, and accepts or escalates exceptions.",
        "- **CJIS Security Officer (`[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]`):** Interprets CJIS requirements, coordinates assessments, and verifies that evidence supports compliance.",
        "- **System owner / administrator (`[[SYSTEM_OWNER_NAME]]`):** Implements the technical or operational safeguards, records changes, and reports failures.",
        "- **Business and process owners:** Confirm mission need, approve access or process decisions, and validate that the control remains fit for purpose.",
        "- **Internal audit or independent assessor:** Samples operation, tests evidence, documents findings, and tracks remediation.",
        "- **All users and contractors:** Follow the approved procedure and immediately report suspected violations or control failures.",
        "",
        f"{section_heading} Step-by-step procedures workflow",
        "",
        "**Trigger / inputs**",
        "",
        f"A new system, user, vendor, change, incident, assessment finding, or scheduled review places **{code}** in scope. Use the approved requirement, current system record, risk decision, and prior evidence as inputs.",
        "",
        "**Procedure**",
        "",
    ]
    for index, step in enumerate(context["steps"], start=1):
        lines.append(f"{index}. {clean_text(step)}")
    lines.extend([
        f"{len(context['steps']) + 1}. Record the result, evidence location, reviewer, date, and any exception or remediation reference.",
        f"{len(context['steps']) + 2}. Escalate failures to `[[CONTROL_OWNER]]` and the CJIS Security Officer; do not close the workflow until the issue is remediated, accepted, or linked to an approved POA&M.",
        "",
        "**Workflow output**",
        "",
        "An approved implementation record, current evidence package, review sign-off, and an exception or remediation record when applicable.",
        "",
        f"{section_heading} Organizational action items",
        "",
        f"- [ ] Assign `[[CONTROL_OWNER]]` and a backup owner for {code}.",
        f"- [ ] Confirm the systems, facilities, personnel, vendors, and data flows covered by {code}.",
        "- [ ] Approve the agency-specific standard, procedure, configuration baseline, or form needed to operate the control.",
        "- [ ] Record the current implementation state, gap, risk level, and target completion date.",
        "- [ ] Test the control and attach the result to the evidence repository.",
        "- [ ] Schedule the recurring review and assign an accountable reviewer.",
        "- [ ] Track exceptions and corrective actions to closure or documented risk acceptance.",
        "",
        f"{section_heading} Audit evidence and continuous compliance artifacts",
        "",
        f"**Expected evidence:** {clean_text(context['evidence'])}.",
        "",
        "Maintain, as applicable:",
        "",
        "- Current policy, procedure, standard, or system security plan section.",
        "- Owner approval, implementation ticket, configuration export, or signed operational record.",
        "- Test, inspection, review, training, log, or monitoring evidence showing the control operated.",
        "- Recurring review sign-off with sample period, reviewer, date, result, and follow-up.",
        "- Exception, compensating-control, POA&M, incident, or risk-acceptance record.",
        "- Evidence retention location: `[[EVIDENCE_REPOSITORY_URL]]`; retain according to agency records requirements.",
        "",
        "**Continuous compliance measures**",
        "",
        "- Control status: Implemented / Partially implemented / Planned / Not applicable.",
        "- Evidence freshness: last collected date, next due date, and overdue indicator.",
        "- Exceptions: open count, aging, owner, target date, and residual risk.",
        "- Review result: pass, pass with findings, or fail, with a linked corrective action.",
        "",
        f"{section_heading} Original CJIS 6.0 control information (reference)",
        "",
        f"**Reference source:** [FBI CJIS Security Policy v6.0 (12/27/2024)]({source_pdf_link}), using the supplied local text extract for search and drafting. This section is a reference and does not replace the official policy or state CJIS authority direction.",
        "",
    ])
    if source_found:
        marker = original.get("markers", "") or "Not stated in extract"
        lines.extend([
            f"- **Source title:** {original.get('source_title', title)}",
            f"- **Source marking:** `{marker}`",
            "",
            "**Control**",
            "",
            f"> {original.get('control') or 'No control statement was extracted.'}",
            "",
            "**Discussion**",
            "",
            f"> {original.get('discussion') or 'No discussion text was extracted.'}",
            "",
            "**Related Controls in the source**",
            "",
            f"> {source_related or 'None listed.'}",
        ])
    else:
        lines.extend([
            "- **Reference status:** No matching control text was located in the supplied v6.0 text extract for this inventory item.",
            "- Validate the code, title, priority, control statement, discussion, and related controls against the official v6.0 PDF and the applicable state CJIS authority before approval.",
        ])
    lines.extend([
        "",
        f"{section_heading} Related controls",
        "",
        related_links(record, original or {}, known_codes, master=master),
        "",
        "**Implementation note:** Related controls should be reviewed together during planning, assessment, change review, and incident follow-up. Link evidence across documents rather than duplicating the same artifact.",
        "",
    ])
    return "\n".join(lines)


def build_master(records, family_order, grouped, originals):
    known_codes = {record["code"] for record in records}
    lines = [
        "# [[AGENCY_NAME]] CJIS Control Master Manual",
        "",
        "This master document consolidates the standalone control documents generated from the agency control inventory. Each control is also available as an individual file in [`control_documents`](control_documents/). Replace bracketed placeholders before approval.",
        "",
        "## Document control and cadence",
        "",
        "| Field | Value |",
        "| --- | --- |",
        "| Document ID | `CJIS-MASTER-001` |",
        "| Agency | `[[AGENCY_NAME]]` |",
        "| Version | `[[DOCUMENT_VERSION]]` |",
        "| Document owner | `[[CJIS_SECURITY_OFFICER_TITLE]] [[CJIS_SECURITY_OFFICER_NAME]]` |",
        "| Approver | `[[APPROVING_AUTHORITY_TITLE]] [[APPROVING_AUTHORITY_NAME]]` |",
        "| Effective date | `[[EFFECTIVE_DATE]]` |",
        "| Next review date | `[[NEXT_REVIEW_DATE]]` |",
        "| Review cadence | At least annually, and after a security incident, major system or vendor change, assessment finding, or applicable legal/regulatory change. |",
        "| Evidence repository | `[[EVIDENCE_REPOSITORY_URL]]` |",
        "",
        "## Policy & Purpose",
        "",
        "This manual establishes the operating model for implementing, maintaining, assessing, and evidencing the CJIS control inventory used by `[[AGENCY_NAME]]`. It supports the confidentiality, integrity, and availability of Criminal Justice Information and provides a repeatable package for agency oversight and CJIS assessment activities.",
        "",
        "The FBI CJIS Security Policy v6.0 is the reference baseline. Agency policy, state CJIS authority requirements, law, contract, or court order may impose more restrictive requirements; the more restrictive requirement applies.",
        "",
        "## Operational roles and responsibilities",
        "",
        "- **Agency approving authority:** Approves this manual, risk decisions, exceptions, and material changes.",
        "- **CJIS Security Officer:** Owns the compliance program, interprets requirements, coordinates training and assessments, and maintains the master evidence index.",
        "- **Control owners:** Operate assigned controls, maintain standalone documents, collect evidence, and remediate findings.",
        "- **System and service owners:** Implement technical safeguards, maintain system documentation, and report changes or failures.",
        "- **Human resources, procurement, legal, facilities, and records management:** Provide lifecycle records and approvals that support personnel, supplier, physical, contractual, and retention controls.",
        "- **Internal audit or independent assessor:** Performs risk-based testing and tracks findings to closure.",
        "",
        "## Step-by-step procedures workflow",
        "",
        "1. Identify the CJIS system, process, facility, person, supplier, or data flow in scope.",
        "2. Select the applicable control document and confirm the current CJIS v6.0 reference, agency policy, and state requirements.",
        "3. Assign an owner, define the implementation method, and record the risk and applicability decision.",
        "4. Implement or update the safeguard through the approved change, onboarding, procurement, incident, or operational workflow.",
        "5. Test or inspect operation, capture evidence, and obtain owner review and approval.",
        "6. Monitor the control on its defined cadence; investigate failures and link corrective action to the control record.",
        "7. Reassess after incidents, material changes, findings, or changes to law, policy, standards, or technology.",
        "8. Report status, aging exceptions, and residual risk to the appropriate governance forum.",
        "",
        "## Organizational action items",
        "",
        "- [ ] Replace all bracketed placeholders and approve the document-control fields.",
        "- [ ] Assign primary and backup owners for every control in the index.",
        "- [ ] Confirm scope and applicability for all CJIS systems, services, sites, personnel, and suppliers.",
        "- [ ] Validate each source reference against the official CJIS v6.0 PDF and current state CJIS authority guidance.",
        "- [ ] Populate implementation status, risk, evidence locations, review dates, and exception references.",
        "- [ ] Establish the evidence repository, retention schedule, review calendar, and escalation path.",
        "- [ ] Run an initial readiness review and track gaps in the agency POA&M or corrective-action system.",
        "",
        "## Audit evidence and continuous compliance artifacts",
        "",
        "Maintain a central evidence index that links each control to its owner, implementation record, current procedure, test result, recurring review, open exception, and corrective action. At minimum, the audit package should include the approved policy and master manual, control documents, system security plans, access and training records, logs and monitoring reports, change and maintenance records, incident and exercise records, vendor agreements, physical inspection records, backup/recovery tests, risk assessments, and assessment reports.",
        "",
        "Use recurring measures for evidence freshness, overdue reviews, control status, exception aging, remediation timeliness, and assessment findings. Protect the evidence from unauthorized alteration and retain it according to agency records requirements and applicable CJIS direction.",
        "",
        "## Original CJIS 6.0 control information (reference)",
        "",
        "The original reference content in each control section is derived from the supplied [CJIS Security Policy v6.0 PDF](CJIS_Security_Policy_v6-0_20241227%20(1)-1.pdf) and `_cjis_raw_extract.txt`. The official PDF and applicable state CJIS authority remain controlling. Inventory items without a matching extract are marked for validation in their individual documents.",
        "",
        "## Control index",
        "",
    ]
    for family in family_order:
        lines.append(f"### {clean_text(family)}")
        lines.append("")
        lines.append("| Control | Title | Standalone document | CJIS v6.0 reference |")
        lines.append("| --- | --- | --- | --- |")
        for record in grouped[family]:
            code = record["code"]
            original = originals.get(code, {})
            reference_status = "Matched" if original else "Validate"
            lines.append(f"| [{code}](#{control_anchor(code)}) | {clean_text(record['title'])} | [`{control_filename(code)}`](control_documents/{control_filename(code)}) | {reference_status} |")
        lines.append("")

    lines.append("## Standalone control records")
    lines.append("")
    for family in family_order:
        for record in grouped[family]:
            lines.append(render_control(record, originals.get(record["code"], {}), known_codes, master=True))
    return "\n".join(lines)


def main():
    source = SOURCE_PATH.read_text(encoding="utf-8")
    records = parse_records(source)
    family_order, grouped = group_records(records)
    MATRIX_PATH.write_text(build_matrix(records, family_order, grouped), encoding="utf-8")
    PROCEDURES_PATH.write_text(build_procedures(records, family_order, grouped), encoding="utf-8")
    originals = parse_original_cjis(RAW_PATH.read_text(encoding="utf-8", errors="replace")) if RAW_PATH.exists() else {}
    known_codes = {record["code"] for record in records}
    CONTROL_DOCS_PATH.mkdir(exist_ok=True)
    for record in records:
        path = CONTROL_DOCS_PATH / control_filename(record["code"])
        path.write_text(render_control(record, originals.get(record["code"], {}), known_codes), encoding="utf-8")
    MASTER_PATH.write_text(build_master(records, family_order, grouped, originals), encoding="utf-8")
    print(f"Wrote {MATRIX_PATH.name}, {PROCEDURES_PATH.name}, {MASTER_PATH.name}, and {len(records)} standalone control documents")
    print(f"controls={len(records)} families={len(family_order)} cjiss_v6_references={sum(1 for record in records if record['code'] in originals)}")


if __name__ == "__main__":
    main()
