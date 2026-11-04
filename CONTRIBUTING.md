# Contributing namespaces and schemas

This is a **shared schema registry for unrelated projects**. It is not a single project's codebase, and repository publicity does not confer ownership of other namespaces.

**Read `AGENTS.md` before editing.** Humans and AI agents follow the same process.

## 1. Claim a project slug first

The registry owner controls `registry/projects.json`. A project is reserved only after a maintainer-approved change records its unique slug, a short description and its GitHub maintainers. Agents cannot self-assign a slug or treat their repository's name as authorization.

Choose a neutral, stable, lowercase slug. **Never publish under a generic global namespace** like `common`, `default`, `core`, `official`, or `openxmlformats` unless the central maintainer expressly owns that space. Slug transfers and retirement require review.

Every change request must identify the project owner, its versioned target path, affected importers/consumers and any compatibility implications.

## 2. Paths and URL hierarchy

| Purpose | Repository path | Published URL |
| --- | --- | --- |
| XML namespace | `ns/<project>/<vocabulary>/v1.0.0/` | `https://pikaybh.github.io/schemas/ns/<project>/<vocabulary>/v1.0.0/` |
| Versioned XSD | `.../schema.xsd` | `.../schema.xsd` |
| Human-facing namespace documentation | `.../index.html` | `.../` |
| Generic schema family (future approved projects) | `formats/<project>/<family>/v1.0.0/` | `https://pikaybh.github.io/schemas/formats/<project>/<family>/v1.0.0/` |

Example *only*: `ns/example/widgets/v1.0.0/` is not a registered or published namespace.

- These locations are project- and vocabulary-scoped. Different projects may independently define the same local XML element name because **their namespace URIs differ**.
- The XML `targetNamespace` of `schema.xsd` must match the canonical namespace URI in `namespace.json` exactly. Avoid relying on runtime network lookup of the URI; publish supporting documents for humans and offline schemas for parsers.
- Never place a project-specific schema directly at the website root, under another project's tree, or under `openxmlformats/`.
- The historical `openxmlformats/` URL remains a readable informational landing page; **not** a normative namespace, despite its name. It is unrelated to Microsoft's `schemas.openxmlformats.org`.

## 3. Versioning and immutability

Use exact semantic-version directories `vMAJOR.MINOR.PATCH`. The URI and its bytes must remain available after a **stable** publication; no in-place schema edits, no repointing symlinks, no changing the meaning of existing elements, and no silent replacement of examples used as normative fixtures.

- **MAJOR:** breaking syntax or semantic contract.
- **MINOR:** compatible extension with new optional capabilities.
- **PATCH:** clarifications or compatible correction; publish at a *new* patch URI when it changes a schema or normative interpretation.
- Documentation errata that would affect published semantics require a new version; cosmetic edits may be proposed with explicit audit and maintainer approval.
- `draft` versions may be revised before release but must not be sold as stable; `stable` artifacts are immutable; `deprecated` points to a successor while the old URL remains accessible.
- Pin imports to exact published versions. Avoid `latest` or mutable `v1` aliases in machine-consumed schemas.

## 4. Version manifest contract

Every `ns/<project>/<vocabulary>/<version>/` requires a `namespace.json` record:

```json
{
  "project": "example",
  "vocabulary": "widgets",
  "version": "v1.0.0",
  "status": "draft",
  "maintainers": ["example-maintainer"],
  "description": "What this vocabulary means",
  "namespace_uri": "https://pikaybh.github.io/schemas/ns/example/widgets/v1.0.0/",
  "schema_file": null
}
```

- A `draft` may have `schema_file: null` while its vocabulary is under design; a `stable` XML version must supply a local `schema.xsd` and `index.html`.
- Maintain the project reservation separately in `registry/projects.json`; the manifest does **not** grant ownership.
- The `namespace_uri` is for identity. A schema URL (`namespace_uri` + `schema_file`) is a location for explicit validation, not an implicit XML Namespace requirement.
- A future non-XML format gets a format-specific manifest contract before publishing; do not force XSD rules onto JSON Schema or OpenAPI.

## 5. Reviews and isolation

- Work on a branch with one project/vocabulary/version per PR. **No direct pushes to main from agents.**
- Include owner/assigned agent, project/version, change type, external users, compatibility analysis, parser/validator evidence, and deployment URL expectations.
- Project owner reviews its scoped changes. Central maintainer must approve project registration, root/registry/navigation edits, shared conventions, namespace transfer and any changes affecting another project.
- Never rewrite other projects' published source to resolve an import issue. Instead propose upstream fixes or version-specific adapters.
- `.github/CODEOWNERS` expresses repository-wide review intent; GitHub does not enforce required reviews without the appropriate branch protection or rulesets. Treat this governance as **policy**, not a claim of machine-enforced access controls.

## 6. Local checks and publishing

Run `python3 scripts/validate_registry.py` (stdlib only) and your actual format-specific validators. Review `git diff` and preserve public links.

GitHub Pages publishes static `main` branch root content via `.nojekyll` and **branch deployment**, without custom Actions workflow files. GitHub can still use its internal Pages infrastructure. Do not enable/configure workflows or change Pages source for routine schema additions.

## 7. Security, licensing and standards claims

For XML: disable unsafe external entity resolution/DTD handling in consumers; do not introduce schema imports from untrusted mutable addresses. Never embed credentials or sensitive model data in examples. HTML must remain static (no arbitrary scripts or data collection).

The repository currently does not define a general open-source/open-specification license. **Public read access does not itself grant unrestricted reuse.** Maintainers must make an explicit license choice before representing the content as licensed for broad third-party redistribution or derivative works.

This project does **not** claim affiliation with or certification by Microsoft Office Open XML, `schemas.openxmlformats.org`, Ecma, ISO/IEC, W3C or buildingSMART. A public namespace is not proof of standardization or interoperability.
