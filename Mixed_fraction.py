from fractions import Fraction

# Helper function: Mixed → Improper Fraction
def mixed_to_improper(whole, numerator, denominator):
    return Fraction(whole * denominator + numerator, denominator)

# Helper function: Improper Fraction → Mixed Fraction
def improper_to_mixed(frac):
    whole = frac.numerator // frac.denominator
    remainder = frac.numerator % frac.denominator
    if remainder == 0:
        return f"{whole}"
    elif whole == 0:
        return f"{remainder}/{frac.denominator}"  # fraction
    else:
        return f"{whole} {remainder}/{frac.denominator}"  # Mixed fraction

# User Input
print("Enter first mixed fraction:")
w1 = int(input("Whole number: "))
n1 = int(input("Numerator: "))
d1 = int(input("Denominator: "))

print("\nEnter second mixed fraction:")
w2 = int(input("Whole number: "))
n2 = int(input("Numerator: "))
d2 = int(input("Denominator: "))

# Convert to Improper Fractions
frac1 = mixed_to_improper(w1, n1, d1)
frac2 = mixed_to_improper(w2, n2, d2)

# Addition
sum_frac = frac1 + frac2

# Output
print("\nSum as Improper Fraction:", sum_frac)
print("Sum as Mixed Fraction:", improper_to_mixed(sum_frac))
