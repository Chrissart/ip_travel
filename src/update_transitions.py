def update_transitions(transitions, current_nivel, next_nivel) -> dict:
    # Si el nivel actual no está en las transiciones, añadirlo
    if current_nivel not in transitions:
        transitions[current_nivel] = {}
    
    # Actualizar el conteo de transiciones del nivel actual al siguiente
    if next_nivel not in transitions[current_nivel]:
        transitions[current_nivel][next_nivel] = 0
    transitions[current_nivel][next_nivel] += 1

    # Convertir el conteo en probabilidad para el nivel actual
    total = sum(transitions[current_nivel].values())
    for next_level, count in transitions[current_nivel].items():
        transitions[current_nivel][next_level] = count / total

    return transitions