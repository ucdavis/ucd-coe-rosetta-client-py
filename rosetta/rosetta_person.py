
from .rosetta_employee_association import RosettaEmployeeAssociation
from .rosetta_student_association import RosettaStudentAssociation

class RosettaPerson:
    def __init__(self):
        self.iam_id = ""
        self.login_id = ""
        self.mothra_id = ""
        self.employee_id = ""
        self.display_name = ""
        self.mail_id_campus = ""
        self.mail_id_health = ""
        self.email_address_campus = ""        
        self.email_address_health = ""
        self.lived_first_name = ""
        self.lived_last_name = ""
        self.lived_pronouns = ""
        self.provisioning_status_primary = ""
        self.provisioning_status_employee = ""
        self.provisioning_status_faculty = ""
        self.provisioning_status_student = ""
        self.affiliation_employee = False
        self.affiliation_faculty = False
        self.affiliation_temporary_affiliate = False
        self.affiliation_student = False
        self.affiliation_student_applicant = False
        self.affiliation_health_affiliate = False
        self.employment_is_academic = False
        self.employment_is_academic_senate = False
        self.employment_is_academic_federation = False
        self.employment_is_faculty = False
        self.employment_is_teaching_faculty = False
        self.employment_is_ladder_rank = False
        self.employment_is_without_salary = False
        self.employment_is_msp = False
        self.employment_is_ssp = False
        self.employment_is_manager = False
        self.employment_is_campus_employee = False
        self.employment_is_health_employee = False
        self.student_associations: list[RosettaStudentAssociation] = []
        self.employee_associations: list[RosettaEmployeeAssociation] = []


