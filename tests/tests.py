'''
Created on 16 sept 2024

@author: jcgon
'''
# a,b,c que sume los cuadradosde los valores del rango [a,b) que son multiplos de c
from src.env_variables.env_variables import chest_exercises
from src.functions.functions import list_to_array, check_date


def rango( a:int, b:int, c:int ) -> int:
    res = 0
    for i in range( a, b ):
        if( ( c / i ).is_integer() ):
            res += i ** 2
    return res


print( rango( 1, 18, 4 ) )

print( check_date( "12/09/2024" ) )
