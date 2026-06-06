# data-insight-generator-genai


An AI-powered data analysis tool that uses **CrewAI multi-agent framework** 
and a **local LLM (Ollama/LLaMA 3.2)** to automatically generate human-readable 
insights from any CSV dataset.

## 🔍 About the Project
Three specialized AI agents collaborate to analyze your data:
- **Data Loader Agent** — loads the CSV and summarizes structure
- **Data Analyzer Agent** — detects missing values and statistics
- **Insight Generator Agent** — writes plain-English insights from the analysis

## 🛠️ Tech Stack
- **Python**
- **CrewAI** — multi-agent orchestration
- **Ollama (LLaMA 3.2)** — local LLM (no OpenAI API needed)
- **Pandas** — data processing
- **LangChain** — LLM tooling

## 🚀 How to Run
1. Clone the repo
2. Install Ollama and pull the model:
   ollama pull llama3.2
3. Install dependencies:
   pip install -r requirements.txt
4. Run the script:
   python genai_data_insight_agents.py
5. Enter the path to your CSV file when prompted

## 📁 Sample Dataset
`sales1.csv` is included as a sample dataset to test the agents.

## 📌 Note
Create a `.env` file with your API keys if needed. Never commit it to GitHub.
