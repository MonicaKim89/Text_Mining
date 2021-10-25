import pandas as pd
import numpy as np
import os
import matplotlib as plt
import seaborn as sns

#시각화
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline

from matplotlib import font_manager, rc
rc('font',family="Malgun Gothic")
plt.rcParams["font.family"]="Malgun Gothic" #plt 한글꺠짐
plt.rcParams["font.family"]="Arial" #외국어꺠짐
plt.rcParams['axes.unicode_minus'] = False # 마이너스 부호 출력 설정
plt.rc('figure', figsize=(20,10))

sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid') #sns 한글깨짐
#그래프 세팅
font = {'family': 'serif',
        'color':  'white',
        'weight': 'normal',
        'size': 16,
        }

#마이너스 폰트
plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정

#판다스 컬럼 다보기
pd.set_option('display.max_columns', 100)

#시각화?
import platform
platform.system()

# 운영체제별 한글 폰트 설정
if platform.system() == 'Darwin': # Mac 환경 폰트 설정
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': # Windows 환경 폰트 설정
    plt.rc('font', family='Malgun Gothic')

# 글씨 선명하게 출력하는 설정
%config InlineBackend.figure_format = 'retina'





import tensorflow as tf
from tensorflow.python.client import device_lib

import torch
print(torch.cuda.is_available())


import transformers
import tweepy
from tweepy import StreamListener
from tweepy import Stream
from konlpy.tag import Okt
from wordcloud import WordCloud






####setting####

SEED = 1337

def set_seeds(seed=SEED):
    os.environ['PYTHONHASHSEED']= str(seed)
    random.seed(seed)
    tf.random.set_seed(seed)
    np.random.seed(seed)

def set_global_determinism(seed=SEED):
    set_seeds(seed=seed)
    os.environ['TF_DETERMINISTIC_OPS']= '1'
    os.environ['TF_CUDNN_DETERMINISTIC']= '1'
    tf.config.threading.set_inter_op_parallelism_threads(1)
    tf.config.threading.set_intra_op_parallelism_threads(1)

# Call the above function with seed value
set_global_determinism(seed=SEED)
gpu_check()

### konlpy Jpype문제 해결 https://daewonyoon.tistory.com/386
### JAVA_HOME https://liveyourit.tistory.com/56
