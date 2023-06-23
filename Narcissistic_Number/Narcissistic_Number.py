while True:
  num = input("\nInput a  number on 'n' to stop: ")
  sum = 0
  if num == 'n':
    break
  elif int(num) <= 0:
    print("\nThe number is less than 0, retry")
    continue
  for i in range(len(num)):
    sum += int(num[i])**len(num)
  if sum == int(num):
    print("\nThe number is narcissistic! :D")
  else:
    print("\nThe number is not narcissistic! D:")