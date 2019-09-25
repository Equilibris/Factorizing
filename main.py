import numbers

n = numbers.Number.fromFloat(10)
n2 = numbers.Number.fromFloat(30)

print(n.value,n.fractData)
# print(n2.factors)
# n3 = n/100
# n3 = numbers.Fraction.fromSpecal(1000,10)

f = n/n2

print(f.value, f.fractData)

f = f/numbers.Number.fromFloat(9)

print(f.value, f.fractData)


