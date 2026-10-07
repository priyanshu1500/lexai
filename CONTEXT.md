# CONTEXT.md - LexAI Domain Model

## Core Terminology & Domain Glossary

- **SCC (Supreme Court Cases / SCC Online)**: Commercial legal database used in India to search and download case laws, judgments, and legal precedents.
- **Official Court Portals**: Verified e-courts, High Courts, and Supreme Court of India digital platforms (e.g. `ecourts.gov.in`, `sci.gov.in`).
- **Regulatory & Statutory Portals**: Government agency decision archives including MCA (Ministry of Corporate Affairs), ED (Enforcement Directorate), SBI, CCI (Competition Commission of India), RBI (Reserve Bank of India), SFIO (Serious Fraud Investigation Office), and SEBI (Securities and Exchange Board of India).
- **Citation / Reference Number**: Canonical legal identifier (e.g. `2024 INSC 123` or `(2023) 4 SCC 567` or Case/CNR Number) used to index and locate court judgments.
- **Verification Engine**: Automated document comparison pipeline comparing extracted text/PDF structures from commercial copies (SCC) against primary government source copies.
- **Key Case Note**: Summarized briefing document auto-generated from live daily cause lists and hearing updates for ongoing litigation.
- **Legal Agent**: Autonomous agent capable of navigating court web portals, solving CAPTCHAs, parsing cause lists, fetching order PDFs, and alerting counsel.
