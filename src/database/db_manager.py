'''
Created on 16 sept 2024

@author: jcgon
'''
# import os
import sqlite3


class db_manager:

    def __init__( self, db_path ) -> None:
    # Nobre de la base de datos
        self.db_name = db_path
    # Conexión con la base de datos
        self.connection = sqlite3.connect( db_path )
    # Cursor = tabla devuelta tras petición (creo)
        self.cursor = self.connection.cursor()
    # Crear base de datos en memoria RAM
        # db_connection: sqlite3.Connection = sqlite3.connect(":memory:")

    def init_database( self, sql_path ):
        # Leer contenido del archivo
        with open( sql_path, 'r' ) as file:
            sql_str = file.read()
        self.cursor.executescript( sql_str )

    def get_personal_data( self ):
        try:
            self.cursor.row_factory = sqlite3.Row
            res = self.cursor.execute( "SELECT * FROM User" ).fetchone()
            dictionary = dict()
            if res:
                for index, content in enumerate( res ):
                    dictionary[res.keys()[index]] = content
                return dictionary
            else:
                return dict()
        except sqlite3.OperationalError:
            return False

    def create_user( self, name_: str, first_surname_: str, second_surname_: str ):
        self.cursor.executescript( f"INSERT INTO User (name, first_surname, second_surname) VALUES ('{name_}','{first_surname_}','{second_surname_}');" );

    def create_exercise( self, user_id_, date_, muscle_, exercise_name_ ):
        self.cursor.executescript( f"INSERT INTO ExerciseLog (date, muscle, exercise_name, user_id) VALUES ('{date_}','{muscle_}', '{exercise_name_}','{user_id_}');" )

    def delete_exercise( self, exercise_log_id_ ):
        print( exercise_log_id_ )
        self.cursor.executescript( f"DELETE FROM ExerciseSet WHERE exercise_log_id = {exercise_log_id_}" )
        self.cursor.executescript( f"DELETE FROM ExerciseLog WHERE id = {exercise_log_id_}" )

    def create_exercise_set( self, exercise_log_id_, set_, repetitions_, weight_, rest_duration_ ):
        self.cursor.executescript( f"INSERT INTO ExerciseSet (exercise_log_id, set_name, repetitions, weight, rest_duration) VALUES ('{exercise_log_id_}','{set_}','{repetitions_}','{weight_}', '{rest_duration_}');" )

    def get_exercise_log( self, date_, user_id_, exercise_name_, muscle_ ) -> bool | dict:
        try:
            self.cursor.row_factory = sqlite3.Row
            res = self.cursor.execute( f"SELECT * FROM ExerciseLog WHERE date = '{date_}' AND user_id = {user_id_} AND exercise_name = '{exercise_name_}' AND muscle = '{muscle_}'" ).fetchone()
            dictionary = dict()
            if res:
                for index, content in enumerate( res ):
                    dictionary[res.keys()[index]] = content
                return dictionary
            else:
                return dict()
        except sqlite3.OperationalError:
            return False

    def get_exercise_logs_by_date( self, date_, user_id_ ):
        try:
            exercise_logs = self.cursor.execute( f"SELECT * FROM ExerciseLog WHERE user_id = {user_id_} AND date = '{date_}'" ).fetchall()

            print( exercise_logs )
            editor_view = """
                1. Inicio

                Repeticiones (num_serie,r,num_rep)

                Peso (num_serie,p,peso)

                Descanso (num_serie,d,minutos)\n
            """

            for exercise_log in exercise_logs:
                exercise_log = dict( exercise_log )
                exercise_name_str = f' {exercise_log["exercise_name"]}'  # 13 characters
                print( exercise_log )
                while( len( exercise_name_str ) < 13 ):
                    exercise_name_str = exercise_name_str + " "

                exercise_set = self.get_exercise_set( exerercise_log_id_ = exercise_log["id"] )

                sets_str = ""
                if( set != None ):
                    print( set )
                    set_str = f'     Serie {exercise_set["set"]} |  {exercise_set["repetitions"]}  |  {exercise_set["weight"]}  |  {exercise_set["rest_duration"]} \n'
                    sets_str += set_str

                editor_view += f"""
        ----------------------------------------------------
        {exercise_name_str}   Repeticiones/ Peso/ Descanso
        {sets_str}
        Fecha: {exercise_log["date"]}
        ----------------------------------------------------\n
        """
                return editor_view
        except sqlite3.OperationalError:
            return False

    def get_exercise_set( self, exerercise_log_id_ ):
        try:
            return self.cursor.execute( f"SELECT * FROM ExerciseSet WHERE exercise_log_id = {exerercise_log_id_}" ).fetchone()
        except sqlite3.OperationalError:
            return False

    def get_all_exercise_logs( self, user_id_ ):
        try:
            res = self.cursor.execute( f"SELECT * FROM ExerciseLog WHERE user_id = {user_id_}" ).fetchall()
            return res
        except sqlite3.OperationalError:
            return False

    def close_connection( self ):
        self.connection.close();

