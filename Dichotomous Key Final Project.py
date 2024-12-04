class Node: #this forms the basic 'building blocks' of the key
    def __init__(self, question, yes_branch = None, no_branch = None):
        self.question = question
        self.yes_branch = yes_branch
        self.no_branch = no_branch

def nav_key(node): #this function allows the user to navigate the key
    if isinstance(node, str): #if the current node is a string, then it is the species
        print(f"Your species is the {node}!")
        return
    print(node.question) #asks the user a question
    answer = input("Yes or No? ").strip().lower()
    if answer == "yes":
        nav_key(node.yes_branch) #follows the 'yes' branch of the key
    elif answer == "no":
        nav_key(node.no_branch) #follows the 'no' branch of the key
    else:
        print("Invalid input. Please answer Yes or No.")
        nav_key(node) #retries the current question upon an invalid user input

dichotomous_key = Node( #this defines the questions and species in the key
    "Does the animal have scales?",
    yes_branch = Node(
        "Your animal is a Reptile! Does it have a shell?",
        yes_branch = Node(
            "Your animal is a Turtle! Is it a sea turtle?",
            yes_branch = Node(
                "Does the animal have a leathery shell?",
                yes_branch = "Leatherback Sea Turtle (Dermochelys coriacea)",
                no_branch = Node(
                    "Does the animal have one pair of forehead scales?",
                    yes_branch = "Green Sea Turtle (Chelonia mydas)",
                    no_branch = Node(
                        "Does the animal have a distinctly pronounced beak?",
                        yes_branch = "Hawksbill Sea Turtle (Eretmochelys imbricate)",
                        no_branch = "Loggerhead Sea Turtle (Caretta caretta)"
                    ),
                ),
            ),
            no_branch = Node(
                "Is the animal adapted for life on land?",
                yes_branch = "Gopher Tortoise (Gopherus polyphemus)",
                no_branch = Node(
                    "Does the animal have a leathery shell?",
                    yes_branch = "Florida Softshell Turtle (Apalone ferox)",
                    no_branch = Node(
                        "Is the animal a snapping turtle?",
                        yes_branch = Node(
                            "Does the animal have a 'prehistoric' look?",
                            yes_branch = "Alligator Snapping Turtle (Macrochelys temminckii)",
                            no_branch = "Common Snapping Turtle (Chelydra serpentina)"
                        ),
                        no_branch = Node(
                            "Does the animal have a red spot by its ear?",
                            yes_branch = "Red-eared Slider (Trahcemys scripta elegans)",
                            no_branch = "Yellow-bellied Slider (Trachemys scripta scripta)"
                        ), 
                    ),
                ),
            ),
        ),
        no_branch = Node(
            "Is a grown adult of this animal bigger than you?",
            yes_branch = Node(
                "Your animal is a Crocodilian! Are its bottom teeth visible?",
                yes_branch = "American Crocodile (Crocodylus acutus)",
                no_branch = "American Alligator (Alligator mississippiensis)"
            ),
            no_branch = Node(
                "Does the animal have legs?",
                yes_branch = Node(
                    "Your animal is a lizard! Does it have toe pads?",
                    yes_branch = Node(
                        "Does the animal have distinct patterning on its back?",
                        yes_branch = "Mediterranean Gecko (Hemidactylus turcicus)",
                        no_branch = "Common House Gecko (Hemidactylus frenatus)"
                    ),
                    no_branch = Node(
                        "Does the animal have smooth, almost shiny scales?",
                        yes_branch = Node(
                            "Does the animal have a blue tail?",
                            yes_branch = Node(
                                "Does the animal have noticeably broad scales on the underside of its tail?",
                                yes_branch = "Common Five-lined Skink (Plestiodon fasciatus)",
                                no_branch = "Southeastern Five-Lined Skink (Plestiodon inexpectatus)"
                            ),
                            no_branch = "Six-lined Racerunner (Aspidoscelis sexlinneata)"
                        ),
                        no_branch = Node(
                            "Does the animal have an elongated snout?",
                            yes_branch = "Green Anole (Anolis carolinensis)",
                            no_branch = "Brown Anole (Anolis sagrei)"
                        ),
                    ),
                ),
                no_branch = Node(
                    "Your animal is a Snake! Does it have a triangular head?",
                    yes_branch = Node(
                        "Does the animal have a rattle on its tail?",
                        yes_branch = Node(
                            "Does the animal have a diamond-shaped pattern on its back?",
                            yes_branch = "Eastern Diamondback Rattlesnake (Crotalus adamanteus)",
                            no_branch = "Timber Rattlesnake (Crotalus horridus)"
                        ),
                        no_branch = "Cottonmouth (Agkistrodon piscivorus)"
                    ),
                    no_branch = Node(
                        "Does the animal have brightly colored black, red, and yellow bands?",
                        yes_branch = "Eastern Coral Snake (Micrurus fulvius)",
                        no_branch = Node(
                            "Does the animal have a yellow band around its neck?",
                            yes_branch = "Ring-necked Snake (Diadophis punctatus)",
                            no_branch = Node(
                                "Does the animal have bright patterns on its scales?",
                                yes_branch = "Corn Snake (Pantherophis guttatus)",
                                no_branch = "Eastern Rat Snake (Pantherophis alleghaniensis)"
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
    no_branch = Node(
        "Your animal is an Amphibian! Does it have a tail?",
        yes_branch = Node(
            "Your animal is either a Salamander or Newt! Does it have hind legs?",
            yes_branch = Node(
                "Does the animal have visible gill slits?",
                yes_branch = "Three-toed Amphiuma (Amphiuma tridactylum)",
                no_branch = Node(
                    "Does the animal have a flat, paddle-like tail?",
                    yes_branch = "Eastern Newt (Notophthalmus viridescens)",
                    no_branch = Node(
                        "Does the animal have grooves running from its nose to its mouth?",
                        yes_branch = "Southeastern Slimy Salamander (Plethodon grobmani)",
                        no_branch = "Tiger Salamander (Ambystoma tigrinum)"
                    ),
                ),
            ),
            no_branch = "Greater Siren (Siren lacertina)"
        ),
        no_branch = Node(
            "Your animal is either a Frog or Toad! Does it have dry, warty skin?",
            yes_branch = Node(
                "Your animal is a Toad! Does it have a vertical pupil?",
                yes_branch = "Eastern Spadefoot Toad (Scaphiopus holbrookii)",
                no_branch = Node(
                    "Does the animal have pronounced ridges on its head?",
                    yes_branch = "Southern Toad (Anaxyrus terrestris)",
                    no_branch = "Cane Toad (Rhinella marina)"
                ),
            ),
            no_branch = Node(
                "Your animal is a Frog! Does it have toe pads?",
                yes_branch = Node(
                    "Are the animal's toe pads abnormally large?",
                    yes_branch = "Cuban Tree Frog (Osteopilus septentrionalis)",
                    no_branch = Node(
                        "Does the animal have a bright line running down its side?",
                        yes_branch = "Green Tree Frog (Hyla cineria)",
                        no_branch = "Squirrel Tree Frog (Hyla squirella)"
                    ),
                ),
                no_branch = Node(
                    "Does the animal have a distinct spotted pattern?",
                    yes_branch = "Southern Leopard Frog (Lithobates utricularia)",
                    no_branch = Node(
                        "Does the animal's feet webbing reach the tip of its toes?",
                        yes_branch = "Pig Frog (Lithobates grylio)",
                        no_branch = "American Bullfrog (Lithobates catesbeiana)"
                    ),
                ),
            ),
        ),
    ),
)

def loop_key(): #main loop for restarting the key
    print("Welcome to the Herps of Florida Dichotomous Key!") #displays a welcome message upon starting the program
    while True:
        nav_key(dichotomous_key) #executes the function to navigate our key
        while True:
            restart = input("Would you like to identify another species? Yes or No?: ")
            if restart == 'yes': #resets the function to navigate the key again
                break
            elif restart == 'no': #ends the program with a friendly message
                print('Thank you for using the key! Happy herping!')
                return
            else: #retries the above question upon an invalid entry
                print('Invalid input, please answer Yes or No.')

loop_key()