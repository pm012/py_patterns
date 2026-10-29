from abc import ABC
from dataclasses import dataclass
from functools import singledispatchmethod

#================================================================
# PURE DATA STRUCTURES (No Boilerplate, Simple Nodes)
#================================================================
class Expression(ABC):
    pass

@dataclass
class DoubleExpression(Expression):
    value: int

@dataclass
class AdditionExpression(Expression):
    # Changed type hint to Expression to properly allow nested trees
    left: Expression
    right: Expression

#================================================================
# THE VISITORS (Using Python Standard Library)
#================================================================
class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @singledispatchmethod
    def visit(self, expression: Expression):
        """Fallback method for unregistered Expression subtypes."""
        raise TypeError(f"Unknown expression type: {type(expression).__name__}")

    @visit.register
    def _(self, expr: DoubleExpression):
        self.buffer.append(str(expr.value))

    @visit.register
    def _(self, expr: AdditionExpression):
        self.buffer.append('(')
        self.visit(expr.left)
        self.buffer.append('+')
        self.visit(expr.right)
        self.buffer.append(')')

    def __str__(self):
        return ''.join(self.buffer)


class ExpressionEvaluator:
    # Instead of an instance side-effect, we can return values directly,
    # making the code much more functional and thread-safe.
    @singledispatchmethod
    def visit(self, expression: Expression) -> int:
        """Fallback method."""
        raise TypeError(f"Unknown expression type: {type(expression).__name__}")

    @visit.register
    def _(self, expr: DoubleExpression) -> int:
        return expr.value

    @visit.register
    def _(self, expr: AdditionExpression) -> int:
        return self.visit(expr.left) + self.visit(expr.right)

#================================================================
# EXECUTION
#================================================================
if __name__ == "__main__":
    # Represents 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    printer = ExpressionPrinter()
    printer.visit(e)

    evaluator = ExpressionEvaluator()
    result = evaluator.visit(e)

    print(f'{printer} = {result}')  # Output: (1+(2+3)) = 6
