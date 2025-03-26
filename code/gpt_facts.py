import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_fact():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Tell me one cool owl fact."}],
            max_tokens=60
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.RateLimitError:
        return "🧠 GPT is too tired right now (quota exceeded). Try again later."
    except Exception as e:
        print("GPT error:", e)
        return "GPT is currently unavailable."
