#!/usr/bin/env python3
"""Generate all stakeholder PDFs from HTML source files."""

import subprocess
import sys
import os

PRINT_DIR = "./print"
OUTPUT_DIR = "./stakeholder_pdfs"

DOCUMENTS = [
    {
        "html": "executive_summary.html",
        "pdf": "01_Executive_Summary.pdf",
        "title": "Executive Summary"
    },
    {
        "html": "business_case.html",
        "pdf": "02_Business_Case.pdf",
        "title": "Business Case"
    },
    {
        "html": "investor_brief.html",
        "pdf": "03_Investor_Brief.pdf",
        "title": "Investor Brief"
    },
    {
        "html": "financial_model.html",
        "pdf": "04_Financial_Model.pdf",
        "title": "Financial Model & Investment Analysis"
    },
    {
        "html": "government_brief.html",
        "pdf": "05_Government_Brief.pdf",
        "title": "Government Brief"
    },
    {
        "html": "white_paper.html",
        "pdf": "06_Technical_White_Paper.pdf",
        "title": "Technical White Paper"
    },
    {
        "html": "market_research.html",
        "pdf": "07_Market_Research.pdf",
        "title": "Market Research & Opportunity Analysis"
    },
    {
        "html": "risk_assessment.html",
        "pdf": "08_Risk_Assessment.pdf",
        "title": "Risk Assessment Matrix"
    },
    {
        "html": "technology_partners.html",
        "pdf": "09_Technology_Partner_Brief.pdf",
        "title": "Technology Partner Brief"
    },
    {
        "html": "community_brief.html",
        "pdf": "10_Community_Brief.pdf",
        "title": "Community Brief"
    },
]


def generate_pdf(html_filename, pdf_filename, title):
    html_path = os.path.join(PRINT_DIR, html_filename)
    pdf_path = os.path.join(OUTPUT_DIR, pdf_filename)

    if not os.path.exists(html_path):
        print(f"  [SKIP] {html_filename} — file not found")
        return False

    print(f"  Generating: {pdf_filename} ...", end="", flush=True)
    try:
        result = subprocess.run(
            ["python3", "-m", "weasyprint", html_path, pdf_path],
            capture_output=True,
            text=True,
            timeout=120
        )
        if result.returncode == 0:
            size = os.path.getsize(pdf_path)
            print(f" OK ({size/1024:.0f} KB)")
            return True
        else:
            # weasyprint often exits 0 even with warnings; check file
            if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
                size = os.path.getsize(pdf_path)
                print(f" OK with warnings ({size/1024:.0f} KB)")
                return True
            print(f" FAILED")
            print(f"    stderr: {result.stderr[:300]}")
            return False
    except subprocess.TimeoutExpired:
        print(f" TIMEOUT")
        return False
    except Exception as e:
        print(f" ERROR: {e}")
        return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\nGenerating {len(DOCUMENTS)} stakeholder PDF documents...")
    print(f"Source: {PRINT_DIR}")
    print(f"Output: {OUTPUT_DIR}\n")

    success = 0
    failed = 0

    for doc in DOCUMENTS:
        result = generate_pdf(doc["html"], doc["pdf"], doc["title"])
        if result:
            success += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print(f"Complete: {success} PDFs generated, {failed} failed")
    print(f"Output directory: {OUTPUT_DIR}")

    if success > 0:
        print("\nGenerated files:")
        for f in sorted(os.listdir(OUTPUT_DIR)):
            if f.endswith(".pdf"):
                size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
                print(f"  {f} ({size/1024:.0f} KB)")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
