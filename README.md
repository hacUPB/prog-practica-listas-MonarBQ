[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/oCjy4n5N)
# Ejercicios de Programación en Python

## Descripción
Este repositorio contiene una serie de ejercicios que debes completar utilizando los conceptos de **funciones**, **matrices (listas de listas)**, **condicionales**, y **bucles** en Python. Cada ejercicio tiene una función correspondiente que debes implementar en el archivo `ejercicios.py`.

Además, hemos configurado un sistema de pruebas automáticas usando **Pytest** que evaluará tu código una vez que completes los ejercicios. No es necesario que modifiques los archivos de prueba. Solo debes concentrarte en implementar correctamente las funciones dentro de `ejercicios.py`.

## Cómo trabajar en este repositorio
1. Clona este repositorio en tu máquina local.
2. Abre el archivo `ejercicios.py` y completa las funciones que están marcadas con `pass`.
3. Cada función tiene un enunciado correspondiente en este archivo README para guiarte.
4. No modifiques el archivo de pruebas `test_ejercicios.py`.
5. Asegúrate de que tu código pase las pruebas automáticas antes de enviar el repositorio.

## Ejercicios

### 1. `suma_matriz(matriz)`
Escribe una función que reciba una lista de listas (matriz) y devuelva la **suma** de todos los elementos.
- **Entrada**: `[[1, 2], [3, 4]]`
- **Salida esperada**: `10`

### 2. `maximo_matriz(matriz)`
Escribe una función que reciba una lista de listas (matriz) y devuelva el **valor máximo** encontrado.
- **Entrada**: `[[1, 2], [3, 4]]`
- **Salida esperada**: `4`

### 3. `es_primo(n)`
Escribe una función que determine si un número es **primo** o no.
- **Entrada**: `7`
- **Salida esperada**: `True`
  
- **Entrada**: `4`
- **Salida esperada**: `False`

### 4. `transponer_matriz(matriz)`
Escribe una función que devuelva la **matriz transpuesta** de una lista de listas.
- **Entrada**: `[[1, 2], [3, 4]]`
- **Salida esperada**: `[[1, 3], [2, 4]]`

### 5. `filtrar_pares(lista)`
Escribe una función que reciba una lista de números y devuelva una nueva lista con solo los **números pares**.
- **Entrada**: `[1, 2, 3, 4]`
- **Salida esperada**: `[2, 4]`

### 6. `contar_palabras(frase)`
Escribe una función que reciba una cadena de texto y cuente la **cantidad de palabras** que contiene.
- **Entrada**: `"Hola Mundo"`
- **Salida esperada**: `2`

### 7. `tabla_multiplicar(n)`
Escribe una función que reciba un número y devuelva una **lista con su tabla de multiplicar** del 1 al 10.
- **Entrada**: `2`
- **Salida esperada**: `[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]`

### 8. `contar_negativos(lista)`
Escribe una función que reciba una lista de números y cuente cuántos son **negativos**.
- **Entrada**: `[-1, 0, 1, 2, -3]`
- **Salida esperada**: `2`

### 9. `lista_ordenada(lista)`
Escribe una función que verifique si una lista está **ordenada** de menor a mayor.
- **Entrada**: `[1, 2, 3, 4]`
- **Salida esperada**: `True`
  
- **Entrada**: `[1, 3, 2, 4]`
- **Salida esperada**: `False`

### 10. `cifrado_cesar(texto, desplazamiento)`
Escribe una función que aplique el **cifrado César** a un string con el desplazamiento dado.
- **Entrada**: `"abc", 1`
- **Salida esperada**: `"bcd"`

## Ejecución de pruebas locales
Puedes ejecutar las pruebas localmente para verificar si tu implementación es correcta. Para ello, sigue estos pasos:

1. Asegúrate de tener **pytest** instalado. Si no lo tienes, instálalo con:
    ```bash
    pip install pytest
    ```

2. Ejecuta las pruebas:
    ```bash
    pytest
    ```

Si todas las pruebas pasan, tu solución es correcta.

## Envío del proyecto
1. Una vez que hayas completado todos los ejercicios y hayas verificado que las pruebas pasan correctamente, realiza un commit de tus cambios:
    ```bash
    git add .
    git commit -m "Solución de ejercicios completada"
    ```

2. Sube tus cambios al repositorio:
    ```bash
    git push
    ```

## Notas adicionales
- No modifiques los archivos de prueba en la carpeta `/tests/`.
- Intenta realizar las soluciones sin utilizar bibliotecas externas, solo con lo visto en clase.
- Si tienes dudas, revisa la documentación de Python o consulta al profesor.

¡Buena suerte y que disfrutes resolviendo los ejercicios!
