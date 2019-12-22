def pig_latin(word):

    if word[0] in 'aeiou':
        pig_word = word + 'ay'
    else:
        if word[1] in 'aeiou':
            pig_word = word[1:] + word[0] + 'ay'
        else:
            if word[2] in 'aeiou':
                pig_word = word[2:] + word[0] + word[1] + 'ay'
            else:
                pig_word = word[3:] + word[0] + word[1] + word[2] + 'ay'

    return pig_word.lower()



def pig_sentence(string):
    
    piggified = []

    for word in string.split():
        p_word = pig_latin(word)
        piggified.append(p_word)
    
    s = " "
    s = s.join(piggified)
    return s
    

print(pig_sentence("This should be latinized"))