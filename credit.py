from cs50 import get_string

s = get_string("Number: ")
n = len(s)
total = 0
for i in range(n - 1, -1, -1):
    d = int(s[i])
    total += d if (n - i) % 2 else (d * 2 if d * 2 < 10 else d * 2 - 9)

if total % 10 != 0:
    print("INVALID")
elif n == 15 and s[:2] in ["34", "37"]:
    print("AMEX")
elif n == 16 and 51 <= int(s[:2]) <= 55:
    print("MASTERCARD")
elif n in [13, 16] and s[0] == "4":
    print("VISA")
else:
    print("INVALID")