d = int(input('Quantos dia alugados? '))
km = float(input('Quantos KM rodados ? '))
total = (d * 60) + (km * 0.15)
print(f'O total a pagar é de R${total:.2f}')


