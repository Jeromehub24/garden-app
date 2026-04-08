# Supported values for simple validation.
valid_seasons = {"summer", "winter"}
valid_plant_types = {"flower", "vegetable"}

# Collect user input instead of relying on hardcoded values.
season = input("Enter the season (summer/winter): ").strip().lower()
plant_type = input("Enter the plant type (flower/vegetable): ").strip().lower()

if season not in valid_seasons:
    raise SystemExit(
        "Unsupported season. Please choose either 'summer' or 'winter'."
    )

if plant_type not in valid_plant_types:
    raise SystemExit(
        "Unsupported plant type. Please choose either 'flower' or 'vegetable'."
    )

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
