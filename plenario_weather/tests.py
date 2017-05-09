from os.path import isfile
from unittest import TestCase

from plenario_weather.tasks import download_hourly


class TestIngest(TestCase):

    def test_download_noaa_hourly_data(self):

        download_hourly('2017-01-01')
        self.assertTrue(isfile('QCLCD201701.zip'))
