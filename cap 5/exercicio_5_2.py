def main() :
    a = float(input('a: '))

    b = float(input('b: '))
    
    c = float(input('c: '))

    n = float(input('a: '))
    return check_fermat(a, b, c, n)  

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")    


main()