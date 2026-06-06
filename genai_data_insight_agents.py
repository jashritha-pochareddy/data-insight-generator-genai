# =============================================================
# 📊 GenAI Data Insight Generator using CrewAI Agents + Ollama
# =============================================================

import pandas as pd
from crewai import Agent, Task, Crew, LLM
import warnings
warnings.filterwarnings("ignore")

print("Topic: GenAI Data Insight Generator using CrewAI Agents\n")

# -------------------------------------------------------------
# 🔹 Step 1: Configure Local LLM (Ollama)
# -------------------------------------------------------------
llm = LLM(
    model="ollama/llama3.2",     # Use your local Ollama model
    base_url="http://localhost:11434",
    api_key="ollama"             # Dummy key to avoid OpenAI fallback
)

# -------------------------------------------------------------
# 🔹 Step 2: Define Agent Roles
# -------------------------------------------------------------
data_loader_agent = Agent(
    role="Data Loader",
    goal="Load CSV data and provide its basic information like rows, columns, and column names.",
    backstory="An expert data analyst who quickly loads CSV files and summarizes structure.",
    verbose=True,
    llm=llm
)

data_analyzer_agent = Agent(
    role="Data Analyzer",
    goal="Analyze missing values and statistical summary of the dataset.",
    backstory="A skilled data scientist who identifies missing data and gives numeric summaries.",
    verbose=True,
    llm=llm
)

insight_generator_agent = Agent(
    role="Insight Generator",
    goal="Generate human-like insights from the analyzed data.",
    backstory="An AI writer that explains data findings in a simple, human-readable way.",
    verbose=True,
    llm=llm
)

# -------------------------------------------------------------
# 🔹 Step 3: Ask User for CSV File
# -------------------------------------------------------------
csv_path = input("Enter path to your CSV file: ").strip()
df = pd.read_csv(csv_path)
print("\n✅ CSV Loaded Successfully!\n")

# -------------------------------------------------------------
# 🔹 Step 4: Define Tasks for Agents
# -------------------------------------------------------------
task1 = Task(
    description="Load the dataset and describe number of rows, columns, and column names.",
    agent=data_loader_agent,
    expected_output=f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns. Columns: {list(df.columns)}."
)

missing = df.isnull().sum().to_dict()
task2 = Task(
    description="Analyze missing values and show basic statistics.",
    agent=data_analyzer_agent,
    expected_output=f"Missing values summary: {missing}. Numeric summary:\n{df.describe(include='all').to_string()}"
)

task3 = Task(
    description="Create an AI-generated summary of the dataset in natural language using previous outputs.",
    agent=insight_generator_agent,
    expected_output="A paragraph describing the dataset insights in plain English."
)

# -------------------------------------------------------------
# 🔹 Step 5: Create Crew and Execute
# -------------------------------------------------------------
crew = Crew(
    agents=[data_loader_agent, data_analyzer_agent, insight_generator_agent],
    tasks=[task1, task2, task3],
    verbose=True
)

print("🚀 Running the Crew...\n")
result = crew.kickoff()

# -------------------------------------------------------------
# 🔹 Step 6: Display the Final Result
# -------------------------------------------------------------
print("\n🤖 Final AI-Generated Insight:\n")
print(result)
