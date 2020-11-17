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
    
if __name__ == "__main__":
    main()