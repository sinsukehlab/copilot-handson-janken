import unittest
from unittest.mock import patch
from app import janken_game

class TestJankenGame(unittest.TestCase):
    @patch('app.input', return_value='0')
    @patch('app.random.randint', return_value=1)
    @patch('sys.stdout.write')
    def test_gu_win(self, mock_stdout, mock_randint, mock_input):
        janken_game()
        mock_stdout.assert_any_call("あなたの勝ちです！")

    @patch('app.input', return_value='0')
    @patch('app.random.randint', return_value=4)
    @patch('sys.stdout.write')
    def test_gu_lose(self, mock_stdout, mock_randint, mock_input):
        janken_game()
        mock_stdout.assert_any_call("あなたの負けです！")

    @patch('app.input', return_value='0')
    @patch('app.random.randint', return_value=0)
    @patch('sys.stdout.write')
    def test_gu_draw(self, mock_stdout, mock_randint, mock_input):
        janken_game()
        mock_stdout.assert_any_call("引き分けです！")

    @patch('app.input', return_value='0')
    @patch('app.random.randint', return_value=2)
    @patch('sys.stdout.write')
    def test_gu_no_match(self, mock_stdout, mock_randint, mock_input):
        janken_game()
        mock_stdout.assert_any_call("勝負なしです！")

    # 以下、チョキ、パー、リンゴ、バナナについても同様にテストケースを作成します。
    # ...

if __name__ == '__main__':
    unittest.main()
    