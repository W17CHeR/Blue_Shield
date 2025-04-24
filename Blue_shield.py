# -------------------------------------------------------
# Bienvenido al programa de especificaciones del sistema
# -------------------------------------------------------

import os
import subprocess

def mostrar_presentacion():
    print("="*75)
    print("     Bienvenido a Specs".center(75))
    print("="*75)
    print("Esta herramienta te mostrara en CLI las especificaciones de su equipo".center(50))
    print("="*75)
    print()

def mostrar_menu():
    scripts = {
        "1": ("Mostrar especificaciones del sistema", "./specs.py")
    }

    while True:
        print("Menu de opciones:")
        for key, value in scripts.items():
            print(f"{key}. {value[0]}")
        
        opcion = input("Selecciona la opción (1) o 'q' para salir: ")
        if opcion == 'q':
            print("Saliendo del programa...")
            break
        elif opcion in scripts:
            script_path = scripts[opcion][1]
            if os.path.exists(script_path):
                try:
                    subprocess.run(["python", script_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error al ejecutar el script: {e}")
            else:
                print(f"El script {script_path} no existe.")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_presentacion()
    mostrar_menu()
    print("Gracias por usar Specs. ¡Hasta luego!")

# -------------------------------------------------------
# Programa creado por Sergio (aka W17CHeR)
# -------------------------------------------------------
