# Proyecto Nayely y Ricardo. Trivia de los temas vistos en clase

preguntas_3 = {'1. En regex el patron "\w{4, }" corresponde a caracteres alfanuméricos con una extensión de 4.':False,
            '2. El método capitalize( ) permite ubicar letras mayúsculas en cada elemento de un string.':False,
            '3. El orden de un loop puede ser el mismo para una lista regular y para un list comprehension.':True,
            '4. Una lambda utiliza la misma sitaxis que una funcion.':False,
            '5. Las funciones solo pueden ser llamadas una sola vez.':False,
            '6. Los sets nos permiten relizar analisis de valores únicos.':True,
            '7.‘\W’ refiere a caracteres alfanuméricos en regex.':False,
            '8. Los strings son inmutables.':True,
            '9. Un list comprehension no puede funcionar con condicionales.':False,
            '10. Una lambda no puede estár dentro de una Funcion.':False,
            '11. Las variable locales de las funciones, pueden ser llamadas en otras funciones.':False,
            '12. Podemos acceder a los elementos de los diccionarios con los metodos keys() y values().':True,
            '13. En regex el set "[^a-z]" corresponde a cualquier minúscula entre a y z.':False,
            '14. Empleamos el método split( ) para convertir strings en listas.':True,
            '15. Con list comprehension solemos usar el método append( ).':False,
            '16. Todas las lambdas son funciones, pero no todas las funciones son lambdas.':True,
            '17. Todas las funciones deben contener un "return".':False,
            '18. Los diccionarios están compuestos por "Keys" y "Values".':True,
            '19. El método re.findall muestra los match objects de un string a modo de lista.':True,
            '20. Se pueden aplicar operaciones matemáticas a strings':True,
            '21. Otro nombre de las "Lambdas" es "Anónimas".':True,
            '22. Los list comprehension pueden funcionar para almacenamiento iterativo. -':True,
            '23. La palabra reservada para inciar una funcion es: "Lambda".':False,
            '24. Las tuplas se definen con []':False,
            '25. Regex nos permite identificar diferentes patrones en un texto.':True,
            '26. Un list comprehension permite optimizar la lógica de una lista.':True,
            '27. La palabra reservada para inciar una lambda es: "def."':False,
            '28. Un string es una secuencia de caracteres y espacios delimitados por comillas.':True,
            '29. Las funciones son un conjunto de código que retornan un resultado.':True,
            '30. Las tuplas son mutables,':False}

preguntas_2 = {'1. Las tuplas son mutables.':False,
            '2. Las funciones son un conjunto de código que retornan un resultado.':True,
            '3. La palabra reservada para inciar una lambda es: "def".':False,
            '4. Un list comprehension permite optimizar la lógica de una lista.':True,
            '5. Un string es una secuencia de caracteres y espacios delimitados por comillas.':True,
            '6. Regex nos permite identificar diferentes patrones en un texto.':True,
            '7. Las tuplas se definen con [].':False,
            '8. La palabra reservada para inciar una funcion es: "Lambda". ':False,
            '9. Otro nombre de las "Lambdas" es "Anónimas".':True,
            '10. Un list comprehension puede funcionar para almacenamiento iterativo.':True,
            '11. Se pueden aplicar operaciones matemáticas a strings.':True,
            '12. El método re.findall muestra los match objects de un string a modo de lista.':True,
            '13. Los diccionarios están compuestos por "Keys" y "Values".':True,
            '14. Todas las funciones deben contener un "return"':False,
            '15. Todas las lambdas son funciones, pero no todas las funciones son lambdas.':True,
            '16. En un list comprehension usamos el método append( ).':False,
            '17. Empleamos el método split( ) para convertir strings en listas.':True,
            '18. El set [^a-z] corresponde a cualquier minúscula entre a y z.':False,
            '19. Los sets nos permiten relizar analisis de valores únicos.':True,
            '20. Las funciones solo pueden ser llamadas una sola vez.':False}

preguntas_1 = {'1. Un string es una secuencia de caracteres y espacios delimitados por comillas.':True,
            '2. Regex nos permite identificar diferentes patrones en un texto.':True,
            '3. Las tuplas son mutables.':False,
            '4. Los diccionarios están compuestos por "Keys" y "Values".':True,
            '5. Todas las funciones deben contener un "return".':False,
            '6. Se pueden aplicar operaciones matemáticas a strings.':True,
            '7. Los strings son inmutables.':True,
            '8. Un list comprehension puede funcionar para almacenamiento iterativo.':True,
            '9. Otro nombre de las "Lambdas" es "Anónimas".':True,
            '10. Las tuplas se definen con [].':False}

# Seleccion de Jugador y su nombre
list_jugadores = []
def jugadores():
    
    list_jugadores = []
    
    for i in range(int(input("Seleccione el numero de jugadores: "))):
        i = input("Ingrese nombre del jugador: ")
        list_jugadores.append(i)
    
    return list_jugadores

preguntas_juego = dict()
puntos_jugador = []
resultado_juego = dict(zip(list_jugadores,puntos_jugador))
list_jugadores = []


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

def reglas_de_juego():
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

list_jugadores = jugadores()
seleccion_dificultad()

for jugador in list_jugadores:
    reglas_de_juego()