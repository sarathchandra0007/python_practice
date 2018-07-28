
def word_split(phrase,set_words,output=None):
    if output is None:
        output=[]
    for word in set_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word): ] ,set_words,output)

    return output



print (word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
