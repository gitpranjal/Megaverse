
import time
from ObjectFactory import ObjectFactory

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


