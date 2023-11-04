mantissa = 1 + int("10110011001100110011001", 2) * 2 ** (-23)
exp = int("1111111", 2)

apprx = mantissa * 2 ** (exp - 127)
print(f"Przybliżenie 1.7: {apprx}")
print(f"Błąd względny: {abs(apprx - 1.7)}")
print(f"Błąd bezwzględny: {abs(apprx - 1.7)/1.7}")
