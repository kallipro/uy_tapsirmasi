# # # # ! Nesting


# # # avto1 = {
# # #     "model": "lacetti",
# # #     "ren": "aq",
# # #     "jil": 2019,
# # #     "bahasi": 17000,
# # #     "km": 50000,
# # #     "karovka": "avtomat",
# # # }

# # # avto2 = {
# # #     "model": "nexia 3",
# # #     "ren": "qara",
# # #     "jil": 2015,
# # #     "bahasi": 9000,
# # #     "km": 89000,
# # #     "karovka": "mexanika",
# # # }

# # # avto3 = {
# # #     "model": "gentra",
# # #     "ren": "qizil",
# # #     "jil": 2019,
# # #     "bahasi": 15000,
# # #     "km": 20000,
# # #     "karovka": "mexanika",
# # # }


# # # # avto = avto1
# # # # print(
# # # #     f"{avto['model'].title()},\
# # # #   {avto['ren']} rende,\
# # # #   {avto['jil']}-jil, {avto['bahasi']}$"
# # # # )

# # # # avto = avto2
# # # # print(
# # # #     f"{avto['model'].title()},\
# # # #   {avto['ren']} rende,\
# # # #   {avto['jil']}-jil, {avto['bahasi']}$"
# # # # )

# # # # avto = avto3
# # # # print(
# # # #     f"{avto['model'].title()},\
# # # #   {avto['ren']} rende,\
# # # #   {avto['jil']}-jil, {avto['bahasi']}$"
# # # # )

# # # avto = [avto1, avto2, avto3]
# # # for car in avto:
# # #     print(
# # #         f"{car['model'].title()}, "
# # #         f"{car['ren']} rende, "
# # #         f"{car['jil']}-jil, {car['bahasi']}$"
# # #     )


# # # print(avto[0])
# # # print(avto[1])
# # # print(avto[2])

# # # print(avto[0]["model"])
# # # print(avto[0]["ren"])

# # malibu = []
# # for n in range(10):
# #     new_avto = {  # har bir taza mashin ushin sozlik
# #         "Mamleket" : "Uzbekistan",
# #         "model": None,
# #         "reni": None,  # reni belgsiz
# #         "jil": None,
# #         "bahasi": None,  # bahasi belgilenbegen
# #         "km": None,
# #         "korobka": None,
# #     }
# #     malibu.append(new_avto)  # taza avtoni listke qosamiz!

# # for avto in malibu[:3]:
# #     avto["reni"] = input('modeli jaz : ')
# #     avto['model'] = 'matiz'
# # for new in malibu[3:6]:
# #     new["reni"] = "qara"


# # for avto in malibu[6:]:  # aqirgi 4 mashinnin
# #     avto["reni"] = "qara"  # reni qara
# #     avto["korobka"] = "mexanika"  # karobkasi mexanika


# # for avto in malibu:
# #     if avto["korobka"] == "avto":
# #         avto["bahasi"] = 40000
# #     else:
# #         avto["bahasi"] = 35000

# # print(malibu)


# # sozlik ishinde sozlik jaratamiz:
# # dasturshiler = {
# #     "farxad": ["python", "c++"],
# #     "shayda": ["html", "css", "js"],
# #     "kallibek": ["php", "sql"],
# #     "aytmurat": ["python", "php"],
# #     "jamila": ["c++", "c#"],
# # }

# # for ati, tiller in dasturshiler.items():
# #     print(f"\n{ati.title()} usi tillerdi biledi. :")
# #     for til in tiller:
# #         print(til.upper())


# # for ati, tiller in dasturshiler.items():
# #     print(f"\n{ati.title()} usi tillerdi biledi : ", end="")
# #     for til in tiller:
# #         print(f"{til.upper()} ", end="")


# # sozlik ishinde list:
# oqiwshilar = {
#     "aytmurat": {
#         "familiya": "shamuratov",
#         "tjili": 2009,
#         "magliwmati": "orta",
#         "tiller": ["python", "c++"],
#     },
#     "shayda": {
#         "familiya": "amanova",
#         "tjili": 2009,
#         "magliwmati": "orta",
#         "tiller": ["html", "css", "js"],
#     },
#     "kallibek": {
#         "familiya": "iskenderov",
#         "tjili": 1997,
#         "magliwmati": "joqari",
#         "tiller": ["python", "php"],
#     },
# }
# print(oqiwshilar)


# for ati, info in oqiwshilar.items():
#     print(
#         f"\n{ati.title()} {info['familiya'].title()}, "
#         f"{info['tjili']}-jilda tuwilg'ani."
#         f"Mag'liwmati: {info['magliwmati']}. \n"
#         "usi tillerdi biledi:"
#     )
#     for til in info["tiller"]:
#         print(til.upper())
