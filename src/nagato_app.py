import time
from modules.so1602 import so1602
            
def app_nagato():
    line1 = "YUKI.N > "
    line2 = "sleeping beauty"
    
    oled = so1602( 1, 0x3c )
    oled.move_home()
    
    idx1 = 0
    idx2 = 0
    
    time.sleep(1) 
    
    while idx1 < 9:
        oled.write( line1[idx1] )
        time.sleep(0.1)
        idx1 += 1
    
    time.sleep(3) 
    oled.move( 0x00, 0x01 )
        
    while idx2 < 15:
        oled.write( line2[idx2] )
        time.sleep(0.2)
        idx2 += 1

def main():
    app_nagato()
    
main()
