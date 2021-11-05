import numpy_financial as npf


def show(label, value):
    print(f'{label:>25}: {value}')


line = '1 200000	60000	60000	50000	60000	50000	6'

text_list = line.split()
show('text_list', text_list)

raw_data = [float(part) for part in text_list]
show('raw_data', raw_data)

raw_data[1] = -raw_data[1]
show('raw_data', raw_data)

cash_flows = raw_data[1:7]
show('cash_flows', cash_flows)

discount_rate_percent = raw_data[7]
show('discount_rate_percent', discount_rate_percent)

discount_rate = discount_rate_percent / 100
show('discount_rate', discount_rate)

npv = npf.npv(discount_rate, cash_flows)
show('npv', npv)

irr = npf.irr(cash_flows)
show('irr', irr)

show('irr * 100', irr * 100)
show('round(irr * 100)', round(irr * 100))

irr_percent = int(round(irr * 100))
show('irr_percent', irr_percent)

worth_investing = npv > 0 and irr_percent > discount_rate_percent
show('worth_investing', worth_investing)

row_data = raw_data + [npv, irr_percent, worth_investing]
show('row_data', row_data)


def format_row_data(data):
    tint = '{:,.0f}'
    tfloat = '{:,.2f}'
    tpercent = '{:.0f}%'
    tbool = '{}'
    templates = [tint, tint, tint, tint, tint, tint, tint, tpercent, tfloat, tpercent, tbool]
    return [templates[idx].format(value) for idx, value in enumerate(data)]


formatted_row_data = format_row_data(row_data)
show('formatted_row_data', formatted_row_data)
