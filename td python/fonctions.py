# Q1)
# def compteCar(ca, ch):
#     counter = 0
#     for c in ch:
#         if c == ca:
#             counter += 1
#
#     return counter
#
#
# print ( compteCar('e','Cette phrase est un exemple'))


# Q2)
# def indexMax(liste):
#     maximum = max(liste)
#     return liste.index(maximum)
#
#
# print(indexMax([5, 8, 2, 1, 9, 3, 6, 7]))

# Q3
# def nomMois(n):
#     mois = {
#         1: "Janvier",
#         2: "Fevrier",
#         3: "Mars",
#         4: "Avril",
#         5: "Mai",
#         6: "Juin",
#         7: "Juillet",
#         8: "Aout",
#         9: "Septembre",
#         10: "Octobre",
#         11: "Novembre",
#         12: "Decembre",
#     }
#     return mois[n]
#
# print(nomMois(4))

# Q4)
# def inverse(ch):
#     return ch[::-1]
#
# print(inverse("hello"))

# Q5)
# def compteMot(ch):
#     list_mots = ch.split()
#     return len(list_mots)
#
# print("nombre de mot:", compteMot("Hi je suis imad"))



# Q1
# def changeCar(ch,ca1,ca2,debut,fin):
#     new_string = ""
#     for i in range(debut, fin+1):
#         if ch[i] == ca1:
#             new_string = new_string + ca2
#         else:
#             new_string = new_string + ch[i]
#
#     return new_string
#

# print(changeCar("imad ouairem", "a", "*", 0, 7))

#
# def eleMax(liste,debut=0,fin=0):
#     if fin == 0 :
#         indx_fin = len(liste)
#     else:
#         indx_fin = fin
#     max = liste[0]
#     for i in range(debut, indx_fin):
#         if liste[i] > max:
#             max = liste[i]
#     return max
#
# liste = [4, 2,1,6,7]
# print(eleMax(liste, 0,3))