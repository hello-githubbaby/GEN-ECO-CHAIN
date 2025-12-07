from src.agents.llm_client import call_llm
import json

def optimize_route(locations: list):
    """
    Optimize return pickup route for minimum cost and distance.
    """

    prompt = f"""
    Optimize this reverse logistics route.

    Objectives:
    - minimize distance
    - minimize fuel/time
    - consolidate pickups
    - reduce carbon emissions

    Respond as:
    {{
        "optimized_route": ["ordered list of locations"],
        "total_distance_km": float,
        "notes": "text"
    }}

    LOCATIONS:
    {locations}
    """

    resp = call_llm(prompt)

    try:
        return json.loads(resp)
    except:
        return {"raw_output": resp}
