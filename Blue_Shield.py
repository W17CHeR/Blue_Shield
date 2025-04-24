# --------------------------------------------------------------------
#                    Bienvenido a Py_Script
# --------------------------------------------------------------------
# Esta herramienta te mostrará en CLI una lista de programas de Python
# que puedes usar para hacer diferentes tareas.
# --------------------------------------------------------------------

import os

def mostrar_presentacion():
    print("=" * 75)
    print("     Bienvenido a Py_Script".center(75))
    print("=" * 75)
    print("Esta herramienta te mostrará en CLI una lista de programas de Python".center(75))
    print("=" * 75)
    print()

def mostrar_menu():
    scripts = {
        "1": ("Mostrar especificaciones del sistema", "./specs.py"),
        "2": ("Mostrar el uso de la red", "./network_usage.py"),
        "3": ("Antivirus Clamav", "./antivirus_usage.py"),
        # Se agregara más funciones en el futuro
    }

    while True:
        print("\nMenu de opciones:")
        for key, value in scripts.items():
            print(f"{key}. {value[0]}")

        opcion = input("Selecciona una opción (1-3) o 'q' para salir: ").strip()

        if opcion.lower() == 'q':
            print("Saliendo del programa...")
            break
        elif opcion in scripts:
            script_path = scripts[opcion][1]
            if os.path.exists(script_path):
                try:
                    # ⚠️ Esta línea reemplaza el proceso actual
                    os.execlp("python", "python", script_path)
                except Exception as e:
                    print(f"Error al ejecutar el script: {e}")
                    break
            else:
                print(f"El script '{script_path}' no existe.")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_presentacion()
    mostrar_menu()
    print("Gracias por usar Py_Script. ¡Hasta luego!")

# -------------------------------------------------------
# Programa creado por Sergio (aka W17CHeR)
# -------------------------------------------------------
