import os
import time

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

Colors = [RED, BLUE , WHITE]


def light(color):
    for i in range(9):
        if i == 0:
            print(f'{(color+" "*2) + (END + " "*(14)) + (color + " "*(2)) + (END + " "*(14)) + (color+" "*(2))}')
        if 0<i<4:
            print(f'{(END+" "*(2*i)) + (color +" "*(2)) + (END+(" "*((18)-(4*i+4)))) + (color + " "*(2)) + (END+(" "*((-6)+(4*i+4)))) + (color +" "*(2)) + (END+(" "*((18)-(4*i+4)))) + (color + " "*(2)) + (END +" "*(2*i+2))}')
        if i == 4:
            print(f'{(END+" "*(8)) + (color + " "*(2)) + (END + " "*(14)) + (color + " "*(2)) + (END + " "*(10))}')
        if 4<i<8:
            print(f'{(END+" "*((16)-(2*i))) + (color +" "*(2)) + (END+(" "*((-22)+(4*i+4)))) + (color + " "*(2)) + (END+(" "*((34)-(4*i+4)))) + (color +" "*(2)) + (END+(" "*((-22)+(4*i+4)))) + (color + " "*(2)) + (END +" "*((16)-(2*i)))}')
        if i == 8:
            print(f'{(color+" "*2) + (END + " "*(14)) + (color + " "*(2)) + (END + " "*(14)) + (color+" "*2) + END}')
        
while True:
    for cadr in range(3):
        if cadr == 0:  
            light(RED)
            light(BLUE)
            light(WHITE)
        if cadr == 1:
            light(BLUE)
            light(WHITE)
            light(RED)
        # if cadr == 2:
        #     light(BLUE)
        #     light(RED)
        #     light(WHITE)
        time.sleep(0.5)
        os.system("cls")