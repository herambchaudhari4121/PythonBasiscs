#Librerias

import time

#Funciones (Ejercicios)

def Ej1():
    print("Compras")

    C = int(input("Ingrese la cantidad: "))
    VU = int(input("Ingrese el valor unitario: "))
    T= C * VU
    print("El valor total es de: ",T)
    time.sleep(3)

    #Volver al menu
    VM()


def Ej2():
    print("Servicio de estacionamiento")

    VPH = int(input("Ingrese el valor de la hora: "))
    CH = int(input("Ingrese la cantidad de horas: ")) 
    VP = VPH * CH
    print("El valor total es de: ",VP)
    time.sleep(3)

    #Volver al menu
    VM()


def Ej3():
    print("Espectaculo")

    VE = int(input("Ingrese el valor de la boleta: "))
    VD = VE * 0.20
    T = VE - VD
    print("El descuento es de:", VD)
    print("La boleta queda en: ",T)
    time.sleep(3)

    #Volver al menu
    VM()


def Ej4():
    print("Promedio")

    n1 = float(input("Ingrese nota 1: "))
    n2 = float(input("Ingrese nota 2: "))
    n3 = float(input("Ingrese nota 3: "))
    n4 = float(input("Ingrese nota 4: "))
    n5 = float(input("Ingrese nota 5: "))
    S = round (n1 + n2 + n3 + n4 + n5, 2) / 5
    print("El promedio es de: ",S)
    time.sleep(3)

    #Volver al menu
    VM()


def Ej5():
    print("Colegio")

    CM = int(input("Ingrese la cantidad de meses: "))
    VMC = int(input("Ingrese el valor de cada mes: "))
    T= CM * VMC
    print("El valor total es de: ",T)
    time.sleep(3)

    #Volver al menu
    VM()


def Ej6():
    print("Compras")

    VP = int(input("Ingrese el valor total: "))
    VD = VP * 20/100
    VPD = VP - VD
    print("El descuento equivale a: ",VD)
    print("El valor total es de:", VPD)
    time.sleep(3)

    #Volver al menu
    VM()

def Ej7():
    print("Nomina")
    SB = int(input("Ingrese el salario basico mensual: "))
    CD = int(input("Ingrse la cantidad de dias laborales: "))
    V = SB / 30
    VN = CD * V
    print("El valor de la nomina es: ",VN)
    time.sleep(3)

    #Volver al menu
    VM()

def Ej8():
    print("Area triangulo")
    B = int(input("Ingrese la base del triangulo: "))
    H = int(input("Ingrese la altura del triangulo: "))
    A = (B * H) / 2
    print("El area del triangulo equivale a: ",A)
    time.sleep(3)

    #Volver al menu
    VM()

def Ej9():
    print("Muestre nomina")
    B = int(input("Ingrese la bonificacion: "))
    CH = int(input("Ingrese la cantidad de hijos: "))
    S = int(input("Ingrese sueldo: "))
    BT = S * 0.10
    B = BT * CH
    T = B + S
    print("La bonificacion es de: ",B)
    print("El total a pagar es de: ",T)
    time.sleep(3)

    #Volver al menu
    VM()


def Ej10():
    print("Calificacion Final")

    N1 = float(input("Ingrese nota 1: "))
    N2 = float(input("Ingrese nota 2: "))
    N3 = float(input("Ingrese nota 3: "))
    N4 = float(input("Ingrese nota 4: "))
    N5 = float(input("Ingrese nota 5: "))
    NA = N1 * 0.15
    NB = N2 * 0.30
    NC = N3 * 0.25
    ND = N4 * 0.10
    NE = N5 * 0.20
    F = (NA + NB + NC + ND + NE)
    print("La calificacion final es: ",F)
    time.sleep(3)

    #Volver al menu
    VM()

    

def Ej11():
    print("Descuentos")

    S = int(input("Ingrese el salario base: "))
    SH = S * 0.01
    SS = S * 0.04
    SF = S * 0.05
    CA = S * 0.05
    D = SH + SS + SF + CA
    TP = S - D
    print("El descuento equivale a: ",D)
    print("El total a pagar es de:", TP)
    time.sleep(3)

    #Volver al menu
    VM()

def Ej12():
    print("Banco")
    S = int(input("Saldo del ahorrista: "))
    SI = S * 0.015
    SL = S + SI
    print("Saldo final: ",SL)
    time.sleep(3)

    #Volver al menu
    VM()

#Volver al menu
def VM():
    UserI = input("¿Quieres elegir otro ejercicio?\n")
    if UserI == "Si":
        Menu()
    elif UserI == "si":
        Menu()
    else:
        return()

#Menu

def Menu():
    SEJ = input("Seleccione un ejercicio: ")

    if SEJ == "1":
        Ej1()
    elif SEJ == "2":
        Ej2()
    elif SEJ == "3":
        Ej3()
    elif SEJ == "4":
        Ej4()
    elif SEJ == "5":
        Ej5()
    elif SEJ == "6":
        Ej6()
    elif SEJ == "7":
        Ej7()
    elif SEJ == "8":
        Ej8()
    elif SEJ == "9":
        Ej9()
    elif SEJ == "10":
        Ej10()
    elif SEJ == "11":
        Ej11()
    elif SEJ == "12":
        Ej12()
    else:
        print("La entrada es invalida, intentalo de nuevo")
        Menu()



Menu()
