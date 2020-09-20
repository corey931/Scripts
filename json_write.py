import json
import yaml

data = {}
data['people'] = []
data['people'].append({
    'name':'Celia',
    'job':'Crazy',
    'from':'Island'
})
data['hobbies'] = []


with open('json_write.txt','w') as file:
    json.dump(data, file, indent=4)

with open('json_write.txt') as file:
    fi = json.load(file)
    print(type(fi))
    fi = json.dumps(fi, sort_keys=True, indent=4)
    print(fi)


print('-----------------\nJSON TO YAML\n-----------------\n')
# yaml.dump(data)

# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/