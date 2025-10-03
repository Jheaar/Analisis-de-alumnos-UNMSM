import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt

ruta = r'C:\Users\Usuario\Downloads'

archivos = os.listdir(ruta)
archivos_xlsx = [archivo for archivo in archivos if archivo.endswith('.xlsx') and 'DATASET_ALUMNOS_FISI PRE_POS' in archivo]

df_ = pd.read_excel(os.path.join(ruta, archivos_xlsx[0]), sheet_name='Hoja 1', engine='openpyxl')
df_ = df_[df_['ano_ingreso0'].isnull() == False]

# quiero ver ambos graficos en la misma figura
def limpieza(campana):
    if 'EGRESADO' in campana or len(campana) > 6:
        return campana[:6]
    else:
        return campana

df_['tiempo_key'] = df_['tiempo_key'].apply(limpieza)

plt.figure(figsize=(12, 6))
import seaborn as sns
plt.subplot(1, 2, 1)
sns.violinplot(x='ano_ingreso0', y='nota', data=df_)
plt.title('Distribución de Notas por Año de Ingreso')
plt.xlabel('Año de Ingreso')
plt.ylabel('Nota')


plt.subplot(1, 2, 2)
sns.countplot(x='tiempo_key', data=df_)
plt.title('Cantidad de Alumnos por Año de Ingreso')
plt.xlabel('Año de Ingreso')
plt.ylabel('Cantidad de Alumnos')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

print(df_.head())