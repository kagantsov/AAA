def count_letters(word: str) -> tuple[int, int]:
    letters_count = 0
    for x in word:
        if x.isalpha():
            letters_count = letters_count + 1
    return letters_count, len(word) - letters_count

class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


def test_cont_letters():
    word = "Hello world!"
    res = count_letters(word)
    assert res == (10, 2), f"input: {word}, expected (10, 2), got: {res}"
    word = "."
    res = count_letters(word)
    assert res == (0, 1), f"input: {word}, expected (0, 1), got: {res}"
    word = "Hello"
    res = count_letters(word)
    try:
        assert res == (0, 4), f"input {word}, expected (0, 4), got: {res}"
    except AssertionError:
        pass


if __name__ == '__main__':
    test_cont_letters()
    name = 'Bulbasaur'
    poketype = 'grass'
    assert (x := Pokemon(name, poketype).__str__()) == f'{name}/{poketype}', \
        f'Test for {name}/{poketype} failed as {x}'
    name = 'Pikachu'
    poketype = 'electric\r\npower'
    assert (x := Pokemon(name, poketype).__str__()) == f'{name}/{poketype}', \
        f'Test for {name}/{poketype} failed as {x}'
    name = 'Squirtle'
    poketype = 'water' * 30
    assert (x := Pokemon(name, poketype).__str__()) == f'{name}/{poketype}', \
        f'Test for {name}/{poketype} failed as {x}'
    print('All tests passed successfully')
