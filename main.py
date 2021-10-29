# การวิเคราะห์การลงทุน

def calculate_npv(cfs, k, i):
    summ = 0
    for index, cf in enumerate(cfs):
        t = index + 1
        value = cf / (1 + k) ** t
        summ += value
    return summ - i


line_length = 136
thin_line = '-' * line_length
thick_line = '=' * line_length
print(thick_line)

template = '{0:>3}{1:>20}{2:>15}{3:>15}{4:>15}{5:>15}{6:>15}{7:>15}{8:>15}'
print(template.format(
    '#', 'Initial Capital', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', 'Yield Rate', 'NPV'))

print(thin_line)

file = open('Data_ลงทุน.txt', 'r')
line = file.readline()

while line:
    data = [int(part) for part in line.split()]
    real_eastate_number = data[0]
    initial_capital = data[1]
    year1 = data[2]
    year2 = data[3]
    year3 = data[4]
    year4 = data[5]
    year5 = data[6]
    yield_rate = data[7]
    cfs = [year1, year2, year3, year4, year5]
    npv = calculate_npv(cfs, yield_rate / 100, initial_capital)
    template = '{0:>3,}{1:>20,}{2:>15,}{3:>15,}{4:>15,}{5:>15,}{6:>15,}{7:>15,}{8:>15,.2f}'
    print(template.format(*data, npv))
    line = file.readline()

print(thick_line)
