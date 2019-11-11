'''
Логические операции
'''
def to_bin(s):
    bin_s = ''
    while s != 0:
        bin_s += str(s % 2)
        s //= 2
    return bin_s[::-1]

f = True
g = False
print("f: ", f)
print("not f: ", not f)
print("f and g: ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g: ", f != g)
print("\n")
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h <= i: ", 0 < h <= i)
print("\n\n")
'''
9Побитовые операции
'''
j = 7
k = 20
print("j = %d; j in binary format: %s" % (j, bin(j))
)
print("k = %d; k in binary format: %s" % (k, bin(k))
)
print("j & k: %d; binary: %s" % (j & k, bin(j & k)) )
# побитовое AND
print("j | k: %d; binary: %s" % (j | k, bin(j | k)) )
# побитовое OR
print("j ^ k: %d; binary: %s" % (j ^ k, bin(j ^ k)) )
# побитовое XOR
print("~k: %d; binary: %s" % (~k, bin(~k)) ) #
#инверсия двоичного числа
print("k>>1: %d; binary: %s" % (k>>1, bin(k>>1)) ) #
#сдвиг на один бит вправо
print("k<<1: %d; binary: %s" % (k<<1, bin(k<<1)) ) #
#сдвиг на один бит влево
print("\n\n")

# Задание 9
a = 42
b = 1337
c = True
d = False

#Задание 10
print(not (c and d))
print(c and d or(not (c and d)))
print(not (c or d))
print("A <= B", a <= b)
print("A>B ∨ A==B", a>b or a == b)
print("¬(A<B)", not (a<b))
s = 154
p = 6
print("s (dec): ", s)
print("p (dec): ", p)
print("s (bin): ", to_bin(s))
print("p (bin): ", to_bin(p))
s ^= p
print("s xor p (dec): ", s)

print("s xor p (bin): ", to_bin(s))

s = s << 2
p = p << 2
print("s << 2", s)
print("p << 2", p)
print("s << 2", to_bin(s))
print("p << 2", to_bin(p))
