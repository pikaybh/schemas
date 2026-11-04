# Agent policy — shared Schema Registry

**Canonical instructions for every AI or human coding agent in this repository.**
This repository is a **multi-project, multi-format schema registry**; it does not belong to BIXML, Xim, or any single product.
Read this file **before any write**, regardless of whether an agent was invoked through ChatGPT, Claude Code, Codex, Copilot, a terminal, or another tool.

## Authority and required reading
1. Owner's explicit task and existing GitHub issue/PR assignment (never infer ownership from intent).
2. This `AGENTS.md` for repo-wide safety; `CONTRIBUTING.md` for published path/version contracts.
3. `registry/projects.json` for reserved project slugs and maintainers; then the relevant `ns/<project>/` or `formats/<project>/` metadata and local instructions.
4. Actual repository state, commit, tests and Pages responses are evidence. A document or link is not proof of deployment or conformance.

If two rules conflict or no assignment/owner is recorded, **stop and report the conflict** rather than improvise.

## Isolation: independent projects must not interfere
- **One project = one owned slug and subtree.** Only edit `ns/<assigned-project>/...` and/or `formats/<assigned-project>/...` for which your task and registered project owner expressly permit edits.
- **Global shared files are maintainer-owned:** `README.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `index.html`, `registry/**`, `templates/**`, `scripts/**`, `.github/**`, `openxmlformats/**`, and top-level navigation pages. Contributors may *propose* global changes in a separate PR, but must not mix them with a project's schema release without explicit maintainer approval.
- An agent must not reserve a new project slug, claim another project's folder, rename/move/delete unrelated files, modify another project's schema, or perform cross-project bulk formatting.
- **Within one project**, coordinate mutually exclusive vocabulary/version path ownership through a linked issue/PR. Two agents must not write the same manifest or version concurrently; the later change rebases and revalidates.
- **Cross-project reuse** is by pinned versioned imports/references, not by copying or modifying someone else's published schema in place. No implicit unversioned cross-project dependency.
- Published namespace URIs and versioned content are permanent compatibility commitments. Never silently retarget, repurpose, or delete them. Deprecate in metadata; add a new version for a change.

## Publishing layout
- XML namespaces: `ns/<project>/<vocabulary>/v<major>.<minor>.<patch>/`.
- Other schema families, when approved: `formats/<project>/<family>/v<major>.<minor>.<patch>/` (e.g. JSON Schema, OpenAPI; do not invent a convention that conflicts with an existing family).
- `<project>` and `<vocabulary/family>` are lowercase ASCII slugs: `[a-z][a-z0-9-]*`, unique in their scope; no aliases or special reserved names (including `shared`, `common`, `default`, `core`) unless reserved by a maintainer.
- XML namespace URI example: `https://pikaybh.github.io/schemas/ns/example/widgets/v1.0.0/`. Files such as `schema.xsd` and `index.html` are published beneath that URL. The namespace URI is an **identifier**, not a requirement to perform network requests at runtime.
- Each published version has a `namespace.json` manifest with exact project/vocabulary/version, owner, status, canonical URI and schema filename. `registry/projects.json` is the explicit project reservation list.
- The older `/schemas/openxmlformats/` URL is a **legacy informational landing page**, not a shared project folder, a canonical vocabulary, or Microsoft's Office Open XML namespace. Preserve its route.

## Safe release and behavior
- Draft content must clearly be `draft`; do **not** call it an approved standard, W3C/ISO/Ecma/buildingSMART-compliant, safe, production-ready, or independently validated without evidence.
- Never publish credentials, private data, unreviewed third-party copyrighted material, secrets or active content that executes untrusted code. Prefer static HTML, JSON, XML, XSD and docs. Do not add GitHub Actions, Pages workflows, CI services, dynamic servers, or install dependencies without owner approval.
- Run `python3 scripts/validate_registry.py` and the appropriate local parser/schema checks. A passing local check does not prove cross-tool compatibility.
- Open a focused PR to `main`; **do not push directly to `main`, change Pages source, force-push, merge, alter permissions, or deploy externally** without explicit owner approval. Report actual commit SHA, changes, validation and unknowns.
- If a project needs new version semantics, package structure or a breaking contract, write down alternatives and seek a project owner/maintainer decision *before* changing published files.

## How to start work
1. Inspect `README.md`, this file, `CONTRIBUTING.md`, `registry/projects.json`, and relevant project manifests.
2. Check `git status` and the latest default branch SHA; preserve all existing work.
3. Confirm assignment's project slug, path ownership, version, review authority and intended status.
4. Make minimal path-scoped changes. Never edit another project's files to make your change compile.
5. Validate, review diff, submit PR, wait for required human decision.

**한국어 요약:** 이 저장소는 특정 프로젝트 전용이 아닙니다. Agent는 배정·등록된 프로젝트의 버전별 폴더만 수정하고, 공용 인덱스와 다른 프로젝트 파일은 침범하지 않습니다. 공개 버전/URI는 불변으로 취급하며, 변경은 새 버전으로 발행합니다. 새 프로젝트 등록과 공용 파일 수정은 저장소 관리자의 승인이 필요합니다. Actions 추가 금지.
