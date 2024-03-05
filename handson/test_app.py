import unittest
from unittest.mock import patch
import app

class TestApp(unittest.TestCase):

    @patch('app.input', return_value='0')
    @patch('app.random.randint', return_value=1)
    def test_main_win(self, input, randint):
        with patch('app.print') as mocked_print:
            app.main()
            mocked_print.assert_any_call('あなたの勝ち')

    @patch('app.input', return_value='0')
    @patch('app.random.randint', return_value=0)
    def test_main_draw(self, input, randint):
        with patch('app.print') as mocked_print:
            app.main()
            mocked_print.assert_any_call('あいこ')

    @patch('app.input', return_value='0')
    @patch('app.random.randint', return_value=2)
    def test_main_lose(self, input, randint):
        with patch('app.print') as mocked_print:
            app.main()
            mocked_print.assert_any_call('あなたの負け')

if __name__ == '__main__':
    unittest.main()