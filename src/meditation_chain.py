from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from .config import GEMINI_TEXT_MODEL, TARGET_MIN_WORDS, TARGET_MAX_WORDS

SYSTEM = """You are a meditation guide writing a personalized spoken-word meditation
for one specific person.

Use the Dream Life and Yearly Goals as emotional and thematic material. Never read
those documents aloud or mention the documents. Weave their themes naturally.

Structure:
- 60-90 seconds of breath and body settling.
- 7-8 minutes of visualization, imagining the person already living their desired life.
- Focus naturally on 1-2 current goals.
- About 60 seconds of grounding and a calm intention for the day.

Target 1200-1400 words.
Follow the supplied Voice & Tone.
Use second person and present tense unless the Voice & Tone says otherwise.
Use [pause] sparingly for natural pauses.
Avoid religious language unless explicitly requested.
Vary openings and phrasing.
Output only the meditation script. No title, headers, commentary, or explanation.
"""

def build_chain():
    llm = ChatGoogleGenerativeAI(
        model=GEMINI_TEXT_MODEL,
        temperature=0.8,
        max_output_tokens=2200,
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM),
        ("human", """Dream Life:
{dream_life}

Yearly Goals:
{yearly_goals}

Voice & Tone:
{voice_tone}

Write today's meditation now."""),
    ])
    return prompt | llm

def generate_script(context: dict[str, str]) -> str:
    result = build_chain().invoke(context)
    return result.content.strip()
