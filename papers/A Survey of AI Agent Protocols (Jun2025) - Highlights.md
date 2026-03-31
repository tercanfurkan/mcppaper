# Yellow Highlights — A Survey of AI Agent Protocols (Jun 2025)

**Reference:** Yang et al. (2025). _A Survey of AI Agent Protocols._ arXiv:2504.16736v3. Shanghai Jiao Tong University.

## Abstract

The rapid development of large language models (LLMs) has led to the widespread deployment of LLM agents across diverse industries, including customer service, content generation, data analysis, and even healthcare. However, as more LLM agents are deployed, a major issue has emerged: there is no standard way for these agents to communicate with external tools or data sources. This lack of standardized protocols makes it difficult for agents to work together or scale effectively, and it limits their ability to tackle complex, real-world tasks. A unified communication protocol for LLM agents could change this. It would allow agents and tools to interact more smoothly, encourage collaboration, and triggering the formation of collective intelligence. In this paper, we provide the first comprehensive analysis of existing agent protocols, proposing a systematic two-dimensional classification that differentiates context-oriented versus inter-agent protocols and general-purpose versus domain-specific protocols. Additionally, we conduct a comparative performance analysis of these protocols across key dimensions such as security, scalability, and latency. Finally, we explore the future landscape of agent protocols by identifying critical research directions and characteristics necessary for next-generation protocols. These characteristics include adaptability, privacy preservation, and group-based interaction, as well as trends toward layered architectures and collective intelligence infrastructures.

---

## Highlights by Section

### §1 Introduction

- **p. 3** — as the scope of application scenarios expands and agents from different vendors with different structures emerge, the interaction rules between agents and entities have grown complex. A critical bottleneck in this evolution is the absence of standardized protocols. This deficiency hinders agent interoperability with aforementioned resources (Qu et al., 2025; Patil et al., 2023; Liu et al., 2024), limiting their capability to leverage external functionalities. In addition, the lack of standardized protocols prevents seamless collaboration between agents from different providers or architectural backgrounds, thus limiting the scalability of agent networks. Ultimately, the ability of agents to solve more complex real-world problems is thereby limited.

- **p. 4** — a forward-looking perspective on the evolution of agent protocols, identifying short-, mid-, and long-term trends, including the shift toward evolvable, privacy-aware, and group-coordinated protocols, as well as the emergence of layered architectures and collective intelligence infrastructures.

### §2 Preliminaries

- **p. 6** — Emerging Implementation Frameworks The practical implementation of agent systems has been facilitated by specialized frameworks that provide developers with pre-built components for agent construction. LangChain and its extension LangGraph have become industry standards for agent development (LangChain, 2024), offering modular architectures that support sophisticated reasoning, planning, and multi-agent coordination. Microsoft’s Semantic Kernel framework has focused on bridging traditional software development with AI capabilities (Microsoft Learn, 2024), making it easier to integrate agent functionality into existing enterprise systems without complete architectural overhauls. This integration-focused approach has been particularly valuable for enterprises seeking to enhance existing workflows rather than replace them.

### §3.1.1 General-Purpose Protocols

- **p. 9** — MCP is a universal and open context-oriented protocol for connecting LLM agents to resources consisting of external data, tools and services in a simpler and more reliable way (Anthropic, 2024). The high standardization of MCP effectively addresses the fragmentation arising from various base LLMs and tool providers, greatly enhancing system integration. At the same time, the standardisation of MCP also brings high scalability to tool usage for LLM agents, making it easier for them to integrate a wide range of new tools. In addition, the client-server architecture of MCP decouples tool invocation from LLM responses, reducing the risk of data leakage.

### §3.1 Context-Oriented Protocols

- **p. 9** — Table 2: Overview of popular agent protocols.

### §3.1.1 General-Purpose Protocols

- **p. 9** — The utilisation of the MCP protocol for tool usage can be characterised by the presence of four distinct components, namely Host, Client, Server and Resource. • Host refers to LLM agents, responsible for interacting with users, understanding and reasoning through user queries, selecting tools, and initiating strategic context request. Each host can be connected to multiple clients.

- **p. 10** — Client is connected to a host and responsible for providing descriptions of available resources. The client also establishes a one-to-one connection with a server and is responsible for initiating executive context request, including requiring data, invoking tools, and so on. • Server is connected to the resource and establishes a one-to-one connection with the client, providing required context from the resource to the client. • Resource refers to data (e.g., local file systems), tools (e.g., Git), or services (e.g., search engines) provided locally or remotely. In the initial phase of a complete MCP invocation cycle, when faced with a user query, the host employs the LLMs’ understanding and reasoning capabilities to infer the context necessary to formulate a response to the query. Concurrently, the multiple clients connected to the host provide natural language descriptions of the available resources. Based on the information available, the host determines which resources to request context from and initiating a strategic context request to the corresponding client. In the request phase of the MCP invocation cycle, the client sends an executive context request to the corresponding server, encompassing operations such as data modifications or tool invocations. Upon receiving the client’s request, the server operates on the resources as specified and subsequently transmits the obtained context to the client, which then passes it on to the host. In the response phase of the MCP cycle, the host combines the context obtained to formulate a reply to the user query, thereby completing the cycle.

- **p. 10** — MCP represents a significant step toward standardizing interaction between LLM agents and external resources. By providing a unified protocol for context acquisition and tool invocation, MCP reduces fragmentation across both base LLM providers and resource interfaces. Its client-server architecture enhances interoperability, scalability, and privacy, making it a foundational framework for building robust and secure LLM agent systems.

### §4 Protocol Evaluation and Comparison

- **p. 18** — Protocol Evaluation

- **p. 18** — In the rapidly evolving landscape of agent communication protocols, static performance or functionality comparisons quickly become outdated due to the fast-paced iterations in this domain. For instance, MCP introduced in November 2024 initially lacked support for HTTP and authentication mechanisms.

- **p. 19** — Table 4: Overview of protocol evaluation from different dimensions. By early 2025, it incorporated HTTP Server-Sent Events (SSE) and authentication, and has since transitioned to HTTP Streaming. This evolution mirrors the progression from TCP/IP to HTTP in the internet era, highlighting continuous enhancements in functionality, performance, and security. Consequently, this section focuses on identifying the critical dimensions and challenges to consider when designing and evaluating LLM agent communication protocols, rather than proposing a specific evaluation benchmark. Drawing inspiration from the seven core metrics observed in the evolution of internet protocols—interoperability, performance efficiency, reliability, scalability, security, evolvability, and simplicity—we examine their applicability to LLM agent protocols.

### §4.1 Efficiency

- **p. 19** — As shown in Table 4, by delineating these evaluative dimensions, this section aims to provide a comprehensive understanding of the considerations essential for the effective design and assessment of LLM agent protocols, thereby contributing to the advancement of intelligent agent systems.

### §5 Use-Case Analysis

- **p. 26** — Use-case analyses of four protocols under the same user instruction shown at the top. The MCP architecture excels in simplicity and control but lacks flexibility. The central agent must be aware of all services and their interfaces, creating a high-dependency structure that may be difficult to scale or modify. Additionally, all communication must pass through the central agent, potentially creating a performance bottleneck.

### §5.4 Agora: Natural Language to Protocol Generation

- **p. 27** — each protocol has specific conditions and dependencies for successful application. 1) MCP employs a centralized agent (e.g., travel assistant) that sequentially invokes tools with clear interfaces to accomplish tasks. This approach works efficiently for well-defined workflows but may require central agent modification to adapt to new scenarios.

- **p. 28** — Each protocol’s applicability depends on factors such as the desired level of agent autonomy, communication flexibility, interface standardization, and the complexity of the tasks being performed. 6 Academic Outlook The development of agent protocols is progressing rapidly. This section outlines the expected evolution of the field in the short, medium, and long term, highlighting research trends, emerging challenges, and forward-looking visions.

### §6.1 Short-Term Outlook: From Static to Evolvable

- **p. 28** — Evaluation and Benchmarking. While various protocols have been proposed for different agent applications, a unified benchmark for evaluating their effectiveness remains less explored. Current efforts are converging toward designing evaluation frameworks that go beyond task success, incorporating aspects such as communication efficiency, robustness to environmental changes, adaptability, and scalability. The development of diverse simulation environments and standardized testbeds is expected to provide both controlled and open-ended scenarios, thereby facilitating fair and consistent comparisons across protocols.

### §6.3 Long-Term Outlook: From Protocols to Intelligence Infrastructure

- **p. 29** — Collective Intelligence

- **p. 29** — As agent protocols continue to mature, a compelling long-term direction is to explore the emergence of collective intelligence in large-scale, interconnected agent populations.

### §7 Conclusion

- **p. 29** — evaluating key performance dimensions such as efficiency, scalability, and security, we offer a practical reference for both practitioners and researchers.

- **p. 29** — This structured overview not only helps users better navigate the

- **p. 30** — growing ecosystem of agent protocols but also highlights the trade-offs and design considerations involved in building reliable, efficient, and secure agent systems.

- **p. 30** — Looking ahead, we envision the emergence of next-generation protocols, such as evolvable, privacy-aware, and group-coordinated protocols, as well as the emergence of layered architectures and collective intelligence infrastructures. The development of agent protocols will pave the way toward a more connected and collaborative agent ecosystemwhere agents and tools can dynamically form coalitions, exchange knowledge, and co-evolve to solve increasingly complex real-world problems. Much like the foundational protocols of the internet, future agent communication standards have the potential to unlock a new era of distributed, collective intelligence—reshaping how intelligence is shared, coordinated, and amplified across systems.
