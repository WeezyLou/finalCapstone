#create a Ceasor cypher with a shift of 15
#create a function to encode any message
#research how to turn a letter into a number
#be aware of capital and lower case
#punctuation needs to stay the same
#I did have help from Stack overflow

cipher = lambda w, s:''.join(chr(a + (i - a + s) % 26) if (a := 65) <= (i := ord(c)) <= 90 or (a := 97) <= i <= 122 else c for c in w)
word = input("Please enter a phrase: ")

print(cipher(word, 15)) # positive shift