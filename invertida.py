frase = str(input('A frase que sera invertida'))


def sentence(frase):
    words = frase.split(" ")
    novaWords = [palavra[::-1] for palavra in words]
    newSentence = " ".join(novaWords)
    return newSentence


print(sentence(frase))
