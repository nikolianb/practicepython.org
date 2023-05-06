a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
over_lap = []
d = []

# for num in range(len(a)):
#     print(num+1)

for num in a:
    if num in b:
        over_lap.append(num)
        if num not in d:
            d.append(num)    


print(over_lap)
print(d)

#For the second extra we can also do set
print (set(a) & set(b))