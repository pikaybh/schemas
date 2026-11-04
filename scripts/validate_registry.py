#!/usr/bin/env python3
"""Validate the shared namespace registry layout with only Python stdlib.

Does not modify files or access the network. Policy-level ownership and
published-version immutability also require human PR review.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SLUG = re.compile(r"^[a-z][a-z0-9-]*$")
VERSION = re.compile(r"^v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
BASE_URL = "https://pikaybh.github.io/schemas/ns/"
RESERVED = {"common", "core", "default", "official", "shared", "openxmlformats"}
STATUSES = {"draft", "stable", "deprecated"}


def report_error(errors: list[str], message: str) -> None:
    errors.append(message)


def read_json(path: Path, errors: list[str]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError, ValueError) as exc:
        report_error(errors, f"{path}: invalid or missing JSON: {exc}")
        return None


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    reg = read_json(root / "registry/projects.json", errors)
    if not isinstance(reg, dict):
        return errors
    if reg.get("registryVersion") != 1 or not isinstance(reg.get("projects"), list):
        report_error(errors, "registry/projects.json: require registryVersion=1 and projects array")
        return errors

    projects: dict[str, list[str]] = {}
    for i, project in enumerate(reg["projects"]):
        label = f"registry/projects.json: projects[{i}]"
        if not isinstance(project, dict):
            report_error(errors, f"{label}: object required")
            continue
        slug = project.get("slug")
        maintainers = project.get("maintainers")
        if not isinstance(slug, str) or not SLUG.fullmatch(slug) or slug in RESERVED:
            report_error(errors, f"{label}: invalid or reserved slug: {slug!r}")
            continue
        if slug in projects:
            report_error(errors, f"{label}: duplicate project slug: {slug}")
        if (not isinstance(maintainers, list) or not maintainers
                or any(not isinstance(x, str) or not x.strip() for x in maintainers)
                or len(maintainers) != len(set(maintainers))):
            report_error(errors, f"{label}: maintainers must be unique nonempty GitHub IDs")
            continue
        if not isinstance(project.get("description"), str) or not project["description"].strip():
            report_error(errors, f"{label}: missing description")
        projects[slug] = maintainers

    ns_root = root / "ns"
    seen_uris: set[str] = set()
    if not ns_root.exists():
        report_error(errors, "ns/: missing namespace root")
        return errors
    for project_dir in sorted(x for x in ns_root.iterdir() if x.is_dir()):
        project = project_dir.name
        if project not in projects:
            report_error(errors, f"{project_dir}: unregistered project; request a maintainer-owned registry reservation")
            continue
        for vocabulary_dir in sorted(x for x in project_dir.iterdir() if x.is_dir()):
            vocabulary = vocabulary_dir.name
            if not SLUG.fullmatch(vocabulary) or vocabulary in RESERVED:
                report_error(errors, f"{vocabulary_dir}: invalid vocabulary slug")
                continue
            for version_dir in sorted(x for x in vocabulary_dir.iterdir() if x.is_dir()):
                version = version_dir.name
                if not VERSION.fullmatch(version):
                    report_error(errors, f"{version_dir}: version must be vMAJOR.MINOR.PATCH")
                    continue
                manifest = read_json(version_dir / "namespace.json", errors)
                if not isinstance(manifest, dict):
                    continue
                expected = BASE_URL + f"{project}/{vocabulary}/{version}/"
                label = str(version_dir / "namespace.json")
                for field, expected_value in (
                    ("project", project), ("vocabulary", vocabulary),
                    ("version", version), ("namespace_uri", expected)
                ):
                    if manifest.get(field) != expected_value:
                        report_error(errors, f"{label}: {field} must be {expected_value!r}")
                if expected in seen_uris:
                    report_error(errors, f"{label}: duplicated canonical URI: {expected}")
                seen_uris.add(expected)
                status = manifest.get("status")
                if status not in STATUSES:
                    report_error(errors, f"{label}: status must be one of {sorted(STATUSES)}")
                authors = manifest.get("maintainers")
                if (not isinstance(authors, list) or not authors
                        or any(not isinstance(x, str) or x not in projects[project] for x in authors)):
                    report_error(errors, f"{label}: maintainers must be registered project maintainers")
                if not isinstance(manifest.get("description"), str) or not manifest["description"].strip():
                    report_error(errors, f"{label}: nonempty description required")
                schema_file = manifest.get("schema_file")
                if schema_file is not None:
                    if schema_file != "schema.xsd":
                        report_error(errors, f"{label}: schema_file must be 'schema.xsd' or null")
                    else:
                        xsd_path = version_dir / schema_file
                        if not xsd_path.is_file():
                            report_error(errors, f"{xsd_path}: referenced schema does not exist")
                        else:
                            try:
                                raw = xsd_path.read_text(encoding="utf-8")
                                if "<!DOCTYPE" in raw.upper() or "<!ENTITY" in raw.upper():
                                    report_error(errors, f"{xsd_path}: DTD/entity declarations forbidden")
                                parsed = ET.fromstring(raw)
                                if parsed.tag != "{http://www.w3.org/2001/XMLSchema}schema":
                                    report_error(errors, f"{xsd_path}: root must be xs:schema")
                                if parsed.get("targetNamespace") != expected:
                                    report_error(errors, f"{xsd_path}: targetNamespace must be {expected}")
                            except (OSError, UnicodeError, ET.ParseError) as exc:
                                report_error(errors, f"{xsd_path}: XML parse failed: {exc}")
                if status in ("stable", "deprecated"):
                    if schema_file is None:
                        report_error(errors, f"{label}: released XML namespace requires schema.xsd")
                    if not (version_dir / "index.html").is_file():
                        report_error(errors, f"{version_dir}: released namespace requires index.html")

    for family_root in [root / "formats"]:
        if family_root.exists():
            for project_dir in sorted(x for x in family_root.iterdir() if x.is_dir()):
                if project_dir.name not in projects:
                    report_error(errors, f"{project_dir}: unregistered project; obtain reservation before publishing")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        print(f"Registry validation failed: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print("PASS: registry ownership, paths, versions and published XML schema references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
