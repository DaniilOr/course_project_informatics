reverals = {'F':15, 'E':14, 'D':13, 'C':12, 'B':11,'A':10}
back = {15:'F', 14:'E', 13:'D', 12:'D', 11:'B', 10:'A'}
def reverse_code(x):
    if not x[0] == 'F':
        return x
    else:
        inversed = []
        for i in x:
            if i in reverals.keys():
                inversed.append(15 - reverals[i])
            else:
                inversed.append(15 - int(i))
        inversed = inversed[::-1]
        inversed[0] += 1
        for i in range(len(inversed)):
            if i < len(inversed) - 1:
                inversed[i + 1] += (inversed[i] // 16)
            inversed[i] %= 16
        for i in range(len(inversed)):
            if inversed[i] in back.keys():
                inversed[i] = back[inversed[i]]

        return inversed[::-1]
if __name__ == '__main__':
    print(reverse_code('F0682'))
    print(reverse_code('CFFF1111'))
