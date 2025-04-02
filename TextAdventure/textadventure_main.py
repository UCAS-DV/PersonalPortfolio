import random
import math

# Code written by Darius

# Information for team: 
# The code may seem large but that's purely because most of it is dialogue, as you can see by how most of the code is orange on the right side.
# The score value is on in the player_stats dictionary on line 123.
# The way score is added is shown in Fight function on lines 1297 and 1298

# Debug Values. Do not apply to game.
skip_intro = False
debug_attacks = False
print_all_dialogue = False

game_title_screen = '''
-~-~-~-~-~-~Quest for the Country!-~-~-~-~-~-~
           Enter Anything to Start
                      '''

locations = [
    "Just a White Void",
    "Spookyland",
    "Area 51",
    "The Mythical State of North Dakota",
    "The North Pole",
    "The Roman Empire",
    "Town City",
    "British Texas",    
    "American Australia",
]
places_to_go = [
    # Just a White Void [0]
    [1, 2, 3, 4, 8],
    # Spookyland [1]
    [0, 4, 5, 6, 8],
    # Area 51 [2]
    [0, 3, 8],
    # The Mythical State of North Dakota [3]
    [0, 2, 4],
    # The North Pole [4]
    [0, 3, 5],
    # The Roman Empire [5]
    [1, 4, 6],
    # Town City [6]
    [1, 5, 7],
    # British Texas [7]
    [6, 8],
    # American Australia [8]
    [0, 1, 2, 7]
]
places_been = []
location_dialogue = [
    # White Void
    ["Boss"],
    # Spookyland
    ["Boss"],
    # Area 51
    ['Due to some unfortunate events, the government was running low on cash so they opened Area 51 to the public for tourism.', 
    'Of course, you have to sign a massive waiver to get in because of the crazy stuff happening.', 
    'For example, just last week they were testing to see if radiation from nuclear fission could be used for cereal production and they used tourists to test the quality of the cereal.',
    '...', "I'm just kidding of course.", "They don't have you sign a waiver.", 
    "Anyway, Area 51 has been effectively abandoned because apparently government facilities aren't too useful without the government.",
    'So you shrug and aimlessly wander the facility, trying to find a page but when digging around a bin with the label "Biohazard", you hear a familiar voice', '"Veep bloop glorb?"',
    "That's right, it's your childhood friend and your neighborhood's resident alien, Zeep Vorp!", '"Vlam yoop blam zeep."', '"Yeem glob tram!"', 
    "You laugh hysterically. Seems like Zeep hasn't lost his wit!", '"Yam uup glep?"', "You show him a page of the constitution and he suddenly realizes what you're doing.", 
    '"Zeee, hep jam"', 'He hands you a laser pistol, although it seems that he accidentally left a proton charge on the trigger. Classic Zeep Vorp!', 'You remove the charge, bow in gratitude, and go on your way!', '"Verplum!"'
    ],
    # North Dakota
    ['Out of boredom, you read through a page of the constitution you have and on it you notice that it mentions how the government should treat North Dakota.', 'Wait...', 
    'North Dakota?!', "There's no way...", 
    'Apparently the mythical state of North Dakota is not as mythical as commonly thought.', "Maybe the state is real but the sky cities and robot dogs and magic isn't real",
    "Well, there's no harm in checking for pages there.", "So, before you know it, you're dining with the king of North Dakota and his robot dog in a city 1000 meters up, levitated with magic.",
    'This is... odd, to say the least.', 'Anyways, you show the king your page and he explains he has not seen anything like it so after you finish eating you decide to go on your way',
    'He hands you a slab of "Northdakotium" and wishes you safe travels.', 
    "He forgot to explain to you what it does, assuming that you already know, so you don't really know what to do with it", "It's a nice gift so you're still happy."],
    # North Pole
    ['Boss'],
    # Roman Empire
    ['Somehow, someway, the Roman Empire was able to reform fully within the borders of EMUSA.', "Apparently, they were able to revive Julius Ceaser and now he's the governor.",
    "Anyway, you're probably famous enough from your previous battles so that you can just talk to the governor.", 
    'So after struggling to get an appointment (they kept putting you on hold), you are able to speak with Ceaser in his office.', 
    'Oddly enough, when you walk in, you can hear cheering from what seems to be an audience', "So, I don't know how to put this but, Julius Ceaser is...", "Let's just say...", 
    'A giant hulking mass of wires and machinery on wheels with a paper cut out of the face of Julius Caeser on the head of it...', 
    'You try to ignore that and you hold up a page of the constitution and point to it.', 'Ceaser replies "BAJUNGA" and you can hear an uproarious laughter.', 
    'You turn your head and realize this is all happening in front of a live studio audience.', "You're not quite sure how you didn't notice earlier", 
    'Anyway, Ceaser tells you:', '"SEEN_PAGES = FALSE. PAGES MAY BE IN... GENERATING JOKE... CHAIR"', 
    'You almost went deaf from the laughter. You shrug and decide to leave but before you leave Ceaser stops you',
    'WAIT. I HAVE AN ITEM FOR YOU.', 'He pulls out a book from his robotic chest cavity. He hands it to you. The title reads "The Amazing Guide for Conflict by Super-Robo-Caeser."', 
    'You bow in gratitude and leave.', 'Not really sure what that was supposed to do'],
    # Town City
    ['Boss'],
    # British Texas
    ["Oh, wow.", 'This place is beautiful.', 'Just you, me, and the vast outback.', "Isn't this the dream?", 
    "Hey, after this, we should move here and make a small little wood cabin out here.", 'No country to save.', 
    'No constition to restore.', 'No unpaid internship.', 'No living skeletons or off-tone metaphors.', 'What could go wrong?', 'Oh I know!', 
    'A giagantic swarm of dangerous wildlife that go out to horizon could come at us.', "I'm talking about snakes with gigantic longswords and battle axes.", 
    'Koalas on orbital death rays capable of erasing a continent off of the map.', 'Kangaroos, no further details.', 'Oh, oh!', 'What if there were also emus in WW2 era tanks?',
    'That would be crazy!', "Like, I'm talking about a swarm like the swarm that's coming right toward us right now!", 'Wait.', '[One really amazing, spectacular fight later]',
    'Well, that sucked.', "I'll give you credit, that super backflip you did to ward off the zombie dingos was art.", 'Oh, hey! One of the snakes left their longsword!'],
    # American Australia
    ['W-what are you doing?!', "You can't possibly be... no no no no no... be reasonable here!", "We can look for the pages else where I promise!", 
    "PLEASE, I DON'T WANT TO GO TO AMERICAN AUSTRALIA (what you may know as Texas).", 'sigh...', 'You go do some stuff in American Australia or something or whatever.',
    'Also, there was no pages so we just wasted our time!', 'Congratulations!', "We didn't even get an item or anything.", 
    'Whenever we tried to talk to someone, they just yelled at us to get off their property.', 'We were on the other side of the street!', 
    'You know what, you see that tumble weed over there.', 'Yeah, that one.', "Let's just grab that and call it this location's item."]
]

player_stats = {
    "health": 100,
    "nerves": 100,
    "strength": 0,
    "bravery": 0,
    "durability": 0,
    "recovery": 0,
    "max_health": 100,
    "max_nerves": 100,
    "min_nerves": 25,
    "attack_potency": 1,
    'recovery_potency': 1,
    'pages': 0,
    'level': 0,
    'position': 0,
    'score': 0
}

player_attacks = [
    {
        "name": "Uncouth Declaration",
        "description": '''Forget physical damage! Emotional damage is where it's at!''',
        "health_effect": 0,
        "nerves_effect": -20,
        'to_player': False,
        "super_success": ["Oh...", "wow...", "I get how intense this situation is but you didn't have to go that far.", "To be frank I don't even know if you can legally say that."],
        "success": ["Oh! He's absolutely devastated!"],
        "failure": ["Okay, so, pro tip...", 'Calling your opponent "Stinky" is not very effective past the first grade'],
        "super_failure": ["What was that?!", "That is likely the single most tame, polite sentence ever constructed"],
        "is_item": False
    },
    {
        "name": "School-Appropriate Attack",
        "description": '''Deal damage to your opponent in a very school appropriate way with one simple trick!''',
        "health_effect": -15,
        "nerves_effect": 0,
        'to_player': False,    
        "super_success": ['Oh my!', 'That attack was not only devasting, but incredibly appropriate and conducive to a learning enviornment!', "Incredible!"],
        "success": ['Whoa!', 'Bet they never saw that School-Appropriate Attack coming!'],
        "failure": ['I mean,', 'it was an attack alright, but it was not very conducive to a learning environment so you basically failed.', 
        "Also the fact you almost completely missed is why you failed but that's irrelevant"],
        "super_failure": ['Whoa! Whoa! Whoa!', 'Not only did you miss that attack horrendously,', 'That attack does not represent a growth mindset!', 'Shame!'],
        "is_item": False
    },
    {
        "name": "Deep Breaths",
        "description": '''Breathe in... Breathe out... Feels better right?''',
        "health_effect": 0,
        "nerves_effect": 25,
        'to_player': True,
        "super_success": ['You not only decided to do deep breaths.', 'You went further and did box breathing', 
        'In the distance you can hear every school councillor and therapist rejoice.'],
        "success": ['You decide to take some deep breaths to help your nerves.'],
        "failure": ["Huh,", "Apparently it's hard to find time to do some deep breathing in the midst of battle. You still somehow found a little time so it's alright."],
        "super_failure": ["Yeah,", "so it's a little hard to practice proper breathing tactics in the middle of battle so you weren't able to do any deep breathing at all."],
        "is_item": False
    },
]

items = [
    {
        "name": "High Hopes and Determination",
        'description': "Well, this isn't quite what you signed up for but your main character syndrome stops you from letting your country fall.",
        "health_effect": 30,
        "nerves_effect": 30,
        "to_player": True,
        'use_text': ["While on the ropes, it all comes back to you in a flash.", 
"You remember who you truly are.",
"You are not someone to be defeated by mere fatal injuries.",
"This journey has reminded you that, not only you have friends and a family to come back to, but everyone in this country you've been fighting for has people to come back to as well.",
"You are suddenly filled with high hopes and determination."],
        'is_item': True
    },
    {
        'name': 'Skull of Mr. Skellybones',
        'description': f'"Raaah. Thank you. Let us save our country. For Spookyland!"',
        'health_effect': -10,
        'nerves_effect': -40,
        'to_player': False,
        'use_text': ['You pull out the skull of Mr. Skellybones.', '"RAAAAAAAAHHHHHHHH! I AM MR. SKELLYBONES AND I AM A MAN!"', 
        '"I HAVE COME TO TELL YOU THAT ALL OF YOUR CELLS ARE REPLACED EVERY 7-10 YEARS!"',
        "Your opponent sits down in complete terror as they contemplate the implications of that fact.", 
        'As they start muttering to themselves about the Ship of Theseus, Mr. Skellybones tells you, "I am sorry, that is all I can muster without any milk to fuel me."', 
        'Well, given how shaken your opponent is, maybe you did make the right call bringing him along.', f'Great job!'],
        'is_item': True
    },
    {
        "name": "Laser Blaster",
        'description': 'A state of the art plasma pistol designed by the best of Vorlom and made in China!',
        "health_effect": -35,
        "nerves_effect": 0,
        "to_player": False,
        'use_text': ['"Pew Pew!"', 'A flurry of deep blue rays of plasma cover your opponent.', 
        "As your opponent panics as to what to do, you try to fire several more shots but it seems its jammed", 'You look down at the display on the gun. It reads:',
        '"You have reached the limit for free shots from this weapon. If you wish to fire more, join Laser Premium for $8.99 a week."', 'Gross...', 
        'You shrug and chuck the blaster at your opponent.', 'It lands and they reel from the collision. They place an icepack on their head and the battle continues.'],
        'is_item': True,
    },
    {
        "name": "Slab of Northdakotium",
        'description': "You're not quite sure what to do with it but it's a nice gift.",
        "health_effect": 50,
        "nerves_effect": 0,
        "to_player": True,
        'use_text': ['In despiration, you pull out your slab of Northdakotium.', "You then pause as you realize you don't really know what to do with it.", 
        'You shrug and take a bite out of it for some reason?', 'Why was that the first thing that you thought to do?', 
        'Anyway, after taking a bite out of a literal block of metal, you suddenly feel siginficantly healthier for some reason?', 'Huh.', 
        'That should not have worked but what works, works, I guess.'],
        'is_item': True,
    },
    {
        "name": "Boat",
        'description': "Yay! We can now go to British Texas!",
        "health_effect": 0,
        "nerves_effect": 0,
        "to_player": True,
        'use_text': ['You decide to sail the 7 seas to British Texas!'],
        'is_item': True,
    },
    {
        "name": "GIGANTIC LONGSWORD",
        'description': "How the heck was a snake able to hold this? It's taller than you!",
        "health_effect": -65,
        "nerves_effect": 0,
        "to_player": False,
        'use_text': ['You pull out a gigantic, 3 meter longsword from your back pocket.', 
        'The fear that you were able to strike in your enemy purely by wielding it incites a heart attack in your enemy.',
        'Somehow, they recover partially within just 15 minutes but damage has been done.', 'As you watch your opponent recover, you accidentally drop the sword and it breaks in two.',
        'Oops.'],
        'is_item': True
    },
    {
        'name': 'The Amazing Guide For Conflict by Super-Robo-Caeser',
        'description': "I'm getting the feeling that this isn't the real Julius Caeser...",
        'health_effect': 0,
        'nerves_effect': 60,
        'to_player': True,
        'use_text': ["You decide to quickly read Super-Robo-Caeser's book.", 
        "You were the fastest reader back in high school so you were easily able to blow through the 700 page book in about 5 minutes", 
        "You didn't understand any of it (I never said you understood any of the books you read in high school) but you feel more confident in your abilities."],
        'is_item': True
    },
    {
        'name': 'A Single Tumbleweed',
        'description': "This is why I don't go to American Australia. Well I don't really go anywhere since I don't exist. But if I could, I would go to somewhere cool instead!",
        'health_effect': -10,
        'nerves_effect': -10,
        'to_player': False,
        'use_text': ["You decide that you might as well use your Tumbleweed since it's been cluttering your inventory", 
        'You pull it out of your back pocket and gently roll it towards your opponent.', "They're mildly annoyed at the tumbleweed and the tiny thorns bother them.",
        'Congrats?'],
        'is_item': True
    },
    {
        'name': "Santa's Hat",
        'description': "Legend says that whoever holds his hat, holds his armies of elves. I'm not sure if elves will be good fighters but it's worth a shot!",
        'health_effect': -50,
        'nerves_effect': -25,
        'to_player': False,
        'use_text': ["In a last ditch effort, you pull out Santa's hat, and wear it.", 'You intially feel nothing but shaking.', 'You seem to be more nervous than you think...',
        'or...', "there's something else at play.", "Suddenly, Santa's hat glows brightly and your opponent is shutters at the overwhelming amount of Christmas Spirit displayed.",
        "You don't feel shooken by the Christmas Spirit at all but you are shooken by what feels like a whole battalion charging to your position.", "It's the elves?!",
        'A familiar voice calls to you, "Hey! We got ya covered!"', 
        "The elves pester your opponent and although they have the power of an athletic 6 year old, your opponent is no match for their sheer numbers.", 
        'Eventually, your hat seems to run out of Christmas Spirit and the elves shrug and leave.', '"We hope to see ya later!"', "I honestly didn't think that would work."],
        'is_item': True, 
    }
]
location_items = [
    # Just a White Void (No Item)
    {},
    # Spookyland (No Item)
    {},
    # Area 51
    items[2],
    # North Dakota
    items[3],
    # North Pole (No Item)
    {},
    # Roman Empire
    items[6],
    # Town City (No Item)
    {},
    # British Texas
    items[5],
    # American Australia
    items[7]
]

inventory = []

if debug_attacks:
    player_attacks.append({
        "name": "Falcon Punch",
        "description": '''Insta-Kill for Debugging''',
        "health_effect": -1000,
        "nerves_effect": -1000,
        'to_player': False,
        "super_success": ['The Debugging is Debugging Greatly'],
        "success": ['The Debugging is Debugging'],
        "failure": ['The Debugging is Kinda Debugging'],
        "super_failure": ['The Debugging is Not Debugging'],
        "is_item": False
    })
    player_attacks.append({
        'name': 'Resign',
        'description': 'Instant Game Over for Debugging',
        "health_effect": -1000,
        "nerves_effect": -1000,
        'to_player': True,
        "super_success": ['The Debugging is Debugging Greatly'],
        "success": ['The Debugging is Debugging'],
        "failure": ['The Debugging is Kinda Debugging'],
        "super_failure": ['The Debugging is Not Debugging'],
        "is_item": False
    })

reward_attacks = [
    {
        "name": "Pep Talk",
        'description': 'No pain can beat out the power of a good pep talk!',
        "health_effect": 15,
        "nerves_effect": 0,
        "to_player": True,
        "super_success": ['You give such an incredible, rousing self pep talk that even your enemy feel a little inspired.'],
        "success": ['You give yourself a pep talk and feel inspired by your own words.'],
        "failure": ['You try to give yourself a pep talk but you suck at public speaking so it proves ineffective,', "even though the only person it's directed to is yourself."],
        "super_failure": ['...', "That was...", 'something.', "Don't beat yourself up about it,", 'just ensure that you will never have to do any sort of public speaking...', 'ever...'
        "and you'll be fine!"],
        'is_item': False
    },
    {
        "name": "Funny Bone Blow",
        'description': "HEY! This is no laughing matter!",
        "health_effect": -20,
        "nerves_effect": 0,
        "to_player": False,
        "super_success": ["You look at your opponent with a deadpan expression", 'You walk up to your opponent, menacingly and your mere aura brings them to your knees.',
        "You lightly taps their funny bone.", "He looks at you confused but suddenly... what feels like a jolt of lightening traverses through their arm and you can infer the rest"],
        "success": ['You hit their funny bone in a very unfunny way'],
        "failure": ['You try to hit their funny bone in a very unfunny way but you only lightly tap it'],
        "super_failure": ["You try to hit your enemy's funny bone but you miss terribly.", 
        'You fall to the ground from the missed swing and you contemplate why you were even bothering with this quest.',
        'Your opponent pities you and encourages you to get back into the fight.', 'Eventually, the fight continues.'],
        'is_item': False
    },
    {
        "name": "Investment",
        'description': "You watched one guide on stock trading and now you believe you're an expert.",
        "health_effect": 30,
        "nerves_effect": -20,
        "to_player": True,
        "super_success": ['Despite having absolutely 0 experience in stock trading, you discovered this trick called "Fraud" and you were able to make a ton of money,', 
                          'which is time,', 'which is health.' ],
        'success': ['You hesistently decided to invest in stocks of several Wealth200 companies and since time is money and health is time, you were able to increase your health.'],
        "failure": ['You hesistently decided to invest in stocks based off of advise from several online forums.', 
                    'By the most incredible stroke of luck the world has ever seen, you were able to profit, but not by much.'],
        "super_failure": ['You invested in crypto currency.'],
        'is_item': False
    },
    {
        "name": "Intimidating Christmas MegaBlast",
        'description': "You're no where near cool enough to actually preform a Christmas MegaBlast but you can start one up to scare your opponents",
        "health_effect": 0,
        "nerves_effect": -25,
        "to_player": False,
        "super_success": ['You begin to charge up a Christmas MegaBlast.', 'The charged blast is significantly more powerful than you projected.', "You can likely see it from space.",
        "You don't know how this happened.", 'All you know is that your optometrist will likely be livid.', 'You then shrug and cancel the blast.'],
        'success': ['You begin to charge up a Christmas MegaBlast of your own.', "You're enemies quiver in fear as you charge the blast, but then you shrug and cancel it."],
        "failure": ["You begin to charge up a Christmas MegaBlast and they panic for a little bit, until they realize that you've been charging it for more than 5 minutes now.", 
        'So they shrug, walk up, and knock your hat off your head.'],
        "super_failure": ['You charge up your Christmas MegaBlast but then,', 
        "you remember that one, really funny video you watched like 3 months ago and the restraint you're exercising to not laugh breaks your blast.",
        "You figure that you might as well show your opponent the video since it's stuck in your head so you have to watch it anyway.", 'Your opponent basically dies laughing at the video.',
        'Your opponent then tells you about how that video reminded them of their former passions.', 'The two of you have a jolly time as your opponent reveals more about themselves.',
        'Eventually, the two of you exchange phone numbers and the fight continues.', "Sadly, since you did not bring your opponent's nerves down, I must say that..."],
        'is_item': False
    }
]
boss_attacks = [
    # The Voice in Your Head
    [
        {
            "name": "Terrible Pessimism",
            "health_effect": 0,
            "nerves_effect": -10,
            "to_player": True,
            "super_success": ["To be frank, given how absolutely dysfunctional the country was,", "with the Roman Empire, and Santa Claus, and them causing trouble",
            "I don't even think it's worth it."],
            "success": ["I'm going to be honest, I don't think we, an unpaid intern and a voice in that intern's head can save America like Mr. President wants us to."],
            "failure": ['I believe that you will make a mistake at some point in time!', 'Take that!'],
            "super_failure": ['I have so many negative things to say but they bum me out too so I will just take the L on this turn and not say it.']
        },
        {
            "name": "Pep Talk",
            "health_effect": 10,
            "nerves_effect": 0,
            "to_player": False,
            "super_success": ['I give myself such an incredible, rousing self pep talk that even you feel a little inspired.', 'Wow, I should really pursue public speaking!',
            "You know, I think I might do so!", 'Yeah...', 'wait, the only person who can hear me is you.', '...', 'Ow.'],
            "success": ['I give myself a pep talk and feel inspired by my own words.'],
            "failure": ["You know...", 'I am so happy that the only person who can hear me is you.'],
            "super_failure": ['Um...', "I thought I would be better at speaking given that it's the only thing I can do.", 'Just...', 'please forget everything I just said.']
        },
        {
            "name": "Unbearable Yell",
            "health_effect": -10,
            "nerves_effect": -5,
            "to_player": True,
            "super_success": ['NO, YOU DID NOT WIN THAT ONLINE ARGUMENT LAST NIGHT!', 'YOU WERE JUST FLAT OUT WRONG!'],
            "success": ["THE ORIGINAL MOVIE WASN'T THAT GOOD!", "YOU ARE JUST LOOKING AT IT WITH ROSE-TINTED GLASSES!"],
            "failure": ['aaaaaaa?'],
            "super_failure": ['Um...', 'uh...', "I don't have anywhere near enough energy to yell."]
        },
        {
            "name": "Positive Affirmations",
            "health_effect": 0,
            "nerves_effect": 10,
            "to_player": False,
            "super_success": ['I mutter the most incredibly positive affirmations you have ever heard.', 'Even you feel a little inspired by my affirmations!'],
            "success": ['I mutter a bunch of positive affirmations to myself to make myself feel better.'],
            "failure": ['I mutter a bunch of positive affirmations but I felt almost nothing.'],
            "super_failure": ['I am going to lose this fight.', "Wait.", "That isn't very positive.", 'I am going to lose this fight,', 'yet.', 
            'See! I have practice a growth mindset!']
        }
    ],
    # Mr. Skellybones
    [
        {
            "name": "Funny Bone Blow",
            "health_effect": -20,
            "nerves_effect": 0,
            "to_player": True,
            "super_success": ["With what you think is a deadpan expression", "(you can't really tell because he's just a faceless skeleton)", 
                              "He lightly taps your funny bone.", "You look at him confused but suddenly... what feels like a jolt of lightening traverses through your arm and-",
                              '...', '...', 'You good?', 'It seems like your brain was too focused on writhing in very unfunny pain to remember to conjure my existence.', "Uh, don't do that again.",
                              "It's kind of a buzzkill."],
            "success": ['He hits your funny bone in a very unfunny way'],
            "failure": ['He tries to hit your funny bone in a very unfunny way but he only lightly taps it'],
            "super_failure": ['He tries to hit your funny bone but he trips and hits his own funny bone.', 'He lays on the ground immobilized as you look down at him with pity.',
                              '"THIS IS NOT FUNNY RAAAAAAH"', 'Eventually he gets his footing and the battle continues.']
        },
        {
            "name": "Disturbing Truth",
            "health_effect": 0,
            "nerves_effect": -20,
            "to_player": True,
            "super_success": ['He walks up to you and whispers to you...', '"Raaaah."', '[My lawyer has advised me to remove the following dialogue]'],
            "success": ['"Raaaah. 2017 was 7 years ago."', 'You feel disturbed.'],
            "failure": ['"Raaaah. Some people are poor."', 'You feel a little bummed out.'],
            "super_failure": ['Mr. Skellybones tries to disturb you but it ended up being such a blatant truth that you feel nothing.', 'You look at him with a deadpan expression.', 
                              'He feels a little embarressed.']
        },
        {
            "name": "Got Milk?",
            "health_effect": 20,
            "nerves_effect": 0,
            "to_player": False,
            "super_success": ['He reaches behinda grave and grabs a jug of Clarkplace(TM) milk.', '"Raaaah. Only Clarkplace Milk(TM) makes feel this good."', 
            '"You can find Clarkplace Milk(TM) at your local PriceCo(TM) for only $4.29"', 'He tilts his skull in what you think is a wink and drinks the whole cartoon.', 
            'He looks significantly more health y.'],
            "success": ['He reaches behind a grave and grabs a jug of Awesome Price(TM) milk.', 'He drinks it and looks revitalized.'],
            "failure": ['He reaches behind a grave and grabs a jug of expired Awesome Price(TM) milk.', "He drinks it and seems disgusted, you can't tell because he's just a skeleton."],
            "super_failure": ['He reaches behind a grave and grabs an empty jug of Clarkplace milk.', 'He looks at the jug with despair.', '"Raaaah. Why did you have to leave me too dear Kirkland Milk"',
            'You reconcile him as he despairs', '"Raaaah. Thank you"', "Now that he's feeling better, you hug and then continue the fight"]
        },
    ],
    # Metaphor for Capitalism
    [
        {
            "name": "Deep Allegory",
            "health_effect": 0,
            "nerves_effect": -15,
            "to_player": True,
            "super_success": ['"And so, the rat suplexed the snake into the sun, saving the galaxy."', 'You feel extremely confounded at the story he just told.', '"Do you honestly not understand such a simple allegory? You truly are an imbecile."',
                              'He then walks up to a small child, no older than 4, and tells him the story. The child replies:', '"Wow, thwat was a bwilliant allegowy for the state of amewican society since the adwent of mass media."',
                              "You've never felt stupider."],
            "success": ['He tells you a story about a rat, snake, and bird saving the galaxy from a super death laser.', "Apprently it's supposed to be a really deep allegory about something but you don't get it so you feel stupid"],
            "failure": ["He tries to tell you a story but you can barely hear him because of all of the city noises. You feel confused about what you did hear but you didn't hear all too much so you don't feel too stupid."],
            "super_failure": ['He tries to tell you a story but he keeps forgetting where he is in the story.', 'It takes him about 45 minutes for him to tell the 10 minute story.'],
        },
        {
            "name": "Bribery",
            "health_effect": -20,
            "nerves_effect": 0,
            "to_player": True,
            "super_success": ['He pulls out his phone from his pocket and calls someone:', "Hello General Monger, would you kindly take care of the gentleman I am currently engaged in combat with? I will reward you greatly if you do so.",
                              "About 5 minutes later the enterity of main street is nothing but rubble and ash.", "Fortunately, the general completely failed at attacking you, so you're unscaved...", 'Until you trip and scrape your knee.'],
            "success": ['He pulls out his phone from his pocket and calls someone:', '"Hello Mayor Michells, if you would be so kind as to suplex this gentleman in front of me, I will reward you greatly."', 
                        'He hangs up and suddenly, you feel someone grab you and suplex you. As you recuperate, you see the Metaphor hand the Mayor a briefcase. The Mayor leaves gleefully.'],
            "failure": ["He tries to call someone on his phone but it seems that he has no service, so he just throws a briefcase filled with $100 bills."],
            "super_failure": ['He tries to call someone on his phone but before he can make the call, a bunch of IRS employees tackle him.', 'Shockingly, the multibillionare has violated several tax codes.', 
                              'Somehow, he is able to fend off all 23.6 of them on his lonesome using nothing but shear will.', "I'm just kidding, he just threatened to dock their pay because he's friend with Commisioner of Internal Revenue.",
                              "After they leave, he tries to call someone on his phone but apparently he has no service."]
        },
        {
            "name": "Investment",
            "health_effect": 35,
            "nerves_effect": 15,
            "to_player": False,
            "super_success": ['"You know what?"', '"I will just commit fraud"', '"I will not stand for market instability"', "He shurgs and does a bunch of stuff you don't understand."],
            'success': ['He sells his stocks in a major company, gaining millions of dollars to afford healthcare.', 
            'He is significantly more healthy.'],
            "failure": ['He tries to sell his stocks in a major company but the companies stock price was falling, so he only got a quarter as much money as he wanted.'],
            "super_failure": ['He decided to invest in crypto currency.'],
            'is_item': False
        }
    ],
    # Santa Claus
    [
        {
            "name": "Christmas MegaBlast",
            "health_effect": -25,
            "nerves_effect": 0,
            "to_player": True,
            "super_success": ['"Hohoho!"', '"I did not want to go this far but I will if I must."', '"I CALL UPON EVERY GREAT POWERS BEFORE I,"',
            '"FROM FATHER CHRISTMAS TO KRIS KRINGLE,"', '"I HARNESS THEE FOR A..."', '"CHRISTMAS"', '"ULTRA"', '"BLAST!"', "For a moment, all you can see is red, green, and white.",
            'Once the blast is over, you notice a several meter wide whole blasted through the wall behind you with a trail spanning to the horizon.', 'How did you even survive that?',
            'Do you have plot armor or something?'],
            'success': ['Santa harnesses his Christmas Spirit and does his iconic and famous Christmas MegaBlast,', 
            'Completely blinding you in its brilliance.', 'Oh, classic Santa!'],
            "failure": ['Santa attempts to harness his Christmas Spirit but it seems that the stress of preparing for Christmas has gotten to him.', 'His spirit is considerably weaker.'],
            "super_failure": ['"Hohoho!"', '"I wanted to go this far as much as you but you leave me no choice"', '"CHRISTMAS"', '"SUPER"', '"BLA-"', 'His hat falls off his head, cancelling his attack',
            '"Oh! Pardon me!"'],
            'is_item': False
        },
        {
            "name": "Intimidation",
            "health_effect": 0,
            "nerves_effect": -20,
            "to_player": True,
            "super_success": ['Santa walks up to you and places a hand on your shoulder.', '"114.234.123.65"', '"Am I correct?"'],
            'success': ['Santa pulls out his naughty list and he writes a name in it.', 'You stress out, worried that he put your name on the list.'],
            "failure": ["Santa begins to charge up a Christmas MegaBlast and you panic for a little bit, until you realize he's been charging it for longer than usual.", 
            'So you  shrug, walk up, and knock his hat off his head.'],
            "super_failure": ['"Why you have tested me patience for too long!"', '"I am going to say a horrible thing!"', '"You will not even believe what I am about to say!"',
            'You stress out, worried that Santa is going to destroy his precious, pure image. You brace for the worst.', '"YOU ARE SUBPAR IN SOME OF YOUR HOBBIES!"', 
            '"do not worry though, practice makes perfect"', '"BUT YOU WILL HAVE TO PRACTICE A LOT!"', 'Santa smirks, proud of his own audacity.'],
            'is_item': False
        }
    ],
    # Zeep Vorp
    [
        {
            'name': 'Proton Charges',
            'health_effect': -35,
            'nerves_effect': 0,
            'to_player': True,
            "super_success": ['You notice a $20 at your feet so you pick it up, feeling lucky as ever,', "just to realize that you actually picked up a Proton Charge.",
            '...', 'In retrospect,', "I'm not sure how you made that mistake."],
            'success': ['Using the ever-so-lovely power of nuclear fission, Zeep sets off several Proton Charges at your feet.', "You know, the Zeep I know would've used Neutron Blasts.",
            "I should've known he would go down this path from the moment I saw that first charge."],
            "failure": ['Zeep throws several Proton Charges at your feet, but it seems he set them to "Inconvinence" instead of "Illegal in All Places except American Australia"'],
            "super_failure": ["Zeep Vorp being the massive stinky stupid idiot he is forgets to activate his Proton Charges when he throws them at us because he's stupid and dumb."],
            'is_item': False
        },
        {
            'name': 'Regenerate',
            'health_effect': 20,
            'nerves_effect': 15,
            'to_player': False,
            "super_success": ['Zeep somehow created a better, more evolved version of himself who kicked him out of the mech, fixed the mech, and took charge himself.'],
            'success': ['In what I can only describe as a crime against biology,', 'Zeep duplicates himself several times to tend to him and fix his ship as he pilots it.'],
            "failure": ["Zeep duplicates himself several times to tend to him and fix his ship, but apparently it's hard to repair a flying mech's external wounds, as it is flying,",
            'So nothing really gets done.', "They were able to stick a princess-branded bandages on it so I'm sure it's fine."],
            "super_failure": ['In what I can only describe as an attempted crime against biology,', 'Zeep duplicates himself several times to tend to his own wounds and fix his ship as he pilots it...',
            'but he forgot to duplicate his conscious so the clones just run off on their own endeavors.', "I hope they're okay, wherever they went."],
            'is_item': False
        },
    ]
]
bosses = [
    {
        "name": "The Voice In Your Head",

        "health": 50,
        "nerves": 100,
        "max_health": 50,
        "max_nerves": 100,
        "min_nerves": 25,
        'def_health': 50,
        'def_nerves': 100,
        
        "victory_item": items[0],
        'score': 100,

        "location": 0,
        'index': 0,

        "intro": ["...", 'Wait a second...', "You don't know how to fight, do you?", "Well, these guys are not going to willing give up their pages so let's learn.",
        "I'm sure you're already familiar with how health works, but people often underestimate how important it is to keep a cool head.", 
        "You see, if you let your nerves get too low, you're attacks' effectiveness will likely be greatly reduced, or worse, they'll completely fail.",
        "If you keep cool and have high nerves, you're attacks won't only be likely to land properly, they may even be more powerful.", 
        'The same goes for your enemies. So make sure to maintain high nerves for yourself, and reduce their nerves.', 
        "Don't worry if you get too nervous, you will likely have items you collect from bosses or location that you can use as hail marys, regardless of your nerves.", 
        "Although, you can only use them once so be conservative with your item use.",
        "Also, if things get too bad, there's a minimum value your nerves can fall under. Although sadly, your enemies also have a minimum nerves value.",
        "Now that we have that settled, let's begin! I'll be your first boss so you can apply your new knowledge.", 
        'By the way, to traverse menus, you must enter the numbers of the options and if you enter a menu you wish to exit, type anything but the selected options.'],

        "boss_victory_text": ["Oh!", "How did you...", "I don't even exist!", "Wait, if you're gone, and I'm in your head, what does that mean for me?", "...", "Uh oh."],

        "boss_defeat_text": ["Wow! Bravo! Now that you know how to battle, it seems like you're ready to save the country and retrieve the pages!", 
                             "And don't worry, since I don't exist, I'm completely fine!", "I'll never leave...", 
                             "Anyways, now that you've defeated me, you will get my item and be given the opportunity to upgrade one of your stats.", 'You have 4 stats:',
                             'Strength, which increases the power of your offensive attacks,', 'Bravery, which increases your maximum and minimum amount of nerves,',
                             'Durability, which increase your maximum health,', 'And Recovery, which increase the power of attacks that boost you.', 
                             'Also, you will pick up attacks from your opponents and you can learn one of them if you want', "But you're brain isn't limitless, so you'll have to forget an attack to make up for it.",
                             'Keep that in mind when deciding whehter or not you want to learn their attack.',
                             "Anyway, usually you will get a page from defeated bosses but I don't have any pages to give-",
                             "You look down at your feet to see you're standing on a page of the constitution.", "Well that's convienient."],

        "is_defeated": False,
        'encountered': False,
        'level_last_encountered': 0
    },
    {
        "name": "Mr. Skellybones",

        "health": 60,
        "nerves": 100,
        "max_health": 60,
        "max_nerves": 100,
        "min_nerves": 25,
        'def_health': 80,
        'def_nerves': 100,

        "victory_item": items[1],
        'score': 500,

        "location": 1,
        'index': 1,

        "intro": ["As you traverse the spookyland, you can feel chills go down your spine", 'As you go, you see a variety of ghouls, ghosts, zombies, and skeletons living their lives.'
                  "You've always heard tales about the scariness of spookyland but you never believed it",
                  'I mean, back in grade school folks would say that spookyland was ruled by a living skeleton called Mr. Skellybones.', 'How absurd...', 
                  'How could you tell it is a "Mr." if it is just bones?', "It just doesn't make sense", 'Anyway, you cautiously traverse the dark and cool landsc-',
                  '"RAAHHHHHHHHHHHHHH!"', '"IT IS I, MR. SKELLYBONES AND..."', '"I AM A MAN"', '"RAHHHHHHHHHHHHH!"', 
                  "AAAAA!", "You quiver in fear, hoping to pass through peacefully. Hopefully this detour will end so we can go back to getting the pa-", 
                  'You see a piece of parchment in his hand.', 'Uh oh...'],

        "boss_victory_text": ['"Raaaah. No one can withstand Mr. Skellybones!"', 'Hint: Skellybones thrives off of your fear, so keep cool and give him a taste of his own medicine.'],

        "boss_defeat_text": ['The skeleton looks up at you and suddenly collapses.', 'His bones are everywhere.', '"Raaaah, you have defeated me. What do you wish to do with me?"',
        'You walk to his hand and grab the page of the constitution and you begin to walk away.', 
        '"Raaaah. I see. Spookyland has been long neglected these days. We have not been as scary as we used to since my father retired"', 
        '"Raaaah. I hoped that I could hold the government hostage, so that they would support my people and I."', "Just a reminder, you have the page now, you can go now.",
        '"Raaaah. You have no reason to fulfill any request from me, but I ask for my people, please do not let us fall into the shadows"', 'Well, that sucks for him, you walk away and-', 
        'What are you doing?', 'You nod and gently pat him on the head.', '"Raaaah. Thank you. If you are truly dedicated to saving Spookyland, wherever you go, take me with you and I will assist you as best as I can."', 
        "You ignore the skeleton who was attacking you just 5 minutes ago because that's the normal thing to-",
        'Are you serious?', 'You pick up his skull and nod again.', 'Well, fine then, I guess he may be useful in battle.'],

        "is_defeated": False,
        'encountered': False,
        'level_last_encountered': 0
    },
    {
        "name": "A Very Deep and Subtle Metaphor for Capitalism that Only Intellectuals",

        "health": 60,
        "nerves": 80,
        "max_health": 120,
        "max_nerves": 120,
        "min_nerves": 15,
        'def_health': 50,
        'def_nerves': 80,

        "victory_item": items[4],
        'score': 300,

        "location": 6,
        'index': 2,

        "intro": ['Welcome to Town City, your home town.', "Why isn't it great to be home!", 'Air: Polluted', "Tap Water: Don't Drink", 'Crime: Of Course', 'Labor Laws: Ignored', "Truly lovely isn't it?",
        "Although, given how big this city is, if there's a page here, there's no way that we could find it anytime soon.", "Well then, let's go searching.", 
        'You traverse all throughout the city, going down a pleasant trip on Memory Lane.', 'As you peacefully go around, you notice a black limousine go through the street.', 
        'It quite literally stretches all of the way down to the horizon.', 'As you ponder who such a car would turn, you see well dressed gentleman exit right behind the front of the vehicle.', 
        'In his hand, a piece of parchment.', 'He looks back at you and fear glistens in his eyes.', 'You have garnered quite a reputation after your previous victories.', '"Henchmen, get him!"', 
        'They stand still and after you do a backflip to assert dominance, they scurry off.', '"Imbeciles! You! I will let you know that any attempt to take this page is futile."',
        '"Get any closer and I will strike you down like I strike down unions!"', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'PRETENTIOUS SOCIAL COMMENTARY!'],

        "boss_victory_text": ['"You look just as hopeless as my employees after 15 hours of mandatory labor on Christmas. Hehehehe"', 'Hint: The Personification of Capitalism starts off extremely weak. Try to keep him from buffing himself'],

        "boss_defeat_text": ['"What?!"', '"No!"', '"This can not be!"', '"How dare you!"', '"I worked so hard to be the first born son of my billonare father and this is what I get! Do you not know how hard it is to dock my workers pay?!"', 
        '"I have to tell my intern to change the numbers and send out the emails!"', '"It is so tiring on my part!"', 'You shrug and grab the page out of his hand. You also take his monocle because why not?',
        '"I get it, you want to destroy me because you are too lazy to work as hard as I did to be born to a rich family!"', 'He keeps rambling as you walk away. Eventually he leaves earshot',
        'Well...', 'that was pretentious.', 'If I had eyes I would be rolling them.', "Receiving a lecture about the dangers of unfettered capitalism in a journey where you fight Santa Claus and Mr. Skellybones was not what I expected.", 
        "Well, hey, we got a page."],

        "is_defeated": False,
        'encountered': False,
        'level_last_encountered': 0
    },
    {
        "name": "Santa Claus",

        "health": 150,
        "nerves": 130,
        "max_health": 100,
        "max_nerves": 130,
        "min_nerves": 10,
        'def_health': 100,
        'def_nerves': 100,

        "victory_item": items[8],
        'score': 500,

        "location": 4,
        'index': 3,

        "intro": ['H-Hey,', 'so,', 'maybe it was a bad idea to come to the north pole...', 'in nothing but a polo and jeans...', 'in the winter.', 
        "E-even I-I'm cold, and I don't have any p-physical feeling.", 'Anyway, you come upon a factory in the middle of no-where.', "Santa's Workshop.",
        'Santa is not a man to triffle with, especially since Christmas is coming close.', "It may be best if we hold off on coming here unti-",
        "...", "...", "...", '"Hey!"', '"Hey!"', '"HEY!"', 'Wait, what happened?!', 'Oh, so, you wake up, bound to an armchair near a fireplace with a small elf in a suit and green hat.', 
        '"Mind tellin us what ya were doin so close to the Workshop?"', "You try to show her a page of the constitution but it seems that you're bound by present wrapping.",
        "Oh,", "you're only bound by present wrapping.", "You stand up, destroying all of the wrapping.", '"Hey! You stand when I tell ya to stand!"', 
        'You show her a page of the constitution', '"The constitution, huh? Well, we have no idea where any page could be, so you are wasting ya time here!"',
        'As she says that, Santa himself walks in laughing while holding a page of the constitution in his hand.', "She immediately scurries off, leaving you alone with ol' Saint Nick",
        '"Hohoho! It seems like you are lost! Allow me to show you out!"', 
        'You immediately try to grab the page out of his hand but he effortlessly tosses you across the room, into a Christmas tree.', "Welp, seems like we're fighting Santa Claus.", 'Oops.'],

        "boss_victory_text": ['"Hohoho! It seems like all you will be getting this Christmas is a lump of coal!"', 
        "Hint: Santa is a tank when it comes to health and damage, so try to make him nervous so that he can't attack you."],

        "boss_defeat_text": ['"Ho... ho... ho..."', '"You are very skilled."', 'Santa then falls asleep on the armchair.', 
        '"Seems like the fight exhausted the old man." says the elf, back after the battle.', '"Look, we cannot afford these complications so close to Christmas."',
        '"So just take the page and whatever else ya need and never come back here again. Ya hear me?"', "You nod and grab the page from Santa's hand.", 
        'As you take the page, the hat starts glowing brightly', '"Oh my... there is no way... it seems like the hat is callin to ya..."', 
        'You shrug and walk away but the hat gently floats on your head', '"How is that even... wow, what can I say..."', 'You give a thumbs up and leave.'],

        "is_defeated": False,
        'encountered': False,
        'level_last_encountered': 0
    },
    {
        "name": "Zeep Vorp",

        "health": 120,
        "nerves": 130,
        "max_health": 120,
        "max_nerves": 130,
        "min_nerves": 10,
        'def_health': 100,
        'def_nerves': 120,

        'score': 800,

        "location": 4,
        'index': 4,
        "intro": ['4 pages down, 1 more to go.', 'Where could it be though?', 'We looked almost everywhere!', 'Maybe we have to double check British Texas?',
        'We did get very busy with that horde back there.', '...', 'Oh...', 'oh my!', 'You hear a deafening humming noise behind you.', 
        'You turn around and you see large flying mech piloted by none other than...', 'Zeep Vorp!', "Oh, thank goodness, he's here to help!", 'BLAM!', 'POW!', 'ZOOM!',
        'Zeep Vorp is...', 'firing at us?!', "You wave to Zeep Vorp trying to signal to him that you're his friend but he won't listen.", 
        'After doding his attacks for a while, he finally stops.', '"Vorleem..."', 'Yeah, he better be!', '"Vop xansti twop zoap"', 'What?!', 'He wants the pages too?!', 
        '"Verloo zat bes veem mattz"', '"Rlaty vrium skizt"', '"Lito vem plee tros vetr"', 'Are you kidding?!', 
        'I cannot believe that he was originally planning to destory us with the proton charge, but he changed his mind once he saw us take down our first boss so that we can gather the pages,'
        'just for him to take it!', "I can't believe he would do that!", '"Ves votto plam!"', '"Tulap!"'],

        "boss_victory_text": ['"Veeleem dorp... vine vot"', 
        "Hint: Remember all of what you learned"],

        "boss_defeat_text": ['Wow...', "That was something... wasn't it?", 'Oh, look, in his hand,', 'he had the last page!', "You take the page out of his hand and you nod.",
        "I can't believe this quest already over.", 'That was what?', '3 days?', "Well, I suppose that now we have the pages, we should go and return them to where they belong."],

        "is_defeated": False,
        'encountered': False,
        'level_last_encountered': 0
    }
]

def Dialogue(dialogue):

    i = 0

    if not print_all_dialogue:
        for line in dialogue:
            i += 1
            input(f'{line} ({i}/{len(dialogue)})')
    else:
        for line in dialogue:
            print(f'{line} ({dialogue.index(line) + 1}/{len(dialogue)})')
        else:
            input('Enter anything to continue: ')

def ShowOptions(choices, selection_prompt, display_only):
    input_taken = False
    player_choice = 0
    
    while not input_taken:
        for choice in choices:

            # Checks if the choice has an health_effect because only items and attacks have them, so this is to check if the choice is an attack or item
            if type(choice) is dict:

                print(f'{choices.index(choice)}. {choice['name']}')

                for stat in choice:
                    if choice[stat] == 0 or stat == 'name':
                        continue

                    match stat:
                        case 'description':
                            print(f'    - {choice[stat]}')
                        case 'health_effect':
                            if choice[stat] > 0:
                                print(f'    - Heals {choice[stat]} Health')
                            else:
                                print(f'    - Deals {choice[stat] * -1} Damage')
                        case 'nerves_effect':
                            if choice[stat] > 0:
                                print(f'    - Adds {choice[stat]} Nerves')
                            else:
                                print(f'    - Inflicts {choice[stat]} Nerves')
                        case 'health_overtime_effect':
                            if choice[stat] > 0:
                                print(f'    - Heals additional {choice[stat]} health every turn for {choice['duration']} turns')
                            else:
                                print(f'    - Deals additional {choice[stat]} damage every turn for {choice['duration']} turns')
                        case 'nerves_overtime_effect':
                            if choice[stat] > 0:
                                print(f'    - Adds additional {choice[stat]} nerves every turn for {choice['duration']} turns')
                            else:
                                print(f'    - Inflicts additional {choice[stat]} nerves every turn for {choice['duration']}')

                if choice['to_player'] == True:
                    print('    - Affects: Player')
                if choice['to_player'] == False:
                    print('    - Affects: Opponent')
            else:
                print(f'{choices.index(choice)}. {choice}')

        if not display_only:    
            try:
                player_choice = int(input(selection_prompt))
            except:
                print("Oops! Seems like you inputted something wrong. Let's roll that back.")
                continue

            if player_choice < 0 or player_choice > (len(choices) - 1):
                return -1
        
        return player_choice
       
def Move(current_local, desired_local):

    if desired_local == current_local:
        print(f"Um, are you crazy? {desired_local} doesn't exist. \nYou did not move.")
        return current_local
    elif locations[desired_local] not in locations:
        print(f"Um, you're already at {desired_local}. Congrats? \nYou did not move.")
        return current_local

    # On the chance the player is in Town City or American Australia, the game will verify whether or not they have a boat to determine if they succesfully move.
    if current_local in [6, 8]:
        if desired_local == 7:
            if items[4] in inventory:
                print(f"Yar Har Har! You sailed the 7 seas! \nYou successfully moved to {locations[desired_local]}")
                return desired_local
            else:
                print(f'Unless your name is "Michael Fred Phelps," you are not making across the sea without a boat. \nYou did not move.')
                return current_local     
    
    # The game will check if the player can actually move to their desired_local from where they are. If they are, they can move, if not, they stay.
    if desired_local in places_to_go[current_local]:
        print(f"You successfully moved to {locations[desired_local]}")
        return desired_local
    else:
        print(f"Sorry pal, you can't move to {locations[desired_local]} from {locations[current_local]} \nYou did not move.")
        return current_local

# Rolls effectivness of attack depending on nerves.
def RollNerveEffect(nerves):
    rolled_number = random.randint(1,100)

    if rolled_number > nerves:
        if rolled_number > (nerves * 1.5):
            return 0
        else:
            return 0.5
    else:
        if rolled_number < (nerves * 0.1):
            return 1.5
        else:
            return 1  

def TakeAction(action, nerves_value, from_player, boss):

    # Rolls for effectiveness
    nerve_multipler = RollNerveEffect(nerves_value)
    effectiveness = ['I do not know the effectiveness of this action']
    user_text = [f'I do not know who did this action']

    if from_player:
        user_text = [f'You used {action['name']}!']
    else:
        user_text = [f'{boss['name']} used {action['name']}!']

    health_effect = 0
    nerves_effect = 0


    if not from_player or not action['is_item']: 
        match nerve_multipler:
            case 0:
                effectiveness = ['Action was a complete failure.']
                Dialogue(user_text + action['super_failure'] + effectiveness)
            case 0.25:
                effectiveness = ['Action was a ineffective.']
                Dialogue(user_text + action['failure'] + effectiveness)         
            case 1:
                effectiveness = ['Action was a success!']
                Dialogue(user_text + action['success'] + effectiveness)
            case 1.5:
                effectiveness = ['Action was super effective!']
                Dialogue(user_text + action['super_success'] + effectiveness)
    elif action['is_item']:
        Dialogue(user_text + action['use_text'])
    else:
        Dialogue(action['use_text'])
    
       
    # Verifies whether the attack came from the player or boss
    if from_player and not action['is_item']:

        # Applies effects to player
        if action['to_player']:

            # Modifies effectiveness based off of nerve_multiplier and player_stats
            health_effect = math.floor(action['health_effect'] * nerve_multipler * player_stats['recovery_potency'])
            nerves_effect = math.floor(action['nerves_effect'] * nerve_multipler * player_stats['recovery_potency'])

            player_stats['health'] += health_effect
            player_stats['nerves'] += nerves_effect

            if action['health_effect'] < 0:
                print(f'You lost {health_effect} health.')
            else:
                print(f'You healed {health_effect} health.')

            if action['nerves_effect'] < 0:    
                print(f'You lost {nerves_effect} nerves.')
            else:
                print(f'You gained {nerves_effect} nerves.')

        # Applies effects to enemy
        else:

            # Modifies effectiveness based off of nerve_multiplier and player_stats
            health_effect = math.floor(action['health_effect'] * nerve_multipler * player_stats['attack_potency'])
            nerves_effect = math.floor(action['nerves_effect'] * nerve_multipler * player_stats['attack_potency'])

            boss['health'] += health_effect
            boss['nerves'] += nerves_effect

            if action['health_effect'] < 0:
                print(f'You dealt {health_effect * -1} damage.')
            else:
                print(f'Your opponent healed {health_effect} health from your attack.')

            if action['nerves_effect'] < 0:
                print(f'{boss['name']} lost {nerves_effect * -1} nerves.')  
            else:
                print(f'Your opponent gained {nerves_effect} nerves from your attack.')

    # If player is using an item
    elif from_player and action['is_item']:

        health_effect = action['health_effect']
        nerves_effect = action['nerves_effect']

        Dialogue(user_text)

        if action['to_player']:
            player_stats['health'] += health_effect
            player_stats['nerves'] += nerves_effect
        
            if action['health_effect'] < 0:
                print(f'You lost {health_effect} health.')
            else:
                print(f'You healed {health_effect} health.')

            if action['nerves_effect'] < 0:    
                print(f'You lost {nerves_effect} nerves.')
            else:
                print(f'You gained {nerves_effect} nerves.')

        else:
            boss['health'] += health_effect
            boss['nerves'] += nerves_effect

            if action['health_effect'] < 0:
                print(f'You dealt {health_effect * -1} damage.')
            else:
                print(f'Your opponent healed {health_effect} health from your attack.')

            if action['nerves_effect'] < 0:
                print(f'{boss['name']} lost {nerves_effect * -1} nerves.')  
            else:
                print(f'Your opponent gained {nerves_effect} nerves from your attack.')

        inventory.pop(inventory.index(action))

    # If the action was not from a player, it will be handled as an item and use the boss's pool of attacks
    else:
        health_effect = math.floor(action['health_effect'] * (nerve_multipler + (0.05 * player_stats['level'])))
        nerves_effect = math.floor(action['nerves_effect'] * (nerve_multipler + (0.05 * player_stats['level'])))

        if action['to_player']:
            player_stats['health'] += health_effect
            player_stats['nerves'] += nerves_effect

            if action['health_effect'] < 0:
                print(f'{boss['name']} dealt {health_effect * -1} damage to you.')
            else:
                print(f'You gained {health_effect} health from {boss['name']}.')

            if action['nerves_effect'] < 0:
                print(f'You lost {nerves_effect * -1} nerves.')
            else:
                print(f'You gained {nerves_effect} nerves.')
        else:
            boss['health'] += health_effect
            boss['nerves'] += nerves_effect

            if action['health_effect'] > 0:
                print(f'{boss['name']} healed {health_effect} health.')
            else:
                print(f'{boss['name']} lost {health_effect * -1} health.')

            if action['nerves_effect'] > 0:
                print(f'{boss['name']} gained {nerves_effect} nerves.')
            else:
                print(f'{boss['name']} lost {nerves_effect} nerves.')

    if player_stats['health'] > player_stats['max_health']: player_stats['health'] = player_stats['max_health'] 

    if player_stats['nerves'] > player_stats['max_nerves']: player_stats['nerves'] = player_stats['max_nerves']
    elif player_stats['nerves'] < player_stats['min_nerves']: player_stats['nerves'] = player_stats["min_nerves"] 

    if boss['health'] > boss['max_health']: boss['health'] = boss['max_health']
       
    if boss['nerves'] > boss['max_nerves']: boss['nerves'] = boss['max_nerves']
    elif boss['nerves'] < boss['min_nerves']: boss['nerves'] = boss["min_nerves"] 

# Game Over Sequence
def GameOver(boss):

    # Resets player and boss stats
    player_stats["health"] = player_stats['max_health']
    player_stats['nerves'] = player_stats['max_nerves']

    boss['health'] = boss['def_health']
    boss['nerves'] = boss['def_nerves']

    Dialogue(['-!-!-!-GAME OVER-!-!-!-'] + boss['boss_victory_text'] + ["Let's run that back..."])

# Function to reward player with page and item after beating a boss
def GiveReward(boss):         

    # Gives Player Page
    player_stats['pages'] += 1
    Dialogue([f'You now have {player_stats['pages']}/5 pages!'])
                
    # Give Player Reward Item
    inventory.append(boss['victory_item'])
    input('You have a new item! (1/1)')
    input(ShowOptions([boss['victory_item']], 'Test', display_only=True))
    rewards_recieved = True

# Function that manages battles
def Fight(boss):
    turn = -1
    fight_finished = False
    player_action = {}

    rewards_recieved = False
    stat_boosted = False
    monologue_complete = False

    saved_inventory = []
    
    # This resets the boss's health after a game over and makes sure that the boss's health is properly scaled with player level
    boss['health'] = boss['def_health'] + (10 * player_stats['level'])
    boss['nerves'] = boss['def_nerves']
    # This ensures that the boss's max health doesn't infinitely stack
    if not boss['encountered'] or boss['level_last_encountered'] != player_stats['level']:
        boss['max_health'] += 10 * player_stats['level']
        boss['level_last_encountered'] = player_stats['level']
    # This ensures that the Metaphor for Capitalism doesn't start at max health
    if boss['index'] != 2:
        boss['health'] = boss['max_health']

    while not fight_finished:

        if boss['health'] > 0 and player_stats['health'] > 0:

            # Boss Intro Sequence
            if turn == -1:
                if not boss['encountered']:
                    Dialogue(boss["intro"])
                turn += 1
                boss['encountered'] = True

            # Player Turn
            elif turn % 2 == 0:

                input(f"-+-+-+-+-Your Turn-+-+-+-+-")
                print(f'-~-~-~-~-~{boss["name"]}-~-~-~-~-~ ')

                # Gets whether player wants
                try:
                    action = ShowOptions(['Check Stats', 'Select Item', 'Select Attack'], 'What is your choice? ', False)

                    if action < 0 or action > 2:
                        continue
                except:
                    print("Seems like you entered that incorrectly. Let's roll this back. ")
                    continue

                match action:

                    # Shows Stats
                    case 0:
                        print(f"-=-=-=-Your Stats-=-=-=-")
                        print(f"Health: {player_stats["health"]}/{player_stats["max_health"]} \nNerves: {player_stats["nerves"]}/{player_stats["max_nerves"]} \nAttack Potency: {player_stats["attack_potency"]}x \nRecovery Potency: {player_stats['recovery_potency']}")
                        print(f"Minimum Nerves: {player_stats['min_nerves']} \nDurability: {player_stats['durability']} \nBravery: {player_stats["bravery"]} \nStrength: {player_stats["strength"]}")
                        print(f"-=-=-=-{boss['name']}'s Stats-=-=-=-")
                        print(f"Health: {boss['health']}/{boss['max_health']} \nNerves: {boss['nerves']}/{boss['max_nerves']} \nMinimum Nerves: {boss['min_nerves']}")
                        input("Enter Anything to go back to main battle menu: ")
                        continue

                    # Opens Inventory
                    case 1:

                        # Tell player if inventory is closed, then goes back to menu
                        if not inventory:
                            input("Welp, there's nothing here, back to the main battle menu. ")
                            continue

                        player_action = ShowOptions(inventory, "Which item do you wish to use (Enter Number)? ", False)

                        if player_action < 0:
                            continue
                        

                        if inventory[player_action]['name'] == 'Boat':
                            Dialogue('Um... what were you thinking their?', "It's a boat.", 'What possible use could a boat have in combat.')
                            continue

                        # Saves item in saved_inventory then uses items
                        saved_inventory.append(inventory[player_action])
                        TakeAction(inventory[player_action], player_stats['nerves'], True, boss)       

                    # Attacks Menu
                    case 2:        
                        player_action = ShowOptions(player_attacks, "Which attack do you wish to use (Enter Number)? ", False)

                        if player_action < 0:
                            continue
                            
                        TakeAction(player_attacks[player_action], player_stats['nerves'], True, boss)        
                  
                turn += 1  
                if boss['health'] > 0:
                    input(f"-+-+-+-+-{boss['name']}'s Turn-+-+-+-+-")

            # Boss Turn
            else:      
                
                # Randomly selects boss_attacks
                boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]

                rerolls = 0

                while rerolls < 6:

                    # Following If Statements are to ensure the boss doesn't make any redundant moves
                    if boss_attack['health_effect'] > 0 and boss['health'] == boss['max_health']:
                        boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]
                        rerolls += 1
                        continue

                    if boss_attack['nerves_effect'] > 0 and boss['nerves'] == boss['max_nerves']:
                        boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]
                        rerolls += 1
                        continue

                    if player_stats['nerves'] <= player_stats['max_nerves'] / 2 and boss_attack['health_effect'] >= 0:
                        boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]
                        rerolls += 1
                        continue

                    break
                    

                TakeAction(boss_attack, boss['nerves'], False, boss)
                turn += 1
        # Game Over Sequence
        elif player_stats['health'] <= 0:
           
            GameOver(boss)
            
            # If the player is on the tutorial boss, automatically restart the boss fight
            if player_stats['position'] == 0:
                turn = -1
                continue

            player_stats['position'] = 0

            # Restock inventory with all lost items
            for saved_item in saved_inventory:
                inventory.append(saved_item)

            fight_finished = True

        # Victory Sequence
        elif boss['health'] <= 0 and boss['index'] != 4:

            if not monologue_complete:
                Dialogue(boss['boss_defeat_text'])
                monologue_complete = True

            if rewards_recieved == False:
                GiveReward(boss)
                rewards_recieved = True
                
            if not stat_boosted:
                # Have player choose what stat to level up
                match ShowOptions([f'Strength: {player_stats["strength"]}', f'Bravery: {player_stats['bravery']}', f'Durability: {player_stats['durability']}', f'Recovery: {player_stats['recovery']}'], 'Which stat do you wish to level up? ', False):

                    # Invalid Option
                    case -1:
                        continue

                    # Boost Strength
                    case 0:
                        player_stats['strength'] += 1
                        player_stats['attack_potency'] += (player_stats["strength"]) * 0.15
                        Dialogue([f'Your strength is now at Level {player_stats['strength']}!'])

                    # Boost Durability
                    case 2:
                        player_stats['durability'] += 1
                        player_stats['max_health'] += (player_stats['durability']) * 15
                        Dialogue([f'Your durability is now at Level {player_stats['durability']}!'])

                    # Boost Bravery
                    case 1:
                        player_stats['bravery'] += 1
                        player_stats['max_nerves'] += (player_stats["bravery"]) * 10
                        Dialogue([f'Your bravery is now at Level {player_stats['bravery']}!'])

                    # Boost Recovery
                    case 3:
                        player_stats['recovery'] += 1
                        player_stats['recovery_potency'] += (player_stats["recovery"]) * 0.15
                        Dialogue([f'Your recovery stat is now at Level {player_stats['recovery']}!'])
                stat_boosted = True
            
            ShowOptions([reward_attacks[boss['index']]], 'Yippee', True)

            # If the boss is the Voice In Your Head, automatically give reward_attack
            if boss['name'] == "The Voice In Your Head":
                Dialogue([f'You have learned Pep Talk. Congratualations!'])
                player_attacks.append(reward_attacks[0])

            # Gives player the option of whether or not to take a reward item
            else:

                replace = ShowOptions(['Yes', 'No'], 'Would you like to replace any of your attacks with this one? ', False)

                if replace == 0:                
                    player_attacks[ShowOptions(player_attacks, 'Which attack would you like to replace ? ', False)] = reward_attacks[boss['index']]
                    Dialogue([f'You have learned {reward_attacks[boss['index']]['name']}!'])

                elif replace == 1:
                    Dialogue([f'You have decided not to learn {reward_attacks[boss['index']]['name']}.'])

                else:
                    continue

            player_stats['level'] += 1
            
            # Reset Player health and nerves and mark boss as defeated
            player_stats["health"] = player_stats['max_health']
            player_stats['nerves'] = player_stats['max_nerves']

            # Adds Score
            added_score = boss['score'] - (5 * (turn - 10))
            added_score -= 20 * len(saved_inventory)

            player_stats['score'] += added_score

            input(f'+{added_score} score!')

            boss['is_defeated'] = True
            fight_finished = True

        # If the final boss is defeated
        elif boss['health'] <= 0 and boss['index'] == 4:
            added_score = round((boss['score'] * (1.0 - ((0.01 * turn) - (0.2 * (player_stats['health']/player_stats['max_health']))))))

            player_stats['score'] += added_score

            input(f'+{added_score} score!')
            Dialogue(boss['boss_defeat_text'])

            boss['is_defeated'] = True
            fight_finished = True

def main():
    # Intro Sequence
    if not skip_intro:
        input(game_title_screen)
        Dialogue([
            "Once upon a time,", 
            "There was a great nation known as the Even More United States of America, or EMUSA.", 
            'The nation lived harmoniously. Folks from around the nation, from the North Pole to British Texas (which you may know as "Australia") were united under a common love for peace and democracy.',
            "But one day, all of that changed.",
            'A man only known as "N. Cage" stole the constitution of EMUSA, sending the country into chaos.',
            'Apparently, he meant to steal a different document, so one thing led to another, and the 5 pages of the constitution were spread across the land.',
            'Naturally, the most powerful of the nation jumped at the opportunity for power and stole the pages near to them.',
            'You are a new intern at the White House.',
            'So before you knew it, you were sent off to retrieve the pages and save EMUSA.',
            '...',
            'Who am I?',
            "I'm the voice in your head, of course! I'll be guiding you on this important quest.",
            "Now, let's save America!"
        ])
    
        Fight(bosses[0])

    want_final_fight = True
    
    while True:
        # If player wants final fight
        if player_stats['pages'] == 4 and want_final_fight:
            choice = ShowOptions(['Yes', 'No'], 'You are approaching the final boss. It is HIGHLY recommended to get ALL items available. Do you wish to continue and fight the final boss?', False)
            
            if choice == 1:
                want_final_fight = False
                continue
            elif choice == 0:
                Fight(bosses[4])
                
                # Ending Sequence
                if bosses[4]['is_defeated']:
                    Dialogue([
                        'And so, your journey concluded.',
                        'After returning the constitution to your White House, a grand festival was hosted in your honor.',
                        'Everyone from all walks of life, from British Texas to the North Pole, attended in high spirits.',
                        'As the fireworks show begins, you sit upon a far-off hilltop and watch.',
                        'The fireworks are mesmerizing and the amazed crowds bring a smile to your face.',
                        '"Hey!"',
                        'You turn around, confused to see the elf that captured you earlier.',
                        '"The fat man could not attend, so I am here to represent him."',
                        '"He says sorry. It was not in the spirit of Christmas to try to hold the country hostage."',
                        '"Thank ya. It seems like after yer fight with him, he has been a lot kinder."',
                        'You nod and then remember the hat you took from him.',
                        'You shrug and toss it to her.',
                        '"Oh! Ya do not have to do this."',
                        '"The hat called to ya!"',
                        'You shrug.',
                        '"Wow... thank ya..."',
                        "Suddenly, Mr. Skellybones interjects.",
                        '"Raaaah. Honored one, is that you?"',
                        '"I have come to thank you, on behalf of the monsters of Spookyland."',
                        '"We would not be thriving without your advocacy."',
                        '"HELLO! I_THANK_YOU = TRUE. RATINGS = 10000!" says Super-Robo-Caesar.',
                        '"Hello, dear intern, the Royal Family of North Dakota wishes to congratulate you on this incredible achievement."',
                        'Hey, I thank you too.',
                        "You've probably showed me some of the greatest excitement a voice in someone's head can ever have.",
                        'Thank you.',
                        'And so, the fireworks shine brighter than ever,',
                        'and even better,',
                        'after the show, you were bestowed the greatest honor an unpaid intern can get...',
                        'a wage of $8 an hour.',
                        'This is the End of the quest for the country.'
                    ])
                    
                    input(f'Final Score: {player_stats["score"]}')
                    input(f'Quest for the Country designed, written, and developed by Darius Vaiaoga')
                    break
                else:
                    continue
        
        if player_stats['position'] != 0:
            for boss in bosses:
                if boss["location"] == player_stats['position'] and not boss["is_defeated"]:
                    Fight(boss)
                    break
                elif boss["location"] == player_stats['position'] and boss["is_defeated"]:
                    break
            else:
                if player_stats['position'] not in places_been:
                    Dialogue(location_dialogue[player_stats['position']])
                    places_been.append(player_stats['position'])
                    inventory.append(location_items[player_stats['position']])
                    input('You have a new item! (1/1)')
                    ShowOptions([location_items[player_stats['position']]], 'Test', display_only=True)
                    input('Press anything to continue')
        
        print(f'You are at {locations[player_stats["position"]]}')
        
        menu_options = ['Move', 'Stats', 'Inventory', 'Attacks', 'Settings', 'Exit']
        if player_stats['pages'] == 4:
            menu_options.append('Fight Final Boss')
        
        choice = ShowOptions(menu_options, 'What would you like to do? ', False)
        
        if choice == 0:
            try:
                print(f"Since you're currently at {locations[player_stats['position']]}, you can go to: ")
                for place in places_to_go[player_stats['position']]:
                    print(f"{place}. {locations[place]}")
                player_stats['position'] = Move(player_stats['position'], int(input("Where would you like to go? ")))
            except:
                print("Oops! Seems like you entered something incorrectly. Let's try that again")
        elif choice == 1:
            print(f"-=-=-=-Your Stats-=-=-=-")
            print(f"Health: {player_stats['health']}/{player_stats['max_health']}")
            print(f'Pages: {player_stats["pages"]}/5')
            print(f'Score: {player_stats["score"]}')
            input('Type anything to go back. ')
        elif choice == 2:
            ShowOptions(inventory, "Here are your items. ", True)
            input('Enter anything to go back. ')
        elif choice == 3:
            ShowOptions(player_attacks, '', True)
            input('Enter anything to go back. ')
        elif choice == 4:
            print(f'0. Instant Dialogue [{print_all_dialogue}]')
            if input('Modify a setting? (0 for instant dialogue) ') == '0':
                print_all_dialogue = not print_all_dialogue
        elif choice == 5:
            Dialogue(['Hey!', 'What are you doing?!', "If you exit back to the main menu, you'll lose all of your progress!"])
            if input('If you are sure you want to leave, type "Yes":') == "Yes":
                Dialogue(["I see...", 'Welp.', 'I guess our country is doomed because of YOUR actions.', 'Wait, if you leave, what will happen to me?', '...', 'WAIT N-'])
                break

        elif choice == 6:
            want_final_fight = True
            continue