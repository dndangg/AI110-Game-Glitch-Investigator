# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## Hints for Students

### Bug 1: Inverted Hints (Lines 42-45)
- Play the game and guess too high (80 when secret is 50)
- The message says "Go HIGHER!" but you should go lower
- Swap the hint messages. If guess > secret, say "Go LOWER!"

### Bug 2: Difficulty Range Mismatch (Line 9)
- Hard (1-50) has fewer numbers than Normal (1-100).That's easier, not harder.
- Change Hard from `1, 50` to `1, 500`
## ✅ Summary of Changes Made

### 1. Fixed Inverted Hint Logic
- **File:** `app.py` and `logic_utils.py` (lines 42-45)
- **Change:** Swapped hint messages in `check_guess()`
  - When guess > secret: Changed from "Go HIGHER!" to "Go LOWER!"
  - When guess < secret: Changed from "Go LOWER!" to "Go HIGHER!"
- **Impact:** Hints now correctly guide players to find the secret number

### 2. Fixed Difficulty Range Order
- **File:** `app.py` and `logic_utils.py` (line 9)
- **Change:** Updated Hard difficulty range from `1, 50` to `1, 500`
- **Impact:** Difficulty levels now properly ordered: Easy (20) < Normal (100) < Hard (500)

### 3. Refactored Functions into `logic_utils.py`
- Moved `get_range_for_difficulty()` from app.py
- Moved `parse_guess()` from app.py
- Moved `check_guess()` from app.py (with bug fixes)
- Moved `update_score()` from app.py

### 4. Added Comprehensive Test Cases
- **File:** `tests/test_game_logic.py`
- **Tests added:** 4 new pytest cases targeting the bugs
  - `test_guess_too_high_hint_is_go_lower()` - Verifies inverted hints fix
  - `test_guess_too_low_hint_is_go_higher()` - Verifies inverted hints fix
  - `test_difficulty_ranges_are_correctly_ordered()` - Verifies difficulty order
  - `test_hard_difficulty_larger_than_normal()` - Verifies Hard > Normal
- **Result:** All 7 tests passing ✅
