# Task 1

import logging
from functools import wraps

# One-time setup for logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Handle positional and keyword parameters
        pos_params = list(args) if args else "none"
        kw_params = dict(kwargs) if kwargs else "none"

        # Call the original function and capture the return value
        result = func(*args, **kwargs)

        # Log the details
        logger.info(
            f"function: {func.__name__} "
            f"positional parameters: {pos_params} "
            f"keyword parameters: {kw_params} "
            f"return: {result}"
        )
        return result
    return wrapper

# To write a log record:
logger.log(logging.INFO, "this string would be logged")