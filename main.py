# การวิเคราะห์การลงทุน

import numpy_financial as npf


def format_row_data(data):
    tint = "{:,.0f}"
    tfloat = "{:,.2f}"
    tpercent = "{:.0f}%"
    templates = [tint, tint, tint, tint, tint, tint, tint, tpercent, tfloat, tpercent]
    return [templates[idx].format(value) for idx, value in enumerate(data)]


def stream_lines_from_file(file_name, mode='r'):
    with open(file_name, mode) as f:
        for line in f:
            yield line


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
}
display_width = sum(col_widths.values())
thin_line = '-' * display_width
thick_line = '=' * display_width
row_template = '{:>{idw}}{:>{icw}}{:>{y1w}}{:>{y2w}}{:>{y3w}}{:>{y4w}}{:>{y5w}}{:>{yrw}}{:>{npvw}}{:>{irrw}}'
headers = ['#', 'Initial Capital', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', 'Yield Rate', 'NPV', 'IRR']

print(thick_line)
print(row_template.format(*headers, **col_widths))
print(thin_line)

for line in stream_lines_from_file('Data_ลงทุน.txt', 'r'):
    raw_data = [float(part) for part in line.split()]
    raw_data[1] = -raw_data[1]
    cash_flows = raw_data[1:7]
    yield_percent = raw_data[7]
    npv = npf.npv(yield_percent / 100, cash_flows)
    irr = npf.irr(cash_flows)
    irr_percent = int(round(irr * 100))
    row_data = raw_data + [npv, irr_percent]
    formatted_row_data = format_row_data(row_data)
    print(row_template.format(*formatted_row_data, **col_widths))

print(thick_line)
