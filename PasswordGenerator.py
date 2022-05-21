import string
import random


def main(size):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase 
    s3 = string.digits
    s4 = string.punctuation 

    password = []
    password.extend(list(s1))
    password.extend(list(s2))
    password.extend(list(s3))
    password.extend(list(s4))

    random.shuffle(password)
    print ("".join(password[0:length]))

    print (f'The password is: {password}')

if __name__ == '__main__':
    try:
        length = int(input("Enter the password length:\n"))
        main(length)
    except Exception as e:
        print ('Error! Invalid Value')