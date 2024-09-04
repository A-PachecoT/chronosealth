def check_llm_consistency():
    # Implementa aquí las 3 métricas de consistencia en LLM
    # Por ejemplo:
    metrics = {
        "coherencia": check_coherence(),
        "diversidad": check_diversity(),
        "relevancia": check_relevance(),
    }

    print(f"Métricas de consistencia LLM: {metrics}")
    return metrics


def check_coherence():
    # Implementa la lógica para verificar la coherencia
    return 0.85


def check_diversity():
    # Implementa la lógica para verificar la diversidad
    return 0.75


def check_relevance():
    # Implementa la lógica para verificar la relevancia
    return 0.90
