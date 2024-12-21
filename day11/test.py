import math

n = 1234
logged = math.log10(n)
print(n)
digits = int(logged) + 1
antilogged = 10 ** logged
print(antilogged)
