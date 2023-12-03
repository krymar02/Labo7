#ejercicio 3 
"""El objetivo de este ejercicio es crear una herramienta que nos permita de manera
automatica monitorear el consumo de CPU y memoria de un proceso. Para ello, escriba
un script en Python que haga lo siguiente:
Recibe como parametro un ejecutable
Ejecuta el binario recibido
Periodicamente lee y registra en un archivo de log el consumo de CPU y de memoria.
Al finalizar el proceso grafica los valores sobre el tiempo utilizando matplotlib."""


#importacion de bibliotecas importantes para la ejecucion
import os
import sys
import time
import matplotlib.pyplot as plt

#definiciones importantes
def monitor_resource(executable_path):
    #variables vacias para guardar informacion 
    cpu_usage = []
    memory_usage = []
    
    #manejo de errores
    try:
        # Iniciar el proceso
        process = os.popen(executable_path)
        process_pid = process.pid
        
        #ciclo while para el consumo de cpu y mem
        while True:
            # Obtener el consumo de CPU y memoria
            cpu_percent = os.popen(f"ps -p {process_pid} -o %cpu | tail -n 1").readline().strip()
            memory_percent = os.popen(f"ps -p {process_pid} -o %mem | tail -n 1").readline().strip()
            
            # Registrar valores
            cpu_usage.append(float(cpu_percent))
            memory_usage.append(float(memory_percent))
            
            # Esperar 1 segundo antes de la siguiente lectura
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        # Graficar los resultados
        plt.plot(cpu_usage, label='CPU Usage')
        plt.plot(memory_usage, label='Memory Usage')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Usage (%)')
        plt.legend()
        plt.show()

#ejecucion del programa 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resource_monitor.py <executable_path>")
    else:
        executable_path = sys.argv[1]
        monitor_resource(executable_path)
