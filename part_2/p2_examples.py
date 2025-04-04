# mein_input = int(input("Zahl? "))
# meine_namen_input = input("Name? ")
#
# if 3 == mein_input or "Valentin" == meine_namen_input:
#     print("Hallo Welt")
#     print("Cool")
#     if not (mein_input == 3):
#         print("Der name gut, die zahl aber nicht")
#     if mein_input % 2 == 0:
#         print("die zahl war aber gerade!")
#     elif mein_input % 2 == 1:
#         print("die Zahl war ungerade")
# else:
#     print("War keine 3!!!!!")
#
# print("hehe")
#
#
# mein_name = "Valentin"

#meine_zahl = 0
#weiter = "ja"

# while meine_zahl <= 100:
#     print("Hallo" + str(meine_zahl))
#     meine_zahl = meine_zahl + 1
#     weiter = input("Weiter?")
#     if weiter != "ja":
#         print("Du willst anscheinend nicht mehr!")
#         break

def print_some_stuff(name):
    print('Hallo ' + name)


#
#
print_some_stuff("Valentin")

var_1 = 5

def quadrat_und_mehr(x, y):
    if (y < 0):
        print("warum negativ?")
    var_2 = 5
    print(x*x+y)
    print(y*x*var_1)


quadrat_und_mehr(10, 4)
quadrat_und_mehr(var_2, var_1)