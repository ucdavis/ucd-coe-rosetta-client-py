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


    def parse_rosetta_person_json(self,person) -> RosettaPerson:
        #Initialize Person to Return
        rosetta_person = RosettaPerson()

        rosetta_person.displayname = "Deannnnn"


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


