def add_sum(x, y, z):
    return x + y + z


s1 = add_sum(1, 2, 3)
print(s1)
s2 = add_sum(10, 20, 30)
print(s2)
# Positional arguments
def print_it(*args):
    for var in args:
        print(var, end="")


print_it(10)
print_it(10, 3.14)
print_it(10, 3.14, "Sicilian")
print_it(10, 3.14, "Silician", "Punekar")
