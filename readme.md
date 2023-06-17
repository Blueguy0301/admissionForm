# How to read the data inside the forms:

The data structure of the file will look like this :

```json
{
    'f137': False,
    'f138': False,
    'gmc': False,
    'idPic': False,
    'interview': False,
    'lpe': False,
    'lbe': False,
    'psa': False,
    'f137Right': False,
    'f138Right': False,
    'gmcRight': False,
    'idPicRight': False,
    'interviewRight': False,
    'lpeRight': False,
    'lbeRight': False,
    'psaRight': False,
    'age': '',
    'daMonth': '',
    'daDay': '',
    'daYear': '',
    'firstName': '',
    'middleInitial': '',
    'lastName': '',
    'address': '',
    'dobMonth': '',
    'dobYear': '',
    'dobDay': '',
    'sex': 'M',
    'religion': '',
    'pob': '',
    'citizenship': '',
    'status': '',
    'contact': '',
    'email': '',
    'mother': '',
    'mOccupation': '',
    'father': '',
    'fOccupation': '',
    'gName': '',
    'gContact': '',
    'gRelationship': '',
    'gAddress': '',
    'pSchool': '',
    'pGraduate': '',
    'pAddress': '',
    'sSchool': '',
    'sGraduate': '',
    'sAddress': '',
    'sStrand': '',
    'tSchool': '',
    'tGraduate': '',
    'tAddress': '',
    'tNA': False,
    'vSchool': '',
    'vAddress': '',
    'vNA': False,
    'firstCourse': '',
    'firstMajor': '',
    'secondCourse': '',
    'secondMajor': ''
}
```

to read the data in python just simply add [] plus the key:

```python
sex = data['sex']
print(sex) #prints M
```

[documentation](https://www.w3schools.com/python/python_dictionaries.asp)

## Adding data to the database.

ISANG file na lang ang i eedit niyo. to add the data to the data base, just open the `validation.py` and ENTER YOUR CODE INSIDE THE ONE AND ONLY FUNCTION/METHOD na meron ang file nayon.
