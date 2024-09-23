'''
Created on 16 sept 2024

@author: jcgon
'''
from datetime import datetime
import re
from src.database.db_manager import db_manager
from src.env_variables.env_variables import header_view, exercise_editor_view, exercise_creator_view, \
    choose_muscle, back_exercises, chest_exercises, legs_exercises, \
    biceps_exercises, triceps_exercises, shoulders_exercises, exercise_delete_view, exercises_show_view


def connect_database() -> db_manager:
    db_path = "./database/db.db"
    return db_manager( db_path )


def init_database( main_database: db_manager ) -> dict:
    sql_path = "./database/sql_script.sql"
    return main_database.init_database( sql_path )


def home_inputs_manager( num, date, personal_data: dict = {} ) -> None | bool:
    match int( num ):
        case 0:
            print( header_view )
        case 1:
            print( home_view_formater( date ) )
        case 2:
            print( personal_data_formater( personal_data, date ) )
        case 3:
            show_input_manager()
        case 4:
            print( exercise_editor_view )
        case 5:
            print( exercise_creator_view )
            creator_input_manager( date, personal_data )
        case 6:
            print( exercise_delete_view )
            delete_input_manager( date, personal_data )
        case "exit":
            return True
        case _:
            pass


def creator_input_manager( date, personal_data: dict = {} ):
    input_str = input( "Introduce un número: " ).strip()
    if( input_str != "" and re.match( r'[0-9]', input_str ) ):
        match int( input_str ):
            case 1:
                home_inputs_manager( num = "1", date = date )
            case 2:
                print( choose_muscle )
                muscle = input( "Choose one: " ).strip()
                if muscle != "" and re.match( r'[0-9]', muscle ):
                    muscle = exercise_name_format( muscle, choose_muscle )
                    exercise_name = muscle_input_manager( muscle )
                    connect_database().create_exercise( user_id_ = personal_data["id"], date_ = date, muscle_ = muscle, exercise_name_ = exercise_name )
                    home_inputs_manager( num = "1", date = date )
            case 3:
                selected_date = input( "Introduce la fecha (dd/mm/yyyy): " ).strip()
                if( check_date( selected_date ) ):
                    print( choose_muscle )
                    muscle = input( "Choose one: " ).strip()
                    if muscle != "" and re.match( r'[0-9]', muscle ):
                        muscle = exercise_name_format( muscle, choose_muscle )
                        exercise_name = muscle_input_manager( muscle )
                        connect_database().create_exercise( user_id_ = personal_data["id"], date_ = selected_date, muscle_ = muscle, exercise_name_ = exercise_name )
                        home_inputs_manager( num = "1", date = date )


def delete_input_manager( date, personal_data: dict = {} ):
    input_str = input( "Introduce un número: " ).strip()
    if( input_str != "" and re.match( r'[0-9]', input_str ) ):
        match int( input_str ):
            case 1:
                home_inputs_manager( num = "1", date = date )
            case 2:
                print( choose_muscle )
                muscle = input( "Choose one: " ).strip()
                if muscle != "" and re.match( r'[0-9]', muscle ):
                    muscle = exercise_name_format( muscle, choose_muscle )
                    exercise_name = muscle_input_manager( muscle )
                    db = connect_database()
                    exercise_log = db.get_exercise_log( user_id_ = personal_data["id"], date_ = date, muscle_ = muscle, exercise_name_ = exercise_name )
                    print( exercise_log )
                    if type( exercise_log ) == dict: db.delete_exercise( exercise_log_id_ = exercise_log["id"] )
                    else: print( "Ejercicio inexistente" )
                    home_inputs_manager( num = "1", date = date )

            case 3:
                selected_date = input( "Introduce la fecha (dd/mm/yyyy): " ).strip()
                if( check_date( selected_date ) ):
                    print( choose_muscle )
                    muscle = input( "Choose one: " ).strip()
                    if muscle != "" and re.match( r'[0-9]', muscle ):
                        muscle = exercise_name_format( muscle, choose_muscle )
                        exercise_name = muscle_input_manager( muscle )
                        db = connect_database()
                        exercise_log = db.get_exercise_log( user_id_ = personal_data["id"], date_ = selected_date, muscle_ = muscle, exercise_name_ = exercise_name )
                        print( exercise_log )
                        if type( exercise_log ) == dict: db.delete_exercise( exercise_log_id_ = exercise_log["id"] )
                        else: print( "Ejercicio inexistente" )
                        home_inputs_manager( num = "1", date = date )


def show_input_manager():
    print( exercises_show_view )
    input_str = input( "Introduce a number:" )


def muscle_input_manager( muscle ) -> str | None:
    match muscle.lower():
        case "chest":
            print( chest_exercises )
            input_str = input( "Choose one: " ).strip()
            return exercise_name_format( input_str, chest_exercises )
        case "back":
            print( back_exercises )
            input_str = input( "Choose one: " ).strip()
            return exercise_name_format( input_str, back_exercises )
        case "legs":
            print( legs_exercises )
            input_str = input( "Choose one: " ).strip()
            return exercise_name_format( input_str, legs_exercises )
        case "bíceps":
            print( biceps_exercises )
            input_str = input( "Choose one: " ).strip()
            return exercise_name_format( input_str, biceps_exercises )
        case "tríceps":
            print( triceps_exercises )
            input_str = input( "Choose one: " ).strip()
            return exercise_name_format( input_str, triceps_exercises )
        case "shoulders":
            print( shoulders_exercises )
            input_str = input( "Choose one: " ).strip()
            return exercise_name_format( input_str, shoulders_exercises )
        case _:
            print( "No muscle found" )


def personal_data_formater( personal_data: dict , date ) -> str:
    return f"""
Fecha actual: {date}

                1. Inicio

                Nombre: {personal_data["name"]}

                Primer apellido: {personal_data["first_surname"]}

                Segundo apellido: {personal_data["second_surname"]}

            """


def home_view_formater( date ) -> str:
    return f"""
Fecha actual: {date}

                1. Inicio

                2. Datos personales

                3. Ver ejercicios (3) o ejercicio (3,{date})

                4. Editar ejercicion (4,{date})

                5. Crear ejercicios (5,{date})

                6. Borrar ejercicios (6,{date})

            """


def check_date( date_str: str ):
    if re.match( r'^\d{2}/\d{2}/\d{4}', date_str ):
        print( "here" )
        date_components = date_str.split( '/' )
        if( 
            int( date_components[0] ) <= 31
            and int( date_components[1] ) <= 12
            and int( date_components[2] ) <= int( re.findall( r'\d{4}', get_current_date() )[0] )
            ):
            print( "Valid date." )
            return True
        else:
            return False
    else:
        return False


def validate_name( name: str ):
    return bool( re.fullmatch( r'[a-zA-ZáéíóúüñÑ]+\s+[a-zA-ZáéíóúüñÑ]+\s+[a-zA-ZáéíóúüñÑ]+', name.strip() ) )


def validate_input( string: str ) -> dict | bool:
    if re.match( r'[0-9],[0-9][0-9][^\\][0-9][0-9][^\\][0-9][0-9][0-9][0-9]', string ):
        first_letter = string.strip()[0]
        date = string.strip()[2:12]
        date = re.match( r'.*[0-9][0-9][^\\][0-9][0-9][^\\][0-9][0-9][0-9][0-9]', date ).group()
        return { "first_number": first_letter, "date": date }
    else:
        return False


def get_current_date() -> str:
    return datetime.today().strftime( '%d/%m/%Y' )


def list_to_array( env_variable ) -> list:
    res = env_variable.split( '\n' )
    fin = []
    for  line in res:
        if len( line ) != 0 and re.match( r'[0-9]', line.strip() ):
            fin.append( re.search( r'[a-zA-Z].*', line.strip() ).group() )
    return fin


# Devolver el ejercicio a partir del número
def exercise_name_format( exercise_number, exercise_env ) -> str:
    values = list_to_array( exercise_env )
    match int( exercise_number.strip() ):
        case 1:
            return values[0]
        case 2:
            return values[1]
        case 3:
            return values[2]
        case 4:
            return values[3]
        case 5:
            return values[4]
        case 6:
            return values[5]
        case _:
            return "No exercise found"
