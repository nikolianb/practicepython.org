a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [] #number less than 5
c = [] #number less than input
num = int(input("What is the number you want to check? "))
for el in a:
    if(el < 5):
        b.append(el)
    if(el < num):
        c.append(el)
print("Less than 5: ",b)
print(f"Less than {num}: {c}")
    
