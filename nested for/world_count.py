contries = ['India', 'US', "Australia", 'Japan', 'China', 'kajagistan', 'Iran', 'England', 'somalia', 'kuwet','mangolia','NetherLand','indoneshia']

count = 0
output = []
for cntr in contries:
    if cntr.startswith('I') or cntr.startswith('i'):
        count = count + 1
        output.append(cntr)

print('count of country starts with i is : ')
print('countries : ', output)