## Change ownership

- Project slug (or **maintainer-owned global change**):
- Registered maintainer / requesting owner:
- Assigned paths (one project/vocabulary/version per PR):
- Version and status (`draft` / `stable` / `deprecated`):
- Linked discussion / issue and explicit cross-project approvals, if applicable:

## Compatibility and publication

- Does this change an already-published URI, schema, namespace semantics, or examples used as normative fixtures? If yes, explain the **new version** instead of overwriting.
- Existing consumers, pinned imported namespace versions, and migration plan:
- Canonical namespace URL and XSD `targetNamespace` (for XML):
- Are any unrelated projects, central registry files, or shared landing pages affected? Why was central approval obtained?

## Checks

- [ ] Read root `AGENTS.md` and `CONTRIBUTING.md`.
- [ ] Confirmed project slug reserved in `registry/projects.json` (or this is an owner-approved reservation PR).
- [ ] No changes outside the assigned project scope without explicit approval.
- [ ] Ran `python3 scripts/validate_registry.py` and checked output.
- [ ] Ran applicable XML/JSON/other schema parsers and included evidence.
- [ ] No custom Actions workflows, secrets, sensitive fixtures, or unsupported standardization claims.
- [ ] Published URLs and existing versioned artifacts remain stable.

## Results / unknowns

- Commit SHA:
- Tests and expected Pages URL:
- Known unsupported behaviors, risks, or limitations:
