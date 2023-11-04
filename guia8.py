from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# 1.1
def contar_lineas(nombre_archivo : str) -> int:
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

# print(contar_lineas("archivo_palabras.txt"))

# 1.2
def existe_palabra(palabra : str, nombre_archivo : str) -> bool:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    contenido = contenido.split()
    res = pertenece3(contenido, palabra)
    # otra opcion es res = palabra in contenido
    archivo.close()

    return res

def pertenece3(s,e) -> bool:
    for i in range(0,len(s),1):
        if s[i] == e:
            return True
    return False

# print(existe_palabra("prueba","archivo_palabras.txt"))

# 1.3
def cantidad_apariciones(nombre_archivo:str, palabra:str) -> int:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read().split()
    contador = 0
    for i in range(0,len(contenido)):
        if contenido[i] == palabra:
            contador += 1
    archivo.close()
    return contador
# print(cantidad_apariciones("archivo_palabras.txt",'prueba'))

# 2
def clonar_sin_comentarios(nombre_archivo:str) -> str:
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    lineas_sin_comentarios = []
    for i in range(0,len(lineas)):
        if lineas[i][0] == '#':
            lineas_sin_comentarios.append(lineas[i].lstrip('#'))
        elif lineas[i][0] == ' ':
            intermedio = lineas[i].lstrip() #remueve los espacios a la izquierda
            if intermedio[0] == '#':
                lineas_sin_comentarios.append(intermedio.lstrip('#'))
            else:
                lineas_sin_comentarios.append(intermedio)
        else:
            lineas_sin_comentarios.append(lineas[i])
    sin_comments = open('sin_comments.txt', 'x')
    sin_comments.writelines(lineas_sin_comentarios)
    return lineas_sin_comentarios
# print(clonar_sin_comentarios("comentarios.txt"))

# 3
def reverso(nombre_archivo:str) -> str:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.readlines()
    reverso = open('reverso.txt', 'w')
    contenido_reverso = []
    for i in range(0,len(contenido)):
        contenido_reverso.append(contenido[-1-i])
    reverso.writelines(contenido_reverso)
    return contenido_reverso

# print(reverso('archivo_palabras.txt'))

# 4
def agrega_frase(nombre_archivo:str, frase:str) -> str:
    archivo = open(nombre_archivo, 'a')
    archivo.write('\n' + frase)
    archivo.close()
# print(agrega_frase('archivo_palabras.txt', 'esto es una frase'))

#5
def agrega_al_principio(nombre_archivo:str, frase:str) -> str:
    archivo = open(nombre_archivo, 'r+')
    data_archivo = archivo.read()
    archivo.seek(0,0)
    archivo.write(frase + '\n' + data_archivo)
    archivo.close()
# print(agrega_al_principio('archivo_palabras.txt', 'frase al principio'))

#6

def palabras_legibles(nombre_archivo: str) -> list:
    palabrasLegibles = []
    f = open(nombre_archivo, mode="rb")
    palabra = ""
    for lines in f.readlines():
        for letter in lines:
            letter = chr(letter)
            if (letter.isalpha() == True) or (letter.isalnum() == True) or (letter == "_") or (letter == " "):
                palabra += letter
            else:
                if len(palabra) >= 5:
                    palabrasLegibles.append(palabra)
                palabra = ""
    f.close()
    return palabrasLegibles

# print(palabras_legibles('binary.wav'))

# 7
def promedioEstudiante(nombre_archivo: str, LU: str) -> float:
    archivo = open(nombre_archivo, 'r')
    filas : list[str] = archivo.read().split('\n')
    sumador_notas = []
    for fila in filas:
        fila_separada: list[str] = fila.split(',')
        if fila_separada[0] == LU:
            sumador_notas.append(float(fila_separada[-1]))
    res = sum(sumador_notas) / len(sumador_notas)
    return res

# print(promedioEstudiante('p8_historia_academica.csv','820/23'))

# 8
def generar_nros_al_azar(n : int, desde : int, hasta : int) -> Pila:
    pila = Pila()
    for i in range(0,n):
        pila.put(random.randint(desde,hasta))
    return pila

# print(generar_nros_al_azar(10,1,100))

# 9
def cantidad_elementos(p: Pila) -> int:
    return len(p.queue)

# print(cantidad_elementos(generar_nros_al_azar(10,1,100)))

# 10
def buscar_el_maximo(p: Pila) -> int:
    return max(p.queue)

# print(buscar_el_maximo(generar_nros_al_azar(10,1,100)))

# 11
def esta_bien_balanceada(s: str) -> bool:
    p = Pila()
    for char in s:
        if char == '(':
            p.put(char)
        elif char == ')':
            if p.empty():
                return False
            p.get()
    if p.empty():
        return True
    else:
        return False
# print(esta_bien_balanceada('1 + (2 x 3 - (20 / 5))'))

# 12
def postfix(s: str) -> bool:
    tokens = s.split(' ')
    p = Pila()
    for char in tokens:
        if char.isalnum() == True:
            p.put(char)
        else:
            e1 = int(p.get())
            e2 = int(p.get())
            match char:
                case '+':
                    p.put(e1+e2)
                case '-':
                    p.put(e2-e1)
                case '*':
                    p.put(e1*e2)
                case '/':
                    p.put(e2/e1)
    return p.get()

# print(postfix('6 4 + 5 / 2 -')) = 0
# 13
def cola_enteros(p: Pila) -> Cola:
    c = Cola()
    # print(list(p.queue))
    for i in list(p.queue):
        c.put(p.get())
    return c
# print(cola_enteros(generar_nros_al_azar(10,1,100)))

def generar_nros_al_azar_cola(n:int,desde:int,hasta:int) -> Cola:
    cola = Cola()
    for i in range(0,n):
        cola.put(random.randint(desde,hasta))
    return cola

# 14
def cantidad_elementos_cola(c: Cola) -> int:
    contador = 0
    while not c.empty():
        contador+=1
    return contador
# print(cantidad_elementos_cola(generar_nros_al_azar_cola(10,1,100)))

# 15
def buscar_el_maximo_cola(c: Cola) -> int:
    # print(list(c.queue))
    return max(c.queue)

# print(buscar_el_maximo_cola(generar_nros_al_azar_cola(10,1,100)))
# 16
def armar_secuencia_bingo() -> Cola:
    c = Cola()
    while c.qsize() < 100:
        n = random.randint(0,99)
        if not n in list(c.queue):
            c.put(n)
    return c

def jugar_carton_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas = 0
    while len(carton) > 0:
        e = bolillero.get()
        if e in carton:
            carton.remove(e)
        jugadas += 1
    return bolillero.queue, jugadas
# print(jugar_carton_bingo([18,22,31,44,57,60,78,86,97,0,11,12],armar_secuencia_bingo()))

# 17
def n_pacientes_urgentes(c: Cola[int,str,str]) -> int:
    contador = 0
    while not c.empty():
        paciente = c.get()
        if paciente[0] == 1:
            contador +=1
    return contador
cola = Cola()
cola.put([1,'juan','clinica'])
cola.put([3,'test','card'])
# print(n_pacientes_urgentes(cola))

# 18
def a_clientes(c : Cola) -> Cola:
    nueva_cola = Cola()
    cola_preferencial = Cola()
    cola_resto = Cola()

    while not c.empty():
        cliente = c.get()
        if cliente[3] == True:
            nueva_cola.put(cliente)
            continue
        elif cliente[2] == True:
            cola_preferencial.put(cliente)
        else:
            cola_resto.put(cliente)
    while not cola_preferencial.empty():
        nueva_cola.put(cola_preferencial.get())
    while not cola_resto.empty():
        nueva_cola.put(cola_resto.get())
    return nueva_cola

# print(a_clientes(cola_banco))

# 19
def agrupar_por_longitud(nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read().split()
    diccionario = dict()
    for word in contenido:
        if len(word) in diccionario:
            diccionario[len(word)] += 1
        else:
            diccionario[len(word)] = 1
    return diccionario

# print(agrupar_por_longitud('archivo_palabras.txt'))
# 20
def promedio_estudiantes(nombre_archivo : str) -> dict:
    archivo = open(nombre_archivo, 'r')
    filas : list[str] = archivo.read().split('\n')
    filas.pop(0)
    promedios = dict()
    for fila in filas:
        fila_separada: list[str] = fila.split(',')
        if fila_separada[0] not in promedios:
            promedios[fila_separada[0]] = [float(fila_separada[-1]),1]
        else:
            sumador_notas = promedios[fila_separada[0]][0]
            cantidad_notas = promedios[fila_separada[0]][1]
            promedios[fila_separada[0]] = [sumador_notas+float(fila_separada[-1]),cantidad_notas+1]
    for key,value in promedios.items():
        promedios[key] = value[0]/value[1]
    return promedios

# print(promedio_estudiantes('p8_historia_academica.csv'))
# 21
def la_palabra_mas_frecuente(nombre_archivo : str) -> str:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read().split()
    diccionario = dict()
    for word in contenido:
        if word in diccionario:
            diccionario[word] += 1
        else:
            diccionario[word] = 1
    mas_frecuente_key = ''
    mas_frecuente_value = 0
    for k,v in diccionario.items():
        if v > mas_frecuente_value:
            mas_frecuente_key = k
            mas_frecuente_value = v
    return mas_frecuente_key

# print(la_palabra_mas_frecuente('archivo_palabras.txt'))

# 22
historiales = dict()

def visitar_sitio(historiales: dict[str, (Pila, Pila)], usuario:str, sitio: str) -> dict:
    if usuario in historiales.keys():
        historiales[usuario][0].put(sitio)
    else:
        historiales[usuario] = (Pila(), Pila())
        historiales[usuario][0].put(sitio)

    return historiales

def navegar_atras(historiales: dict[str,(Pila,Pila)],usuario:str) -> dict:
    sitio_atras = historiales[usuario][0].get()
    historiales[usuario][1].put(sitio_atras)
    return historiales[usuario][0].queue

def navegar_adelante(historiales: dict[str,(Pila,Pila)], usuario : str) -> dict:
    sitio_adelante = historiales[usuario][1].get()
    historiales[usuario][0].put(sitio_adelante)
    return historiales[usuario][0].queue

# visitar_sitio(historiales,'martin','netflix.com')
# # print(historiales)
# visitar_sitio(historiales,'martin','apple.com')
# print(navegar_atras(historiales, 'martin'))
# visitar_sitio(historiales, 'martin','youtube.com')
# print(navegar_adelante(historiales,'martin'))

# 23
inventario = {}
def agregar_producto(inventario: dict, nombre:str, precio:float, cantidad: int) -> dict:
    inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
    return inventario

def actualizar_stock(inventario, nombre, cantidad) -> dict:
    inventario[nombre]['cantidad'] = cantidad
    return inventario

def actualizar_precios(inventario,nombre,precio) -> dict:
    inventario[nombre]['precio'] = precio
    return inventario

def calcular_valor_inventario(inventario) -> float:
    total = 0
    for producto in inventario:
        total += inventario[producto]['precio'] * inventario[producto]['cantidad']
    return total



agregar_producto(inventario, 'remera', 20.0, 50)
agregar_producto(inventario, 'camisa', 30.0, 30)
print(actualizar_stock(inventario,'remera',10))
# actualizar_precios(inventario,'remera',120)
print(calcular_valor_inventario(inventario))
