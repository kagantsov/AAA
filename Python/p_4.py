class Pokemon:
    def __init__(self, name, category, weaknesses: tuple):
        self.name = name
        self.category = category
        self._weaknesses = weaknesses

    def get_weaknesses(self):
        return self._weaknesses[0]

bulbasaur = Pokemon(
   name='Bulbasaur',
   category='seed',
   weaknesses=('fire', 'psychic', 'flying', 'ice'))

print(bulbasaur.get_weaknesses())