import numpy as np
import pandas as pd


def estimate_time_to_stationary(
            transition_matrix: pd.DataFrame,
            threshold=1e-6,
            max_iterations=int(1e6)
        ) -> int:
    """
    Estima el tiempo que tarda una cadena de Markov en volverse estacionaria.

    Args:
    - transition_matrix: Matriz de transición.
    - threshold: Umbral para considerar que la cadena es estacionaria.
    - max_iterations: Número máximo de potenciaciones antes de detenerse.

    Returns:
    - int:
        Número de iteraciones antes de que
        la cadena sea considerada estacionaria.
    """
    current_matrix = transition_matrix.values
    previous_matrix = np.zeros_like(current_matrix)
    for k in range(1, max_iterations + 1):
        current_matrix = np.dot(current_matrix, transition_matrix.values)
        if np.linalg.norm(current_matrix - previous_matrix, ord=1) < threshold:
            return k
        previous_matrix = current_matrix

    return -1
    # Retorna -1 si no se vuelve estacionaria después de max_iterations.
