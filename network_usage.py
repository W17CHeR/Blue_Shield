# -------------------------------------------------------
# Bienvenido al programa de especificaciones del sistema
# -------------------------------------------------------
import os
import subprocess

def mostrar_menu():
    while True:
        print("=" * 60)
        print("        Análisis de Red - Blue_Shield".center(60))
        print("=" * 60)
        print("1. Escanear red con Nmap")
        print("2. Analizar conexiones activas con Netstat")
        print("3. Volver al menú principal de Blue_Shield.py")
        print("q. Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            escanear_con_nmap()
        elif opcion == "2":
            analizar_con_netstat()
        elif opcion == "3":
            regresar_a_blue_shield()
        elif opcion.lower() == "q":
            print("Saliendo del análisis de red...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def escanear_con_nmap():
    objetivo = input("\nIntroduce la IP o rango a escanear (ej. 192.168.1.0/24): ").strip()
    print(f"\n🔍 Ejecutando escaneo Nmap en {objetivo}...\n")
    try:
        subprocess.run(["nmap", "-sP", objetivo], check=True)
    except FileNotFoundError:
        print("❌ Error: Nmap no está instalado o no se encuentra en el PATH.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ocurrió un error al ejecutar Nmap: {e}")

def analizar_con_netstat():
    print("\n🔍 Mostrando conexiones activas con Netstat...\n")
    try:
        subprocess.run(["netstat", "-tunap"], check=True)
    except FileNotFoundError:
        print("❌ Error: Netstat no está disponible en tu sistema.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ocurrió un error al ejecutar Netstat: {e}")

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
