# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from nltk.probability import FreqDist
# from nltk.tokenize import RegexpTokenizer

from hazm import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# from nltk.corpus import stopwords
from hazm import Normalizer
# import nltk.data


class Summarizer(object):
    def __init__(self):
        self.normalizer = Normalizer()

    def summarize(self, input, num_sentences=2):
        self.input = self.normalizer.normalize(input)
        return self._get_summarize(num_sentences)

    def _get_summarize(self, num_sentences):
        base_words = [word for word in word_tokenize(self.input)]
        words = [word for word in base_words] #if str(word not in stopwords.words()]
        word_frequencies = FreqDist(words)

        most_frequent_words = [pair[0] for pair in
            word_frequencies.items()[:100]]
        
  
        working_sentences = sent_tokenize(self.input)
        actual_sentences = sent_tokenize(self.input)

        output_sentences = []

        for word in most_frequent_words:
            for i in range(0, len(working_sentences)):
                if (word in working_sentences[i]
                  and actual_sentences[i] not in output_sentences):
                    output_sentences.append(actual_sentences[i])
                    break
                if len(output_sentences) >= num_sentences: break
        
            if len(output_sentences) >= num_sentences: break

        return self._reorder_sentences(output_sentences)

    def _reorder_sentences(self, output_sentences):
        output_sentences.sort(lambda s1, s2:
            self.input.find(s1) - self.input.find(s2))
        return output_sentences
