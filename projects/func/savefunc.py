import os


def function_to_save():
    if not os.path.exists("projects/data"):
        os.makedirs("projects/data")
