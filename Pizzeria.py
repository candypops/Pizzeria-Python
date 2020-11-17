## DICCIONARIOS DE DATOS GLOBALES CON LOS PRECIOS Y NOMBRES DE LOS INGREDIENTES
ingredientes = {'ja': 40, 'ch': 35, 'pi': 30, 'dq': 40, 'ac': 57.5, 'pp': 38.5, 'sa': 62.5}
ingNombre = {'ja': 'Jamón', 'ch': 'Champiñones', 'pi': 'Pimentón', 'dq': 'Doble Queso', 'ac': 'Aceitunas', 'pp': 'Pepperoni', 'sa': 'Salchichón'}

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

## FUNCION PARA AGREGAR INGREDIENTES A UNA PIZZA
## PARAMETROS: NINGUNO
## RETURN: NINGUNO
def llenarPizza():
    print('Ingredientes:')
    liValue = ingNombre.values()
    liKey = ingNombre.keys()
    agregados = []
    agregados.clear()
    for i in zip(liKey, liValue):
        print(format(i[1],'15s'), end=' ')
        print('('.format(i[0])+i[0]+')')
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

## FUNCION QUE MUESTRA EL MENSAJE INICIAL DE LA APLICACION
## PARAMETROS: NINGUNO
## RETURN: NINGUNO
def mensaje_inicial():
    print ("************************")
    print ("*     PIZZERIA UCAB    *")
    print ("************************")

## FUNCION PARA SELECCIONAR EL TAMAÑO DE LA PIZZA
## PARAMETROS: OPCION 
## RETURN: NINGUNO
def tamanos(opcion):
    print("Opciones: ")
    opcion = input("Tamaños:  Grande ( g )  Mediana ( m )  Personal ( p ): ")
    if opcion not in ['g', 'm', 'p'] :
        print("=>Debe seleccionar el tamaño correcto!!")
        tamanos(opcion) 
    else: 
        if opcion == 'g': opcion = "Grande"
        elif opcion == 'm': opcion = "Mediana"
        else: opcion = "Personal"
        print("Tamaño seleccionado: ", opcion)

def main():
    mensaje_inicial()
    n_pizzas = 1
    print("Pizza número {} \n".format(n_pizzas))
    tamanos("a")
    llenarPizza()
    
if __name__ == "__main__":
    main()