# Q1)

# n = int(input("Donner n: "))
# i = 0
# somme = 0
# while i <= n:
#     somme += i
#     i += 1
# print(somme)

# Q2)

# n = int(input("N: "))
#
# fact = 1
# i=1
#
# while i <= n:
#     fact *= i
#     i += 1
#
# print(fact)

# Q3)

# n = int(input("Donner un nombre: "))
# for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")

# Q4)
# n_string = input("Donner un nombre: ")
# inversed_n_string = n_string[::-1]
# if n_string == inversed_n_string:
#     print("le nombre " + n_string + " est palindrome.")
# else:
#     print("le nombre " + n_string + " n'est pas palindrome.")


# Q5)
# n = int(input("Donner un nombre: "))
# is_premier = True
#
# for i in range(2, n):
#     if n % i == 0:
#         is_premier = False
#
# if is_premier:
#     print(f"{n} est premier")
# else:
#     print(f"{n} n'est pas premier")

# Q6)
# n1 = int(input("Donner un le premier nombre: "))
# n2 = int(input("Donner le second nombre: "))
#
# a = max(n1, n2)
# b = min(n1, n2)
# r = -1
# while r != 0:
#     r = a % b
#     if r != 0:
#         a = b
#         b = r
#     else:
#         pgcd = b
#
# print("pgcd : ", pgcd)

# Q7)

# n = input("donner un nombre: ")
# nb = 0
# for chiffre in n:
#     nb += 1
#
# print("nombre de chiffre dans " + n + " : ", nb )

# Q8)

# for i in range(8):
#     for j in range(i):
#         print("*", end="")
#     print("\n",end="")

