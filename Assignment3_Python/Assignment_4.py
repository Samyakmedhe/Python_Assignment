


def DisplayConvert (Cvalue):
    if 'A' <= Cvalue <= 'Z':
        print(Cvalue.lower())
    else:
        print(Cvalue.upper())
    print()
def main():
    
    print("Enter Character  : ")
    cValue = input().strip()
    DisplayConvert(cValue)

if __name__ =="__main__":
    main()