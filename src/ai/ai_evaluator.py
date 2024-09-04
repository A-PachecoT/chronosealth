import openai


def evaluate_conversation(conversation):
    # Evalúa la conversación contra el prompt del cliente usando IA
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Evalúa si la siguiente conversación cumple con los criterios del cliente. Proporciona una puntuación de 0 a 100 y una breve explicación.",
                },
                {
                    "role": "user",
                    "content": f"Conversación: {conversation}\n\nEvalúa si esta conversación es apropiada y cumple con las expectativas del cliente.",
                },
            ],
        )
        evaluation = response.choices[0].message["content"]

        # Extraer puntuación y explicación
        score = int(evaluation.split()[0])
        explanation = " ".join(evaluation.split()[1:])

        return {"score": score, "explanation": explanation}
    except Exception as e:
        print(f"Error al evaluar la conversación: {e}")
        return None
