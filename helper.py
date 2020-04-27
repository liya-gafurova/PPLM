with open('custom_bow_raw.txt') as raw:
    text = raw.readlines()
    words = [item for line in text for item in line.split()]
    with open('customBoW.txt', 'w') as clear:
        clear.write('\n'.join(words))