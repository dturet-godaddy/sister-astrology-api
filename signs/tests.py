from django.conf import settings
from django.test import TestCase

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


class SignTest(TestCase):

    def _check_chart(self, chart, expected):
        for position, sign in expected.items():
            self.assertEqual((chart.getObject(position)).sign, sign) \
                if position not in const.LIST_ANGLES \
                else self.assertEqual((chart.getAngle(position)).sign, sign)

    def test_july_30_1989_in_dallas_at_00_05(self):
        date = Datetime('1989/07/30', '00:05', '-05:00')
        pos = GeoPos(30.2643, -97.7139)
        chart = Chart(date, pos)
        expected = {
            const.SUN: const.LEO,
            const.MOON: const.CANCER,
            const.MERCURY: const.LEO,
            const.VENUS: const.VIRGO,
            const.MARS: const.LEO,
            const.ASC: const.ARIES,
        }
        self._check_chart(chart, expected)

    def test_may_27_1991_in_cincinatti_at_07_15(self):
        date = Datetime('1991/05/27', '07:15', '-4:00')
        pos = GeoPos(39.1031, -84.5120)
        chart = Chart(date, pos)
        expected = {
            const.SUN: const.GEMINI,
            const.MOON: const.SCORPIO,
            const.MERCURY: const.TAURUS,
            const.VENUS: const.CANCER,
            const.MARS: const.LEO,
            const.ASC: const.GEMINI,
        }
        self._check_chart(chart, expected)

