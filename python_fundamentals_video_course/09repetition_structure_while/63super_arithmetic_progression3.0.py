# Improve EXERCISE 62 by asking the user if they want to show some more terms. The program ends when it says it wants to show 0 terms.

print('Arithmetic Progression Generator with While')
print('_/\_' * 10)

first = int(input('First term: '))
reason = int(input('PA reason: '))
term = first
count = 1
total = 0
more = 10

while more != 0:
  while count <= 15:
    print(f'{term} -> ', end='')
    term += reason
    count += 1
  print('PAUSE')
  more = int(input('How many more terms do you want to show? '))
print(f'Arithmetic Progression with {total} terms shown')