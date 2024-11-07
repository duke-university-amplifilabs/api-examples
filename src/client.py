import requests
import os
from schemas import State, MeasureCategory, MeasureLevel, DemographicData
from dotenv import load_dotenv

load_dotenv()


class DukeApi:
    """
    DukeApi provides methods to interact with the Duke API for retrieving demographic data
    and other relevant measures across different states and categories.

    Attributes:
        base_api (str): The base URL of the Duke API.
        session (requests.Session): A session object for making API requests with shared headers.
        auth_token (str): The authentication token for accessing the API.
    """

    def __init__(
        self, username: str | None = None, password: str | None = None
    ) -> None:
        """
        Initializes the DukeApi instance with authentication credentials and session setup.

        Args:
            username (str | None): The API username (optional; will use environment variable if not provided).
            password (str | None): The API password (optional; will use environment variable if not provided).

        Raises:
            ValueError: If no username or password is provided, either as an argument or environment variable.
        """
        # Get username and password from arguments or environment variables
        username = username or os.getenv("DUKE_API_USERNAME")
        password = password or os.getenv("DUKE_API_PASSWORD")

        if not username or not password:
            raise ValueError("Username and password are required")

        # Define the base API URL, defaulting to a test environment if not set
        self.base_api = os.getenv(
            "DUKE_API_HOST", "https://sdoh-test.azurewebsites.net"
        )

        # Initialize a session to reuse the same headers and connection
        self.session = requests.Session()

        # Authenticate and set authorization headers
        self.auth_token = self.authenticate(username, password)
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.auth_token}",
            }
        )

    def authenticate(self, username: str, password: str) -> str:
        """
        Authenticates the user and retrieves an access token for API requests.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.

        Returns:
            str: The access token to be used in further API requests.

        Raises:
            ValueError: If the response does not contain an access token.
        """
        # Construct the URL for the login endpoint
        url = f"{self.base_api}/auth/login"

        # Update headers for form data submission
        self.session.headers.update(
            {"Content-Type": "application/x-www-form-urlencoded"}
        )
        print({"username": username, "password": password})
        # Send the login request
        response = self.session.post(
            url, data={"username": username, "password": password}
        )

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the response and retrieve the access token
        data = response.json()

        if "access_token" not in data:
            raise ValueError("Invalid token")

        return data["access_token"]

    def list_measures(
        self, category: MeasureCategory, level: MeasureLevel
    ) -> list[str]:
        """
        Lists available measures for a given category and level.

        Args:
            category (MeasureCategory): The category of the measure (e.g., health, income).
            level (MeasureLevel): The level of the measure (e.g., county, state).

        Returns:
            list[str]: A list of available measures as strings.

        Raises:
            requests.exceptions.RequestException: If the request fails.
        """
        # Construct the URL for listing measures
        url = f"{self.base_api}/cube/measures/{category}/{level}"

        # Send a GET request to retrieve measures
        response = self.session.get(url)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        return response.json()

    def list_measure_years(self, category: str, level: str, measure: str) -> list[str]:
        """
        Lists available years for a specific measure, category, and level.

        Args:
            category (str): The category of the measure.
            level (str): The level of the measure.
            measure (str): The specific measure to retrieve years for.

        Returns:
            list[str]: A list of years in which data for the measure is available.

        Raises:
            requests.exceptions.RequestException: If the request fails.
        """
        # Construct the URL to list available years for the specified measure
        url = f"{self.base_api}/cube/measure-years/{category}/{level}/{measure}"

        # Send a GET request to retrieve the years
        response = self.session.get(
            url, params={"category": category, "level": level, "measure": measure}
        )

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        return response.json()

    def list_states(self) -> list[State]:
        """
        Lists all states for which data is available.

        Returns:
            list[State]: A list of states, where each state is an instance of the State schema.

        Raises:
            requests.exceptions.RequestException: If the request fails.
        """
        # Construct the URL to retrieve the list of states
        url = f"{self.base_api}/cube/states"

        # Send a GET request to retrieve states
        response = self.session.get(url)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the response into State objects
        return [State(**state) for state in response.json()]

    def query(
        self,
        category: MeasureCategory,
        level: MeasureLevel,
        measures: list[str],
        states: list[str],
        years: list[int],
    ) -> list[DemographicData]:
        """
        Queries demographic data based on specified filters.

        Args:
            category (MeasureCategory): The category of the measure (e.g., health, income).
            level (MeasureLevel): The level of the measure (e.g., county, state).
            measure (list[str]): A list of measure names to include in the query.
            state (list[str]): A list of state codes to filter the data.
            year (list[int]): A list of years to retrieve data for.

        Returns:
            list[DemographicData]: A list of demographic data objects matching the filters.

        Raises:
            requests.exceptions.RequestException: If the request fails.
        """
        # Construct the URL for the query endpoint
        url = f"{self.base_api}/cube/query"

        # Send a POST request with the specified filters to retrieve demographic data
        response = self.session.post(
            url,
            json={
                "category": category,
                "level": level,
                "measures": measures,
                "states": states,
                "years": years,
            },
        )

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the response into DemographicData objects
        return [DemographicData(**data) for data in response.json()]
