import google.generativeai as genai

# ⚠️ Move this to environment variables before deployment
YOUR_API_KEY = ""

genai.configure(api_key=YOUR_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")


def summarize_and_rewrite(text: str) -> str:
    """
    Summarizes and rewrites text into a neutral, unbiased, fact-based report
    with a strictly structured format.
    """

    prompt = f"""
You are given informational text collected from multiple reliable sources.

OBJECTIVE:
Generate a neutral, unbiased, fact-based summary.

STRICT RULES:
- Do NOT add opinions, predictions, or interpretations
- Remove emotional or persuasive language
- Preserve only key facts and essential statistics

OUTPUT STRUCTURE (MANDATORY):

### Overview
- 1–2 bullet points summarizing the topic

### Key Facts
- 2–3 bullet points with the most important verified facts

### Positive Indicators
- 1–2 bullet points highlighting factual positives (if present)

### Challenges and Concerns
- 1–2 bullet points highlighting factual challenges (if present)

FORMAT RULES:
- Use ONLY the section headings shown above
- Bullet points only (no paragraphs)
- One sentence per bullet point
- Maximum total length: 220 words

TEXT:
{text}
"""

    response = model.generate_content(prompt)
    return response.text.strip()
