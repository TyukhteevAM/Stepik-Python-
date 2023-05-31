def closest_mod_5(x):
    while x % 5:
        x += 1
    return x


print(closest_mod_5(11))

"""ответ с применением рекурсии"""
# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     else:
#         return closest_mod_5(x + 1)


# print(closest_mod_5(11))
