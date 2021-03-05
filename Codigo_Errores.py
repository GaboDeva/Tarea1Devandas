b = 12  # constante utilizada


def y_rectax(x, m, b):

    # toma los valores introducidos para obtener el valor y de una rexta "mx+b"

    y = (m * x) + b
    return y


# solicita los valores deseados

m = int(input("Introduzca el valor de m de la recta: "))
x = int(input("introduzca el valor de x de la recta: "))

# Imprime el resultado y

print("El valor de y es: ", y_rectax(x, m, b))
