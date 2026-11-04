# Registry contribution templates

Templates are **examples, not published schemas or reserved project names**.

- `project-registration.json` describes an entry for `registry/projects.json`. Only a maintainer-approved registry change reserves a project slug.
- `namespace.json` is a draft XML namespace version manifest. Copy it into your assigned `ns/<registered-project>/<vocabulary>/vMAJOR.MINOR.PATCH/namespace.json` and replace **all** placeholder values.
- Add a human-readable `index.html` and matching `schema.xsd` for stable XML releases.
- Use exact canonical URLs. Do not publish files in `templates/` as a production namespace.
- See [`AGENTS.md`](../AGENTS.md) and [`CONTRIBUTING.md`](../CONTRIBUTING.md).
