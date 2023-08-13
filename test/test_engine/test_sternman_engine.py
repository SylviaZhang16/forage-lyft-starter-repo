import unittest

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test__needs_service_true(self):
        last_service_mileage = 10000
        warning_light_is_on = True
        engine = SternmanEngine(last_service_mileage, warning_light_is_on)
        self.assertTrue(engine.needs_service)
