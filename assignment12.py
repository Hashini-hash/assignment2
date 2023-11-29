#quiz1

import requests


def fetch_random_chuck_norris_joke():
    api_url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            joke_text = data["value"]
            print("Chuck Norris Joke:")
            print(joke_text)
        else:
            print(f"Error: {data['error']}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    fetch_random_chuck_norris_joke()


