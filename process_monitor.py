#ejercicio 2
""" El objetivo de este ejercicio es crear una herramienta que nos permita automatizar el monitoreo de un proceso, puesto que a pesar de que hay herramientas que nos
permiten observar el estado de un proceso en un momento determinado, es importante aprender como delegar tareas facilmente automatizables a otros procesos. Utilice el
módulo os para crear un script de Python que haga lo siguiente:
Recibir como parametro el nombre de un proceso y el comando para ejecutarlo.
Revise periodicamente el estado del proceso. Si el proceso cierra, debe volver a
levantarlo.
"""

#importacion de bibliotecas importantes para la ejecucion 
import os
import sys
import time

#definicion para el monitoreo del proceso
def monitor_process(process_name, command):
    try:
        while True:
            # Verifica si el proceso está en ejecución
            if not any(process_name in line for line in os.popen("ps aux").readlines()):
                # Si el proceso no está en ejecución, lo levanta
                os.system(command)
                print(f"Process '{process_name}' restarted.")
            time.sleep(10)  # Espera 10 segundos antes de revisar nuevamente
    
    #manejo de excepciones
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

#ejecuta el programa
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_monitor.py <process_name> <command>")
    else:
        process_name = sys.argv[1]
        command = sys.argv[2]
        monitor_process(process_name, command)
