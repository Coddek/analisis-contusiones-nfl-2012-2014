import pandas as pd
import plotly.express as px
import warnings
import os

# Quitar límite para visualización de tablas
warnings.filterwarnings('ignore')
pd.set_option('display.max_rows', None)

# Crear carpeta para guardar visualizaciones
os.makedirs("visualizations", exist_ok=True)

# Cargar el dataset
dataset = pd.read_csv("data/Concussion Injuries 2012-2014.csv")

print(dataset.columns)
print("-----------------------------")
print(dataset.info())
print("-----------------------------")
print(dataset.nunique())
print("-----------------------------")

# Elegir variables para análisis
total_contusiones = dataset["Position"].value_counts().reset_index()
total_contusiones.columns = ["Position", "Count"]

resultados_partidos = dataset["Winning Team?"].value_counts().reset_index()
resultados_partidos.columns = ["Winning Team?", "Count"]

relacion = dataset.groupby(["Position", "Winning Team?"]).size().reset_index(name="Count")

# Gráfico: Relación entre posición y resultado del equipo
relacion = relacion.sort_values(by='Count', ascending=False)
barra_relacion = px.bar(
    relacion,
    x="Position",
    y="Count",
    color="Winning Team?",
    barmode="group",
    title="Relación entre Posición y Resultado del Equipo",
    labels={"Position": "Posición", "Count": "Número de Ocurrencias", "Winning Team?": "¿Ganó el Equipo?"}
)
barra_relacion.write_html("visualizations/Barra_relacion.html")

# Gráfico: Distribución total de contusiones por posición
barra = px.bar(
    total_contusiones,
    x="Position",
    y="Count",
    title="Distribución de Contusiones por Posición",
    labels={"Count": "Número de Contusiones", "Position": "Posición"}
)
barra.write_html("visualizations/Barra_posiciones.html")

# Gráfico: Distribución de resultados de partidos
torta = px.pie(
    resultados_partidos,
    values="Count",
    names="Winning Team?",
    title="Distribución de Resultados de Partidos",
    labels={"Winning Team?": "¿Ganador del Partido?", "Count": "Cantidad de Partidos"}
)
torta.write_html("visualizations/Torta_resultados.html")

# Mostrar mensaje para confirmar los guardados
print("Visualizaciones generadas y guardadas en la carpeta 'visualizations'.")
