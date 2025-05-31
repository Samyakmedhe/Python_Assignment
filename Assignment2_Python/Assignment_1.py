
def Display(iNo):
    for iCnt in range(iNo):
        print(" * ",end= " ")
    print()
def main():
    iValue = 0
    print("Enter number :" )
    iValue = int(input())
    Display(iValue)


if __name__== "__main__":
    main()