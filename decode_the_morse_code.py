from preloaded import MORSE_CODE

def decode_morse(morse_code):
    morse_words = morse_code.split('   ') # separate each word into an item
    decoded_sentence = []

    for word in morse_words:
        morse_characters = word.split()
        decoded_word = [] # reset decoded_word for each new word
        for character in morse_characters:
            decoded_word.append(MORSE_CODE[character])
        decoded_sentence.append("".join(decoded_word))

    decoded_sentence_str = " ".join(decoded_sentence).strip()
    
    return decoded_sentence_str
