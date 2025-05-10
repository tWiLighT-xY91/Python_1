# To count the frequency of each word in a sentence

def word_freq(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0)+1
    return freq


print(word_freq("Millie Bobby Millie"))