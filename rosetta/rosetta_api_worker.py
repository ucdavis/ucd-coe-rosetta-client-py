import os
import requests
import json
from datetime import datetime, timedelta
from enum import StrEnum

from .rosetta_person import RosettaPerson
from .rosetta_employee_association import RosettaEmployeeAssociation
from .rosetta_student_association import RosettaStudentAssociation

class RosettaAPIWorker:
    def __init__(self,base_url: str,token_url: str,client_id: str,client_secret: str):
        #Validate Parameters
        if not isinstance(base_url, str) or not base_url.strip():
            raise ValueError("Base URL is missing")

        if not isinstance(token_url, str) or not token_url.strip():
                    raise ValueError("Token URL is missing")

        if not isinstance(client_id, str) or not client_id.strip():
                    raise ValueError("Client ID is missing")

        if not isinstance(client_secret, str) or not client_secret.strip():
                    raise ValueError("Client Secret is missing")

        self.base_url = base_url
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.oath_token = ""
        self.expires_in = datetime.now() + timedelta(hours=-1)

    class PeopleSearchBy(StrEnum):
        IAMID = "iamid"
        LOGINID = "loginid"
        EMAIL = "email"
        EMPLOYEEID = "employeeid"
        STUDENTID = "studentid"
        MAILID = "mailid"
        DEPARTMENT = "department"

    class EmployeeSearchBy(StrEnum):
        IAMID = "iamid"
        DEPARTMENTID = "departmentid"
        DIVISIONID = "divisionid"
        SUBDIVISIONID = "subdivisionid"
        SUBDIVISIONL4ID = "subdivisionl4id"
        ORGANIZATIONID = "organizationid"

    class StudentSearchBy(StrEnum):
        IAMID = "iamid"
        PIDM = "pidm"
        STUDENTID = "studentid"
        MAJORCODE = "majorcode"
        COLLEGECODE = "collegecode"


    def check_oauth_token(self) -> bool:
        #Var for Return Status
        b_token_status = True

        if self.expires_in < datetime.now() + timedelta(minutes=1):

            #Configure OAuth Header
            headersOAuthCall = {"client_id": self.client_id,
                                "client_secret": self.client_secret,
                                "grant_type":"CLIENT_CREDENTIALS",
                                "scope":"read:public"}

            #Make Rest Call to Token EndPoint to Get Access Token
            responseTokenInfo = requests.post(self.token_url,headers=headersOAuthCall)

            if(responseTokenInfo.status_code == 200):

                #Var for Response Headers
                responseHeaders = responseTokenInfo.headers

                #Var for Response Json Data
                responseData = responseTokenInfo.json()
                  
                if(len(responseData['access_token']) > 0):
                    self.oath_token = responseData['access_token']
                    self.expires_in = datetime.now() + timedelta(seconds=responseData['expires_in'])
                else:
                    b_token_status = False

            else:
                b_token_status = False
                

        return b_token_status
    

    def parse_rosetta_employee_assoc_json(self,empassoc) -> RosettaEmployeeAssociation:
        #Initialize Employee Association to Return
        rosetta_emp_assoc = RosettaEmployeeAssociation()

        #Retrieve IAM ID
        if empassoc.get("iam_id") is not None:
            rosetta_emp_assoc.iam_id = empassoc["iam_id"]

        #Retrieve Reports to IAM ID
        if empassoc.get("reports_to_iam_id") is not None:
            rosetta_emp_assoc.reports_to_iam_id = empassoc["reports_to_iam_id"]

        #Retrieve Reports to Employee ID
        if empassoc.get("reports_to_employee_id") is not None:
            rosetta_emp_assoc.reports_to_employee_id = empassoc["reports_to_employee_id"]

        #Retrieve Employee ID
        if empassoc.get("employee_id") is not None:
            rosetta_emp_assoc.employee_id = empassoc["employee_id"]

        #Retrieve Employee Record
        if empassoc.get("employee_record") is not None:
            rosetta_emp_assoc.employee_record = empassoc["employee_record"]

        #Retrieve Position Number
        if empassoc.get("position_number") is not None:
            rosetta_emp_assoc.position_number = empassoc["position_number"]

        #Retrieve Position Title
        if empassoc.get("position_title") is not None:
            rosetta_emp_assoc.position_title = empassoc["position_title"]

        #Retrieve Job Indicator
        if empassoc.get("job_indicator") is not None:
            rosetta_emp_assoc.job_indicator = empassoc["job_indicator"]

        #Retrieve Relationship to Organization
        if empassoc.get("relationship_to_organization") is not None:
            rosetta_emp_assoc.relationship_to_organization = empassoc["relationship_to_organization"]

        #Retrieve Employee Classification
        if empassoc.get("employee_classification") is not None:
            rosetta_emp_assoc.employee_classification = empassoc["employee_classification"]

        #Retrieve Employee Classification Description
        if empassoc.get("employee_classification_description") is not None:
            rosetta_emp_assoc.employee_classification_description = empassoc["employee_classification_description"]

        #Retrieve Status
        if empassoc.get("status") is not None:
            rosetta_emp_assoc.status = empassoc["status"]

        #Retrieve Hire Date
        if empassoc.get("hire_date") is not None:
            rosetta_emp_assoc.hire_date = empassoc["hire_date"]

        #Retrieve Start Date
        if empassoc.get("start_date") is not None:
            rosetta_emp_assoc.start_date = empassoc["start_date"]

        #Retrieve FTE Percentage
        if empassoc.get("fte_percentage") is not None:
            rosetta_emp_assoc.fte_percentage = empassoc["fte_percentage"]

        #Retrieve Reports to Position
        if empassoc.get("reports_to_position") is not None:
            rosetta_emp_assoc.reports_to_position = empassoc["reports_to_position"]

        #Retrieve Job Type ID
        if empassoc.get("job_type_id") is not None:
            rosetta_emp_assoc.job_type_id = empassoc["job_type_id"]

        #Retrieve Job Type Description
        if empassoc.get("job_type_description") is not None:
            rosetta_emp_assoc.job_type_description = empassoc["job_type_description"]

        #Retrieve Organization ID
        if empassoc.get("organization_id") is not None:
            rosetta_emp_assoc.organization_id = empassoc["organization_id"]

        #Retrieve Organization Title
        if empassoc.get("organization_title") is not None:
            rosetta_emp_assoc.organization_title = empassoc["organization_title"]

        #Retrieve Division ID
        if empassoc.get("division_id") is not None:
            rosetta_emp_assoc.division_id = empassoc["division_id"]

        #Retrieve Division Title
        if empassoc.get("division_title") is not None:
            rosetta_emp_assoc.division_title = empassoc["division_title"]

        #Retrieve Subdivision ID
        if empassoc.get("subdivision_id") is not None:
            rosetta_emp_assoc.subdivision_id = empassoc["subdivision_id"]

        #Retrieve Subdivision Title
        if empassoc.get("subdivision_title") is not None:
            rosetta_emp_assoc.subdivision_title = empassoc["subdivision_title"]

        #Retrieve Subdivision L4 ID
        if empassoc.get("subdivision_l4_id") is not None:
            rosetta_emp_assoc.subdivision_l4_id = empassoc["subdivision_l4_id"]

        #Retrieve Subdivision L4 Title
        if empassoc.get("subdivision_l4_title") is not None:
            rosetta_emp_assoc.subdivision_l4_title = empassoc["subdivision_l4_title"]

        #Retrieve Business Unit ID
        if empassoc.get("business_unit_id") is not None:
            rosetta_emp_assoc.business_unit_id = empassoc["business_unit_id"]

        #Retrieve Business Unit Title
        if empassoc.get("business_unit_title") is not None:
            rosetta_emp_assoc.business_unit_title = empassoc["business_unit_title"]

        #Retrieve Department ID
        if empassoc.get("department_id") is not None:
            rosetta_emp_assoc.department_id = empassoc["department_id"]

        #Retrieve Department Title
        if empassoc.get("department_title") is not None:
            rosetta_emp_assoc.department_title = empassoc["department_title"]

        #Retrieve Department Short Title
        if empassoc.get("department_short_title") is not None:
            rosetta_emp_assoc.department_short_title = empassoc["department_short_title"]

        #Retrieve Is Health Position
        if empassoc.get("is_health_position") is not None:
            rosetta_emp_assoc.is_health_position = empassoc["is_health_position"]

        #Retrieve Is Campus Position
        if empassoc.get("is_campus_position") is not None:
            rosetta_emp_assoc.is_campus_position = empassoc["is_campus_position"]

        #Retrieve Modified Date
        if empassoc.get("modified_date") is not None:
            rosetta_emp_assoc.modified_date = empassoc["modified_date"]

        #Retrieve Create Date
        if empassoc.get("create_date") is not None:
            rosetta_emp_assoc.create_date = empassoc["create_date"]


        return rosetta_emp_assoc


    def parse_rosetta_person_json(self,person) -> RosettaPerson:
        #Initialize Person to Return
        rosetta_person = RosettaPerson()

        #Retrieve Display Name
        if person.get("displayname") is not None:
            rosetta_person.display_name = person["displayname"]

        #Retrieve IAM ID
        if person.get("iam_id") is not None:
            rosetta_person.iam_id = person["iam_id"]
        
        #Retrieve IDs
        if person.get("id") is not None:
            #Pull ID Node
            jn_ids = person["id"]

            #Retrieve IAM ID
            if jn_ids.get("iam_id") is not None:
                rosetta_person.iam_id = jn_ids["iam_id"]

            #Retrieve Login ID
            if jn_ids.get("login_id") is not None:
                rosetta_person.login_id = jn_ids["login_id"]

            #Retrieve Mothra ID
            if jn_ids.get("mothra_id") is not None:
                rosetta_person.mothra_id = jn_ids["mothra_id"]

            #Retrieve Employee ID
            if jn_ids.get("employee_id") is not None:
                rosetta_person.employee_id = jn_ids["employee_id"]

            if jn_ids.get("mail_id") is not None:
                #Pull Mail ID Node
                jn_ids_mail = jn_ids["mail_id"]

                if jn_ids_mail.get("campus") is not None:
                    rosetta_person.mail_id_campus = jn_ids_mail["campus"]

                if jn_ids_mail.get("health") is not None:
                    rosetta_person.mail_id_health = jn_ids_mail["health"]

        #Retrieve Names Node
        if person.get("name") is not None:
            #Pull Name Node
            jn_names = person["name"]

            #Retrieve Lived First Name
            if jn_names.get("lived_first_name") is not None:
                rosetta_person.lived_first_name = jn_names["lived_first_name"]

            #Retrieve Lived Last Name
            if jn_names.get("lived_last_name") is not None:
                rosetta_person.lived_last_name = jn_names["lived_last_name"]

            #Retrieve Lived Pronouns
            if jn_names.get("lived_pronouns") is not None:
                rosetta_person.lived_pronouns = jn_names["lived_pronouns"]

        #Retrieve Email Addresses
        if person.get("email") is not None:

            #Retrieve Email Node
            jn_email = person["email"]

            #Retrieve Campus Email Address
            if jn_email.get("campus") is not None:
                rosetta_person.email_address_campus = jn_email["campus"]

            #Retrieve Health System Email Address
            if jn_email.get("health") is not None:
                rosetta_person.email_address_health = jn_email["health"]


        #Retrieve Provisioning Status
        if person.get("provisioning_status") is not None:

            #Retrieve Provisioning Status Node
            jn_provisioning_status = person["provisioning_status"]

            #Retrieve Primary Provisioning Status
            if jn_provisioning_status.get("primary") is not None:
                rosetta_person.provisioning_status_primary = jn_provisioning_status["primary"]

            #Retrieve Employee Provisioning Status
            if jn_provisioning_status.get("employee") is not None:
                rosetta_person.provisioning_status_employee = jn_provisioning_status["employee"]

            #Retrieve Faculty Provisioning Status
            if jn_provisioning_status.get("faculty") is not None:
                rosetta_person.provisioning_status_faculty = jn_provisioning_status["faculty"]

            #Retrieve Student Provisioning Status
            if jn_provisioning_status.get("student") is not None:
                rosetta_person.provisioning_status_student = jn_provisioning_status["student"]


        #Retrieve Affiliations
        if person.get("affiliation") is not None:

            #Retrieve Affiliation Node
            jn_affiliation = person["affiliation"]

            #Retrieve Employee Affiliation
            if jn_affiliation.get("employee") is not None:
                if jn_affiliation["employee"].upper() == "Y":
                    rosetta_person.affiliation_employee = True
                else:
                    rosetta_person.affiliation_employee = False

            #Retrieve Faculty Affiliation
            if jn_affiliation.get("faculty") is not None:
                if jn_affiliation["faculty"].upper() == "Y":
                    rosetta_person.affiliation_faculty = True
                else:
                    rosetta_person.affiliation_faculty = False

            #Retrieve Temporary Affiliation
            if jn_affiliation.get("temporary_affiliate") is not None:
                if jn_affiliation["temporary_affiliate"].upper() == "Y":
                    rosetta_person.affiliation_temporary_affiliate = True
                else:
                    rosetta_person.affiliation_temporary_affiliate = False

            #Retrieve Student Affiliation
            if jn_affiliation.get("student") is not None:
                if jn_affiliation["student"].upper() == "Y":
                    rosetta_person.affiliation_student = True
                else:
                    rosetta_person.affiliation_student = False

            #Retrieve Student Applicant Affiliation
            if jn_affiliation.get("student_applicant") is not None:
                if jn_affiliation["student_applicant"].upper() == "Y":
                    rosetta_person.affiliation_student_applicant = True
                else:
                    rosetta_person.affiliation_student_applicant = False

            #Retrieve Health Affiliation
            if jn_affiliation.get("health_affiliate") is not None:
                if jn_affiliation["health_affiliate"].upper() == "Y":
                    rosetta_person.affiliation_health_affiliate = True
                else:
                    rosetta_person.affiliation_health_affiliate = False


        #Retrieve Employment Status
        if person.get("employment_status") is not None:

            #Retrieve Employment Statuses
            jn_employment_status = person["employment_status"]

            #Retrieve Academic Status
            if jn_employment_status.get("is_academic") is not None:
                if jn_employment_status["is_academic"].upper() == "Y":
                    rosetta_person.employment_is_academic = True
                else:
                    rosetta_person.employment_is_academic = False

            #Retrieve Academic Senate Status
            if jn_employment_status.get("is_academic_senate") is not None:
                if jn_employment_status["is_academic_senate"].upper() == "Y":
                    rosetta_person.employment_is_academic_senate = True
                else:
                    rosetta_person.employment_is_academic_senate = False

            #Retrieve Academic Federation Status
            if jn_employment_status.get("is_academic_federation") is not None:
                if jn_employment_status["is_academic_federation"].upper() == "Y":
                    rosetta_person.employment_is_academic_federation = True
                else:
                    rosetta_person.employment_is_academic_federation = False

            #Retrieve Faculty Status
            if jn_employment_status.get("is_faculty") is not None:
                if jn_employment_status["is_faculty"].upper() == "Y":
                    rosetta_person.employment_is_faculty = True
                else:
                    rosetta_person.employment_is_faculty = False

            #Retrieve Teaching Faculty Status
            if jn_employment_status.get("is_teaching_faculty") is not None:
                if jn_employment_status["is_teaching_faculty"].upper() == "Y":
                    rosetta_person.employment_is_teaching_faculty = True
                else:
                    rosetta_person.employment_is_teaching_faculty = False

            #Retrieve Ladder Rank Status
            if jn_employment_status.get("is_ladder_rank") is not None:
                if jn_employment_status["is_ladder_rank"].upper() == "Y":
                    rosetta_person.employment_is_ladder_rank = True
                else:
                    rosetta_person.employment_is_ladder_rank = False

            #Retrieve Without Salary Status
            if jn_employment_status.get("is_without_salary") is not None:
                if jn_employment_status["is_without_salary"].upper() == "Y":
                    rosetta_person.employment_is_without_salary = True
                else:
                    rosetta_person.employment_is_without_salary = False

            #Retrieve MSP Status
            if jn_employment_status.get("is_msp") is not None:
                if jn_employment_status["is_msp"].upper() == "Y":
                    rosetta_person.employment_is_msp = True
                else:
                    rosetta_person.employment_is_msp = False

            #Retrieve SSP Status
            if jn_employment_status.get("is_ssp") is not None:
                if jn_employment_status["is_ssp"].upper() == "Y":
                    rosetta_person.employment_is_ssp = True
                else:
                    rosetta_person.employment_is_ssp = False

            #Retrieve Manager Status
            if jn_employment_status.get("is_manager") is not None:
                if jn_employment_status["is_manager"].upper() == "Y":
                    rosetta_person.employment_is_manager = True
                else:
                    rosetta_person.employment_is_manager = False

            #Retrieve Campus Employee Status
            if jn_employment_status.get("is_campus_employee") is not None:
                if jn_employment_status["is_campus_employee"].upper() == "Y":
                    rosetta_person.employment_is_campus_employee = True
                else:
                    rosetta_person.employment_is_campus_employee = False

            #Retrieve Health Employee Status
            if jn_employment_status.get("is_health_employee") is not None:
                if jn_employment_status["is_health_employee"].upper() == "Y":
                    rosetta_person.employment_is_health_employee = True
                else:
                    rosetta_person.employment_is_health_employee = False


        return rosetta_person


    def get_people_by_search_term(self,search_by: PeopleSearchBy, search_term: str) -> list[RosettaPerson]:
        #Var for Returned People List
        people: list[RosettaPerson] = []

        #Var for Search Result Limit
        n_srch_rslt_limit = 100

        #Var for Search Result Offset
        n_srch_rslt_offset = 0

        #Var for Retrieve More Search Results
        b_retr_more_srch_rslts = True

        while b_retr_more_srch_rslts == True:
            if self.check_oauth_token():
                #Var for Header of People EndPoint Call
                headerEPCall = {"Authorization":"Bearer " + self.oath_token}

                #Var for URI
                peopleUri = self.base_url + "people?" + search_by + "=" + search_term + "&offset=" + str(n_srch_rslt_offset) + "&limit=" + str(n_srch_rslt_limit) + "&count=true"

                #Call to People Endpoint
                responsePeople = requests.get(peopleUri,headers=headerEPCall)

                #Check Returned Status Code
                if responsePeople.status_code == 200:

                    #Pull X-Total-Count and X-Response-Count Values
                    nTotalCnt: int | None = int(responsePeople.headers.get("x-total-count"))
                    nRspnCnt: int | None = int(responsePeople.headers.get("x-response-count"))

                    #Check Total and Reponse Counts are Not Empty
                    if nTotalCnt is not None and nTotalCnt > 0 and nRspnCnt is not None and nRspnCnt > 0:
                        #Var for Response Data
                        responseData = responsePeople.json()

                        for person in responseData:
                            parsed_person = self.parse_rosetta_person_json(person)
                            people.append(parsed_person)

                        #Increment Offset
                        n_srch_rslt_offset += n_srch_rslt_limit

                        #Check Offset to Total Count
                        if n_srch_rslt_offset >= nTotalCnt:
                            b_retr_more_srch_rslts = False

                    else:
                        b_retr_more_srch_rslts = False

                else:
                    b_retr_more_srch_rslts = False

            else:
                b_retr_more_srch_rslts = False
                

        return people


