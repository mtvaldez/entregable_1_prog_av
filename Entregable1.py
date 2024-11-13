import pandas as pd
from random import randint

'''Asigno cada respuesta al numero de opcion que le corresponde con la funcion lambda y me quedo con la opcion igual a la correcta'''
translateAnswer = lambda row: [1, 2, 3][[row['Respuesta1'], row['Respuesta2'], row['Respuesta3']].index(row['Correcta'])]

'''Le paso un array de la cantidad de preguntas disponibles y devuelvo uno aleatoreo sacandolo de la lista con el metodo .pop()'''
def chooser(possible_values):
    intRandom = randint(0,len(possible_values)-1)
    return possible_values.pop(intRandom)

'''Funcion que devuelve un generador con un orden posible de preguntas'''
def question_generator(possible_values):
    while possible_values:
        yield file.iloc[chooser(possible_values)]

'''Funcion llamada por el checkeador de respuestas para comunicar si la respuesta fue correcta'''
def prefix(func):
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs):
            print("Bien ahí")
            return 10
        else:
            print("Esta no era")
            return 0
    return wrapper

'''Se fija si la respuesta correcta es igual a la del usuario'''
@prefix
def check_answer(correct_answer, user_answer):
    return correct_answer == user_answer

'''Funcion recursiva que imprime en la consola las preguntas con sus respectivas opciones'''
def preguntador(generator,cc):
    if cc < 5:
        row = next(generator)
        print(" ")
        print("Pregunta",cc+1,row['Pregunta'])
        print('1)',row['Respuesta1'])
        print('2)',row['Respuesta2'])
        print('3)',row['Respuesta3'])
        return check_answer(translateAnswer(row), int(input("Responder con el número de la opción: "))) + int(preguntador(generator,cc+1))
    else: 
        print(" ")
        print("Puntos:")
        return 0

'''Cargo el file usando la libreria pandas'''
file = pd.read_csv("trivia_questions.csv")
'''Creo una lista del tamaño de la cantidad de preguntas posibles'''
possibleValues = [i for i in range(0,len(file))]
'''Crea el generador para usar en la funcion recursiva para elegir las preguntas'''
generator = question_generator(possibleValues)
  
print(preguntador(generator,0))
