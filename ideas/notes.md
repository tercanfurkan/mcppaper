## MCP strengths, weaknesses, advancements, innovations

- building on strengths, acknowledging weaknesses and hardening weaknesses using best practices and new usage patterns (e.g. code execution with MCP, introducing code as reusable functions using skills

- [What's the relation of this to MCP?]using compaction, sub-agent arcitecutre and agentic memory as structured note taking outside of the context window, to optimize context delivery to maximize the likelyhood of the desired outcome: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

- MCP and using self optimizing context strageties (e.g dynamically tuning context parameters, dynamically constructing context per query using adaptive context construction policies with Markov Decision Process or Reinforecement Learning)

- context lazy loading and intelligent caching of hot, warm, cold context with appropriate TLLs

- performance metrics (per context source?), tracking, logging of context retreival. Context Provenance Protocol - How do you trace where a piece of context came from, how it was transformed, and who touched it? Critical for debugging, compliance, and trust. MCP doesn’t track provenance.

What can & cannot be done with MCP, what are the necessary improvements for MCP?

MCP already de-facto. Question is how to increase MCP maturity? What should be the next advancements, optimizations, improvements which MCP can impact in the Agentic AI engineering? What extensions does MCP need?

- building the infrastructure for agent-to-agent communication or the communication infrastructure for Agentic AI

- exposing AI agents as MCP tools as appose to using A2A. What's the use-case? https://docs.langchain.com/langsmith/server-mcp#expose-an-agent-as-mcp-tool

- Observability crossing layers: distributed tracing for the Agentic AI communication between separate layers, e.g. LLM, agent, MCP, A2A.

- Governance: monitor, observe and intervene agents and MCP interactions for policy violations.

- Do we need separate concerns wihtin the MCP ecosystem? Should things be divided into separate layers? e.g. is context delivery (MCP) really the same layer as tool execution (also MCP)?

- Phased Adoption Roadmap for Agent Interoperability, MCP sits in stage 1, well-suited for use cases focused on tool invocation, deterministic execution, and typed input/output. This stage establishes a foundation for context enrichment in single-model systems.

- The A survey on model context protocol: Architecture, state-of-the-art, challenges and future directions paper tackes the state-of-the-art MCP implementations, but what are the state-of-the-art end-to-end agentic AI and MCP interactions ((e.g. code execution with MCP, introducing code as reusable functions using skills)?

- Relevant work on MCP security aspect: Adversa AI published a taxonomy of 25 MCP vulnerability categories. VentureBeat reported on Pynt’s research showing that deploying just ten MCP plugins creates a 92% probability of exploitation. OWASP published an MCP-specific Top 10. And a supply chain worm called Shai-Hulud 2.0 re-emerged in November specifically targeting developer pipelines that use MCP.

- Don’t Ship A2A Until You Need It
  This is my most controversial take: A2A solves a real problem — but it’s a problem most teams haven’t hit yet.

If your agents are all within the same organization, running in the same infrastructure, and you control the entire pipeline - you don’t need a cross-organization agent communication protocol. Use simpler orchestration (LangGraph, CrewAI, direct function calls). The overhead and attack surface of A2A aren’t justified.

A2A becomes essential when:

Agents from different organizations need to collaborate
You’re building a marketplace of agent capabilities
You need formal task lifecycle management across trust boundaries
Agents run on different platforms and can’t share memory or tools
If none of those apply, simpler orchestration patterns will serve you better while the protocol matures.
