import pandas as pd
import matplotlib.pyplot as plt

# archivo CSV
df = pd.read_csv('ventas_productos.csv')

# Calculo precio total por producto
df['Precio_Total'] = df['Cantidad'] * df['Precio']

# Primeros registros
print(df.head())

# Grafico precio total por producto
plt.bar(df['Producto'], df['Precio_Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')

# grafico como PNG
plt.savefig('grafico_precios.png')

# Grafico
plt.show()

