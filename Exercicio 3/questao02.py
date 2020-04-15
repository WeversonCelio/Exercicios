#Abelindo é um professor muito malvado. Ele quer decidir como
#reprovar Rondinelly, que tirou 8.66, 5.35, 5 e 1, respectivamente,
#nas provas P1, P2, P3 e P4. Para isso, ele pode calcular a nota final
#usando média aritmética (M.A.), média geométrica (M.G.) ou média
#harmônica (M.H.).
#Qual dessas médias dá a maior nota pra Rondinelly? E qual das médias
#dá a pior nota?

p1 = 8.66
p2 = 5.35
p3 = 5
p4 = 1

ma = (p1 + p2 + p3 + p3 + p4)/4
mg = (abs(p1 + p2 + p3 + p4)) ** 1/4
mh = 4 / ((1/p1) +  (1/p2) + (1/p3) + (1/p4))


print ('ma = ', ma)
print( 'mg = ', mg)
print (' mh = ', mh)      
