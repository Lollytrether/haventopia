# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ash = Character("Asher", color="#38468D")
define bryce = Character("Bryce", color="#731B1B")
define harper = Character("Harper", color="#A245BC")
define mum = Character("Mum", color="#000000")
define unknown_voice = Character("Unknown_voice", color="#ffffff")
image bg corridor = "images/Bg/corridor.jpg"
image bg gym = "images/Bg/gym.jpg"
image bg locker = "images/Bg/locker.jpg"
image bg toilet = "images/Bg/toilet.jpg"
image bg black = "images/Bg/black.jpg"
image punch movie = Movie(play="punch.webm", side_mask = True)

image ash = "images/ash.png"
image bryce = "images/bryce.png"
image harper = "images/harper.png"


default happiness = 5

label start:
    while True:
        if happiness == 0:
            ash "I'm so done. I can't do this anymore. I'm going home"
            "Ending 2: Forever hopeless"
            show bg black with fade
            return
        else:
            pass
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg locker

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ash at left

    # These display lines of dialogue.

    ash "Hi, my name is Asher."
    ash "I’m 16 attending Pinewood High."
    ash "I’m outcasted from the others since I’m different."
    ash "I dress like a dork as they like to call it."
    ash "I like dorky things as they say."
    ash "My life is fine I guess, I have a nice family and a kind girlfriend."
    ash "But, some things aren't right."
    ash "I want it all to end"
    ash "I hate it here."
    ash "But it feels like forces are pulling me back."
    #Edit this metaphor
    ash "Dark thoughts start to swarm my head, it feels like there is a heavy burden on my shoulders."
    ash "My thoughts quickly pop as I hear."

    "Harper holds opens the locker door with Asher standing inside the looker locking back at her"
    show harper at right
    harper "Asher, come on! What are you doing in the locker?"

    menu:
        "Apologise and take her hand":
            "He reaches out his hand after apologising Harper rolls her eyes up at him and takes his hand aggressively grabbing onto it to pull him out"
            ash "Sorry for the trouble, but thank you"
            harper "Yeah, it’s whatever."
            jump start_2
        "Ask why she took so long to find him.":
            "After asking what took her so long she gets angry at him for being ungrateful and yells at him"
            ash "What took you so long to get here"
            harper "Be grateful i got here and am saving your PUNY LITTLE ass"
            $ happiness -= 1
            jump start_2
        "Make a joke about living in the locker.":
            ash "At least I don't pay rent and utilities"
            harper "You can't live here forever"
            ash "Try me"
            harper "*rolls eyes* C'mon, we've got things to do"
            $ happiness -= 1
            jump start_2
        "Say nothing and get out.":
            "..."
            jump start_2

label start_2:
    "Asher starts to think, Maybe tomorrow. Maybe tomorrow I’ll do it."
    harper "Have you seen my lipstick, placeholder"
    ash "Place what? No I haven’t seen it, maybe you left it at mine. I’ll keep an eye out for it"

    #Cuts to Asher walking home on a photo path with headphones on listening to music and bumps into bryce on the path who is walking in the opposite direction.

    hide ash at left
    hide harper at right
    show bryce
    bryce "What up, dork, you're in my road"

    menu:
        "punch him":
            $ happiness -=3
            show punch movie
            # Asher moves a fist into bryce's face, bryce moves his fist back into a punch making contact with asher's face, then asher lies on the floor beaten up basically dead
            jump crying

        "apologise for existing":
            ash "Sorry for being here"
            bryce "You should be sorry, nerd"
            jump drawing

        "ignore him":
            $ happiness -=1
            bryce "You deaf or smth?"
            bryce "I said"
            bryce "MOVE!"
            bryce "NOW!"
            bryce "Are you even listening?"
            bryce "I SAID"
            bryce "YOU HEAR ME LOSER?"
            ash "UGHH"
            "bryce bumps ash, he instantly falls on his face"
            jump drawing

        "insult him"
            $ happiness -=3
            #Come up with a better insult
            ash "I’m sorry it’s so hard to stay out of your way when your ego takes up all the space, discombobulated beetle"
            "Bryce beats Asher up"
            jump crying



label crying:
    # crying in his bed at home
    #Phone buzzes physically moving with text message appearing on the screen from mum about dinner and he texts back pizza
    mum "hey, dinner plans?"
    ash "Pizza would be good"
    mum "Alright, come down then"
    #Eats pizza with mum sitting at a table next to each other and mum is oblivious not realy looking at him but rather just on her food unfocused to everything and asher sees sitting on the table a lipsticks grabbing it with his hands and then shoving it in his pocket
    mum "How’s school going for you?"
    ash "It’s going fine"
    "Asher sleeps"
    jump library


label drawing:
    # him at home drawing
    #Phone buzzes physically moving with text message appearing on the screen from mum about dinner and he texts back pizza
    mum "hey, dinner plans?"
    ash "Pizza would be good"
    mum "Alright, come down then"
    # Eats pizza with mum sitting at a table next to each other and mum is oblivious not realy looking at him but rather just on her food unfocused to everything and asher sees sitting on the table a lipsticks grabbing it with his hands and then shoving it in his pocket
    mum "How’s school going for you?"
    ash "It’s going fine"
    "Asher sleeps"
    jump library

label library:
    #school library with harper sitting at a table doing work, harper gets up moving away to get something, her phone is placed facing up positioned on the table with the screen on the table powered on displaying the home screen.
    harper "Okay I’ll be back. Just don’t do anything stupid like I don’t know die"
    "Her phone is unlocked"

    menu:
        "Plays a game on it":
            #he picks up the phone and play lollie rush with a colourful game displayed clearly on the screen with his thumbs touching them and harper gets back to the table standing near and yells
            harper "WHAT THE HELL ARE YOU DOING ON MY PHONE GIVE IT BACK"
            ash "I was just playing Lollie rush, sorry”
            $ happiness -= 2
            jump start_3
        "Leave it":
            "nothing happens"
            #he just sits there and Harper comes back and sits down at the table.
            jump start_3
        "Look through it":
            #he opens the contact app and sees a name, bryce  displayed on the screen in contacts and convinces himself nothing is happening and she gets back and yells
            harper "WHAT THE HELL ARE YOU DOING ON MY PHONE GIVE THAT BACK”
            ash "Sorry"
            $ happiness -= 2
            jump start_3
        "Turn it off":
            # it turns off the phone now is seen to be black and nothing happens

label start_3:
    "the bell rings, telling everyone next period is starting"
    scene bg locker
    "Asher grabs the lipstick"
    "When he comes back, he sees the back of Harper's head"
    "He walks closer and sees"
    "Bryce"
    "The sounds of their lips contracting"
    "Tongues twisting and twirling"
    "Spit covering their mouths"
    menu:
        "Walk away":
            "Asher sprints to the bathroom"
            ash "*sobs*"
            $ happiness -= 2
            jump toilet
        "I'll confront her later":
            $ happiness -= 2
            ash "What the hell was that?"
            harper "Bryce is just amazing and you're not, did you really think I would choose you over someone like him? He’s so much better”
            jump toilet
        "Confront them":
            $ happiness -= 4
            ash "WHAT THE HELLLL IS GOING ON”
            bryce "*laughs* It’s so pathetic that you thought harper actually liked you. I mean, come on, I'm surprised it took you so long to catch on”
            jump toilet
        "Confront Bryce later":
            #he waits until bryce notices him and then bryce laughs at him and how he’s such a loser and shoves him into a bin head first facing down and then once bryce leaves he gets out of the bin and runs away sad to the bathroom.
            $ happiness -=3
            ash "what are you doing with her"
            bryce "*laughs* you're such a loser, isn't it obvious?"
            jump toilet




label toilet:
    ash "I thought she"
    ash "She loved me"
    ash "Maybe"
    ash "She never did after all"
    ash "I'm never falling in love again!"
    ash "It was her fault"
    ash "Women are all the same"
    ash "All they do is fall for the hot bully"
    ash "And as soon as someone like me comes along"
    ash "They play with my feelings"
    ash "And watch me suffer"
    ash "Now it's my turn"
    ash "If I'm coming down"
    ash "She's coming with me"
    unknown_voice "Ash, take a second to think"
    unknown_voice "Is she really worth all that effort?"
    unknown_voice "You still have a life ahead of you"
    "Ending 1: A glint of hope"


return


