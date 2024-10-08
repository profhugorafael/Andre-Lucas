texto = 'hello world'
pares = [2, 4, 6, 8, 10]

# for letra in texto:
#   print(letra)

# for par in pares:
#   print(par)

# range(stop): range(10) = 0, 1, 2, ..., 10
# range(start, stop): range(5, 10) = 5, 6, 7, 8, 9
# range(start, stop, step): range(0, 10, 2): 0, 2, 4, 6, 8

for i in range(10):
  print(i, end=', ')

print()

for i in range(5, 10):
  print(i, end=', ')

print()

for i in range(0, 10, 5):
  print(i, end=', ')

print()

for i in range(10, 0, -1):
  print(i, end=", ")

print()

for i in range(5):
  # print(f'valor na posicao {i} : {pares[i]}')
  print(f'pares[{i}] = {pares[i]}')

