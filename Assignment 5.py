# Decorator that prints the result in a boxed format


def output_decorator(title):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)            # run the real function
            line = "#" * 26
            inputs = ", ".join(str(a) for a in args)

            print(line)
            print("# " + title)
            print("# input: " + inputs)
            print("# output: " + str(result))
            print(line)
            return result
        return wrapper
    return decorator


@output_decorator("Adding")
def add(a, b):
    return a + b


@output_decorator("Multiplying")
def multiply(a, b):
    return a * b


add(4, 3)
multiply(5, 6)
