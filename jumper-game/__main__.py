print(" ___")
print("/___\ ")
print("\   /")
print(" \ /")
print("  o")
print("/ | \ ")
print(" / \ ")
body_list = [" ___","/___\ ", "\   /", " \ /", "  o", "/ | \ ", " / \ "]
words = ["dessert", "cross", "red", "light"]
"""print(body_list[0])
print(body_list[1])
print(body_list[2])
print(body_list[3])
print(body_list[4])
print(body_list[5])
print(body_list[6])"""
for i in body_list:
    print(i)


letter = input("Guess a letter [a - z]: ")

body_list.pop(0)
for i in body_list:
    print(i)