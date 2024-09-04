def crear_tabla_pitagoras(tamano):
    tabla = [[(i + 1) * (j + 1) for j in range(tamano)] for i in range(tamano)]
    return tabla

def mostrar_tabla(tabla):
    for fila in tabla:
        print(' '.join(map(str, fila)))

def multiplicar(factor1, factor2, tabla):
    return tabla[factor1 - 1][factor2 - 1]

# Crear y mostrar la tabla de Pitágoras
tamano = 10
tabla_pitagoras = crear_tabla_pitagoras(tamano)
mostrar_tabla(tabla_pitagoras)

# Solicitar factores al usuario
factor1 = int(input("Introduce el primer factor: "))
factor2 = int(input("Introduce el segundo factor: "))

# Realizar la multiplicación y mostrar el resultado
resultado = multiplicar(factor1, factor2, tabla_pitagoras)
print(f"El resultado de {factor1} x {factor2} es: {resultado}")