import string
import random

if __name__ == "__main__":
    # Using a while loop provides a clean entry and exit point
    while True:
    
        # Create generation definitions
        str1 = string.ascii_lowercase
        str2 = string.ascii_uppercase
        str3 = string.digits
        str4 = string.punctuation
        
        # Take input from the user: 
        pwdlen = int(input("Enter password length: "))
        
        # Assemble the password string
        s = []
        s.extend(list(str1))
        s.extend(list(str2))
        s.extend(list(str3))
        s.extend(list(str4))
        
        # Print the string to StdOut
        print("Your password is: ")
        print("".join(random.sample(s, pwdlen)))
       
        break

