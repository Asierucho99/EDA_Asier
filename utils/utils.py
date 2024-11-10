import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def cargar_datos(archivos, delimiter=';', encoding='utf-8'):
    
    data = ('data')
    return pd.concat(
        [pd.read_csv(archivo, delimiter=delimiter, encoding=encoding) for archivo in data],
        ignore_index=True
    )

def accidentes_por_columna(df, columna, top_n=10):

    conteo = df.groupby(columna).size().reset_index(name='TOTAL').sort_values(by='TOTAL', ascending=False)
    return conteo.head(top_n)

def graficar_accidentes_por_columna(df, columna, titulo, xlabel, ylabel, top_n=10):

    top_data = accidentes_por_columna(df, columna, top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_data, x='TOTAL', y=columna, palette='viridis')
    plt.title(titulo, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.show()

def accidentes_por_año(df):

    conteo = df.groupby('ANYO').size().reset_index(name='TOTAL')
    plt.figure(figsize=(10, 6))
    sns.barplot(data=conteo, x='ANYO', y='TOTAL', palette='viridis')
    plt.title('Distribución de Accidentes por Año', fontsize=16)
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Total de Accidentes', fontsize=12)
    plt.tight_layout()
    plt.show()
    return conteo


