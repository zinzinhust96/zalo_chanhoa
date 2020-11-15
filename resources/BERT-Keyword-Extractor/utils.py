from nltk.tokenize import sent_tokenize

'''
def convert(key, filekey, train_path):
    sentences = ""
    for line in open(train_path + "/" + filekey[key], 'r'):
        sentences += (" " + line.rstrip())
    print('sentences: ', sentences)
    tokens = sent_tokenize(sentences)   # Return a sentence-tokenized
    # print('tokens: ', tokens)
    key_file = open(train_path + "/" + str(key),'r')
    keys = [line.strip() for line in key_file]
    key_sent = []
    labels = []
    for token in tokens:
        z = ['N'] * len(token.split())
        # z ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
        input()
        for k in keys:
            if k in token:
                
                if len(k.split())==1:
                    try:
                        z[token.lower().split().index(k.lower().split()[0])] = 'B'
                    except ValueError:
                        continue
                elif len(k.split())>1:
                    try:
                        if token.lower().split().index(k.lower().split()[0]) and token.lower().split().index(k.lower().split()[-1]):
                            z[token.lower().split().index(k.lower().split()[0])] = 'B'
                            for j in range(1, len(k.split())):
                                z[token.lower().split().index(k.lower().split()[j])] = 'I'
                    except ValueError:
                        continue
        for m, n in enumerate(z):
            if z[m] == 'I' and z[m-1] == 'N':
                z[m] = 'N'

        if set(z) != {'N'}:
            labels.append(z) 
            key_sent.append(token)
    return key_sent, labels
'''

def convert(key, filekey, train_path):
    sentences = ""
    for line in open(train_path + "/" + filekey[key], 'r'):
        sentences += (" " + line.rstrip())
    tokens = sent_tokenize(sentences)
    key_file = open(train_path + "/" + str(key),'r')
    keys = [line.strip() for line in key_file]
    key_sent = []
    labels = []
    for token in tokens:
        z = ['O'] * len(token.split())
        for k in keys:
            if k in token:
                
                if len(k.split())==1:
                    try:
                        z[token.lower().split().index(k.lower().split()[0])] = 'B'
                    except ValueError:
                        continue
                elif len(k.split())>1:
                    try:
                        if token.lower().split().index(k.lower().split()[0]) and token.lower().split().index(k.lower().split()[-1]):
                            z[token.lower().split().index(k.lower().split()[0])] = 'B'
                            for j in range(1, len(k.split())):
                                z[token.lower().split().index(k.lower().split()[j])] = 'I'
                    except ValueError:
                        continue
        for m, n in enumerate(z):
            if z[m] == 'I' and z[m-1] == 'O':
                z[m] = 'O'

        if set(z) != {'O'}:
            labels.append(z) 
            key_sent.append(token)
    return key_sent, labels

