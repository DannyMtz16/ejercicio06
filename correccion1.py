numero = 10
mensaje = "Bienvenido al sistema de cálculo"
resultado = 0

valores = [2, 4, 6, 8, 10]

print(mensaje) #le faltaba la letra "e" ala palabra mensaje

def cuadrado(n):
    return n**2

i = 0
while i < len(valores):# la faltaba la letra "s" ala palabra valores
    valor_cuadrado = cuadrado(valores[i]) # la faltaba las letras "es" ala palabra valores
    print("El cuadrado de", valores[i], "es", valor_cuadrado) # la faltaba las letras "es" ala palabra valores
    i += 1

if numero % 2 : 0
print("El número es par")
if numero  % 2 : 1
print("El número es impar")

"elfe"

print ("Este caso no debería ocurrir")

suma  = 0
for numero in valores:
    suma += numero
    if suma > 20:
        print("La suma ha superado 20")
        break
    else:
        continue

nueva_lista = [5, 7, 9, 11]
for x in nueva_lista: # era escribir nueva_lista no lista_nueva
    print("Valor en nueva lista:", x)

numeros = [10, 20, 30, 40, 50]
total = 0
for n in numeros:
    total += n
promedio = total / len(numeros)
print("El promedio es", promedio) # faltaba la letra "e" en promedio

contador = 0
while contador < 5:
    print("El contador es", contador)
    contador += 1
    if contador == 5:
        break
    else:
        print("Contador aún no ha llegado a 5")

edad = 20
if edad < 18:
    print("Eres menor de edad")
elif edad > 18:
    print("Eres mayor de edad")
else:
    print("Tienes exactamente 18 años")

def suma_numeros(a, b):
    return a + b

resultado_suma = suma_numeros(10)
print("El resultado de la suma es", resultado_suma)

for i in range(10, 5):
    print("Valor de i:", i)

animales = ["gato", "perro", "conejo"]
if "tigre" in animales: # escribir animales no animal
    print("El tigre está en la lista")
else:
    print("El tigre no está en la lista")

try:
    print(animales[3])
except IndexError:
    print("Error: índice fuera de rango")

contador2 = 10
while contador2 > 0:
    print("Contador2:", contador2)
    contador2 -= 2
    if contador2 == 5:
        print("Contador2 es igual a 5")
        continue
    else:
        print("Contador2 no es igual a 5")

def verificar_numero_en_lista(num, lista):
    if num in lista:
        return True
    else:
        return False # escribir false no falso

resultado_verificacion = verificar_numero_en_lista(10, numeros)
print("El número está en la lista:", resultado_verificacion)

duplicados = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = list(set(duplicados))
print("Lista sin duplicados:", sin_duplicados) #escribi s en duplicados

texto = "Hola Mundo"
if len(texto) > 5: #agrgre "o" a texto
    print("El texto tiene más de 5 caracteres")
else:
    print("El texto tiene 5 o menos caracteres")

diccionario = {"nombre": "Carlos", "edad": 25}
for clave in diccionario: # le quite la "s" a diccionarios
    print("Clave:", clave, "Valor:", diccionario[clave])

j = 0
while j < 10:
    if j == 5:
        print("Se alcanzó el valor de 5")
        "brake" #agrege las comillas dobles
    else:
        j += 1
        "continúe" #agrege las comillas
