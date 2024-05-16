import random
import sys
sys.path.insert(0, '/path/to/handson')
from app import hands

# Test 1: User wins with rock (グー)
user_hand = 0
random.seed(1)  # Set the random seed for predictable computer hand
computer_hand = random.randint(0, 5)
print(f"User hand: {hands[user_hand]}")
print(f"Computer hand: {hands[computer_hand]}")
# Expected output: あなたの勝ちです！

# Test 2: User loses with paper (パー)
user_hand = 2
random.seed(2)  # Set the random seed for predictable computer hand
computer_hand = random.randint(0, 5)
print(f"User hand: {hands[user_hand]}")
print(f"Computer hand: {hands[computer_hand]}")
# Expected output: あなたの負けです！

# Test 3: Draw with scissors (チョキ)
user_hand = 1
random.seed(3)  # Set the random seed for predictable computer hand
computer_hand = random.randint(0, 5)
print(f"User hand: {hands[user_hand]}")
print(f"Computer hand: {hands[computer_hand]}")
# Expected output: 引き分けです！

# Test 4: Invalid input
user_hand = 6
try:
    print(f"User hand: {hands[user_hand]}")
    print(f"Computer hand: {hands[computer_hand]}")
except IndexError:
    print("Expected output: 入力が無効です。再入力してください。")
# Expected output: 入力が無効です。再入力してください。

# Test 5: User wins with orange (オレンジ)
user_hand = 5
random.seed(5)  # Set the random seed for predictable computer hand
computer_hand = random.randint(0, 5)
print(f"User hand: {hands[user_hand]}")
print(f"Computer hand: {hands[computer_hand]}")
# Expected output: あなたの勝ちです！