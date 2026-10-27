from enum import Enum, auto

class LockState(Enum):
    LOCKED = auto()
    ENTERING = auto()
    OPEN = auto()
    ERROR = auto()

class CombinationLock:
    def __init__(self, combination):
        self.combination = combination
        self.reset()

    def reset(self):
        """Resets the lock back to its initial LOCKED state."""
        self._state = LockState.LOCKED
        self.status = 'LOCKED'
        self._digits_entered = []

    def enter_digit(self, digit):
        """Processes the entered digit based on the current state."""
        
        # Dictionary acts as our switch statement for Python 3.6
        switch = {
            LockState.LOCKED: self._handle_first_digit,
            LockState.ENTERING: self._handle_subsequent_digit,
            LockState.OPEN: self._ignore_input,
            LockState.ERROR: self._ignore_input
        }
        
        # Execute the function matching the current state
        action = switch.get(self._state)
        if action:
            action(digit)

    def _handle_first_digit(self, digit):
        self._state = LockState.ENTERING
        self._digits_entered.append(digit)
        self.status = str(digit)
        self._validate_sequence()

    def _handle_subsequent_digit(self, digit):
        self._digits_entered.append(digit)
        self.status += str(digit)
        self._validate_sequence()

    def _ignore_input(self, digit):
        pass

    def _validate_sequence(self):
        """Helper to check progress against the target combination."""
        current_len = len(self._digits_entered)
        expected_part = self.combination[:current_len]

        if self._digits_entered != expected_part:
            self._state = LockState.ERROR
            self.status = 'ERROR'
        elif current_len == len(self.combination):
            self._state = LockState.OPEN
            self.status = 'OPEN'