
def PrintEven(iNo):
    if iNo <= 0 :
        return
    
    for iCnt in range(1,iNo):
        if iNo % iCnt == 0 and iCnt % 2 == 0 :
            print(iCnt)   
    print()
def main():
    iValue = 0
    print("Enter number : ",end=' ')
    iValue = int(input())
    PrintEven(iValue)


if __name__== "__main__":
    main()