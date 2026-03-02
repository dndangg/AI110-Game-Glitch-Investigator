import sys
from pathlib import Path

# Add parent directory to path so we can import logic_utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# ===== TESTS FOR INVERTED HINTS BUG FIX =====
# These tests verify that the hint messages are correct (not inverted)

def test_guess_too_high_hint_is_go_lower():
    # BUG FIX: When guess is too high, the hint should tell user to go LOWER, not HIGHER
    # Secret: 50, Guess: 75 (too high)
    # Expected: outcome "Too High" with message containing "LOWER"
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message or "📉" in message
    assert "HIGHER" not in message or "📈" not in message


def test_guess_too_low_hint_is_go_higher():
    # BUG FIX: When guess is too low, the hint should tell user to go HIGHER, not LOWER
    # Secret: 50, Guess: 25 (too low)
    # Expected: outcome "Too Low" with message containing "HIGHER"
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message or "📈" in message
    assert "LOWER" not in message or "📉" not in message


# ===== TESTS FOR DIFFICULTY RANGE BUG FIX =====
# These tests verify that difficulty ranges are correctly ordered: Easy < Normal < Hard

def test_difficulty_ranges_are_correctly_ordered():
    # BUG FIX: Hard difficulty should have a larger range than Normal
    # Before fix: Easy(20) < Hard(50) < Normal(100) [WRONG]
    # After fix: Easy(20) < Normal(100) < Hard(500) [CORRECT]
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    
    # Easy should be the smallest range
    easy_range = easy_high - easy_low
    # Normal should be larger than Easy
    normal_range = normal_high - normal_low
    # Hard should be the largest range
    hard_range = hard_high - hard_low
    
    assert easy_range < normal_range, f"Easy range ({easy_range}) should be smaller than Normal ({normal_range})"
    assert normal_range < hard_range, f"Normal range ({normal_range}) should be smaller than Hard ({hard_range})"


def test_hard_difficulty_larger_than_normal():
    # BUG FIX: Verify that Hard (1-500) is larger than Normal (1-100)
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, f"Hard upper bound ({hard_high}) should be greater than Normal ({normal_high})"
