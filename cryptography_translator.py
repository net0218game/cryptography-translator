text = input(">>> Text goes here: ").lower()

translated = ""

alphabet = {
    "a": "",
    "b": "",
    "c": "",
    "d": "",
    "e": "",
    "f": "",
    "g": "",
    "h": "",
    "i": "",
    "í": "",
    "j": "",
    "k": "",
    "l": "",
    "m": "",
    "n": "",
    "o": "",
    "p": "",
    "r": "",
    "s": "",
    "t": "",
    "u": "",
    "v": "",
    "x": "",
    "y": "",
    "z": "",
    # For space character (leave it empty)
    " ": " "
}

for i in range(len(text)):
    letter = str(alphabet.get(text[i]))
    translated += "".join(letter)

print(translated)