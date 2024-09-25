
def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        o_w = str(other_words[i])
        r_w = str(root_word)
        if r_w.lower() in o_w.lower():
            same_words.append(o_w)
        elif o_w.lower() in r_w.lower():
            same_words.append(o_w)
        i += 1
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)