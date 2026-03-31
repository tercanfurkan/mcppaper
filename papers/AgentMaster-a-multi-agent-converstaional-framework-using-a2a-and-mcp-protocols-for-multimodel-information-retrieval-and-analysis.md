**AgentMaster** is a modular, large language model (LLM)-based Multi-Agent System (MAS) framework designed to handle complex, multimodal information retrieval and analysis. It specifically addresses common bottlenecks in multi-agent systems—such as inter-agent communication, tool integration, and domain-specific reasoning—by being one of the first frameworks to jointly employ two newly developed open standards: **Google’s Agent-to-Agent (A2A) protocol** and **Anthropic’s Model Context Protocol (MCP)**.

Here is a full breakdown of the system's architecture, workflow, and performance based on the pilot study:

### 1. Core Architecture

The AgentMaster framework is composed of four main architectural pillars:

- **Unified Conversational Interface:** Users interact with the system via a chatbot frontend that requires no prior technical expertise. It can process multimodal inputs (text, images, audio, charts) and return multimodal outputs (text, images, structured data tables).
- **Multi-Agent Center (Three-Tier Hierarchy):**
  - **Orchestrator Agent (Coordinator):** The central hub of the system. It analyzes user queries, decomposes complex tasks into smaller sub-tasks, routes them to the correct agents, manages errors, and synthesizes the partial outputs into one cohesive final response.
  - **Domain Agents:** Specialized agents designed to interface with specific tools and datasets. In the paper's case study, these include a **SQL Agent** for relational databases, an **IR Agent** for unstructured knowledge bases, and an **Image Agent** for processing visual data via vision APIs.
  - **General Agents:** Independent LLM-powered agents that handle broad, open-domain questions or fallback cases that do not require domain-specific datasets.
- **Dual-Protocol Communication (A2A & MCP):**
  - The **A2A protocol** manages structured, JSON-based message exchange between the agents, allowing them to collaboratively delegate and orchestrate tasks.
  - The **MCP protocol** acts as the backend bridge, providing a standardized interface for agents to seamlessly access external tools, APIs, and contextual resources.
- **State Management Layer:** To keep the agents context-aware, this layer uses a vector database for persistent long-term semantic memory (recalling past interactions and documents) and a context cache for fast, temporary storage of active session data.

### 2. The System Workflow

When a user submits a query, it is received by a Flask server and forwarded to the Coordinator Agent. The Coordinator performs a **complexity assessment**.

- If the query is simple, it is dispatched directly to a single retrieval agent.
- If the query is complex (e.g., "List the three oldest bridges in Virginia and explain why their maintenance costs are higher"), the Coordinator uses A2A to decompose the prompt into sub-questions and assigns them to multiple agents (e.g., the SQL Agent finds the dates, the IR Agent finds the maintenance guidelines).

The agents execute their retrieval tasks via MCP servers and return the raw data. Finally, an integrated LLM module aggregates these partial outputs to formulate the final, natural-language response delivered to the user.

### 3. Experimental Case Study and Results

The researchers deployed a functional prototype of AgentMaster locally and on AWS, utilizing OpenAI's GPT-4o mini model. To test its domain-specific capabilities, they connected the agents to public datasets from the Federal Highway Administration, focusing on bridge infrastructure data.

The framework successfully handled diverse tasks, such as generating complex SQL database counts, defining engineering concepts, and analyzing non-destructive evaluation contour map images to identify structural bridge damage.

- **Performance Metrics:** Evaluated against several metrics, the framework demonstrated high reliability. It achieved an average **BERTScore F1 of 96.3%** (showing high semantic fidelity) and an average **G-Eval (LLM-as-a-Judge) score of 87.1%**.
- Human evaluation confirmed that the Coordinator Agent accurately decomposed complex queries and assigned task paths correctly.

### 4. System Limitations

Despite strong performance, the paper notes several limitations. The system's accuracy is heavily constrained by the capabilities of the underlying LLM and the completeness of the retrieval corpus. The researchers also observed occasional misclassification during the complexity assessment, where simple queries were unnecessarily decomposed into complex multi-agent workflows. Furthermore, the current iteration lacks established security safeguards for information storage, and the small database size sometimes resulted in answers lacking informational depth.
