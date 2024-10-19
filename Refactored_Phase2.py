import requests
import time

# Constants
BASE_URL = "https://challenge.crossmint.io/api/"
CANDIDATE_ID = "88108289-d898-43ff-8b64-96df02493ccb"


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

class ObjectFactory:
    """Factory class to create objects based on the type from the goal map."""

    @staticmethod
    def create_object(type_string):
        """Method to parse the type string from the goal map and returns the appropriate parameters."""
        if type_string == "POLYANET":
            return {"type": "polyanets"}
        
        typ_string_list = type_string.split("_")
        arg_val = typ_string_list[0].lower()
        obj_type = typ_string_list[1].lower() + "s"

        if obj_type == "comeths":
            return {"type": obj_type, "direction": arg_val}
        elif obj_type == "soloons":
            return {"type": obj_type, "color": arg_val}

        return None

class MegaverseManager:
    """Class that manages the process of retrieving the goal map and placing objects."""

    def __init__(self, api):
        self.api = api

    def process_goal_map(self):
        """Processes the goal map and places the corresponding objects."""
        goal_map = self.api.get_goal_map()
        for i, row in enumerate(goal_map):
            for j, cell in enumerate(row):
                if cell != "SPACE":
                    obj = ObjectFactory.create_object(cell)
                    if obj:
                        self.api.place_object(i, j, obj["type"], **obj)
                        # Optional delay to avoid API throttling issues
                        time.sleep(0.5)

# Main function to run the process
if __name__ == "__main__":
    api = MegaverseAPI(BASE_URL, CANDIDATE_ID)
    manager = MegaverseManager(api)
    manager.process_goal_map()
