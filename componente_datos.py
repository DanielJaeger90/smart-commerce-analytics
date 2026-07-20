# Este componenete se encarga de la ingesta, limpieza y validación de los datos
# Es el motor de datos

import pandas as pd

class IngestorDatos:
    """Componente independiente para la ingesta y validación de datos comerciales"""
    def __init__(self):
        pass

    def cargar_datos(self, archivo) -> pd.DataFrame:
        """Carga los datos desde un archivo CSV y realiza la limpieza inicial."""
        try:
            df = pd.read_csv(archivo, sep=None, engine='python', encoding='utf-8-sig') # Detecta automáticamente el separador
            df = self.limpiar_datos(df)
            return df
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error