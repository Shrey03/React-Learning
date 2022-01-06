# 1 printing each elements in list  and checking it is 1 or not
my_value = [1,2,3,2,3,1,1,1,0,-1,-2]
even_value = [1,2,4,6,82,23,12,25,75,9]
my_name = ['Shrey', 'Heli','yash','kuchi']
my_dict = {'a1':1,'a2':2,'a3':23,'a4':13,'a5':24}

# for val in my_value:
#     if (val == 1):
#         print (val , "THISSS IS 1!!")
#     else:
#         print(val , "this is not 1..lol!")


# 2 check the even number given from the string 

# for val in even_value:
#     if (val%2 == 0):
#         print(val , "this is even")

#     else:
#         print(val , "this is odd!!")


# 3 check the name from the list and count the length of string 

# for name in my_name:
#     print(name , len(name))


# 3 check the name from the list and capitalize all letters

# for name in my_name:
#     new_name = name.upper()
#     print(new_name)

# 3 check the name from the list and capitalize only 3rd letters

# for name in my_name:
#     new_name = name[0:2:]+name[2].upper() + name[3:]

#     print(new_name)

for k,v in my_dict.items():
    print(v)