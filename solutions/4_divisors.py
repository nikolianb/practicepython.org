num = int(input("WHats the num? "))
div = []

for el in range(1,num+1):
    if(num % el == 0):
        div.append(el)
print(f"Divisors of the number {num} are {div}")