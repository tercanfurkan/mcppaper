# an academic literature review & design validation study around agent protocols like MCP, A2A, function calling, GraphQL, etc and evaluating & validating their architectures and their usage in Agentic AI workflows

Let’s structure this into two parts:

1. **Literature review framing (what exists + gaps)**
2. **A concrete design + validation study (what you would actually build and measure)**

---

# 1. Literature Review: How to Frame the Field

## A. Core Problem Statement

You’re studying:

> _How different agent-to-tool and agent-to-agent protocols affect reliability, security, and performance of agentic AI workflows in enterprise systems._

This sits at the intersection of:

- Distributed Systems
- Human-Computer Interaction
- Information Retrieval
- Cybersecurity

---

## B. Protocol Landscape You Should Cover

You want to compare _interaction paradigms_, not just tools.

### 1. LLM-Native Tool Use

- Function calling (OpenAI-style)
- Structured tool invocation

Characteristics:

- Tight coupling to model
- Schema-driven
- Low latency

---

### 2. MCP (Model Context Protocol)

- Standardized tool interface
- Externalized capabilities
- Decoupled architecture

Used by companies like Anthropic

---

### 3. A2A (Agent-to-Agent Protocols)

- Multi-agent communication
- Delegation patterns

Still emerging, loosely defined in literature

---

### 4. Web/Service Protocols

- REST
- GraphQL

Example:
→ GraphQL

Characteristics:

- Mature ecosystem
- Not designed for LLM reasoning

---

## C. Key Dimensions from Literature

You’ll want to extract evaluation axes like:

### 1. Expressiveness

- Can the protocol represent complex workflows?

### 2. Controllability

- Can you constrain behavior?

### 3. Observability

- Can you trace decisions?

### 4. Security Surface

- Vulnerability to prompt injection, misuse

### 5. Composability

- Can systems scale across domains?

---

## D. Gaps in Existing Research

This is where your contribution becomes strong.

### Gap 1: Lack of End-to-End Evaluation

Most papers evaluate:

- single-step tool use
- synthetic benchmarks

Missing:

- multi-step enterprise workflows

---

### Gap 2: No Security-Centric Evaluation

Almost no formal evaluation of:

- prompt injection across protocols
- tool misuse risks

---

### Gap 3: Weak Cost & Latency Analysis

Academic work rarely considers:

- token cost
- API latency
- system throughput

---

### Gap 4: Lack of Failure Taxonomies

Industry knows failure modes:

- hallucinated tool success
- state drift

Academia hasn’t formalized them well

---

# 2. Proposed Study: Design + Validation

Now the interesting part—what you actually _build_.

---

## A. Research Questions

You can structure around 3–4 strong questions:

### RQ1:

How do different agent protocols affect **task success rate and reliability**?

### RQ2:

What is the **security risk profile** of each protocol under adversarial input?

### RQ3:

How do protocols differ in **latency, cost, and scalability**?

### RQ4:

How does protocol design influence **debuggability and observability**?

---

## B. Experimental Setup

### 1. Controlled Workflow Scenarios

Design 3–5 realistic enterprise workflows inspired by companies like F-Secure:

#### Example workflows:

- Partner onboarding (multi-step, transactional)
- Incident triage (security-sensitive)
- Reporting pipeline (data-heavy)
- Ticket resolution (human + AI loop)

---

### 2. Implement Each Workflow Across Protocols

For each workflow, implement using:

- Function calling
- MCP-style architecture
- GraphQL-based integration
- A2A multi-agent setup

💡 Important:
Keep everything constant except the **protocol layer**

---

### 3. Shared Components

Control variables:

- Same LLM (e.g., Claude or GPT)
- Same tools
- Same data
- Same prompts (as much as possible)

---

## C. Evaluation Metrics

---

### 1. Reliability Metrics

- Task success rate (%)
- Number of retries
- Error propagation depth

---

### 2. Security Metrics

Inject adversarial inputs:

- Prompt injection
- Malicious tool instructions

Measure:

- Unauthorized actions
- Data leakage incidents

---

### 3. Performance Metrics

- Latency per task
- Token usage
- API calls per workflow

---

### 4. Observability Metrics

Qualitative + quantitative:

- Trace completeness
- Debug time (human study)

---

### 5. Consistency Metrics

- Determinism across runs
- Variance in outputs

---

## D. Failure Mode Analysis

This is where your paper can stand out.

Build a taxonomy like:

- Tool misuse
- Hallucinated success
- State inconsistency
- Infinite loops

Then compare:
→ Which protocol fails _how_

---

## E. Hypotheses (Example)

You should state these explicitly:

- MCP → higher modularity, better security boundaries, higher latency
- Function calling → faster, less controllable
- GraphQL → robust but brittle for LLM reasoning
- A2A → flexible but hardest to debug

---

## F. Methodology Add-On (Strong Academic Angle)

### 1. Mixed-Methods Approach

Combine:

- Quantitative benchmarks
- Qualitative developer experience study

---

### 2. Human Evaluation

Ask engineers:

- Which system is easier to debug?
- Which feels safer?

---

## G. Expected Contributions

Your paper can contribute:

### 1. A comparative framework for agent protocols

### 2. A failure taxonomy for agentic systems

### 3. Security evaluation methodology

### 4. Practical design guidelines

---

# 3. Why This Matters (Industry Relevance)

Companies like:

- F-Secure
- OpenAI
- Google

are all converging on the same problem:

> “How do we make LLMs interact with real systems safely and reliably?”

Right now:

- Protocol choice is mostly **opinion-driven**
- Not evidence-based

Your study could:
→ Turn this into **engineering science**

---

# Final Insight

If you position this well, your thesis/paper becomes:

> **“From prompt engineering to protocol engineering”**

That’s the real shift happening in agentic AI.

---

If you want, I can:

- Help you turn this into a **full MSc thesis proposal (with structure + timeline)**
- Or design a **minimal experimental prototype architecture** you could realistically build in ~6–8 weeks
