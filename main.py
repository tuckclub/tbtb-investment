# การวิเคราะห์การลงทุน

def calculate_npv(cfs, k, i):
    summ = 0
    for index, cf in enumerate(cfs):
        t = index + 1
        value = cf / (1 + k) ** t
        summ += value
    return summ - i


default_column_width = 13
column_widths = {
    'idw': 3,
    'icw': 17,
    'y1w': default_column_width,
    'y2w': default_column_width,
    'y3w': default_column_width,
    'y4w': default_column_width,
    'y5w': default_column_width,
    'yrw': default_column_width,
    'npvw': default_column_width,
}
line_length = sum(column_widths.values())
thin_line = '-' * line_length
thick_line = '=' * line_length
print(thick_line)

head_template = '{0:>{idw}}{1:>{icw}}{2:>{y1w}}{3:>{y2w}}{4:>{y3w}}{5:>{y4w}}{6:>{y5w}}' \
                '{7:>{yrw}}{8:>{npvw}}'
data_template = '{0:>{idw}}{1:>{icw},}{2:>{y1w},}{3:>{y2w},}{4:>{y3w},}{5:>{y4w},}{6:>{y5w},}' \
                '{7:>{yrw},}{8:>{npvw},.2f}'

print(head_template.format(
    '#', 'Initial Capital', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', 'Yield Rate', 'NPV', **column_widths))

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
    print(data_template.format(*data, npv, **column_widths))
    line = file.readline()

print(thick_line)
