''' Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
contains the word ‘twinkleʼ '''

f = open("poem.txt")
poem = f.read()
if("Twinkle" in poem):
    print("The word twinkle is present is Poem")
else:
    print("The word twinkle is not present in Poem")

    
f.close()

