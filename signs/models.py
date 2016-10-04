from __future__ import unicode_literals
from django.db import models


class Sign(models.Model):
    ARIES = 'Aries'
    TAURUS = 'Taurus'
    GEMINI = 'Gemini'
    CANCER = 'Cancer'
    LEO = 'Leo'
    VIRGO = 'Virgo'
    LIBRA = 'Libra'
    SCORPIO = 'Scorpio'
    SAGITTARIUS = 'Sagittarius'
    CAPRICORN = 'Capricorn'
    AQUARIUS = 'Aquarius'
    PISCES = 'Pisces'
    SIGNS = (
        ('ari', ARIES),
        ('tau', TAURUS),
        ('gem', GEMINI),
        ('can', CANCER),
        ('leo', LEO),
        ('vir', VIRGO),
        ('lib', LIBRA),
        ('sco', SCORPIO),
        ('sag', SAGITTARIUS),
        ('cap', CAPRICORN),
        ('aqu', AQUARIUS),
        ('pis', PISCES),
    )

    WATER = 'Water'
    FIRE = 'Fire'
    EARTH = 'Earth'
    AIR = 'Air'
    ELEMENTS = (
        ('water', WATER),
        ('fire', FIRE),
        ('earth', EARTH),
        ('air', AIR),
    )

    CARDINAL = 'Cardinal'
    FIXED = 'Fixed'
    MUTABLE = 'Mutable'
    MODES = (
        ('cardinal', CARDINAL),
        ('fixed', FIXED),
        ('mutable', MUTABLE),
    )

    PASSIVE = 'Passive'
    ASSERTIVE = 'Assertive'
    DUALITIES = (
        (0, PASSIVE),
        (1, ASSERTIVE),
    )

    name = models.CharField(choices=SIGNS, max_length=12)
    element = models.CharField(choices=ELEMENTS, max_length=8)
    modality = models.CharField(choices=MODES, max_length=10)
    duality = models.IntegerField(choices=DUALITIES)
#
#
# class Chart(models.Model):
#     user = models.ForeignKey(auth.get_user_model(), blank=True, null=True)
#
#     sun_sign = models.ForeignKey(Sign, related_name='charts_with_sun_position')
#     moon_sign = models.ForeignKey(Sign, related_name='charts_with_moon')
#     venus_sign = models.ForeignKey(Sign, related_name='charts_with_venus')
#     mars_sign = models.ForeignKey(Sign)
#     mercury_sign = models.ForeignKey(Sign)
