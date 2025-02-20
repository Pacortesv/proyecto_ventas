import pandas as pd
import matplotlib.pyplot as plt

# archivo CSV
df = pd.read_csv('ventas_productos.csv')

# Precio total por producto
df['Precio_Total'] = df['Cantidad'] * df['Precio']

# Primer registro
print(df.head())

# Grafico
plt.bar(df['Producto'], df['Precio_Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')

# grafico PNG
plt.savefig('grafico_precios.png')

# grafico
plt.show()

