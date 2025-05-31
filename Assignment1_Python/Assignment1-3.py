
def Display(iNo):

    for i in range (iNo, 0 , -1 ):
        print(i)

def main():

    iValue = int(input("Enter number : "))

    Display(iValue)


if __name__ == "__main__":
    main()