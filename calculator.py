num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
def choices():
    print("Menu:")
    print("1. Perform addition")
    print("2. Perform subtraction")
    print("3. Perform multiplication")
    print("4. Perform division")
    print("5. Exit")
def addition():
    print("Result is:",num1+num2)
def subtraction():
    print("Result is:",num1-num2)
def multiplication():
    print("Result is:",num1*num2)
def division():
    print("Result is:",num1/num2)
def main():
    
    while True:
        choices()
        ch = input("Enter your choice: ")
        if ch == "1":
            addition()
        elif ch == "2":
            subtraction()
        elif ch == "3":
            multiplication()
        elif ch == "4":
            division()
        elif ch == "5":
            print("Exit")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

