import time
import os
os.system ("cls")
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

#Рисунок Флага --> Нидерланды
for i in range(9):
    if i < 3:
        print(RED+" "*34+END)
    if 2<i <6 :
        print(WHITE+" "*34+END)
    if 5<i <9:
        print(BLUE+" "*34+END)
     

print(END)


#Рисунок Узоры --> c
# for i in range(9):
#     if i<8:
#         print(f'{(BLUE +" "*(2*i+2))+END+(" "*((34)-(4*i+4))+ END) +(RED + " "*(2*i+2))+END}')
#     else:
#         print(f'{END+" "*(16) + (RED + " "*(2)) + END + " "*(16)}')

for i in range(9):
    if i == 0:
        print(f'{(BLUE+" "*2) + (END + " "*(14)) + (RED + " "*(2)) + (END + " "*(14)) + (BLUE+" "*(2))}')
    if 0<i<4:
        print(f'{(END+" "*(2*i)) + (BLUE +" "*(2)) + (END+(" "*((18)-(4*i+4)))) + (RED + " "*(2)) + (END+(" "*((-6)+(4*i+4)))) + (RED +" "*(2)) + (END+(" "*((18)-(4*i+4)))) + (BLUE + " "*(2)) + (END +" "*(2*i+2))}')
    if i == 4:
        print(f'{(END+" "*(8)) + (RED + " "*(2)) + (END + " "*(14)) + (BLUE + " "*(2)) + (END + " "*(10))}')
    if 4<i<8:
        print(f'{(END+" "*((16)-(2*i))) + (RED +" "*(2)) + (END+(" "*((-22)+(4*i+4)))) + (BLUE + " "*(2)) + (END+(" "*((34)-(4*i+4)))) + (BLUE +" "*(2)) + (END+(" "*((-22)+(4*i+4)))) + (RED + " "*(2)) + (END +" "*((16)-(2*i)))}')
    if i == 8:
         print(f'{(RED+" "*2) + (END + " "*(14)) + (BLUE + " "*(2)) + (END + " "*(14)) + (RED+" "*2) + END}')

time.sleep(3) 
os.system ("cls")

print(END)

  
#Рисунок Функции --> y=2x
plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i * 2    #Рисунок Функция 

step = round(abs(result[0] - result[9]) / 9, 2)
print('f(1) Равен: {}'.format(step))

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += str(int(plot_list[i][j])) + '\t' + (WHITE+" ") + (END+" ")
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += (RED+'!') + END
    print(line)
print((END+" "*8) + (WHITE+" "*20) + END) 
print('\t0 1 2 3 4 5 6 7 8 9')

for i in range(10):
    # print(plot_list[i])
    pass


print(END)


# # Диаграмму процентного
file = open('sequence.txt', 'r')
numbers_list = []
for number in file:
    numbers_list.append(float(number.strip()))
file.close()

even_posit = 0 
odd_posit = 0   

for i, num in enumerate(numbers_list):
    if i % 2 == 0:  
        even_posit += abs(num)  
    else:  
        odd_posit += abs(num)   

print(f"Сумма чисел по модулю, стоящих на чётных позициях: {even_posit}")
print(f"Сумма чисел по модулю, стоящих на нечётных позициях: {odd_posit}")


print(END)


# # Рисунок Диаграмму
plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i*632.34/8
step = round(abs(result[0] - result[9]) / 9, 2)
for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += str(int(plot_list[i][j])) + '\t' + (WHITE+" ") + (END+" ")
        if j == 0 and 0<i:
            line += (END + " "*(3)) + (RED+' '*3) + END
        if j == 0 and 1<i:
            line += (END + " "*(6)) + (BLUE+' '*3) + END


    print(line)
print((END+" "*8) + (WHITE+" "*20) + END) 
print('\t   чётных   нечётных  ')


time.sleep(3)

os.system ("cls")