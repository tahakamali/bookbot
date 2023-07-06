print("enter your book path : ")
url = input()
with open(url) as f:
    file_content = f.read()
def count_words(a):
    words = a.split()  
    words_number = len(words)
    return words_number

def count_letters(a):
    letters_number = {}
    for i in range(ord('a') , ord('z')) :
        x=chr(i)
        letters_number[x] = a.lower().count(x)
    return letters_number

print("this book has " , count_words(file_content) , "words") 
print("\nletters" , "         number")
for i in range(ord('a') , ord('z')) :
     x=chr(i)
     print(x , "       =     " , count_letters(file_content)[x])
     print("---------------------------")
