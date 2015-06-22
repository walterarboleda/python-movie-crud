from django.test import TestCase

from MovieLib.models import Movie
import decimal
import datetime

# Create your tests here.
class MovieTests(TestCase):
    """Movie model tests."""

    def test_str(self):
        m = Movie(title = "The muse",
                  genre = 'Comedy',
                  price = decimal.Decimal(11),
                  release_date = datetime.date(2014, 7, 17))

        self.assertEqual(str(m), "The muse - Comedy - 11 - 2014-07-17")