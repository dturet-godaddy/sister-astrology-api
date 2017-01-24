from django.shortcuts import render


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


class ChartView(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        date = Datetime('1989/07/30', '00:05', '-05:00')
        pos = GeoPos(30.2643, -97.7139)
        chart = Chart(date, pos)

        content = {
            'sun': (chart.getObject(const.SUN).sign).lower(),
            'moon': (chart.getObject(const.MOON).sign).lower(),
            'mercury': (chart.getObject(const.MERCURY).sign).lower(),
            'venus': (chart.getObject(const.VENUS).sign).lower(),
            'mars': (chart.getObject(const.MARS).sign).lower(),
            'ascendant': (chart.getObject(const.ASC).sign).lower(),
        }
        return Response(content)

