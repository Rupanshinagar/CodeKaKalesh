import random
print("==== Password Generator ====")
print()

length = int(input("enter password length\n"))

upper = input(" Include uppercase? (y/n): ")
lower = input(" Include lowercase? (y/n): ")
numbers = input(" Include numbers? (y/n): ")
symbols = input(" Include symbols? (y/n): ")

characters = ""

if upper =="Y"or upper =="y":
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if lower =="Y"or lower =="y":
    characters += "abcdefghijklmnopqrstuvwxyz"
if numbers =="Y"or numbers =="y":
    characters += "0123456789"
if symbols =="Y"or symbols =="y":
    characters += "!@#$%^&*()_+{}|[]:\;'<>,.?/"

if characters == "":
    characters = "abcdefghijklmnopqrstuvwxyz"
    print("You did not select any character types. Defaulting to lowercase letters.")

password = ""
for i in range(length):
    random_char = random.choice(characters)
    password = password + random_char

print()
print("Your generated password is: " )
print(password)

strenght_score = 0 

if len(password) >= 8:
    strenght_score += 1
if len(password) >= 12:
    strenght_score += 1

types_used = 0
if upper =="Y"or upper =="y":
    types_used += 1 
if lower =="Y"or lower =="y":
    types_used += 1
if numbers =="Y"or numbers =="y":
    types_used += 1
if symbols =="Y"or symbols =="y":
    types_used += 1

if types_used >= 3:
    strenght_score += 1

print()
print("Password Strength: ")
if strenght_score <= 1:
    print(" Weak")  
elif strenght_score == 2:
    print(" Moderate")
else:
    print(" Strong")

save = input("\nDo you want to save the password to a file? (y/n): ")
if save == "Y" or save == "y":
    file=open("passwords.txt", "a")
    file.write(password + "\n")
    file.close()
    print("Password saved to passwords.txt")