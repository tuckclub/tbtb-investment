# การวิเคราะห์การลงทุน

import numpy_financial as npf

headers = ['#', 'Investment', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', 'Discount Rate', 'NPV', 'IRR', 'Worth']

num_std_cols = len(headers) - 1
row_template = '{:>3}' + '{:>15}' * num_std_cols
line_length = 3 + 15 * num_std_cols
thin_line = '-' * line_length
thick_line = '=' * line_length

print(thick_line)
print(row_template.format(*headers))
print(thin_line)


def format_row_data(data_list):
    tint = '{:,.0f}'
    tfloat = '{:,.2f}'
    tpercent = '{:.0f}%'
    tbool = '{}'
    templates = [tint, tint, tint, tint, tint, tint, tint, tpercent, tfloat, tpercent, tbool]
    # before [1.0, -200000.0,   60000.0,  60000.0,  50000.0,  60000.0,  50000.0,  6.0,  36873.052574959205, 13,   True]
    # after  ['1', '-200,000', '60,000', '60,000', '50,000', '60,000', '50,000', '6%', '36,873.05',       '13%', 'True']
    return [templates[idx].format(value) for idx, value in enumerate(data_list)]


with open('Data_ลงทุน.txt', 'r') as data_file:
    for line in data_file:
        raw_data = [float(part) for part in line.split()]
        raw_data[1] = -raw_data[1]
        cash_flows = raw_data[1:7]
        discount_rate_percent = raw_data[7]
        discount_rate = discount_rate_percent / 100
        npv = npf.npv(discount_rate, cash_flows)
        irr = npf.irr(cash_flows)
        irr_percent = int(round(irr * 100))
        worth_investing = npv > 0 and irr_percent > discount_rate_percent
        row_data = raw_data + [npv, irr_percent, worth_investing]
        formatted_row_data = format_row_data(row_data)
        print(row_template.format(*formatted_row_data))

print(thick_line)
