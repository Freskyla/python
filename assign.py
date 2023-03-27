my_list = [11, 12, 13, 14, 16, 17, 20,  24,  26,  28, 29, 30]
for num in my_list:
    if num > 2 and num % 2 == 0:
       print(num)
    #elif all(num % i != 0 for i in range(2, int(num**0.5)+1)):
        #print(num, "is prime")
    #else: 
       # print(num, "is neither prime nor even")

          
        


