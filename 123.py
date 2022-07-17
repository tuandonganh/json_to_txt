import json
import os

file_path="ocr_val-labeling"

with open('validatelabel/gt.txt', 'w') as gtfile:
    for pathes in os.listdir(file_path) :
        with open(os.path.join(file_path,pathes), 'r', encoding="UTF8") as file :
            json_data = json.load(file)
            filename = json_data['images'][0]['file_name']
            label = ''
            for data in json_data['annotations']:
                label += data['text']
            gtfile.write('' + filename + '\t' + label + '\n')
