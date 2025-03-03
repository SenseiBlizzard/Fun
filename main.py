import random
from gen import generate_powers, generate_power_levels

# ===========================
# Main Function
# ===========================

def main():
    """
    Main function to handle the entire process of:
    1. Rolling for abundance.
    2. Generating power levels based on abundance.
    3. Displaying the final power details.
    """

    # Step 1: Roll for abundance
    abundance_roll = random.randint(1, 9)  # Directly rolls for abundance without reroll option
    print(f"Abundance Roll: {abundance_roll}")

    # Step 2: Generate initial power levels array based on abundance
    base_levels = generate_power_levels(abundance_roll)

    # Step 3: Generate powers based on the final abundance roll and power levels
    result = generate_powers(abundance_roll, base_levels)

    # ===========================
    # Display Generated Powers
    # ===========================

    for power in result['powers']:
        theme = power['theme'].upper()
        level = power['level']
        points = power['points']
        cap = power['cap']
        class_name = power['class_name']
        class_description = power['class_description']
        trait_description = power['trait_description']

        # Extract trait stats if applicable
        trait_stats = {}
        if "Stats:" in trait_description:
            stats_part = trait_description.split("Stats:")[1].strip()
            for stat in stats_part.split(","):
                parts = stat.strip().split()
                stat_value = parts[0].replace("+", "").strip()
                stat_name = parts[1].strip()
                trait_stats[stat_name.lower()] = int(stat_value)

        # Print power details
        print(f"{theme} ({level}) - {points} points")

        # Print stats with +Trait if applicable
        for stat in ["attack", "defense", "mobility", "range", "control", "endurance"]:
            base_stat = f"0/{cap}"
            print(f"{stat.capitalize()}: {base_stat}")

        # Print class and trait details
        print("CLASSES")
        print(f"{class_name}: {class_description}")
        print("TRAITS")
        print(f"{trait_description}")

        # Print trait bonuses if applicable
        if trait_stats:
            print("\nTrait Bonuses (Add manually can go over cap):")
            for stat, value in trait_stats.items():
                print(f"{stat.capitalize()}: {'+' if value >= 0 else ''}{value}")

        print("\n" + "=" * 40 + "\n")

# ===========================
# Entry Point
# ===========================

if __name__ == "__main__":
    main()
