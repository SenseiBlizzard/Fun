import random
import streamlit as st
from gen import generate_powers, generate_power_levels

# ===========================
# Streamlit Configuration
# ===========================
st.set_page_config(page_title="Power Generator", layout="centered")
st.title("🌀 Power Generator")

st.markdown("Welcome to the Power Generator! Click the button below to generate random power details.")

# ===========================
# Main Function for Streamlit
# ===========================
def main():
    """
    Main function to handle the entire process of:
    1. Rolling for abundance.
    2. Generating power levels based on abundance.
    3. Displaying the final power details.
    """
    if st.button("Generate Powers ⚡"):
        # Step 1: Roll for abundance
        abundance_roll = random.randint(1, 9)  # Directly rolls for abundance without reroll option
        st.subheader(f"🎲 Abundance Roll: {abundance_roll}")

        # Step 2: Generate initial power levels array based on abundance
        base_levels = generate_power_levels(abundance_roll)

        # Step 3: Generate powers based on the final abundance roll and power levels
        result = generate_powers(abundance_roll, base_levels)

        # ===========================
        # Display Generated Powers
        # ===========================
        for idx, power in enumerate(result['powers'], start=1):
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

            # Display power details
            st.write(f"### {theme} ({level}) - {points} points")
            
            # Print stats with +Trait if applicable
            st.write("### Stats")
            for stat in ["attack", "defense", "mobility", "range", "control", "endurance"]:
                base_stat = f"0/{cap}"
                if stat in trait_stats and trait_stats[stat] != 0:
                    base_stat += f" +Trait"
                st.write(f"- **{stat.capitalize()}:** {base_stat}")

            # Print class and trait details
            st.write("### CLASSES")
            st.write(f"**{class_name}:** {class_description}")
            st.write("### TRAITS")
            st.write(f"{trait_description}")

            # Print trait bonuses if applicable
            if trait_stats:
                st.write("### Trait Bonuses (Add manually can go over cap):")
                for stat, value in trait_stats.items():
                    st.write(f"- **{stat.capitalize()}:** {'+' if value >= 0 else ''}{value}")

            # Separator between powers
            st.write("-----")

# ===========================
# Run the Streamlit App
# ===========================
if __name__ == "__main__":
    main()
