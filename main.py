import requests


class JustEatAPIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)


class JustEatAPI:
    def __init__(self):
        self.base_url = "https://api.just-eat.com/restaurants"

    def get_by_postcode(self, postcode):
        url = f"{self.base_url}/bypostcode/{postcode}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                all_restaurants = []

                for restaurant_data in data.get("Restaurants", []):
                    restaurant_info = {
                        "name": restaurant_data.get("Name"),
                        "rating": restaurant_data.get("RatingStars"),
                        "Cuisines": restaurant_data.get("Cuisines"),
                    }
                    all_restaurants.append(restaurant_info)
                return all_restaurants

            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None


postcode = "EC4"
client = JustEatAPI()
restaurants = client.get_by_postcode(postcode)

try:
    restaurants = client.get_by_postcode(postcode)
    for restaurant in restaurants:
        print("Name:", restaurant["name"])
        print("Rating:", restaurant["rating"])
        print("Cuisines:", restaurant["Cuisines"])

except JustEatAPIError as er:
    print(f"An error occurred: {er}")
