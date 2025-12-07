from src.agents.llm_client import call_llm
import json

def detect_anomaly(order: dict):
    """
    Detect abnormal return activity patterns.
    """

    prompt = f"""
    Identify anomalies in the return request.

    Types:
    - Unusual repeat patterns
    - Product-switch returns
    - Location irregularities
    - Time-of-day spikes
    - Rare category returns

    Respond as:
    {{
        "is_anomaly": bool,
        "reason": "text"
    }}

    ORDER:
    {order}
    """

    resp = call_llm(prompt)

    try:
        return json.loads(resp)
    except:
        return {"raw_output": resp}
