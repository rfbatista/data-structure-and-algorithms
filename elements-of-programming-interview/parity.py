# In mathematics, parity is the property of an integer of whether it is even or odd.
# An integer is even if it is a multiple of two, and odd if it is not.
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def parity_2(x):
    result = 0
    while x:
        result ^= 1
        print('before: ' + "{0:b}".format(x))
        x &= x - 1 # erase the lowest set bit
        print('after: ' + "{0:b}".format(x))
    return result

print(parity_2(12600))
