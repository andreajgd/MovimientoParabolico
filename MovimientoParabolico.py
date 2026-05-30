# Importamos la libreríapara usar funciones
# como tan(), cos() y la conversión a radianes.
import math


# Funcion que calcula la trayectoria de un proyectil
# y muestra una tabla con los valores de X y Y
def trayectoria(y0, v0, angulo):

    # Aceleración de la gravedad (m/s²)
    g = 9.81

    # Convertimos el ángulo de grados a radianes,
    # ya que las funciones trigonometricas de Python
    # trabajan con radianes
    theta = math.radians(angulo)

    # Valor inicial de la distancia horizontal
    x = 0

    # Encabezado de la tabla
    print(f"{'X':<10}{'Y':<10}")
    print("-" * 20)

    # Se repite el calculo hasta que Y sea negativa
    while True:

        # Ecuacion de la trayectoria:
        # y = y0 + x*tan(theta) - [g*x² / 2(v0*cos(theta))²]
        y = y0 + x * math.tan(theta) - (
            g * x**2 /
            (2 * (v0 * math.cos(theta))**2)
        )

        # Mostramos los valores de X y Y
        print(f"{x:<10}{y:.2f}")

        # Si la altura es negativa, se detiene el ciclo
        if y < 0:
            break

        # Incrementamos X en 1 unidad
        x += 1


# Solicita al los datos
y0 = float(input("Altura inicial: "))
v0 = float(input("Velocidad inicial: "))
angulo = float(input("Ángulo: "))

trayectoria(y0, v0, angulo)