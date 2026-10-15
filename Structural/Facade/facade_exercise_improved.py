"""
A magic square is a square matrix of numbers where the sum in each row, each column, and each of the diagonals is the same.

You are given a system of 3 classes that can be used to make a magic square. The classes are:

Generator: this class generates a 1-dimensional list of random digits in range 1 to 9.

Splitter: this class takes a 2D list and splits it into all possible arrangements of 1D lists. 
It gives you the columns, the rows and the two diagonals.

Verifier: this class takes a 2D list and verifies that the sum of elements in every sublist is the same.

Please implement a Façade class called MagicSquareGenerator  which simply generates the magic square of a given size.
"""

from random import randint
import random
import sys
import time

def time_decorator(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        print(f"Executing {func.__name__}...")
        res=func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {(end_time - start_time)*1000} milliseconds")
        return res
    return inner

class Generator:
  def generate(self, count):
    return random.sample(range(1, count+1), count) #[randint(1,9) for x in range(count)]

class Splitter:
    def split(self, array):
        row_count = len(array)        
        # Rows
        rows = list(array)
        # Columns
        cols = list(zip(*array))
        # Diagonals
        diag1 = [array[i][i] for i in range(row_count)]
        diag2 = [array[i][row_count - 1 - i] for i in range(row_count)]
        
        return rows + list(cols) + [diag1, diag2]
    
class Verifier:
  def verify(self, arrays):
    first = sum(arrays[0])

    for i in range(1, len(arrays)):
      if sum(arrays[i]) != first:
        return False

    return True

class MagicSquareGenerator:  
  def generate(self, size):
    if size <=2:
      print("Incorrect dimension of square. It should be >=2.")
      print(f"Exit with code: 0")
      sys.exit(0)
      
    generator = Generator()
    splitter = Splitter()
    verifier = Verifier()
    while True:
        square = []
        for _ in range(size):
            square.append(generator.generate(size))
        all_lines = splitter.split(square)

        if verifier.verify(all_lines):
          return square

#=================START More Optimized Version==========================
class SiamMagicSquareGenerator:
    def generate(self, size: int) -> list[list[int]]:
        """Universal method to generate magic square depending from its size."""
        if size < 3:
            raise ValueError("Magic squares less than 3х3 don't exist.")
        
        if size % 2 != 0:
            return self._generate_odd(size)
        elif size % 4 == 0:
            return self._generate_doubly_even(size)
        else:
            raise ValueError(
                f"Size {size}x{size} (singly even: 6x6, 10x10..etc) requires distinct algorithm "
                "and for now it is not supported by this basic class."
            )

    def _generate_odd(self, size: int) -> list[list[int]]:
        """Algorith for odds(Siam Method)."""
        square = [[0] * size for _ in range(size)]
        row, col = 0, size // 2

        for num in range(1, size * size + 1):
            square[row][col] = num
            next_row = (row - 1) % size
            next_col = (col + 1) % size

            if square[next_row][next_col] != 0:
                row = (row + 1) % size
            else:
                row = next_row
                col = next_col

        return square

    def _generate_doubly_even(self, size: int) -> list[list[int]]:
        """Algorithm for even sizes, multiple of 4 (4x4, 8x8, 12x12)."""
        square = [[0] * size for _ in range(size)]
        
        # 1. Filling in the matrix with sequence of numbers from  1 to size^2
        num = 1
        for r in range(size):
            for c in range(size):
                square[r][c] = num
                num += 1

        # 2. Inverting values on diagonals of 4x4 blocks
        total = size * size + 1
        for r in range(size):
            for c in range(size):
                if (r % 4 == c % 4) or (r % 4 + c % 4 == 3):
                    square[r][c] = total - square[r][c]

        return square

#=================END More Optimized Version==========================


class SquarePrinter:
  def print_square(self, square):
    for row in square:
        print(" ".join(f"{num:2d}" for num in row))

@time_decorator
def simple_magic_square_generator_launch(size:int):
   
   msg = MagicSquareGenerator()
   magic_square = msg.generate(size)
   
   print("Magic square:")
   sp = SquarePrinter()
   sp.print_square(magic_square)

@time_decorator
def improved_magic_square_generator_launch(size:int):
   
   msg = SiamMagicSquareGenerator()
   magic_square = msg.generate(size)
   
   print("Magic square:")
   sp = SquarePrinter()
   sp.print_square(magic_square)
   

    

if __name__ == "__main__":
   
   print("Simple 5")
   simple_magic_square_generator_launch(5)
   print("Simple 4")
   simple_magic_square_generator_launch(4)

   print("Improved 5")
   improved_magic_square_generator_launch(5)
   print("Improved 4")
   improved_magic_square_generator_launch(4)


    


