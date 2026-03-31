# Yellow Highlights — A survey of the model context protocol (mcp)- Standardizing context to enhance large language models (llms)

**Reference:** Not peer-reviewed version

## Abstract

The Model Context Protocol (MCP), recently introduced by Anthropic, proposes a stan- dardized framework for integrating large language models (LLMs) with dynamic external systems.

---

## Highlights by Section

### Abstract

- **p. 2** — foundational architecture of MCP, including its client-server model, standardized messaging protocols, dynamic tool discovery, and security mechanisms, against the backdrop of current, fragmented API solutions. Although the protocol promises enhanced interoperability and scalability for Agentic AI systems, data supporting its long-term performance remains limited. MCP’s design is critically evaluated, potential applications in domains such as finance, healthcare, and customer service are discussed, and the key challenges are outlined. This work aims to inform researchers and practitioners of MCP’s potential benefits and its present limitations in the evolving AI integration landscape.

- **p. 2** — Keywords:

- **p. 2** — Model Context Protocol (MCP);

- **p. 2** — Large Language Models (LLMs);

- **p. 2** — agentic AI,

- **p. 2** — contextual integration;

- **p. 2** — dynamic tool discovery;

- **p. 2** — workflow orchestration;

### 1. Introduction

- **p. 2** — The emergence of Large Language Models (LLMs) [1] has fundamentally reshaped artificial intelligence, demonstrating extraordinary capabilities in natural language understanding and generation. Despite these successes, LLMs remain inherently constrained by their reliance on static, pre-existing training datasets, which limits their applicability to dynamic, real-world scenarios. Consequently, research has increasingly focused on integrating LLMs with external data sources and practical tools to enhance their responsiveness, relevance, and operational effectiveness. Current integration approaches predominantly rely on fragmented, custom-built Application Programming Interfaces (APIs) [2], each tailored to individual tools or datasets. This lack of standardization introduces substantial challenges, including increased integration complexity, difficulties in scaling across multiple sources, interoperability issues, and inconsistent security practices. Such hurdles significantly impede the development and deployment of scalable and adaptive Agentic AI systems (i.e., systems that operate autonomously and adapt dynamically without continuous human intervention). To address these limitations, Anthropic introduced the Model Context Protocol (MCP) [3], described metaphorically as a USB-C port for AI [4]. MCP is an open protocol that standardizes how applications provide context to LLMs, much like USB-C standardizes device connectivity.

### 2 of 16

- **p. 3** — MCP offers a unified approach to connect AI models to diverse external resources, replacing the fragmented, custom-built API integrations that currently hinder scalability and interoperability.

- **p. 3** — MCP facilitates the development of complex, agent-based workflows. It provides a growing ecosystem of pre-built integrations, the flexibility to switch between LLM providers, and adherence to best practices for securing data within infrastructure.

- **p. 3** — By defining structured communication methods, dynamic tool discovery mechanisms, secure data handling processes, and flexible context management, MCP significantly enhances LLMs’ capabilities to autonomously execute complex tasks and adapt to evolving data contexts.

- **p. 3** — architectural components and core concepts of MCP.

- **p. 3** — Critically assess how MCP compares with conventional API integrations,

- **p. 3** — Identify challenges and propose directions for future work, acknowledging that empirical validation is still emerging.

### 2. Background

- **p. 3** — LLMs have exhibited substantial progress over recent years, demonstrating exceptional proficiency in a variety of complex tasks such as natural language generation, machine translation, question answering, and code [1]. However, despite their remarkable capabilities [5], these models encounter fundamental limitations, primarily due to their reliance on static, pre-collected training datasets. This reliance results in significant operational constraints, particularly in dynamic and real-world application scenarios, manifesting as: Knowledge Staleness: LLMs frequently lack up-to-date information, causing inaccuracies or • irrelevant outputs when responding to queries related to recent developments. • Contextual Limitations: Static models are often unable to adapt dynamically to changing contexts or effectively integrate external real-time information, limiting their contextual responsiveness. Addressing these limitations necessitates seamless integration between LLMs and external resources such as real-time data sources, databases, and specialized tools. Traditionally, this integration has been accomplished via Application Programming Interfaces (APIs), each customized for specific use-cases and requiring substantial configuration effort. The prevalent usage of such individualized integration solutions presents multiple significant challenges: • Integration Complexity: Building diverse API integrations requires repeated effort, extending development cycles. • Scalability Issues: Adding new data sources or tools is cumbersome, limiting scalability and adaptability [6]. • Interoperability Barriers: The absence of standardized protocols hinders reuse across AI models, leading to redundancy.

### 3 of 16

- **p. 4** — Security Risks: Custom API integrations often lack consistent security measures, increasing the risk of data breaches [7].

- **p. 4** — In response to these challenges [8], MCP has emerged as a standardized open protocol specifically designed to facilitate the seamless integration of AI applications with external systems. Drawing inspiration from established standardization successes such as web APIs and the Language Server Protocol (LSP) [9], MCP establishes a unified framework that significantly simplifies interactions between AI applications and external resources.

- **p. 4** — APIs historically standardized interactions between web applications and backend services like servers, databases, and software services. Similarly, LSP standardized interactions between Integrated Development Environments (IDEs) and programming languagespecific tools, thereby improving code navigation, analysis, and intelligence. MCP extends this lineage of standardization explicitly into the AI domain, focusing on three core interfaces: • Prompts: [10] Standardizing the provision and formatting of input context to AI models. • Tools: Establishing consistent methodologies for dynamic tool [11] discovery, integration, and usage by AI agents. • Resources: Defining standardized access to and utilization of external data and auxiliary resources for contextual enrichment. The central idea behind MCP is the acknowledgement that a model’s quality depends entirely upon the context it is provided. Historically, context management relied heavily on manual or fragmented solutions such as copying and pasting context data into AI interfaces. MCP eliminates these inefficient methods by enabling automated, structured, and secure integration of context, significantly enhancing AI responsiveness, personalization, and effectiveness.

- **p. 4** — MCP not only addresses the practical limitations faced by current LLM applications but also provides a robust foundation for the development of advanced Agentic AI systems capable of autonomous perception, reasoning, decision-making, and real-world interaction. Its adoption promotes scalability, interoperability, and security, positioning MCP as a critical component in the future development trajectory of intelligent AI systems.

### 3.1. Client-Server Architecture

- **p. 7** — 3.1. Client-Server Architecture MCP is designed around a structured client-server [12] model that facilitates efficient interaction between LLMs, external tools, and supporting resources,

- **p. 7** — Hosts refer to LLM applications, such as IDEs or platforms like Claude Desktop, that initiate communication. • Clients establish dedicated one-to-one connections with servers within these host applications. • Servers provide essential contextual data, tools, and prompts to enhance the client’s functionality.

- **p. 7** — This design promotes modularity, scalability, and seamless interoperability, ensuring AI systems can efficiently integrate and utilize external resources while maintaining security and efficiency. 3.2. Protocol Layer The protocol layer [12] governs structured communication by managing message framing, requestresponse handling, and notifications. MCP enforces a standardized message format, ensuring consistency across diverse implementations. It supports asynchronous communication, enabling nonblocking operations for efficient data exchange. The protocol also incorporates error handling mechanisms, ensuring robustness by validating responses and managing failures gracefully. This approach enhances interoperability, simplifies integration, and reduces overall system complexity. 3.3. Transport Layer The transport layer [12] underpins message delivery between MCP components. Currently, MCP supports: • Standard Input/Output (Stdio): Ideal for local and command-line based interactions, efficient in same-machine scenarios. • HTTP with Server-Sent Events (SSE): Suitable for remote interactions and streaming scenarios, leveraging widely-adopted web standards. Selection of appropriate transport mechanisms depends on application requirements such as locality, scalability, security constraints, and network configurations.

### 4.1. Resources

- **p. 8** — Text Resources:

- **p. 8** — Binary Resources:

### 3.4. Message Types

- **p. 8** — 3.4. Message Types MCP employs four primary message types: • Requests: Initiated by a client expecting a response. • Results: Successful responses to requests. • Errors: Responses signaling failures in request processing. • Notifications: One-way informational messages that do not require responses. 4. Fundamental MCP Concepts MCP introduces several fundamental concepts designed to facilitate structured interactions between LLMs and external resources or tools. These concepts include resources, prompts, tools, sampling, and roots. Understanding these components is essential for effectively utilizing MCP in diverse application scenarios. 4.1. Resources Resources [13] in MCP refer to structured data or content that servers expose to clients, which can then be utilized by LLMs to gain contextual insights during interactions. Resources can include a variety of data types such as textual documents, database entries, file contents, images, system logs, and real-time data streams. Each resource is uniquely identifiable using Uniform Resource Identifiers (URIs), conforming to a standardized schema to ensure consistency and ease of discovery. MCP resources are categorized broadly into two types:

### 4.1. Resources

- **p. 8** — Resources are discoverable via two primary mechanisms: 1. Direct Resource Listing: Servers explicitly list available resources through the resources/list endpoint, providing metadata including the resource URI, descriptive name, optional detailed description, and MIME type. 2. Resource Templates: Servers can define dynamic resources via URI templates following RFC 6570 standards. Templates enable clients to construct specific resource URIs dynamically based on contextual requirements or parameters.

### 4.2. Prompts

- **p. 8** — 4.2. Prompts Prompts [14] within MCP are structured templates provided by servers to standardize and streamline interactions between users, clients, and LLMs.These templates enable consistent, reusable workflows and interactions, enhancing both user productivity and model efficiency by clearly defining how interactions should be presented and processed.

### 8 of 16

- **p. 9** — MCP prompts serve several important functions: • Standardization of Interactions:

- **p. 9** — • Dynamic Context Integration:

- **p. 9** — • Workflow Automation and Composability:

- **p. 9** — • Name and Description:

- **p. 9** — • Arguments:

### 4.3. Tools

- **p. 9** — 4.3. Tools Tools [15] in MCP represent executable capabilities exposed by servers, empowering LLMs to perform actions, interact with external systems, and execute dynamic operations. Distinct from passive resources or static prompts, tools are designed for active invocation by models typically with human approval thereby significantly expanding the Agentic functionalities of LLM-driven systems.

### 9 of 16

- **p. 10** — Tools Tools: Enable LLMs to execute actions, interact with external systems, and perform dynamic operations beyond static prompts. Dynamic Invocation: Models trigger computations, system commands, and API interactions without manual preconfiguration. Structured Definition: JSON schemas define each tool’s inputs, ensuring validation, security, and precise execution. Discoverability & Integration: Tools are listed via tools/list and invoked through tools/call for controlled execution and output handling. Schema Components: Includes name, description, input schema, and structured results with error reporting, enabling model-driven corrective actions. Use Cases & Best Practices: Tools support computations, system management, and API interactions, emphasizing security, validation, access control, logging, and auditing.

- **p. 10** — Common use cases for tools range from simple local computations and file manipulations to sophisticated operations such as system management, database queries, and API interactions.

### 4.4. Sampling

- **p. 10** — 4.4. Sampling Sampling [16] within MCP enables servers to initiate inference requests directly to LLMs through clients, allowing dynamic retrieval of model-generated completions. This capability is crucial for developing sophisticated, interactive, and context-aware Agentic workflows that integrate human oversight and adaptive model interactions.

### 10 of 16

- **p. 11** — Sampling Server Request: Servers request LLM completions via sampling/createMessage, defining context, preferences, and parameters. User Oversight: Ensures human review and approval before invoking the LLM, maintaining security and transparency. Controlled Execution: Generates LLM responses with temperature, token limits, and stop sequences, ensuring adaptive behavior. Structured Response: Returns model details, termination reason, and output to the server for further processing. Advanced Agentic AI: Supports autonomous workflows, enabling dynamic decision-making and intelligent execution. Security & Validation: Implements role-based context, model preferences, and controlled execution policies for privacy, accuracy, and oversight.

- **p. 11** — Sampling requests use clearly defined JSON-based structures to ensure interoperability and transparency, specifying: • Contextual Messages: Input messages structured with roles (e.g., user or assistant) and content type (text or images), guiding model responses clearly and effectively. • Model Preferences: Providing hints or priorities for cost-efficiency, response speed, and model intelligence, assisting clients in optimal model selection and use. • Context Inclusion Policies: Defining the scope of additional context to be included in the sampling request, such as data from the current or connected servers, enhancing the relevance and accuracy of model completions. This mechanism enables adaptive interactions while ensuring security through human approval, input validation, and controlled execution. 4.5. Roots Roots [17] define logical boundaries indicating the scope or context within which servers are expected to operate.They serve as structured guides provided by clients to inform servers about relevant resources or operational contexts, thus streamlining interactions and clarifying operational scope

### 11 of 16

- **p. 12** — Roots Roots: Define logical boundaries to guide servers on scope, context, and resource access. URI-Based Targeting: Uses Uniform Resource Identifiers (URIs) for precise resource access. Operational Role: * Contextualization – Keeps operations within defined resource boundaries. Prioritization – Allocates resources efficiently based on root definitions. Multi-Context Management – Supports simultaneous environments. Adaptive

- **p. 12** — L Multi-Context Management – Supports simultaneous environments. Adaptive Updates: Clients can dynamically modify roots, requiring servers to adjust in real time.

- **p. 12** — When establishing connections, clients specify supported roots, allowing servers to: 1. Contextualize Operations: Focus their data retrieval or tool invocation strictly within relevant resource boundaries. 2. Prioritize Activities: Allocate resources and execution priority based on the specified roots, improving operational efficiency. 3. Manage Multi-Context Environments: Seamlessly support scenarios involving multiple simultaneous operational contexts, such as multiple project directories or diverse remote services.

### 5. Building Effective Agents with MCP

- **p. 12** — 5. Building Effective Agents with MCP MCP offers powerful features to develop sophisticated Agentic AI systems, primarily through its capabilities of Sampling and Composability. 5.1. Sampling: Federated Intelligence Requests Sampling within MCP enables servers to request completions directly from the MCP client. This shifts control over LLM interactions entirely to the client side, enhancing security, privacy, and cost-efficiency. 5.2. Composability: Logical Separation and Agent Chaining Composability in MCP refers to each node’s ability to function as both client and server

### 5.2. Composability: Logical Separation and Agent Chaining

- **p. 12** — This facilitates chaining, enabling complex, hierarchical, and specialized agent-based architectures.

### 12 of 16

- **p. 13** — Composability Dual Role of Components: Function as both clients and servers to build layered workflows. Data Flow: Fetch, process, and aggregate data to return refined results. Privacy Protection: Routes requests through the client to protect privacy. Composability: Enables modular systems with specialized agents. Human Oversight: Integrates human supervision when needed. Workflow Management: Supports chaining and hierarchical workflows. Figure 7. Overview of Composability.

- **p. 13** — MCP Composability illustrating logical separation, allowing MCP client to simultaneously act as clients and servers. Significant advantages: • Modular design of complex agent systems • Clear task specialization among agents • Scalability in multi-agent systems 5.3. Combined Sampling and Composability Integration of sampling and composability provides a robust foundation for federated, hierarchical agent networks.

### 5.3. Combined Sampling and Composability

- **p. 13** — Combined MCP Features: A central orchestrator manages multiple specialized agents using sampling and composability. The combined approach allows: • Centralized control and orchestration • Secure and flexible agent interactions • Enhanced capabilities for complex task management

### 6. Applications and Impact

- **p. 14** — 6. Applications and Impact MCP revolutionizes LLM interactions by standardizing integration, enabling robust, agentic AI systems to perform complex tasks and access real-time information.

### 15 of 16

- **p. 16** — MCP Impact on Agentic AI Development.

### 7. Challenges

- **p. 16** — challenges remain in adoption, standardization, security, scalability, and ecosystem development. • Adoption and Standardization: Establishing MCP as the industry standard requires active community involvement. • Security and Privacy: Implementing comprehensive security mechanisms is crucial. • Scalability and Performance: Ensuring low-latency communication as the system scales is essential. • Ecosystem Development: Building a robust ecosystem of compatible tools and services is necessary.
