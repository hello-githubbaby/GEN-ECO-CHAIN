from src.agents.llm_client import call_llm
import json

def personalize_customer(order: dict):
    """
    Customer behavior clustering / personalization.
    """

    prompt = f"""
    Analyze customer return behavior and produce a cluster label.

    Clusters:
    - Eco Saver
    - High Spender
    - Deal Hunter
    - Return Sensitive
    - Impulse Buyer
    - Loyal Customer

    Respond as:
    {{
        "cluster": "text",
        "recommendations": ["list of suggestions"]
    }}

    ORDER:
    {order}
    """

    resp = call_llm(prompt)

    try:
        return json.loads(resp)
    except:
        return {"raw_output": resp}
