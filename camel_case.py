def to_camel_case(text):
    text_list = text.replace("-","_").split("_")
    new_list = [text_list[0]]
    for word in text_list[1:]:
       new_word = word[0].upper() + word[1:]
       new_list.append(new_word)
    text = "".join(new_list)

    return text
