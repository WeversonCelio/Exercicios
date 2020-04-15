''' Josefson deseja fazer compras na China. Ela quer comprar um
celular de USD 299,99, uma chaleira de USD 23,87, um gnomo de
jardim de USD 66,66 e 6 adesivos de unicórnio de USD 1,42 cada
um. O frete de tudo isso para a cidade de Rolândia, no Paraná,
ficou em USD 12,34.
a. Calcule o valor total da compra em dólares.
b. Usando o mesmo valor do dólar do exercício anterior,
calcule o preço final em Reais. Lembre-se que o valor do IOF
é de 6,38 %.
c. Quanto ela pagou apenas de IOF? '''

celularUSD = 299.99
chaleiraUSD = 23.87
gnomoUSD = 66.66
adesivosUSD = 1.42 * 6

freteUSD = 12.34


USD = 3.65

compraUSD = celularUSD + chaleiraUSD + gnomoUSD + adesivosUSD + freteUSD
conversao = compraUSD * USD
IOF = conversao * 0.0638

compraBRL = conversao + IOF

print(' O total da compra foi USB ', compraUSD )
print(' O valor pago em Reais foi de R$ ', compraBRL)
print ('sendo o valor de IOF de R$ ', IOF)


