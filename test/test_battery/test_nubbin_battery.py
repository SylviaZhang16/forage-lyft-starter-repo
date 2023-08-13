import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-05-15")
        last_service_date = date.fromisoformat("2020-05-15")
        battery = NubbinBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())
