# garden_advice.py
# A gardening advice app that provides tips based on season and plant type.


def get_season_advice(season):
    # Return advice based on the given season
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    # Return advice based on the given plant type
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def display_advice(season, plant_type):
    # Combine and print the advice for season and plant type
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)
    print(advice)


def main():
    # Hardcoded values for the season and plant type
    season = "summer"       # TODO: Replace with input() to allow user interaction.
    plant_type = "flower"   # TODO: Replace with input() to allow user interaction.

    display_advice(season, plant_type)


if __name__ == "__main__":
    main()