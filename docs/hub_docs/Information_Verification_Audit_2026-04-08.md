# Trinity Air Link / HUB Information Verification Audit
**Date:** April 8, 2026  
**Reviewer:** Codex (repository + targeted external source verification)

## 1) Scope Reviewed
This review covered major public-facing and stakeholder-facing materials with emphasis on financial claims, numbers, and externally verifiable statements.

### Repository materials reviewed
- `index.html` (primary public webpage)
- `outreach.md`
- `docs/hub_docs/PROJECT_STATUS.md`
- `docs/hub_docs/Market_Data_Reference_2026.md`
- `docs/hub_docs/HUB_Executive_Summary.md`
- `docs/hub_docs/HUB_Financial_Model.md`
- `print/executive_summary.html`
- `print/government_brief.html`
- `print/investor_brief.html`
- `print/financial_model.html`

### External verification sources reviewed (targeted)
- FAA eIPP announcement + fact sheet
- U.S. DOT briefing post about eIPP selections
- FAA AAM / Air Taxis page
- Archer investor releases
- Joby filings / investor materials (high-level check)

---

## 2) Executive Findings (High Priority)

### A. One major factual contradiction found (must fix)
**Claim repeated in multiple docs:** eIPP allows revenue passenger operations before full type certification.

**Finding:** FAA eIPP fact sheet states the opposite: eIPP is not a mechanism to bypass certification; aircraft must already be in type certification process.

**Impact:** High legal/regulatory credibility risk in government and investor outreach.

**Action:** Replace all “pre-certification revenue ops allowed” wording with compliant wording (e.g., “eIPP accelerates operational learning and regulatory coordination while certification requirements remain in force”).

---

### B. Internal data inconsistency across docs/pages (must normalize)
The same core metrics appear with materially different values:

- **DFW population:** 8.3–8.5M, 8.5M, 8.7M (different docs)
- **DFW GDP:** $640B+, $710B+, and other variants
- **Traffic delay hours:** 74M (one file) vs 174M (others)
- **Break-even year labels:** Year 5 shown as 2030 in some places and 2031 in others

**Impact:** Undermines trust during diligence and makes numbers appear ungoverned.

**Action:** Create a single canonical metrics table and reference it everywhere.

---

### C. Financial realism concerns (important for investor-grade materials)
Current model can be presented as a directional scenario model, but several assumptions are aggressive and need tighter framing:

1. **Personnel cost realism vs headcount**
   - Financial docs indicate **800+ permanent jobs** while Year 5 personnel line is **$32.5M**.
   - This implies very low loaded cost per worker if interpreted literally.
   - Recommendation: separate direct payroll vs induced jobs, and disclose direct FTE assumptions by function.

2. **eVTOL unit economics**
   - Uses ~$1.3M per aircraft as if deployable acquisition cost in project CAPEX.
   - This appears closer to manufacturing-cost signaling than market-ready delivered cost for operator procurement.
   - Recommendation: use scenario bands for lease/purchase structures with explicit source notes.

3. **Demand and utilization assumptions**
   - Moderate case implies ~1,500 eVTOL passenger seats/day and ~7,500 AV passenger trips/day equivalent at assumed occupancies.
   - These are possible but require clear adoption ramp assumptions, route density, and load-factor evidence.
   - Recommendation: add ramp curve (Years 1–5) and sensitivity by load factor, utilization, and fare.

4. **Returns presentation style**
   - IRR, NPV, EBITDA margins are currently shown as point estimates in public-facing collateral.
   - Recommendation: show base + downside + upside with transparent assumptions and caveat confidence level.

---

## 3) What Appears Directionally Solid
- The existence of an eIPP program and March 2026 selected projects is supported by FAA/DOT materials.
- Texas participation and Archer linkage appear directionally supported.
- Project structure (phased build + diversified revenue streams) is coherent as a concept deck framework.

---

## 4) File-Level Issues Observed

### `docs/hub_docs/Market_Data_Reference_2026.md`
- Strongest source index among project docs.
- Contains the most useful “outdated number correction” notes.
- Still includes the problematic statement that eIPP enables revenue ops before full certification.

### `docs/hub_docs/PROJECT_STATUS.md`
- Good project narrative, but mixes verified facts with high-confidence forward claims.
- Includes claims that should be labeled as assumptions/projections rather than facts.

### `docs/hub_docs/HUB_Executive_Summary.md`
- Investor/government-ready tone is strong.
- Contains a few hard claims that should be softened or sourced more directly (especially regulatory and near-term operations timing claims).

### `docs/hub_docs/HUB_Financial_Model.md`
- Comprehensive structure and scenario math framework.
- Needs assumption governance note and explicit realism bounds for fleet economics, staffing, and adoption ramp.

### `print/*.html` (Executive, Government, Investor, Financial)
- Visually strong and consistent branding.
- Repeats inconsistent metrics and some overconfident regulatory wording.
- Requires one pass for data harmonization and legal-safe phrasing.

### `index.html`
- Strong narrative and CTAs.
- “Sources & Methods” section references internal docs but not enough direct external citations for sensitive claims.
- Should move from “internal-source linked claims” to explicit external references for major stats.

---

## 5) Recommended Remediation Plan

### Priority 0 (Immediate, before external outreach)
1. Remove/replace all wording that implies certification bypass via eIPP.
2. Freeze one canonical number set for:
   - DFW population
   - DFW GDP
   - congestion hours/cost
   - break-even year and timeline labels

### Priority 1 (Investor/government credibility)
3. Publish a one-page **Assumptions Register** with source/date/owner for every headline KPI.
4. Split **direct jobs vs induced jobs** and align payroll math with staffing assumptions.
5. Reframe returns as scenario ranges with confidence language.

### Priority 2 (Website/document governance)
6. Add externally linked citations in `index.html` for each major stat and regulatory claim.
7. Add “Last verified date” + “next review date” to all print collateral.
8. Set quarterly data refresh cadence and change-log.

---

## 6) Suggested Disclosure Language (Use Immediately)
To keep momentum while reducing risk:

> “All financial projections are scenario-based estimates for planning and partner discussions. Final outcomes depend on certification timelines, market adoption, partner agreements, and financing terms.”

> “eIPP participation supports operational planning and regulatory coordination; all flight operations remain subject to FAA certification and safety requirements.”

---

## 7) Bottom Line
The project narrative is compelling and the materials are well developed, but current collateral mixes strong strategy with a few high-risk factual/regulatory statements and inconsistent headline numbers. Correcting those items will materially improve investor and government confidence.
