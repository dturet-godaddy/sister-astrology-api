from django.test import TestCase

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


class SignTest(TestCase):

    def test_july_30_is_leo_sun(self):
        date = Datetime('1989/07/30', '12:05', '+06:00')
        pos = GeoPos(30.2643, -97.7139)
        self.assertEqual(pos.lat, 30.2643)
        self.assertEqual(pos.lon, -97.7139)
        chart = Chart(date, pos)
        sun = chart.getObject(const.SUN)
        self.assertEqual(sun.sign, const.LEO)

    def test_may_27_is_crazy_ass_gemini_sun(self):
        date = Datetime('1991/05/27', '08:30', '+05:00')
        pos = GeoPos(39.1031, -84.5120)
        self.assertEqual(pos.lat, 39.1031)
        self.assertEqual(pos.lon, -84.5120)
        chart = Chart(date, pos)
        sun = chart.getObject(const.SUN)
        self.assertEqual(sun.sign, const.GEMINI)
