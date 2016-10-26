import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DATA_ROOT = os.path.join(PROJECT_ROOT, 'data')

MODEL_ROOT = os.path.join(DATA_ROOT, 'model')
BATCH_GENERATOR_FILE = os.path.join(MODEL_ROOT, 'batch_gen.pkl')
MODEL_FILE = os.path.join(MODEL_ROOT, 'model.h5')
W2V_READER_FILE = os.path.join(MODEL_ROOT, 'w2v_reader.pkl')

TEST_ROOT = os.path.join(DATA_ROOT, 'test')
TEST_FILE = os.path.join(TEST_ROOT, 'test.txt')

TRAINING_ROOT = os.path.join(DATA_ROOT, 'training')
TRAINING_FILE = os.path.join(TRAINING_ROOT, 'training.txt')

WORD2VEC_ROOT = os.path.join(DATA_ROOT, 'word2vec')

MIDNAMES_FILE = os.path.join(DATA_ROOT, 'mid', 'mid_name_types.tsv')
WORD2VEC_TXT_FILE = os.path.join(WORD2VEC_ROOT, 'w2v.txt')

STANFORD_NER_FOLDER = os.path.join(PROJECT_ROOT, 'stanford-ner-2014-08-27')
# [LOCATION, PERSON, ORGANIZATION]
STANFORD_NER_CLASSIFIER_3C = os.path.join(STANFORD_NER_FOLDER, 'classifiers', 'english.all.3class.distsim.crf.ser.gz')
# [LOCATION, PERSON, ORGANIZATION, MISC]
STANFORD_NER_CLASSIFIER_4C = os.path.join(STANFORD_NER_FOLDER, 'classifiers', 'english.conll.4class.distsim.crf.ser.gz')
STANFORD_NER_JAR = os.path.join(STANFORD_NER_FOLDER, 'stanford-ner.jar')  # can be set in CLASSPATH=

EVALUATOR_LOG_FILE = os.path.join(DATA_ROOT, 'evaluation', 'evaluation.txt')
