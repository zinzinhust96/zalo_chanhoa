import os
import glob
import json
import re
from bs4 import BeautifulSoup
from utils import get_items_that_duplicate_from_list

JSON_PATH = '/hdd/Zalo_Team_HoaChan/data/only_event/goal_info'
DROP_PATH = '/hdd/Zalo_Team_HoaChan/resources/BERT-Keyword-Extractor/data'

CLASSES = ['match_info', 'card_info', 'substitution', 'match_result', 'goal_info']
# class_to_create = CLASSES[-1]
class_to_create = 'goal_info2'

if not os.path.exists(os.path.join(DROP_PATH, class_to_create)):
    os.makedirs(os.path.join(DROP_PATH, class_to_create))

json_paths = glob.glob(os.path.join(JSON_PATH, '*.json'))
# json_paths = ['/hdd/Zalo_Team_HoaChan/data/only_event/goal_info/385.json']

for json_path in json_paths:
    print('\n{}'.format(json_path))
    filename = json_path.split('/')[-1].split('.')[0]
    f = open(json_path)
    doc = json.load(f)
    html_annotations = doc['html_annotation']
    body = doc['original_doc']['_source']['body']
    score_list = doc['match_summary']['score_list']
    event_anno_dict = {}

    print('html_annotations: ', html_annotations)

    # for i, res in enumerate(list(search)):
    #     if res:
    #         event_id = res.group(2)
    #         print('event_id: ', event_id)
    #         event_anno_dict[event_id] = body[i]['text']

    for i, anno in enumerate(html_annotations):
        soup = BeautifulSoup(anno)
        events = soup.find_all("span", {"class": "tag"})
        for e in events:
            event_id = e["event_id"]
            print('event_id: ', event_id)
            event_anno_dict[event_id] = body[i]['text']

    print('event_anno_dict: ', event_anno_dict)

    ref_event_ids = [item['ref_event_ids'] for item in score_list]
    dupl_ref_event_ids = get_items_that_duplicate_from_list(ref_event_ids)
    not_dupl_score_list = [item for item in score_list if item['ref_event_ids'] not in dupl_ref_event_ids]

    counter = 0
    # for NOT duplicate items
    for score_item in not_dupl_score_list:
        key = '{} {}'.format(score_item['time'].strip(), score_item['player_name'].strip())
        with open(os.path.join(DROP_PATH, class_to_create ,'{}-{}.key'.format(filename, counter)), 'w') as fwrite:
            fwrite.write(key + '\n')

        text = ''
        ref_event_ids = score_item['ref_event_ids']
        print('ref_event_ids: ', ref_event_ids)
        for event_id in sorted(ref_event_ids.split(',')):
            if event_id in event_anno_dict.keys():
                text += event_anno_dict[event_id].strip() + '\n'
        # print('text: ', text)
        with open(os.path.join(DROP_PATH, class_to_create ,'{}-{}.txt'.format(filename, counter)), 'w') as fwrite:
            fwrite.write(text)

        # increment
        counter += 1

    # for DUPLICATE items
    for event_id in dupl_ref_event_ids:
        score_list_by_id = [item for item in score_list if item['ref_event_ids'] == event_id]

        key = ''
        for score_item in score_list_by_id:
            key += '{} {}\n'.format(score_item['time'].strip(), score_item['player_name'].strip())
        with open(os.path.join(DROP_PATH, class_to_create ,'{}-{}.key'.format(filename, counter)), 'w') as fwrite:
            fwrite.write(key + '\n')

        text = ''
        ref_event_ids = score_list_by_id[0]['ref_event_ids']
        for event_id in sorted(ref_event_ids.split(',')):
            if event_id in event_anno_dict.keys():
                text += event_anno_dict[event_id].strip() + '\n'
        # print('text: ', text)
        with open(os.path.join(DROP_PATH, class_to_create ,'{}-{}.txt'.format(filename, counter)), 'w') as fwrite:
            fwrite.write(text)

        # increment
        counter += 1

