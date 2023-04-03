print("Welcome to Treasure island.\n Your mission is to find the treasure.")
dir=input("Choose one direction left or right:")
dir1=dir.lower()
if dir1=="right":
  print("game over")
else:
  dir2=input("choose swim or wait:")
  dir3=dir2.lower()
  if dir3=="swim":
    print("Game over")
  elif dir3=="wait":
    col=input("which door blue,yellow or blue:")
    col1=col.lower()
    if col1=="red":
      print("game over")
    elif col1=="blue":
      print("game over")
    else:
      print("you won")