import math
print('1- Resolva essa expressão:')
expressao1 = (100-413 *(20-5 * 4))/5
print(expressao1)

#-----------------------
print('-----------------')
print('2- Enivaldo quer ligar três capacitores, de valores:')
print('c1 = 10 uF, c2 = 22 uF e c3 = 6.8 uF')
c1 = 10
c2=22
c3=6.8
print('capacitores em paralelo')
cp = c1+c2+c3
print(cp)
print('capacitores em serie')
cs = 1/(1/c1+1/c2+1/c3)
print(cs)

#-----------------------
print('-----------------')
print('3- Republica de 5')
cerveja = 75*2.2
macarrao = 2*8.73
mTomate = 1*3.45
cebola = 0.420 * 5.4
alho = .250 * 30
pao = 0.450 * 25
compra = cerveja+macarrao+mTomate+cebola+alho+pao
print('A compra deu: ', compra)
print('Cda um vai pagar:', compra/5)      

#-----------------------
print('-----------------')
print('4- pote de soverte vs bolinha de queijo')
x = 15
y = 10
z = 13

bQRaio = 1.2

fEmpac = 0.74

vBQ = (3/4)*math.pi*bQRaio
vPS = x * y * z
print('volume do bolinha de queijo = ', vBQ, ' volume do pote ', vPS)
nBolinhas = (vPS* 0.74) / vBQ
print('Numero de boinhas', nBolinhas)
