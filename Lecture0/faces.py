
# create a function called convert 
# input: str
# output: all :) to 🙂, :( to 🙁
def convert(message):
    message = message.replace(":)","🙂")
    message = message.replace(":(","🙁")
    return message

# create a function called main
# that prompts user for input
# call convert
# print output

def main():
    emoji = convert(input("Type a message.\n"))
    print(emoji)

main()
