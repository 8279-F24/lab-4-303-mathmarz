import time
from adafruit_circuitplayground import cp

while True:
    cp.pixels.auto_write = False
    cp.pixels.brightness = 0.3

    max = 255
    while max > 0:
        
        for i in range(10):
            cp.pixels[i] = (max, 0, 0) 
        cp.pixels.show()
        time.sleep(0.3)

        max = max - 1

    restart = input(
        "Do you want to start again? (q to stop, any other key to continue): "
    ).lower()
    if restart == "q":
        print("Program ended.")
        for i in range(10):
            cp.pixels[i]=(0,0,0)
        break