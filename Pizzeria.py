## DICCIONARIOS DE DATOS GLOBALES CON TAMAÑOS DE PIZZAS, COMBOS Y PRECIOS, LOS PRECIOS Y NOMBRES DE LOS INGREDIENTES, DESCUENTOS
ingredientes = {'ja': 40, 'ch': 35, 'pi': 30, 'dq': 40, 'ac': 57.5, 'pp': 38.5, 'sa': 62.5}
ingNombre = {'ja': 'Jamón', 'ch': 'Champiñones', 'pi': 'Pimentón', 'dq': 'Doble Queso', 'ac': 'Aceitunas',
             'pp': 'Pepperoni', 'sa': 'Salchichón'}
tamano_precio = {'Grande': 580, 'Mediana': 430, 'Personal': 280}
tamanos = {'g': 'Grande', 'm': 'Mediana', 'p': 'Personal'}
combos_precios = {'c1': 685, 'c2': 650, 'c3': 539, 'c4': 988, 'c5': 305, 'c6': 469, 'c7': 610}
combos = {'c1': 'Pizza Margarita Grande + 2 Refrescos de 2lts + Dulce         ',
          'c2': 'Pizza Cuatro Quesos Grande + 1 Refreco de 2lts               ',
          'c3': 'Pizza Cuatro Estaciones Medina + 1 Refreco de 1.5lts + Dulce ',
          'c4': 'Pizza Primavera Grande + Extra de Queso + 2 Refrescos de 2lts',
          'c5': 'Pizza Pepperoni Personal + 1 Refreco de 1.5lts + Dulce       ',
          'c6': 'Pizza Vegetariana Mediana + Dulce                            ',
          'c7': 'Pizza Caprese Grande + 1 Refreco de 1.5lts + Dulce           '}
codigos = {'DELIFREE': 3, 'HALFFREE': 0.50, 'PREMIUMFRIEND': 0.80}

## VARIABLES GOBLALES
precio_total = 0
n_pizzas = 0


## FUNCION PARA APLICAR CODIGO DE DESCUENTOS
## PARAMETROS: TOTAL
## RETURN: PRECIO CON DESCUENTO
def setDescuento(total: float):
    descuento = input('Ingrese el codigo de descuento en mayúsculas: ')
    tot = 0
    if descuento in codigos:
        per = float(codigos.get(descuento))
        if descuento == 'DELIFREE':
            total -= per
            print('¡Felicitaciones! su código es correcto, descuento de: ', str(per))
        else:
            total -= total * per
            print('¡Felicitaciones! su código es correcto, descuento de: %s %%' % (str(per * 100)))
        return total
    else:
        r = input('Código erroneo, desea intentar nuevamente [s/n]: ')
        if r == 's':
            setDescuento(total)
        else:
            return tot


## FUNCION QUE DEVUELVE EL PRECIO DE UN INGREDIENTE
## PARAMETROS: INGREDIENTE ABREVIADO
## RETURN: PRECIO DEL INGREDIENTE
def getPrecio(ing: str):
    return ingredientes.get(ing)


## FUNCION QUE DEVUELVE EL NOMBRE DE LOS INGREDIENTES SEGUN SE ABREVIADO
## PARAMETROS: INGREDIENTE ABREVIADO
## RETURN: NOMBRE DEL INGREDIENTE
def getNombre(ing: str):
    return ingNombre.get(ing)


## FUNCION QUE DEVUELVE EL PRECIO DEL TAMANO DE LA PIZZA
## PARAMETROS: TAMANO DE LA PIZZA
## RETURN: PRECIO DEL TAMANO DE LA PIZZA
def getPrecioTamano(ing: str):
    return tamano_precio.get(ing)


## FUNCION PARA AGREGAR INGREDIENTES A UNA PIZZA
## PARAMETROS: NINGUNO
## RETURN: INGREDIENTES DE LA PIZZA (AGREGADOS)
def llenarPizza():
    print('\nIngredientes:')
    liValue = ingNombre.values()
    liKey = ingNombre.keys()
    agregados = []
    agregados.clear()
    for i in zip(liKey, liValue):
        print(format(i[1], '15s'), end=' ')
        print('('.format(i[0]) + i[0] + ')')
    print('\n')
    while True:
        respuesta = input('Indique ingrediente (enter para terminar): ')
        if respuesta == '':
            break
        elif respuesta in liKey:
            agregados.append(respuesta)
        else:
            print('Ingrediente no disponible en la lista')
            continue

    return agregados


## FUNCION QUE MUESTRA EL MENSAJE INICIAL DE LA APLICACION
## PARAMETROS: NINGUNO
## RETURN: NINGUNO
def mensaje_inicial():
    print("************************")
    print("*     PIZZERIA UCAB    *")
    print("************************")


## FUNCION PARA SELECCIONAR EL TAMAÑO DE LA PIZZA
## PARAMETROS: OPCION 
## RETURN: OPCION
def elegir_tamano(opcion):
    print("\nOpciones: ")
    opcion = input("Tamaños:  Grande ( g )  Mediana ( m )  Personal ( p ): ")
    if opcion not in ['g', 'm', 'p']:
        print("=>Debe seleccionar el tamaño correcto!!")
        tamanos(opcion)
    else:
        opcion = tamanos.get(opcion)
        print("Tamaño seleccionado: ", opcion)
        return opcion


## FUNCION PARA SELECCIONAR EL COMBO A COMPRAR
## PARAMETROS: NUMERO DE PIZZAS YA ORDENADAS (n), TOTAL DE LA COMPRA (total)
## RETURN: RESPUESTA SI DESEA SEGUIR ORDENANDO (respuesta), TOTAL DE LA COMPRA (total)
def menu_combos(n, total):
    print("\nCombos disponibles")
    combo_value = combos.values()
    combo_key = combos.keys()

    for i in zip(combo_key, combo_value):
        print(format(i[1], '15s'), end=' ')
        print('('.format(i[0]) + i[0] + ')')

    opcion = input("Indique el combo: ")

    if opcion not in combo_key:
        print("=>Debe seleccionar un combo!!")
        menu_combos(n, total)

    print("****************************")
    respuesta = input("¿Desea continuar [s/n]?: ")
    print("****************************")

    precio_combo = combos_precios.get(opcion)
    total += precio_combo

    while True:
        if respuesta == 's':
            print("Subtotal por el combo: ", precio_combo)
            print("Subtotal de toda su orden ({} pizzas): {}".format(n_pizzas + 1, total))
            print("****************************\n")
            return respuesta, total
        elif respuesta == 'n':
            print("El pedido tiene un total de %s pizza(s) por un monto de %s" % (n, total), end='.')
            print('\n')
            res = input('¿Desea usar un código de promoción[s/n]?')
            if res == 's':
                descuento = setDescuento(total)
                print("El pedido con descuento tiene un total de %s pizza(s) por un monto de %s" % (n, descuento),
                      end='.')
                print("\n\nGracias por su compra, regrese pronto")
                return respuesta, total
            elif res == 'n':
                print("\n\nGracias por su compra, regrese pronto")
                return respuesta, total


## FUNCION PARA DAR RESULTADOS DE LAS PIZZAS
## PARAMETROS: TAMANO DE LA PIZZA, INGREDIENTES, PRECIO DE LA PIZZA, NUMERO DE PIZZA Y MONTO TOTAL
## RETURN: RESPUESTA DE SI COMPRAR OTRA PIZZA O NO
def pedido(opcion_tamano, opcion_ingrediente, precio_pizza, n, total):
    string_opcion_ingrediente = ""
    for i in opcion_ingrediente:
        string_opcion_ingrediente += " %s," % (getNombre(i))
    strip_opcion_ingrediente = string_opcion_ingrediente.rstrip(',')
    if strip_opcion_ingrediente == '':
        print("Usted eligio una pizza %s Margarita" % opcion_tamano)
    else:
        print("Usted selecciono una pizza %s con%s" % (opcion_tamano, strip_opcion_ingrediente), end='.')
    print('\n')
    print("Subtotal a pagar por una pizza %s: %s" % (opcion_tamano, precio_pizza))
    print("****************************")
    respuesta = input("¿Desea continuar [s/n]?: ")
    print("****************************")

    while True:
        if respuesta == 's':
            return respuesta
        elif respuesta == 'n':
            print("El pedido tiene un total de %s pizza(s) por un monto de %s" % (n, total), end='.')
            print('\n')
            res = input('¿Desea usar un código de promoción[s/n]?')
            if res == 's':
                descuento = setDescuento(total)
                print("El pedido con descuento tiene un total de %s pizza(s) por un monto de %s" % (n, descuento),
                      end='.')
                print("\n\nGracias por su compra, regrese pronto")
                return respuesta
            elif res == 'n':
                print("\n\nGracias por su compra, regrese pronto")
                return respuesta


def main():
    mensaje_inicial()
    n_pizzas = 0
    precio_total = 0
    respuesta = ''
    opcion_combo = ''
    while respuesta != 'n':
        precio_ingrediente = 0
        n_pizzas += 1
        print("Pizza número {} \n".format(n_pizzas))

        print("a) Combos ( c ) b) Personalizada ( p )")
        opcion_combo = input("Opcion: ")

        if opcion_combo == 'c':
            respuesta, precio_total = menu_combos(n_pizzas, precio_total)
        elif opcion_combo == 'p':
            opcion_tamano = elegir_tamano("a")
            precio_tamano = getPrecioTamano(opcion_tamano)
            opcion_ingrediente = llenarPizza()
            for i in opcion_ingrediente:
                precio_ingrediente += float(getPrecio(i))
            precio_pizza = precio_tamano + precio_ingrediente
            precio_total += precio_pizza
            respuesta = pedido(opcion_tamano, opcion_ingrediente, precio_pizza, n_pizzas, precio_total)
        else:
            print("Opción inexistente")
            n_pizzas -= 1


if __name__ == "__main__":
    main()
