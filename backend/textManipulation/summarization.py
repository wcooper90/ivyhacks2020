from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import nltk
nltk.download('punkt')

from UserInputs import UserInputs
from inputs.article_scraper import url_text_conversion, collect_text


# default summarization for text
def summarize_text(text, num_sentences):
    LANGUAGE = "english"
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    # use text rank as default
    summarizer = TextRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    result = ''
    counter = 0
    for sentence in summarizer(parser.document, num_sentences):

        counter += 1
        # if counter > num_sentences / 2:
        #     break
        # print(sentence)
        result += ' ' + str(sentence)


    title = 'to be implemented'
    return result, title


# adjust to summarize speech better
def summarize_speech_transcription(text, num_sentences):
    body = text
    model = Summarizer()
    result = model(body, num_sentences=num_sentences)
    result = ''.join(result)
    title = 'to be implemented'
    return result, title


# summarization for an article
def summarize_article_text(url, num_sentences):
    LANGUAGE = "english"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    # parser = PlaintextParser.from_string("Check this out.", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    result = ''
    for sentence in summarizer(parser.document, num_sentences):
        result += str(sentence)
    title = 'to be implemented'
    return result, title
