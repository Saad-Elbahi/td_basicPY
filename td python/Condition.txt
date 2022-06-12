# Q1)
# num = int(input("give a number : "))
#
#
# if num % 2 == 0:
#     print("pair")
# else:
#     print("impair")

# Q2)
# num = int(input("give a number: "))
#
# if num % 3 == 0 and num % 13 == 0:
#     print("Divisible par 3 est 13")


# Q3 - Q4)
# annee = int(input("Donner une annee : "))
# mois = int(input("Donner le mois: "))
#
# bissextile = False
#
# if annee % 400 == 0:
#     bissextile = True
# elif annee % 4 == 0 and annee % 100 != 0:
#     bissextile = True
#
# if bissextile:
#     print(f"{annee} est une annee bissextile")
# else:
#     print(f"{annee} n'est pas une annee bissextile")
#
#
# if mois == 2:
#     if bissextile:
#         print("29 days")
#     else:
#         print("28 days")
# elif mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
#     print("31 days")
# else:
#     print("30 days")


# Q5)

# c = input("Donner un caractere: ")
# c_ascii = ord(c)
#
# if 32 <= c_ascii <= 47 or 58 <= c_ascii <= 64 or 91 <= c_ascii <= 96 or 123 <= c_ascii <= 126:
#     print("Caractere special")
# elif 65 <= c_ascii <= 90 or 97 <= c_ascii <= 122:
#     print("Alphabet")
# elif 48 <= c_ascii <= 57:
#     print("Chiffre")


# Q6)
# c = input("Donner un caractere: ")
# c_ascii = ord(c)
#
# if 65 <= c_ascii <= 90 or 97 <= c_ascii <= 122:
#     if c_ascii == 65 or c_ascii == 69 or c_ascii == 73 or c_ascii == 79 or c_ascii == 97 or c_ascii == 101 or c_ascii == 105 or c_ascii == 111:
#         print("Voyelle")
#     else:
#         print("Consonne")
# else:
#     print("Pas de l'alphabet")



