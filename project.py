#function to convert str to int
def to_int(s):
    number = 0
    for char in s:
        number = number * 10 + ord(char) - ord('0')
    return number


#get data from a file
def get_data(lines):
    data = []
    for line in lines:
        line = line.replace('\n', '').split(' ')
        name = line[0] + ' ' + line[1]
        birth_date = line[2]
        pass_date = line[3]
        avrg_une = to_int(line[4]) + to_int(line[5]) + to_int(line[6])
        avrg_une /= 3
        data.append((name, birth_date, pass_date,line[4], line[5], line[6], avrg_une))
    return data


#sorting by birthday date
def sort_by_bd(data):
    for i in range(len(data)):
        for j in range(len(data)):
            #flags for every case. A person is younger if their bd is a larger number
            f1 = data[i][1].split('.')[2] > data[j][1].split('.')[2]
            f2 = data[i][1].split('.')[1] > data[j][1].split('.')[1]
            f3 = data[i][1].split('.')[0] > data[j][1].split('.')[0]
            f4 = data[i][1].split('.')[2] == data[j][1].split('.')[2]
            f5 = data[i][1].split('.')[1] == data[j][1].split('.')[1]
            if f1:
                data[i], data[j] = data[j], data[i]
            elif f4 and f2:
                data[i], data[j] = data[j], data[i]
            elif f4 and f5 and f3:
                data[i], data[j] = data[j], data[i]
    return data


#pretty output
def prettify(list):
    for item in list:
        print(item[0], ' | ', item[1], ' | ', item[2], ' | ', item[3], ' ', item[4], ' ', item[5], ' -> ', item[6])


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        prettify(sort_by_bd(get_data(f.readlines())))
