memes = {
    "LOL": "odpowiedź na coś zabawnego",
    "CRINGE": "coś dziwnego lub wstydliwego",
    "ROFL": "odpowiedź na żart",
    "SHEESH": "lekka dezaprobata",
    "CREEPY": "straszny, złowieszczy",
    "AGGRO": "stać się agresywnym/zły"
}
print("Wybierz z listy: LOL, CRINGE, ROFL, SHEESH, CREEPY, AGGRO")
while True:
    word = input("Podaj slowo ktorego nie rozumiesz duzymi literami: ")
    if word in memes.keys():
        print(word + " = " + memes[word])
    else:
        print("Nie odnaleziono tego slowa!")