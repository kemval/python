letter = input ("Enter the letter ")

if letter.lower() in ("a", "e", "i", "o", "u"):
    print("it is a vowel")
elif letter.upper() in ("A","E", "I","O","U"):
    print("vowel as well")   
else:
    print("consonant") 
    