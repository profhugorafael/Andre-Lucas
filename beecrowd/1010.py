entrada = input().split()

codigo1 = int(entrada[0])
quantidade1 = int(entrada[1])
valor1 = float(entrada[2])

entrada = input().split()

codigo2 = int(entrada[0])
quantidade2 = int(entrada[1])
valor2 = float(entrada[2])

subtotal1 = quantidade1 * valor1
subtotal2 = quantidade2 * valor2

total = subtotal1 + subtotal2

print(f'VALOR A PAGAR: R$ {total:.2f}')