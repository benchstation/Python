# Receive input value in US dollars and show the conversion to euro and Brazillian real
# Entry -> Dollars (USD)
# Output -> Euro and reais (BRL)
# Output must round up the numeric value to two decimal places

#     Input     				Output  

# 	Dollar : 5.00                Real : 25					
# 								Euro : 4.80

# As of June 04 (2023), 1 dollar is equivalent to 4.96 reais and equivalent to 0.93 euros.

real = 0
euro = 0

dollar = float(input("Enter a value in dollar to convert:\n"))

dollar_to_real = dollar * 4.96
dollar_to_euro = dollar * 0.93

print(f"Dollar: {dollar: .2f}\nReal: {dollar_to_real: .2f}\nEuro: {dollar_to_euro: .2f}")
