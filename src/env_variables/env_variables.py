'''
Created on 16 sept 2024

@author: jcgon
'''
# Views variables
header_view = """
#############################################################
                           Gym App
"""

exit_app_view = """

                Thank you for using this App
#############################################################
            """
exercises_show_view = """
Current date:
            1. Inicio

            2. Mostrar los ejrcicios de hoy

            3. Mostrar ejercicios de una fecha concreta

            4. Mostrar todos los ejercicios
            """
exercise_editor_view = """
                1. Inicio

                Repeticiones (num_serie,r,num_rep)

                Peso (num_serie,p,peso)

                Descanso (num_serie,d,minutos)
                __________________________________________
                Press Banca    rep     peso    Descanso
                    Serie 1 |       |        |
                    Serie 2 |       |        |
                    Serie 3 |       |        |
                    Serie 4 |       |        |
                Fecha: 26/05/2024
                __________________________________________
            """
exercise_creator_view = """
                1. Inicio

                2. Crear ejercicio hoy

                3. Crear ejercicio en otra fecha

"""
exercise_delete_view = """
                1. Inicio

                2. Eliminar ejercicio hoy

                3. Eliminar ejercicio en otra fecha

"""

# Muscles and exercises variables
choose_muscle = """
            ·Choose muscles:
                1. Chest
                2. Back
                3. Legs
                4. Bíceps
                5. Tríceps
                6. Shoulders
            """
chest_exercises = """
            Chest:
                1. Bench Press (Press de banca)
                2. Push-ups (Flexiones)
                3. Dumbbell Flyes (Aperturas con mancuernas)
                4. Incline Bench Press (Press inclinado)
                5. Chest Dips (Fondos en paralelas)
"""
back_exercises = """
            Back:
                1. Pull-ups (Dominadas)
                2. Deadlift (Peso muerto)
                3. Barbell Row (Remo con barra)
                4. Lat Pulldown (Jalón al pecho)
                5. T-Bar Row (Remo con barra en T)
"""
legs_exercises = """
            Legs:
                1. Squat (Sentadillas)
                2. Lunges (Zancadas)
                3. Leg Press (Prensa de piernas)
                4. Romanian Deadlift (Peso muerto rumano)
                5. Leg Curl (Curl de piernas)
"""
biceps_exercises = """
            Bíceps:
                1. Barbell Curl (Curl con barra)
                2. Dumbbell Curl (Curl con mancuernas)
                3. Concentration Curl (Curl de concentración)
                4. Hammer Curl (Curl martillo)
                5. Preacher Curl (Curl en banco predicador)
"""
triceps_exercises = """
            Tríceps:
                1. Tricep Dips (Fondos para tríceps)
                2. Tricep Pushdown (Extensiones de tríceps en polea)
                3. Skull Crushers (Rompecráneos)
                4. Close-grip Bench Press (Press con agarre cerrado)
                5. Overhead Tricep Extension (Extensión de tríceps sobre la cabeza)
"""
shoulders_exercises = """
            Shoulders:
                1. Overhead Press (Press militar)
                2. Lateral Raise (Elevaciones laterales)
                3. Front Raise (Elevaciones frontales)
                4. Arnold Press (Press de Arnold)
                5. Face Pulls (Jalones hacia la cara)
"""
