import pandas as pd
import numpy as np
import os

ruta = r'C:\Users\Usuario\Downloads'

archivos = os.listdir(ruta)
archivos_xlsx = [archivo for archivo in archivos if archivo.endswith('.xlsx') and 'DATASET_ALUMNOS_FISI PRE_POS' in archivo]

df_ = pd.read_excel(os.path.join(ruta, archivos_xlsx[0]), sheet_name='Hoja 1', engine='openpyxl')

print(df_)