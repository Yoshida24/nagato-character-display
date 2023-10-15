import time
from modules.so1602 import so1602


def left_shift(message):
    str_first = message[:1]
    str_not_first = message[1:]
    return str_not_first + str_first

def right_shift(message):
    str_last = message[len(message)-1:]
    str_not_last = message[:len(message)-1]
    return str_last + str_not_last

def app_clock():
    cute_message = " I LOVE YOU    "
    
    oled = so1602( 1, 0x3c )
    oled.move_home()
    oled.set_cursol( 0 )
    oled.set_blink( 0 )

    while True:
        oled.move( 0x00, 0x00 )
        oled.write(cute_message[:16] )
        oled.move( 0x00, 0x01 )
        oled.write( time.strftime("    %H:%M:%S") )
        cute_message = left_shift(cute_message)
        time.sleep(0.1)

def main():
    app_clock()
    
main()
