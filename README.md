# Data Center Water Audit

A source-backed reconstruction of the widely circulated claim that U.S. data centers used about **228 billion gallons of water in 2023**, plus a practical framework for evaluating what that number does—and does not—say about a specific project.

This repository separates the readable essay from the evidence and reproducible arithmetic. It is designed so a reader can check the assumptions instead of trusting the author’s summary.

## Start here

- **Live reading edition:** `index.html`
- **Article PDF:** `article/About_That_228_Billion_Gallons.pdf`
- **Evidence companion:** `evidence/Sources_and_Calculations.pdf`
- **Machine-readable source register:** `evidence/SOURCE_REGISTER.json`
- **Reproduction script:** `analysis/reproduce_calculations.py`

## What this project establishes

The 228-billion-gallon figure can be reconstructed from Lawrence Berkeley National Laboratory’s 2024 model of 2023 U.S. data-center operations using its reported electricity use, direct water consumption, and electricity-source water-consumption intensity.

The reconstruction does **not** mean 228 billion gallons flowed through data-center buildings. Most of the modeled footprint is associated with electricity generation. It also does not establish whether a particular proposed facility will strain a particular town’s water supply. That requires local source, peak-demand, utility-capacity, cooling, grid, and contractual evidence.

The project also examines a second question: what useful work is actually delivered by the computing load? It separates measured productivity or capability results from speculative benefits and from environmental-offset claims.

## Repository map

- `article/` — publication-ready PDF, Word, and copy-ready text
- `evidence/` — source ledger, methods companion, release manifest
- `analysis/` — reproducible calculations
- `data/` — compact derived metrics and audit schemas
- `methods/` — definitions, decision framework, limitations
- `records-requests/` — reusable public-record request templates
- `distribution/` — optional social and newsroom copy
- `portfolio/` — short project description for a resume or portfolio

## Reproduce the headline calculation

```bash
python analysis/reproduce_calculations.py
```

The script is intentionally small. The value of the repository is not that multiplication is difficult; it is that the units, system boundaries, and source definitions are explicit.

## Decision standard

This repository does not argue that every data center should be approved or rejected. For a specific proposal, the useful questions are narrower:

1. What water and power demand is actually proposed, under which operating conditions?
2. Which source and utility systems would serve it, and what capacity is already committed?
3. What cooling and backup arrangements change peak demand during difficult conditions?
4. Who pays for project-driven infrastructure, and what happens if the forecast is wrong?
5. Which authority can enforce the limits and obligations?
6. Can expansion be staged behind measurable milestones instead of relying on a twenty-year crystal ball?

## Corrections

If a factual or arithmetic error is found, open an issue with the exact claim, source, and proposed correction. Policy disagreement by itself is not a factual correction.

## Authorship and assistance

Robert Thomas King directed the investigation, questions, judgments, and publication decisions. Research and drafting were assisted by AI. The evidence files are provided so readers can evaluate the work independently of either author or tool.
