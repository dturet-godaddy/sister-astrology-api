from django.test import TestCase

# Create your tests here.
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


class SignTest(TestCase):

    def test_july_30_is_leo_sun(self):
        # from flatlib.datetime import Datetime
        date = Datetime('2015/03/13', '06:05', '+06:00')
        pos = GeoPos(30.2643,-97.7139)
        self.assertEqual(pos.lat, 30.2643)
        self.assertEqual(pos.lon, -97.7139)
        from flatlib import const
        import ipdb; ipdb.set_trace()
        chart = Chart(date, pos)
