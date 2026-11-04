# XML namespaces

This directory hosts **project-scoped, versioned XML namespaces for any approved project**, not only BIM.

Canonical layout:

```text
ns/
  <project-slug>/
    <vocabulary-slug>/
      v1.0.0/
        namespace.json
        index.html
        schema.xsd             # required once stable
        examples/              # optional versioned samples
```

The canonical namespace URI is:

```text
https://pikaybh.github.io/schemas/ns/<project-slug>/<vocabulary-slug>/v1.0.0/
```

**Registration and owner reservation:** [`registry/projects.json`](../registry/projects.json) (central maintainer-controlled).

**Mandatory agent instructions:** [`AGENTS.md`](../AGENTS.md).

**Contribution process and versioning:** [`CONTRIBUTING.md`](../CONTRIBUTING.md).

No released namespaces are registered yet. The legacy [`/schemas/openxmlformats/`](../openxmlformats/) page is informational and is **not** a namespace to publish under.

Do not assume that a namespace URI being dereferenceable implies a consumer must fetch it over a network.
