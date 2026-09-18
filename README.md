# Trinity Air Link public site

This repository publishes the public website at [trinityair.link](https://trinityair.link/).

## Project status

Trinity Air Link is in **Phase 0: validation and site control**. The T&P Warehouse at 401 W Lancaster Avenue is a preferred site under evaluation; the project does not publicly represent that it controls the site, holds FAA operating authority, has operator commitments, or is conducting a public securities offering.

## Public-content policy

This repository is public. It must contain only material approved for unrestricted release.

Do not commit:

- financial models, investor memoranda, securities-return projections, or investor pricing tools;
- contact databases, outreach plans, direct personal contact details, or email drafts;
- property negotiations, lease terms, title material, diligence reports, or legal work product;
- passwords, hashes used as access gates, API keys, secrets, or private data-room links;
- claims of partnerships, approvals, funding, site control, or project status without current evidence.

Private diligence belongs in a server-authenticated data room or private repository. Client-side JavaScript is not access control.

The public interactive concept demo is permitted only while it remains unmistakably
simulated. It may demonstrate the full customer funnel—route planning, traveler
options, checkout, pass confirmation, and trip tracking—but it must contain no
live-booking language, real form submission, personal or payment-data collection,
networked checkout, or implied operator affiliation. Routes, times, availability,
vehicles, and prices must remain persistently labeled as illustrative.

## Source of truth

Approved public facts live in [`data/site-facts.json`](data/site-facts.json). Every quantitative or status claim needs a source, verification date, and owner before publication.

## Local validation

Run:

```bash
python scripts/check_site.py
```

The checker validates local links, required metadata, withdrawn path controls, and prohibited stale claims. GitHub Actions runs the same check on pull requests and changes to `main`.

## Deployment

The site is plain static HTML. `index.html` is the only indexed public content
page. `booking_app.html` is a public, noindex interactive concept experience.
Legacy URLs show a withdrawal notice and are marked `noindex`.

## Release checklist

1. Update facts and sources in `data/site-facts.json`.
2. Run `python scripts/check_site.py`.
3. Review all external claims and relationship language.
4. Confirm email routing and domain authentication.
5. Open a pull request and wait for checks before merging.

## Historical-material warning

Removing files from the current branch does not remove them from Git history. Repository visibility or a coordinated history rewrite is required before treating any previously committed material as confidential.
