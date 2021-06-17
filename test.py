import json
  

with open('C:/SAI KUMAR/srujana/test.json') as json_file:
    data = json.load(json_file)
print("Type:", type(data))
#print("Data:", data)
for item in data['panels']:
    d = {'target': 1}
    d['querylist'] = d.pop('target')
    print(d)
    

        



