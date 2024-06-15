def convert_sentence(sentence):
    words=sentence.lower().split()
    converted_sentence=words[0].capitalize()+" "+" ".join(words[1:])
    return converted_sentence
input_sentence="My name is Jayanthi and Completed B Tech"
converted_sentence=convert_sentence(input_sentence)
print(converted_sentence)
