from cal import MagicCal

if __name__ == '__main__':
    val1 = input("Pleas enter first number: ")
    val2 = input("Please type the operator [A,B,C,D] :")
    if val2=='A':
        result=MagicCal(val1,0)
        print(result.doublenum())
    elif val2=='B':
        val3 = input("Pleas enter second number: ")
        result=MagicCal(val1,val3)
        print(result.add())
    elif val2=='C':
        val3 = input("Pleas enter second number: ")
        result=MagicCal(val1,val3)
        print(result.subract())
    elif val2=='D':
        result=MagicCal(val1,0)
        print(result.precentage())