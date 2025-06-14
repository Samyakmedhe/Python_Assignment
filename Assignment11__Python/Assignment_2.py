def Pattern(iNo):

    for iCnt in range(iNo, 0 , -1):
        print(iCnt," # ",end = " ")

    print(" ") 
    
def main():

    iValue = int(input("Enter Number : "))
    Pattern(iValue)

if __name__ == "__main__":
    main()