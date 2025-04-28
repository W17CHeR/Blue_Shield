# -------------------------------------------------------
# Bienvenido al programa del antirootkit RKHunter
# -------------------------------------------------------

import os
import subprocess
import shutil

def mostrar_menu():
    while True:
        print("=" * 70)
        print("        Análisis de Rootkits - Rkhunter - Blue_Shield".center(70))
        print("=" * 70)
        print("1. Analizar el sistema (rkhunter --check)")
        print("2. Análisis rápido y silencioso (rkhunter -c -sk)")
        print("3. Volver al menú principal de Blue_Shield.py")
        print("q. Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            verificar_rkhunter()
            ejecutar_rkhunter_check()
        elif opcion == "2":
            verificar_rkhunter()
            ejecutar_rkhunter_silencioso()
        elif opcion == "3":
            regresar_a_blue_shield()
        elif opcion.lower() == "q":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def verificar_rkhunter():
    """Verifica si rkhunter está instalado. Si no, ofrece instalarlo."""
    if shutil.which("rkhunter") is None:
        print("⚠️ Rkhunter no está instalado en el sistema.")
        instalar = input("¿Deseas instalar Rkhunter ahora? (s/n): ").strip().lower()
        if instalar == "s":
            try:
                print("🚀 Instalando Rkhunter...")
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "rkhunter"], check=True)
                print("✅ Rkhunter instalado correctamente.")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error al intentar instalar Rkhunter: {e}")
                exit(1)
        else:
            print("❌ No se puede continuar sin Rkhunter. Saliendo...")
            exit(1)

def solicitar_ruta_log():
    """Pregunta si se desea guardar log, y solicita la ruta si es afirmativo."""
    desea_log = input("¿Deseas guardar el resultado en un log? (s/n): ").strip().lower()
    if desea_log == "s":
        ruta = input("Introduce la ruta donde deseas guardar el log (ej: /home/usuario/MisLogs/): ").strip()
        if not os.path.exists(ruta):
            print(f"⚠️ La ruta {ruta} no existe. Creándola...")
            os.makedirs(ruta)
        return os.path.join(ruta, "rkhunter_log.txt")
    else:
        return None

def ejecutar_rkhunter_check():
    print("\n🚀 Ejecutando análisis completo con Rkhunter...\n")
    try:
        ruta_log = solicitar_ruta_log()
        if ruta_log:
            comando = f"sudo rkhunter --check --logfile {ruta_log}"
        else:
            comando = "sudo rkhunter --check"
        subprocess.run(comando, shell=True, check=True)
        if ruta_log:
            print(f"✅ Análisis completo realizado. Log guardado en {ruta_log}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ocurrió un error al ejecutar Rkhunter: {e}")

def ejecutar_rkhunter_silencioso():
    print("\n🚀 Ejecutando análisis rápido/silencioso con Rkhunter...\n")
    try:
        ruta_log = solicitar_ruta_log()
        if ruta_log:
            comando = f"sudo bash -c 'rkhunter -c -sk --logfile {ruta_log}'"
        else:
            comando = "sudo rkhunter -c -sk"
        subprocess.run(comando, shell=True, check=True)
        if ruta_log:
            print(f"✅ Análisis silencioso realizado. Log guardado en {ruta_log}")
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
