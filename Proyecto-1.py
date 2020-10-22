# Proyecto Nayelly y Ricardo. Trivia de los temas vistos en clase

# Variables Globales
list_jugadores = []
preguntas_juego = dict()

# Seleccion de Jugador y su nombre
def jugadores():
        
    for i in range(int(input("Seleccione el numero de jugadores: "))):
        i = input("Ingrese nombre del jugador: ")
        list_jugadores.append(i)


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
	1. seleccionar una pregunta random de nuestro diccionario de preguntas
	2. recibo el input de la respuesta por jugador
	3. checo si el input es correcto en el diccionario original
	4. guardo la pregunta en el listado de "ya no preguntar" -- Se 
	5. acumulo los puntos por cada uno de lus jugadores

# Juego
# Se van mostrando pregunta por pregunta y se recibe la respuesta del jugador. T o F en mayusculas. la respuesta del jugador debe de ser convertida a mayusculas
def Juego():
	1. llamar funcion de jugadores
	2. llamar la funcion de dificultad
	3. definir las variables de los puntos por jugador -> para acumular los puntos de los jugadores
	4. while cantidad de preguntas de acuerdo a la dificultad y hacer la pregunta por cada jugador y llamar la funcion "reglas de juego".
	   imprimir al final los puntajes totales de los jugadores.



# Preguntas
# Preguntas de muestra, pendiente por sustituir por las verdaderas
preguntas_3 = {'pregunta1':True,
            'pregunta2':False,
            'pregunta3':True,
            'pregunta4':False,
            'pregunta5':True,
            'pregunta6':False,
            'pregunta7':True,
            'pregunta8':False,
            'pregunta9':True,
            'pregunta10':False,
            'pregunta11':True,
            'pregunta12':False,
            'pregunta13':True,
            'pregunta14':False,
            'pregunta15':True,
            'pregunta16':False,
            'pregunta17':True,
            'pregunta18':False,
            'pregunta19':True,
            'pregunta20':False,
            'pregunta21':True,
            'pregunta22':False,
            'pregunta23':True,
            'pregunta24':False,
            'pregunta25':True,
            'pregunta26':False,
            'pregunta27':True,
            'pregunta28':False,
            'pregunta29':True,
            'pregunta30':False}

preguntas_2 = {'pregunta1':True,
            'pregunta2':False,
            'pregunta3':True,
            'pregunta4':False,
            'pregunta5':True,
            'pregunta6':False,
            'pregunta7':True,
            'pregunta8':False,
            'pregunta9':True,
            'pregunta10':False,
            'pregunta11':True,
            'pregunta12':False,
            'pregunta13':True,
            'pregunta14':False,
            'pregunta15':True,
            'pregunta16':False,
            'pregunta17':True,
            'pregunta18':False,
            'pregunta19':True,
            'pregunta20':False}

preguntas_1 = {'pregunta1':True,
            'pregunta2':False,
            'pregunta3':True,
            'pregunta4':False,
            'pregunta5':True,
            'pregunta6':False,
            'pregunta7':True,
            'pregunta8':False,
            'pregunta9':True,
            'pregunta10':False}