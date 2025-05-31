def Pattern(iNo):
    ch = 'A'

    for iCnt in range(iNo):
        print(ch, end= " ")
        ch = chr(ord(ch)+ 1)
    
def main():

    iValue = int(input("Enter Number : "))
    Pattern(iValue)

if __name__ == "__main__":
    main()