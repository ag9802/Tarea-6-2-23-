# Practica 6 del lunes 6-2-23
text = open('text.txt', 'w' ) 

list= [1,2,3,4,5,6,7,8,9,10]
text.writelines(['1\t 2 \n','3 \t 4 \n','5 \t 6 \n','7 \t 8 \n','9 \t 10 \n', '\n'])

x = 0
v = 1
for i in list:
    if i%2 == 0:
        x += i
        text.write(str(x) + ' \t \n') 
    else:
        v *= i
        text.write( str(v) + '\t ')
  