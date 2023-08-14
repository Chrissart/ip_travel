import pandas as pd


def get_transition_matrix(dataframe: pd.DataFrame) -> dict:
    # Estimar la matriz de transición
    transitions = {nivel: {} for nivel in dataframe['level'].unique()}

    for iterator in range(len(dataframe)-1):
        current_nivel = dataframe.iloc[iterator]['level']
        next_nivel = dataframe.iloc[iterator+1]['level']
        if next_nivel not in transitions[current_nivel]:
            transitions[current_nivel][next_nivel] = 0
        transitions[current_nivel][next_nivel] += 1

    # Convertir el conteo en probabilidad
    for nivel, next_levels in transitions.items():
        total = sum(next_levels.values())
        for next_nivel, count in next_levels.items():
            transitions[nivel][next_nivel] = count / total

    return transitions
