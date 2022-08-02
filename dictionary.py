animalNames = [
    "Sheep",
    "Pig",
    "Rabbit",
    "Horse",
    "Cow",
    "Unicorn",
    "Chicken",
    "Kangaroo",
    "Platypus",
    "Crocodile",
    "Koala",
    "Cockatoo",
    "Tiddalik",
    "Echidna",
    "Zebra",
    "Hippo",
    "Giraffe",
    "Lion",
    "Elephant",
    "Gryphon",
    "Rhinoceros",
    "Bear",
    "Skunk",
    "Beaver",
    "Moose",
    "Fox",
    "Sasquatch",
    "Otter",
    "Penguin",
    "Seal",
    "Muskox",
    "Polar Bear",
    "Walrus",
    "Yeti",
    "Snowy Owl",
    "Monkey",
    "Toucan",
    "Gorilla",
    "Panda",
    "Tiger",
    "Phoenix",
    "Lemur",
    "Diplodocus",
    "Stegosaurus",
    "Raptor",
    "T Rex",
    "Triceratops",
    "Dragon",
    "Ankylosaurus",
    "Wooly Rhino",
    "Giant Sloth",
    "Dire Wolf",
    "Saber Tooth",
    "Mammoth",
    "Akhlut",
    "Yukon Camel",
    "Raccoon",
    "Pigeon",
    "Rat",
    "Squirrel",
    "Opossum",
    "Sewer Turtle",
    "Chipmunk",
    "Goat",
    "Cougar",
    "Elk",
    "Eagle",
    "Coyote",
    "Aatxe",
    "Pika",
    "Moonkey",
    "Lunar Tick",
    "Tribble",
    "Moonicorn",
    "Luna Moth",
    "Jade Rabbit",
    "Babmoon",
    "Marsmot",
    "Marsmoset",
    "Rock",
    "Rover",
    "Martian",
    "Marsmallow",
    "Marsten"
]

animalPatterns = [

    # Farm

    [['X','X','X','X']],

    [['X','X'],
     ['X','X']],

    [['X'],
     ['X'],
     ['X'],
     ['X']],

    [['X'],
     ['X'],
     ['X']],

    [['X','X','X']],

    [['X','O','O'],
     ['O','X','X']],

    [['O','O','X'],
     ['O','X','O'],
     ['X','O','O']],

    # Outback

    [['X','O','O','O'],
     ['O','X','O','O'],
     ['O','O','X','O'],
     ['O','O','O','X']],

    [['X','X','O'],
     ['O','X','X']],

    [['X','X','X','X']],

    [['X','X'],
     ['O','X']],

    [['X','O'],
     ['O','X'],
     ['O','X']],

    [['O','X','O'],
     ['X','O','X']],

    [['O','O','X'],
     ['X','X','O']],

    # Savanna

    [['O','X','O'],
     ['X','O','X'],
     ['O','X','O']],

    [['X','O','X'],
     ['O','O','O'],
     ['X','O','X']],

    [['X'],
     ['X'],
     ['X'],
     ['X']],

    [['X','X','X']],

    [['X','X'],
     ['X','O']],

    [['X','O','X'],
     ['O','X','O']],

    [['O','X'],
    ['X','O'],
    ['O','X']],

    # Northern

    [['X','X'],
     ['O','X'],
     ['O','X']],

    [['O','X','X'],
     ['X','X','O']],

    [['O','O','X'],
     ['X','X','O'],
     ['O','O','X']],

    [['X','O','X'],
     ['O','X','O']],

    [['X','X','O'],
     ['O','O','X']],

    [['X'],
     ['X']],

    [['X','O'],
     ['X','X']],

    # Polar

    [['O','X','O'],
     ['O','X','O'],
     ['X','O','X']],

    [['X','O','O','O'],
     ['O','X','O','X'],
     ['O','O','X','O']],

    [['X','X','O'],
     ['X','O','X']],

    [['X','O','X'],
     ['O','O','X']],

    [['X','O','O'],
     ['O','X','X']],

    [['X'],
     ['O'],
     ['X']],

    [['X','X'],
     ['O','X']],

    # Jungle

    [['X','O','X','O'],
     ['O','X','O','X']],

    [['O','X'],
     ['X','O'],
     ['O','X'],
     ['O','X']],

    [['X','O','X'],
     ['X','O','X']],

    [['O','O','X'],
     ['X','O','O'],
     ['O','O','X']],

    [['X','O','X','X']],

    [['X','O','O'],
     ['O','O','O'],
     ['O','O','X']],

    [['X','O'],
     ['O','X'],
     ['X','O']],

    # Jurassic

    [['X','O','O'],
     ['O','X','X'],
     ['O','X','O']],

    [['O','X','X','O'],
     ['X','O','O','X']],

    [['X','X','O'],
     ['O','X','O'],
     ['O','O','X']],

    [['X','O'],
     ['O','O'],
     ['X','X']],

    [['X','O','O'],
     ['O','O','X'],
     ['X','O','O']],

    [['X','O','O'],
     ['O','O','X']],

    [['O','O','X'],
     ['X','O','X']],

    # Ice Age

    [['O','O','X','O'],
     ['X','O','O','X'],
     ['O','X','O','O']],

    [['X','O','O'],
     ['O','O','X'],
     ['X','O','X']],

    [['O','X','O','O'],
     ['X','O','O','X'],
     ['O','X','O','O']],

    [['X','O','O'],
     ['O','O','X'],
     ['O','X','O']],

    [['O','X','O'],
     ['X','O','O'],
     ['O','O','X']],

    [['O','O','X'],
     ['X','O','O'],
     ['O','O','X']],

    [['O','O','X','O'],
     ['X','O','O','O'],
     ['O','O','O','X']],

    # City

    [['X','O','X','O'],
     ['X','O','O','X']],

    [['X','O','O'],
     ['O','X','O'],
     ['O','X','X']],

    [['X','X','O','O'],
     ['O','X','O','X']],

    [['O','O','X'],
     ['X','O','O'],
     ['O','X','O']],

    [['X','O','O'],
     ['X','O','X']],

    [['X','X']],

    [['O','X','O','O'],
     ['X','O','O','X']],

    # Mountain

    [['X','O','O'],
     ['X','X','X']],

    [['X','O','O'],
     ['O','X','O'],
     ['X','O','X']],

    [['X','O','X'],
     ['O','X','X']],

    [['X','O'],
     ['X','O'],
     ['O','X']],

    [['X','X','O'],
     ['O','O','X']],

    [['O','O','X'],
     ['X','O','O']],

    [['X','O','X'],
     ['O','O','X']],

    # Moon

    [['X','O','O'],
     ['X','O','X'],
     ['O','O','X']],

    [['O','X','O'],
     ['O','O','O'],
     ['O','X','O'],
     ['X','O','X']],

    [['O','X','O'],
     ['X','X','X']],

    [['X','O'],
     ['X','X']],

    [['X','O','X'],
     ['O','O','O'],
     ['O','X','O']],

    [['X','O'],
     ['O','O'],
     ['O','X']],

    [['O','X','O'],
     ['O','O','X'],
     ['X','O','O']],

    # Mars

    [['O','X'],
     ['O','X'],
     ['X','X']],

    [['X','O','X'],
     ['O','O','X'],
     ['O','X','O']],

    [['X','X'],
     ['X','X']],

    [['O','X','O'],
     ['X','O','X']],

    [['X','O','X'],
     ['O','X','O']],

    [['X'],
     ['O'],
     ['X']],

    [['X','O','X','O'],
     ['O','O','O','X']]
]