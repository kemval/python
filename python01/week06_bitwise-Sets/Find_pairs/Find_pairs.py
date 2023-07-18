while True:
  def pairs(lst, K):
      result = []
      for i in range(len(lst)):
          for j in range(i + 1, len(lst)):
              if lst[i] + lst[j] == K:
                  result.append((lst[i], lst[j]))
      return result
  
  lst = [1, 2, 4, 6, 8, 10, 12, 13]  

  print("Hello stranger, This is your current list: \n", lst)

  K = int (input("Enter number grather than 0: "))

  print("Here you can find your pairs: \n", (pairs(lst, K)))

  check = input("would you like to enter another number? y or n: ")
  
  if check.lower () != "y":
      print ("bye")
      break
  
  

