CupcakeInvoices = open('CupcakeInvoices.csv')
# for line in CupcakeInvoices:
# print(line)

# for line in CupcakeInvoices:
#     line = line.strip('\n').split(',')
# print(line)
# print(line[2])

# for line in CupcakeInvoices:
#     line = line.strip('\n').split(',')
#     print(float(line[3]) * float(line[4]))

total = 0

for line in CupcakeInvoices:
    line = line.split(',')
    total = total + (float(line[4]) * int(line[3]))

print(round(total, 2))


CupcakeInvoices.close()