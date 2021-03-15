from datetime import date

atual = date.today().year

totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
  nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
  idade = atual - nasc
  if idade >= 21:
  
  else:
  print('Essa pessosa é menor de idade')
