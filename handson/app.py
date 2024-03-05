# じゃんけんゲームを作成します。
# じゃんけんの手は、0: グー、1: チョキ、2: パーとする
# じゃんけんの手を入力すると、コンピュータの手と勝敗が表示されます。
# じゃんけんの手は、標準入力から受け取ります。
# じゃんけんの手は、整数値で受け取ります。
# じゃんけんの手は、整数値以外が入力された場合は、再入力を求めます。
# じゃんけんの手とコンピュータの手、勝敗は、標準出力に出力します。

# じゃんけんの勝敗を判定する
# @param hand: じゃんけんの手
# @param computer_hand: コンピュータの手
# @return じゃんけんの勝敗
def judge(hand, computer_hand):
    if hand == computer_hand:
        return 'あいこ'
    elif hand == 0 and computer_hand == 1:
        return 'あなたの勝ち'
    elif hand == 1 and computer_hand == 2:
        return 'あなたの勝ち'
    elif hand == 2 and computer_hand == 0:
        return 'あなたの勝ち'
    else:
        return 'あなたの負け'

# ユーザーのじゃんけんの手を受け取り、コンピューターの手とともにjudge関数に渡す
# ユーザーとコンピューターの手をそれぞれ日本語で表示する
# judge関数の結果を標準出力に出力する
def main():
    hand = int(input('じゃんけんの手を入力してください（0: グー、1: チョキ、2: パー）: '))
    while hand < 0 or 2 < hand:
        hand = int(input('0から2の整数で入力してください: '))
    computer_hand = random.randint(0, 2)
    print('あなた: ' + ['グー', 'チョキ', 'パー'][hand])
    print('コンピューター: ' + ['グー', 'チョキ', 'パー'][computer_hand])
    print(judge(hand, computer_hand))

if __name__ == '__main__':
    main()
