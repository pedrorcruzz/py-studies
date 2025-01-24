input_user = int(input("Put your number: "))

a, b = 0, 1

while a <= input_user:
    print(a)
    a, b = b, a + b

# Example with for
for _ in range(input_user):
    print(a)
    a, b = b, a + b
