import datetime
import time

from nerdl.dataset.taggers.cw_top275_tagger import CWTop275Tagger
from nerdl.dataset.taggers.figer_tagger import FigerTagger
from nerdl.dataset.taggers.stanford_four_tagger import StanfordFourTagger
from nerdl.ner.models.keras.keras_model import KerasNERModel
from settings import path_settings
from settings import settings

start = time.time()

################################################################################
# settings.MAX_SENTENCE_LEN
# settings.TAG2VEC_CLASS_LIST
# path_settings.WORD2VEC_TXT_FILE
# path_settings.TRAINING_FILE
# path_settings.TEST_FILE
# path_settings.TRAINING_CHECKPOINT_FILE
# path_settings.MODEL_FILE

settings.MAX_SENTENCE_LEN = 50

# settings.TAG2VEC_CLASS_LIST = settings.STANFORD_FOUR_CLASS_LIST
settings.TAG2VEC_CLASS_LIST = settings.FIGER_CLASS_LIST
# settings.TAG2VEC_CLASS_LIST = settings.CW_TOP275_CLASS_LIST

# path_settings.WORD2VEC_TXT_FILE = path_settings.CW_W2V_TXT_FILE.replace('.txt', '-old.txt')
# path_settings.WORD2VEC_TXT_FILE = path_settings.CW_W2V_TXT_FILE
# path_settings.TRAINING_FILE = path_settings.CW_TRAIN_FILE
# path_settings.TEST_FILE = path_settings.CW_TEST_FILE

path_settings.WORD2VEC_TXT_FILE = path_settings.FIGER_W2V_TXT_FILE
# path_settings.TRAINING_FILE = path_settings.FIGER_TRAIN_FILE
path_settings.TRAINING_FILE = path_settings.FIGER_TRAIN_FILE.replace('.tsv', '-top100k-lines.tsv')
path_settings.TEST_FILE = path_settings.FIGER_TEST_FILE

path_settings.TRAINING_CHECKPOINT_FILE = path_settings.TRAINING_FILE.replace('.tsv', '-checkpoint.tsv')

dt = datetime.datetime.now().isoformat()
path_settings.MODEL_FILE = path_settings.MODEL_FILE.replace('.h5', '_{}.h5'.format(dt))

# tagger = None
# tagger = StanfordFourTagger()
tagger = FigerTagger()
# tagger = CWTop275Tagger()

model = KerasNERModel(tagger=tagger)
model.train()
# REMEMBER TO CLEAN 'TRAINING_CHECKPOINT_FILE'
# PUT MODEL IN model-to-load.h5
# model.resume_train()
################################################################################

end = time.time()
print('{} seconds'.format(str(end - start)))
