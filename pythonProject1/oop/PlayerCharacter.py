class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def run():
        print('run')


player1 = PlayerCharacter('Kevin', 35)
player2 = PlayerCharacter('LeBron', 39)

# print(player1)
# print(player2)

help(player1)
