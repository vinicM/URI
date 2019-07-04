A,B,C=map (float,input().split(" "))
areaT = ((A*C)/2)
areaC = (3.14159*(C**2))
areaTR= ((A+B)/2)*C
areaQ= B**2
areaR=A*B
print('TRIANGULO: {:.3f}'.format(areaT))
print('CIRCULO: {:.3f}'.format(areaC))
print('TRAPEZIO: {:.3f}'.format(areaTR))
print('QUADRADO: {:.3f}'.format(areaQ))
print('RETANGULO: {:.3f}'.format(areaR))
