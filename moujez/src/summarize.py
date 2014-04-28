# -*- coding: utf-8 -*-
import math

from nltk.probability import FreqDist
from nltk.corpus import stopwords
from hazm import sent_tokenize, word_tokenize
from hazm import Normalizer


class Summarizer(object):

    def __init__(self):
        self.normalizer = Normalizer()

    def summarize(self, input):
        self.input = self.normalizer.normalize(input)
        self.base_words = word_tokenize(self.input)
        self.working_sentences = sent_tokenize(self.input)
        self.sentences_number = len(self.working_sentences)
        return self._get_summarize(num_sentences=self._find_num_sentences())

    def _find_num_sentences(self):
        return (int(math.log(self.sentences_number) ** 2 + 1) + 1) if self.sentences_number >= 6 else self.sentences_number
        # return int(self.sentences_number - 0.2 * self.sentences_number)

    def _get_summarize(self, num_sentences):
        # if str(word not in stopwords.words()]
        words = [word for word in self.base_words if word not in stopwords.words('persian')]
        word_frequencies = FreqDist(words)

        most_frequent_words = [pair[0] for pair in
                               word_frequencies.items()[:100]]

        actual_sentences = sent_tokenize(self.input)
        output_sentences = []

        for word in most_frequent_words:
            for i in range(0, len(self.working_sentences)):
                if (word in self.working_sentences[i]
                        and actual_sentences[i] not in output_sentences):
                    output_sentences.append(actual_sentences[i])
                    break
                if len(output_sentences) >= num_sentences:
                    break

            if len(output_sentences) >= num_sentences:
                break

        return self._reorder_sentences(output_sentences)

    def _reorder_sentences(self, output_sentences):
        output_sentences.sort(lambda s1, s2:
                              self.input.find(s1) - self.input.find(s2))
        return output_sentences
