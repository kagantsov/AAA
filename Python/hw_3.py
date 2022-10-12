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


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    assert count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    print(count_matrix)
    feature_list = vectorizer.get_feature_names()
    assert feature_list == ['crock', 'pot', 'pasta', 'never',
                            'boil', 'again', 'pomodoro', 'fresh',
                            'ingredients', 'parmesan', 'to', 'taste']
    print(feature_list)
