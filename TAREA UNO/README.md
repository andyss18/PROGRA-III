# PROGRA-III
# TAREA 1


Estructura           | Tiempo Promedio  | Memoria aproximada usada | Complejidad teórica
----------------------------------------------------------------------------------------------------
Arreglo Ordenado     | 0.00174 ms       | BAJA                     | O(log n)
Tabla Hash           | 0.000183 ms      | ALTA                     | o(1)


Conclusion: 

utilizamos la funcion perf_counter() para medir los tiempos promedios de busqueda y podemos ver una diferencia
siempre es la tabla hash la manera mas eficiente de organizar los datos ya que en la notacion Big(o) tiene una clase 
de complejidad de o(1).

Con el arreglo ordenado realiza una busqueda binaria con complejidad en notacion Big(o) de O(LOG N)

en este caso son 10,000,000 numeros por lo que con la funcion Hash se podrá encontrar resultados mas eficientes que con 
arreglos ordenados.

Se usa mas ram en uno que en otro pero la eficiencia aumenta de la mano con el consumo.
