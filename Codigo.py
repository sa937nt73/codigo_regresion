import matplotlib.pyplot as plt

def regresion_lineal(datos):
  n = len(datos)

  x_vals = [p[0] for p in datos]
  y_vals = [p[1] for p in datos]

  x_barra = sum(x_vals) / n
  y_barra = sum(y_vals) / n

  Sxx = sum((x - x_barra) ** 2 for x in x_vals)
  Sxy = sum((x - x_barra) * (y - y_barra) for x, y in zip(x_vals, y_vals))


  m = Sxy / Sxx
  b = y_barra - m * x_barra

  # R^2

  SStot = sum((y - y_barra) ** 2 for y in y_vals)
  SSres = sum((y - (m * x + b)) ** 2 for x, y in zip(x_vals, y_vals))

  R2 = 1 - (SSres / SStot)

  return m, b, R2, x_vals, y_vals


#========= Datos de ejemplo ==========
# Datos de salario vs experiencia

datos = [(1, 30000), (2, 35000), (3, 42000), (4, 47000), (5, 35000)]


# Calcular la regresión
m, b, R2, x_vals, y_vals = regresion_lineal(datos)

# Mostrar resultados
print("=" * 50)
print("RREGRESIÓN LINEAL - RESULTADOS")
print("=" * 50)
print(f"Ecuación: y = {m:.2f}x + {b:.2f}")
print(f"R^2 = {R2:.6f}")
print("=" * 50)


# Predecir para x = 7
x_pred = 7
y_pred = m * x_pred + b
print(f"Predicción para x = {x_pred}: y = {y_pred:.2f}")
print("=" * 50)


# ==== GRÁFICA ====
plt.figure(figsize=(8, 5))


# Datos originales
plt.scatter(x_vals, y_vals, color='blue', s=50, label='Datos originales')


# Línea de regresión
x_linea = [min(x_vals), max(x_vals)]
y_linea = [m * x + b for x in x_linea]
plt.plot(x_linea, y_linea, color='red', linewidth=2, label='Regresión lineal')


# Punto predicho
plt.scatter([x_pred], [y_pred], color='green', s=100, marker='*', label=f'Predicción x={x_pred}')


# Presonalizar
plt.xlabel('Experiencia (años)', fontsize=12)
plt.ylabel('Salario', fontsize=12)
plt.title('Regresión lineal - Salario vs Experiencia', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()