
def FactRev(iNo):  
    iCnt = iNo  
    for iCnt in range(1,iNo):
        if iNo % iCnt != 0:
            print(iCnt,end=" ")
    print()
def main():
    iValue = 0
    print("Enter number : ",end=' ')
    iValue = int(input())
    FactRev(iValue)

if __name__== "__main__":
    main()