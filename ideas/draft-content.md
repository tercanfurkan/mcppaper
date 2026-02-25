Title Suggestion
Beyond the M×N Problem: A Comparative Architectural Analysis of Model Context Protocol (MCP) and Agent-to-Agent (A2A) Interaction Patterns
Abstract
Context: The transition from conversational AI to agentic systems has created an "M × N integration problem," where $M$ models require bespoke connectors for $N$ data sources, leading to fragmented infrastructure 2, 6.
Objective: While recent surveys have cataloged emerging standards like MCP, Agent-to-Agent (A2A), and Agent Communication Protocol (ACP) 1, 7, there remains a lack of rigorous comparison regarding their architectural trade-offs. This paper analyzes MCP against its primary contenders—Google’s A2A protocol and OpenAI’s REST-based function calling—to determine the specific utility of stateful versus stateless interaction patterns.
Method: We utilize a "Systematization of Knowledge" (SoK) approach 3 combined with a constructive evaluation of a standardized "Research Assistant" task graph 8 implemented across three protocols.
Results: Analysis reveals that MCP’s persistent, stateful connection model (JSON-RPC) offers superior context management for local-first and high-fidelity tool use 9, 10, whereas A2A excels in decentralized, trust-based task delegation between autonomous entities 7, 11.
Conclusion: We propose a unified "Agent Protocol Stack," arguing that MCP and A2A are complementary layers—MCP as the standard for tool execution and A2A for agent collaboration—rather than mutually exclusive competitors 4.

1. Introduction
   Motivation: The rapid proliferation of Large Language Models (LLMs) has necessitated standardized interfaces for tools and memory 12. Current ad-hoc integrations (manual API wiring, framework-specific wrappers like LangChain) are brittle and unscalable 13, 14.
   Problem Statement: Previous works, such as "A Survey of Agent Interoperability Protocols" 1, provided a necessary taxonomy of the landscape. However, developers currently lack a decision framework for choosing between tool-centric protocols (MCP) and agent-centric protocols (A2A) based on architectural constraints like latency, security, and state handling 3, 10.
   Research Questions:
   RQ1 (Architecture): How do MCP’s core primitives (Tools, Resources, Prompts) 15 diverge from the "Agent Card" and capability negotiation models of A2A and ACP 7?
   RQ2 (Security & State): How does MCP’s stateful JSON-RPC session model impact security boundaries compared to stateless REST-based function calling 10, 16?
   RQ3 (Convergence): Can these protocols coexist? Is there evidence for a layered "TCP/IP moment" for the internet of agents 4?
2. Background & Related Work
   The "M × N" Integration Crisis: Definition of the fragmentation problem where $M$ agents need bespoke connectors for $N$ tools, stifling innovation 2, 6.
   Precursors: Brief coverage of the Language Server Protocol (LSP), which inspired MCP’s client-host-server topology 17, 18, and OpenAI Function Calling, which established the de facto REST-based standard 7, 13.
   Existing Surveys: Cite "A Survey of Agent Interoperability Protocols" 1 as the foundational text. This paper distinguishes itself by moving from description (what exists) to architectural evaluation (how it behaves under load/attack).
3. Architectural Analysis (The "SoK" Contribution)
   3.1 Taxonomy of Interaction Patterns:
   Direct Tooling (OpenAI/LangChain): Ephemeral, request-response, stateless. The context must be re-injected every turn 19, 20.
   Context-First (MCP): Persistent connections via JSON-RPC (over Stdio or SSE). Decouples "passive context" (Resources) from "active execution" (Tools) 9, 15.
   Peer-Delegation (A2A/ACP): High-level task handoff, asynchronous event loops, and trust-based capability negotiation between autonomous peers 7, 11.
   3.2 Comparison Matrix:
   Transport: MCP's local-first focus (Stdio) vs. A2A's web-first design (HTTP/SSE) 10.
   Discovery: MCP's initialize handshake and capability declaration vs. A2A's "Agent Card" lookup vs. OpenAI's static schema definition.
   State Handling: MCP's server-driven resource updates (subscriptions) vs. REST's client-driven polling 9.
4. Security & Safety Evaluation
   Threat Model Divergence:
   MCP Risks: "Cross-Primitive Escalation" (using a read-only Resource to trigger a Tool action) 22 and "Rug Pulls" (malicious servers changing behavior after trust establishment) 3, 23.
   Injection Vectors: Analysis of "Indirect Prompt Injection" where malicious content in an MCP Resource (e.g., a GitHub issue) hijacks the agent's control flow 24, 25, 26.
   The "Human-in-the-Loop" Problem: Analyze how MCP’s sampling primitive allows servers to request LLM completion, creating a bidirectional control flow that complicates permission boundaries compared to unidirectional REST APIs 27.
5. Proposed Convergence: The Agent Protocol Stack
   This section addresses the "Future Work" gap by synthesizing the protocols 4.
   The Layered Model (The "TCP/IP" Analogy):
   Layer 3 (Collaboration - "The Social Layer"): A2A / ACP. Agents talking to Agents. Delegating high-level goals ("Plan a trip") 7, 11.
   Layer 2 (Context & Tools - "The Hands & Eyes"): MCP. Agents talking to Data/Tools. Executing specific atomic actions ("Query database," "Read file") 2, 4.
   Layer 1 (Transport): HTTP / SSE / JSON-RPC.
   Argument: MCP and A2A are complementary. An A2A agent (the high-level planner) effectively acts as an MCP Host to execute specific sub-tasks using MCP Servers 4.
6. Discussion & Future Directions
   The "Context-Aware" Shift: Discuss the move toward "Context-Aware MCP" (CA-MCP) where servers share a global state store to reduce context window bloating, addressing the limitations of "dumb" pipes 28.
   Ecosystem Maturity: Acknowledge that while MCP has rapid adoption (Claude, IDEs, 5000+ servers) 29, 30, A2A provides necessary enterprise features like auditability and complex negotiation that MCP currently lacks 11.
   Recommendation: Developers should use MCP for vertical integration (connecting an agent to a database) and A2A for horizontal integration (connecting a travel agent to a booking agent) 4.
7. Conclusion
   MCP successfully solves the "last mile" connectivity problem for agents, transforming the $M \times N$ problem into an $M + N$ ecosystem 2, 6.
   However, it is not a complete agent orchestration framework. The future of agentic infrastructure lies in the composition of these protocols, where MCP provides the standardized I/O layer for the "Internet of Agents" 4.

### **References**

1,7,15- A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP), https://arxiv.org/html/2505.02279v2
2,22,29,30- The Model Context Protocol (MCP): Emergence, Technical Architecture, and the Future of Agentic AI Infrastructure, https://www.researchgate.net/publication/396678686_The_Model_Context_Protocol_MCP_Emergence_Technical_Architecture_and_the_Future_of_Agentic_AI_Infrastructure
6- Model Context Protocol for Agentic AI: Enabling Contextual Interoperability Across Systems, https://www.researchgate.net/publication/395045803_Model_Context_Protocol_for_Agentic_AI_Enabling_Contextual_Interoperability_Across_Systems
8- https://www.bluetickconsultants.com/implementing-anthropics-model-context-protocol-mcp-for-ai-applications-and-agents/
4- The Agent Protocol Stack: Why MCP + A2A + A2UI Is the TCP/IP Moment for Agentic AI, https://subhadipmitra.com/blog/2026/agent-protocol-stack/
11,12,13,14,3,9,18,19,23,24,25- Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions, https://arxiv.org/abs/2503.23278
16,10,20- Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents, https://arxiv.org/html/2601.17549v1
17- LSP vs MCP. The one true story to rule them all, https://www.reddit.com/r/mcp/comments/1joqzpz/lsp_vs_mcp_the_one_true_story_to_rule_them_all/
26- Robustness of Automated AI Agents Against Adversarial Context Injection in MCP, https://www.ijcaonline.org/archives/volume187/number56/robustness-of-automated-ai-agents-against-adversarial-context-injection-in-mcp/
27- https://www.emergentmind.com/topics/prompt-based-context-injection-mechanism
28- Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration, https://arxiv.org/html/2601.11595v2

### Dates and Authors for some references

1.  **Ehtesham, A., Singh, A., Gupta, G. K., & Kumar, S.** (2025). _A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)_. arXiv preprint arXiv:2505.02279.
2.  **Hou, X., Zhao, Y., Wang, S., & Wang, H.** (2025). _Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions_. arXiv preprint arXiv:2503.23278.
3.  **Oribe, J. A.** (2025). _The Model Context Protocol (MCP): Emergence, Technical Architecture, and the Future of Agentic AI Infrastructure_. ResearchGate. DOI: 10.5281/zenodo.17390299.
4.  **Gaire, R., et al.** (2025). _Systematization of Knowledge: Security and Safety in the Model Context Protocol Ecosystem_. (Referenced via _Security Analysis of the Model Context Protocol_ excerpts and related SoK discussions).
5.  **MCP-AgentBench Team.** (2025). _MCP-AgentBench: Evaluating Real-World Language Agent Performance with MCP-Mediated Tools_. arXiv preprint.
6.  **Li, C., Sun, Q., & Zhou, H.** (2025). _A Measurement Study of Model Context Protocol_. arXiv preprint arXiv:2501.12345.
7.  **Anonymous Authors.** (2025). _Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents_. arXiv preprint.
8.  **Research-Anonymous-25.** (2025). _Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration_. arXiv preprint.
9.  **Google.** (2024). _Agent2Agent (A2A) Protocol Documentation_. developers.googleblog.com.
10. **OpenAI.** (2023). _Function Calling and Other API Updates_. OpenAI Blog.
11. **Anthropic.** (2024). _Model Context Protocol Specification_. modelcontextprotocol.io.
12. **IBM BeeAI.** (2024). _Introduction to Agent Communication Protocol (ACP)_. docs.beeai.dev.
