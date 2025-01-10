import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
data = pd.read_csv('meteo.csv')

plt.figure(figsize=(10, 6))
sns.histplot(data['y'], kde=True, bins=30, color='blue') 
plt.title('Distribución de la Temperatura')
plt.xlabel('Temperatura')
plt.ylabel('Frecuencia')
plt.grid()

# Guardar el gráfico como imagen
plt.savefig('distribucion_temperatura.png')  # Guardar el gráfico como un archivo PNG








print("Análisis completado.")

