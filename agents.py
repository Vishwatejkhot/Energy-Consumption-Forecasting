from prompts import get_energy_prompt

def energy_forecast_agent(llm, prediction, version="v1"):
    prompt = get_energy_prompt(version)
    chain = prompt | llm
    return chain.invoke({"prediction": f"{prediction:.4f}"}).content


def cost_agent(llm, prediction):
    prompt = """
You are an energy cost analyst.
If energy price is £0.30 per kWh,
estimate hourly cost and give saving advice.

Consumption: {prediction} kW
"""

    response = llm.invoke(prompt.format(prediction=prediction))
    return response.content


def anomaly_agent(llm, prediction, threshold=4.0):
    if prediction > threshold:
        prompt = f"""
Energy spike detected: {prediction} kW.
Explain possible anomaly reasons and mitigation.
"""
        return llm.invoke(prompt).content
    return "No anomaly detected." 