



def Display(iNo):

    for i in range(1, iNo+1):
        print(" * ")

def main():
    iValue = int(input("Enter number to print * : "))

    Display(iValue)

if __name__ =="__main__":
    main()