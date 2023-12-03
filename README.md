# Laboratorio 7 - Python Scripting

**Universidad de Costa Rica  
Curso: Principios de Informática  
Código del Curso: IE-0117 Programación Bajo Plataformas Abiertas  
Profesora: Carolina Trejos  
Fecha: 3 de diciembre de 2023  
Estudiante: Kryssia Martínez, Carne: B84636**

## Descripción

El presente laboratorio tiene como objetivo evaluar los conocimientos adquiridos en Python, convirtiendo el desarrollo previo en Bash scripting a Python scripting.

## Archivos

- `process_info.py`: Script que obtiene información relevante de un proceso.
- `process_monitor.py`: Script que automatiza el monitoreo de un proceso.
- `resource_monitor.py`: Script que monitorea el consumo de CPU y memoria de un proceso y grafica los resultados.

## Instrucciones de Instalación de Librerías
Para una correcta ejecucion se deben tener instaladas las librerias. 

Librerías antes de ejecutar los scripts. Puedes instalarlas utilizando el siguiente comando:

```bash
pip install psutil matplotlib

psutil: Librería para acceder a información sobre los procesos y el sistema.
matplotlib: Librería para la creación de gráficos y visualización de datos.

## Ejecución y resultados

### Ejercicio 1: Obtener Información de un Proceso

```bash
python process_info.py 5072
Nombre del proceso: code
ID del proceso: 5072
Parent process ID: 83148
Usuario propietario: kryssia martinez0
Porcentaje de uso de CPU: 14,42%
Consumo de memoria: 219 MB
Estado: Running
Path del ejecutable: C:\Windows\visual studio code\process_info.py

### Ejercicio 2: Monitorear un proceso

```bash
python process_monitor.py firefox "Brave"

Resultado:
Process 'Brave' restarted.
Process 'Brave' restarted.
Process 'Brave' restarted.
...
Monitoring stopped.

### Ejercicio 3: Monitorear consumo de CPU y Memoria
```bash
python resource_monitor.py "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

Resultados:
Graficando resultados...
(Se muestra una gráfica con el tiempo y el uso de CPU y memoria)


