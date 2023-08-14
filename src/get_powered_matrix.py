import numpy as np
import pandas as pd


def get_powered_matrix(transitions: dict, n: int) -> pd.DataFrame:
    """
    Eleva la matriz de transición a la potencia n.
    Args:
    - transitions (dict): La matriz de transición en forma de diccionario.
    - n (int): La potencia a la que se desea elevar la matriz.

    Returns:
    - pd.DataFrame: Matriz de transición (en forma de DataFrame) elevada
        a la potencia n.
    """
    # Convertimos el diccionario a una matriz
    nodes = sorted(transitions.keys())
    matrix = np.array(
            [[transitions[i].get(j, 0) for j in nodes] for i in nodes]
        )

    # Elevamos la matriz a la potencia n
    powered_matrix = np.linalg.matrix_power(matrix, n)

    # Convertimos la matriz resultante en un DataFrame para
    # una representación más visual
    df_powered_matrix = pd.DataFrame(
            powered_matrix,
            index=nodes,
            columns=nodes
        )

    return df_powered_matrix
