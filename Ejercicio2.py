# Ejercicio 1
# nro=int(input("Por favor ingrese un número impar: "))

# while nro%2==0:
#     nro=int(input("El número ingresado no es impar, por favor ingrese un número impar: "))
# print("El número ingresado es impar")

# Ejercicio 2
nro1=int(input("Por favor, ingrese un número: "))
nro2=int(input("Por favor, ingrese otro número: "))
opcion=int(input("Por favor seleccione qué operación realizar con los números ingresados: \n1. Sumar \n2. Restar \n3. Multiplicar \nOpcion elegida: "))

if opcion == 1:
    resultado=nro1+nro2
    print(f"El resultado de la suma es {resultado}")
elif opcion == 2:
    resultado=nro1-nro2
    print(f"El resultado de la resta es {resultado}")
elif opcion == 3:
    resultado=nro1*nro2
    print(f"El resultado de la multiplicación es {resultado}")
else:
    opcion=int(input("Opción inexistente. \nPor favor seleccione qué operación realizar con los números ingresados: \n1. Sumar \n2. Restar \n3. Multiplicar \nOpcion elegida: "))
    