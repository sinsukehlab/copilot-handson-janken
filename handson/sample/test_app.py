import unittest
from handson.sample.app import judge

class TestJudge(unittest.TestCase):
    def test_judge_draw(self):
        self.assertEqual(judge(0, 0), 'あいこ')
        self.assertEqual(judge(1, 1), 'あいこ')
        self.assertEqual(judge(2, 2), 'あいこ')

    def test_judge_user_win(self):
        self.assertEqual(judge(0, 1), 'あなたの勝ち')
        self.assertEqual(judge(1, 2), 'あなたの勝ち')
        self.assertEqual(judge(2, 0), 'あなたの勝ち')

    def test_judge_user_lose(self):
        self.assertEqual(judge(0, 2), 'あなたの負け')
        self.assertEqual(judge(1, 0), 'あなたの負け')
        self.assertEqual(judge(2, 1), 'あなたの負け')

if __name__ == '__main__':
    unittest.main()