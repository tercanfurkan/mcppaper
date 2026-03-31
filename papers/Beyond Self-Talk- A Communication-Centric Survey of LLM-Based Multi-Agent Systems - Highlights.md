# Yellow Highlights — Beyond Self-Talk- A Communication-Centric Survey of LLM-Based Multi-Agent Systems

**Reference:** Beyond Self-Talk: A Communication-Centric Survey of LLM-Based  arXiv:2502.14321v2

## Abstract

Large language model-based multi-agent systems have recently gained significant attention due to their potential for complex, collaborative, and intelligent problem-solving capabilities. Existing surveys typically categorize LLM-based multi-agent systems (LLM-MAS) according to their application domains or architectures, overlooking the central role of communication in coordinating agent behaviors and interactions.

---

## Highlights by Section

### Abstract

- **p. 1** — Key words large language model;

- **p. 1** — LLM-based multi-agent systems;

- **p. 1** — agent communication protocols

### 3.3 Communication Protocol

- **p. 6** — communication architecture decides who can talk to whom and the communication goal clarifies why they talk, a dedicated communication protocol specifies how the messages actually flow between agents and external systems. Standardized protocols are now emerging that make LLM-MAS deployments portable, secure, and easier to audit. Communication protocols detail the actual mechanics of interaction, ensuring consistent, secure, and efficient communication.

- **p. 6** — MCP is a general-purpose context-oriented protocol developed to facilitate secure and structured interactions between LLM agents and external resources such as tools, data, and services. MCP utilizes a JSON-RPC client-server architecture, enabling agents (hosts) to request and receive context from external resources through intermediate components—clients and servers. In this architecture, the host initiates context requests based on user queries, and the client manages connections to both the host and server, providing resource descriptions and

### 3.2 Communication Goal

- **p. 6** — executing context requests. The server directly interacts with resources to execute client requests and relay context, while resources include data, tools, or services. This layered approach reduces fragmentation across various agents and tool providers, significantly improving interoperability and scalability. Additionally, MCP enhances data security by decoupling sensitive tool invocations from LLM-generated responses, thus minimizing the risks of data exposure.

- **p. 6** — A2A supports inter-agent communication, emphasizing secure and structured peer-to-peer interactions among LLM agents. A2A employs capability-based ”Agent Cards” distributed via HTTP and Server- Sent Events, facilitating efficient task outsourcing and collaboration within enterprise-scale deployments. Agents advertise their capabilities through Agent Cards, enabling dynamic task delegation based on real-time capability awareness. Communication occurs directly between peers without centralized intermediaries, significantly reducing latency and improving responsiveness. Additionally, asynchronous messaging via server-sent events enhances scalability and robustness. A2A’s structured, capability-driven interactions improve task efficiency and collaboration fidelity, particularly suited for complex enterprise environments.

### 3.3 Communication Protocol

- **p. 6** — ANP facilitates decentralized agent communication and discovery over open networks. Built upon decentralized identifiers (DIDs) and JSON- LD graphs, ANP promotes secure, interoperable interactions among heterogeneous agents. Agents dynamically discover and verify peers using DIDs, ensuring secure identification across network boundaries. Communication is structured via JSON-LD graphs, enabling semantic clarity and context-aware interactions. ANP also incorporates encryption and secure channels, safeguarding data integrity and confidentiality. Its decentralized infrastructure supports robust, crossorganizational collaboration, fostering scalable and secure multi-agent ecosystems on a global scale. Table 2 adapts the comparative framework proposed by Abul et

- **p. 7** — al. [92], complements it and extends it with additional dimensions such as security and use cases to better contextualise LLM-MAS. MCP, A2A, and ANP represent significant advancements in standardizing and enhancing communication within LLM-based multi-agent systems. Additionally, other emerging protocols such as Agent Communication Protocol (ACP) [93], Agent Interaction and Task Protocol (AITP) [94], and Agent Content Protocol (AConP) [95] are also gaining attention, highlighting the dynamic and evolving landscape of communication protocols. Collectively, these protocols address interoperability, security, scalability, and context management, paving the way toward more integrated and intelligent multi-agent deployments. Table 2 Comparison of Three Emerging Agent Protocols

### 5.5 Communication Security

- **p. 12** — 5.3 Unified Communication Protocol The rapid emergence and deployment of multiple new communication protocols such as MCP, A2A, ANP, ACP, AITP, and AConP in LLM- MAS underscore the field’s dynamism and growth. However, this proliferation also brings critical challenges. One significant issue is functional redundancy, as different protocols often overlap in terms of capabilities such as secure communication, context management, and agent discovery. This redundancy can lead to unnecessary complexity, resource wastage, and increased difficulty in protocol management. Moreover, the lack of interoperability among existing protocols poses substantial barriers. Different agent groups employing distinct protocols cannot seamlessly communicate or collaborate, significantly hindering the scalability and integration of multi-agent systems. This situation mirrors early-stage internet communication challenges, which were eventually resolved through standardized protocols like HTTPS.
