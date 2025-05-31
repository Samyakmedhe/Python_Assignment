def Table(iNo):
    for iCnt in range(10, iNo-iNo , -1):
        print(iCnt * iNo,end=" ")

    print(" ")

    
def main():
    
    iValue = int(input("Enter number : "))
    Table(iValue)

    
if __name__ =="__main__":
    main()