
def Odd(iNo):  
    for iCnt in range(1,iNo):
        if iCnt % 2 != 0:
            print(iCnt)
def main():
    iValue = 0
    print("Enter number : ",end=' ')
    iValue = int(input())
    Odd(iValue)
    
if __name__== "__main__":
    main()