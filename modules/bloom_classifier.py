import ollama
import json

def classify_question(question, model="llama3.2:latest"):
    prompt = f"""
Classify the following question into one of Bloom's Taxonomy levels:
(Remember, Understand, Apply, Analyze, Evaluate, Create)

Question: "{question}"

Respond in JSON format:
{{
  "bloom_level": "...",
  "reason": "...",
  "suggestion": "..."
}}
"""
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    try:
        return json.loads(response['message']['content'])
    except:
        return {
            "bloom_level": "Unknown",
            "reason": "Parsing error",
            "suggestion": "Check formatting"
        }
