from math import radians, cos, sin, tan
angulo = float(input('Informe um angulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O seno do angulo e: {:.2f}\nO cosseno do alguni e: {:.2f}\nA tangente do angulo e: {:.2f}'.format(sen, cos, tan))