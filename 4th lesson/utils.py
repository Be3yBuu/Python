import sys
from currency_module import currency_rates

print(currency_rates(sys.argv[0])[0])
for i in range(1, len(sys.argv)):
    print(currency_rates(sys.argv[i])[2], currency_rates(sys.argv[i])[1])
