import math

# Some random values
valueA = 11.2829850
valueB = 19.2545879
valueC = 0.50000001
valueD = 34.6403001
valueE = -9.9121138

# Truncate values (throw away the fractional part)
truncA = math.trunc(valueA)
truncB = math.trunc(valueB)
truncC = math.trunc(valueC)
truncD = math.trunc(valueD)
truncE = math.trunc(valueE)

# Output the results
print(valueA, "truncated =", truncA)
print(valueB, "truncated =", truncB)
print(valueC, "truncated =", truncC)
print(valueD, "truncated =", truncD)
print(valueE, "truncated =", truncE)