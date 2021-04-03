startcal = input("Roger's calculator! You wanna do math ? (y/n)")
if startcal =="y":
  print("great then lets start!")
  n1 = input(("Give me the first number to operate:"))
  n2 = input(("Give me the second number to operate:"))
  n1 = int(n1)
  n2 = int(n2)
  opera = input("Which operation do you want to do?\n 1 - Add\n 2 - Subtract\n 3 - Mutiply \n 4 - Divide\n ? = ...")
  if opera == "1":
    print("your result is ", n1 + n2)
  if opera == "2":
    print("your result is ",n1 -n2)
  if opera == "3":
    print("your result is ",n1 * n2)
  if opera == "4":
    print("your result is ",n1 / n2)
else:
  print("goodbye then!")