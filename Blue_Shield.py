# -------------------------------------------------------
# Bienvenido al programa de Blue_Shield
# -------------------------------------------------------

import os
import subprocess

def mostrar_ascii_azul():
    ascii_art = r"""
            .                                   
                                 :--===.                                
                             .:--:    .=++=.                            
                     .::::-::.    :--=.   .=+**#*+=-                    
                    .:.      ..-----=-==+=:       *#                    
                    .:. :::::-------==+++++++*#%. *#                    
                    .:. :::---------==++++++***#. *#                    
                    .-. ::--------=-=++++******#. *#                    
                    .-: :---------==+++*******#%  #*                    
                     -: .------=====+******####@  %=                    
                     :-  =---====++++******#*##= :%.                    
                     .=. :--====++++***#*######  #%                     
                      ==  =====++++*****######% .%-                     
                      .=: .++++++****#######*@  %#                      
                       :+. .+++*****########%  %@                       
                        :+. .******#######%%  @%                        
                         .**  **#######%#%- .%@                         
                           #*.  ####%##%+  *%+                          
                            :##.  **%@:  +@%                            
                              .#%-     %%#                              
                                 ##%=%%=                                
                                 .:=%-..
    """
    print("\033[94m" + ascii_art + "\033[0m")  # 94 = azul claro ANSI

def mostrar_presentacion():
    print("="*75)
    print("     Bienvenido a Blue_Shield".center(75))
    print("="*75)
    print("Esta herramienta te mostrara en CLI una lista de programas de Python".center(50))
    print("="*75)
    print()

def mostrar_menu():
    scripts = {
        "1": ("Mostrar especificaciones del sistema", "./specs.py"),
        "2": ("Mostrar el uso de la red", "./network_usage.py"),
        "3": ("Antivirus Clamav", "./antivirus_usage.py"),
        "4": ("capturar y analizar el tráfico de red con Wireshark", "./wireshark_usage.py"),
    }

    while True:
        print("Menu de opciones:")
        for key, value in scripts.items():
            print(f"{key}. {value[0]}")

        opcion = input("Selecciona una opción (1-4) o 'q' para salir: ")
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
    mostrar_ascii_azul()
    mostrar_presentacion()
    mostrar_menu()
    print("Gracias por usar Blue_Shield. ¡Hasta luego!")

# -------------------------------------------------------
# Programa creado por Sergio (aka W17CHeR)
# -------------------------------------------------------
