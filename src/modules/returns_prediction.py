from src.agents.llm_client import call_llm
import json

def predict_return_likelihood(order: dict):
    """
    LLM-based return likelihood predictor.
    """

    prompt = f"""
    You are an AI for reverse logistics. Analyze this order and
    estimate return likelihood from 0 to 1.

    Consider:
    - past return behavior
    - product category
    - sentiment signals
    - price range
    - delivery delays
    - customer profile

    Respond as:
    {{
        "likelihood": float,
        "explanation": "text"
    }}

    ORDER:
    {order}
    """

    resp = call_llm(prompt)

    try:
        return json.loads(resp)
    except:
        return {"raw_output": resp}
