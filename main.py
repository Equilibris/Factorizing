import numbers


print(numbers.Equation.fromSpecal(23,25,numbers.OpperationFactory.divide).factors)

n = numbers.Number.fromFloat(10)
n2 = numbers.Number.fromFloat(300)

print(n.value,n.fractData)
# print(n2.factors)
# n3 = n/100
# n3 = numbers.Fraction.fromSpecal(1000,10)

f = n / n2

print(f.value, f.fractData)

print(n.value,n2.value)

f = f/numbers.Number.fromFloat(9.21124)

print(f.value, f.fractData)


