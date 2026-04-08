"""Provide simple gardening advice based on season and plant type."""

SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

SEASON_RECOMMENDATIONS = {
    "summer": ("sunflowers", "lavender", "tomatoes"),
    "winter": ("kale", "spinach", "pansies"),
}


def get_user_choice(prompt, valid_options):
    """Collect and validate a normalized user choice."""
    choice = input(prompt).strip().lower()

    if choice not in valid_options:
        options = ", ".join(sorted(valid_options))
        raise SystemExit(f"Unsupported choice. Please choose one of: {options}.")

    return choice


def build_advice(season, plant_type):
    """Create the final advice message shown to the user."""
    recommended_plants = ", ".join(SEASON_RECOMMENDATIONS[season])

    advice_lines = [
        SEASON_ADVICE[season],
        PLANT_ADVICE[plant_type],
        f"Plants that thrive in {season}: {recommended_plants}.",
    ]

    return "\n".join(advice_lines)


def main():
    """Run the gardening advice app."""
    season = get_user_choice(
        "Enter the season (summer/winter): ",
        SEASON_ADVICE,
    )
    plant_type = get_user_choice(
        "Enter the plant type (flower/vegetable): ",
        PLANT_ADVICE,
    )

    print(build_advice(season, plant_type))


if __name__ == "__main__":
    main()
