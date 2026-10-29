from abc import ABC
from dataclasses import dataclass

#================================================================
# 1. PURE DATA STRUCTURES
#================================================================
class Expression(ABC):
    pass

@dataclass
class DoubleExpression(Expression):
    value: int

@dataclass
class AdditionExpression(Expression):
    left: Expression
    right: Expression

#================================================================
# 2. PATTERN MATCHING PROCESSORS
#================================================================
def print_expression(expr: Expression) -> str:
    """Recursively formats the expression tree into a string."""
    match expr:
        case DoubleExpression(value):
            return str(value)
        case AdditionExpression(left, right):
            return f"({print_expression(left)}+{print_expression(right)})"
        case _:
            raise TypeError(f"Unknown expression type: {type(expr).__name__}")


def evaluate_expression(expr: Expression) -> int:
    """Recursively evaluates the expression tree to an integer."""
    match expr:
        case DoubleExpression(value):
            return value
        case AdditionExpression(left, right):
            return evaluate_expression(left) + evaluate_expression(right)
        case _:
            raise TypeError(f"Unknown expression type: {type(expr).__name__}")

#================================================================
# 3. EXECUTION
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

    expr_str = print_expression(e)
    expr_val = evaluate_expression(e)

    print(f'{expr_str} = {expr_val}')  # Output: (1+(2+3)) = 6
