from datetime import datetime

name = input('what is your name: ')
birth_date = eval(input('when were you born:  '))

current_year = datetime.today().year
age = current_year - birth_date

print(name,'you are', age, 'years old')