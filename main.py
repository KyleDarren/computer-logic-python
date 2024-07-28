def AND(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def OR(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def NOT(a):
    if a == 1:
        return 0
    else:
        return 1
    
def XOR(a, b):
    return AND(NOT(AND(a, b)), OR(a, b))
    
def NAND(a, b):
    return NOT(AND(a, b))

def NOR(a, b):
    return NOT(OR(a, b))

def XNOR(a, b):
    return NOT(XOR(a, b))
    
def HALF_ADDER(a, b):
    arr = []

    arr.append(AND(a,b))
    arr.append(XOR(a, b))

    return arr

def FULL_ADDER(a, b, c):
    A = HALF_ADDER(a, b)
    B = HALF_ADDER(c, A[1])
    C = OR(A[0], B[0])

    return [C, B[1]]

def THREE_BIT_ADDER(a, b):    
    A = HALF_ADDER(a[2], b[2])
    B = FULL_ADDER(a[1], b[1], A[0])
    C = FULL_ADDER(a[0], b[0], B[0])
    
    return [C[0], C[1], B[1], A[1]]

def EIGHT_BIT_ADDER(a, b):
    A = HALF_ADDER(a[7], a[7])
    B = FULL_ADDER(a[6], b[6], A[0])
    C = FULL_ADDER(a[5], b[5], B[0])
    D = FULL_ADDER(a[4], b[4], C[0])
    E = FULL_ADDER(a[3], b[3], D[0])
    F = FULL_ADDER(a[2], b[2], E[0])
    G = FULL_ADDER(a[1], b[1], F[0])
    H = FULL_ADDER(a[0], b[0], G[0])

    return [H[0], H[1], G[1], F[1], E[1], D[1], C[1], B[1], A[1]]
