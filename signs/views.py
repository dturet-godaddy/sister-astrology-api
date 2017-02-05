import requests
from django.db import models
from django.shortcuts import render
from rest_framework import status

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView

from flatlib import const
from flatlib.chart import Chart
from flatlib.chart import Datetime
from flatlib.geopos import GeoPos

from datetime import datetime, timedelta
import pytz
import time

class ChartView(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get_chart(self, birthdayString, birthTimeString, offsetString, geo_coordinates):
        # date = Datetime('1989/07/30', '00:05', '-05:00')
        date = Datetime(birthdayString, birthTimeString, offsetString)
        # pos = GeoPos(30.2643, -97.7139)
        pos = GeoPos(geo_coordinates['lat'], geo_coordinates['lng'])
        return Chart(date, pos)

    def get_sign(self, chart, position):
        return str(chart.getObject(position).sign).lower()

    def get_angle(self, chart, obj):
        return (chart.getAngle(obj).sign).lower()

    def toDateTimeObject(self, birthday, birthtime=None):
        date = [int(d) for d in birthday.split("/")]
        time = ([int(d) for d in birthtime.split(":")]) if birthtime else [12, 0]  # default to noon
        d = date + time + [0]
        return datetime(d[0], d[1], d[2], d[3], d[4], d[5])

    def post(self, request, format=None):
        serializer = ChartRequest(data=request.data)
        if serializer.is_valid():
            serializer.save()
            birthday, birthtime, birthplace = serializer.data["birthday"], serializer.data["birthtime"], serializer.data["birthplace"]
            geo_coordinates = self.get_geo_cords(birthplace)
            birthdate = self.toDateTimeObject(birthday, birthtime)
            offset = self.get_offset(birthdate, geo_coordinates)
            chart = self.get_chart(birthday, birthtime, offset, geo_coordinates)
            return Response(self.create_chart_map(chart))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_chart_map(self, chart):
        content = {
            'sun': self.get_sign(chart, const.SUN),
            'moon': self.get_sign(chart, const.MOON),
            'mercury': self.get_sign(chart, const.MERCURY),
            'venus': self.get_sign(chart, const.VENUS),
            'mars': self.get_sign(chart, const.MARS),
            'ascendant': self.get_angle(chart, const.ASC)
        }
        return content

    def format_offset(self, off):
        # get the time delta from utcoffset
        if off is not None:
            if off.days < 0:
                sign = "-"
                off = -off
            else:
                sign = "+"
            hh, mm = divmod(off, timedelta(hours=1))
            assert not mm % timedelta(minutes=1), "whole minute"
            mm //= timedelta(minutes=1)
            print("%s%02d:%02d" % (sign, hh, mm))
            return "%s%02d:%02d" % (sign, hh, mm)

    def get_offset(self, datetime, geo_coordinates):
        TIMEZONE_URL = "https://maps.googleapis.com/maps/api/timezone/json"
        TIMEZONE_KEY = "AIzaSyC9zVD_QM8eg0iigqYQ5CeCrpydPIf654w"

        lat_long = str(geo_coordinates["lat"]) + "," + str(geo_coordinates['lng'])
        payload = {"key": TIMEZONE_KEY, "location": lat_long, "timestamp": int(time.time())}

        r = requests.get(TIMEZONE_URL, params=payload)

        zone_id = r.json()["timeZoneId"]
        time_zone = pytz.timezone(zone_id)

        return self.format_offset(time_zone.utcoffset(datetime))

    def get_geo_cords(self, place):
        GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
        GEOCODE_KEY = "AIzaSyCZS0Whye8bkySqyIQrq3hPVMSz9ZGjZkU"

        payload = {"key": GEOCODE_KEY, "address": place}

        r = requests.get(GEOCODE_URL, params=payload)

        return r.json()["results"][0]["geometry"]["location"]


class ChartRequest(serializers.Serializer):
    birthday = serializers.CharField()
    birthtime = serializers.CharField(required=False)
    birthplace = serializers.CharField(required=False, max_length=100)

    def create(self, validated_data):
        return validated_data
