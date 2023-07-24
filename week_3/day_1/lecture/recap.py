# Recap topics:
### Lambda
### General problem/solution tackling

thousands_a = 100
thousands_b = 500

print(thousands_a * 1000)
print(thousands_b * 1000)

# Much simpler, quicker
# But don't overuse or use it for complex stuff
# It will just confuse everyone
ab = lambda p: print(p * 1000)
ab(thousands_a)
ab(thousands_b)

# Mystery operator!
# Walrus
# :=


# Too long, takes too much time, we're lazy
def convert_to_thousands(thousands):
    print(thousands * 1000)
