import sys
import analizador


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 demo_analizador.py <text_file>")
        return

    archivo = sys.argv[1]
    print(f"--- Analizando: {archivo} ---")

    # 1. Carga
    palabras = analizador.cargar_fichero(archivo)

    # 2. Estadísticas básicas
    total, unicas = analizador.contar_palabras(palabras)
    print(f"Total palabras: {total}, Únicas: {unicas}")

    # 3. Frecuencias y ordenación
    frec = analizador.calcular_frecuencia(palabras)
    ordenadas = analizador.ordenar_por_frecuencia(frec)
    print(f"Top 3 más frecuentes: {ordenadas[:3]}")

    # 4. Anagramas
    ana = analizador.buscar_anagramas(palabras)
    print(f"Anagramas encontrados: {ana}")

    # 5. Cifrado
    cifradas = analizador.aplicar_cifrado(palabras[:5], 3)
    print(f"Primeras 5 cifradas (+3): {cifradas}")

    # 6. Opcionales (ejemplo rápido)
    stats = analizador.analizar_longitudes(palabras)
    print(f"Palabra más larga: {stats['mas_larga']} ({stats['max_longitud']} letras)")

    # Exportar
    analizador.exportar_CSV(ordenadas, "frecuencias.csv")
    print("Fichero frecuencias.csv generado con éxito.")


if __name__ == "__main__":
    main()