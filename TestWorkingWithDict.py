import unittest
import WorkingWithDict as wwd
import myException as me


class Test(unittest.TestCase):
    def test_exception(self):
        self.assertRaises(me.DataTypeError, wwd.addDict, "Петров Иван Иванович", "1986",
                          "г. Москва, ул. Ленина, д. 10, кв. 5", "ОРВИ", 5)
        self.assertRaises(me.DataTypeError, wwd.addDict, "Петров Иван Иванович", 1986,
                          "г. Москва, ул. Ленина, д. 10, кв. 5", "ОРВИ", "5")
        self.assertRaises(me.DataTypeError, wwd.addDict, "Петров Иван Иванович", "1986",
                          "г. Москва, ул. Ленина, д. 10, кв. 5", "ОРВИ", .5)
        self.assertRaises(me.DataTypeError, wwd.addDict, "Петров Иван Иванович", 19.86,
                          "г. Москва, ул. Ленина, д. 10, кв. 5", "ОРВИ", 5)
        self.assertRaises(me.DataTypeError, wwd.addDict, "Петров Иван Иванович", 1986,
                          "г. Москва, ул. Ленина, д. 10, кв. 5", True, 5)
        self.assertRaises(me.DataTypeError, wwd.addDict, "Петров Иван Иванович", False,
                          "г. Москва, ул. Ленина, д. 10, кв. 5", "ОРВИ", 5)
        self.assertRaises(me.DataTypeError, wwd.addDict, 123, 1986, "г. Москва, ул. Ленина, д. 10, кв. 5", "ОРВИ", 5)
        self.assertRaises(me.DataTypeError, wwd.addDict, "Петров Иван Иванович", 1986, False, "ОРВИ", 5)
        self.assertRaises(me.DataTypeError, wwd.addDict, "Петров Иван Иванович", 1986,
                          "г. Москва, ул. Ленина, д. 10, кв. 5", "ОРВИ", [1, 2])

        self.assertRaises(me.DataTypeError, wwd.findBySurname, 123)
        self.assertRaises(me.DataTypeError, wwd.findBySurname, True)
        self.assertRaises(me.DataTypeError, wwd.findBySurname, 1.2)

        self.assertRaises(me.DataTypeError, wwd.findByDiagnosis, 123)
        self.assertRaises(me.DataTypeError, wwd.findByDiagnosis, True)
        self.assertRaises(me.DataTypeError, wwd.findByDiagnosis, 1.2)

        self.assertRaises(me.DataTypeError, wwd.findByYearRange, "1999", 2015)
        self.assertRaises(me.DataTypeError, wwd.findByYearRange, 1965, True)
        self.assertRaises(me.DataTypeError, wwd.findByYearRange, False, 2000)
        self.assertRaises(me.DataTypeError, wwd.findByYearRange, 19.22, 2000)

        self.assertRaises(me.DataTypeError, wwd.findByYearRange, 2000, 1996)


if __name__ == "__main__":
    unittest.main()
