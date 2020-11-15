import json

jsonl_content = open('/hdd/Zalo_Team_HoaChan/data/train/train.jsonl', 'r').readlines()
# print(len(jsonl_content))

results = [json.loads(jline) for jline in jsonl_content]

n_file = len(results)

for result in results:
    print(result['original_doc']['_source']['original_url'])
# for i in range(n_file):
#     with open('{}.json'.format(i), 'w', encoding='utf8') as outfile:
#         json.dump(results[i], outfile, ensure_ascii=False)
