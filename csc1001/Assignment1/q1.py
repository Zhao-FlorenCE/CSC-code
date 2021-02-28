final = int(input('Pelase enter the final account value: '))
interest = float(input('Pelase enter the annual interest value: '))
year = int(input('Pleast enter the number of years: '))

initial = final / (1 + interest / 100) ** year

print('The initial value is:', initial)