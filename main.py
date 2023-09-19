import WorkingWithDict as wwd


def main():
    filePath = "C:\\Users\\Andrew\\Desktop"
    fileName = "PatientList"
    surname = "Петров"
    minYear = 1965
    maxYear = 1999
    diagnosis = "ОРВИ"
    wwd.dataImport(filePath, fileName)
    print("\n\t\t======= Полный словарь =======")
    wwd.printDict()
    print(f'\n\t\t======= Поиск по фамилии: {surname} =======')
    wwd.findBySurname(surname)
    print(f'\n\t\t======= Поиск по диапазону рождения с {minYear} по {maxYear} год =======')
    wwd.findByYearRange(minYear, maxYear)
    print(f'\n\t\t======= Поиск по диагнозу: {diagnosis} =======')
    wwd.findByDiagnosis(diagnosis)
    pass


if __name__ == '__main__':
    main()
