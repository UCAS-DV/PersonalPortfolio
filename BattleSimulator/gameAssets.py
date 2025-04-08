intro = ['Once upon a time,', 'There was a great nation known as the Even More United States of America, or EMUSA', 
         'The nation lived harmonously, with citizens of all different species and creeds living peacefully amongst each other,', 
         'until the day the constitution was split across the land.', 'Chaos erupted as regional leaders took the pages of the constitution for themselves for power and glory.', 
         'For days it seemed like EMUSA was going to meet its end', 'until...', 
         'A heroic intern alongside the very witty and attractive voice in his head fought the leaders and reunited the constitution',
         "They held grand festival in the intern's honor, unifying the country once again.", "It's almost been a year since that intern's quest for the country.", 
         'Well, I should say, it has almost been a year since YOUR quest for the country.',
         "Also don't forget how I, the voice in your head, helped you out.", "That's besides the point.", 'The point is that the country, yet again, finds itself divided.', 
         'The North Pole, Spookyland, The Mythical State of North Dakota, and the planet Vorlum are fighting over who gets to hold the festival celebrating your victory this year!', 
         'In a panic, President Daniel Smithson has organized a tournament.',
         'Whoever wins the tournament, their region gets to host the festival,', 'and you get to choose who fights!', "Now, let's see how this tournament goes!"]

tutorial = ["Oh,", 'yeah.', "It's almost been a year since you last battled.", 'You might need a refresher.', 'You see, alongside having to manage your health,', 
            'you gotta manage your nerves.', "If you have low nerves, you'll likely fail your attacks",
            'On the other hand,', "if you have high nerves, you're more likely to hit an attack really well.", 
            'Fighters with high amounts of bravery have higher amounts of nerves than most.', 
            "Also, you didn't have to worry about this but in arena settings, means a ton.", 'If you have more speed than your opponent, you get to go first.', 
            "If you have the same amount of speed as your opponent, it's basically a coin flip as to who goes first.",
            "Since there are no items in this arena setting, that's all there is!", 'Feel refreshed?']

classes = [
    {
        'name': 'Elf',
        'brief': 'Damage Dealing',
        'description': 'Elves are small and fiesty. They may be easy to underestimate but trust me. You do not want to mess with an elf.',
        'alligence': 'The North Pole',
        'attacks': [
            {
                'name': 'Christmas Blast',
                'damage': 25,
                'discomfort': 0,
                'target_self': False,
                'super_effective': ['{wname} calls upon the ghosts of Christmas Past, Present, and Yet to Come.', 
                                    'Together they channel the power of all Christmases that have been and all Christmases that will be',
                                    '""CHRIIIIIIIIIST-"', '""MAAAAAAAAAS"', '"BLAST!!!!"', 'The sheer amount of Christmas Sprit in the area threatens the space-time continuum itself.',
                                    '{lname} is overwhelmed by the blinding light of Christmas'],
                'effective': ["To {lname}'s horror, {wname} charges up a Christmas Blast and blasts him with Christmas spirit!"],
                'failure': ['{wname} attempts to channel the spirit of Christmas but fails due to their misdeeds.', 'Said misdeeds were not holly nor jolly.'],
                'super_failure': ['{wname} calls upon the ghosts of Christmas Past, Present, and Yet to Come.', 
                                  'When the ghosts arrive, instead of using their overwhelming Christmas spirit to blast...',''
                'They start listing off every non-holly and non-jolly thing {wname} has done.', 'The Ghosts rise up above the arena to the level of the crowd.', 
                'Present speaks in an oddly solemn tone', '"Dear members of the audience, it appears that {wname} is not worthy of summoning us."', 
                'Past speaks, "For he has committed great crimes against Christmas."',
                '"Such as..."', 'Present says...', 'Oh...', 'oh wow...', 'How can a person even do such a thing...', 'Goodness...', 'You know what.', 'Just forget about it.']
            },
            {
                'name': 'Coal',
                'damage': 0,
                'discomfort': 10,
                'target_self': False,
                'super_effective': ['After a quick signal, Santa N. Claus himself jumps into the arena and personally hands {lname} a lump of coal!', 
                                    'Santa Claus then pulls out a piece of piece of paper and a microscope', 'He puts the paper under the microscope',
                                    '"Hohoho, it seems like you are on my naughty list"', "{lname}'s eyes widen in shock", 
                                    '{lname} kneels down, and with tears in their eyes, beg and plead for forgivness', 
                                    'Santa Claus silently shakes his head and leaves the arena.'],
                'effective': ['{wname} delivers a lump of coal to {lname}', 'From what it seems, {lname} has ended up on the naughty list.', 
                              '{lname} cries, devastated that they will not be getting the Playbox 5 they asked for this Christmas.'],
                'failure': ['{wname} chucks a lump of coal at {lname}.', '{lname} is too dazed to realize that they are on the naughty list.'],
                'super_failure': ['After a quick signal, Santa N. Claus himself jumps into the arena and personally hands {lname} a present', 
                                  '"Hohoho! Thank You for being such a good person this year!"', '{lname} opens their present to see the Playbox 5 they asked for',
                                  'They are estatic and heel-click for joy.', '{wname} just stares at them, dumbfounded.']
            },
            {
                'name': 'Candy Cane',
                'damage': -15,
                'discomfort': 0,
                'target_self': True,
                'super_effective': ['{wname} takes a bite of a Candy Cane...', 'but oops!', "It wasn't a Candy Cane but a medium rare, well seasoned, Wagyu steak!", 
                                    "{wname}'s common mistake seems to have rejuvinated them far more than a Candy Cane ever could!"],
                'effective': ['{wname} takes a bite of a Candy Cane in their pocket.', 'They feel rejuvinated.'],
                'failure': ['{wname} takes a bite of a Candy Cane in their pocket', 'but then they realize that Candy Canes are awful so they only feel mildly rejuvinated.'],
                'super_failure': ['{wname} attempts to pull out a Candy Cane but drops it on the ground.', 'They try to pick it up but by the time they picked it up,', 
                                  'it had already been 6 seconds.', 
                                  'For the first time in history,', 'the 5-second rule has failed someone.']
            },
            {
                'name': 'Christmas Movie',
                'damage': 0,
                'discomfort': -15,
                'target_self': True,
                'super_effective': ['{wname} reaches into his pocket and pulls out...', 'a 63 inch flatscreen,', 'an orange, three-seat sofa,', 'a bucket of popcorn,', 'and two friends!', 
                                    'They have the best movie night of their life!'],
                'effective': ['{wname} whips out his phone and watches a Christmas movie.', "They feel soothed by the movie's cheer."],
                'failure': ['{wname} whips out his phone and attempts to watch a Christmas movie.', 'It appears that the internet inside the arena is not great.', 
                            'The movie is watchable but barely.'],
                'super_failure': ['{wname} whips out his phone and attempts to watch a Christmas movie.', 'But as he pulls it out he drops it.', 
                                  'After bouncing it around,', 'they finally catch it.', 
                                  'Just to realize that they have to watch 30 seconds of ads.', '{wname} throws the phone down to the ground in anger.']
            }
            #{
            #    'name': 'Falcon Punch',
            #    'damage': 1000,
            #    'discomfort': 0,
            #    'target_self': False,
            #    'super_effective': ['0'],
            #    'effective': ['1'],
            #    'failure': ['2'],
            #    'super_failure': ['3']
            #}
        ]
    },
    {
        'name': 'Skeleton',
        'brief': 'Causing Nervousness',
        'description': 'AAAAAA! Sorry, got a little spooked. Skeletons are terrifying creatures but do not worry, they are very weak.',
        'alligence': 'Spookyland',
        'attacks': [
            {
                'name': 'Shin Kick',
                'damage': 15,
                'discomfort': 0,
                'target_self': False,
                'super_effective': ['Pow!', 'The shin kick does...', 'absolutely nothing!', '{wname} missed completely!', 'But {lname} then slipped on a convienently placed banana peel.'],
                'effective': ['Pow!', '{wname} goes for a kick to the shin!'],
                'failure': ['Pow?', '{wname} goes for a kick to the shin but apparently without skin, muscles, or anything but bones, it is not very effective.'],
                'super_failure': ['Womp!', '{wname} goes for a kick to the shin but spins around and falls over.', 'The entire stadium laughs at {wname}.', 
                                'They get a call informing them they are now disowned by their mother due to how terrible the kick was',
                                'Their phone buzzes with notifications about news articles about how terrible the kick was.', 
                                'President Daniel Smithson comments on the kick, labeling it "a disgrace to democracy."']
            },
            {
                'name': 'Spook',
                'damage': 0,
                'discomfort': 30,
                'target_self': False,
                'super_effective': ['{wname} walks up to {lname}.', "They place their hand on {lname}'s shoulder.", 'You can barely hear what is being said.',
                                    '{lname} falls to their knees.', 'From what I can tell, {wname} said...', '...', '...', 'Y-you know w-what...', 'N-nevermind...', "I-it's not important..."],
                'effective': ['"RAAAAAAAAAAAAAAAAAAAAAH!"', '{wname} scares {lname}!', '{lname} is left shivering his timbers.'],
                'failure': ['"RAAAAAAAAAAAAAAAAAAAAAAAAAH!"', '"AAAAAAAAAAAAAAAAAAAAAAAAAH"', '{wname} scares themself instead of {lname}.', "{lname} is a little unsettled but it's alright."],
                'super_failure': ['"RAAAA...', '{wname} suddenly stops themself.', "They ponder why they are doing this.", 'What even is the point?', 'Is any of this worth it?',
                                  'What difference does it make if Spookyland or the North Pole gets to host the festival?', 'All it is about is celebrating the past.', 
                                  'Why do we celebrate the past?', 'Should we not focus on our future?', 'Or something like that!', "I wouldn't feel that!", "I'm too cool to feel that way.",
                                  'Haha...']
            },
            {
                'name': 'Got Milk?',
                'damage': -20,
                'discomfort': 0,
                'target_self': True,
                'super_effective': ['{wname} pulls out a jug of milk', 'and instead of chugging it,', 'they use a crazy straw.', 'The majesty of the crazy straw makes the milk more effective',
                                    '{lname} quivers in fear as they witness how cool {wname} is with his crazy straw'],
                'effective': ['{wname} pulls out a jug of milk.', 'They chug it until not even a drop is in it.', "Their bones are now stronger."],
                'failure': ['{wname} pulls out a jug of milk.', "They chug it just to realize that it's expired."],
                'super_failure': ['{wname} pulls out a...', 'nothing.', 'It seems that they have forgotten their milk at home.', 'They quickly rush home to get their milk just to see that they never had milk',
                                  'They then rush to the supermarket to buy milk but they are out.', 'Straight to the farmers they go but it seems like they are out of cows.', 
                                  "{wname} then goes to the cow factory but it's closed on the weekends.", '{wname} heads back to the arena, disappointed and milkless.']
            },
            {
                'name': 'Reassurance',
                'damage': 0,
                'discomfort': -15,
                'target_self': True,
                'super_effective': ['{wname} calls upon a motivational speaker.', '"{wname}, if you are sad..."', '"stop being sad."', "The motivational speaker's wise words reassures {wname} greatly."],
                'effective': ['{wname} gives themself a pat on the back to reassure themself that it will be alright.'],
                'failure': ['{wname} tries to reassure themself but their nerves get to them.', 'They do not feel reassured.'],
                'super_failure': ['{wname} puts in headphones playing nothing but motivational speeches.', 'They jump up and down,', 'now sufficently hyped up.', 
                                  'They charge at {lname} just for their headphones to die midcharge.', 'Their motivation dies out and they end up tumbling across the ground.', 
                                  'They regret buying headphones from the dollar store']
            }
        ]
    }
]