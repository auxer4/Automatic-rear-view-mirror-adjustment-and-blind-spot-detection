import inspect
inspect.getargspec = inspect.getfullargspec

from pyfirmata import Arduino, SERVO
import time

board = Arduino('COM5')

board.digital[9].mode = SERVO
board.digital[10].mode = SERVO

while True:
    board.digital[9].write(0)
    board.digital[10].write(0)
    time.sleep(1)

    board.digital[9].write(90)
    board.digital[10].write(90)
    time.sleep(1)

    board.digital[9].write(180)
    board.digital[10].write(180)
    time.sleep(1)