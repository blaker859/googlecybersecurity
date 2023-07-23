# working with files in python

# read file and store in a variable 'file'
# with open ("random.txt", "r") as file:
#     file_text=file.read()
    
# print(file_text)

# converting file into a list
# with open ("random.txt", "r") as file:
#     file_text=file.read()
    
# print(file_text.split())


"""
count words in a file
"""
def count_variables(list_words,current_word):
    counter = 0
    for i in list_words:
        if i==current_word:
          counter = counter + 1
    print(counter,current_word)
    return(counter,current_word)
    
with open('random.txt', 'r') as file:
    filetext=file.read()
    
result=count_variables(filetext.split(),"his")
# print(result)