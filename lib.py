import random
from english_words import get_english_words_set  # Requires "pip install english_words" to function

# ===========================
# Word List Setup
# ===========================

# Fetch a set of English words
raw_word_list = get_english_words_set(["web2"], lower=True)

# Filter words to ensure they contain only alphabetic characters and are longer than 2 letters
WORDS = [word for word in raw_word_list if word.isalpha() and len(word) > 2]

# ===========================
# Power Class Definitions
# ===========================
# CLASSES dictionary contains descriptions of various power classes.
# Each key is a class name and the value is a brief description of that class.

CLASSES = {
    "Blaster": "Blasters are empowered individuals with ranged offensive options. While most of these powers are damaging, this is not always the case.",
    "Breaker": "Breakers can alter themselves to a different state in which they gain different abilities, although some have permanently altered states.",
    "Brute": "Brutes are typically big, strong, and tough or possess some other method of self-protection, usually a permanent mutation.",
    "Changer": "Changers can alter their form, appearance, or natural abilities through manipulation of their own bodies.",
    "Master": "Masters can manipulate others or create minions to do their bidding.",
    "Mover": "Movers have abilities that allow them to transport themselves or others via various non-standard methods.",
    "Shaker": "Shakers can affect a broader area, asserting some degree of control over the battlefield.",
    "Stranger": "Strangers have powers related to stealth, distraction, infiltration, or subterfuge. ",
    "Striker": "Strikers have powers that are touch-based or melee ranged.",
    "Thinker": "Thinkers have powers related to knowledge, skills, and enhanced perception.",
    "Tinker": "Tinkers fabricate things, with stats reflecting the gear they can make, often based around a theme.",
    "Trump": "Trumps can manipulate powers in various capacities, including altering, granting, strengthening, weakening, or removing them entirely."
}

# ===========================
# Power Trait Definitions
# ===========================
# TRAITS dictionary contains specific power variations for each class.
# Each class key contains a list of trait strings, each with a description and associated stat modifications.

TRAITS = {
    "Blaster": [
        "Damage Blaster: Emphasizes raw offensive power. Stats: +1 attack, +1 range",
        "Ruin Blaster: Has a lot of destructive power, used for or against the environment. Stats: +1 attack, +1 range",
        "Barrage Blaster: Produces a large amount of projectiles at the cost of accuracy or damage. Stats: -1 control",
        "Range Blaster: More dangerous or accurate when attacking from a great distance. Stats: +2 range",
        "Accuracy Blaster: Produces projectiles that either home in on the target or are very hard to dodge. Stats: +2 control",
        "Effect Blaster: Emphasizes the secondary characteristics of a projectile, sacrificing damage for other qualities. Stats: -1 attack, +2 control",
        "Impact Blaster: Focuses on big shots and massive impacts that send enemies flying. Stats: +2 range",
        "Object Blaster: Blasts originate from or are capitalized on by some power-created object or field. Stats: +1 attack, +1 control",
        "Versatile Blaster: High utility or a variety of attack forms, making them more competent in various scenarios. Stats: +1 defense",
        "Beam Blaster: Produces lasers or stream attacks. Stats: +1 control",
        "Enchantment Blaster: Imbues items, applying an effect that makes them effective as ammunition or melee weapons. Stats: +1 attack, -2 range",
        "Conditional Blaster: Form has set requirements to activate. Stats: +2 attack, +1 defense, +1 mobility, -2 control"
    ],
    "Breaker": [
        "Death Breaker: An improved powerset requiring the user to actively enter their powered form, with associated costs or penalties. Stats: +1 attack, +1 endurance",
        "Time Breaker: A powered form dependent on or limited by time limits or time of day. Stats: +1 attack, +1 defense, -2 endurance",
        "Fate Breaker: Entering the powered form grants a special effect, but exiting creates a consequence. Stats: +1 mobility, +1 defense",
        "War Breaker: A powered form fueled or strengthened by violence. Stats: +2 endurance",
        "Nature Breaker: A change allowing the user to become or merge with the environment. Stats: +1 defense, +1 control",
        "Hysteria Breaker: Users enter a powered state where their minds and emotions become warped. Stats: +2 attack, +2 defense, +2 mobility, -5 control",
        "Tribulation Breaker: Users enter a state where their ability to interact with the world becomes limited, as does the world's ability to interact with them. Stats: -1 attack, +2 defense",
        "Desire Breaker: Users enter a powered state where they become linked to or merge with others in some way. Stats: +2 control"
    ],
    "Brute": [
        "Muscle Brute: Physical strength and size. Stats: +2 attack",
        "Armor Brute: Shell around themselves. Stats: +2 defense",
        "Shield Brute: Direction-dependent defense or defense based around an object or field that can be moved. Stats: +1 defense, +1 range",
        "Intensity Brute: Offensive lean using an 'element', with assisting defensive powers. Stats: +2 attack, +1 defense",
        "Field Brute: A personal forcefield or durability that's very potent but temporary or readily broken. Stats: +2 defense, -2 endurance",
        "Dynamic Brute: Skill-based defensive measures or ways of redirection. Stats: +1 defense, +1 mobility",
        "Sunder Brute: Aggressive defense measures that weaken foes. Stats: +2 defense",
        "Repression Brute: Abstract or indirect measures used to moderate harm. Stats: +1 attack, +1 control",
        "Negate Brute: All-or-nothing attack/defense. Stats: +2 attack, +2 defense, -5 control",
        "Regen Brute: Offers benefits over time or healing abilities. Stats: +2 endurance",
        "Transfiguration Brute: Abilities related to transformation and revival. Stats: +1 defense, +1 endurance",
        "Immortal Brute: Permanent change to biology, cannot heal easily. Stats: +2 attack, -1 endurance"
    ],
    "Changer": [
        "Growth Changer: The power to grow extra weapons or armor. Stats: +1 attack, +1 defense",
        "Streamline Changer: The ability to streamline one's body, allowing for improved movement and evasion. Stats: +2 mobility",
        "Shifter Changer: The ability to alter one's appearance or human features. Stats: +1 control",
        "Regen Changer: The use of self-targeted biokinesis, possibly to heal oneself. Stats: +2 endurance"
    ],
    "Master": [
        "Conjurer Master: The ability to summon or conjure minions to control. Stats: +1 attack, +1 range",
        "Puppeteer Master: The ability to control existing things, typically inorganic. Stats: +1 range, +1 control",
        "Herder Master: The ability to control existing things, typically organic. Stats: +2 range",
        "Master Master: The ability to control other people actively or passively, either directly or by manipulating emotions or attitudes. Stats: -1 range"
    ],
    "Mover": [
        "Takeoff Mover: Produces an effect on departure. Stats: +1 attack, +1 mobility",
        "Transit Mover: Produces an effect while traveling. Stats: +1 mobility, +1 control",
        "Terminus Mover: Produces an effect on arrival. Stats: +1 attack, +1 mobility",
        "Slip Mover: Maximizes maneuverability and avoidance but doesn't cover a great deal of ground. Stats: +1 defense, +1 mobility",
        "Hurdle Mover: Capable of enhanced running, jumping, or climbing. Stats: +2 mobility",
        "Rocket Mover: Rushes towards their destination, often with little maneuverability. Stats: +2 mobility, -1 control",
        "Run Mover: Travels along the ground, emphasizing speed. Stats: +2 mobility",
        "Fly Mover: Uses either physical means or some sort of mechanism to become airborne. Stats: +2 mobility",
        "Blink Mover: Capable of teleportation. Stats: +2 mobility",
        "Ride Mover: Uses something as a vehicle to travel. Stats: +1 defense, +1 mobility",
        "Gate Mover: Creates something that grants movement, often an emplacement, gateway, launchpad, or similar. Stats: +1 mobility, +1 endurance",
        "Conveyance Mover: Requires a great deal of setup but acts on a greater scale, often moving others or setting up for later actions. Stats: +1 mobility, +2 endurance"
    ],
    "Shaker": [
        "Aura Shaker: An effect that surrounds the user. Stats: +1 control, +1 endurance",
        "Anchor Shaker: An effect that surrounds a set point. Stats: +2 range",
        "Woe Shaker: An AOE that produces a harmful effect. Stats: +1 attack, +1 range",
        "Adorn Shaker: Produces a non-physical effect in a radius such as a buff, debuff, or obscure. Stats: +1 range, +1 control",
        "Barrier Shaker: An ability centered around creating defensive emplacements. Stats: +2 defense",
        "Warp Shaker: An ability that warps the environment or surroundings. Stats: +1 defense, +1 range",
        "Tempest Shaker: Effects that create or remove material or energy from their environment. Stats: +1 control, +1 range",
        "Kinesis Shaker: An ability that functions by exerting force or movement on inorganic objects in their vicinity. Stats: +1 attack, +1 defense",
        "Sprawl Shaker: Effects that are massive in scale but are slow to reach full power. Stats: +2 range",
        "Control Shaker: A radius that directly debilitates enemies. Stats: +2 control"
    ],
    "Stranger": [
        "Obscure Stranger: Obscuring or altering the senses of others. Stats: +1 defense, +1 control",
        "Debilitate Stranger: Affecting the target's mind to distract or debilitate. Stats: +2 control",
        "Disable Stranger: Allowing the user to disable, deny, or repossess enemy equipment and objects. Stats: +1 defense, +1 range",
        "Stealth Stranger: Granting invisibility, stealth, or different forms of camouflage. Stats: +1 control, +1 endurance",
        "Surprise Stranger: Enabling or benefiting surprise attacks. Stats: +1 attack, +1 control",
        "Unobserved Stranger: Granting or enhancing skills and abilities while unobserved. Stats: +2 endurance",
        "Imitate Stranger: Imitating others in appearance, voice, and mannerisms. Stats: +2 endurance"
    ],
    "Striker": [
        "Empower Striker: The ability to empower weapons or other objects. Stats: +2 attack",
        "Impart Striker: The power to impart some sort of changed state on a target through touch. Stats: +2 control",
        "Armory Striker: The power to create weapons. Stats: +1 attack, +1 range",
        "Enhance Striker: Abilities that enhance melee strikes with various effects. Stats: +2 attack",
        "Short Striker: Particularly short-ranged forms of telekinesis or elemental effects. Stats: +1 attack, +1 control"
    ],
    "Thinker": [
        "Combat Thinker: Powers that enable them to fight more effectively. Stats: +1 control, +1 endurance",
        "Zone Thinker: Particularly good at using or reading the surroundings effectively. Stats: +1 range, +1 control",
        "Scatterbrain Thinker: Highly adaptable power that can be molded in how it's utilized. Stats: +2 control",
        "Sense Thinker: Enhanced or augmented senses. Stats: +2 control",
        "Proficiency Thinker: Powers that enhance or grant abilities to perform, learn, or execute techniques. Stats: +1 control, +1 endurance",
        "Social Thinker: Can manipulate, study, or control others through information or skills. Stats: +1 control"
    ],
    "Tinker": [
        "Hyperspecialist Tinker: Emphasis on their specialty alone. Stats: +1 attack, +1 defense, +1 mobility, +1 range, +1 control",
        "Focal Tinker: Focuses on a single item they build and rebuild. Stats: +2 endurance",
        "Multithreaded Tinker: Has two or more specialties. Stats: +2 control",
        "Combat Tinker: Flexible in specialty but leans heavily towards battlefield applications. Stats: +2 attack",
        "Chaos Tinker: Doesn't have complete control over what they build. Stats: -2 control",
        "Resource Tinker: Leans heavily on materials for their creations. Stats: +1 control, +1 endurance",
        "Controller Tinker: Creates drones as part of their primary field of specialty. Stats: +2 range",
        "Architect Tinker: Works primarily with large-scale constructions. Stats: +2 range",
        "Mad Scientist Tinker: More power or breadth of options but at a cost. Stats: -1 endurance",
        "Magi Tinker: Focuses on self-improvement through direct modification or assistive devices. Stats: +1 control, +1 endurance"
    ],
    "Trump": [
        "Null Trump: Reducing the effectiveness of other powers. Stats: -2 attack, -2 defense, -2 mobility",
        "Switch Trump: Powers with variable aspects. Stats: +2 control",
        "Gift Trump: Powers involved with partnering, bonding, and gifting. Stats: +1 attack, +1 defense",
        "Copy Trump: Allows the empowered to steal, borrow, or copy other powers. Stats: -2 endurance",
        "Library Trump: Abilities where one can pick between different options. Stats: -1 attack, -1 defense, -1 mobility, +1 control",
        "Disrupt Trump: Scrambling, disrupting, or altering powers. Stats: +1 control",
        "Wildcard Trump: Powers that cycle between different variants. Stats: -2 control",
        "Unlimiter Trump: Powers that remove limits or enhance abilities. Stats: +2 attack, +2 defense, +2 mobility, +2 control"
    ]
}