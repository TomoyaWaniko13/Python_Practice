# # def make_list(num):
# #     result = []
# #     for i in range(num):
# #         result.append(i * 2)
# #     return result
# #
# #
# # my_list = make_list(10000000000)
# # print(my_list)
#
# def generator_function(num):
#     for i in range(num):
#         yield i
#
#
# for item in generator_function(100000000000):
#     print(item)

def generator_function(number_of_iteration):
    for i in range(number_of_iteration):
        yield i * 2


generator = generator_function(1)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))