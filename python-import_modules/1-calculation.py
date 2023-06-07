#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    a = 10
    b = 5
    addres = add(a, b)
    addsub = sub(a, b)
    adddiv = div(a, b)
    addmul = mul(a, b)
    bbc = "{} {} {} = {}"
    print(bbc.format(a, "+", b, addres))
    print(bbc.format(a, "-", b, addsub))
    print(bbc.format(a, "*", b, addmul))
    print(bbc.format(a, "/", b, adddiv))
