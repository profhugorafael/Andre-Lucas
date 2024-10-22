esta_chovendo = True
a = 1
b = 2
c = 3

#if...then
if esta_chovendo:
  print('vou ficar em casa')

# se delta for negativo e a for positivo entao diga que todos os valores sao positivos

delta = b * b - 4 * a * c
sempre_positivo = delta < 0 and a >0

if sempre_positivo:
  print('todos os valores sao positivos')

print('fim do programa')
