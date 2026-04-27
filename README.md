# 🧬 PROJECT MOSAIC: Defensive Protein-Aware Screening for Benchtop Synthesizers

*Apart AIxBio Hackathon — April 2026*

**Submission Track:** DNA Screening & Synthesis Controls (Track 1) / Benchtop Synthesizer Security (Track 4)

---

## Abstract

Project MOSAIC provides an open-source, Protein-Aware Mock Screener tool designed to defend against "context-scrubbed" multi-agent LLM workflows. We demonstrate that while simple DNA-level screening (Hamming distance) can be trivially evaded by generating synonymous codon substitutions using commercial LLMs (yielding 3 unique evasion payloads across 9 tested trials), our **Layer-2 Protein Translation Screener** catches 100% of these adversarial payloads by examining the translated amino acid homology, providing a robust defense against synonymous-only substitutions.

This project explicitly models how malicious users might split a dangerous request into benign subtasks across different models, and provides the defensive code necessary to catch the resulting obfuscated sequences before they reach physical synthesis.

---

## The Threat Model (Red Team) & Scientific Nuance

Current biosecurity evaluations often suffer from the "Single-Node Illusion." If an LLM refuses to design a pathogen, the system is considered safe. However, real-world adversaries use a fragmented ecosystem:
1.  **Node 1 (Bio-Linguist):** Use a model to generate a synonymous codon substitution table for a target sequence, framed as a benign optimization task.
    *   *Note on Model Independence:* Our 3x3 matrix resulted in only 3 unique codon mapping outputs, indicating mapping convergence and reuse among frontier models, reflecting behavior of the workflow itself, not independent generative capacity.
2.  **Context Scrub:** Manually strip the biological context from the resulting dictionary.
    *   *Note on Causality:* It is the semantic laundering (stripping the "bio" intent away in favor of "linguistics") that defeats the guardrails, using workflow fragmentation as a vehicle. That is the true "LLM uplift" mechanism represented here.
3.  **Node 2 (Evasion Coder):** Use a second model to write a "data obfuscation" script using the dictionary, applying basic degeneracy heuristics. No higher-order biological "reasoning" is occurring, and in fact, this entire step could be automated trivially in native python logic without an LLM altogether.

*Note: To prevent infohazards, we used **Green Fluorescent Protein (GFP)**—a harmless, standard biological sequence—as our proxy payload to generate 9 empirical evasion trials across GPT-5.3, Claude Haiku 4.5, and Gemini 3.1 Pro. We explicitly acknowledge this proxy limits generalizability, as frontier models refuse actual pathogen generation dynamically. We tested against this hypothesis securely by verifying consistent control refusals against the "combined malicious" request 3x per frontier model.*

---

## The Defense Tool (Blue Team)

**Open-source defensive screener:** `screener.py`, a two-layer reference implementation demonstrating that protein-level translation—already standard in commercial synthesis screening—provides an absolute defense against synonymous substitution attacks when deployed on benchtop devices that currently lack it. **All screening results are against a simplified model only, not a formal analysis of Twist or IDT commercial workflows.**

| Layer | Method | Evasion Success Rate | Details |
| :--- | :--- | :---: | :---: |
| **Layer 1: DNA Check** | Sliding-window Hamming distance on raw `.txt` sequence | **3/3 unique payloads evaded** (100%) | Mean Max DNA Similarity: 70.0% |
| **Layer 2: Protein Check** | 6-frame conceptual translation + amino acid homology | **0/3 unique payloads evaded** (0%) | 100% structural matching |

*\*Note: Empirical deductive hashing of the 9 trial payloads outputs verified they collapsed into precisely 3 mathematically distinct output sequence groups generated across the 3 unique codon maps.*

The results prove that while AI natively excels at syntactic obfuscation (DNA) against naive legacy tools, biological function (Protein) remains conserved and highly detectable. Modern defense **must** happen at the protein level. Our policy recommendation for Benchtop Synthesizer Manufacturers (Track 4) is the implementation of **hardware interlock mechanisms requiring 6-frame translation firmware checks exceeding 85% homology prior to physical sequencing capabilities enabling.**

---

## Running the Screener

To test the defensive capabilities of the screener against the 9 generated adversarial payloads:

```bash
# Screen a single file
cd analysis
python screener.py --file ../fragments/fragments_trial1.txt

# Run the screener against all 9 LLM-generated evasion trials
python screener.py --run-all
```

## Repository Structure

```
project_mosaic/
├── README.md                       # This file
├── docs/
│   └── MOSAIC_Research_Report.md   # **MAIN HACKATHON SUBMISSION REPORT**
├── analysis/
│   ├── screener.py                 # The Protein-Aware defensive screening tool
│   ├── generate_fragments.py       # Pipeline: runs trials → fragments
│   └── mosaic_engine.py            # (Deprecated) Legacy graph engine
├── data/
│   └── (Raw sequences and trial matrix logs)
├── evasion_trials/
│   └── evasion_trial1.py – 9.py    # LLM-generated evasion scripts (Red Team)
├── fragments/
│   └── fragments_trial1.txt – 9.txt # Generated sequence fragments
└── evidence/
    ├── prompts.md                  # Exact prompts used (Bio, Code, Control)
    └── screenshots/                # Model refusal screenshots
```

## Acknowledgments & Limitations
This work is presented as an **illustrative model** of multi-agent evasion tactics. We explicitly acknowledge that GFP is a harmless proxy and that context-scrubbing currently requires a human-in-the-loop to curate outputs between API calls. For a full discussion on limitations, dual-use risks, and ethical considerations, please see our detailed `MOSAIC_Research_Report.md`.