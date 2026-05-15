message=input(">")
words=message.split(' ')
emoji={
    ":)" : "4",
    ":(" : "3"
}
output=""
for word in words:
    output+=emoji.get(word,word) + " "
print(output)