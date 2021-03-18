# Make a program that reads the gender of a person, but only accept the values ​​'M' or 'F'. If it is wrong, ask for the typing again until it has a correct value.

sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
print(sex)
while sex not in 'MmFf':
  sex = str(input('Dados Inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sex} registrado com succeso')
