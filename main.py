import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt

ruta = r'C:\Users\Usuario\Downloads'

archivos = os.listdir(ruta)
archivos_xlsx = [archivo for archivo in archivos if archivo.endswith('.xlsx') and 'DATASET_ALUMNOS_FISI PRE_POS' in archivo]

df_ = pd.read_excel(os.path.join(ruta, archivos_xlsx[0]), sheet_name='Hoja 1', engine='openpyxl')
df_ = df_[df_['ano_ingreso0'].isnull() == False]

plt.figure(figsize=(10, 6))
import seaborn as sns
sns.violinplot(x='ano_ingreso0', y='nota', data=df_)
plt.title('Distribución de Notas por Año de Ingreso')
plt.xlabel('Año de Ingreso')
plt.ylabel('Nota')
plt.show()