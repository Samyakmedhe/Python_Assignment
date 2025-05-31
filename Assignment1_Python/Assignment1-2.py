
def Display(iNo):

    for i in range (1 ,iNo+1):
        print(i,": Marvellous...")

def main():

    iValue = int(input("Enter number : "))

    Display(iValue)


if __name__ == "__main__":
    main()