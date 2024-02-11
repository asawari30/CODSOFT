import random
import string

def generate_pwd(len, complexity):
    char = ""
    if complexity == "1":
        char = string.ascii_letters 
    elif complexity == "2":
        char = string.ascii_letters + string.digits 
    elif complexity == "3":
        char = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "4":
        exit(0)
    else:
        print("Re-enter your choice")
        return False
    
    pwd = ''.join(random.choice(char) for _ in range(len))
    return pwd

len = int(input("Enter the length of the password: "))
while True:
  complexity = input("Enter the complexity level\n1. Only letters\n2. Letters and numbers\n3. Letters, numbers, and symbols\n4. Exit\n")
  pwd = generate_pwd(len, complexity)
  if pwd:
    print("Generated password is :", pwd)