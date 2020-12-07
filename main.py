def morse(text):

    morseovka = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                 'Z': '--..', ' ': '.....'}
    preklad = ''

    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    else:
        return 'Vstupni retezec neni napsan v uvozovkach'

    if text.startswith('.') or text.startswith('−'):
        morseovka_preklad = dict([(v, k) for k, v in morseovka.items()])
        text = text.split(' ')
        for x in text:
            preklad += morseovka_preklad.get(x)

    else:
        text = text.upper()
        for x in text:
            preklad += morseovka.get(x) + ' '
    return preklad.strip()


print("Zadejte retezec (musi byt v uvozovkach):")
inputstr = str(input())

print(morse(inputstr))
