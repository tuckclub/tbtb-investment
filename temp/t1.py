def show(label, value):
    print(f'{label:>25}: {value}')


line = '1 200000	60000	60000	50000	60000	50000	6'

text_data = line.split()
show('text_data', text_data)

raw_data = [float(part)
            for part in text_data]
show('raw_data', raw_data)

data_list = []
for part in text_data:
    f = float(part)
    data_list.append(f)
show('data_list', data_list)

raw_data[1] = -raw_data[1]
show('raw_data', raw_data)

show('raw_data[7]', raw_data[7])
cash_flows = raw_data[1:7]  # list slice
show('raw_data[1:7]', raw_data[1:7])
show('cash_flows', cash_flows)

#  | 5 | 6 | 7 | 8 | 9 |
#  0   1   2   3   4   5
# -5  -4  -3  -2  -1

ls = [5, 6, 7, 8, 9]
l1 = ls[1:4]
show('ls', ls)
show('l1', l1)
show('ls[2]', ls[2])
show('ls[2:]', ls[2:])
show('ls[:4]', ls[:4])
show('ls[:]', ls[:])
show('ls', ls)
show('ls[1:5]', ls[1:5])
show('ls[1:10]', ls[1:10])
show('ls[-2]', ls[-2])
show('ls[1:-2]', ls[1:-2])
show('ls[-4:-1]', ls[-4:-1])
show('ls[:-1]', ls[:-1])
show('ls[0:-1]', ls[0:-1])
