# -------------------------------------------------------
# Bienvenido al programa de especificaciones del sistema
# -------------------------------------------------------

import os
import subprocess

def mostrar_menu():
    while True:
        print("=" * 60)
        print("        Análisis de Antivirus - ClamAV".center(60))
        print("=" * 60)
        print("1. Analizar la carpeta raíz de Linux (/)")
        print("2. Analizar el directorio Home (/home)")
        print("3. Volver al menú principal de Blue_Shield.py")
        print("q. Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            analizar_con_clamav("/")
        elif opcion == "2":
            analizar_con_clamav("/home")
        elif opcion == "3":
            regresar_a_blue_shield()
        elif opcion.lower() == "q":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def analizar_con_clamav(directorio):
    print(f"\n🔍 Iniciando análisis de ClamAV en el directorio: {directorio}...\n")
    try:
        subprocess.run(["clamscan", "-r", directorio], check=True)
    except FileNotFoundError:
        print("❌ Error: ClamAV no está instalado o no se encuentra en el PATH.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ocurrió un error al ejecutar ClamAV: {e}")

def regresar_a_blue_shield():
    print("\n🔙 Volviendo al menú principal de Blue_Shield.py...")
    try:
        os.execlp("python", "python", "Blue_Shield.py")
    except Exception as e:
        print(f"❌ Error al intentar regresar al menú principal: {e}")

if __name__ == "__main__":
    mostrar_menu()


# -------------------------------------------------------
# Programa creado por Sergio (aka W17CHeR)
# -------------------------------------------------------
