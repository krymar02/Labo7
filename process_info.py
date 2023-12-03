#ejercicio 1 El objetivo de este ejercicio es repasar como obtener parte de la informacion
#mas relevante de un proceso. Utilice el módulo os para crear un script de Python que
#reciba como argumento un numero correspondiente al ID de un proceso y devuelva la
#siguiente informacion:
#a) Nombre del proceso
#b) ID del proceso
#c) Parent process ID
#d) Usuario propietario
#e) Porcentaje de uso de CPU al momento de correr el script
#f ) Consumo de memoria
#g) Estado (status)
#h) Path del ejecutable

#importar lo importante, las librerias
import os
import sys

#definicion para obtener el proceso.
def get_process_info(process_id):
    try:
        process_id = int(process_id)
        process_info = {}
        
        # Obtener información que se solicita del proceso
        # a) Nombre del proceso
        process_info['name'] = os.path.basename(open(f"/proc/{process_id}/comm").readline().strip())
        
        # b) ID del proceso
        process_info['pid'] = process_id
        
        # c) Parent process ID
        process_info['ppid'] = int(open(f"/proc/{process_id}/stat").readline().split()[3])
        
        # d) Usuario propietario
        process_info['user'] = os.stat(f"/proc/{process_id}").st_uid
        
        # e) Porcentaje de uso de CPU
        process_info['cpu_percent'] = os.popen(f"ps -p {process_id} -o %cpu | tail -n 1").readline().strip()
        
        # f) Consumo de memoria
        process_info['memory'] = os.popen(f"ps -p {process_id} -o %mem | tail -n 1").readline().strip()
        
        # g) Estado (status)
        process_info['status'] = open(f"/proc/{process_id}/status").readline().split()[1]
        
        # h) Path del ejecutable
        process_info['executable'] = os.readlink(f"/proc/{process_id}/exe")
        
        #se retorna lo necesario
        return process_info
    
    #manejo de errores
    except Exception as e:
        return f"Error: {e}"

#ejecucion del programa main
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_info.py <process_id>")
    else:
        process_id = sys.argv[1]
        result = get_process_info(process_id)
        print(result) #resultado000000
