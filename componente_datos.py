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
            self.datos = pd.read_csv(self.ruta_archivo)
            self.limpiar_datos()
            return self.datos
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            return None

    def limpiar_datos(self):
        """
            Realiza la limpieza de los datos, eliminando valores nulos y duplicados.
        """
        if self.datos is not None:
            self.datos.dropna(inplace=True)
            self.datos.drop_duplicates(inplace=True)