
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from pprint import pprint

#Import Rosetta Classes
from rosetta import RosettaAPIWorker, RosettaPerson, RosettaEmployeeAssociation, RosettaStudentAssociation


def main():

    #Load the .env file
    load_dotenv()

    #Initialize Rosetta API Worker
    rosetta_api_wrkr = RosettaAPIWorker(os.getenv("ROSETTA_BASE_URL"),
                                        os.getenv("ROSETTA_OAUTH_URL"),
                                        os.getenv("ROSETTA_CLIENT_ID"),
                                        os.getenv("ROSETTA_CLIENT_SECRET"))

    #Pull People by Search Term
    lpeople: list[RosettaPerson] = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.LOGINID,"dbunn")

    #Display People API Query Results
    for upeep in lpeople:
        for property_name, value in upeep.__dict__.items():
            print(f"{property_name}: {value}")


#Standard Main Function Setup
if __name__ == "__main__":
    main()




