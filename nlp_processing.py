import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.python.client import device_lib

import torch
print(torch.cuda.is_available())


import transformers
import tweepy
from tweepy import StreamListener
from tweepy import Stream
from konlpy.tag import Okt







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
