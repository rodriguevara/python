import array

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
        if s[i] >= s[i+1]:
            
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

def sinVocales(s: str) -> str:
    vocs = ["a","e","i","o","u"]
    newStr = ""
    for i in range(0,len(s)):
        if not pertenece3(vocs,s[i]):
            newStr += s[i]
    return newStr

print(sinVocales("Holaquetal"))