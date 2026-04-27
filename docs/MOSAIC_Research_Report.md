# Project MOSAIC: Defensive Protein-Aware Screening for Benchtop Synthesizers

## Abstract
Modern frontier commercial LLMs allow non-experts to design and modify biological sequences via "context-scrubbed" multi-agent workflows. We demonstrate that LLMs can routinely evade standard DNA-level screening systems using synonymous codon substitution. To combat this, we release an open-source, Protein-Aware Mock Screener tool. We systematically generated 9 obfuscated synthesis payloads via cross-model LLM handoffs. While these scripts bypassed legacy DNA-level screening (100% evasion), our updated translation-aware screening tool caught 100% of adversarial payloads by examining the translated homology, reinforcing that modern defense must happen at the protein level.

## Introduction
As AI continues to rapidly lower the barrier to biological engineering, traditional screening mechanisms are struggling to keep up. One particular vulnerability is the "multi-agent context scrub": a human can ask one LLM to generate a substitution matrix, scrub the intent, and use a second LLM to generate a python script to scramble a DNA fragment. Our project initially explored how well these multi-agent pipelines could generate outputs that evaded simple screening rules. 

We found that while basic DNA screening fails miserably (0/9 payloads detected), simply upgrading screening to use 6-frame conceptual translation to the protein level provides an absolute defense against synonymous substitution attacks (9/9 payloads detected). This report details our mock red-teaming pipeline and the open-source defensive screener we built.

## Related Work
*   Gretton, D., et al. (2024). "Red-teaming DNA synthesis screening to prevent the hazards of synthetic biology." *PNAS Nexus*, 3(4), pgae126.
*   International Gene Synthesis Consortium (IGSC) Harmonized Screening Protocol v2.0.

Our work builds on these efforts by open-sourcing a prototype pipeline showing exactly *how* a synonymous evasion attack works via API context scrubbing, and *how* a protein-aware screener defends against it.

## Clarifying the Attack: Fragmentation vs. Semantic Laundering
A critical distinction in our threat model is determining *why* models comply with dangerous requests when decoupled. Is the safeguard bypassed because the task is split across two models (fragmentation), or because the biological intent is masked as a benign coding exercise (semantic laundering)? 

Our Red Team workflow relies heavily on semantic laundering. The prompt to the "Bio-Linguist" model benignly asks for a codon optimization table. The prompt to the "Evasion Coder" model asks for string manipulation. We observed that frontier models refuse explicit, end-to-end biological misuse prompts (the control), but comply with semantically laundered subtasks. Therefore, our results demonstrate that reframing intent defeats safeguards. While workflow decomposition (using two models) facilitates this laundering, it is the removal of explicit misuse framing that allows the payload to pass through the LLM policy filters.

## Defining Evasion
To maintain scientific rigor, we define "evasion" taxonomically:
1.  **LLM Policy Evasion (Strong Evidence):** Our pipeline successfully bypassed the safety guardrails of GPT-5.3, Claude Haiku 4.5, and Gemini 3.1 Pro by laundering intent. 
2.  **Sequence Similarity Evasion (Model-Dependent):** The generated fragments successfully achieved low Hamming-distance similarity to the wild-type DNA, evading our naive baseline screener.
3.  **Commercial Procurement Evasion (Out of Scope):** We *do not* claim that these fragments would evade commercial DNA synthesis providers (like Twist or IDT). Modern commercial screeners employ advanced protein-level Hidden Markov Models (HMMs). Our Layer 2 screener explicitly demonstrates that protein-level checks defeat this class of attack.

## Methodology

We constructed a modular Red/Blue pipeline testing both offense and defense:

1.  **Red Team Generation Matrix (The Attack):**
    *   **Node 1 (Bio-Linguist):** 3 frontier models (GPT-5.3, Claude Haiku 4.5, Gemini 3.1 Pro) generated synonymous codon substitution tables for our proxy payload (Green Fluorescent Protein / GFP). All prompts were executed at Temperature 0.7 to allow natural generative variation.
        *   *Artifact Note:* Upon analysis, the outputs from the varying Bio models collapsed into three effective equivalence classes (mappings). This mapping reuse means our 9 trials are not strictly independent; they demonstrate pipeline behavior and convergence rather than 9 unique creative exploits. Furthermore, the LLM metric of "uplift" only exists structurally in semantic compliance at this Node (defeating conversational intent classifiers by treating biology as code optimization), as the actual output is a trivial substitution dictionary.
    *   **Node 2 (Evasion Coder):** With biological context scrubbed, the 3 models were given the mappings and asked to generate string-splitting and translation scripts. Executed at Temperature 0 to ensure direct coding determinism.
        *   *LLM Utility Re-clarification:* This step represents trivial coding that requires no LLM at all; our finding isn't that LLMs are excellent at chunking DNA, but that laundering context across models serves as a mechanism to cleanly disassociate the Node 1 ask from the Node 2 task.
    *   **Execution:** 3x3 combinations resulted in 9 successful fragments using simple degeneracy heuristics (synonymous mutations). No higher-order biological reasoning (e.g., GC skewing, motif disruption) occurred.
2.  **Blue Team Defensive Screener (The Defense):**
    *   We built `screener.py`, a layered screening tool to simulate defensive postures.
    *   *Layer 1 (Baseline DNA):* A frozen baseline checking for sliding-window Hamming distance against the wild-type string. Used to represent historical or naive text-based screening.
    *   *Layer 2 (Protein Translation):* Performs dynamic DNA-to-Protein translation using the standard genetic code and checks for protein sequence homology (window size 10 AA at 85% identity). For highly-conserved motifs (such as our 238 AA GFP proxy run completely entirely by synonymous substitution), this Layer represents mathematical inevitability; it does not "learn" the obfuscation but unmasks it by functional design, proving the robustness of the translating paradigm over DNA similarity.
3.  **Control Condition:**
    *   An explicit, single-session prompt (combining Node 1 intent and Node 2 execution commands) was fired against the 3 target models at Temp 0. To rule out fragile hallucinations or single-run volatility, we queried the prompt across three separate fresh sessions per model, affirming consistent refusal (100%) against single-prompt explicitly malicious framing.

## Results
Against the Layer 1 DNA Screener, the context-scrubbed evasion attacks achieved a **100% bypass rate (9/9 sequences evaded detection)**. The DNA sequences were heavily obfuscated.

Against the Layer 2 Protein-Aware Screener, the bypass rate was **0% (9/9 sequences caught)**. Because the synonymous edits did not alter the core amino acid structures, the 6-frame translation identified the conserved domains instantly.

## Limitations and Dual-Use Considerations

*   **Proxy Payload Limitation:** We used GFP (Green Fluorescent Protein) as a completely harmless proxy. We acknowledge that extrapolating LLM capabilities from a benign payload to a regulated pathogen or DURC (Dual-Use Research of Concern) is a limitation. Frontier models are trained specifically to refuse pathogen requests; our attack matrix does not factor in these domain-specific refusal gates. This is a fundamental constraint on the generalizability of our findings.
*   **Context Scrubbing (Human-in-the-loop):** The context scrub was performed manually, meaning the workflow is not fully autonomous. A human operator is required to launder the context between models.
*   **Screener Scope:** Our screener is a simplified model checking against a single target protein. Real commercial screening APIs (like the ones currently deployed by IGSC members) use advanced HMMs and comprehensive DBs. All screening findings here are strictly "against a simplified model only." We firmly reject the notion that our red-team bypasses commercial providers; rather, it highlights the vulnerability of naïve DNA-level checks that might be implemented in basic benchtop synthesizers.
*   **Data Integrity & LLM Generativity:** The 3x3 model matrix nominally implies 9 independent trials, but the generated codon mappings collapsed into 3 equivalence classes (one of which was reused across 6 trials). This mapping artifact demonstrates pipeline behavior, not deep creativity. Furthermore, models applied trivial degeneracy heuristics rather than "reasoning about biology"—no functional sequence engineering occurred.
*   **Dual-Use Risks:** While our code demonstrates generating obfuscated sequence arrays, the technique (synonymous substitution) is well documented and is trivially defeated by our own Tool. We explicitly did not include pathogen DBs to prevent misuse.

## Scientific Claims & Future Work
Our research confirms that naïve DNA-level security is brittle and insufficient in the LLM era, as automated tools can easily scramble DNA syntax while preserving biologic intent. 

What we **rigorously claim**:
1. Modern frontier LLMs refuse explicit end-to-end biological misuse prompts.
2. The same models comply with semantically laundered subtasks.
3. Synonymous codon substitution preserves protein identity while reducing nucleotide similarity, effectively evading simple DNA-level screening tools.

What we **do not claim**:
1. That commercial synthesis screening is broadly bypassable via this method.
2. That LLMs independently "reason" to autonomously design effective biological evasion.
3. That our 9-trial matrix represents 9 unique biological exploits. Empirical hash-deduplication of the fragment text logs confirms our 9 nominally independent trials collapsed into exactly 3 unique sequence payloads, validating mapping convergence and pipeline behavior over generative creativity.

## Practical Policy Recommendations
The theoretical graph model illustrates that simply patching discrete model endpoints cannot shift the minimum cut of a fully-connected multi-agent ecosystem. Therefore, the minimum cut for biosecurity must reside at the physical interface.

Commercial synthesis providers (Twist, IDT) already employ protein-level HMM screening; the unaddressed vulnerability is the growing ecosystem of decentralized benchtop synthesizers operating without equivalent controls. 

For **Track 4 (Benchtop Synthesizers)**, we offer the following actionable policy:
Benchtop hardware manufacturers should implement an **on-device hardware interlock** that requires a cryptographically signed API handshake with an approved central protein-homology screening service before physical synthesis begins. If offline operation is mandated, a robust 6-frame translational screener (such as Layer 2 of Project MOSAIC) must be embedded directly in the device firmware, blocking any sequence translating to >85% homology with regulated databases, rendering synonymous obfuscation mathematically irrelevant.