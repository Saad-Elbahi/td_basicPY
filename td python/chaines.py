# Q1)
# chaine = input("donner une chaine: ")
#
# hasE = False
# for char in chaine:
#     if char == 'e':
#         hasE = True
#         break
#
# if hasE:
#     print("cette chaine contient 'e'")
# else:
#     print("cette chaine ne contient pas 'e'")


# Q2)
# chaine = input("donner une chaine: ")
# nbe = 0
#
# for char in chaine:
#     if char == 'e':
#         nbe +=1
#
# print("L'occurrences du caractere 'e' dans la chaine est ", nbe)


# Q3)
# chaine = input("Donner une chaine: ")
# new_chaine = ""
# i=0
# for char in chaine:
#     if i == len(chaine)-1:
#         new_chaine += char
#     else:
#         new_chaine += char + "*"
#     i += 1
#
# print(new_chaine)


# Q4)
# chaine = input("Donner une chaine: ")
# new_chaine = ""
#
# for i in range(len(chaine) -1, -1, -1):
#     new_chaine += chaine[i]
#
# print(new_chaine)
