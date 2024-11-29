
#default arguments
#def add(num1,num2=5):
 #   return num1+num2

#print(add(3))

def sum_of_numbers(list_of_num,filter_func=None):
    sum_of_n = 0
    if filter_func is not None:
        res = filter_func(list_of_num)
        for i in res:
            sum_of_n += i

    else:
        for j in list_of_num:
            sum_of_n += j
    return sum_of_n

def even(data):
    evn_list = []                    
    for i in data:
        if i % 2 == 0:
            evn_list.append(i)
    return evn_list

def odd(data):
    odd_list = []            
    for i in data:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list
sample_data = range(1,11)

print(sum_of_numbers(sample_data,even))