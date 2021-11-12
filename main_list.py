# การวิเคราะห์การลงทุน

import statistics
import numpy_financial as npf

headers = ['#', 'Investment', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', 'Discount Rate',
           'NPV', 'IRR', 'Suggestion']

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
    tintpercent = '{:.0f}%'
    ttext = '{}'
    templates = [tint, tint, tint, tint, tint, tint, tint, tintpercent, tfloat, tintpercent, ttext]
    # before [1.0, -200000.0,   60000.0,  60000.0,  50000.0,  60000.0,  50000.0,  6.0,  36873.052574959205, 13,   True]
    # after  ['1', '-200,000', '60,000', '60,000', '50,000', '60,000', '50,000', '6%', '36,873.05',       '13%', 'True']
    return [templates[idx].format(value) for idx, value in enumerate(data_list)]


def select_col_elements(list_of_lists, col_idx):
    return [row[col_idx]
            for row in list_of_lists
            if len(row) > col_idx]


row_data_list = []

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
        suggestion = 'Invest' if worth_investing else "Don't Invest"
        row_data = raw_data + [npv, irr_percent, suggestion]
        row_data_list.append(row_data)
        formatted_row_data = format_row_data(row_data)
        print(row_template.format(*formatted_row_data))

print(thin_line)

npvs = select_col_elements(row_data_list, 8)
npv_min = min(npvs)
npv_max = max(npvs)
npv_mean = statistics.mean(npvs)
npv_stdev = statistics.stdev(npvs, npv_mean)
t_npv = '{:>15}{:>15,.2f}'
print(t_npv.format('NPV Min:', npv_min))
print(t_npv.format('NPV Max:', npv_max))
print(t_npv.format('NPV Mean:', npv_mean))
print(t_npv.format('NPV STDEV:', npv_stdev))

print(thin_line)

irrs = select_col_elements(row_data_list, 9)
irr_min = min(irrs)
irr_max = max(irrs)
irr_mean = statistics.mean(irrs)
irr_stdev = statistics.stdev(irrs, irr_mean)
t_irr = '{:>15}{:>14,.0f}%'
t_irr_float = '{:>15}{:>14,.2f}%'
print(t_irr.format('IRR Min:', irr_min))
print(t_irr.format('IRR Max:', irr_max))
print(t_irr_float.format('IRR Mean:', irr_mean))
print(t_irr_float.format('IRR STDEV:', irr_stdev))

print(thick_line)
print()
