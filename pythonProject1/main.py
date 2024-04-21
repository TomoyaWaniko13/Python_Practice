# print('hello!')
#

# name = input('What is your name?')
# print(name)

# print(type(2))
# print(type(False))
# print(type('Kevin'))

# print(9.9 + 0.1)
# print(5 // 4)
# print(6 % 4)

# items = ['notebooks', 'sunglasses', 'toys', 'grapes']
# print(items[0:1])
# print(items[0:3])
#
# print(items[0::1])
# print(items[0::2])

# items = ['notebooks', 'sunglasses', 'toys', 'grapes']
# sameItems = items
# sameItems[0] = 'apple'
# print(items)
# copiedItems = items[0:4]
# copiedItems[0] = 'apple'
# print(items)

# matrix = [
#     [1, 5, 1],
#     [0, 1, 0],
#     [1, 0, 1],
# ]
#
# print(matrix[0][2])

# tuple1 = (1, 2, 3, 4, 5) // immutable
# TypeError: 'tuple' object does not support item assignment
# tuple1[0] = 2

# tuple1 = (1, 2, 3, 4, 5)
# print(5 in tuple1)
# user = {
#     'basket': [1,2,3],
#     'greet': 'hello',
#     'age': 20
# }
#
# print(user.items())

# name = 'BOB'
# greeting = f'Hello,{name}'
#
# print(greeting)

# name = 'Bob'
# greeting = 'Hello, {}'
# with_name = greeting.format(name)
# print(with_name)

# local = ['Bob', 'Rolf', 'Anne']
# abroad = ['Bob','Anne']

# number = 7
# user_input = input('Would you like to play? (y/n)')
#
# while user_input != 'n':
#     user_number = int(input("Guess our number"))
#     if user_number == number:
#         print('correct')
#         break
#     elif abs(number - user_number) == 1:
#         print('off by one')
# else:
#      print('wrong')

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def add(self):
        return self.age + 20


player1 = PlayerCharacter('Tom',20)
player1.shout()
print(player1.shout())
