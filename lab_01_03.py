'''
Форматированный ввод/вывод данных
'''
MY_BASE = 4
def to_dec(x):
    res = 0
    for i in range(len(x)):

        res += (MY_BASE ** (len(x) - i - 1)) * int(x[i])
    return res
m = 10
pi = 3.1415927
print("m = ",m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {:4}, pi = {:.3f}".format(m,pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")
print("m = {:4}, pi = {:.3f}".format(m,pi))
print("m = %4d, pi = %.3f" % (m, pi))
year  = input("Enter your year of study: ")
print(year)
r1, m1, p1 = input("Enter your unt scores in format \"r m p\", where letters are your scores \
in Russian, Maths, Additional subject: ").split()
print("scores are %s %s %s" % (r1, m1, p1))
numbers = input("Enter a series of 12-digit numbers, separated with ' ': ").split()
for number in numbers:
    dec_number = to_dec(number)
    print(number, " = ", dec_number)
    print(dec_number << 1)
    print(dec_number >> 1)
