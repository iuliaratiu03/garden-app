# garden_advice.py
# A gardening advice app that provides tips based on season and plant type.


# Dictionary storing advice for each season
SEASON_ADVICE = {
    "spring": "Great time to plant! Make sure to water regularly and watch for late frosts.",
    "summer": "Water your plants regularly and provide some shade during peak heat.",
    "autumn": "Start preparing your garden for winter. Plant bulbs for spring blooms.",
    "winter": "Protect your plants from frost with covers and reduce watering frequency."
}

# Dictionary storing advice for each plant type
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms and deadhead regularly.",
    "vegetable": "Keep an eye out for pests and rotate crops each season.",
    "tree": "Prune dead branches and mulch around the base to retain moisture.",
    "herb": "Harvest regularly to encourage new growth and prevent flowering.",
    "cactus": "Water sparingly and ensure the soil drains well."
}

# Dictionary recommending plants for each season
PLANT_RECOMMENDATIONS = {
    "spring": ["tulips", "daffodils", "lettuce", "peas"],
    "summer": ["sunflowers", "tomatoes", "basil", "lavender"],
    "autumn": ["chrysanthemums", "garlic", "kale", "asters"],
    "winter": ["holly", "winter jasmine", "hellebores", "cyclamen"]
}


def get_season_advice(season):
    """
    Return gardening advice based on the given season.

    Args:
        season (str): The current season (spring, summer, autumn, winter).

    Returns:
        str: Advice for the given season, or a default message if not found.
    """
    return SEASON_ADVICE.get(season.lower(), "No advice available for this season.")


def get_plant_advice(plant_type):
    """
    Return gardening advice based on the given plant type.

    Args:
        plant_type (str): The type of plant (flower, vegetable, tree, herb, cactus).

    Returns:
        str: Advice for the given plant type, or a default message if not found.
    """
    return PLANT_ADVICE.get(plant_type.lower(), "No advice available for this plant type.")


def recommend_plants(season):
    """
    Recommend plants suitable for the given season.

    Args:
        season (str): The current season (spring, summer, autumn, winter).

    Returns:
        list: A list of recommended plants, or an empty list if season not found.
    """
    return PLANT_RECOMMENDATIONS.get(season.lower(), [])


def get_user_input(prompt, valid_options):
    """
    Prompt the user for input and validate against a list of accepted options.

    Args:
        prompt (str): The message displayed to the user.
        valid_options (list): List of accepted input values.

    Returns:
        str: A valid input string entered by the user.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}\n")


def display_advice(season, plant_type):
    """
    Display the full gardening advice for a given season and plant type,
    including plant recommendations for the season.

    Args:
        season (str): The current season.
        plant_type (str): The type of plant.
    """
    print("\n--- Gardening Advice ---")
    print(f"Season  : {season.capitalize()}")
    print(f"Plant   : {plant_type.capitalize()}")
    print(f"\nSeason advice : {get_season_advice(season)}")
    print(f"Plant advice  : {get_plant_advice(plant_type)}")

    recommendations = recommend_plants(season)
    if recommendations:
        print(f"\nRecommended plants for {season}: {', '.join(recommendations)}")
    print("------------------------\n")


def main():
    """
    Main function that runs the gardening advice app.
    Collects user input and displays personalised gardening advice.
    """
    print("Welcome to the Gardening Advice App!\n")

    valid_seasons = list(SEASON_ADVICE.keys())
    valid_plants = list(PLANT_ADVICE.keys())

    # Replace hardcoded values with user input
    season = get_user_input(
        f"Enter the current season ({', '.join(valid_seasons)}): ",
        valid_seasons
    )

    plant_type = get_user_input(
        f"Enter your plant type ({', '.join(valid_plants)}): ",
        valid_plants
    )

    display_advice(season, plant_type)


if __name__ == "__main__":
    main()