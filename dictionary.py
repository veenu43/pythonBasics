my_empty_dict={}
print('dict: {}, type: {}'.format(my_empty_dict,type(my_empty_dict)))

test={1,2,3}
print('data: {}, type: {}'.format(test,type(test)))

user_details={"name":"Vinit","age":33}
print(user_details)

user_details["loc"]="mumbai"
print(user_details)

user_details["name"]="kumar"
print(user_details)

user_details1={}

for i in range(3):
    key= input("enter key")
    value= input("enter value")
    user_details1[key]= value

print(user_details1)