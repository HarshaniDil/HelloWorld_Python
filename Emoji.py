message = input(">")
words = message.split(' ')
emojis ={
    ":)" : "😊",
    ":(" : "😒"

}
output = ""
for word in words:
    output += emojis.get(word,word) + " "

print(output)

def emoji_converter(message1):
    words = message1.split(' ')
    emojis ={
        ":)": "😊",
        ":(": "😒"
    }
    output = " "
    for word in words:
        output +=emojis.get(word,word) + " "
    return output

message1 = input(">")
print(emoji_converter(message1))
