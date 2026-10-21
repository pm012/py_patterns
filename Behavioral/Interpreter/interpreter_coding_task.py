"""
You are asked to write an expression processor for simple numeric expressions with the following constraints:

Expressions use integral values (e.g., '13' ), single-letter variables defined in Variables, as well as + and - operators only

There is no need to support braces or any other operations

If a variable is not found in variables  (or if we encounter a variable with >1 letter, e.g. ab), the evaluator returns 0 (zero)

In case of any parsing failure, evaluator returns 0

Example:

calculate("1+2+3")  should return 6

calculate("1+2+xy")  should return 0

calculate("10-2-x")  when x=3 is in variables  should return 5
"""

from enum import Enum, auto

class Token:
    class Type(Enum):
        INTEGER = auto()
        VARIABLE = auto()
        PLUS = auto()
        MINUS = auto()

    def __init__(self, type, text):
        self.type = type
        self.text = text

# Abstract base class for expressions (Interpreter)
class Expression:
    def eval(self, variables) -> int:
        pass

# Terminal expression for digits
class IntegerExpression(Expression):
    def __init__(self, value: int):
        self.value = value

    def eval(self, variables) -> int:
        return self.value

# Terminal expression for strings
class VariableExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def eval(self, variables) -> int:
        # If variable is longer than 1 letter or it is absent in the dictionary -> return 0 (per task description)
        if len(self.name) != 1 or self.name not in variables:
            raise ValueError("Invalid variable")
        return variables[self.name]

# Non terminal expression for binary operations (+ or -)
class BinaryExpression(Expression):
    class Type(Enum):
        ADD = auto()
        SUBTRACT = auto()

    def __init__(self, left: Expression, right: Expression, op_type: Type):
        self.left = left
        self.right = right
        self.op_type = op_type

    def eval(self, variables) -> int:
        if self.op_type == self.Type.ADD:
            return self.left.eval(variables) + self.right.eval(variables)
        else:
            return self.left.eval(variables) - self.right.eval(variables)


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def lex(self, expression: str):
        """Converts string to list of token (Lexer)"""
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            elif expression[i] == '+':
                tokens.append(Token(Token.Type.PLUS, '+'))
                i += 1
            elif expression[i] == '-':
                tokens.append(Token(Token.Type.MINUS, '-'))
                i += 1
            elif expression[i].isdigit():
                # Read integer (can be several digits in a row)
                digits = []
                while i < len(expression) and expression[i].isdigit():
                    digits.append(expression[i])
                    i += 1
                tokens.append(Token(Token.Type.INTEGER, ''.join(digits)))
            elif expression[i].isalpha():
                # Read variable name (can be several letters in a row)
                letters = []
                while i < len(expression) and expression[i].isalpha():
                    letters.append(expression[i])
                    i += 1
                tokens.append(Token(Token.Type.VARIABLE, ''.join(letters)))
            else:
                # Any other symbol throws ValueError
                raise ValueError("Unknown character")
        return tokens

    def parse(self, tokens) -> Expression:
        """Converts token to expressions tree (Parser"""
        if not tokens:
            raise ValueError("Empty expression")

        # Check base structure: number of tokens should be even (operand, operator, operand...)
        if len(tokens) % 2 == 0:
            raise ValueError("Invalid structural layout")

        # Create first (left) expression
        first = tokens[0]
        if first.type == Token.Type.INTEGER:
            root = IntegerExpression(int(first.text))
        elif first.type == Token.Type.VARIABLE:
            root = VariableExpression(first.text)
        else:
            raise ValueError("Expression must start with an operand")

        # Handle pairs (operator, operand) and increase tree to the left(left associativity)
        i = 1
        while i < len(tokens):
            op_token = tokens[i]
            next_token = tokens[i+1]

            # Check if the operators and operands are located on correct places
            if op_token.type not in (Token.Type.PLUS, Token.Type.MINUS):
                raise ValueError("Expected operator")
            
            if next_token.type == Token.Type.INTEGER:
                right_expr = IntegerExpression(int(next_token.text))
            elif next_token.type == Token.Type.VARIABLE:
                right_expr = VariableExpression(next_token.text)
            else:
                raise ValueError("Expected operand")

            # Define operation type
            op_type = BinaryExpression.Type.ADD if op_token.type == Token.Type.PLUS else BinaryExpression.Type.SUBTRACT
            
            # Build new tree root, where current root becomes left branch
            root = BinaryExpression(root, right_expr, op_type)
            i += 2

        return root

    def calculate(self, expression):
        """Main method, called by the clinent"""
        try:
            tokens = self.lex(expression)
            tree = self.parse(tokens)
            return tree.eval(self.variables)
        except Exception:
            # Any failure of parsing should return 0 (due to the task description)
            return 0


# --- Tests ---
ep = ExpressionProcessor()
ep.variables = {'x': 3}

print(ep.calculate("1+2+3"))          # 6
print(ep.calculate("1+2+xy"))         # 0 (length of the variable > 1)
print(ep.calculate("10-2-x"))         # 5 (10 - 2 - 3)
print(ep.calculate("5 + y"))          # 0 (no variable in the dictionary)
print(ep.calculate("1++2"))           # 0 (error in expression structure)