from random import choice, randint
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY: str = os.getenv('API_KEY')

genai.configure(api_key=os.environ['API_KEY'])
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain"
}

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    else:
        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        )

        chat_session = model.start_chat(history=[
            
        ])

        response = chat_session.send_message(lowered)

        if response.text == '':
            return 'I have no idea what you are talking about'

        return response.text