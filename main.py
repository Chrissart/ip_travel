import time
import pandas
from src.get_sampling_data import get_sampling_data
from src.get_transition_matrix import get_transition_matrix
from src.get_graph import get_graph
from src.update_transitions import update_transitions
from src.manage_dataframe_size import manage_dataframe_size
from src.get_certain_transitions import get_certain_transitions
from src.is_stationary import is_stationary
from src.estimate_time_to_stationary import estimate_time_to_stationary

if __name__ == '__main__':
    # Obtenemos data por primera vez
    data = get_sampling_data(
        number_of_rows=100000
    )
    # Obtenemos los valores de transición según la data obtenida
    transitions = get_transition_matrix(data)
    # Obtenemos la primer representación en grafo
    graph, fig, ax, pos = None, None, None, None  # Agregar 'pos' aquí

    # Obtenemos nueva data y alimentamos la cadena de Markov
    vueltas = 0
    while True:
        new_data = get_sampling_data(
            number_of_rows=1,
            ip_address=list(data['ip'].unique())[0]
        )
        data = pandas.concat([data, new_data], ignore_index=True)
        last_transition = tuple(data['level'].tail(2).tolist())
        transitions = update_transitions(transitions, *last_transition)
        graph, fig, ax, pos = get_graph(
                transitions,
                data['ip'].unique().tolist()[0],
                graph,
                fig,
                ax,
                pos
            )
        data = manage_dataframe_size(data, 100)
        certain_transitions = get_certain_transitions(transitions)
        if certain_transitions:
            print(
                'El proceso llegó a un punto '
                'cíclico en las siguientes transiciones:'
            )
            for transition in certain_transitions:
                print(transition)
            input()
            break
        vueltas += 1
        time.sleep(60)
    print(f'Número de iteraciones: {vueltas}')
    print(
        f'La matriz es estacionaria?: {is_stationary(transitions)} '
        f'en {estimate_time_to_stationary(pandas.DataFrame(transitions))}'
        ' tiempos'
    )
