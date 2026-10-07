# CONTEXT.md - LexAI Domain Model & Expert Legal Architecture

## Core Terminology & Domain Glossary

### 1. Citation Formats & Neutral Identifiers
- **SCC Citation**: `(YYYY) Vol SCC Page` (e.g., `(2018) 1 SCC 1`) - Primary commercial reporter standard in India.
- **Supreme Court Neutral Citation (INSC)**: `YYYY INSC [Number]` (e.g., `2024 INSC 835`) - Official court-assigned digital identifier introduced in 2023.
- **AIR Citation**: `AIR YYYY SC Page` / `AIR YYYY [State] Page` - All India Reporter standard.
- **SCR / SCALE / JT**: `[YYYY] Vol SCR Page`, `JT YYYY (Vol) SC Page`, `SCALE`.
- **Regulatory / Tribunal Citations**: NCLT/NCLAT Order Nos, `(YYYY) SEBI Order`, CCI Case Nos, ITAT/CESTAT Appeal Nos.
- **Academic Standards**: 
  - **SILC (Standard Indian Legal Citation)**: India-centric citation standard.
  - **ILI (Indian Law Institute)**: Footnote standard widely used in Indian law reviews.
  - **Bluebook (21st ed)** & **OSCOLA (4th ed)**: US/UK international standards used by top global/Indian law firms.

### 2. Practice Areas (AoP) Classification
- **AoP-1: Corporate Law & M&A / Governance** (Companies Act 2013, NCLT, NCLAT, MCA).
- **AoP-2: Banking, Finance & Insolvency** (IBC 2016, IBBI, RBI Circulars, DRT/DRAT).
- **AoP-3: Competition & Antitrust** (Competition Act 2002, CCI, NCLAT Appellate).
- **AoP-4: Securities & Capital Markets** (SEBI Regulations, SAT, Listing Obligations - LODR).
- **AoP-5: White-Collar Crime & Financial Enforcement** (PMLA, ED, SFIO, CBI, IPC/BNS).
- **AoP-6: Taxation & Revenue** (Income Tax Act, ITAT, GST Council, CESTAT, Customs).
- **AoP-7: Commercial Arbitration & Litigation** (Arbitration & Conciliation Act 1996, DIAC, MCIA, Commercial Courts).
- **AoP-8: Constitutional & General Civil Litigation** (Supreme Court, High Courts, District e-Courts).

### 3. Single-Line Proposition Extractor (Senior Counsel Prompt Distiller)
- Transforms verbose, multi-page client facts or lengthy prompts into a crisp, single-line **Proposition of Law** (Framed Issue of Law) as prepared by Senior Advocates before legal research or oral argument.

### 4. Advanced Legal Boolean Search Engine
- Generates structured Boolean queries (`AND`, `OR`, `NOT`, `NEAR/n`, `"exact phrase"`, `sec:...`) tailored to official government portals and legal repositories.
