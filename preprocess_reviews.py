import re
from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer
#from nltk.tokenize import word_tokenize
#import deepl


def limpiar(texto):
    caracteres = r'[^A-Za-z0-9 ]+'
    texto = re.sub(caracteres, ' ', texto) # Se eliminan todos los caracteres que no sean letras, números o espacios
    return texto


def normalizar(texto):
    texto = texto.lower() # Se pasa el texto a minúsculas
    """ # Finalmente se decidió no aplicar stemming
    porter = PorterStemmer()
    stemmed = ""
    tokens = word_tokenize(texto)
    for token in tokens:
        palabra = porter.stem(token)
        stemmed += palabra + " "
    """
    return texto


def quitar_vacias(texto):
    palabras_vacias = set(stopwords.words('english')) # Se genera un array con las palabras vacías del inglés
    f = open("data/processed_reviews.txt", "a")
    tokens = ""
    for palabra in texto.split(" "):
        if palabra not in " " and palabra not in palabras_vacias: # Se comprueba iterativamente si la palabra no es vacía (no aporta significado)
            tokens += palabra + " "
    f.write(tokens + "\n")
    f.close()


if __name__ == "__main__":
    """ # Está comentado porque la traducción se llevó a cabo una vez y se guardó en el fichero para trabajar con él posteriormente
    auth_key = ""
    translator = deepl.Translator(auth_key)
    with open("data/reviews.txt", "r") as f: # Se lee el fichero de opiniones y se almacenan en una lista
        lines = f.readlines()
        f.close()

    f = open("data/translated_reviews.txt", "a")
    for line in lines:
        traducido = translator.translate_text(line, target_lang='EN-US').text # Se traduce al inglés
        f.write(traducido)
        limpio = limpiar(traducido) # El texto se limpia y normaliza
        normalizado = normalizar(limpio)
        quitar_vacias(normalizado)
    f.close()
    """

    with open("data/translated_reviews.txt", "r") as f: # Se lee el fichero de opiniones y se almacenan en una lista
        lines = f.readlines()
        f.close()

    for line in lines:
        limpio = limpiar(line) # El texto se limpia y normaliza
        normalizado = normalizar(limpio)
        quitar_vacias(normalizado)
