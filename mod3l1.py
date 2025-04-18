import unittest
from freezegun import freeze_time
from mod2 import l4

class HelloWorldTest(unittest.TestCase):
    def setUp(self):
        self.app = l4.app.test_client()
        self.app.testing = True

    @freeze_time("2025-03-31")
    def can_get_correct_username_with_weekdate_on_monday(self):
        response = self.app.get('/hello_world/Max')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Max. Хорошего понедельника!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-01")
    def can_get_correct_username_with_weekdate_on_tuesday(self):
        response = self.app.get('/hello_world/Хорошего вторника')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошего вторника. Хорошего вторника!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-02")
    def can_get_correct_username_with_weekdate_on_wednesday(self):
        response = self.app.get('/hello_world/Хорошей среды')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошей среды. Хорошей среды!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-03")
    def can_get_correct_username_with_weekdate_on_thursday(self):
        response = self.app.get('/hello_world/Хорошего четверга')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошего четверга. Хорошего четверга!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-04")
    def can_get_correct_username_with_weekdate(self):
        response = self.app.get('/hello_world/Петр')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Петр. Хорошей пятницы!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-05")
    def can_get_correct_username_with_weekdate_on_saturday(self):
        response = self.app.get('/hello_world/Хорошей субботы')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошей субботы. Хорошей субботы!'.encode('utf-8'), response.data)

    @freeze_time("2025-04-06")
    def can_get_correct_username_with_weekdate_on_sunday(self):
        response = self.app.get('/hello_world/Хорошего воскресенья')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошего воскресенья. Хорошего воскресенья!'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()