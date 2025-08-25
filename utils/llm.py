# utils/llm.py
import ollama

def run_local_model(prompt: str, model: str = "codellama:7b") -> str:
    resp = ollama.chat(
      model=model,
      messages=[{"role": "user", "content": prompt}],
      stream=False
    )
    return resp["message"]["content"]
