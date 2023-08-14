import os
from datetime import datetime
import pandas as pd


def manage_dataframe_size(
            dataframe: pd.DataFrame,
            max_number: int = 2e6
        ) -> pd.DataFrame:

    # Si el dataframe es menor que max_number, simplemente regresarlo
    if len(dataframe) < max_number:
        return dataframe

    # Tomar todos los registros menos los últimos dos para guardar
    to_save = dataframe.head(len(dataframe) - 2)

    # Si no hay registros para guardar, regresa el dataframe original
    if len(to_save) == 0:
        return dataframe

    # Ruta del archivo parquet
    file_path = (
            './assets/data/saved_data'
            f'{datetime.now().strftime("_%Y-%m-%d_%H")}'
            '.parquet'
        )

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if not os.path.exists(file_path):
        to_save.to_csv(file_path)
    else:
        to_save.to_csv(
            file_path,
            index=False,
            mode='a'
        )

    # Eliminar los registros guardados del DataFrame en memoria
    dataframe.drop(to_save.index, inplace=True)

    return dataframe
