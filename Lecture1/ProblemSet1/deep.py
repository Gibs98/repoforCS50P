#A program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
#Author - Quiana Gibson
#Date - 8 Feb 2024
#Summary: A program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.



#Define answer 
def answer(n):
    if n == "42" or "forty-two" or "forty two":
        print("yes")
    else:
        print("no")
#a main function   
def main():
    question = "What is the great question of life and the meaning of everything?"

text = input(question)


answer(text.lower())
main()