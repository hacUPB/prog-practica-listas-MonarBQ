# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    suma_total = 0  #Empezamos en cero 
    for fila in matriz:
        for elemento in fila: #Para cada elemento de las filas en la matriz 
            suma_total += elemento #Se va sumando cada elemento al acumulador
    return suma_total
    pass

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    maximo = matriz[0][0] #Empezamos con el primer elemento de la matriz
    for fila in matriz:
        for elemento in fila: #Para cada elemento de las filas en la matriz
            if elemento > maximo: #Comparamos cada elemento 
                maximo = elemento
    return maximo

    pass

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    if n <= 1: #Descartamos los negativos y el 1
        resultado = False
    for i in range(2, int(n**0.5) + 1): #Buscamos divisores hasta la raiz cuadrada de n, el 1 es para que tambien tome el valor de la raiz 
        if n % i == 0: # si tiene divisores es falso
            resultado = False
    resultado = True
    return resultado
    pass

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_transpuesta = [] #Matriz vacia 
    for col in range(columnas): #Recorremos los elementos de cada columna 
        fila_transpuesta = []
        for fila in range(filas): #Convertimos los elementos de las columnas en filas 
            fila_transpuesta.append(matriz[fila][col])
        matriz_transpuesta.append(fila_transpuesta)
    
    return matriz_transpuesta
    pass

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    return [numero for numero in lista if numero % 2 == 0] #Evalua numero a numero de las lista y devuelve otra lista con los numero divisibles por dos 
    pass

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    palabras = frase.split() #Dividimos la cadena de texto en palabras cada que haya un espacio
    return len(palabras) #Devolvemos la cantidad de palabras 
    pass

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    tabl_de_mult =[]
    for i in range(1,11):
        tabl_de_mult.append(n * i)
    return tabl_de_mult
    pass

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    contador = 0  # Definimos el contador 

    for numero in lista: #Recorremos cada numero en la lista
        if numero < 0:
            contador += 1  # Si el número es negativo, aumentamos el contador

    return contador
    pass

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    for i in range(len(lista) - 1): #Recorro lo lista hasta el penultimo numero 
        if lista[i] > lista[i + 1]: #Comparo cada numero(i) con el que sigue(i+1) 
            return False  
    return True  
    pass

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    abecedario = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ'
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
    ]
    #Listamos el abecedario 
    texto_cifrado = "" #Declaramos el texto cifrado vacio 
    
    for letra in texto: # Recorremos cada letra en el texto 
        minuscula = letra.lower() #La ponemos minuscula para evaluarla en el abecedario
        if minuscula in abecedario: # Encontramos la posición actual en el abecedario
            posicion_actual = 0 #Se declara la posicion actual como cero
            for i in range(len(abecedario)): #Se recorre el abecedario letra a letra para comparalo con la letra del texto
                if abecedario[i] == minuscula:
                    posicion_actual = i #Se encuentra la posicion de la letra 
                    break
            
            # Calculamos la nueva posición
            nueva_posicion = (posicion_actual + desplazamiento) % 27 #se calcula la posicion como el residuo de la suma dividido la cantidad de caracteres del abecedario (27)
            nueva_letra = abecedario[nueva_posicion]
            
            if letra.isupper(): #Preguntamos si la letra era mayuscula o no con este metodo
                nueva_letra = nueva_letra.upper() #Si lo era mantenemos la mayuscula 
                
            texto_cifrado += nueva_letra #Vamos introducion cada letra al texto 
        else:
            texto_cifrado += letra # Si no es una letra (espacio, número, símbolo), lo dejamos igual
    
    return texto_cifrado

    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
   pass

if __name__ == "__main__":
    main()