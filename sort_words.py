def sort_words(sentence):
    words=sentence.split()
    sorted_words=sorted(words,key=lambda word:word[1], reverse=True)
    return sorted_words
user_input=input("Enter a sentence")
sorted_words=sort_words(user_input)

print("sorted_words")
for word in sorted_words:
    print(word)
