# Weather Agent
**AUTHOR . . . . . . .** Shahar Ankonina                                                                              
**DESCRIPTION. . .** LLM-powered agent for real-time weather retrieval and reasoning

---
## About
Weather Agent is an AI-powered assistant that retrieves real-time weather information for any location using Python, LangGraph, and Tavily. It leverages a language model to interpret user queries and dynamically calls web-based tools to fetch accurate data. This project demonstrates the ability to design modular AI workflows, orchestrate LLM reasoning, and integrate external APIs, showcasing skills in AI, Python programming, and system architecture.

---
## Features
- *LLM Reasoning:* Uses LangGraph to orchestrate reasoning and task execution.
- *Real-Time Data Retrieval:* Integrates Tavily web search to get up-to-date weather information.
- *Modular Architecture:* Easy to extend for additional tools or APIs.
- *Interactive Queries:* Users can ask for weather by location and date.
- *Testing & Validation:* Iterative testing ensures accurate query responses.

---
## Tech Stack
- *Programming Languages:* Python
- *Libraries & Frameworks:* LangGraph
- *Tools & Platforms:* Git/GitHub, VS Code

---
## Installation
Requires Python 3.8+ and dependencies in requirements.txt
Follow these steps to run the project locally:

```bash
# Clone the repo
git clone https://github.com/AnkoninaShahar/LangGraph-Weather-Agent.git

# Navigate into the directory
cd LangGraph-Weather-Agent

# Install dependencies (Python example)
pip install -r requirements.txt

# Run the project
python weather_agent.py

```

---
## Usage
*Requires Users to enter an OpenAI API key, a Langsmith API key, and a Tavily API key before using the agent*                                                            
Enter a query like:
"What is the weather today in New York?"
The agent retrieves and displays current or forecasted weather.
Extend the workflow by adding new tools or APIs for additional capabilities.
