user_number = int(input("Write a whole number and discover if it is a prime number"))

def main():

    for i in range(2, user_number // 2):
        if(user_number % i) == 0:
            print(user_number, "is not a prime number")
            break      
        else:
            print(user_number, "is a prime number")

if __name__ == "__main__":
    main()
