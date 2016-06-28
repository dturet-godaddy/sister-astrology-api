from __future__ import unicode_literals
from django.contrib import auth
from django.db import models


# class Sign(models.Model):
#     ARIES = 'Aries'
#     TAURUS = 'Taurus'
#     GEMINI = 'Gemini'
#     CANCER = 'Cancer'
#     LEO = 'Leo'
#     VIRGO = 'Virgo'
#     LIBRA = 'Libra'
#     SCORPIO = 'Scorpio'
#     SAGITTARIUS = 'Sagittarius'
#     CAPRICORN = 'Capricorn'
#     AQUARIUS = 'Aquarius'
#     PISCES = 'Pisces'
#
#
# class Chart(models.Model):
#     user = models.ForeignKey(auth.get_user_model(), blank=True, null=True)
#
#     sun_sign = models.ForeignKey(Sign, related_name='charts_with_sun')
#     moon_sign = models.ForeignKey(Sign, related_name='charts_with_moon')
#     venus_sign = models.ForeignKey(Sign, related_name='charts_with_venus')
#     mars_sign = models.ForeignKey(Sign)
#     mercury_sign = models.ForeignKey(Sign)
