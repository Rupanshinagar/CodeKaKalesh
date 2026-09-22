import os

filename = "expenses.csv"

def add_expense():
    amount = input("How much did you bleed this time? ")
    category = input("What was the reason for this financial hemorrhage? ")

    with open(filename, "a") as file:
        file.write(f"{amount},{category}\n")
    print("Logged it. Your wallet is crying, but at least you have a record now.")

def view_expenses():
    if not os.path.exists(filename):
        print("Wow, no expenses yet? Suspiciously responsible of you.\n")
        return

    with open(filename, "r") as file:
        expenses = file.readlines()

    if not expenses:
        print("Wow, no expenses yet? Suspiciously responsible of you.\n")
        return

    print("\n--- Where Did Your Money Go ---")
    total = 0
    for line in expenses:
        line = line.strip()
        if not line:          
            continue
        parts = line.split(",")
        if len(parts) != 2:   
            continue
        amount, category = parts
        print(f"₹{amount} vanished into {category}")
        total += float(amount)
    print(f"Grand total damage: ₹{total}\n")

def main():
    while True:
        print("1. Add Expense (go on, hurt yourself)")
        print("2. View Expenses (face the truth)")
        print("3. Exit (pretend this never happened)")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye! Your bank account thanks you for leaving.")
            break
        else:
            print("That's not even an option. Try again, genius.\n")

main()