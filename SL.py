import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) 

class SL():
    def __init__(self):
         # motor
        self.SL_INT1=38
        self.SL_INT2=40
         # switch, C is node 1 to GND, 2 is NC
        self.switch_up=36     #NC T2T
        self.switch_down=35   #NC T2B

        GPIO.setup(self.SL_INT1,GPIO.OUT)
        GPIO.setup(self.SL_INT2,GPIO.OUT)
        GPIO.setup(self.switch_up,GPIO.IN)
        GPIO.setup(self.switch_down,GPIO.IN)

    def ccw(self): #go up
        print("go up")
        GPIO.output(self.SL_INT1, GPIO.HIGH)
        GPIO.output(self.SL_INT2, GPIO.LOW)
        time.sleep(0.5)

    def cw(self): #go down
        print("go down")
        GPIO.output(self.SL_INT1, GPIO.LOW)
        GPIO.output(self.SL_INT2, GPIO.HIGH)
        time.sleep(0.5)
    
    # no line-stop SL goes up until swich_up is activated -- stop -- wait
    # switch_up connects to NO, LOW means not pressed,     # if switch_up connects to NC, ==1
    def run(self):
        while True:
            if (GPIO.input(self.switch_up)==1):
                print("switch up is not pressed")
                self.ccw()
            
            elif (GPIO.input(self.switch_up)==0): #pressed
                print("switch up is pressed")
                break

        time.sleep(5) # sleep 5 secs, charging time 

        # SL goes down until switch_down is activated -- stop -- go home 
        # switch_down connects to NO, LOW means not pressed,    # if switch_down connects to NC, ==1
        while True:
            if (GPIO.input(self.switch_down)==1):                   # if switch_down connects to NO, ==0
                print("switch down is not pressed")
                self.cw()
            
            elif (GPIO.input(self.switch_down)==0): #pressed
                print("switch down is pressed")
                break
    print("clean up")
    GPIO.cleanup() #### try to comment this one 

SL().run()
