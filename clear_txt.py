#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:07:48 2021

@author: ademoguzhanozdemir
"""

#pip install html2text
import nltk
from html2text import html2text
import re
import itertools
import chardet 

nltk.download('stopwords')
WPT = nltk.WordPunctTokenizer()
stop_words_list = nltk.corpus.stopwords.words('turkish')
stop_words_list += ["migros", "reyondan", "orgnanik", "gezen", "boy", "küçük"]
TAG_RE = re.compile(r'<[^>]+>')

def html_totext(text):
    return html2text(text)


def remove_tags(text):
    return TAG_RE.sub(' ', text)


def lower_letters(txt):
    txt = txt.replace("İ", "i")
    return txt.lower()


def resub_comma(txt):
    return txt.replace(",", " ")


def remove_stopwords(txt):
    return ' '.join([word for word in txt.split()
                     if word.strip() not in stop_words_list]) 


def remove_punctuation(txt):
    return re.sub(r'[^\w\s]', ' ', txt)


def remove_repeatedLetter(txt):
     return (''.join(i for i, _ in itertools.groupby(txt)))
 

def remove_integer(txt):
    return ''.join([word for word in txt if not word.isdigit()])


def just_one_word(txt):
    new_txt = []
    for word in txt.split(' '):
        if word not in new_txt:
            new_txt.append(word)
    return ' '.join(new_txt)


def clean_text(txt):
    txt = html_totext(txt)
    txt = remove_tags(txt)
    txt = lower_letters(txt)
    txt = resub_comma(txt)
    txt = remove_punctuation(txt)
    txt = remove_stopwords(txt)
    txt = remove_integer(txt)
    txt = remove_repeatedLetter(txt)
    txt = just_one_word(txt)
    return txt

def main():
    pass

if __name__ == "__main__":
    main()
