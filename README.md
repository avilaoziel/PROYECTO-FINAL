REQUERIMIENTOS-CONTROL-DE-ASISTENCIAS-PARA-FABRICA
1-Interfaz grafica 
2-Importar hora tiempo para la interfaz 
3-Tener en cuenta vacaciones del Obrero
4-Tener datos basicos del Trabajador al momento de registar asitencia
5-Crear un folder donde se tenga registro de las asistencias 
6-Al momento de imprimir o mostar las asistencias, estas sean precisas u ordenadas 
7-Tener sanciones o avisos que queden registrados al momento de que alguien no se resgistre 
8-Tener bases de datos de trbajadores
9-Crear un comando que justifique faltas o anule el registro(Una clave o palabra especial)
10-Que la interfaz sea enendible y tenga botones para las tareas habladas con anterioridad
11-El folder donde se guardara las asistncias creado sera un archivo csv

Usar:
import datetime
hora_actual = datetime.datetime.now().strftime("%H:%M:%S") 
fecha_actual = datetime.date.today().strftime("%Y-%m-%d")
