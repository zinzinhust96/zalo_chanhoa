import os

TEXT_DATA = '/hdd/namtp/zalo_ai/data/data.txt'
BY_CLASS_TEXT_PATH = '/hdd/Zalo_Team_HoaChan/data/divided_by_classes'

CLASSES = ['match_info', 'card_info', 'substitution', 'match_result', 'goal_info']

with open(TEXT_DATA, 'r') as fread:
    lines = fread.readlines()

lines = [l.strip() for l in lines]

for line in lines:
    sentence, class_types = line.split('<xxx>')
    # print(sentence, class_types)
    for c in CLASSES:
        if c in class_types:
            with open(os.path.join(BY_CLASS_TEXT_PATH, '{}.txt'.format(c)), 'a') as fwrite:
                fwrite.write(sentence + '\n')