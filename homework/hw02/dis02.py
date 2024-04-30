x = 3
def p(rint):
    print(rint)
def g(x, y):
    if x:
        print("one")
    elif x:
        print(True, x) # Does x being truth-y affect the printed value?
    if y:
        print(True, y) # Does y being truth-y affect the printed value?
    else:
        print(False, y) # Does y being false-y affect the printed value?
    return print(p(y)) + x