from math import log
from typing import List


class CountVectorizer():
    """Преобразовывает входной текст в матрицу, заключающую количества вхождения слов в текст"""

    def __init__(self, delimiter: str = ' '):
        self.delimiter = delimiter
        self.feature_names = []

    def get_feature_names(self) -> List[str]:
        """Получить список слов"""
        if len(self.feature_names) == 0:
            raise ValueError('The list of words is empty.')
        return self.feature_names

    def fit_transform(self, corpus) -> List[List[int]]:
        """Создать спискок слов по полученной матрице"""
        self._features(corpus)
        return self._count_matrix(corpus)

    def _features(self, corpus) -> None:
        """Разбить слова и в правильном порядке добавить их в список"""
        new_feature_names = []
        feature_names = [word.lower() for text in corpus for word in text.split()]
        for word in feature_names:
            if word not in new_feature_names:
                new_feature_names.append(word)
        self.feature_names = list(new_feature_names)

    def _count_matrix(self, corpus) -> List[List[int]]:
        """Посчитать встречаемость слов"""
        matrix = []
        for text in corpus:
            matrix.append([])
            for word in self.feature_names:
                text_words = [word.lower() for word in text.split()]
                matrix[-1].append(text_words.count(word))

        return matrix


class TfidfTransformer:
    def tf_transform(self, matrix: list[list[int]]) -> list[list[float]]:
        freq_list = []
        sum_word = 0
        for one_list in matrix:
            sum_word = sum(one_list)
            sentence_tf = []
            for number in one_list:
                freq = number / sum_word
                sentence_tf.append(freq)
            freq_list.append(sentence_tf)
        return freq_list

    def idf_transform(self, matrix: list[list[int]]) -> list[float]:
        docs_count = len(matrix)
        colm_len = len(matrix[0])
        idf = []
        for i in range(colm_len):
            counter = 0
            for doc in matrix:
                if doc[i] != 0:
                    counter += 1
            idf.append(log((docs_count + 1) / (counter + 1)) + 1)
        return idf

    def count_pos(self, matrix: list[int]) -> int:
        counter = 0
        for elem in matrix:
            if elem > 0:
                counter += 1
        return counter

    def fit_transform(self, matrix: list[list[int]]) -> list[list[float]]:
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        tf_idf: list[list[float]] = [[x * y for x, y in zip(row, idf)] for row in tf]

        return tf_idf

abc = [i > 0 for i in [1, 2, 3, 0]]

count_matrix_1: list[int] = [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0]

count_matrix: list[list[int]] = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

pos_numb = list(filter(bool, count_matrix_1))

if __name__ == '__main__':
    transformer = TfidfTransformer()
    tf_idf = transformer.tf_transform(count_matrix)
    print(tf_idf)

