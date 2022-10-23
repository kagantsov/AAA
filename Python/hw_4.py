from math import log

from hw_3 import CountVectorizer


class TfidfTransformer:
    """Term frequency = количество повторений слова / общее количество слов"""

    @staticmethod
    def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
        """Term frequency = количество повторений слова / общее количество слов"""
        freq_list: list[list[float]] = []
        for vector in count_matrix:
            freq_list.append([freq / sum(vector) for freq in vector])
        return freq_list

    @staticmethod
    def idf_transform(count_matrix: list[list[int]]) -> list[float]:
        """Inverse document-frequency = ln(количество документов + 1 / документов со словом + 1)"""
        idf: list[float] = []
        docs_count = zip(*count_matrix)
        for element in range(len(count_matrix[0])):
            current_sum = sum([1 for x in next(docs_count) if x])
            idf.append(log((len(count_matrix) + 1) / (current_sum + 1)) + 1)
        return idf

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """tf-idf transformer = tf * idf"""
        tf_matrix: list[list[float]] = self.tf_transform(count_matrix)
        idf_matrix: list[float] = self.idf_transform(count_matrix)
        tf_idf_matrix: list[list[float]] = []
        for vector in tf_matrix:
            tf_vector: list[float] = []
            idf_vector = zip(vector, idf_matrix)
            for tf, idf in idf_vector:
                tf_vector.append(round(tf * idf, 2))
            tf_idf_matrix.append(tf_vector)
        return tf_idf_matrix


class TfifdVectorizer(CountVectorizer):
    """Класс, объединяющий в себе функции CountVectorizer и TfidfTransformer"""

    def __init__(self):
        super().__init__()
        self.tfidf = TfidfTransformer()

    def fit_transform(self, text_corpus: list[str]) -> list[list[float]]:
        count_matrix: list[list[int]] = super().fit_transform(text_corpus)
        return self.tfidf.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus: list[str] = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfifdVectorizer()
    count_matrix: list[list[float]] = vectorizer.fit_transform(corpus)
    assert count_matrix == [[0.2, 0.2, 0.29, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0.14, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
    print(count_matrix)
