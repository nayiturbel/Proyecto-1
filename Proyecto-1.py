# Proyecto Nayelly y Ricardo. Trivia de los temas vistos en clase

# Variables Globales

preguntas_juego = dict()
puntos_jugador = []
resultado_juego = dict(zip(list_jugadores,puntos_jugador))

# Seleccion de Jugador y su nombre
def jugadores():
	
	list_jugadores = []

    for i in range(int(input("Seleccione el numero de jugadores: "))):
        i = input("Ingrese nombre del jugador: ")
        list_jugadores.append(i)

    return list_jugadores

# Seleccion de nivel de dificultad del juego
def seleccion_dificultad():
    
    dificultad = (int(input("Seleccione la dificultad deseada 1, 2 o 3: ")))
    
    if dificultad == 1:
        preguntas_juego.update(preguntas_1)
    elif dificultad == 2:
        preguntas_juego.update(preguntas_2)
    elif dificultad == 3:
        preguntas_juego.update(preguntas_3)
    else:
        print('Nivel no identificado, vuelva a intentar')

# Reglas del Juego

# si la respuesta del usuario es igual al valor de la pregunta se suma un punto
# al jugador. 
# El jugador que al final tenga mas puntos gana. 
# si quedan empate se muestra mensaje de empate.
def reglas_de_juego():
# Se van imprimiendo las preguntas y se reciben las respuestas y se comparan contra las respuestas preestablecidas
# si la respuesta es correcta se tiene un 1, si es incorrecta o no se recibe un valor valido es 0

# Pasos a Seguir:
#1. seleccionar una pregunta random de nuestro diccionario de preguntas
#2. recibo el input de la respuesta por jugador
#3. checo si el input es correcto en el diccionario original
#4. guardo la pregunta en el listado de "ya no preguntar" -- Se 
#5. acumulo los puntos por cada uno de los jugadores
	preguntas = []
	respuestas = []

	for i in preguntas_juego:
	    preguntas.append(i)

	for i in preguntas:
	    pregunta_en_turno = i
	    print(pregunta_en_turno)
	    respuesta = input("Indique su respuesta: T o F ")
	    if respuesta == "T" or respuesta == "t":
	        respuesta = True
	        if preguntas_juego.get(i)==respuesta:
	            print("Respuesta Correcta")
	            respuestas.append(1)
	        else:
	            print("Respuesta incorrecta")
	            respuestas.append(0)
	            
	    elif respuesta == "F"or respuesta == "f":
	        respuesta = False
	        if preguntas_juego.get(i)==respuesta:
	            print("Respuesta Correcta")
	            respuestas.append(1)
	        else:
	            print("Respuesta incorrecta")
	            respuestas.append(0)
	    else:
	        print("Respuesta no recibida")
	        respuestas.append(0)

	puntos_fin_jugador = sum(respuestas)
    puntos_jugador.append(puntos_fin_jugador)

    print(dict(zip(list_jugadores,puntos_jugador)))

# Juego
# Se van mostrando pregunta por pregunta y se recibe la respuesta del jugador. T o F en mayusculas. la respuesta del jugador debe de ser convertida a mayusculas
def Juego():
	#1. llamar funcion de jugadores
	#2. llamar la funcion de dificultad
	#3. definir las variables de los puntos por jugador -> para acumular los puntos de los jugadores -> convertir en funcion.
	#4. while cantidad de preguntas de acuerdo a la dificultad y hacer la pregunta por cada jugador y llamar la funcion "reglas de juego".
	#   imprimir al final los puntajes totales de los jugadores.

	list_jugadores = jugadores()
	seleccion_dificultad()

	for jugador in list_jugadores:
	    reglas_de_juego()


# Preguntas
# Preguntas de muestra, pendiente por sustituir por las verdaderas
preguntas_3 = {'En regex el patron "\w{4, }" corresponde a caracteres alfanuméricos con una extensión de 4.':False,
            'El método capitalize( ) permite ubicar letras mayúsculas en cada elemento de un string.':False,
            'El orden de un loop puede ser el mismo para una lista regular y para un list comprehension.':True,
            'Una lambda utiliza la misma sitaxis que una funcion.':False,
            'Las funciones solo pueden ser llamadas una sola vez.':False,
            'Los sets nos permiten relizar analisis de valores unicos.':True,
            '‘\W’ refiere a caracteres alfanuméricos en regex.':False,
            'Los strings son inmutables.':False,
            'Un list comprehension no puede funcionar con condicionales.':False,
            'Una lambda no puede estár dentro de una Funcion.':False,
            'Las variable locales de las funciones, pueden ser llamadas en otras funciones.':False,
            'Podemos acceder a los valores de los diccionarios con los metodos keys() y values().':True,
            'En regex el set "[^a-z]" corresponde a cualquier minúscula entre a y z.':False,
            'Empleamos el método split( ) para convertir strings en listas.':True,
            'Con list comprehension solemos usar el método append( ).':False,
            'Todas las lambdas son funciones, pero no todas las funciones son lambdas.':True,
            'Todas las funciones deben contener un "return".':False,
            'Los diccionarios están compuestos por "Keys" y "Values".':True,
            'El método re.findall muestra los match objects de un string a modo de lista.':True,
            'Se pueden aplicar operaciones matemáticas a strings':True,
            'Otro nombre de las "Lambdas" es "Anonimas".':True,
            'Los list comprehension pueden funcionar para almacenamiento iterativo. -':True,
            'La palabra reservada para inciar una funcion es: "Lambda".':False,
            'Las tuplas se definen con []':False,
            'Regex nos permite identificar diferentes patrones en un texto.':True,
            'Un list comprehension permite optimizar la lógica de una lista.':True,
            'La palabra reservada para inciar una lambda es: "def."':False,
            'Un string es una secuencia de caracteres y espacios delimitados por comillas.':True,
            'Las funciones son un conjunto de código que retornan un resultado.':True,
            'Las tuplas son mutables,':False}

preguntas_2 = {'Las tuplas son mutables.':False,
            'Las funciones son un conjunto de código que retornan un resultado.':True,
            'La palabra reservada para inciar una lambda es: "def".':False,
            'Un list comprehension permite optimizar la lógica de una lista.':True,
            'Un string es una secuencia de caracteres y espacios delimitados por comillas.':True,
            'Regex nos permite identificar diferentes patrones en un texto.':True,
            'Las tuplas se definen con [].':False,
            'La palabra reservada para inciar una funcion es: "Lambda". ':False,
            'Otro nombre de las "Lambdas" es "Anonimas".':True,
            'Un list comprehension puede funcionar para almacenamiento iterativo.':True,
            'Se pueden aplicar operaciones matemáticas a strings.':True,
            'El método re.findall muestra los match objects de un string a modo de lista.':True,
            'Los diccionarios están compuestos por "Keys" y "Values".':True,
            'Todas las funciones deben contener un "return"':False,
            'Todas las lambdas son funciones, pero no todas las funciones son lambdas.':True,
            'En un list comprehension usamos el método append( ).':False,
            'Empleamos el método split( ) para convertir strings en listas.':True,
            'El set [^a-z] corresponde a cualquier minúscula entre a y z.':False,
            'Los sets nos permiten relizar analisis de valores únicos.':True,
            'Las funciones solo pueden ser llamadas una sola vez.':False}

preguntas_1 = {'Un string es una secuencia de caracteres y espacios delimitados por comillas.':True,
            'Regex nos permite identificar diferentes patrones en un texto.':True,
            'Las tuplas son mutables.':False,
            'Los diccionarios están compuestos por "Keys" y "Values".':True,
            'Todas las funciones deben contener un "return".':False,
            'Se pueden aplicar operaciones matemáticas a strings.':True,
            'Los strings son inmutables.':False,
            'Un list comprehension puede funcionar para almacenamiento iterativo.':True,
            'Otro nombre de las "Lambdas" es "Anonimas".':True,
            'Las tuplas se definen con [].':False}