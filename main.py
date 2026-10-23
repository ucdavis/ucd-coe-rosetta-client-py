
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

#Import Rosetta Classes
from rosetta import RosettaAPIWorker, RosettaPerson, RosettaEmployeeAssociation, RosettaStudentAssociation, RosettaDepartment, RosettaJobTypeID


def main():

    #Load the .env file
    load_dotenv()

    #Initialize Rosetta API Worker
    rosetta_api_wrkr = RosettaAPIWorker(os.getenv("ROSETTA_BASE_URL"),
                                        os.getenv("ROSETTA_OAUTH_URL"),
                                        os.getenv("ROSETTA_CLIENT_ID"),
                                        os.getenv("ROSETTA_CLIENT_SECRET"))

    # List for Returned List of Rosetta People
    l_people: list[RosettaPerson] = []

    #Set for Unique IDs for Post People Lookup
    s_mpl_ids = set()

    # Demo Data
    # "1000550201,1000016201,1000438403,1000227051"
    # "1000010578,1000438054,1000269748,1000004984"
    # "1000505549,1000213158,1000572411,1000632980"
    # "1000090068,1000054150,1000008378,1000326424"
    
    ############################
    # People Get EndPoint Query
    ############################

    #Pull People by Search Term
    l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.IAMIDS,"1000550201,1000016201,1000438403,1000227051")

    #######################################
    # Employee Associations Endpoint Query
    #######################################

    #Pull Rosetta Employee Associations by Search Term
    l_employee_assocs: list[RosettaEmployeeAssociation] = rosetta_api_wrkr.get_employee_associations_by_search_term(rosetta_api_wrkr.EmployeeSearchBy.DEPARTMENTID,"024000")

    #Display Employee Associations API Query Results
    for uemp_assoc in l_employee_assocs:

        #Add Employee's IAM to MPL IDs Set for People Post Lookup 
        s_mpl_ids.add(uemp_assoc.iam_id)

        #Display Employee Association Info
        rosetta_api_wrkr.display_rosetta_employee_association_info(uemp_assoc)
  
    #For Readability
    print(" ")

    #######################################
    # Student Associations Endpoint Query
    #######################################

    #Pull Rosetta Student Associations by Search Term
    l_student_assocs: list[RosettaStudentAssociation] = rosetta_api_wrkr.get_student_associations_by_search_term(rosetta_api_wrkr.StudentSearchBy.MAJORCODE,"GBIM")

    #Display Student Associations API Query Results
    for ustdnt_assoc in l_student_assocs:

        #Add Student's IAM to MPL IDs Set for People Post Lookup 
        s_mpl_ids.add(ustdnt_assoc.iam_id)

        #Display Student Association Info
        rosetta_api_wrkr.display_rosetta_student_association_info(ustdnt_assoc)

    #For Readability
    print(" ")

    #######################################
    # People Lookup by Post Query
    #######################################
    
    #Check MPL IDs Set Count
    if len(s_mpl_ids) > 0:

        #Pull List of Rosetta People by Post Lookup
        l_people = rosetta_api_wrkr.post_mass_people_lookup(rosetta_api_wrkr.PeoplePostLookupBy.IAMIDS,s_mpl_ids)

    #######################################
    # Display List of Rosetta People
    #######################################

    for upeep in sorted(l_people, key=lambda x: x.display_name):
        rosetta_api_wrkr.display_rosetta_person_info(upeep)

    #For Readability
    print(" ")

    ########################################
    # Departments Listing
    ########################################

    #Pull List of Rosetta Departments
    l_departments: list[RosettaDepartment] = rosetta_api_wrkr.get_departments()

    #Display Department Information
    for u_dept in l_departments:
        rosetta_api_wrkr.display_rosetta_department_info(u_dept)

    #For Readability
    print(" ")

    ########################################
    # Job Type IDs Listing
    ########################################

    #Pull List of Rosetta Job Type IDs
    l_jtids: list[RosettaJobTypeID] = rosetta_api_wrkr.get_job_type_ids()

    #Sort List by Job Type ID
    l_jtids.sort(key=lambda x: x.job_type_id)

    #Display Returned Job Type IDs
    for ucd_jtid in l_jtids:
        rosetta_api_wrkr.display_rosetta_job_type_id_info(ucd_jtid)

    #For Readability
    print(" ")


#Standard Main Function Setup
if __name__ == "__main__":
    main()




