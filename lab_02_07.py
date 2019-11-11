MY_BASE = 12
reverals = {'F':15, 'E':14, 'D':13, 'C':12, 'B':11,'A':10}
back = {15:'F', 14:'E', 13:'D', 12:'D', 11:'B', 10:'A'}
def to_dec(x):
    res = 0
    for i in range(len(x)):
        res += (MY_BASE ** (len(x) - i - 1)) * ( int(x[i]) if not x[i] in reverals.keys() else reverals[x[i]])
    print(res)
    return res
def to_14(x):
    str_buf = ''
    while x > 0:
        str_buf += str(x % 14) if not x % 14 in back.keys() else back[x % 14]
        x //= 14
    return str_buf[::-1]


if __name__ == '__main__':
    print(to_14(to_dec(input('Enter a number: '))))
