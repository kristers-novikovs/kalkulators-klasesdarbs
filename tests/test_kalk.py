from main import (
    addition,
    subtraction,
    division,
    multiplication
)

# Does not work if outside the main.py
# def test_addition():
#     if addition (3,4) == 7:
#         print("Test was successful! | addition succeeded")
#     else:
#         print("Test was unsuccessful! | addition failed")

# def test_subtraction():
#     if subtraction (3,4) == -1:
#         print("Test was successful! | subtraction succeeded")
#     else:
#         print("Test was unsuccessful! | subtraction failed")

# def test_division():
#     if division (8,4) == 2:
#         print("Test was successful! | division succeeded")
#     else:
#         print("Test was unsuccessful! | division failed")

# def test_multiplication():
#     if multiplication (3,4) == 12:
#         print("Test was successful! | mumultiplication succeeded")
#     else:
#         print("Test was unsuccessful! | mumultiplication failed")

def test_addition():
    assert addition (3,4) == 7
    assert addition (0,2) == 2
    assert addition (6.0,4) == 10.0
    assert addition (0.0,0.0) == 0.0
    assert addition (-4,7) == 3
def test_subtraction():
    assert subtraction (3,4) == -1
    assert subtraction (0,2) == -2
    assert subtraction (6.0,4) == 2.0
    assert subtraction (0.0,0.0) == 0.0
    assert subtraction (-4,7) == -11
def test_division():
    assert division (4,4) == 1
    assert division (4,-2) == -2
    assert division (8.0,4) == 2.0
    assert division (1.0,0.0) == "One cannot divide with 0."
    assert division (-14,7) == -2
def test_multiplication():
    assert multiplication (3,4) == 12
    assert multiplication (0,2) == 0
    assert multiplication (6.0,4) == 24.0
    assert multiplication (0.0,0.0) == 0.0
    assert multiplication (-4,7) == -28

# if __name__ == "__main__":
#     test_addition()
#     test_subtraction()
#     test_division()
#     test_multiplication()
