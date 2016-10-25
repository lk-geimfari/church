# -*- coding: utf-8 -*-

from . import DummyCase


class DatetimeTestCase(DummyCase):
    def test_day_of_week(self):
        result = self.church.datetime.day_of_week()
        self.assertIn(result, self.church.datetime.data['day']['name'])

        result_abbr = self.church.datetime.day_of_week(abbr=True)
        self.assertIn(result_abbr, self.church.datetime.data['day']['abbr'])

    def test_month(self):
        result = self.church.datetime.month() + '\n'
        self.assertGreater(len(result), 3)

        result_abbr = self.church.datetime.month(abbr=True)
        self.assertIsInstance(result_abbr, str)

    def test_year(self):
        result = self.church.datetime.year(from_=2000, to=2016)
        self.assertTrue((result >= 2000) and (result <= 2016))

    def test_periodicity(self):
        result = self.church.datetime.periodicity()
        self.assertIn(result, self.church.datetime.data['periodicity'])

    def test_day_of_month(self):
        result = self.church.datetime.day_of_month()
        self.assertTrue((result >= 1) or (result <= 31))

    def test_birthday(self):
        result = self.church.datetime.birthday()
        self.assertIsInstance(result, str)
