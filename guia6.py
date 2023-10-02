import math
#Ej 1.1
def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

#1.2
def imprimir_verso():
    print("Y dale alegria alegria a mi corazon,\nlo unico que te pido es salir campeon")

imprimir_verso()
#1.3
def raiz2():
    x = round(math.sqrt(2),4)
    print(x)

raiz2()

#1.4
def factorial_2():
    print(math.factorial(2))

factorial_2()

#1.5
def perimetro():
    print(math.pi * 2)

perimetro()

#2.1
def imprimir_saludo(nombre: str):
    print("Hola:",nombre)

imprimir_saludo("Juan")

#2.2
def raiz_cuadrada_de(numero):
    math.sqrt(numero)

raiz_cuadrada_de(9)

#2.3
def fahr_a_celcius(t):
    res = ((t - 32) * 5)/9
    return res
print(fahr_a_celcius(100))

#2.4
def imprimir_dos_veces(estribillo):
    print(estribillo*2)

imprimir_dos_veces("I still havent found what im looking for ")

#2.5
def es_multiplo_de(n: int, m: int):
    if (n%m == 0):
        return True
    return False
print(es_multiplo_de(45,15))   

#2.7
def cantidad_de_pizzas(comensales, min_cantidad_de_porciones):
    cant_total = comensales * min_cantidad_de_porciones
    res = math.trunc(cant_total/8) + 1
    return res
print(cantidad_de_pizzas(9,3))

#3.1
def alguno_es_0(numero1,numero2):
    res = numero1 == 0 or numero2 == 0
    return res

print(alguno_es_0(50,20))

#3.2
def ambos_son_0(numero1,numero2):
    res = numero1 == 0 and numero2 == 0
    return res

print(ambos_son_0(0,10))
 
#3.3 and, or, not. Resolverlos sin utilizar alternativa condicional (if)
def es_nombre_largo(nombre: str):
    res = (len(nombre)>=3) and (len(nombre)<=8)
    return res

print(es_nombre_largo("Rodri"))


#3.4
def es_bisiesto(año):
    res = es_multiplo_de(año,400) or ((es_multiplo_de(año,4) and not(es_multiplo_de(año,100))))
    return res

print(es_bisiesto(2012))

#4.1
def peso_pino(altura):
    if altura > 3:
        parte_baja = 3 * 3 * 100
        parte_alta = 2 * (altura - 3) * 100
        res = parte_baja + parte_alta
    else:
        res = 3 * altura * 100
    return res
print(peso_pino(3))
def es_peso_util(peso):
    if(peso >= 400 and peso <= 1000):
        return True
    else:
        return False
print(es_peso_util(600))

def sirve_pino(altura):
    return es_peso_util(peso_pino(altura))

print(sirve_pino(4))


#5.1
def devolver_el_doble_si_es_par(numero):
    if (numero%2 == 0):
        return 2*numero
    return numero

print(devolver_el_doble_si_es_par(5))

#5.2
def par_o_el_que_sigue(numero):
    if (numero%2 == 0):
        return numero
    return numero+1
print(par_o_el_que_sigue(6))

def doble_mult3_triple_mult9(numero):
    if numero%3 == 0:
        return 2*numero
    if numero%9 == 0:
        return 3*numero
    return numero
print(doble_mult3_triple_mult9(9))

#5.4
def lindo_nombre(nombre):
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    return "Tu nombre tiene menos de 5 caracteres"

print(lindo_nombre("Juaen"))

#5.5
def elRango(numero):
    if numero < 5:
        return "menor a 5"
    if (numero > 10 and numero < 20):
        return 'entre los 10 y 20'
    if numero > 20:
        return "mayor a 20"
    return numero
        
print(elRango(117))

#5.6
def trabajo_o_vacas(sexo,edad):
    if sexo == "F":
        if edad < 18 or edad > 60:
            return "anda de vacaciones"
        else:
            return "te toca laburar"
    elif sexo == "M":
        if edad < 18 or edad > 65:
            return "anda de vacaciones"
        else:
            return "te toca laburar"

print(trabajo_o_vacas("F",65))   

#6.1
def print_1al10():
    i:int = 1
    while i <= 10:
        print(i)
        i+=1

print_1al10()

#6.2
def print_pares_10al40():
    i = 10
    while i <= 40:
        print(i)
        i+=2

print_pares_10al40()

#6.3
def eco_10():
    i = 1
    while i <= 10:
        print("eco")
        i+=1

eco_10()

#6.4
def despegue(numero):
    i = numero
    while i > 0:
        print(i)
        i-=1
    print("Despegue!")

despegue(10)