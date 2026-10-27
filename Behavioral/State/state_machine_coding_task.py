from enum import Enum, auto
import unittest

class LockState(Enum):
    LOCKED = auto()
    ENTERING = auto()
    OPEN = auto()
    ERROR = auto()

class CombinationLock:
    def __init__(self, combination):
        self.combination = combination
        self._state = LockState.LOCKED
        self.status = 'LOCKED'
        self._digits_entered = []

    def reset(self):
        """Resets the lock back to its initial LOCKED state."""
        self._state = LockState.LOCKED
        self.status = 'LOCKED'
        self._digits_entered = []

    def enter_digit(self, digit):
        """Processes the entered digit based on the current state."""
        match self._state:
            case LockState.OPEN | LockState.ERROR:
                # Once OPEN or ERROR, ignore further input until reset
                return
            
            case LockState.LOCKED:
                # Transition to ENTERING state on the first digit
                self._state = LockState.ENTERING
                self._digits_entered.append(digit)
                self.status = str(digit)
                self._validate_sequence()

            case LockState.ENTERING:
                # Continue appending digits
                self._digits_entered.append(digit)
                self.status += str(digit)
                self._validate_sequence()

    def _validate_sequence(self):
        """Helper to check progress against the target combination."""
        current_len = len(self._digits_entered)
        expected_part = self.combination[:current_len]

        # If the input doesn't match the expected prefix so far -> ERROR
        if self._digits_entered != expected_part:
            self._state = LockState.ERROR
            self.status = 'ERROR'
        # If it matches and we've reached the full length -> OPEN
        elif current_len == len(self.combination):
            self._state = LockState.OPEN
            self.status = 'OPEN'


# --- Unit Tests ---

class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

    def test_failure(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(9)  # Wrong digit
        self.assertEqual('ERROR', cl.status)
        
    def test_reset(self):
        cl = CombinationLock([1, 2])
        cl.enter_digit(1)
        cl.reset()
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        cl.enter_digit(2)
        self.assertEqual('OPEN', cl.status)

if __name__ == '__main__':
    unittest.main()
