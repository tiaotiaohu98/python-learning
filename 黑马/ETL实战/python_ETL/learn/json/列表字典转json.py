import json

dict1 = {'id':'1','name':'Tom','age':'23','gender':'male','register_date':'2023-11-10'}
print(json.dumps(dict1))
print(type(json.dumps(dict1)))

json_str = '{"id":"1","name":"Tom","age":"23","gender":"male","register_date":"2023-11-10"}'
dict1 = json.loads(json_str)
print(dict1)
print(type(dict1))