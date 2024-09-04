import schedule
import time
from src.communication import send_message, notify_slack, notify_threshold_downgrade
from src.ai import generate_conversation, evaluate_conversation
from src.data import clear_history, save_status
from src.monitoring import (
    check_llm_consistency,
    check_health,
    start_health_check_server,
)


def job():
    # Enviar mensaje
    send_message()

    # Generar y evaluar conversación
    conversation = generate_conversation()
    evaluation = evaluate_conversation(conversation)

    # Limpiar historial y guardar estado
    clear_history()
    save_status(evaluation)

    # Verificar consistencia LLM
    metrics = check_llm_consistency()

    # Verificar salud del sistema
    system_health = check_health()

    # Notificar a Slack si es necesario
    if not system_health:
        notify_slack("¡Alerta! El sistema de salud ha fallado.")

    # Ejemplo de notificación de degradación de umbral
    if metrics["coherencia"] < 0.7:
        notify_threshold_downgrade("ClienteX", "Coherencia LLM")


# Iniciar el servidor de verificación de salud
start_health_check_server()

# Programar el trabajo para que se ejecute cada 2 minutos
schedule.every(2).minutes.do(job)

# Bucle principal
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
