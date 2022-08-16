import time

formato = '%H:%M:%S'

def obj_date_to_str( hora ) :
    return time.strftime( formato, hora )

# Convertir a segundos
def convertir_a_segundos( hora_tuple ) :
    return time.mktime( hora_tuple )

# Obtiene hora actual
def get_hora_actual() :
    return obj_date_to_str( time.localtime() )

def set_hora( hora_str ) :
    horas, minutos, segundos = hora_str.split( ':' )

    data = list( time.localtime() )

    data[ 3 ] = int( horas )
    data[ 4 ] = int( minutos )
    data[ 5 ] = int( segundos )

    return tuple( data )

def convertir_hora( seconds ):
    seconds = seconds % ( 24 * 3600 )
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % ( hour, minutes, seconds )

def main() :
    h_salida = '19:00:00'
    h_actual = get_hora_actual()

    print( f'Son las { h_actual }, la salida es a las { h_salida }' )
    
    h_salida_tuple = set_hora( h_salida )
    h_actual_tuple = time.localtime()
    
    secs_salida = convertir_a_segundos( h_salida_tuple )
    secs_actual = convertir_a_segundos( h_actual_tuple )

    # print( secs_actual, secs_salida )

    # Verifica si la hora actual es menor a la hora de salida del trabajo
    if secs_actual > secs_salida :

        print( f' > Es hora de ir a casa' )
    else :
        tdelta = secs_salida - secs_actual
        # print( tdelta )
        # print( time.localtime( tdelta ) )

        print( f' > Falta { convertir_hora( tdelta ) } para salir del trabajo' )

if __name__ == '__main__' :
    main()