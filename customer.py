customer = input("What is your Name ? ")
print(f"Hi {customer}  Nice to meet you")

if len(customer) < 3:
    print("Name is short")
elif len(customer) > 10:
    print("name is too long")
else:
    print("Name looks good")
budget = input("What is your Budget ? ")
if int(budget) < 1000:
    print("Too low")
else:
    print("Enjoy shopping")
