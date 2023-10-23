import array
import random
import numpy as np
s = [1,2,3,4]
e = 6
f = "F"
abc = "abcdefghijklmnñopqrstuvwxyz"
abcMayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
nums = "0123456789"
#1.1
def pertenece1(s: [int], e: int) -> bool:
    for i in range(0,len(s),1):
        if s[i] == e:
            return True
    return False

def pertenece2(s: list, e: int) -> bool:
    i = 0
    print(len(s))
    while i < len(s):
        if s[i] == e:
            return True
        i+=1
    return False

#print(pertenece2(s,e))

def pertenece3(s,e) -> bool:
    for i in range(0,len(s),1):
        if s[i] == e:
            return True
    return False

#print(pertenece3(["a","e","i","o","u"],"f"))

#1.2
def divideATodos(s:[int], e: int) -> bool:
    for i in range(0,len(s),1):
        if s[i] % e != 0:
            return False
    return True

#print(divideATodos([4,6,8],2))

#1.3



def sumaTotal(s: [int]) -> int:
    res: int = 0
    for i in range(0,len(s),1):
        res += s[i]

    return res

#print(sumaTotal(s))

#1.4

def ordenados(s:list) -> bool:
    for i in range(0,len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

#print(ordenados([1,2,3,3]))

#1.5
def palabraLarga(s:list) -> bool:
    for i in range(0,len(s)):
        if len(s[i]) >= 7:
            return True
    return False

#print(palabraLarga(["elefante"]))

#1.6
def palindromo(s: str) -> bool:
    for i in range(0,len(s)):
        if s[i] != s[-1-i]:
            return False
    return True

#1.7

abc = "abcdefghijklmnñopqrstuvwxyz"
abcMayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
nums = "0123456789"

def contraseña(s: str) -> str:
    cond1 = False
    cond2 = False
    cond3 = False
    res = ""
    if len(s) < 5:
        return "ROJA"

    for i in range(0,len(s)):
        if pertenece3(abc,s[i]):
            cond1 = True
        if pertenece3(abcMayus,s[i]):
            cond2 = True
        if pertenece3(nums,s[i]):
            cond3 = True
    if cond1 == True and cond2 == True and cond3 == True and len(s) > 8:
        return "VERDE"
    return "AMARILLA"

#print(contraseña("Holaquetal1"))

def contraseña2(s: str) -> str:
    cond1 = False
    cond2 = False
    cond3 = False

    res = ""

    for i in range(0,len(s)):
        if s[i] <= "z" and s[i] >= "a":
            cond1 = True
        if s[i] <= "Z" and s[i] >= "A":
            cond2 = True
        if s[i] <= "9" and s[i] >= "0":
            cond3 = True

    if cond1 == True and cond2 == True and cond3 == True and len(s) > 8:
        res = "VERDE"
    elif len(s) < 5:
        res = "ROJA"
    else:
        res = "AMARILLA"
    return res

#print(contraseña2("Holaquetal1"))



#1.8

def saldo(s: list) -> int:
    res = 0
    for i in range(0,len(s)):
        if s[i][0] == "I":
            res += s[i][1]
        else:
            res -= s[i][1]
    return res

#print(saldo([("I",2000), ("R", 20),("R", 1000),("I", 300)]))

#1.9
def tresVocales(s: str) -> bool:
    vocs = ["a","e","i","o","u"]
    s = s.lower()
    vocsDistintas = 0
    res = False
    for i in range(0,len(s)):
        if pertenece3(vocs,s[i]):
            vocsDistintas +=1
            vocs.remove(s[i])
    if vocsDistintas >= 3:
        res = True
    return res

#print(tresVocales("aadadaaa"))

#2.1
def paresBorra0(s: list) -> list:
    for i in range(0,len(s),2):
        s[i] = 0
    return s

#print(paresBorra0([1,2,3,4,5,6,7]))

#2.2
def paresBorraNuevaLista(s:list) -> list:
    newList = []
    for i in range(0,len(s)):
        if i % 2 == 0:
            newList.append(0)
        else:
            newList.append(s[i])
    print(s)
    return newList

#print(paresBorraNuevaLista([1,2,3,4,5]))
# 2.3
def sinVocales(s: str) -> str:
    vocs = ["a","e","i","o","u"]
    newStr = ""
    for i in range(0,len(s)):
        if not pertenece3(vocs,s[i]):
            newStr += s[i]
    return newStr

# print(sinVocales("Holaquetal"))

# 2.4
def reemplazaVocales(s: list) -> list:
    vocs = ["a","e","i","o","u"]
    newStr = ""
    for i in range(0,len(s)):
        if not pertenece3(vocs,s[i]):
            newStr += s[i]
        else:
            newStr += '-'
    return newStr
# print(reemplazaVocales("Holaquetal"))

# 2.5

def daVueltaString(s: str) -> str:
    newStr = ""
    for i in range(0,len(s)):
        newStr += s[-1-i]
    return newStr

# print(daVueltaString("Holaquetal"))

# 2.6
def eliminarRepetidos(s:str) -> str:
    newStr = ''
    for i in range(0,len(s)):
        if not pertenece3(newStr,s[i]):
            newStr += s[i]
    return newStr
# print(eliminarRepetidos('menemer'))

# 3
def aprobado(s: list) -> int:
    res = 0
    promedio = sumaTotal(s)/len(s)

    if promedio < 4 or menorA4(s) == True:
        res = 3
    elif promedio < 7:
        res = 2
    else:
        res = 1
    return res


def menorA4(s: list) -> bool:
    for i in range(0,len(s)):
        if s[i] < 4:
            return True
    return False

# print(aprobado([10,4,-4]))
# 4.1
def nombresEstudiantes() -> list:
    res = []
    palabraEscape = 'listo'
    estudiante: str = input('ingrese el nombre del estudiante: ')
    while estudiante != 'listo':
        res.append(estudiante)
        estudiante: str = input('ingrese el nombre del estudiante: ')
    return res
# print(nombresEstudiantes())

# 4.2
def historial() -> list:
    accion: str = input('Ingrese la accion: C para cargar, D para descontar, X para terminar: ')
    total: int = 0
    res = []
    while accion != 'X':
        monto: int = input('Ingrese la cantidad: ')
        if accion == 'C':
            print(monto)
            total += int(monto)
            res.append([accion,monto,total])
        elif accion == 'D':
            total -= int(monto)
            res.append([accion,monto,total])
        accion: str = input('Ingrese una nueva accion: C para cargar, D para descontar, X para terminar: ')
    return res

# print(historial())

# 4.3
def juego() -> str:
    numsjuego = [1,2,3,4,5,6,7,10,11,12]
    accion = input('Enter para pedir una carta: ')
    cuenta = 0
    while accion != 'plantarse':
        paso = random.choice(numsjuego)
        if paso > 9:
            cuenta += 0.5
        else:
            cuenta += paso
        if cuenta > 7.5:
            print(cuenta)
            return 'perdiste'
        print(cuenta)
        accion: str = input('Ingrese plantarse para finalizar o enter para pedir una carta: ')
    return cuenta
# print(juego())
# 5.1
def perteneceACadaUno(s: [[int]], e: int) -> [bool]:
    res = []
    for i in range(0,len(s)):
        if pertenece3(s[i],e):
            res.append(True)
        else:
            res.append(False)
    return res

# print(perteneceACadaUno([[1,2,3,5],[3,4,5]],5))
# 5.2
def esMatriz(s: [[int]]) -> bool:
    for i in range(1,len(s)):
        if len(s[i]) != len(s[0]):
            return False
    return True

# print(esMatriz([[0,1,2],[3,4]]))

# 5.3
def filasOrdenadas(s: [[int]]) -> [bool]:
    res = []
    for i in range(0,len(s)):
        if ordenados(s[i]):
            res.append(True)
        else:
            res.append(False)
    return res

# print(filasOrdenadas([[0,1,2],[3,3,4,4]]))
# 5.4
def potenciaMatriz(d: int, p: int) -> list:
    m = np.random.random((d, d))**2
    p = np.linalg.matrix_power(np.array(m),p)
    return p
# print(potenciaMatriz(5,3))
