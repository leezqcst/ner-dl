import string

from nltk.tokenize import word_tokenize, sent_tokenize


def tokenize_in_words(text):
    return word_tokenize(text.decode('utf-8'))


def tokenize_in_sentences(text):
    return sent_tokenize(text.decode('utf-8'))


# N.B. Remember that tokenization isn't a fully reversible process. Information is lost in tokenization.
def untokenize_words(tokens):
    return "".join([" " + i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()


def untokenize_words_custom(tokens):
    result = ' '.join(tokens)
    result = result.replace(' , ', ',')
    result = result.replace(' .', '.')
    result = result.replace(' !', '!')
    result = result.replace(' ?', '?')
    result = result.replace(' : ', ': ')
    result = result.replace(' \'', '\'')
    return result
