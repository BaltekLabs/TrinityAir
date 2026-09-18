#!/usr/bin/env python3
"""Fail fast on stale claims, exposed diligence paths, and broken local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_HTML = [ROOT / "index.html", ROOT / "booking_app.html", ROOT / "404.html"]
REQUIRED_FILES = [
    ROOT / "index.html",
    ROOT / "booking_app.html",
    ROOT / "404.html",
    ROOT / "robots.txt",
    ROOT / "sitemap.xml",
    ROOT / "favicon.svg",
    ROOT / "data/site-facts.json",
]
PROHIBITED_PATHS = [
    ROOT / "stakeholder_pdfs",
    ROOT / "docs/hub_docs",
    ROOT / "js/gate.js",
    ROOT / "outreach.md",
    ROOT / "prep_sheet.txt",
]
PROHIBITED_PATTERNS = {
    "confidential-label": re.compile(r"\bconfidential\b", re.I),
    "fake-client-gate": re.compile(r"gate\.js|restricted access", re.I),
    "underway-claim": re.compile(r"phase\s*1[^\n<]{0,90}underway|underway\s+now", re.I),
    "first-mover-claim": re.compile(r"first[- ]mover", re.I),
    "unsupported-traffic-claim": re.compile(r"15\s*[–-]\s*25\s*%", re.I),
    "wrong-economy-rank": re.compile(r"3(?:rd|d)\s+largest.{0,25}metro\s+economy", re.I),
    "pid20-claim": re.compile(r"PID\s*20", re.I),
    "public-return-claim": re.compile(r"\b(?:IRR|NPV)\b", re.I),
}
DEMO_PROHIBITED_PATTERNS = {
    "live-booking-action": re.compile(r"confirm\s+booking|reserve\s+now|buy\s+(?:a\s+)?ticket", re.I),
    "real-payment-field": re.compile(r'type=[\"\'](?:email|password)[\"\']|autocomplete=[\"\']cc-|name=[\"\'][^\"\']*card', re.I),
    "checkout-network-call": re.compile(r"\bfetch\s*\(|XMLHttpRequest|sendBeacon\s*\(", re.I),
    "checkout-form-submit": re.compile(r"<form\b|formaction\s*=", re.I),
}
ATTR_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.I)


def local_target(value: str) -> Path | None:
    value = value.strip()
    if not value or value.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        return None
    clean = unquote(parsed.path)
    if not clean or clean == "/":
        return ROOT / "index.html"
    return ROOT / clean.lstrip("/")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    for path in PROHIBITED_PATHS:
        if path.exists():
            errors.append(f"restricted public path exists: {path.relative_to(ROOT)}")

    facts_path = ROOT / "data/site-facts.json"
    if facts_path.is_file():
        try:
            facts = json.loads(facts_path.read_text(encoding="utf-8"))
            if facts.get("project", {}).get("phase") != "Phase 0 - validation and site control":
                errors.append("site-facts project phase is not the approved public phase")
            for field in ("site_control_confirmed", "operator_commitment_confirmed", "faa_operating_authority_confirmed"):
                if facts.get("project", {}).get(field) is not False:
                    errors.append(f"site-facts {field} must remain false until evidence review")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid data/site-facts.json: {exc}")

    for path in PUBLIC_HTML:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if path.name == "index.html":
            for required in ('<meta name="description"', '<link rel="canonical"', 'Phase 0'):
                if required not in text:
                    errors.append(f"index.html missing required marker: {required}")
        if path.name == "booking_app.html":
            for required in (
                '<meta name="robots" content="noindex,follow">',
                "Interactive concept only.",
                "not a live booking service",
                "no affiliation or service commitment is implied",
                'data-demo-step="payment"',
                'id="tracking-map"',
                "Complete simulated purchase",
                "No charge will be made.",
            ):
                if required not in text:
                    errors.append(f"booking_app.html missing required demo disclosure: {required}")
            for label, pattern in DEMO_PROHIBITED_PATTERNS.items():
                if pattern.search(text):
                    errors.append(f"booking_app.html contains prohibited {label}")
        for label, pattern in PROHIBITED_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.name} contains prohibited {label}")
        for value in ATTR_RE.findall(text):
            target = local_target(value)
            if target is not None and not target.exists():
                errors.append(f"{path.name} has broken local reference: {value}")

    if errors:
        print("Site validation failed:")
        for error in sorted(set(errors)):
            print(f"- {error}")
        return 1

    print("Site validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
