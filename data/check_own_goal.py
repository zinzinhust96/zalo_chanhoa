import os
import glob
import json
import re
from bs4 import BeautifulSoup
import shutil

def get_items_that_duplicate_from_list(dup_list):
    seen = {}
    dupes = []

    for item in dup_list:
        if item not in seen:
            seen[item] = 1
        else:
            if seen[item] == 1:
                dupes.append(item)
            seen[item] += 1

    return dupes

JSON_PATH = '/hdd/Zalo_Team_HoaChan/data/only_event/goal_info'
DROP_PATH = '/hdd/Zalo_Team_HoaChan/data/only_event/own_goal'

json_paths = glob.glob(os.path.join(JSON_PATH, '*.json'))
# json_paths = ['/hdd/Zalo_Team_HoaChan/data/only_event/goal_info/460.json']

need_review = []

for index1, json_path in enumerate(json_paths):
    json_name = json_path.split('/')[-1]
    # print('\n{}'.format(json_path))
    f = open(json_path)
    doc = json.load(f)

    # need to review
    body = doc['original_doc']['_source']['body']

    for item in body:
        if "đốt lưới" in item['text'] or "phản lưới" in item['text']:
            shutil.copy2(os.path.join(JSON_PATH, json_name), os.path.join(DROP_PATH, json_name))