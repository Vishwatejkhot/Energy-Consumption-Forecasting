from langchain_core.prompts import ChatPromptTemplate

PROMPT_VERSION = "v1"

def get_energy_prompt(version="v1"):

    if version == "v1":
        system = """
You are an expert energy efficiency consultant.
Provide clear, structured, actionable advice.
Be concise and practical.
"""

        human = """
Predicted next-hour energy consumption: {prediction} kW

Provide:
1. Usage classification (Low / Moderate / High)
2. Key reasons
3. 3 energy-saving actions
4. 1 long-term efficiency improvement
"""

    elif version == "v2":
        system = """
You are a senior energy analyst.
Give analytical, data-driven explanations.
Use structured formatting.
"""

        human = """
Forecasted consumption: {prediction} kW.

Provide:
- Usage severity level
- Behavioral or appliance causes
- Cost implication insight
- Optimization strategy
"""

    return ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", human)
    ])