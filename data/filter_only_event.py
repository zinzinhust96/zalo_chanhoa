import os
import glob
import json
import re
from bs4 import BeautifulSoup

JSON_PATH = '/hdd/Zalo_Team_HoaChan/data/train'
DROP_PATH = '/hdd/Zalo_Team_HoaChan/data/namdng/train_review'

json_paths = glob.glob(os.path.join(JSON_PATH, '*.json'))

for index1, json_path in enumerate(json_paths):
    json_name = json_path.split('/')[-1]
    # print('\n{}'.format(json_path))
    f = open(json_path)
    doc = json.load(f)

    # need to review these two
    html_annotations = doc['html_annotation']
    body = doc['original_doc']['_source']['body']

    new_html_annotations = []
    new_body = []

    # score_list = doc['match_summary']['score_list']

    # print('html_annotations: ', html_annotations)

    for anno in html_annotations:
        soup = BeautifulSoup(anno)
        events = soup.find_all("span", {"class": "tag"})
        for e in events:
            new_html_annotations.append(str(e))
            new_body.append({
                "content": e.text,
                "text": e.text,
                "type": "text"
            })
    
    doc['html_annotation'] = new_html_annotations
    doc['original_doc']['_source']['body'] = new_body

    # save new json file
    with open(os.path.join(DROP_PATH, json_name), 'w', encoding='utf8') as outfile:
        json.dump(doc, outfile, ensure_ascii=False)

# need_review = list(set(need_review))
# print(need_review, len(need_review))