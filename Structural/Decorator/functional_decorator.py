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

@time_decorator
def function1(seconds:int):
    time.sleep(seconds)
    print("Function 1 executed")

@time_decorator
def function2(seconds:int):
    time.sleep(seconds)
    print("Function 2 executed")

if __name__ == "__main__":
    function1(1)
    function2(2)