from abc import ABC

class Expression(ABC):
    pass

class DoubleExpression(Expression):
    def __init__(self, value:int):
        self.value = value  
         

class AdditionExpression(Expression):
    def __init__(self, left:DoubleExpression, right:DoubleExpression):
        self.left = left
        self.right = right

class ExpressionPrinter:
    @staticmethod
    def print(expression: Expression,  buffer:list):
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(')')

    Expression.print = lambda self, b: ExpressionPrinter.print(self,b)

# Still breaks OCP because new types require MxN modifications



    
if __name__ == "__main__":
    # represents 1+(2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []
    #e.print(buffer)
    # ExpressionPrinter.print(e, buffer)
    e.print(buffer)


    print(''.join(buffer))  