# Main function to run the process
from MegaverseAPI import MegaverseAPI 
from MegaverseManager import MegaverseManager
# Constants
BASE_URL = "https://challenge.crossmint.io/api/"
CANDIDATE_ID = "88108289-d898-43ff-8b64-96df02493ccb"


if __name__ == "__main__":


    api = MegaverseAPI(BASE_URL, CANDIDATE_ID)
    manager = MegaverseManager(api)
    manager.process_goal_map()