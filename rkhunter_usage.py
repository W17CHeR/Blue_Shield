# -------------------------------------------------------
# Bienvenido al programa del antirootkit RKHunter
# -------------------------------------------------------

import os
import subprocess

def mostrar_menu():
    while True:
        print("=" * 70)
        print("        Análisis de Rootkits - Rkhunter - Blue_Shield".center(70))
        print("=" * 70)
        print("1. Analizar el sistema (rkhunter --check)")
        print("2. Análisis rápido y silencioso (rkhunter -c -sk)")
        print("3. Volver al menú principal de Blue_Shield")
        print("q. Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            ejecutar_rkhunter_check()
        elif opcion == "2":
            ejecutar_rkhunter_silencioso()
        elif opcion == "3":
            regresar_a_blue_shield()
        elif opcion.lower() == "q":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def ejecutar_rkhunter_check():
    print("\n🚀 Ejecutando análisis completo con Rkhunter...\n")
    try:
        comando = "sudo rkhunter --check --logfile ~/Desktop/Rkhunter_analisis_sistema.txt"
        subprocess.run(comando, shell=True, check=True)
        print("✅ Análisis completo realizado. Log guardado en ~/Desktop/Rkhunter_analisis_sistema.txt")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ocurrió un error al ejecutar Rkhunter: {e}")

def ejecutar_rkhunter_silencioso():
    print("\n🚀 Ejecutando análisis rápido/silencioso con Rkhunter...\n")
    try:
        comando = "sudo rkhunter -c -sk --logfile ~/Desktop/informe_antirootkit-$(date +%Y-%m-%d).log"
        subprocess.run(comando, shell=True, check=True)
        print("✅ Análisis silencioso realizado. Log guardado en ~/Desktop con fecha incluida.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ocurrió un error al ejecutar Rkhunter: {e}")

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
