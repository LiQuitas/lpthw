from sys import exit

def wrasslebox():
    print("\n\tTime for everone's favorite leisure activity!")
    print("\tWatching big sweaty men slap meat!")
    print("\tIs it going to be [AEW] tonight, or [WWE]?")
    print("\tYou know, [popcorn] sounds good...")
    popcorn = False

    while True:
        choice = input("> ").lower()

        if "wwe" in choice:
            dead("\t\nWhy won't the camera stop zooming?!  Who watches this crap?")
        elif "popcorn" in choice and not popcorn:
            print("\n\tYou used just the perfect amount of Flavacol!")
            print("\tSo what's on, [AEW] or [WWE]?")
            popcorn = True
        elif choice == "aew" and popcorn:
            print("\n\tYou managed to miss the Hook match!")
            print("\tYou got back just in time for Adam Cole Vs. Adam Page!")
            dead("\tIt was the best under 5 foot bout you've ever seen!! \n\t6 stars for sure!")
        elif choice == "aew" and not popcorn:
            print("\n\tUnfortunately Hook was in the first match.")
            dead("\tand now you're having a bad time.")
        else:
            print("\n\tI know it's hard to decide.")
            print("\tThere's just so much quality product.")
            print("\tSo, [AEW] or [WWE]?")



def hkmovie():
    print("\n\tTime for a trip to the HK Movie Dojo!")
    print("\tThis promises to be an exciting night of Kung-Fu fighting!")
    print("\tWanna prep by making [popcorn], having some [Four Loko], or taking a [Benadryl]?")
    print("\tOr should we go straight to the [movie]?")
    four_loko = False
    benadryl = False

    while True:
        choice = input("> ").lower()

        if "popcorn" in choice:
            dead("\t\nYou attempted to make popcorn but accidentally burned your house down!")
        elif "benadryl" in choice and not benadryl:
            print("\n\tYou pop a couple Benadryl.  You've been itchy!")
            print("\tYou're definitely ready for the movie now.")
            print("\tWant to start the [movie]?")
            benadryl = True
        elif "four loko" in choice and not four_loko:
            print("\t\nYou pop open a cold one and get to sippin.  Ahh, tastes like poison!")
            print("\tWant to start the [movie]?")
            four_loko = True
        elif choice == "movie" and benadryl and not four_loko:
            print("\t\n11 minutes into the feature you've passed out.")
            dead("\tNow everybody in voice chat can hear you snoring, sleepyhead...")
        elif choice == "movie" and four_loko and not benadryl:
            print("\t\nYou had a great time and enjoyed what you remember of the movie!")
            dead("\tYou rated it 7/10 on criticker and went to sleep.")
        elif choice == "movie" and four_loko and benadryl:
            dead("\t\nLike a fool you have mixed drugs and alcohol and have died.")
        elif choice == "movie" and not four_loko and not benadryl:
            dead("\t\nYour wound has gotten so itchy you scratched yourself bloody.")
        else:
            print("\t\nYou're going to have to be more specific (dumbass).")


def start():
    print("\n\tIt's April 2022.  You're recovering from surgery.")
    print("\tYou've logged into the Geekbox Discord server.")
    print("\tLet's have some fun with the homies!")
    print("\tWould you like to enter the HK [Movie] Dojo, [wrasslebox], or brave the depts of [shitposting]?")

    choice = input("> ")

    if "movie" in choice:
        hkmovie()
    elif "wrasslebox" in choice:
        wrasslebox()
    elif "shitposting" in choice:
        dead("\t\nKindGalaxy has bored you to death with tales of how much America sucks.")
    else:
        dead("\t\nI guess you're just gonna waste the night looking at Reddit...")

def dead(why):
    print(why, "Great job!")
    exit(0)

start()
