
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


    ############################
    # People Get EndPoint Query
    ############################

    #Pull People by Search Term
    lpeople: list[RosettaPerson] = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.IAMIDS,"1000550201,1000016201,1000438403,1000227051")

    # "1000550201,1000016201,1000438403,1000227051"
    # "1000010578,1000438054,1000269748,1000004984"
    # "1000505549,1000213158,1000572411,1000632980"
    # "1000090068,1000054150,1000008378,1000326424"

    #Display People API Query Results
    for upeep in sorted(lpeople, key=lambda x: x.display_name):
        #Print Separator for Readability
        print("\n=============== " + upeep.display_name  + " ===============\n")

        #Print Rosetta Person Basic Properties
        for property_name, value in upeep.__dict__.items():
            if property_name != "employee_associations" and property_name != "student_associations":
                print(f"{property_name}: {value}")

        print(" ")

        #Print Employee Associations If Any
        if upeep.employee_associations is not None:
            for empassoc in upeep.employee_associations:
                for property_name, value in empassoc.__dict__.items():
                    print(f"{property_name}: {value}")

                print(" ")
                
        #Print Student Associations If Any
        if upeep.student_associations is not None:
            for stdntassoc in upeep.student_associations:
                for property_name, value in stdntassoc.__dict__.items():
                    print(f"{property_name}: {value}")

                print(" ")


    #######################################
    # Employee Associations Endpoint Query
    #######################################

    # #Pull Rosetta Employee Associations by Search Term
    # l_employee_assocs: list[RosettaEmployeeAssociation] = rosetta_api_wrkr.get_employee_associations_by_search_term(rosetta_api_wrkr.EmployeeSearchBy.DEPARTMENTID,"024000")

    # #Display Employee Associations API Query Results
    # for uemp_assoc in l_employee_assocs:

    #     #Print Separator for Readability
    #     print("\n=============== " + uemp_assoc.iam_id  + " ===============\n")

    #     #Print Rosetta Employee Association Properties
    #     for property_name, value in uemp_assoc.__dict__.items():
    #         print(f"{property_name}: {value}")

    #######################################
    # Student Associations Endpoint Query
    #######################################

    # #Pull Rosetta Student Associations by Search Term
    # l_student_assocs: list[RosettaStudentAssociation] = rosetta_api_wrkr.get_student_associations_by_search_term(rosetta_api_wrkr.StudentSearchBy.MAJORCODE,"GBIM")

    # #Display Student Associations API Query Results
    # for ustdnt_assoc in l_student_assocs:

    #     #Print Separator for Readability
    #     print("\n=============== " + ustdnt_assoc.iam_id  + " ===============\n")

    #     #Print Rosetta Student Association Properties
    #     for property_name, value in ustdnt_assoc.__dict__.items():
    #         print(f"{property_name}: {value}")

    #For Readability
    print(" ")

#Standard Main Function Setup
if __name__ == "__main__":
    main()




