import unittest
from custom_functions import temperature_methods

class pruebas_unitarias(unittest.TestCase):

    def test_des_estandar(self):

        list_temps = [12, 12, 12, 12, 13, 12, 12, 12, 12, 12, 12, 14]
        total= temperature_methods.des_estandar(list_temps)

        self.assertEqual(total, 3.75)


if __name__ == '__main__':
    unittest.main()
