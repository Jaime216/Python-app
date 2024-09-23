'''
Created on 16 sept 2024

@author: jcgon
'''
from src.env_variables.env_variables import exit_app_view
from src.functions.functions import home_inputs_manager, validate_name, \
    get_current_date, connect_database, init_database

# Database options
main_database = connect_database()

# Print header
home_inputs_manager( 
num = "0",
date = get_current_date()
 )

# Save personal data
personal_data = main_database.get_personal_data()
if ( personal_data == False ):
    init_database( main_database )
    personal_data = main_database.get_personal_data()
else:
    home_inputs_manager( 
    num = "1",
    date = get_current_date()
     )

# Loop options: open_bool, input and printed
open_bool = True
input_str: str = ""

while open_bool:
    if( ( type( personal_data ) != bool ) and ( len( personal_data ) == 0 ) ):
        input_str = input( "Introduce tu nombre y tus apellidos separados por espacios:" )
        if( validate_name( input_str ) ):
            personal_values = input_str.strip().split( ' ' )
            new_txt = []
            for i, content in enumerate( personal_values ):
                if ( content.strip() != '' ): new_txt.append( content )
            main_database.create_user( *new_txt )
            personal_data = main_database.get_personal_data()
            home_inputs_manager( 
            num = "1",
            date = get_current_date()
             )
        else:
            print( "!Sigue las instrucciones¡\n" )

    elif( ( type( personal_data ) != bool ) and ( len( personal_data ) > 0 ) ):
        input_str = input( "Introduce un número: " ).strip()
        if( len( input_str.strip() ) == 1 ):
            home_inputs_manager( num = input_str, date = get_current_date(), personal_data = personal_data )

        # if( len( input_str ) == 1 ):
        #    print( home_inputs_manager(
        #        num = input_str,
        #        date = get_current_date(),
        #        personal_data = personal_data
        #        ) )
        # elif( len( input_str ) > 1 and input_str.lower() != "exit" ):
        #    validated_input = validate_input( input_str )
        #    if( validated_input != False ):
        #        first_number, date = validated_input.values()
        #        user_id = personal_data["id"]
        #
        #        res = creator_inputs_manager( first_number = first_number, date = date, personal_data = personal_data )
        #        if ( type( res ) == dict ):
        #            muscle_name, exercise_name = res.values()
        #            main_database.create_exercise( user_id_ = user_id, date_ = date, muscle_ = muscle_name, exercise_name_ = exercise_name )
        #
        elif( input_str.strip().lower() == "exit" ):
            print( exit_app_view )
            break

        # input_str = check_date(input_str)
        # print(f"Hoy es {input_str}\n") if input_str != False else print("Not valid date.\n")

