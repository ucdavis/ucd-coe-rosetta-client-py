## Rosetta API Client Example

A simple repository demonstrating how to access the UCD Rosetta API. You can integrate the Rosetta package into another project or use this repository as a standalone client.

To obtain the API credentials required for authentication, please contact the Campus Identity team.

### Resource Links

- [Rosetta - UC Davis IAM API](https://anypoint.mulesoft.com/exchange/portals/university-of-california-346/9b04bfa8-6eeb-4d85-b676-91db930f8411/iam-rosetta-api/minor/1.0/pages/home/)

### Example of .env file

```bash
# Rosetta Client ID
ROSETTA_CLIENT_ID=obtain-from-the-identity-team

# Rosetta Client Secret
ROSETTA_CLIENT_SECRET=obtain-from-the-identity-team

# Rosetta Base URL
ROSETTA_BASE_URL=https://obtain-from-the-identity-team.io/api/v1/

# Rosetta OAuth URL
ROSETTA_OAUTH_URL=https://obtain-from-the-identity-team.io/token

# Rosetta Test IAM ID
ROSETTA_TEST_ID=member-iam-id-to-test-with

```

### Script Usage Examples

Get Members by IAM IDs
```bash
python3 ./main.py people-iamids "1000550201,1000016201,1000438403,1000227051"
```
Get Member by Login
```bash
python3 ./main.py people-login dbunn
```
Get Member by Email Address
```bash
python3 ./main.py people-email dbunn@ucdavis.edu
```
Get All Members in a Department
```bash
python3 ./main.py people-department 024000
```
Get Employee Associations by Department
```bash
python3 ./main.py employee-departmentid 024000
```

### Script Argument Options

- people-iamid \<iamid\>
- people-iamids \<iamid,iamid,iamid\>
- people-iamids-all-state \<iamid,iamid,iamid\>
- people-login \<userid\>
- people-login-all-state \<userid\>
- people-email \<emailaddress\>
- people-employeeid \<employeeid\>
- people-studentid \<studentid\>
- people-pidm \<pidm\>
- people-mailid \<mailid\>
- people-mailid-all-state \<mailid\>
- people-department \<departmentcode\>
- employee-iamid \<iamid\>
- employee-departmentid \<departmentid\>
- employee-divisionid \<divisionid\>
- employee-subdivisionid \<subdivisionid\>
- employee-subdivisionl4id \<subdivisionl4id\>
- student-iam \<iamid\>
- student-pidm \<pidm\>
- student-studentid \<studentid\>
- student-majorcode \<majorcode\>
- student-collegecode \<collegecode\>
- departments show
- jobtypeids show