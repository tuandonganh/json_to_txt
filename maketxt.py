import json
import os

file_path="./ocr_tr_labeling_data"

with open(file_path, 'r', encoding="UTF8") as file:
    json_data = json.load(file)

imagepath = json_data['bbox']['file_name']
label = ''
for text in json_data['text']['word']:
    label += text['value']

to_write = str(imagepath+ '\t'+ label+ '\n')

with open('gt.txt', 'w') as file:
    file.write(to_write)