'''
Created on 16 sept 2024

@author: jcgon
'''
from src.functions.functions import connect_database

db = connect_database( "../src/database/db.db" )
print( db.get_exercise_set_by_exercise_log_id( 5 ) )
