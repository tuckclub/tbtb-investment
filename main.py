# การวิเคราะห์การลงทุน

import numpy_financial as npf

default_col_width = 13
col_widths = {
    'idw': 3,
    'icw': 17,
    'y1w': default_col_width,
    'y2w': default_col_width,
    'y3w': default_col_width,
    'y4w': default_col_width,
    'y5w': default_col_width,
    'yrw': default_col_width,
    'npvw': default_col_width,
    'irrw': default_col_width,
    'wthw': default_col_width,
}
display_width = sum(col_widths.values())
thin_line = '-' * display_width
thick_line = '=' * display_width
row_template = '{:>{idw}}{:>{icw}}{:>{y1w}}{:>{y2w}}{:>{y3w}}{:>{y4w}}{:>{y5w}}' \
               '{:>{yrw}}{:>{npvw}}{:>{irrw}}{:>{wthw}}'
headers = ['#', 'Initial Capital', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5',
           'Yield Rate', 'NPV', 'IRR', 'Worth']

print(thick_line)
print(row_template.format(*headers, **col_widths))
print(thin_line)


def format_row_data(data):
    tint = '{:,.0f}'
    tfloat = '{:,.2f}'
    tpercent = '{:.0f}%'
    tbool = '{}'
    templates = [tint, tint, tint, tint, tint, tint, tint, tpercent, tfloat, tpercent, tbool]
    return [templates[idx].format(value) for idx, value in enumerate(data)]


with open('Data_ลงทุน.txt', 'r') as data_file:
    for line in data_file:
        raw_data = [float(part) for part in line.split()]
        raw_data[1] = -raw_data[1]
        cash_flows = raw_data[1:7]
        yield_percent = raw_data[7]
        npv = npf.npv(yield_percent / 100, cash_flows)
        irr = npf.irr(cash_flows)
        irr_percent = int(round(irr * 100))
        worth_investing = npv > 0 and irr_percent > yield_percent
        row_data = raw_data + [npv, irr_percent, worth_investing]
        formatted_row_data = format_row_data(row_data)
        print(row_template.format(*formatted_row_data, **col_widths))

print(thick_line)
