
def FhtoCs(fTemp):
    Celsius = ((fTemp - 32) * (5/9))

    return Celsius
def main():

    fValue = float(input("Enter temperature inn Fahrenheit : "))
    dRet = FhtoCs(fValue)

    print(f"Celsius is  : {dRet:.4f}")


if __name__ == "__main__":
    main()