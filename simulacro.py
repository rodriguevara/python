# problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#   requiere: {e pertenece a s }
#   asegura: {res es la posición de la última aparición de e en s}
# }

# TIP: realizar la iteración mediante índices y no mediante elementos

# Por ejemplo, dados
# s = [-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]
# e = 0
# se debería devolver res = 7

def ultima_aparicion(s: [int], e: int) -> int:
    indice = 0
    for i in range(0,len(s)):
        if e == s[i]:
            indice = i
    return indice
s = [1,2,3,4,1,6]
# print(ultima_aparicion(s,1))

def elementos_exclusivos(s:[int],t:[int]) ->[int]:
    elementos = []
    for i in s:
        if not i in t:
            elementos.append(i)
    for i in t:
        if not i in s:
            elementos.append(i)
    return list(set(elementos))
s = [-1, 4, 0, 4, 3, 0, 100, 0, -1, -1]
t = [0, 100, 5, 0, 100, -1, 5]
# print(elementos_exclusivos(s,t))

def contar_traducciones_iguales(ing: dict, ale: dict) -> int:
    contador = 0
    for k,v in ing.items():
        if v == ale[k]:
            contador +=1
    return contador

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
# print(contar_traducciones_iguales(ingles,aleman))

def convertir_a_diccionario(lista:list) -> dict:
    diccionario = dict()
    for i in lista:
        if not i in diccionario.keys():
            diccionario[i] = 1
        else:
            diccionario[i] += 1
    return diccionario

lista = [-1, 0, 4, 100, 100, -1, -1]
print(convertir_a_diccionario(lista))


lista = [-1, 0, 4, 100, 100, -1, -1]
