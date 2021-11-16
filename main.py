import string
import random

if __name__ == "__main__":
    str1 = string.ascii_lowercase
    # print(s1)
    str2 = string.ascii_uppercase
    # print(s2)
    str3 = string.digits
    # print(s3)
    str4 = string.punctuation
    # print(s4)
    pwdlen = int(input("Enter password length\n"))
    s = []
    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))
    # print(s)
    # random.shuffle(s)
    # print(s)
    print("Your password is: ")
    print("".join(random.sample(s, pwdlen)))
    # print("".join(s[0:pwdlen]))

a = input("")
