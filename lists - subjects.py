name = "Ryan"

#subjects = ["Math","Science","English","History","Spanish"]

print("Hello " + name)

#for i in subjects:
    #print("One of my classes is " + i)

tvshows = ["The Flash","Arrow","Black Lightning","Supergirl"]

for i in tvshows:
    if i == "Supergirl":
        print(i + " is one of the worst shows on The CW.")
    else:
        print("One of the best shows on The CW is " + i)





movies = []


while True:
    print("What movie do you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)



for i in movies:
    print("One of your favorite movies is " + i)
