#  FILE 4 — `src/agents/llm_client.py`
```python
import os

def call_llm(prompt: str, max_tokens=300):
    api_key = os.getenv("OPENAI_API_KEY")

    # Real mode if key present
    if api_key:
        try:
            import openai
            openai.api_key = api_key

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )

            return response["choices"][0]["message"]["content"]

        except Exception as e:
            return f"[LLM error: {e}]"

    # Offline fallback mode
    return f"[PLACEHOLDER RESPONSE]\nPrompt:\n{prompt[:1000]}"
