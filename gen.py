import random
from lib import CLASSES, TRAITS, WORDS

# ===========================
# Character Generation
# ===========================

def generate_character():
    """
    Randomly selects and returns a theme (word), main class, and subclass.
    - Word: Represents a theme for the character.
    - Class: Main category (e.g., Warrior, Mage).
    - Subclass: Specialization within the main class.
    """
    word = random.choice(WORDS)
    char_class = random.choice(list(CLASSES.keys()))
    subclass = random.choice(TRAITS[char_class])
    return word, char_class, subclass

# ===========================
# Variance and Abundance Rolls
# ===========================

def roll_with_variance(base):
    """
    Rolls a number between base and base + 0.9 to add a small variance.
    Used to make power levels less predictable.
    """
    return round(random.uniform(base, base + 0.9), 1)

def roll_abundance():
    """
    Rolls a random abundance level between 1 and 9.
    Higher abundance means more potential power levels.
    """
    return random.randint(1, 9)

# ===========================
# Power Level Generation
# ===========================

def generate_power_levels(abundance):
    """
    Generates power levels based on the given abundance.
    - Abundance 9: Starts with a roll between 5–10, then rolls 1–4 if needed.
    - Other Abundances: Rolls 1–4 until total ≥ abundance.
    - Applies variance (0.0–0.9) to final rolls for more dynamic levels.
    """
    base_levels = []  # Stores the raw rolls before applying variance
    total = 0         # Tracks the sum of all rolls

    if abundance == 9:
        # Special handling for abundance 9
        first_roll = random.randint(5, 10)
        base_levels.append(first_roll)
        total += first_roll

        # Roll additional 1–4 until total ≥ 9 if the first roll is less than 9
        if total < 9:
            while total < 9:
                roll = random.randint(1, 4)
                base_levels.append(roll)
                total += roll
    else:
        # For other abundances, roll 1–4 until total ≥ abundance
        while total < abundance:
            roll = random.randint(1, 4)
            base_levels.append(roll)
            total += roll

    # Apply 0.0–0.9 variance to all rolls after finalizing rolls
    base_levels_with_variance = [round(lvl + random.uniform(0.0, 0.9), 1) for lvl in base_levels]

    # Print only ONCE per function call
    print(f"Generated Power Levels for Abundance {abundance}: {base_levels_with_variance}")
    return base_levels_with_variance

# ===========================
# Stat Cap and Points
# ===========================

def get_stat_cap_and_points(level):
    """
    Returns the stat cap and points available for a given level.
    Caps limit individual stat maximums.
    Points are used to distribute among stats.
    """
    return {
        1: (3, 5), 2: (4, 10), 3: (5, 15), 4: (6, 20),
        5: (7, 25), 6: (8, 30), 7: (9, 35), 8: (10, 40),
        9: (11, 45), 10: (12, 50)
    }.get(int(level), (3, 5))

# ===========================
# Power Details Generation
# ===========================

def generate_powers(abundance, base_levels):
    """
    Generates detailed power information based on abundance and power levels.
    - Includes theme, class, subclass, and stat caps/points.
    """
    power_details = []
    for level in base_levels:
        word, char_class, subclass = generate_character()
        class_desc = CLASSES[char_class]
        cap, points = get_stat_cap_and_points(int(level))
        power_details.append({
            "level": level,
            "whole_level": int(level),
            "theme": word,
            "class_name": char_class,
            "class_description": class_desc,
            "trait_description": subclass,
            "cap": cap,
            "points": points
        })

    return {
        "roll": abundance,
        "powers": power_details
    }
