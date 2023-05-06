import datetime

name = input("What's your name ? ")
age = int(input("What's your age? "))
repeat = int(input("How many copies you want ? "))
age = (100-age)
year = datetime.datetime.today().year + age

for i in range(repeat):
    print(name,"will be 100 years old in",age,"years at year",year)