message=input(">")
words=message.split(' ')
emoji={
    ":)" : "2",
    ":(" : "3"
}
output=""
for word in words:
    output+=emoji.get(word,word) + " "
print(output)