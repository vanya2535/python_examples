from os.path import join
# JSON
import json


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}


with open(join('files', 'data_file.json'), 'w') as write_file:
    json.dump(data, write_file, indent=4)

with open(join('files', 'data_file.json'), 'r') as json_file:
    print(json.load(json_file))