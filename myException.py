class DataTypeError(Exception):
    pass


class CollectionEmpty(DataTypeError):
    pass


class TransendingDataBoundariesError(CollectionEmpty):
    pass


def __raiseCheckInt(i):
    if type(i) not in [int]:
        raise DataTypeError("Invalid data type, must be int."
                            "You have '{0}' with the type of {1}".format(i, type(i)))


def __raiseCheckString(i):
    if type(i) not in [str]:
        raise DataTypeError("Invalid data type, must be String."
                            "You have '{0}' with the type of {1}".format(i, type(i)))


def __raiseCollectionEmpty(i):
    if not i:
        raise CollectionEmpty("It is not possible to determine the minimum and maximum number "
                              "of days of stay, because a dictionary with such a diagnosis was not found.")


def __raiseYearBirth(i):
    if i <= 0:
        raise TransendingDataBoundariesError("Data entered incorrectly. Check the date of birth item, this "
                                             "item cannot have a negative value")


def __raiseExceedingYear(minYear, maxYear):
    if minYear > maxYear:
        raise TransendingDataBoundariesError("Data inconsistency. The 'minYear' parameter connot exceed 'maxYear'")
