from src.agents.llm_client import call_llm
import json

def sustainability_score(order: dict):
    """
    Carbon footprint and sustainability metrics agent.
    """

    prompt = f"""
    Estimate sustainability impact of this return.

    Consider:
    - distance travelled
    - transport mode
    - packaging waste
    - carbon footprint
    - repairability
    - resell probability

    Respond as:
    {{
        "carbon_score": float,
        "recyclability": "low | medium | high",
        "resell_likelihood": float,
        "summary": "text"
    }}

    ORDER:
    {order}
    """

    resp = call_llm(prompt)

    try:
        return json.loads(resp)
    except:
        return {"raw_output": resp}
