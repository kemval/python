while True:
  word= input("enter the word: \n")
  def is_isogram(word):
      soFar =[]
      for letter in word.lower():
          if letter.isalpha():
              if letter in soFar:
                  return False
              else:
                  soFar.append(letter)
      return True
  print (is_isogram(word))


