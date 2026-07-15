# cjis-compliance

This workspace contains a CJIS policy template, a control inventory, family-level companion documents, a master control manual, and one standalone Markdown document for every control or enhancement in the inventory.

## Rebuild Flow

The rebuild process is intentionally simple:

1. Start with [`CJIS_Control_Item_Templates.md`](CJIS_Control_Item_Templates.md).
2. Parse the control families, control codes, titles, explanations, recommendations, and relationships from that file.
3. Use the supplied [`_cjis_raw_extract.txt`](_cjis_raw_extract.txt) to attach CJIS v6.0 reference text when a matching source control is present.
4. Regenerate [`CJIS_Control_Implementation_Matrix.md`](CJIS_Control_Implementation_Matrix.md), [`CJIS_Operating_Procedures.md`](CJIS_Operating_Procedures.md), [`CJIS_Control_Master_Manual.md`](CJIS_Control_Master_Manual.md), and the files under [`control_documents`](control_documents/).

The expanded rebuild path is [`generate_cjis_docs.py`](generate_cjis_docs.py). The Rust source [`generate_cjis_docs.rs`](generate_cjis_docs.rs) remains available for the earlier matrix and operating-procedure generation flow.

## Notes

- The rebuild uses the control template as the source of truth.
- The generated documents stay aligned because both come from the same parsed control list.
- Every generated control document includes document control and cadence, policy and purpose, roles, workflow, organizational action items, evidence and continuous-compliance artifacts, CJIS v6.0 reference information, and related controls.
- Inventory items that do not match the supplied CJIS v6.0 extract are marked for validation against the official PDF before approval.
- The placeholder values remain editable so each agency can personalize the package quickly.
