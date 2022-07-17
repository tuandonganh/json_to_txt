from __future__ import annotations
import json
import os
from tkinter import image_names


file_path ="./ocr_tr-labeling_data"
for pathes in os.listdir(file_path) :

    with open(os.path.join(file_path,pathes), 'r', encoding="UTF8") as file :
        json_data = json.load(file)
    label =''
    for data in json_data['annotations']['bbox']:
        imagepath = ['images'][0]['file_name']
        label += data['bbox']
        f = str(imagepath + '\t' + label + '\n')

    with open('./gt.txt', 'w') as file :

        file.write(f)