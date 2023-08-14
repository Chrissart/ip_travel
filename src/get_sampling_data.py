from typing import List
import random
from datetime import datetime, timedelta
import pandas as pd


def get_sampling_data(
            number_of_rows: int,
            ip_address: str = None,
            ip_addresses: List[str] = ['192.168.1.1', '10.0.0.2', '172.16.0.1']
        ) -> pd.DataFrame:
    # Generar datos de muestra
    niveles = ['medium', 'high', 'critical']
    fechas_base = datetime(2023, 8, 1)  # Fecha base para generar registros
    data = []
    for _ in range(number_of_rows):
        ip = random.choice(ip_addresses)
        nivel = random.choice(niveles)
        fecha = fechas_base + timedelta(
                days=random.randint(0, 10),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59),
                seconds=random.randint(0, 59)
            )
        data.append([ip, nivel, fecha.strftime('%Y/%m/%d %H:%M:%S')])
    df = pd.DataFrame(data, columns=['ip', 'level', 'time'])

    df_ip1 = None
    if ip_address is not None:
        df_ip1 = df[df['ip'] == ip_address]
        df_ip1.sort_values(by='time', inplace=True)
        return df_ip1
    ip_counts = df.value_counts('ip').to_dict()
    most_appeared_ip = next(iter(ip_counts.items()))
    most_appeared_ip = most_appeared_ip[0]
    df_ip1 = df[df['ip'] == most_appeared_ip].copy()
    df_ip1.sort_values(by='time', inplace=True)
    return df_ip1
