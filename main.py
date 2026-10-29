
from dotenv import load_dotenv
import os
import sys
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


    #List for Returned List of Rosetta People
    l_people: list[RosettaPerson] = []

    #List for Returned List of Employee Associations
    l_employee_assocs: list[RosettaEmployeeAssociation] = []

    #List for Returned List of Student Associations
    l_student_assocs: list[RosettaStudentAssociation] = []

    #List for Returned List of Job Type IDs
    l_jtids: list[RosettaJobTypeID] = []

    #List for Returned List of Departments
    l_departments: list[RosettaDepartment] = []

    #Set for Unique IDs for Post People Lookup
    s_mpl_ids = set()


    #Check for Supplied Script Arguments
    if len(sys.argv) == 3:
        
        match sys.argv[1]:
            case "people-iamid":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.IAMID,sys.argv[2])
            case "people-iamids":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.IAMIDS,sys.argv[2])
            case "people-iamids-all-state":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.IAMIDSALLSTATE,sys.argv[2])
            case "people-login":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.LOGINID,sys.argv[2])
            case "people-login-all-state":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.LOGINIDALLSTATE,sys.argv[2])
            case "people-email":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.EMAIL,sys.argv[2])
            case "people-employeeid":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.EMPLOYEEID,sys.argv[2])
            case "people-studentid":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.STUDENTID,sys.argv[2])
            case "people-pidm":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.PIDM,sys.argv[2])
            case "people-mailid":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.MAILID,sys.argv[2])
            case "people-mailid-all-state":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.MAILIDALLSTATE,sys.argv[2])
            case "people-department":
                l_people = rosetta_api_wrkr.get_people_by_search_term(rosetta_api_wrkr.PeopleSearchBy.DEPARTMENT,sys.argv[2])
            case "employee-iamid":
                l_employee_assocs = rosetta_api_wrkr.get_employee_associations_by_search_term(rosetta_api_wrkr.EmployeeSearchBy.IAMID,sys.argv[2])
            case "employee-departmentid":
                l_employee_assocs = rosetta_api_wrkr.get_employee_associations_by_search_term(rosetta_api_wrkr.EmployeeSearchBy.DEPARTMENTID,sys.argv[2])
            case "employee-divisionid":
                l_employee_assocs = rosetta_api_wrkr.get_employee_associations_by_search_term(rosetta_api_wrkr.EmployeeSearchBy.DIVISIONID,sys.argv[2])
            case "employee-subdivisionid":
                l_employee_assocs = rosetta_api_wrkr.get_employee_associations_by_search_term(rosetta_api_wrkr.EmployeeSearchBy.SUBDIVISIONID,sys.argv[2])
            case "employee-subdivisionl4id":
                l_employee_assocs = rosetta_api_wrkr.get_employee_associations_by_search_term(rosetta_api_wrkr.EmployeeSearchBy.SUBDIVISIONL4ID,sys.argv[2])
            case "student-iamid":
                l_student_assocs = rosetta_api_wrkr.get_student_associations_by_search_term(rosetta_api_wrkr.StudentSearchBy.IAMID,sys.argv[2])
            case "student-pidm":
                l_student_assocs = rosetta_api_wrkr.get_student_associations_by_search_term(rosetta_api_wrkr.StudentSearchBy.PIDM,sys.argv[2])
            case "student-studentid":
                l_student_assocs = rosetta_api_wrkr.get_student_associations_by_search_term(rosetta_api_wrkr.StudentSearchBy.STUDENTID,sys.argv[2])
            case "student-majorcode":
                l_student_assocs = rosetta_api_wrkr.get_student_associations_by_search_term(rosetta_api_wrkr.StudentSearchBy.MAJORCODE,sys.argv[2])
            case "student-collegecode":
                l_student_assocs = rosetta_api_wrkr.get_student_associations_by_search_term(rosetta_api_wrkr.StudentSearchBy.COLLEGECODE,sys.argv[2])
            case "departments":
                l_departments = rosetta_api_wrkr.get_departments()
            case "jobtypeids":
                l_jtids = rosetta_api_wrkr.get_job_type_ids()

    else: 
        print(" ")
        print("Argument Options:")
        print("=======================")
        print("people-iamid <iamid>")
        print("people-iamids <iamid>")
        print("people-iamids-all-state <iamids>")
        print("people-login <userid>")
        print("people-login-all-state <userid>")
        print("people-email <emailaddress>")
        print("people-employeeid <employeeid>")
        print("people-studentid <studentid>")
        print("people-pidm <pidm>")
        print("people-mailid <mailid>")
        print("people-mailid-all-state <mailid>")
        print("people-department <departmentcode>")
        print("employee-iamid <iamid>")
        print("employee-departmentid <departmentid>")
        print("employee-divisionid <divisionid>")
        print("employee-subdivisionid <subdivisionid>")
        print("employee-subdivisionl4id <subdivisionl4id>")
        print("student-iam <iamid>")
        print("student-pidm <pidm>")
        print("student-studentid <studentid>")
        print("student-majorcode <majorcode>")
        print("student-collegecode <collegecode>")
        print("departments show")
        print("jobtypeids show")
        print(" ")
        print(" ")

        

    #######################################
    # Display Employee Associations
    #######################################

    if len(l_employee_assocs) > 0:

        #For Readability
        print(" ")

        for uemp_assoc in l_employee_assocs:

            #Add Employee's IAM to MPL IDs Set for People Post Lookup 
            s_mpl_ids.add(uemp_assoc.iam_id)

            #Display Employee Association Info
            rosetta_api_wrkr.display_rosetta_employee_association_info(uemp_assoc)
  
        #For Readability
        print(" ")

    #######################################
    # Display Student Associations 
    #######################################

    if len(l_student_assocs) > 0:

        #For Readability
        print(" ")

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
    # Display Rosetta People
    #######################################

    if len(l_people) > 0:

        for upeep in sorted(l_people, key=lambda x: x.display_name):
            rosetta_api_wrkr.display_rosetta_person_info(upeep)

        #For Readability
        print(" ")

    ########################################
    # Display Departments 
    ########################################

    if len(l_departments) > 0:

        #Display Department Information
        for u_dept in l_departments:
            rosetta_api_wrkr.display_rosetta_department_info(u_dept)

        #For Readability
        print(" ")

    ########################################
    # Display Job Type IDs 
    ########################################

    if len(l_jtids) > 0:

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




