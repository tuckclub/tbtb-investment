def show(label, value):
    print(f'{label:>50}: {value}')


tint = '{:,.0f}'
tfloat = '{:,.2f}'
tpercent = '{:.0f}%'
tbool = '{}'

show('tint', tint)
show('tfloat', tfloat)
show('tpercent', tpercent)
show('tbool', tbool)

print('-' * 100)

show('tint.format(12.34567)', tint.format(12.34567))
show('tint.format(120000000000.34567)', tint.format(120000000000.34567))

print('-' * 100)

show('tfloat.format(12.34567)', tfloat.format(12.34567))
show('tfloat.format(120000000000.34567)', tfloat.format(120000000000.34567))

print('-' * 100)

show('tpercent.format(10)', tpercent.format(10))
show('tpercent.format(10.45)', tpercent.format(10.45))
