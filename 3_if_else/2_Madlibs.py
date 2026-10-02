# Madlibs= a game where one player tells the player some Nouns, Adjectives, Pronouns, Adverbs, Verbs and then these 
#          words are input in the story with blanks marked in it .

print("Select the subject of the Madlib Story.") 
a=int(input('For "Science fiction" - Press 1\nFor " Super Hero" - Press 2'))



if(a==1):
    print("Subject selected - Science Fiction")
    a1=int(input("Enter a no. : "))
    a2=input("Enter a Adjective : ")
    a3=input("Enter a Object : ")
    a4=input("Enter a Place : 1")
    a5=input("Enter a plural creatures : ")
    a6=input("Enter a Occupation : ")

    story="n the year [number], a team of explorers discovered a [adjective] crystal buried beneath " \
    "the surface of [place]. When they activated it, the device released a swarm of [plural creatures] " \
    "that began to change reality itself. Only a [occupation] could stop them before the universe collapsed."

    print(f"Your Funny Madlib Story is :\n"
        f"In the year {a1}, a team of explorers discovered a {a2} crystal buried beneath " \
        f"the surface of {a3}. When they activated it, the device released a swarm of {a4} " \
        f"that began to change reality itself. Only a {a6} could stop them before the universe collapsed.")

elif a==2:
    print("Subject selected - Super Hero")
    b1=input("Enter a City: ")
    b2=input("Enter a Adjective : ")
    b3=input("Enter a Superhero Name : ")
    b4=input("Enter a Verb ")
    b5=input("Enter a Villian Name : ")

    story2="One night in [city], a mysterious [adjective] [object] appeared in the sky. \
    Suddenly, the legendary hero [superhero name] swooped in to [verb] it before villains could take control.\
    But just as victory seemed certain, the evil [villain name] arrived, threatening to destroy everything."

    print(f"One night in {b1}, a mysterious {b2}] crystal appeared in the sky. \
    Suddenly, the legendary hero {b3} swooped in to {b4} it before villains could take control.\
    But just as victory seemed certain, the evil {b5} arrived, threatening to destroy everything.")

else:
    print("Entered Number is Wrong , Select 1 or 2.")


    