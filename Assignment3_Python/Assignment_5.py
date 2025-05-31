
def CheckEven(iNo):
    if iNo == 'A' or iNo == 'E' or iNo == 'I' or iNo == 'O' or iNo == 'U' or iNo == 'a' or iNo == 'e' or iNo == 'i' or iNo == 'o' or iNo == 'u':
        return True
    else:
        return False  

def main():
    bRet = False

    cValue = input("Enter Charater : ")
    bRet = CheckEven(cValue)
    if bRet == True :
        print(cValue,"is Vowel ")
    else:
        print(cValue,"is Not Vowel")

if __name__ =="__main__":
    main()
