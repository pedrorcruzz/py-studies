input_user = int(input("Choice your number: "))

result = 1
for i in range (1, input_user + 1):
   result *=i
   print(result)

print(f"{input_user}! = {result}")
   
   
   