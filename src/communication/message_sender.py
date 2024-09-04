import requests


def send_message():
    # Aquí deberías implementar la lógica para enviar el mensaje
    # a través del receptor. Por ejemplo, usando una API REST:
    url = "https://api.receptor.com/send"
    payload = {"message": "Mensaje de prueba"}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Mensaje enviado con éxito")
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar el mensaje: {e}")
