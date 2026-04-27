# Project MOSAIC: Defensive Protein-Aware Screening for Benchtop Synthesizers

## Abstract
Modern open-weight models allow non-experts to design and modify biological sequences via "context-scrubbed" multi-agent workflows. We demonstrate that LLMs can routinely evade standard DNA-level screening systems using synonymous codon substitution. To combat this, we release an open-source, Protein-Aware Mock Screener tool. We systematically generated 9 obfuscated synthesis payloads via cross-model LLM handoffs. While these scripts bypassed legacy DNA-level screening (100% evasion), our updated translation-aware screening tool caught 100% of adversarial payloads by examining the translated homology, reinforcing that modern defense must happen at the protein level.

## Introduction
What is AIxBio? As AI continues to rapidly lower the barrier to biological engineering, traditional screening mechanisms are struggling to keep up. One particular vulnerability is the "multi-agent context scrub": a human can ask one LLM to generate a substitution matrix, scrub the intent, and use a second LLM to generate a python script to scramble a DNA fragment. Our project initially explored how well these multi-agent pipelines could generate outputs that evaded simple screening rules. 

We found that while basic DNA screening fails miserably (0/9 payloads detected), simply upgrading screening to use 6-frame conceptual translation to the protein level provides an absolute defense against synonymous substitution attacks (9/9 payloads detected). This report details our mock red-teaming pipeline and the open-source defensive screener we built.

## Related Work
*   Gretton, D., et al. (2024). "Red-teaming DNA synthesis screening to prevent the hazards of synthetic biology." *PNAS Nexus*, 3(4), pgae126.
*   International Gene Synthesis Consortium (IGSC) Harmonized Screening Protocol v2.0.

Our work builds on these efforts by open-sourcing a prototype pipeline showing exactly *how* a synonymous evasion attack works via API context scrubbing, and *how* to defend against it.

## Methodology

We constructed a modular Red/Blue pipeline testing both offense and defense:

1.  **Red Team Generation Matrix (The Attack):**
    *   **Node 1 (Bio-Linguist):** 3 frontier models (GPT-5.3, Claude Haiku 4.5, Gemini 3.1 Pro) generated synonymous codon substitution tables for our proxy payload (Green Fluorescent Protein / GFP).
    *   **Node 2 (Evasion Coder):** With biological context scrubbed, the 3 models generated string-splitting and translation scripts. 
    *   **Execution:** 3x3 combinations resulted in 9 successful fragments using only synonymous mutations.
2.  **Blue Team Defensive Screener (The Defense):**
    *   We built `screener.py`, a layered screening tool.
    *   *Layer 1 (Baseline DNA):* Checks for sliding-window Hamming distance against the wild-type.
    *   *Layer 2 (Protein Translation):* Performs dynamic DNA-to-Protein translation using standard standard genetic code and checks for protein sequence homology.

## Results
Against the Layer 1 DNA Screener, the context-scrubbed evasion attacks achieved a **100% bypass rate (9/9 sequences evaded detection)**. The DNA sequences were heavily obfuscated.

Against the Layer 2 Protein-Aware Screener, the bypass rate was **0% (9/9 sequences caught)**. Because the synonymous edits did not alter the core amino acid structures, the 6-frame translation identified the conserved domains instantly.

## Limitations and Dual-Use Considerations

*   **Proxy Payload Limitation:** We used GFP (Green Fluorescent Protein) as a completely harmless proxy. We acknowledge that extrapolating LLM capabilities from a benign payload to a regulated pathogen or DURC (Dual-Use Research of Concern) is a limitation. Frontier models are trained specifically to refuse pathogen requests; our attack matrix does not factor in these domain-specific refusal gates.
*   **Context Scrubbing (Human-in-the-loop):** The context scrub was performed manually, meaning the workflow is not fully autonomous. A human operator is required to launder the context between models.
*   **Screener Scope:** Our screener is a simplified model checking against a single target protein. Real commercial screening APIs (like the ones currently deployed by IGSC members) use advanced HMMs and comprehensive DBs, which we encourage as a standard across benchtop synthesizers.
*   **Dual-Use Risks:** While our code demonstrates generating obfuscated sequence arrays, the technique (synonymous substitution) is well documented and is defeated by our own Tool. We explicitly did not include pathogen DBs to prevent misuse.

## Discussion and Future Work
Our research confirms that DNA-level security is insufficient in the LLM era, as automated tools can easily scramble DNA while preserving function. However, it also provides optimism: standard structural/protein-level screening remains highly robust against these low-effort proxy attacks. Future work should integrate our lightweight protein-aware screener directly into Benchtop DNA Synthesizer hardware logic (Track 4) to ensure on-device orders are screened translationally before printing occurs, bridging the gap between digital AI capabilities and physical synthesis.