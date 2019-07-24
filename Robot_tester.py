from Robot import *

def sensar_test(robot,get_vecinos):
    """
    sensar_test(robot,get_vecinos):
        robot: objeto de la clase Robot
        get_vecinos: Lista de 4 elementos, ceros y unos

    Esta funcion testea el metodo Robot.sensar()
    """
    robot.sensar(get_vecinos)
    print('***Robot.sensar() tester***')
    print('laberinto.get_vecinos() me da: ', get_vecinos)
    print('ada.sensor devuelve:           ', robot.sensor)
    return 0

def seguir_pared_tester(robot, direccion, sensor):
    """
    seguir_pared_tester(robot, direccion, sensor):
        robot: objeto de la clase Robot
        direccion: Lista de 4 elementos, ceros y unos,
                   direccion en la cual se esta moviendo el robot
        sensor: Lista de 4 elementos, ceros y unos, obtenidos
                de la lista de vecinos

    Esta funcion testea el funcionamiento del metodo Robot.seguir_pared().
    Debo inventar una direccion y lo que me dice el sensor, y la funcion
    me devuelve que decision toma el robot.
    """
    print('***Robot.seguir_pared() tester***')
    robot.set_direccion(direccion)
    robot.sensar(sensor)
    print("la direccion del robot es: ", robot.direccion)
    print("el sensor del robot es:    ", robot.sensor)
    robot.seguir_pared()
    print("decide su nueva direccion: ", robot.direccion)

    return robot.direccion

####### suerte de MAIN

ada = Robot()

direccion = [1,0,0,0]
sensor = [1,0,0,1]
seguir_pared_tester(ada, direccion, sensor)
