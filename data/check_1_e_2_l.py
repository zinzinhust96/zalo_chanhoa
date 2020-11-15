import os
import glob
import json
import re
from bs4 import BeautifulSoup

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
# DROP_PATH = '/hdd/Zalo_Team_HoaChan/data/namdng/train_review'

json_paths = glob.glob(os.path.join(JSON_PATH, '*.json'))
# json_paths = ['/hdd/Zalo_Team_HoaChan/data/only_event/goal_info/460.json']

need_review = []

for index1, json_path in enumerate(json_paths):
    json_name = json_path.split('/')[-1]
    # print('\n{}'.format(json_path))
    f = open(json_path)
    doc = json.load(f)

    # need to review
    score_list = doc['match_summary']['score_list']

    ref_event_ids = [item['ref_event_ids'] for item in score_list]
    # # remove duplicate
    # no_dup_ref_event_ids = list(set(ref_event_ids))

    # if len(no_dup_ref_event_ids) != len(ref_event_ids):
    #     print(len(no_dup_ref_event_ids), len(ref_event_ids))
    #     print(json_name)
    #     need_review.append(json_name)

    # get duplicate item
    duplicate_items = get_items_that_duplicate_from_list(ref_event_ids)
    if len(duplicate_items) > 0:
        # further process
        print(duplicate_items)
        print(json_name)

# need_review = list(set(need_review))
# print(need_review, len(need_review))