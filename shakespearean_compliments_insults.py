# imported packages to create this script/program
import random
import tkinter as tk
from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # sets the background color to gray
        self.configure(bg="gray")

        # changing the title of our widget
        self.master.title("Shakespearean Compliments & Insults")

        # allows widget to take the full space of the window
        self.pack(fill=BOTH, expand=1)

        # Generate Compliment button and it's attributes
        create_compliment = Button(self, text="Generate Compliment", fg="green", command=self.compliment_generator)
        create_compliment.place(x=50, y=100)

        # Generate Insult button and it's attributes
        create_insult = Button(self, text="Generate Insult", fg="red", command=self.insult_generator)
        create_insult.place(x=450, y=100)

        # labels display the compliment (or insult) with each button click
        self.text_one = tk.StringVar()
        self.text_two = tk.StringVar()
        self.text_one.set(" ")
        self.text_two.set(" ")

        # label displaying the generated compliments
        self.display_compliment = Label(self, textvariable=self.text_one, fg="green")
        self.display_compliment.pack()
        self.display_compliment.place(x=50, y=150)

        # label displaying the generated insults
        self.display_insult = Label(self, textvariable=self.text_two, fg="red")
        self.display_insult.pack()
        self.display_insult.place(x=450, y=150)

        # the Quit button and it's attributes
        quit_button = Button(self, text="Quit Program", command=self.client_exit)
        quit_button.place(x=335, y=250)

    # function to create the randomly generated compliments
    def compliment_generator(self):
        self.display_compliment.config(text=" ")

        # first list of compliment words
        list_one = ['airy', 'amorous', 'balmy', 'bespiced', 'beteeming', 'blazoning', 'bonny', 'brisky', 'budding',
                    'candied', 'celestial', 'chafeless', 'choicely', 'courtly', 'dainty', 'daisied', 'damasked',
                    'enchanted', 'engilded', 'fettled', 'honeysuckle', 'jovial', 'leavened', 'mannerly', 'marbled',
                    'meek', 'nonpareil', 'orbed', 'palmy', 'posied', 'replenished', 'sightly', 'silken', 'sovereign',
                    'sphery', 'sterling', 'sturdy', 'taffeta', 'tenderful', 'virtuous', 'worthy']

        # random number to choose compliment from first list
        compliment_one = list_one[random.randint(0, len(list_one) - 1)]

        # second list of compliment words
        list_two = ['all-hallown', 'alms-deed', 'brother-love', 'burley-boned', 'cheek-roses', 'crow-feathered',
                    'choice-drawn', 'deed-achieving', 'eagle-sighted', 'ear-bussing', 'even-preached', 'eye-beaming',
                    'face-royal', 'fairy-gold', 'fertile-fresh', 'full-acorned', 'gallant-springing', 'heaven-hued',
                    'honey-bagged', 'leaping-time', 'love-springing', 'life-rendering', 'marble-constant', 'May-morn',
                    'nimble-pinioned', 'nose-herb', 'parti-colored', 'proud-pied', 'right-drawn', 'silver-shedding',
                    'smoothy-pated', 'softly-sprighted', 'sweet-seasoned', 'thrice-crowned', 'tiger-footed',
                    'top-gallant', 'truest-mannered', 'weeping-ripe', 'well-breathed', 'well-flavoured', 'young-eyed']

        # random number to choose compliment from second list
        compliment_two = list_two[random.randint(0, len(list_two) - 1)]

        # third list of compliment words
        list_three = ['aglet-baby', 'argosy', 'bodykins', 'bona-roba', 'bullyrook', 'chuck', 'coach-fellow',
                      'crystal-button', 'cuckoo-bud', 'dewberry', 'eglantine', 'esquire', 'ear-kissing', 'flax-wench',
                      'gamester', 'handy-dandy', 'heartling', 'homage', 'juvenal', 'kicksy-wicksy', 'kid-fox',
                      'lambkin', 'lodestar', 'madonna', 'minstrel', 'nicety', 'pew-fellow', 'pittikins', 'prizer',
                      'primrose', 'rarity', 'ringlet', 'shoulder-clapper', 'tender-smelling', 'thunder-maker',
                      'time-pleaser', 'turtle-dove', 'wafer-cake', 'whiffler', 'wit-snapper', 'velvet-guard']

        # random number to choose compliment from third list
        compliment_three = list_three[random.randint(0, len(list_three) - 1)]

        self.text_one.set("Thou " + compliment_one + " " + compliment_two + " " + compliment_three)

    # function to create the randomly generated insults
    def insult_generator(self):
        self.display_insult.config(text=" ")

        # first list of insult words
        list_one = ['bawdy', 'brainsick', 'fat', 'false', 'foul', 'greasy', 'infectious', 'kindless', 'lecherous',
                    'paunchy', 'puking', 'qualling', 'remorseless', 'rotten', 'sanguine', 'spherical', 'starveling',
                    'vile', 'venomous', 'ugly', 'yeasty']

        # random number to choose insult from first list
        insult_one = list_one[random.randint(0, len(list_one) - 1)]

        # second list of insult words
        list_two = ['bat-fowling', 'beetle-brained', 'dismal-dreaming', 'elvish-mark', 'fat-kidneyed', 'folly-fallen',
                    'hell-hated', 'idle-headed', 'ill-breeding', 'infant-like', 'milk-livered', 'reeling-ripe',
                    'rude-growing', 'sheep-biting', 'sodden-witted', 'swag-bellied', 'tardy-gaited', 'three-inch',
                    'tickle-brained', 'toad-spotted', 'worsted-stocking']

        # random number to choose insult from second list
        insult_two = list_two[random.randint(0, len(list_two) - 1)]

        # third list of insult words
        list_three = ['bed-presser', 'biscuit', 'boar-pig', 'bull-pizzle', 'carbuncle', 'coward', 'death-token',
                      'eel-skin', 'fustilarian', 'harlot', 'hog', 'horseback-breaker', 'knave', 'madman', 'neat-tongue',
                      'ratsbane', 'rogue', 'stock-fish', 'whoson', 'villain', 'worms-meat']

        # random number to choose insult from third list
        insult_three = list_three[random.randint(0, len(list_three) - 1)]

        self.text_two.set("Thou " + insult_one + " " + insult_two + " " + insult_three)

    # close the program function
    def client_exit(self):
        exit()


root = Tk()

# size of the window
root.geometry("800x350")

app = Window(root)
root.mainloop()
