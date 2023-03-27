user_input = input('Enter List')

new_list = user_input.split(',')

result = []

for item in new_list:
    result.append(int(item))



for num in result:
    if(num % 2) == 0:
        print(num)

user_input = input("enter list")
new_list = user_input.split("a")
result = []
for num in new_list:
    if (int(num) % 2) == 0:
        result.append(int(num))
print(result)
