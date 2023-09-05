# Punto 1
lista = []

def consulta():
    nombresuc=int(input("Ingrese el nombre de sucursal: "))
    if nombresuc!=0:
        total=0
        posicion=0
        cantventas=int(input("Ingrese la cantidad de ventas: "))
        ventatotal=int(input("Ingrese la venta total de la sucursal: $"))
        promedio = round(ventatotal/cantventas,2)
        lista.insert(posicion,[[nombresuc],[cantventas],[ventatotal],[promedio]])
        posicion=posicion+1
        consulta()
        total=total+ventatotal
        print(total)
    else:
        for suc in lista:
            print(suc)
    
consulta()

# No puedo indicar el total vendido por toda la cadena por el scope del total asumo, pero no pude asociar como sacarlo del primer condicional y que me lo siga tomando. Me queda el siguiente resultado:
# [[2], [1321], [68789465], [52073.78]]
# [[1], [2], [6548], [3274.0]]
# [[1], [2], [654], [327.0]]
# 68789465
# 6548
# 654


