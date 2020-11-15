from bs4 import BeautifulSoup
import os
import glob

import json

jsonl_content = open('/hdd/Zalo_Team_HoaChan/data/train/train.jsonl', 'r').readlines()
# print(len(jsonl_content))

event_type_list = []

json_results = [json.loads(jline) for jline in jsonl_content]

for doc in json_results:

    for html in doc["html_annotation"]:

        soup = BeautifulSoup(html)

        events = soup.find_all("span", {"class": "tag"})

        for e in events:

            # print("event_type:", e["data"])

            # print("event_id:", e["event_id"])

            # print("text:", e.text)

            event_type_list.extend(e["data"].split(':'))

# set of events
event_type_set = set(event_type_list)
print('event_type_set: ', event_type_set)