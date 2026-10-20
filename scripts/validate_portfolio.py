#!/usr/bin/env python3
"""Validate selected portfolio evidence using Python's standard library."""
import csv
import json
import math
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
failures = []
checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        failures.append(message)

def equal(a, b):
    return math.isclose(float(a), float(b), rel_tol=1e-9, abs_tol=1e-9)

def rows(path):
    with (ROOT / path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def main():
    registry = json.loads((ROOT / "evidence/metric_register.json").read_text())
    datasets = registry["datasets"]
    for data in datasets:
        records = rows(data["source"])
        check(len(records) == data["rows"], f"Row count: {data['source']}")
        check(records[0]["Week"] == data["first_period"], f"First period: {data['source']}")
        check(records[-1]["Week"] == data["last_period"], f"Last period: {data['source']}")
        check([r["Week"] for r in records] == [f"W{i}" for i in range(1, len(records)+1)],
              f"Missing or duplicate week: {data['source']}")
        for metric in data["metrics"]:
            field = metric["field"]
            check(equal(records[0][field], metric["baseline"]), f"Baseline: {field}")
            check(equal(records[-1][field], metric["latest"]), f"Latest: {field}")
            for record in records:
                value = float(record[field])
                check(math.isfinite(value), f"Nonfinite value: {field}")
                if ("%" in field or field.endswith("_Pct")) and field != "Marketing ROI %":
                    limit = 100 if data["percentage_storage"] == "percentage_points" else 1
                    check(0 <= value <= limit, f"Rate range/unit: {field} {record['Week']}")

    marketing = rows(datasets[3]["source"])
    for record in marketing:
        spend, revenue = float(record["Marketing Spend"]), float(record["Attributed Revenue"])
        check(spend > 0, "Marketing spend must be positive")
        check(equal((revenue-spend)/spend, record["Marketing ROI %"]), "Marketing return reconciliation")
        check(equal(revenue/spend, record["ROAS"]), "ROAS reconciliation")

    for record in rows(datasets[4]["source"]):
        otif, otd, full = (float(record[k]) for k in ("OTIF %", "OTD %", "In-Full %"))
        check(max(0, otd+full-1)-1e-9 <= otif <= min(otd, full)+1e-9,
              f"Invalid OTIF intersection: {record['Week']}")

    readme = (ROOT / "README.md").read_text()
    headline = {}
    for line in readme.splitlines():
        if line.startswith("|"):
            cells = [v.strip() for v in line.strip("|").split("|")]
            if len(cells) == 5:
                headline[(cells[0], cells[1])] = cells[3]
    expected = {
        ("Retail", "Labor cost / sales"): "16.7%",
        ("Retail", "NPS"): "67",
        ("Retail", "Average wait"): "5.3 min",
        ("Retail", "Schedule adherence"): "91%",
        ("Retail", "Task completion"): "95%",
        ("CRM", "Active-user adoption"): "93%",
        ("CRM", "UAT pass rate"): "97%",
        ("Onboarding", "14-day activation"): "87%",
        ("Onboarding", "Median time-to-value"): "9 days",
        ("Marketing", "Revenue-based marketing return"): "228%",
        ("Marketing", "ROAS"): "3.28x",
        ("Supply chain", "OTIF"): "95%",
        ("People operations", "90-day retention"): "95%",
    }
    for key, value in expected.items():
        check(headline.get(key) == value, f"README headline: {key}")
    brief = ROOT / datasets[3]["project"] / "01_Executive_Brief.md"
    check("ROI 228%" in brief.read_text() and "ROI 201%" not in brief.read_text(),
          "Marketing executive brief reconciliation")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0]
            if not target or re.match(r"[a-zA-Z]+:", target):
                continue
            resolved = (path.parent / unquote(target)).resolve()
            check(resolved.is_relative_to(ROOT) and resolved.exists(),
                  f"Missing local link: {path.relative_to(ROOT)} -> {target}")
    if failures:
        print("\n".join("FAIL: " + value for value in failures))
        return 1
    print(f"PASS: {checks} checks; 6 datasets; 43 registered metrics; 13 README endpoints.")
    print("Scope: source/register consistency, rate units, marketing math, OTIF bounds, and local file links.")
    print("Not tested: real business outcomes, spreadsheet recalculation/rendering, external URLs, Markdown anchors.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, IndexError) as exc:
        print(f"FAIL: Invalid or missing evidence: {exc}", file=sys.stderr)
        sys.exit(1)
