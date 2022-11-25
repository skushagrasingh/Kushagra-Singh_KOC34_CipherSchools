import random
def start():
    print("Program in which system pick random number from our range and tell that number is odd or even ,positive or negative and prime or composite number \n")
    a = int(input("Enter range"))
    b = int(input("Enter range upto what number"))
    x = random.randint(a, b)
    print("randomly picked number is", x)
    if x % 2 == 0:
        print(x, "is even number")
    else:
        print(x, "is odd number")
    if x > 0:
        print(x, "is positive number")
    elif x == 0:
        print(x, "is zero")
    else:
        print(x, "is negative number")
    if x > 1:
        for i in range(2, int(x / 2) + 1):
            if (x % i) == 0:
                print(x, "is not a prime number")
                break
        else:
            print(x, "is a prime number")
    else:
        print(x, "is composite number")
k=int(input("Enter 1 to start or enter any number to exit "))
while k==1:
    start()
    break
