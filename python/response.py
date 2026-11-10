import os
from typing import Optional

from dotenv import load_dotenv
from google import genai

load_dotenv()

DEFAULT_MODEL = "gemini-3.8-flash"
SYSTEM_INSTRUCTION = (
    "You are a friendly, playful anime-themed Discord bot assistant. "
    "Keep responses concise and under 2000 characters when possible."
)

_client: Optional[genai.Client] = None


def _get_client() -> genai.Client:
    """Return a lazily initialized Gemini API client."""
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("API_KEY")
        if not api_key:
            raise ValueError(
                "Missing Gemini API key: set GEMINI_API_KEY or API_KEY in the environment."
            )
        _client = genai.Client(api_key=api_key)
    return _client


def get_response(
    user_input: str, previous_interaction_id: Optional[str] = None
) -> str:
    """Generate a reply for a user prompt via the Gemini Interactions API."""
    if not user_input or not user_input.strip():
        return "Well, you're awfully silent..."

    client = _get_client()
    params = {
        "model": DEFAULT_MODEL,
        "input": user_input,
        "system_instruction": SYSTEM_INSTRUCTION,
    }
    if previous_interaction_id:
        params["previous_interaction_id"] = previous_interaction_id

    interaction = client.interactions.create(**params)
    text = (interaction.output_text or "").strip()
    if not text:
        return "I have no idea what you are talking about"

    return text
