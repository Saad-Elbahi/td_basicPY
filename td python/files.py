
# f1 = open("myfile.txt", "w")
# f1.write("Hello\n")
# f1.write("World")
# f1.close()


# Q1)
# f1 = open("myfile.txt", "r")
# while 1:
#     txt = f1.readline()
#     print(txt, end="")
#     if txt == "":
#         break
# f1.close()

# # Q2)
# with open("myfile.txt", "r") as file:
#     file_words = file.read().split()
#     print(len(file_words))

# Q3)
# with open("mult.txt", "w") as f:
#     for i in range(1, 10):
#         for j in range(1, 11):
#             f.write(f"{i} x {j} = {i*j}\n")
#         f.write("\n")
