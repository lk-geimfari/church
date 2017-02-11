import unittest
from elizabeth.decorators import romanized_russian


class Decorators(unittest.TestCase):

    @romanized_russian
    def russian_user(self):
        return 'Ликид Геимфари'

    def test_romanize(self):
        user = self.russian_user()
        self.assertEqual(user, 'Likid Geimfari')

        username = self.russian_user()
        username = username.replace(' ', '_').lower()
        self.assertEqual(username, 'likid_geimfari')
