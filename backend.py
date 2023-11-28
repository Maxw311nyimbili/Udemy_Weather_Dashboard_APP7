import requests


def get_data(place, forecast_days):
    """gets temperature or sky condition for a specified city and for specified number of days"""

    api_key = "1b7df5e3bcecdf2d0e11b8aa2e67203d"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place.title()}&appid={api_key}"
    response = requests.get(url)
    data = response.json()  # as a dictionary

    # displaying the number of data corresponding to the user prompt
    desired_data = data["list"]
    data_value = 8*forecast_days
    filtered_data = desired_data[:data_value]
    return filtered_data


if __name__ == "__main__":
    print(get_data("zambia", 3))