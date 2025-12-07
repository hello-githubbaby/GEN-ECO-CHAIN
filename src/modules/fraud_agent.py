from src.agents.llm_client import call_llm
import json

def detect_fraud(order: dict):
    """
    Fraudulent return pattern detector.
    """

    prompt = f"""
    You are an AI that detects potentially fraudulent return behavior.
    Check for:
    - repeated expensive returns
    - mismatched claims
    - promo abuse
    - mismatched addresses
    - unusual timing patterns

    Respond as:
    {{
        "fraud_score": float,
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
