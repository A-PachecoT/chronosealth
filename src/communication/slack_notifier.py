import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.getenv("SLACK_TOKEN", "xoxb-tu-token-de-slack")
client = WebClient(token=slack_token)


def notify_slack(message, channel="#general"):
    try:
        response = client.chat_postMessage(channel=channel, text=message)
        print(f"Mensaje enviado a Slack: {message}")
    except SlackApiError as e:
        print(f"Error al enviar mensaje a Slack: {e}")


def notify_threshold_downgrade(client_name, threshold):
    message = f"¡Alerta! El cliente {client_name} ha degradado el umbral: {threshold}"
    notify_slack(message, channel="#alertas-clientes")
