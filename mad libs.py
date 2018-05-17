import time
### Source: https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjZk5fmg6DXAhUCPhQKHVdBDBcQjRwIBw&url=http%3A%2F%2Fwww.woojr.com%2Fsummer-mad-libs%2Ffunny-mad-libs%2F&psig=AOvVaw0Mq2_JCsyidLCX4f6V7TT-&ust=1509716868331291

print("Write an adjective")
adjective1 = input()

print("Write a nationality")
nationality1 = input()

print("Write a name")
name1 = input()

print("Write another noun")
noun1 = input()

print("Write another adjective")
adjective2 = input()

print("Write another noun")
noun2 = input()

print("Write another adjective")
adjective3 = input ()

print("Write another adjective")
adjective4 = input ()

print("Write a plural noun")
pluralnoun1 = input()

print("Write another noun")
noun3 = input ()

print("Write a number")
number1 = input ()

print("Write a shape")
shape1 = input ()
if number1 != "1":
    shape1 = shape1 + "s"

print("Write a food")
food1 = input ()

print("Write another food")
food2 = input ()

print("Write another number")
number2 = input ()

### MAD LIB ###

print("Pizza was invented by a " + adjective1 + " " + nationality1 +
      " chef named " + name1 + ". " +
      "To make pizza, you need to take a lump of " + noun1 +
      ", make a thin, round " + adjective2 + " " + noun2 +
      ". Then you cover it with " + adjective3 + " sauce, " + adjective4 +
      " cheese,and fresh chopped " + pluralnoun1 +
      ". Next you have to bake it in a very hot "
      + noun3 + ". When it is done, cut it into " + number1 + " " + shape1 +
      ". Some kids like " + food1 +
      " pizza the best, but my favorite is the " + food2 +
      " pizza. If I could, I would eat pizza " + number2 +
      " times a day!")

time.sleep(100)
