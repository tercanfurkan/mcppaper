# Layer-Wise Fidelity Evaluation of Multi-Layer Agentic AI Pipelines: MCP, A2A, and A2UI

**Ömer Furkan Tercan**  
University of Helsinki · omer.tercan@helsinki.fi

---

## Abstract

Multi-layer agentic pipelines — in which an LLM agent retrieves context via a standardised tool protocol, synthesises a response, and renders it through a structured user interface — are increasingly deployed in practice, yet remain poorly understood from an evaluation standpoint. Existing work evaluates such systems at the pipeline level, scoring only the final output against a reference; no framework characterises where information fidelity is gained or lost between architectural layers. We propose _layer-wise fidelity scoring_: BERTScore F1 computed independently at R₀ (raw MCP tool output), R₁ (A2A agent synthesis), and R₂ (A2UI structured payload), each against the same ground-truth reference answer. We instantiate this protocol on a software documentation Q&A task using the httpx Python library, building a minimal end-to-end prototype comprising an MCP retrieval server, a LangGraph A2A orchestrator, and a Streamlit A2UI rendering layer. Experiments across 15 test queries show that A2A synthesis substantially improves BERTScore F1 by +0.039 (Δ₁) while leaving Recall essentially unchanged (Δ₁ᴿ = +0.007), confirming that synthesis improves content selectivity without sacrificing coverage. The A2UI data-formatting step — evaluated via its serialised JSON payload rather than its rendered visual form — is near-lossless on F1 (Δ₂ = −0.0001) with only minor Recall compression — dynamics that are invisible to aggregate end-to-end scoring and only emerge through layer-wise analysis. Our protocol is task-agnostic and reusable; we release the annotated test set and scoring harness to support future benchmarking of UI-terminal agentic systems.

---

## 1. Introduction

The rapid proliferation of large language model (LLM) services has created demand for standardised protocols that allow agents to interact reliably with external tools, data sources, and peer agents. As Yang et al. [1] observe, the absence of such standards causes fragmentation that hinders interoperability and limits the ability of agents to tackle complex real-world tasks. We are witnessing the formation of what practitioners describe as a genuine _protocol stack_ for agentic systems — analogous in significance to the TCP/IP stack for the internet [14]. This stack comprises three distinct layers, each solving a different problem: the _Model Context Protocol_ (MCP) governs how agents access tools and data; the _Agent-to-Agent_ (A2A) protocol governs how agents collaborate with peer agents; and the _Agent-to-UI_ (A2UI) protocol governs how agents render structured interfaces for human consumption [14]. MCP, introduced by Anthropic in November 2024, standardises context delivery through a JSON-RPC client-server architecture [2, 3]. A2A, introduced by Google in April 2025, formalises task delegation and capability discovery through Agent Cards and structured handoff messages [3, 5, 16]. A2UI, introduced by Google in December 2025, defines declarative UI components that render natively across platforms without executing arbitrary client-side code [14, 17]. Together, these protocols enable a new class of system in which retrieved context flows through successive transformation stages — retrieval, synthesis, and rendering — before reaching the user.

Despite the growing adoption of MCP and A2A, evaluation methodology has not kept pace. Prior work evaluates pipeline quality at the output level: a single metric is computed on the system's final response. AgentMaster [6], the closest related system, jointly employs A2A and MCP in a multi-agent framework and reports BERTScore F1 of 96.3% on its final outputs. However, two limitations constrain its scope. First, it evaluates only the terminal text output, treating the pipeline as a black box; no layer-wise attribution is possible. Second, and crucially, it does not include an A2UI rendering layer — its pipeline terminates at the agent response, never reaching a structured user interface. Our system is, to the best of our knowledge, the first experimental instantiation of the complete MCP→A2A→A2UI stack, and the first to evaluate textual information fidelity at each of its three layers. We note that the A2UI layer is evaluated via its serialised JSON payload (the data-formatting step) rather than its rendered visual form; perceptual evaluation of the rendered UI is an open problem we identify as future work.

We address this gap with a simple but principled evaluation protocol: _layer-wise fidelity scoring_. Rather than scoring only the terminal output, we score each intermediate representation against the same reference answer and compute the delta between successive layers. Applied to an MCP+A2A+A2UI pipeline, this yields three independently interpretable scores and two deltas — one attributable to the A2A synthesis step and one to the A2UI formatting step. Any of these outcomes is informative: a large negative Δ₁ implies that the agent's synthesis introduces drift; a large negative Δ₂ implies that the UI schema is too lossy; a positive Δ₁ implies the agent adds genuine value beyond raw retrieval.

Our contributions are as follows. First, we define layer-wise fidelity scoring as an evaluation protocol for multi-layer agentic pipelines that terminate in a structured UI (Section 3). Second, we build a minimal end-to-end prototype on software documentation Q&A and release a 15-item annotated test set (Section 4). Third, we report BERTScore Precision, Recall, and F1 at each layer and identify which architectural transition incurs the greatest fidelity shift (Section 5). Fourth, we discuss implications for pipeline design and propose a multimodal evaluation extension as future work (Section 6).

---

## 2. Background

Given the pace of development in this field, where practitioner knowledge frequently precedes formal publication, this section draws on both peer-reviewed literature and grey literature — including technical blog posts and official protocol documentation — following the Multivocal Literature Review (MLR) methodology established for software engineering research [15].

**Model Context Protocol.** Introduced by Anthropic in November 2024, MCP [2] standardises tool-and-resource invocation by LLM agents via a JSON-RPC client-server architecture. The protocol defines four core primitives — Tools, Resources, Prompts, and Sampling — and separates concerns across a Host (the LLM application), Clients (session managers), and Servers (capability providers) [3, 7, 8]. This decoupling reduces the fragmentation caused by ad-hoc API integrations and enables dynamic tool discovery [3]. From an evaluation standpoint, MCP tool returns (R₀) are the ground-truth information source of the pipeline: they represent what the system actually retrieved before any agent processing.

**Agent-to-Agent coordination.** Introduced by Google in April 2025, A2A protocols govern structured message exchange between agents across different frameworks or organisational boundaries [3, 16]. Frameworks such as LangGraph, AutoGen, and Magentic-One implement A2A semantics locally through explicit handoff protocols and role-constrained reasoning [9, 10]. Each inter-agent communication step introduces summarisation, reformulation, or synthesis — all potential fidelity loss points [5]. We treat the A2A agent's synthesised natural-language response (R₁) as a distinct scoreable intermediate, isolating the transformation effect of this layer.

**Agent-to-UI rendering.** A2UI refers to the translation of agent output into structured UI components — cards, tables, code blocks — for human consumption. As the newest layer of the stack, introduced in December 2025 [17], A2UI has received almost no attention in the academic evaluation literature [14]. Unlike RAG or chatbot evaluation, A2UI output is visual and structured; standard NLP metrics do not apply directly. Practitioners have identified cross-layer observability — the ability to trace a user request coherently through A2UI, A2A, and MCP — as a critical unsolved structural gap in current stacks [14]. Our layer-wise fidelity scoring protocol directly addresses the measurement dimension of this gap. We operationalise R₂ by scoring the serialised JSON payload that drives the UI rendering, and discuss multimodal perceptual scoring via GPT-4o Vision as a direction for future work (Section 6.6).

**Evaluation of agentic pipelines.** BERTScore [12] computes contextual token-level F1 using a pretrained language model, handling paraphrase gracefully and correlating well with human judgement. It is our primary metric. LLM-as-a-Judge [13] uses a judge model with a rubric and is strong for open-ended output but harder to reproduce. No prior work applies layer-wise scoring to decompose fidelity across MCP, A2A, and A2UI stages. AgentMaster [6] is the closest system: it jointly employs A2A and MCP and evaluates with BERTScore and G-Eval, but scores only the final output, treating the pipeline as a black box.

---

## 3. Method

### 3.1 Pipeline Architecture

Our prototype comprises three layers, each producing a scoreable intermediate.

The **MCP layer** is implemented as a FastMCP server wrapping a FAISS vector store of httpx documentation chunks. It exposes a single `retrieve(query, k)` tool. The tool return — the concatenated text of the top-k retrieved chunks — is logged as R₀.

The **A2A layer** is implemented as a two-node LangGraph graph. An orchestrator node receives the user query, calls the MCP tool, receives R₀, and synthesises a natural-language answer. This answer is logged as R₁ before any further processing.

The **A2UI layer** is a formatter node that converts R₁ into a fixed JSON schema: `{summary, key_points[], code_example, source_ref}`. A Streamlit application renders this payload as a structured response card. The serialised JSON payload is logged as R₂ and used as a text proxy for the A2UI transformation step; perceptual evaluation of the rendered Streamlit card is deferred to future work (Section 6.6).

![Figure 1. MCP → A2A → A2UI pipeline architecture with layer-wise fidelity capture points](figures/fig1-pipeline-architecture.svg)

_Figure 1. Each layer produces a scoreable intermediate (R₀, R₁, R₂). Dashed amber arrows indicate BERTScore F1 computation against the same ground-truth reference answer. Δ₁ and Δ₂ are the attribution deltas._

### 3.2 Layer-Wise Fidelity Scoring

**Metric selection.** We select BERTScore [12] as our primary metric for three reasons. First, it handles paraphrase gracefully via contextual embeddings, which is essential here because agent-generated prose will rarely reproduce reference text verbatim. Second, it produces continuous scalars per query, enabling the delta arithmetic central to our protocol. Third, it requires only a reference answer string — no judge model, no API call, no rubric — making the scoring pipeline fully deterministic and reproducible at temperature 0.

The main alternative, LLM-as-a-Judge [13], was considered but deferred to future work (Section 6.6). While strong for open-ended quality assessment, it introduces non-determinism, API cost, and positional bias, all of which complicate fair layer-wise comparison. ROUGE-L was excluded because it penalises valid paraphrases, making it unsuitable for evaluating agent-generated synthesis where rewording is expected and desirable. Exact match was excluded for the same reason, and additionally because reference answers span 1–3 sentences with no single correct surface form.

**Length disparity and the P/R decomposition.** A known limitation of using BERTScore F1 to compare across layers of different lengths is that R₀ — three concatenated documentation chunks (~900 tokens) — will naturally score lower on Precision than R₁ — a synthesised answer (~60–100 tokens) — simply because more of R₀'s tokens are irrelevant to the short reference answer. This means a positive Δ₁ on F1 alone cannot cleanly separate genuine semantic improvement from the mechanical effect of length reduction. To address this, we report BERTScore Precision (P), Recall (R), and F1 separately at each layer. The decomposition is interpretable: if R₁ achieves higher Precision than R₀ while maintaining comparable Recall, this indicates that A2A synthesis improved selectivity without sacrificing coverage — precisely what a grounded synthesis step should do. If Recall drops, synthesis lost information. This framing makes Δ₁ analytically honest.

Each intermediate is scored against the same human-written reference answer using BERTScore with `roberta-large` as the backbone model. For each layer we record three values:

- **P(Rₙ)**: BERTScore Precision — proportion of the candidate's tokens semantically matched in the reference. Sensitive to candidate length; longer candidates are penalised.
- **R(Rₙ)**: BERTScore Recall — proportion of the reference's tokens semantically matched in the candidate. Indicates how completely the candidate covers the reference answer.
- **F1(Rₙ)**: Harmonic mean of P and R. Primary scalar for delta computation.

Applied at each layer:

- **P(R₀), R(R₀), F1(R₀)**: scores of the raw MCP tool return against the reference.
- **P(R₁), R(R₁), F1(R₁)**: scores of the A2A agent's synthesised response against the reference.
- **P(R₂), R(R₂), F1(R₂)**: scores of the A2UI JSON text fields (`summary` concatenated with `key_points`) against the reference.

Four attribution deltas are derived. Δ₁ and Δ₂ denote strictly F1 differences; Recall deltas are tracked separately to diagnose length-confounded effects:

- **Δ₁ = F1(R₁) − F1(R₀)**: A2A transformation effect on F1.
- **Δ₁ᴿ = R(R₁) − R(R₀)**: A2A effect on Recall. Stable or positive Δ₁ᴿ alongside positive Δ₁ confirms genuine condensation; negative Δ₁ᴿ indicates information loss.
- **Δ₂ = F1(R₂) − F1(R₁)**: A2UI compression effect on F1.
- **Δ₂ᴿ = R(R₂) − R(R₁)**: A2UI effect on Recall. A large negative Δ₂ᴿ indicates the JSON schema discards relevant content.

![Figure 2. Layer-wise fidelity scoring: three research questions and testable hypotheses](figures/fig2-evaluation-design.svg)

_Figure 2. The three research questions operationalised as layer comparisons, and the three testable hypotheses. Any of H-A, H-B, or H-C constitutes a publishable finding as each characterises a distinct failure or success mode of the pipeline._

### 3.3 Controlled Variables

The same LLM (`gpt-4o-mini`, temperature 0) is used across all agent calls; only the pipeline stage changes. k=3 retrieved chunks are used for all queries with no re-ranking. Reference answers are written by the authors from primary httpx documentation, independent of system outputs.

---

## 4. Experimental Setup

### 4.1 Domain and Test Set

We use the httpx Python library documentation as our retrieval corpus, chosen because its answers are precise, keyword-dense, and grounded in a single authoritative source — properties that make reference answer construction tractable and BERTScore meaningful. The 15 test queries cover: parameter behaviour (e.g., timeout configuration), error handling, authentication patterns, and method signatures. All queries require specific grounded retrieval; parametric LLM knowledge is insufficient to answer them correctly without tool access. Reference answers are 1–3 sentences extracted or paraphrased from the official httpx documentation.

### 4.2 Implementation

| Component       | Choice                                     |
| --------------- | ------------------------------------------ |
| MCP server      | FastMCP + LangChain FAISS                  |
| Embedding model | `text-embedding-3-small`                   |
| Agent framework | LangGraph (orchestrator + formatter nodes) |
| LLM             | `gpt-4o-mini`, temperature 0               |
| UI              | Streamlit                                  |
| Scoring         | `bert-score` v0.3.13, `roberta-large`      |

`gpt-4o-mini` was selected for four reasons. First, it produces fully deterministic outputs at temperature 0, which is essential for reproducibility — any re-run of the evaluation harness must yield identical R₁ and R₂ intermediates. Second, the task is retrieval-grounded Q&A, not complex multi-step reasoning; a capable but lightweight model is appropriate and avoids conflating model capability with pipeline quality. Third, the LLM is a controlled variable rather than the contribution — the paper evaluates the evaluation protocol and pipeline architecture, and any sufficiently capable instruction-following model at temperature 0 should produce comparable relative deltas. Fourth, low per-call cost reduces the barrier to replication. AgentMaster [6], the closest related system, also uses `gpt-4o-mini`, making scores directly comparable.

`text-embedding-3-small` was selected as the embedding model for three reasons. First, it uses the same OpenAI API as the LLM, requiring no additional credentials or services and keeping the setup minimal. Second, its 1536-dimensional embeddings provide sufficient semantic resolution for a focused, single-library technical corpus — the httpx documentation is narrow in domain, so high-dimensional embeddings offer diminishing returns. Third, like the LLM, the embedding model is a controlled variable: it affects R₀ uniformly across all 15 queries, and what matters for the experiment is retrieval consistency rather than maximising retrieval performance.

---

## 5. Results

### 5.1 Layer-Wise BERTScore Results

**Table 1a.** BERTScore F1 at each pipeline layer across 15 test queries. Δ₁ = F1(R₁) − F1(R₀); Δ₂ = F1(R₂) − F1(R₁).

| Query ID | F1(R₀) | F1(R₁) | F1(R₂) | Δ₁ | Δ₂ |
| -------- | ------ | ------ | ------ | --- | --- |
| Q01 | 0.8451 | 0.8539 | 0.8757 | +0.0088 | +0.0218 |
| Q02 | 0.8525 | 0.8944 | 0.8949 | +0.0419 | +0.0005 |
| Q03 | 0.8443 | 0.8961 | 0.8896 | +0.0518 | -0.0065 |
| Q04 | 0.7964 | 0.8516 | 0.8414 | +0.0552 | -0.0102 |
| Q05 | 0.8138 | 0.8787 | 0.8739 | +0.0649 | -0.0048 |
| Q06 | 0.8549 | 0.8992 | 0.8968 | +0.0443 | -0.0024 |
| Q07 | 0.8621 | 0.8825 | 0.8622 | +0.0204 | -0.0203 |
| Q08 | 0.8344 | 0.8733 | 0.8840 | +0.0389 | +0.0107 |
| Q09 | 0.7941 | 0.8756 | 0.8640 | +0.0815 | -0.0116 |
| Q10 | 0.8282 | 0.8806 | 0.8666 | +0.0524 | -0.0140 |
| Q11 | 0.8228 | 0.8468 | 0.8459 | +0.0240 | -0.0009 |
| Q12 | 0.8372 | 0.8467 | 0.8608 | +0.0095 | +0.0141 |
| Q13 | 0.8523 | 0.8510 | 0.8706 | -0.0013 | +0.0196 |
| Q14 | 0.7851 | 0.8415 | 0.8482 | +0.0564 | +0.0067 |
| Q15 | 0.8210 | 0.8534 | 0.8492 | +0.0324 | -0.0042 |
| **Mean** | **0.8296** | **0.8684** | **0.8683** | **+0.0387** | **-0.0001** |

**Table 1b.** BERTScore Precision and Recall per layer. Recall deltas Δ₁ᴿ = R(R₁) − R(R₀) and Δ₂ᴿ = R(R₂) − R(R₁) disambiguate condensation effects from information loss (see Section 3.2).

| Query ID | P(R₀) | R(R₀) | P(R₁) | R(R₁) | P(R₂) | R(R₂) | Δ₁ᴿ | Δ₂ᴿ |
| -------- | ------ | ------ | ------ | ------ | ------ | ------ | ---- | ---- |
| Q01 | 0.8090 | 0.8845 | 0.8230 | 0.8871 | 0.8736 | 0.8778 | +0.0026 | -0.0093 |
| Q02 | 0.8144 | 0.8943 | 0.8677 | 0.9228 | 0.8982 | 0.8917 | +0.0285 | -0.0311 |
| Q03 | 0.8180 | 0.8723 | 0.9210 | 0.8724 | 0.9043 | 0.8754 | +0.0001 | +0.0030 |
| Q04 | 0.7665 | 0.8288 | 0.8743 | 0.8300 | 0.8536 | 0.8296 | +0.0012 | -0.0004 |
| Q05 | 0.7817 | 0.8486 | 0.9089 | 0.8505 | 0.8908 | 0.8576 | +0.0019 | +0.0071 |
| Q06 | 0.8307 | 0.8806 | 0.9043 | 0.8942 | 0.9023 | 0.8913 | +0.0136 | -0.0029 |
| Q07 | 0.8225 | 0.9057 | 0.8587 | 0.9077 | 0.8737 | 0.8509 | +0.0020 | -0.0568 |
| Q08 | 0.7861 | 0.8890 | 0.8792 | 0.8674 | 0.8891 | 0.8791 | -0.0216 | +0.0117 |
| Q09 | 0.7626 | 0.8282 | 0.8969 | 0.8554 | 0.8801 | 0.8486 | +0.0272 | -0.0068 |
| Q10 | 0.8128 | 0.8442 | 0.8943 | 0.8673 | 0.8672 | 0.8661 | +0.0231 | -0.0012 |
| Q11 | 0.8055 | 0.8409 | 0.8346 | 0.8594 | 0.8577 | 0.8344 | +0.0185 | -0.0250 |
| Q12 | 0.8080 | 0.8686 | 0.8180 | 0.8776 | 0.8679 | 0.8539 | +0.0090 | -0.0237 |
| Q13 | 0.7994 | 0.9127 | 0.8207 | 0.8836 | 0.8712 | 0.8701 | -0.0291 | -0.0135 |
| Q14 | 0.7613 | 0.8104 | 0.8420 | 0.8409 | 0.8624 | 0.8344 | +0.0305 | -0.0065 |
| Q15 | 0.8147 | 0.8273 | 0.8793 | 0.8290 | 0.8711 | 0.8283 | +0.0017 | -0.0007 |
| **Mean** | **0.7995** | **0.8624** | **0.8682** | **0.8697** | **0.8775** | **0.8593** | **+0.0073** | **-0.0104** |

### 5.2 Findings

**F1 results (Table 1a).** Mean F1(R₀) = 0.8296, F1(R₁) = 0.8684, F1(R₂) = 0.8683. The A2A synthesis step improved F1 by Δ₁ = +0.0387, confirming hypothesis H-B. The A2UI formatting step left F1 virtually unchanged (Δ₂ = −0.0001), indicating the JSON schema preserves F1 almost perfectly. All but one query (Q13, Δ₁ = −0.0013) show positive Δ₁, making the A2A improvement highly consistent across the test set.

**P/R decomposition (Table 1b).** The Precision/Recall breakdown reveals the mechanism. R₀ exhibits low mean Precision (0.7995) alongside moderate Recall (0.8624), consistent with the length-disparity effect identified in Section 3.2: the three concatenated documentation chunks contain the answer but also many irrelevant tokens that penalise Precision against the short reference. R₁ achieves substantially higher Precision (0.8682) as synthesis condenses the relevant signal, while Recall remains essentially flat (Δ₁ᴿ = +0.0073). This is the strongest form of hypothesis H-B: synthesis improves selectivity without any sacrifice in coverage. The anticipated Recall trade-off from the length-bias analysis did not materialise, indicating that the LangGraph orchestrator at temperature 0 faithfully preserves reference-relevant content during condensation. R₂ maintains comparable Precision (0.8775) with a minor Recall reduction (Δ₂ᴿ = −0.0104), consistent with hypothesis H-C: the A2UI JSON schema introduces a small but consistent compression at the formatting stage.

**Summary.** The dominant effect is the A2A synthesis step: a Precision gain of +0.0687 with negligible Recall cost produces a net F1 improvement of +0.0387. The A2UI step is near-lossless on F1 and introduces only minor Recall compression. End-to-end fidelity from R₀ to R₂ shows ΔF1 = +0.0387 overall, with the pipeline effectively delivering a more precise answer than raw retrieval while preserving coverage.

---

## 6. Discussion

### 6.1 Interpretation of Results

The layer-wise delta structure allows causal attribution of quality changes to specific architectural decisions. However, Δ₁ must be interpreted through the P/R decomposition, not F1 alone, because R₀ and R₁ differ substantially in length. A positive Δ₁ on F1 reflects improved Precision (synthesis removes irrelevant tokens) but should be accompanied by stable or high Recall (synthesis preserves the relevant content). The results confirm that R₁ achieves higher Precision than R₀ with stable Recall, validating that A2A synthesis genuinely improved content selectivity rather than merely discarding content. The near-zero Δ₂ on both F1 and Recall indicates the JSON schema is well-calibrated: the `summary` and `key_points` fields capture the synthesised content with minimal loss.

These interpretations contrast with what aggregate scoring would reveal. AgentMaster [6] reports a mean BERTScore F1 of 96.3% on final outputs — a strong result, but one that cannot locate where in the pipeline quality is preserved or degraded. Our protocol makes this attribution explicit.

### 6.2 Implications for Pipeline Design

Layer-wise scoring can function as a diagnostic tool during development. A large Δ₂ signals that the UI schema needs richer fields before the system is deployed; a large negative Δ₁ signals that the agent prompt needs stronger grounding constraints. Designers should treat each layer as holding an independent fidelity budget, rather than assuming that end-to-end quality reflects component-level quality.

More fundamentally, our protocol fills a gap that aggregate evaluation cannot: it makes individual protocol layers _accountable_. As the MCP+A2A+A2UI stack matures along the phased adoption roadmap identified by Ehtesham et al. [3] — from MCP for tool access, through A2A for agent coordination, to A2UI for user-facing rendering — each new layer added to a production system introduces a new failure mode that a single terminal score cannot detect. Layer-wise fidelity scoring provides a principled, lightweight instrument for catching these failures at the layer where they originate, making it applicable to any future pipeline that adds new transformation stages above MCP.

More broadly, practitioners have identified three structural gaps in the current MCP+A2A+A2UI stack: the absence of a unified identity model across layers, the lack of cross-layer observability, and undefined error propagation semantics between layers [14]. Layer-wise fidelity scoring directly addresses the observability gap at the information quality dimension: by producing independently interpretable scores at R₀, R₁, and R₂, it gives designers the per-layer signal that current tracing infrastructure cannot provide.

### 6.3 Relation to Prior Work

Our work is most directly comparable to AgentMaster [6], which jointly employs A2A and MCP and evaluates with BERTScore and LLM-as-a-Judge. Two distinctions sharpen the comparison. First, evaluation scope: AgentMaster scores only the final text output; we score each layer independently and derive attribution deltas. Second, pipeline scope: AgentMaster terminates at the agent response — it does not include an A2UI rendering layer. Our prototype extends the pipeline through a structured UI rendering stage, making it the first end-to-end experimental instantiation and textual-fidelity evaluation of the complete MCP→A2A→A2UI stack; we emphasise that R₂ is scored via its pre-rendering JSON payload, and that perceptual evaluation of the rendered interface remains future work. The CA-MCP system [4] demonstrates that augmenting the MCP layer with shared context stores reduces LLM calls and improves robustness, but evaluates only aggregate task performance and also lacks a UI terminal layer. The surveys of Yang et al. [1] and Ehtesham et al. [3] identify evaluation benchmarking as a critical gap in the agent protocol literature, explicitly noting that current efforts focus on task success and latency rather than communication efficiency or information fidelity. Our protocol directly addresses this gap.

### 6.4 Validity and Reliability

_Internal validity:_ All variables except the pipeline stage are held constant (same LLM, temperature, k, reference answers), ensuring that observed fidelity differences are attributable to the architectural layer rather than confounds.

_External validity:_ Our test set covers one library (httpx) and one task type (factual Q&A). Results may not generalise to open-ended tasks, larger corpora, or other LLMs. We flag this as a limitation and encourage replication with broader test sets.

_Reliability:_ The scoring pipeline is fully deterministic at temperature 0 and uses a fixed BERTScore model version. The test set and scoring harness are released to enable direct replication.

### 6.5 Limitations

The test set is small (n=15); results may not reach statistical significance and should be interpreted as indicative rather than conclusive. BERTScore on JSON text fields does not capture visual layout quality — a well-structured card may communicate more clearly than its text similarity score implies. The single-domain setting (software documentation) may favour retrieval-heavy pipelines over those that require multi-step reasoning.

A structural limitation of comparing BERTScore F1 across layers of different lengths is that R₀ (three concatenated chunks, ~900 tokens) will naturally score lower on Precision than R₁ (a synthesised answer, ~60–100 tokens), because many of R₀'s tokens have no counterpart in the short reference answer. A positive Δ₁ on F1 therefore conflates genuine semantic improvement with the mechanical effect of length reduction. We address this by reporting Precision and Recall separately at each layer (Section 3.2), which allows readers to distinguish condensation effects from information loss. In this dataset, the Recall delta (Δ₁ᴿ = +0.0073) confirms that the F1 gain reflects genuine selectivity improvement rather than mere truncation.

This work deliberately scopes out security evaluation of the MCP+A2A pipeline. MCP tool security is an active and serious research area in its own right: a taxonomy of 25 MCP vulnerability categories has been published, empirical work suggests that deploying ten MCP plugins creates a 92% probability of exploitation, and OWASP has released an MCP-specific Top 10 [11, 14]. A rigorous security evaluation of agentic pipelines — covering prompt injection, tool misuse, and supply-chain risks — represents important future work that is orthogonal to the fidelity evaluation presented here.

### 6.6 Multimodal Evaluation

A natural extension of this work is to evaluate R₂ not through its serialised JSON text but through its rendered visual form. Screenshotting the Streamlit UI and passing it to a vision-capable judge model (e.g., GPT-4o Vision) with a structured rubric would yield a perceptual fidelity score that captures layout quality, code block formatting, and visual emphasis — dimensions that the JSON-text proxy cannot measure. This direction would also enable LLM-as-a-Judge [13] to be applied meaningfully at the A2UI layer, where visual structure is part of the communication. We leave this to future work, along with extending the test set beyond n=15 and validating judge scores against human raters.

---

## 7. Conclusions

We introduced _layer-wise fidelity scoring_ as an evaluation protocol for multi-layer agentic pipelines that terminate in a structured UI. Applied to a software documentation Q&A system built on MCP+A2A+A2UI, our results show that A2A synthesis substantially improves BERTScore F1 (+0.039) by raising Precision without sacrificing Recall — condensing retrieved chunks into a more precise answer while preserving coverage. The A2UI formatting step proves near-lossless on F1, with only minor Recall compression. Each layer of the MCP→A2A→A2UI stack makes a distinct and measurable contribution, a dynamic that aggregate end-to-end scoring cannot reveal. The protocol is lightweight — requiring only BERTScore and no human raters — reusable across domains, and exposes intra-pipeline quality dynamics that are invisible to black-box evaluation. By releasing our test set and scoring harness, we aim to provide a practical tool for the growing community building on standardised agent protocols such as MCP and A2A.

---

## References

[1] S. Yang et al., "A Survey of AI Agent Protocols," arXiv preprint arXiv:2504.16736, 2025.

[2] Anthropic, "Model Context Protocol (MCP)," Technical Specification, Nov. 2024. [Online]. Available: https://modelcontextprotocol.io

[3] A. Ehtesham, A. Singh, G. K. Gupta, and S. Kumar, "A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)," arXiv preprint arXiv:2505.02279, 2025.

[4] M. A. Jayanti and X. Y. Han, "Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration," arXiv preprint arXiv:2601.11595, 2026.

[5] B. Yan et al., "Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems," arXiv preprint arXiv:2502.14321, 2025.

[6] C. C. Liao, D. Liao, and S. S. Gadiraju, "AgentMaster: A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis," in _Proc. EMNLP 2025: System Demonstrations_, arXiv:2507.21105, 2025.

[7] P. P. Ray, "A Survey on Model Context Protocol: Architecture, State-of-the-Art, Challenges and Future Directions," _TechRxiv_, doi: 10.36227/techrxiv.174495492, Apr. 2025.

[8] A. Singh, A. Ehtesham, S. Kumar, and T. T. Khoei, "A Survey of the Model Context Protocol (MCP): Standardizing Context to Enhance Large Language Models (LLMs)," _Preprints.org_, 2025.

[9] S. S. K. A. Tokal, V. Jha, A. Eswaran, P. Jayachandran, and Y. Simmhan, "AgentX: Towards Orchestrating Robust Agentic Workflow Patterns with FaaS-hosted MCP Services," arXiv preprint arXiv:2509.07595, 2025.

[10] H. Derouiche, Z. Brahmi, and H. Mazeni, "Agentic AI Frameworks: Architectures, Protocols, and Design Challenges," arXiv preprint arXiv:2508.10146, 2025.

[11] J.-N. Hilgert, C. Jakobs, M. Külper, M. Lambertz, A. Mahr, and E. Padilla, "Chances and Challenges of the Model Context Protocol in Digital Forensics and Incident Response," arXiv preprint arXiv:2506.00274, 2025.

[12] T. Zhang et al., "BERTScore: Evaluating Text Generation with BERT," in _Proc. ICLR 2020_, 2020.

[13] L. Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," in _Proc. NeurIPS 2023_, 2023.

[14] S. Mitra, "The Agent Protocol Stack: Why MCP + A2A + A2UI Is the TCP/IP Moment for Agentic AI," Personal technical blog (grey literature, Tier 2–3 per MLR classification), Jan. 2026. [Online]. Available: https://subhadipmitra.com/blog/2026/agent-protocol-stack/

[15] V. Garousi, M. Felderer, and M. V. Mäntylä, "Guidelines for Including Grey Literature and Conducting Multivocal Literature Reviews in Software Engineering," _Information and Software Technology_, vol. 106, pp. 101–121, 2019.

[16] Google, "Agent2Agent (A2A) Protocol — Official Specification v1.0," a2a-protocol.org, 2025. [Online]. Available: https://a2a-protocol.org/latest/

[17] Google, "A2UI Protocol — Official Specification v0.8," a2ui.org, 2025. [Online]. Available: https://a2ui.org/
