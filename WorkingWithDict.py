import myException as me

__patients = []


def printDict():
    for patient in __patients[:]:
        print(patient)


pass


def findByYearRange(minYear: int, maxYear: int):
    me.__raiseCheckInt(minYear)
    me.__raiseCheckInt(maxYear)
    me.__raiseYearBirth(minYear)
    me.__raiseYearBirth(maxYear)
    me.__raiseExceedingYear(minYear,maxYear)

    for patient in __patients[:]:
        if patient["Year"] >= minYear and patient["Year"] <= maxYear:
            print(patient)
    pass


def findBySurname(surname: str):
    me.__raiseCheckString(surname)
    for patient in __patients[:]:
        if surname == __splitString(patient.get("FullName"))[0]:
            print(patient)
    pass


def findByDiagnosis(diagnosis: str):
    me.__raiseCheckString(diagnosis)

    numDayStay = []
    for patient in __patients[:]:
        if diagnosis == patient.get("Diagnosis"):
            numDayStay.append(patient.get("numDayStay"))
            print(patient)
    me.__raiseCollectionEmpty(numDayStay)

    print(f'Minimum number of days of stay with diagnosis: {diagnosis} = {min(numDayStay)} day')
    print(f'Maximum number of days of stay with diagnosis: {diagnosis} = {max(numDayStay)} day')
    pass


def __splitString(text: str) -> str:
    return text.split()


def addDict(fullName: str, year: int, address: str, diagnosis: str, numDayStay: int):
    me.__raiseCheckInt(year)
    me.__raiseCheckInt(numDayStay)

    me.__raiseCheckString(fullName)
    me.__raiseCheckString(address)
    me.__raiseCheckString(diagnosis)

    __patients.append(
        {'FullName': fullName, 'Year': year, "Address": address, "Diagnosis": diagnosis, "numDayStay": numDayStay})
    pass


def dataImport(filePath: str, fileName: str):
    me.__raiseCheckString(fileName)
    me.__raiseCheckString(filePath)

    file = open(f'{filePath}\\{fileName}.txt', "r", encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            break
        line = line.split(";")
        addDict(line[0].strip(), int(line[1]), line[2].strip(), (line[3]).strip(), int(line[4]))
    file.close()
    pass
