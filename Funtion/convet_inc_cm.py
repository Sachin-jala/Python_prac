def inch_to_cms(inch):
    return inch*2.54
try:
    n = float(input("Enter value in inch: "))
    print(f"Value in cm is: {inch_to_cms(n)}")
except ValueError:
    print("Please enter a valid numeric value.")