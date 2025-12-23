from app.agents.base import BaseAgent
from app.agents.result import AgentResult
from app.services.llm import generate_text 

class SynthesisAgent(BaseAgent):
    name = "synthesis_agent"

    async def run(self, query: str, docs: list) -> AgentResult:
        if not docs:
            print("⚠️ No sources found. Falling back to LLM knowledge.")
        
            fallback_prompt = f"""
            Answer the following question using your general knowledge.
            Be clear, concise, and educational.
        
            QUESTION:
            {query}
            """
        
            answer = generate_text(fallback_prompt)
        
            return AgentResult(
                output=answer,
                confidence=0.6,
                should_continue=False,
                notes="Answered using LLM fallback (no retrieval)"
            )

        print("🤖 Synthesizing answer with Groq...")

        # Prepare Data
        context_text = ""
        for d in docs:
            context_text += f"\n--- SOURCE: {d['source']} ---\n{d['content']}\n"
        
        # Limit context to avoid errors
        context_text = context_text[:8000] 

        prompt = f"""
        You are an expert researcher. Answer the user's question based ONLY on the provided sources.
        
        USER QUESTION: {query}
        
        SOURCES:
        {context_text}
        
        INSTRUCTIONS:
        - Write a clear, well-structured report.
        - Use headers (##) and bullet points.
        - If the sources don't contain the answer, say "I couldn't find that info."
        """

        final_answer = generate_text(prompt)

        if "Error" in final_answer:
             return AgentResult(output=final_answer, confidence=0.0, should_continue=False)

        return AgentResult(
            output=final_answer,
            confidence=1.0,
            should_continue=False,
            notes="Synthesis complete"
        )