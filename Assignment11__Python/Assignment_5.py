def Pattern(iNo):

    for iCnt in range(1, (iNo*2) +1):
        if iCnt % 2 == 0 :
            print(iCnt,end = " ")

    print(" ") 
    
def main():

    iValue = int(input("Enter Number : "))
    Pattern(iValue)

if __name__ == "__main__":
    main()