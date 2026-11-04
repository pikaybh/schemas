# Schemas — shared schema and namespace registry

**A neutral, public home for schema definitions used by multiple independent projects and AI/human contributors.**

- Public registry: https://pikaybh.github.io/schemas/
- XML namespaces: https://pikaybh.github.io/schemas/ns/
- Existing historical URL: https://pikaybh.github.io/schemas/openxmlformats/
- Source repository: https://github.com/pikaybh/schemas

This repository is **not owned by BIXML/Xim or any single project**. No production vocabulary, XML namespace, or third-party standard endorsement is implied merely by publishing a page.

## Before contributing

**All coding and AI Agents MUST read [AGENTS.md](AGENTS.md).**
Also read [CONTRIBUTING.md](CONTRIBUTING.md) for registration, naming, URL/version stability, release gates and interoperability requirements. Claude Code: [CLAUDE.md](CLAUDE.md); GitHub Copilot: [.github/copilot-instructions.md](.github/copilot-instructions.md). These short pointers defer to the same canonical rules.

- `registry/projects.json` is the owner-approved list of project slugs. **Currently no projects are registered**; create a maintainer-reviewed reservation before using a namespace.
- Project work is isolated under `ns/<project>/<vocabulary>/<version>/` for XML, or a separately approved `formats/<project>/<family>/<version>/` for other schema languages.
- Shared root files, registry, templates, generic landing pages and governance are maintainer-owned. One project does not have permission to change another project's content.
- Published stable version URIs are immutable. Publish a new version for behavioral or schema changes.
- Project owners review project content. Central maintainer approves reservations, global navigation, ownership transfers and other cross-project changes.
- Do not add custom GitHub Actions workflows. Static GitHub Pages deploys from `main` / `(root)` with `.nojekyll`.

## Suggested namespace layout

```text
ns/
  <project>/
    <vocabulary>/
      v1.0.0/
        namespace.json         # version, owner, URI, status
        index.html             # human-readable landing
        schema.xsd             # mandatory for stable XML releases
        examples/              # optional
```

Canonical namespace URI example (illustrative, **not yet published**):

```text
https://pikaybh.github.io/schemas/ns/example/widgets/v1.0.0/
```

See [the namespace layout](ns/README.md) and [manifest templates](templates/). Other schema formats may use [formats/](formats/) once their contracts are reviewed.

## What about /openxmlformats/?

The early `/schemas/openxmlformats/` link is preserved so existing bookmarks do not break. It is now an **unscoped informational compatibility landing page**. New project namespaces must **not** publish there. It is not associated with Microsoft's `schemas.openxmlformats.org` or Office Open XML.

## Validation

Run `python3 scripts/validate_registry.py` locally. This uses the Python standard library and checks registry ownership, project-scoped XML version paths, manifest URLs and published XSD `targetNamespace`. This is structural validation, not a substitute for project approval, semantic conformance, or independent interoperability testing.

## Status and licensing

This registry is in its **initial governance / incubation stage**, and has no approved production schemas yet. Publicly visible pages and filenames are not standards-body recognition. A general open-source/open-spec license has **not yet been selected**; do not assume broad reuse rights merely because the repository is public.

**한국어:** 여러 프로젝트가 공유하는 스키마 레지스트리입니다. 프로젝트 등록 후 본인 소유 폴더만 수정하며, 다른 프로젝트·공용 파일을 침범하지 않습니다. 공개한 버전은 변경하지 않고 새 버전으로 발행합니다. AI Agent는 작업 전에 루트 `AGENTS.md`를 필수로 확인해야 합니다.
