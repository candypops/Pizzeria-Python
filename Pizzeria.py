## DICCIONARIOS DE DATOS GLOBALES CON LOS PRECIOS Y NOMBRES DE LOS INGREDIENTES
ingredientes = {'ja': 40, 'ch': 35, 'pi': 30, 'dq': 40, 'ac': 57.5, 'pp': 38.5, 'sa': 62.5}
ingNombre = {'ja': 'Jamón', 'ch': 'Champiñones', 'pi': 'Pimentón', 'dq': 'Doble Queso', 'ac': 'Aceitunas',
             'pp': 'Pepperoni', 'sa': 'Salchichón'}
tamano_precio = {'Grande': 580, 'Mediana': 430, 'Personal': 280}

## VARIABLES GOBLALES
precio_total = 0
n_pizzas = 0


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
def tamanos(opcion):
    print("Opciones: ")
    opcion = input("Tamaños:  Grande ( g )  Mediana ( m )  Personal ( p ): ")
    if opcion not in ['g', 'm', 'p']:
        print("=>Debe seleccionar el tamaño correcto!!")
        tamanos(opcion)
    else:
        if opcion == 'g':
            opcion = "Grande"
        elif opcion == 'm':
            opcion = "Mediana"
        else:
            opcion = "Personal"
        print("Tamaño seleccionado: ", opcion)
        return opcion


## FUNCION PARA DAR RESULTADOS DE LAS PIZZAS
## PARAMETROS: TAMANO DE LA PIZZA, INGREDIENTES, PRECIO DE LA PIZZA, NUMERO DE PIZZA Y MONTO TOTAL
## RETURN: RESPUESTA DE SI COMPRAR OTRA PIZZA O NO
def pedido(opcion_tamano, opcion_ingrediente, precio_pizza, n, total):
    string_opcion_ingrediente = ""
    for i in opcion_ingrediente:
        string_opcion_ingrediente += " %s," % (getNombre(i))
    strip_opcion_ingrediente = string_opcion_ingrediente.rstrip(',')
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
            print("\n\nGracias por su compra, regrese pronto")
            return respuesta


def main():
    mensaje_inicial()
    n_pizzas = 0
    precio_total = 0
    respuesta = ''
    while respuesta != 'n':
        precio_ingrediente = 0
        n_pizzas += 1
        print("Pizza número {} \n".format(n_pizzas))

        opcion_tamano = tamanos("a")
        precio_tamano = getPrecioTamano(opcion_tamano)

        opcion_ingrediente = llenarPizza()
        for i in opcion_ingrediente:
            precio_ingrediente += float(getPrecio(i))

        precio_pizza = precio_tamano + precio_ingrediente

        precio_total += precio_pizza

        respuesta = pedido(opcion_tamano, opcion_ingrediente, precio_pizza, n_pizzas, precio_total)


if __name__ == "__main__":
    main()
