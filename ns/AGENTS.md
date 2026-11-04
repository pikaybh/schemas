# XML namespace subtree agent rules

Inherit and obey [root AGENTS.md](../AGENTS.md) and [CONTRIBUTING.md](../CONTRIBUTING.md).

For `ns/<project>/<vocabulary>/<version>/` edits:
- Verify `<project>` is already reserved in `registry/projects.json` and your task is explicitly authorized by that project's maintainer.
- Do not edit sibling projects, other vocabularies, or version directories outside your assignment.
- Match `schema.xsd` `targetNamespace` to the manifest's canonical `namespace_uri` exactly.
- Do not change already released/stable versioned bytes; publish a new version and migration note.
- Coordinate concurrent agents to avoid overlapping version path writes.
- Do not modify the website root or registry index in the same project-scoped PR without central approval.
- Do not introduce Actions workflows or assert an international-standard endorsement.
