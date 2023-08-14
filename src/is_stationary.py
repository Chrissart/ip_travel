import numpy as np


def is_stationary(transitions: dict) -> bool:
    # Convertir el diccionario de transiciones a una matriz numpy
    states = list(transitions.keys())
    matrix = []
    for state in states:
        row = [transitions[state].get(next_state, 0) for next_state in states]
        matrix.append(row)
    P = np.array(matrix)

    # Encontrar el eigenvector correspondiente al eigenvalor 1
    eigenvalues, eigenvectors = np.linalg.eig(P.T)
    stationary_vector = eigenvectors[:, np.isclose(eigenvalues, 1)]

    # Si no hay eigenvector para el eigenvalor 1, entonces no hay punto estacionario
    if stationary_vector.size == 0:
        return False

    stationary_vector = stationary_vector[:, 0]
    stationary_vector = stationary_vector / stationary_vector.sum()

    # Multiplicar el vector estacionario con la matriz y verificar si es igual al vector estacionario
    result_vector = np.dot(stationary_vector, P)

    return np.allclose(result_vector, stationary_vector)

