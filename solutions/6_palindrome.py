emri = input("Whats the word? ")

a = [] #Here we will store the words
reverse = [] #Here we store the reversed word

for char in emri:
    a.append(char)
# print(a)

for char in (range(1,len(emri)+1)):
    #print(a[-char])
    reverse.append(a[-char])
# print(reverse)

if(a == reverse):
    print("The word is palindrome")
else:
    print("The word is not palindrome")