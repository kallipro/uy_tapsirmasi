# # # # # # Farxad = {'ati': 'farxad',
# # # # # #           'jas':'90',
# # # # # #         #   'xobbiy':'matimatika',
# # # # # #           'ol uyengenba':False,
# # # # # #           'xobbiy' : ['oqiw','oyin','futbol'],
# # # # # #           'ss': 566.55,
# # # # # #           'a' : {'fff','ggfg'}
# # # # # #           }


# # # # # # print(Farxad['xobbiy'])


# # # # # # # print(f'{Farxad['ati']}')

# # # # # # # pri'oyinnt(f' fgfgfdfg     {Farxad['ati']}')


# # # # # # # print(Farxad['ol uyengenba'])

# # # # # # # salem = {'en':'hello','ru':'privet','uz':'salom'}

# # # # # # # print(salem['en'])


# # # # # a = {
# # # # #     'b': '555'
# # # # # }

# # # # # a['c'] = '666'


# # # # # print(a)


# # # # baza = {}

# # # # baza['ati'] = 'Farxad'
# # # # baza['jasi'] = 14

# # # # print(baza)

# # # # del baza['jasi']

# # # # print(baza)

# # # # # print(f'Oqiwsh {baza['ati']}')


# # # # a = {}
# # # telefonlar  = {
# # #     'farxad': 'samsung',
# # #     'shayda': 'texnospark',
# # #     'Iphone': 'Iphone 16.5'
# # # }

# # # # ! get()
# # # # tel = telefonlar['baxadir']

# # # tel = telefonlar.get('baxadir', 'Bunday adam joq')

# # # print(tel)

# # # ! items
# telefonlar = {"farxad": "samsung", "shayda": "texnospark", "Iphone": "Iphone 16.5"}
# # print(telefonlar.items())

# # print(telefonlar.keys())

# # for tel in telefonlar.keys():
# #     print(tel.title())

# telefonlar = {"farxad": "samsung", "shayda": "texnospark", "Iphone": "Iphone 16.5"}

# print(telefonlar.values())

# for tel in telefonlar.values():
#     print(tel)

# for tel in sorted(telefonlar):
#     print(tel.title())
# for  tel in telefonlar.keys():
#     print(tel.upper())


# # print()

# ! hazir dukanimizda bar bolgan tovarlar:
tovarlar = {
    "alma": 10000,
    "qumsheker": 20000,
    "alma": 40000,
    "un": 25000,
    "shabdal": 30000,
    "konfet": 5000,
}

# print(tovarlar.keys())


# print("Dukanimizdagi tovarlar:")
# for tovar in tovarlar.keys():
#     print(tovar.title())


bazarliq = []
for n in range(3):
    bazarliq.insert(0, input("ne alasiz? "))

    if bazarliq[0] in tovarlar.keys():
        print("Yaqshi.")
    else:
        print(f"Keshirersiz {bazarliq[0]} bizlerde joq edi.")

print("Demen siz alg'an tovarlariniz:")

for tovar in tovarlar:
    if tovar in bazarliq:
        print(f"{tovar.title()} {tovarlar[tovar]} swm")
