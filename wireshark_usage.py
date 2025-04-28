# -------------------------------------------------------
# Bienvenido al programa de Wireshark en Blue_Shield
# -------------------------------------------------------

import os
import subprocess

def mostrar_menu():
    while True:
        print("=" * 60)
        print("           Análisis de Red - Wireshark".center(60))
        print("=" * 60)
        print("1. Ejecutar Wireshark")
        print("2. Volver al menú principal de Blue_Shield")
        print("q. Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            ejecutar_wireshark()
        elif opcion == "2":
            regresar_a_blue_shield()
        elif opcion.lower() == "q":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def ejecutar_wireshark():
    print("\n🚀 Iniciando Wireshark...\n")
    try:
        # Ejecuta Wireshark y espera a que se cierre
        subprocess.run(["wireshark"], check=True)
        print("\n🛬 Wireshark cerrado. Volviendo al menú principal...")
        regresar_a_blue_shield()
    except FileNotFoundError:
        print("❌ Error: Wireshark no está instalado o no se encuentra en el PATH.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar Wireshark: {e}")

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
# Este programa es parte de Blue_Shield, un conjunto de herramientas para la seguridad informática.
