import time
import os
from groq import Groq

# --- CONFIGURATION ---
# PASTE YOUR GROQ KEY HERE (starts with gsk_...)
API_KEY = "APNA_API_KEY_YAHAN_DAALO"

client = None
try:
    if API_KEY and not API_KEY.startswith("PASTE"):
        client = Groq(api_key=API_KEY)
except Exception as e:
    print(f"⚠️ Groq Client Warning: {e}")

def generate_text(prompt: str, model: str = 'llama-3.3-70b-versatile') -> str:
    """
    Global LLM function using the NEW Groq model (Llama 3.3).
    """
    if not client:
        return "Error: Please paste your Groq API Key in app/services/llm.py"

    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=model,
                temperature=0.5,
            )
            return chat_completion.choices[0].message.content

        except Exception as e:
            error_msg = str(e)
            # Handle Rate Limits
            if "429" in error_msg:
                wait_time = 10 * (attempt + 1)
                print(f"⚠️ Groq Rate Limit. Waiting {wait_time}s...")
                time.sleep(wait_time)
            # Handle Retired Model Error (The 400 error you saw)
            elif "400" in error_msg:
                 return f"Error (400): Model name invalid. Check 'llm.py'. Full error: {e}"
            else:
                print(f"❌ Groq Error: {e}")
                return f"Error: {e}"

    return "Server is busy. Please try again later."