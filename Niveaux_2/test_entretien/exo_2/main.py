def get_words_of_same_length(sentence):
    words = sentence.split(" ")
    words.sort()
    if not words:
        return None, None

    min_word = min(words, key=len)
    max_word = max(words, key=len)
    
    return min_words, max_words

s = "Un chasseur sachant chasser sait sans son chien"
min_words, max_words = get_words_of_same_length(s)

print("Mots de la même longueur que le mot le plus court :", min_words)
print("Mots de la même longueur que le mot le plus long :", max_words)
