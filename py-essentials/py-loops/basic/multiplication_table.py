def main():
   while True:
      print("-" * 30)
      print("Menu")
      print("1 - make a multiplication table")
      print("2 - Leave")
      print("-" * 30)
      input_user = int(input("Choice:"))
   
      if input_user == 2:
         print("Bye Bye")
         break
      if input_user == 1:
         input_table_user = int(input("What number do you want? "))
         result_table = multiplication_table(input_table_user)
         print(result_table)

 
def multiplication_table(number):
   result = ""
   for i in range (0, 11):
       result += f"{number} x {i} = {number * i}\n" 
   return result

main()


# Example simple without functions and while true
number_input = int(input("Qual número você deseja para a tabuada? "))

for i in range(0, 11):
    resultado = number_input * i
    print(f"{number_input} x {i} = {resultado}")