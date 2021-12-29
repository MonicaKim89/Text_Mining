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

def clean_text(text): 
    """ 한글, 영문, 숫자만 남기고 제거한다. 
    :param text: 
    :return: 
    """ 
    text = text.replace(".", " ").strip() 
    text = text.replace("·", " ").strip() 
    pattern = '[^ ㄱ-ㅣ가-힣|0-9|a-zA-Z]+' 
    text = re.sub(pattern=pattern, repl='', string=text) 
    return text 
    
def get_nouns(tokenizer, sentence): 
    """ 단어의 길이가 2이상인 일반명사(NNG),
     고유명사(NNP), 외국어(SL)만을 반환한다. 
     :param tokenizer: 
     :param sentence: :return: """ 
    tagged = tokenizer.nouns(sentence)
    nouns = [s for s in tagged if len(s)>1] 
     
    return nouns 
     
     
def tokenize(df): 
    tokenizer = okt
    processed_data = [] 
    for sent in tqdm(df['cleaned_reviews']):
        sentence = clean_text(sent.replace('\n', '').strip()) 
        processed_data.append(get_nouns(tokenizer, sentence)) 
        
    return processed_data
    
    
def save_processed_data(processed_data): 
    """ 토큰 분리한 데이터를 csv로 저장 :param processed_data: :return: """ 
    
    with open('lsa_token_pos.csv', 'w', newline='', encoding='utf-8') as f: 
        writer = csv.writer(f) 
        for data in processed_data:
             writer.writerow(data)
             
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