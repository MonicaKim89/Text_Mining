import re
import sys
from konlpy.tag import Okt
okt = Okt()


def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def stemming (text):
    morphs_list = []
    one_words = []
    result = []

    pos = okt.pos(text, join = True)
    # print(pos)
    for j in pos:
        if j.split('/')[1] == 'Noun':
            j = j.split('/')[0]
            morphs_list.append(j)
                    
        elif j.split('/')[1] =='Adjective':
            k = okt.morphs(j,  stem= True)
            k = k[0]
            morphs_list.append(k)
        elif j.split('/')[1] =='Verb':
            v = okt.morphs(j,  stem= True)
            v = v[0]
            morphs_list.append(v)

    for i in morphs_list:
        if len(i) != 1:
            one_words.append(i)
    

    for i in one_words:
        if i not in stopwords:
            result.append(i)

    return result