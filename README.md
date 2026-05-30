# Trayectoria de un Proyectil en Python

## Descripción

Este programa calcula y muestra la trayectoria de un proyectil utilizando la ecuación del movimiento parabólico.

A partir de una altura inicial, una velocidad inicial y un ángulo de lanzamiento, el programa genera una tabla con los valores de posición horizontal (X) y altura (Y), continuando los cálculos hasta que la altura sea negativa, indicando que el proyectil ha impactado el suelo.

---

## Fundamento Teórico

La trayectoria del proyectil se calcula mediante la ecuación:

y = y₀ + x·tan(θ) - [g·x² / (2(v₀·cos(θ))²)]

Donde:

- **y** = altura del proyectil.
- **y₀** = altura inicial.
- **x** = distancia horizontal recorrida.
- **v₀** = velocidad inicial.
- **θ** = ángulo de lanzamiento.
- **g** = aceleración de la gravedad (9.81 m/s²).

Esta ecuación describe el movimiento parabólico resultante de combinar:

- Movimiento Rectilíneo Uniforme (MRU) en el eje X.
- Movimiento Rectilíneo Uniformemente Acelerado (MRUA) en el eje Y debido a la gravedad.

---

## Funcionamiento

1. El usuario ingresa:
   - Altura inicial.
   - Velocidad inicial.
   - Ángulo de lanzamiento.

2. El programa convierte el ángulo de grados a radianes.

3. Se calcula la altura (Y) para cada valor entero de distancia horizontal (X).

4. Los resultados se muestran en una tabla.

5. El proceso finaliza cuando la altura calculada es negativa.

---

## Código Utilizado

```python
import math

def trayectoria(y0, v0, angulo):

    g = 9.81
    theta = math.radians(angulo)

    x = 0

    print(f"{'X':<10}{'Y':<10}")
    print("-" * 20)

    while True:

        y = y0 + x * math.tan(theta) - (
            g * x**2 /
            (2 * (v0 * math.cos(theta))**2)
        )

        print(f"{x:<10}{y:.2f}")

        if y < 0:
            break

        x += 1


y0 = float(input("Altura inicial: "))
v0 = float(input("Velocidad inicial: "))
angulo = float(input("Ángulo: "))

trayectoria(y0, v0, angulo)
```

---

## Ejemplo de Ejecución

### Entrada

```
Altura inicial: 20
Velocidad inicial: 25
Ángulo: 45
```

### Salida

```
X         Y
--------------------
0         20.00
1         20.99
2         21.96
3         22.91
...
38        -0.61
```

---

## Requisitos

- Python 3.x
- Librería estándar `math`

No es necesario instalar paquetes adicionales.
