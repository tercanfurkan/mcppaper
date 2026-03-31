# Yellow Highlights — A survey of agent interoperability protocols- Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)

**Reference:** A SURVEY OF AGENT INTEROPERABILITY PROTOCOLS: MODEL  arXiv:2505.02279v2

## Abstract

Large language model (LLM)-powered autonomous agents demand robust, standardized protocols to integrate tools, share contextual data, and coordinate tasks across heterogeneous systems. Ad-hoc integrations are difficult to scale, secure, and generalize across domains. This survey examines four emerging agent communication protocols: Model Context Protocol (MCP), Agent Communication

---

## Highlights by Section

### ABSTRACT

- **p. 1** — Large language model (LLM)-powered autonomous agents demand robust, standardized protocols to integrate tools, share contextual data, and coordinate tasks across heterogeneous systems. Ad-hoc integrations are difficult to scale, secure, and generalize across domains.

- **p. 1** — MCP provides a JSON-RPC client-server interface for secure tool invocation and typed data exchange.

- **p. 1** — The protocols are compared across multiple dimensions, including interaction modes, discovery mechanisms, communication patterns, and security models.

- **p. 1** — a phased adoption roadmap is proposed: beginning with MCP for tool access,

- **p. 1** — Keywords

- **p. 1** — Interoperability Protocols,

### Introduction

- **p. 1** — Large Language Models (LLMs) have become central to modern artificial intelligence, powering autonomous agents that operate across cloud, edge, and desktop environments [1, 2]. These agents [3] ingest contextual information,

- **p. 2** — execute tasks, and interact with external services or tools. However, inconsistent and fragmented interoperability practices make it difficult to integrate, secure, and scale communication among LLM-driven agents [4]. Interoperability (the ability of distinct agents and systems to discover capabilities, exchange context, and coordinate actions seamlessly) is essential for modular, reusable, and resilient multi-agent [5] workflows. Standardized protocols reduce development overhead, improve security, and enable cross-platform collaboration. Clear, universally adopted standards remain nascent.

- **p. 2** — Model Context Protocol (MCP): A JSON-RPC client–server interface for secure context ingestion and structured tool invocation. MCP streamline the integration of large language models (LLMs) with external data sources and tools. MCP addresses the challenges of fragmented and custom-built integrations by providing a universal, model-agnostic interface for AI systems to access and interact with diverse resources [6, 7, 8]. MCP was launched by Anthropic in Novemeber 2024.

- **p. 2** — Architectural details, integration approaches, communication patterns, and security considerations are reviewed for each protocol. A comparison highlights trade-offs in interaction modes, discovery mechanisms, communication models, and security frameworks. A phased adoption roadmap sequences MCP, A2A, ACP, and ANP to guide progressive deployment in real-world agent ecosystems.

### Challenges and Solutions in Agent Protocol Interoperability

- **p. 2** — Challenges and Solutions in Agent Protocol Interoperability

- **p. 2** — Lack of Context Standardization for LLMs: Large Language Models (LLMs) require contextual grounding to produce accurate outputs. However, existing application architectures provide no unified mechanism to deliver structured context to LLMs, leading to ad hoc tool integrations and unreliable behavior. Solution: The Model Context Protocol (MCP) addresses this by standardizing how applications deliver tools, datasets, and sampling instructions to LLMs, akin to a USB-C for AI. It supports flexible plug-and-play tools, safe infrastructure integration, and compatibility across LLM vendors.

### Background and Related Work

- **p. 4** — Early Symbolic Agent Languages—Evolution of Agent Communication Standards

- **p. 4** — Service-Oriented Integrations and Retrieval-Augmented Generation

- **p. 4** — LLM Agents and Function Calling The rapid evolution of large language models (LLMs) such as GPT-3.5, GPT-4, Claude, and Gemini has fundamentally transformed agent design by enabling zeroand few-shot understanding of complex natural language instructions without bespoke rule engines [2]. These foundation models can parse user intent, plan multi-step workflows, and

- **p. 5** — maintain dialogue coherence across diverse domains, opening the door to “LLM agents” that combine linguistic reasoning with external tool execution. To operationalize tool use, OpenAI introduced function calling in 2023, a lightweight protocol whereby an LLM can output a JSON-formatted signature corresponding to a predefined API endpoint [29]. Under this paradigm, developers supply the model with a catalog of function definitions—each described by a name, JSON schema for arguments, and descriptive help text—and the model decides at generation time whether to invoke a function, emitting well-formed JSON that can be parsed and executed by downstream systems. This approach unifies natural language understanding and action invocation, enabling real-time data fetches, database queries, and transactional operations from within a single LLM response. Building on this core capability, several frameworks have emerged to simplify agent development: • LangChain provides abstractions for chaining LLM calls, memory buffers, and function invocation in modular workflows, with built-in support for retrievers, vector stores, and agent loops [30]. • LlamaIndex (formerly GPT Index) focuses on integrating LLMs with custom knowledge bases, offering document loaders, index wrappers, and a “tool registry” that maps user queries to API calls [31]. • The OpenAI Plugin Store enables third-party tool providers to register plugins that expose RESTful interfaces, metadata, and authentication flows, which can be discovered and invoked by any model with plugin access [32]. Despite these advances, current function-calling ecosystems suffer from several limitations. Tool definitions are typically static: agents must be re-initialized whenever new APIs are added or schemas change, preventing truly dynamic discovery. Security boundaries—such as authentication tokens, rate limits, and access control—are adhoc and framework-specific, increasing the risk of unauthorized calls. Moreover, each framework employs its own metadata conventions, hindering cross-framework reuse of tools and requiring bespoke adapters for interoperability [33]. Addressing these challenges requires protocol-level standards that prescribe a common schema for function metadata, dynamic capability negotiation, and end-to-end security guarantees across heterogeneous LLM agent platforms.

- **p. 5** — Orchestration and Lightweight Agent Frameworks Recent advances have extended the capabilities of LLMs beyond reasoning to include orchestration of external tool invocation. Toolformer employs a self-supervised masking strategy that exposes potential API calls during pretraining, enabling the model to learn when and how to invoke functions as part of its text generation [34]. ReAct interleaves chain-of-thought reasoning with explicit action calls, allowing models to alternate between “thinking” steps and tool invocations based on intermediate observations [35]. These approaches unify reasoning and action at the single-agent level but do not address peer discovery or multi-agent coordination.

- **p. 5** — Protocol Evolution Timeline

- **p. 5** — trajectory of interoperability standards and protocols over time. Three distinct evolutionary phases emerge: 1. Symbolic and SOA Foundations (1993–2006): Early interoperability standards such as KQML and FIPA- ACL set formal semantic foundations. Subsequent developments in Web Services and Enterprise Service Bus (ESB) frameworks streamlined enterprise integration but introduced complexity and limited flexibility. 2. Retrieval and In-Model Action (2020–2023): Marked by the introduction of Retrieval-Augmented Generation (RAG), this phase leveraged vector-based retrieval to enhance the grounding of language model outputs. Innovations like Function Calling, Toolformer, and ReAct enabled LLMs to directly translate reasoning into executable API calls, significantly advancing agent autonomy and flexibility.

### 3. Protocol-Oriented Interoperability (2024–2025): The current phase emphasizes lightweight, standardized

- **p. 6** — Protocol-Oriented Interoperability (2024–2025): The current phase emphasizes lightweight, standardized protocols such as MCP, ACP, ANP, and A2A. These protocols address previous limitations by enabling dynamic discovery, secure communication, and decentralized collaboration across heterogeneous agent systems, promoting scalability and robust interoperability.

### MCP

- **p. 6** — MCP

- **p. 6** — Client Application (Host) The Client Application (Host) serves as the initiator of interactions in the MCP ecosystem. It is responsible for managing connections to one or more MCP Servers and orchestrating communication workflows in accordance with protocol specifications. In practice, the client initializes sessions, requests and processes the four core primitives Resources, Tools, Prompts, and Sampling, and handles asynchronous notifications related to server-side events. The client must also implement robust error-handling routines to gracefully manage communication failures or timeout conditions, ensuring reliable coordination with remote MCP Servers.

- **p. 8** — MCP Server (Providing Context & Capabilities) The MCP Server functions as the provider of data, services, and interaction templates that the client can utilize to enrich LLM-based workflows. It exposes and manages contextual Resources, executes external operations via Tools, defines reusable Prompts for consistent interaction patterns, and optionally delegates text-generation tasks through Sampling. Beyond serving requests, the server is responsible for enforcing access control policies, maintaining operational security, and emitting notifications that reflect changes in its available capabilities. This provider-side architecture complements the client’s orchestration logic by modularizing access to complex or dynamic resources.

- **p. 8** — Core Components The Model Context Protocol is composed of several layered abstractions that govern the structure and semantics of communication. At the foundation lies the Protocol Layer, which defines the semantics of message exchange using the JSON-RPC 2.0 specification. It ensures that each request is linked to a corresponding response and that all interactions conform to predictable patterns. Above this, the Transport Layer handles the physical transmission of messages between the client and server, supporting both local communication via Stdio and network-based channels such as HTTP with optional Server-Sent Events (SSE). At the highest abstraction, MCP organizes messages into four types: Requests, which are calls expecting replies; Results, which are successful responses to earlier requests; and Errors, which indicate failures or invalid invocations. A fourth type, Notifications, is used for asynchronous updates that do not require a client acknowledgment.

- **p. 8** — MCP Server Core Capabilities The MCP Server offers four core capabilities Tools, Resources, Prompts, and Sampling each mapped to a distinct control model that governs the interaction between the client, the server, and the LLM. Tools are model-controlled capabilities that allow the LLM to invoke external APIs or services, often automatically and sometimes with user approval. This facilitates seamless integration with third-party systems and streamlines access to real-world data and operations. Resources are application-controlled elements, such as structured documents or contextual datasets, that are selected and managed by the client application. They provide the LLM with tailored, task-specific inputs and enable context-aware completions. Prompts are user-controlled templates defined by the server but selected by end-users through the client interface. These reusable prompts promote consistency, reduce redundancy, and support repeatable interaction patterns. Sampling is server-controlled and allows the MCP Server to delegate the task of generating LLM completions to the client. This supports sophisticated agentic workflows and enables fine-grained oversight over the model’s generative process, including the ability to adjust temperature, length, and other sampling parameters dynamically.

- **p. 8** — MCP Connection Lifecycle The Model Context Protocol (MCP) defines a three-phase lifecycle for client–server interactions, designed to ensure robust session management, secure capability negotiation, and clean termination. These phases Initialization, Operation, and Shutdown correspond to the temporal sequence of communication between the Client Application and MCP Server. Initialization begins by establishing protocol compatibility and exchanging supported capabilities. During version negotiation, the client and server agree on the highest mutually supported protocol version. This is followed by a capability exchange, in which both sides advertise optional features—such as sampling, prompts, tools, and logging—that can be used during the session. The phase concludes with a notifications/initialized message sent by the client after receiving the server’s initialize response, signaling readiness to proceed to operational communication. Operation represents the core active phase, during which the client and server exchange JSON-RPC method calls and notifications in accordance with the negotiated capabilities. Both parties are expected to adhere strictly to the features agreed upon during initialization, ensuring compatibility and predictability. Each task invocation may include a configurable timeout, and if a response is not received within that window, the client may issue a cancellation notification to prevent resource exhaustion or stale execution threads. Shutdown ensures a clean and predictable end to the session. Either party may initiate termination by closing the transport layer typically HTTP or stdio which signals the end of communication. Upon shutdown, both client and server are responsible for resource cleanup, including the removal of active timeouts, cancellation of subscriptions,

- **p. 9** — and deallocation of any spawned child processes. After this point, no new protocol messages should be sent, with the exception of essential diagnostics like ping or log flush events.

### Comparison of Agent Protocols

- **p. 17** — structured analysis highlights their architectural choices, messaging formats, discovery methods, session models, and intended use cases, offering insights into their suitability across diverse deployment scenarios.

### Phased Adoption Roadmap for Agent Interoperability

- **p. 17** — Stage 1 – MCP for Tool Invocation The initial phase involves adopting the Model Context Protocol (MCP) to enable structured and secure interaction between large language models (LLMs) and external tools or resources. MCP operates over a JSON-RPC-based client-server model and is well-suited for use cases focused on tool invocation, deterministic execution, and typed input/output. This stage establishes a foundation for context enrichment in single-model systems.
