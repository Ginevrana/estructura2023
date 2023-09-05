# Punto 1
# def area_rectangulo(b,a):
#     resultado= b*a
#     print(f"El área del rectángulo es {resultado}")

# area_rectangulo(5,3)

# Punto 2
# pi=3.14159

# def area_circulo(r):
#     resultado=pi*(r**2)
#     print(f"El área del círculo es {resultado}")

# area_circulo(5)

# Punto 3
# def relacion(nro1,nro2):
#     if nro1>nro2:
#         print(1)
#     elif nro1<nro2:
#         print(-1)
#     else:
#         print(0)

# relacion(5,2)

# Punto 4
# def intermedio(n1,n2):
#     resultado=((n2-n1)/2)+n1
#     print(f"El punto intermedio entre {n1} y {n2} es {resultado}")

# intermedio(12,50)

# Punto 5
def recortar(nro,liminf,limsup):
    if int(nro)>int(limsup):
        print(int(limsup))
    elif int(nro)<int(liminf):
        print(int(liminf))
    else:
        print(int(nro))

recortar(10,8,9)