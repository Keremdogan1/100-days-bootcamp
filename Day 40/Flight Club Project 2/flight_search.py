import requests
from datetime import datetime
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:

    def __init__(self):
        """
        Initialize an instance of the FlightSearch class.

        This constructor performs the following tasks:
        1. Retrieves the API key and secret from the environment variables 'AMADEUS_API_KEY'
        and 'AMADEUS_SECRET' respectively.

        Instance Variables:
        _api_key (str): The API key for authenticating with Amadeus, sourced from the .env file
        _api_secret (str): The API secret for authenticating with Amadeus, sourced from the .env file.
        _token (str): The authentication token obtained by calling the _get_new_token method.
        """
        self._api_key = os.getenv("DAY40_AMADEUS_API_KEY")
        self._api_secret = os.getenv("DAY40_AMADEUS_API_SECRET")

        # Token expiry timestamp
        self._token_expiry = 0

        # Getting a new token every time program is run.
        self._token = self._get_new_token()

    # ---------------- TOKEN MANAGEMENT ---------------- #

    def _get_new_token(self):
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.

        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.

        Returns:
            str: The new access token obtained from the API response.
        """
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        data = response.json()

        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {data['access_token']}")
        print(f"Your token expires in {data['expires_in']} seconds")

        # Store expiry timestamp
        self._token_expiry = time.time() + data["expires_in"]

        return data["access_token"]

    def _token_expired(self):
        """Check if the token is expired."""
        return time.time() >= self._token_expiry

    def _ensure_token(self):
        """Refresh token if expired."""
        if self._token_expired():
            print("Token expired — refreshing...")
            self._token = self._get_new_token()

    # ---------------- IATA CODE LOOKUP ---------------- #

    def get_destination_code(self, city_name):
        """
        Retrieves the IATA code for a specified city using the Amadeus Location API.

        Parameters:
        city_name (str): The name of the city for which to find the IATA code.

        Returns:
        str: The IATA code of the first matching city if found; "N/A" if no match is found.
        """

        # Ensure token is valid
        self._ensure_token()

        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")

        try:
            code = response.json()["data"][0]['iataCode']
        except Exception:
            print(f"No airport code found for {city_name}.")
            return "N/A"

        return code

    # ---------------- FLIGHT SEARCH ---------------- #

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        """
        Searches for flight options between two cities on specified departure and return dates
        using the Amadeus API.

        Parameters:
            is_direct (bool) : True for non-stop flights.
            origin_city_code (str): The IATA code of the departure city.
            destination_city_code (str): The IATA code of the destination city.
            from_time (datetime): The departure date.
            to_time (datetime): The return date.

        Returns:
            dict or None: A dictionary containing flight offer data if the query is successful; None
            if there is an error.
        """

        # Ensure token is valid
        self._ensure_token()

        # Amadeus test API does NOT support ANK → fallback to ESB
        if origin_city_code == "ANK":
            print("ANK is not supported by Amadeus test API — using ESB instead.")
            origin_city_code = "ESB"

        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference")
            print("Response body:", response.text)
            return None

        return response.json()