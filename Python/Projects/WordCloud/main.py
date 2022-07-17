#!/usr/bin/env python3
"""
created: 2022-05-07 21:43:53
@author: seraph776
contact: seraph776@gmail.com
project: Word Cloud; The Raven
metadoc: This wordcloud was created using a dictionary with words and word frequencies from teh poem
         The Raven by Edgar Allan Poe
license: MIT License
"""


import os
import re
from collections import Counter
from wordcloud import WordCloud


def get_file(filename):
    with open(filename, encoding='utf-8') as fo:
        content = [i.lower().strip() for i in fo]
    return ' '.join(content)


def clean_file(data):
    data = re.sub(r'[^\w\s]', '', data)
    stopwords = ('a', 'an', 'and', 'as', 'at', 'but', 'by', 'from', 'he', 'him', 'i', 'is', 'my', 'of', 'or',
                 'on', 'said', 'that', 'the', 'there', 'this', 'to', 'with')
    return Counter([word for word in data.split() if word not in stopwords])


def generate_wordcloud(data):
    return WordCloud(height=800, width=1200).generate_from_frequencies(data)


def save_wordcloud(data, filename):
    data.to_file(os.path.join(filename))
    print(f'{filename} has been successfully saved.')


def main():
    raven_path = os.path.join('the_raven.txt')
    raven_file = get_file(raven_path)

    process_file = clean_file(raven_file)
    raven_cloud = generate_wordcloud(process_file)
    save_wordcloud(raven_cloud, 'raven_cloud.jpg')


if __name__ == '__main__':
    main()
