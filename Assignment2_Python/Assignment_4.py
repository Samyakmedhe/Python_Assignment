


def Display(iNo1 , iNo2):
    for iCnt in range(iNo2):
        print(iNo1,end =" ")
    print()
def main():
    iValue1 = 0
    iValue2 = 0 
    print("Enter first number : ")
    iValue1 = int(input())

    print("Enter Second number : ")
    iValue2 = int(input())
    Display(iValue1 , iValue2)

if __name__ =="__main__":
    main()