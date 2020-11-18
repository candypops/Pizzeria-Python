# Pizzeria-Python

### Proyecto 1 de Electiva Programación en Python. Elaborado por el Grupo 3 

### Prerequisitos
* Python 3 o versiones mayores.
* Linea de comandos
### Instrucciones para su uso

* Descargue el archivo _Pizzeria.py_
* Desde la linea de comando, dirigirse a la ubicación del archivo .py
* Ejecute el archivo _Pizzeria.py_ de la siguiente manera
```js
python3 Pizzeria.py
```
### Funciones adicionales

* Combos en pedidos: Se puede elegir entre pedir pizza en combo o armar tu propia pizza.
Combos disponibles:
```
Pizza Margarita Grande + 2 Refrescos de 2lts + Dulce          (c1)
Pizza Cuatro Quesos Grande + 1 Refreco de 2lts                (c2)
Pizza Cuatro Estaciones Medina + 1 Refreco de 1.5lts + Dulce  (c3)
Pizza Primavera Grande + Extra de Queso + 2 Refrescos de 2lts (c4)
Pizza Pepperoni Personal + 1 Refreco de 1.5lts + Dulce        (c5)
Pizza Vegetariana Mediana + Dulce                             (c6)
Pizza Caprese Grande + 1 Refreco de 1.5lts + Dulce            (c7)
```
* Poder usar códigos promocionales: El usuario al final de su compra podra introducir o no un código de descuento.
```
¿Desea usar un código de promoción[s/n]?s
Ingrese el codigo de descuento en mayúsculas: DELIFREE
¡Felicitaciones! su código es correcto, descuento de:  3.0
```
Existen 3 códigos posibles:
1. DELIFREE -- Delivery grátis (-3 al total)
2. HALFFREE -- Descuento del 50% del total
3. PREMIUMFRIEND -- Descuento del 80%

* Opción de delivery: El usuario podra optar por pedir el envio de las pizzas indicando la direccion y numero telefonico.
```
Desea delivery? (Costo de 3) [s/n]: s

Introduzca la direccion de envio: Municipio Libertador, Parroquia San bernardino, AV Jose Felix Ribas, Conjunto residencial terepaima
Introduzca su numero telefonico: 04241037898

El pedido tiene un total de 1 pizza(s) por un monto de 345.5.
El envio se realizara a la direccion Municipio Libertador, Parroquia San bernardino, AV Jose Felix Ribas, Conjunto residencial terepaima, asociado al numero telefonico 04241037898.
```
