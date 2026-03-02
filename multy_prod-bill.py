print('\t CROMA RETAIL.')
date = '02/03/2026'
products = [
    ('laptop', 1, 56734),
    ('Mobile', 2, 26500),
    ('TV 43 ', 3, 44444)
    ]
name = 'Aditya'
mob  = 9964190499


print(f"\t\t\t {date}")
print('------------------------------------')
print('\tCustomer Details\n')
print(f"Customer Name - {name}\nMobile no - {mob}")

print('------------------------------------')

print(f"product name\tQnt\tprice\tTotal\n")

grand_total = 0
for prod,qnt,pric in products:
    total = qnt * pric
    grand_total += total
    print(f"{prod}\t\t{qnt}\t{pric}\t{qnt*pric}")
print('---------------------------------------')
print(f"Grand total\t\t\t{grand_total}\n")
print('------------------------------------')
print('\tThank You\n\tVisit again:)')