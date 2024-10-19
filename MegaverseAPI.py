import requests

class MegaverseAPI:
    """Class to handle API interactions with the Megaverse."""
    
    def __init__(self, base_url, candidate_id):
        self.base_url = base_url
        self.candidate_id = candidate_id

    def get_goal_map(self):
        """ Fuction to fetch goal map from the Megaverse API."""
        try:
            response = requests.get(f"{self.base_url}map/{self.candidate_id}/goal")
            response.raise_for_status()
            return response.json()["goal"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the goal map: {e}")
            return []

    def place_object(self, row, col, typ, **kwargs):
        """Method to place an object in the megaverse based on the given type and parameters."""
        try:
            response = requests.post(
                f"{self.base_url}/{typ}",
                json={"row": row, "column": col, "candidateId": self.candidate_id, **kwargs}
            )
            response.raise_for_status()
            print(f"Object of type {typ} placed at ({row}, {col})")
        except requests.exceptions.RequestException as e:
            print(f"Error placing object of type {typ} at ({row}, {col}): {e}")
