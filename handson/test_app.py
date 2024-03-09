import unittest
from unittest.mock import patch
import app

class TestApp(unittest.TestCase):

    def test_cases(self):
        outcomes = {
            (0, 0): 'あいこ',
            (0, 1): 'あなたの勝ち',
            (0, 2): 'あなたの負け',
            (1, 0): 'あなたの負け',
            (1, 1): 'あいこ',
            (1, 2): 'あなたの勝ち',
            (2, 0): 'あなたの勝ち',
            (2, 1): 'あなたの負け',
            (2, 2): 'あいこ'
        }

        for (input_value, random_value), outcome in outcomes.items():
            with patch('app.input', return_value=str(input_value)), \
                 patch('app.random.randint', return_value=random_value), \
                 patch('builtins.print') as mocked_print:
                app.main()
                mocked_print.assert_any_call(outcome)

if __name__ == '__main__':
    unittest.main()