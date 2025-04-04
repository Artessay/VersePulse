# api_call_example.py
from openai import OpenAI
client = OpenAI(api_key="0",base_url="http://0.0.0.0:8000/v1")

messages = [{"role": "user", "content": "Who are you?"}]
for _ in range(50):
    result = client.chat.completions.create(messages=messages, model="Qwen/Qwen2.5-7B-Instruct")
print(result.choices[0].message)