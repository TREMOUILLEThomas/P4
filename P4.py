#ex 57
def test_Pythagore(a,b,c):
    if a**2+b**2==c**2:
        return True
    else:
        return False

#ex 58
def valeur_absolue(x):
    if x>0:
        return x
    else:
        return -x

#ex 60
def max2(a,b):
    if a>b:
        return a
    else:
        return b
    
#ex 61
def max3(a,b,c):
    return max2(c, max2(a,b))

#ex 62
def puissance(x,k):
    acc=1
    for i in range(k):
        acc=acc*x
    return acc
