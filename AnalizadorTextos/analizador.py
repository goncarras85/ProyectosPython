import sys


def cargar_fichero(ruta_archivo: str) -> list[str]:
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:
        # El enunciado pide este mensaje específico en caso de error
        print("Usage: python3 demo_analizador.py text_file")
        sys.exit(1)

    # Limpieza de acentos y diéresis
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    for con, sin in reemplazos.items():
        contenido = contenido.replace(con, sin)
        contenido = contenido.replace(con.upper(), sin)

    # Reemplazar guiones por espacios y quitar signos
    contenido = contenido.replace('-', ' ')
    signos = ".,;:¿?¡!()\"\'"
    for s in signos:
        contenido = contenido.replace(s, "")

    # Dividir y limpiar palabras con números
    lista_previa = contenido.lower().split()
    palabras_limpias = []

    for p in lista_previa:
        # Comprobar si tiene números
        tiene_num = False
        for char in p:
            if char.isdigit():
                tiene_num = True
                break
        if not tiene_num and p != "":
            palabras_limpias.append(p)

    return palabras_limpias


def contar_palabras(palabras: list[str]) -> tuple:
    return (len(palabras), len(set(palabras)))


def calcular_frecuencia(palabras: list[str]) -> dict:
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
    return frecuencias


def es_anagrama_recursivo(palabra1: str, palabra2: str) -> bool:
    # 1. Comprobar longitud
    if len(palabra1) != len(palabra2):
        return False
    # 2. Caso base: longitud 1
    if len(palabra1) == 1:
        return palabra1 == palabra2
    # 3. Comprobar si letra está en palabra2
    letra = palabra1[0]
    if letra in palabra2:
        # 4. Recursividad quitando la letra común
        idx = palabra2.find(letra)
        nueva_p2 = palabra2[:idx] + palabra2[idx + 1:]
        return es_anagrama_recursivo(palabra1[1:], nueva_p2)
    return False


def buscar_anagramas(palabras: list[str]) -> list:
    v = list(set(palabras))
    resultado = []
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if es_anagrama_recursivo(v[i], v[j]):
                # Guardar tupla ordenada alfabéticamente
                par = tuple(sorted((v[i], v[j])))
                if par not in resultado:
                    resultado.append(par)
    return resultado


def aplicar_cifrado(palabras: list[str], desplazamiento: int) -> list[str]:
    abc = "abcdefghijklmnñopqrstuvwxyz"
    res = []
    # Fórmula: $nuevo\_idx = (idx + desp) \pmod{27}$
    for p in palabras:
        cifrada = ""
        for letra in p:
            if letra in abc:
                idx = abc.find(letra)
                cifrada += abc[(idx + desplazamiento) % 27]
            else:
                cifrada += letra
        res.append(cifrada)
    return res


def ordenar_por_frecuencia(diccionario_frecuencias: dict) -> list:
    items = list(diccionario_frecuencias.items())
    # Algoritmo de Selección (Selection Sort) manual
    for i in range(len(items)):
        max_idx = i
        for j in range(i + 1, len(items)):
            if items[j][1] > items[max_idx][1]:
                max_idx = j
        items[i], items[max_idx] = items[max_idx], items[i]
    return items


# --- OPCIONALES ---

def contador_letras(palabras: list) -> dict:
    abc = "abcdefghijklmnñopqrstuvwxyz"
    d = {l: 0 for l in abc}
    for p in palabras:
        for l in p:
            if l in d: d[l] += 1
    return d


def analizar_longitudes(palabras: list[str]) -> dict:
    if not palabras: return {'promedio': 0.0, 'max_longitud': 0, 'mas_larga': ""}
    mas_larga = ""
    for p in palabras:
        if len(p) >= len(mas_larga): mas_larga = p
    promedio = sum(len(p) for p in palabras) / len(palabras)
    return {'promedio': promedio, 'max_longitud': len(mas_larga), 'mas_larga': mas_larga}


def aplicar_descifrado(palabras_cifradas: list) -> tuple:
    letras = "".join(palabras_cifradas)
    if not letras: return (0, [])
    # Frecuencia de letras para adivinar la 'a'
    conteo = {}
    for l in letras: conteo[l] = conteo.get(l, 0) + 1

    # Letra más frecuente (primera alfabéticamente en empate)
    max_f = max(conteo.values())
    mas_comun = sorted([l for l, f in conteo.items() if f == max_f])[0]

    abc = "abcdefghijklmnñopqrstuvwxyz"
    desplazamiento = (abc.find(mas_comun) - abc.find('a')) % 27
    return (desplazamiento, aplicar_cifrado(palabras_cifradas, -desplazamiento))


def exportar_CSV(palabras_frecuencia: list, ruta_archivo: str) -> None:
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.write("Palabra,Frecuencia\n")
        for p, frec in palabras_frecuencia:
            f.write(f"{p},{frec}\n")