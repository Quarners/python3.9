"""
Merge and update operators to dict  data structure
"""

user_one = {
    "name":"Andrew ng",
    "age":40,
    "email":"andrewng@domain.com"
}

user_update = {

  "name":"Andrew",
    "age":39,
    "email":"andrew@domain.com",
    "is_online":True
}

#new  merge operator
merge_dict = user_one | user_update
print(merge_dict)

"""
Result:

{'name': 'Andrew', 'age': 39, 'email': 'andrew@domain.com', 'is_online': True}
"""



#new update operator

user_one |= user_update
#user_one update
print(user_one)

"""
Result:
{'name': 'Andrew', 'age': 39, 'email': 'andrew@domain.com', 'is_online': True}

"""

a = {'farhad':1, 'blog':2, 'python':3}
b = {'farhad':'malik', 'topic':'python3.9'} 

a |= b

print(a)