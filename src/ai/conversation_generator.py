import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "tu_clave_api_de_openai")


def generate_conversation():
    # Utiliza OpenAI para generar una conversación casual
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Genera una conversación casual entre dos personas.",
                },
                {"role": "user", "content": "Inicia una conversación casual."},
            ],
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Error al generar la conversación: {e}")
        return None
