# -------------------------------------------------------
# Bienvenido al programa de specs.py
# -------------------------------------------------------
import subprocess
import os

def mostrar_presentacion():
    print("="*75)
    print("     Bienvenido a Specs".center(75))
    print("="*75)
    print("Esta herramienta te mostrará en CLI las especificaciones de tu equipo".center(75))
    print("="*75)
    print()

def ejecutar_fastfetch():
    print("\nEjecutando Fastfetch...\n")
    try:
        subprocess.run(["fastfetch"], check=True)
    except FileNotFoundError:
        print("Error: 'fastfetch' no está instalado o no se encuentra en el PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error al ejecutar fastfetch: {e}")

def menu_post_ejecucion():
    while True:
        print("\n¿Qué deseas hacer ahora?")
        print("1. Volver al menú principal de Blue_Shield")
        print("q. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            # ✅ Reemplaza el proceso actual con Blue_Shield.py
            os.execlp("python", "python", "Blue_Shield.py")
        elif opcion.lower() == "q":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar especificaciones del sistema (fastfetch)")
        print("q. Salir")

        opcion = input("Selecciona una opción: ").strip()
        if opcion == 'q':
            print("Saliendo del programa...")
            break
        elif opcion == "1":
            ejecutar_fastfetch()
            menu_post_ejecucion()
            break  # Salimos del menú después de regresar o salir
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_presentacion()
    mostrar_menu()
    print("Gracias por usar Specs. ¡Hasta luego!")

# -------------------------------------------------------
# Programa creado por Sergio (aka W17CHeR)
# -------------------------------------------------------
