def get_certain_transitions(transitions: dict) -> list:
    certain_transitions = []
    for nivel, next_levels in transitions.items():
        # print(f'Nodo a evaluar: {nivel}')
        for next_nivel, prob in next_levels.items():
            # print(f'Ruta a evaluar: {nivel} -> {next_nivel}\nProbabilidad: {prob}')
            if prob >= 0.9:
                certain_transitions.append((nivel, next_nivel))
    return certain_transitions
