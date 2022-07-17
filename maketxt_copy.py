import json
import os
import tqdm

pathes=['/Users/test/Desktop/ocr_tr-labeling data']

to_write = ''

for file_path in pathes :
    for path in os.listdir(file_path):
        if '.json' not in path:
            continue
        with open(os.path.join(file_path, path), 'r', encoding="utf-8") as file:
            json_data = json.load(file)

        imagepath = json_data['image']['file_name']
        label = ''

        for text in json_data['text']['word']:
            label += text['value']

        to_write += str(imagepath+ '\t'+ label+ '\n')

    with open('./makingtxt/train_txt/gt.txt', 'w') as file:
        file.write(to_write)
        #여러파일 돌릴떄 사용 하는것! 위에 방식을봐라