import yaml

data = [{'Name' : ['Chechi', 'Chely', 'Celia', 'Cutie']},
        {'Hobby' : ['Drawing', 'Netflix', 'Instagram', 'Spend time with the Tootie']}]

with open('yaml_write.txt','w') as file:
    yaml.dump(data, file)

with open('yaml_write.txt') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)
    print(yaml.dump(doc, sort_keys=True, indent=4))

# https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/

print('-----------------\nYAML TO JSON\n-----------------\n')
with open('yaml_write.txt') as file:
    print(yaml.load(file, Loader=yaml.FullLoader))