# ENTREGA CONVOCATORIA ENERO.

**Estudiante:** [TU NOMBRE COMPLETO]
**Correo electrónico:** [TU CORREO @ALUMNOS.UNIVERSIDAD.ES]
**Enlace al vídeo de demostración:** [PEGA AQUÍ EL ENLACE DE TU VÍDEO DE YOUTUBE/VIMEO]

---

## Requisitos mínimos:
* `cargar_fichero`: Implementada con limpieza de acentos, eliminación de números y gestión de excepciones.
* `contar_palabras`: Cálculo de palabras totales y vocabulario único mediante estructuras de conjuntos.
* `calcular_frecuencia`: Generación de diccionario de frecuencias palabra-aparición.
* `es_anagrama_recursivo`: Lógica recursiva para la comparación de cadenas letra a letra.
* `buscar_anagramas`: Rastreador de pares de anagramas evitando duplicados y ordenando tuplas alfabéticamente.
* `aplicar_cifrado`: Cifrado César circular con alfabeto de 27 caracteres (incluyendo la 'ñ').
* `ordenar_por_frecuencia`: Algoritmo de ordenación manual (Selección) de mayor a menor frecuencia.

## Requisitos opcionales:
* `contador_letras`: Conteo estadístico de cada letra del abecedario en el texto analizado.
* `analizar_longitudes`: Estadísticas de longitud promedio, máxima y detección de la palabra más larga.
* `aplicar_descifrado`: Descifrado basado en el análisis de frecuencia de la letra 'a'.
* `exportar_CSV`: Exportación de la tabla de frecuencias a un archivo `.csv` compatible con Excel.
* `Tests Extras`: Creación de pruebas unitarias adicionales en `tests/test_extra.py` para casos límite y circularidad.

## Requisitos opcionales propios:
* No se han añadido funciones adicionales fuera de las especificadas en el enunciado para asegurar la estabilidad de los requisitos solicitados.

---

## Comentarios adicionales sobre la práctica:
La práctica se ha desarrollado utilizando un enfoque modular. Se ha prestado especial atención a la función de limpieza de texto para asegurar que caracteres como la "ñ" y la "u" con diéresis se gestionen según las reglas del español. Para la ordenación, se optó por el algoritmo de Selección por su claridad y facilidad de implementación manual sin usar funciones prohibidas por el enunciado.

### Instrucciones de ejecución y pruebas:

Para ejecutar el proyecto, sitúese en la carpeta raíz y utilice los comandos según su sistema operativo:

#### En Windows (CMD / PowerShell):
* **Ejecutar Analizador:** `python demo_analizador.py ficheros/palabras.txt`
* **Ejecutar Tests Mínimos:** `python -m unittest tests/test_minimos.py`
* **Ejecutar Tests Extras:** `python -m unittest tests/test_extra.py`

#### En Linux / macOS:
* **Ejecutar Analizador:** `python3 demo_analizador.py ficheros/palabras.txt`
* **Ejecutar Tests Mínimos:** `python3 -m unittest tests/test_minimos.py`
* **Ejecutar Tests Extras:** `python3 -m unittest tests/test_extra.py`

---