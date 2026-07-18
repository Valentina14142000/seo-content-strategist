# SEO Content Strategist Agent

An autonomous, multi-agent orchestrator built with **LangGraph** designed to scale SEO content strategy. This system automates the end-to-end pipeline from competitive market research to the generation of high-converting, structured content briefs.

##  Overview
By leveraging a **Supervisor-Worker agentic pattern**, this tool eliminates the manual heavy lifting of SEO research. It identifies content gaps, analyzes competitor hierarchies, and outputs ready-to-write briefs, allowing content teams to focus on quality rather than data collection.

##  Core Capabilities
* **Autonomous Intelligence:** Powered by Tavily for real-time web context, ensuring strategy is based on current SERP data.
* **Agentic Workflow:** Employs a robust Supervisor/Worker architecture, ensuring modularity, clear state management, and easier debugging of individual agent nodes.
* **Scalable Output:** Automatically structures complex SEO requirements into H1/H2 hierarchies, intent-based audience profiles, and semantic keyword clusters.
* **Extensible Framework:** Designed for rapid iteration—easily extend the workflow to include automated social media repurposing or direct CMS publishing.

##  Tech Stack
* **Orchestration:** [LangGraph](https://www.langchain.com/langgraph) (State management & workflow control)
* **Intelligence:** OpenAI GPT-4o / LangChain
* **Data Retrieval:** Tavily Search API
* **Language:** Python 3.13+

##  Quick Start
1. **Clone the repo**
2. **Install dependencies**
3. **Configure Environment**
4. **Run the workflow**

##  Roadmap
- [ ] **Multi-Persona Reviewer:** Implement a "Reviewer Node" that critiques briefs against E-E-A-T guidelines.
- [ ] **Internal Linking Engine:** Develop a subgraph to analyze internal site structure for optimized link placement.
- [ ] **Human-in-the-loop (HITL):** Integrate manual approval steps for content briefs via a simple UI.

---
*Built by Valentina Kiyungi*
