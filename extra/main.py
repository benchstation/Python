import time
print("\n" * 3)


print("Upper case alphabet table:")
print()
print("Code - Char")
time.sleep(0.4)
for ind in range(65,91):
    print(ind, "-", chr(ind)*(91 - ind))
time.sleep(0.08)
time.sleep(0.5)
# Cool star effect
l = "*** *** *** *** ***"
star = l * 300
print(star)

# This is not working currently, but it should print stylized text. Including bold and colored text.
print('\033[1;31;43mHello,World!')

N = 1
for i in range(65, 91):
   print(chr(i) * N)
   N += 1
