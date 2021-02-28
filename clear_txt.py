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


nltk.download('stopwords')
__WPT = nltk.WordPunctTokenizer()
__stop_words_list = nltk.corpus.stopwords.words('turkish')
__stop_words_list += ["migros", "g", "kg", "ml", "l", "cm",
                      "x", "li", "lı", "ay", "lü"]

__TAG_RE = re.compile(r'<[^>]+>')


def html_totext(text):
    return html2text(text)


def remove_tags(text):
    return __TAG_RE.sub(' ', text)


def remove_undefine_words(text):
    text = text.replace('&;nbsp;', ' ')
    text = text.replace('\n', ' ')
    text = text.replace('8&;#39', "'")
    text = text.replace('&lt', '')
    text = text.replace('p&gt;', '')
    text = text.replace('strong&gt;', ' ')
    text = text.replace('&;amp;', '&')
    text = text.replace('&;#39;', r'\ ')
    text = text.replace('&;', '')
    text = text.replace('nbsp;', ' ')
    text = text.replace('//', ' ')
    text = text.replace(' /', ' ')
    return text


def remove_html(text):
    txt = remove_undefine_words(text)
    txt = html_totext(text)
    txt = remove_tags(txt)
    return txt.strip()


def lower_letters(txt):
    txt = txt.replace("İ", "i")
    return txt.lower()


def resub_comma(txt):
    return txt.replace(",", " ")


def remove_stopwords(txt):
    return ' '.join([word for word in txt.split()
                     if word.strip() not in __stop_words_list 
                     and len(word) > 1]) 


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
    txt = remove_undefine_words(txt)
    txt = remove_tags(txt)
    txt = lower_letters(txt)
    txt = resub_comma(txt)
    txt = remove_punctuation(txt)
    txt = remove_integer(txt)
    txt = remove_repeatedLetter(txt)
    txt = just_one_word(txt)
    txt = remove_stopwords(txt)
    return txt


def main():
    pass

if __name__ == "__main__":
    main()
