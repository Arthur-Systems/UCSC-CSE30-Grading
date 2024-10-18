# cse30
# pa2: tic-tac-toe
# tests modules board.py and player.py

import os
import re
import difflib
import sys

if __name__ == "__main__":

    score = 0
    extra_credit = 0
    total = 40
    command = "python3"  # may need to change to 'py' or 'python3'
    module1 = "tictac.py"
    module2 = "testAI.py"
    module3 = "testMinimax.py"
    module4 = "testSmartAI.py"

    # 1 Board
    try:
        from board import Board

        print("module board and class Board are implemented +2/2 points")
        score += 2
    except:
        print("module board or class Board is not implemented +0/2 points")
    # 2 Player
    try:
        from player import Player

        print("module player and class Player are implemented +2/2 points")
        score += 2
    except:
        print("module player or class Player is not implemented +0/2 points")
    # 3 Board Methods
    try:
        board = Board()
        board.get_winner()
        board.set("A1", "X")
        board.isempty("A1")
        board.isdone()
        print("All Board methods are implemented +4/4 points")
        score += 4
    except:
        print("Not all Board methods are implemented +0/4 points")
    # 4 Player Methods
    try:
        player = Player("Bob", "X")
        player.get_sign()
        player.get_name()
        print("All Player methods are implemented +4/4 points")
        score += 4
    except:
        print("Not all Player methods are implemented +0/4 points")
    # 5 ex1
    try:
        os.system(f"{command} {module1} < ex1 > output 2> errors")
        with open("errors", "r") as f:
            errors = f.read().strip()
        print(errors)
        assert len(errors) == 0, "Errors detected in player execution."
        print("Player runs without errors with input 1 +2/2 points")
        score += 2

    except AssertionError as e:
        print("Player runs with errors with input 1 +0/2 points")
        print("Error details:", str(e).split(":")[-1].strip())
        print("Player output with input 1 is incorrect +0/2 points")

    else:
        try:
            with open("output", "r") as f:
                output = f.read().strip()

            with open("ex1.out", "r") as f1:
                out = f1.read().strip()

            assert re.sub(r"\s", "", output) == re.sub(
                r"\s", "", out
            ), "Output mismatch."
            print("Player output with input 1 is correct +2/2 points")
            score += 2

        except AssertionError as e:
            print("Player output with input 1 is incorrect +0/2 points")
            print(
                "Error details:", str(e).split(":")[-1].strip()
            )  # Print only the error message

    # 6 ex2
    try:
        # Execute the module and capture stdout, stderr
        os.system(f"{command} {module1} < ex2 > output 2> errors")
        with open("errors", "r") as f:
            errors = f.read().strip()
        assert len(errors) == 0, "Errors detected in player execution."
        print("Player runs without errors with input 2 +2/2 points")
        score += 2

    except AssertionError as e:
        print("Player runs with errors with input 2 +0/2 points")
        print("Error details:", str(e).split(":")[-1].strip())
        print("Player output with input 2 is incorrect +0/2 points")
    else:
        try:
            with open("output", "r") as f:
                student_output = [line.strip() for line in f.readlines()]

            with open("ex2.out", "r") as f1:
                expected_output = [line.strip() for line in f1.readlines()]

            differ = difflib.HtmlDiff()
            html_diff = differ.make_file(student_output, expected_output)

            if '<td class="diff_next"' in html_diff:
                with open("player_diff.html", "w") as f:
                    f.write(html_diff)
                print("Differences found; output does not match expected +0/2 points")
            else:
                print("No differences found.")
                print("Player output with input 2 is correct +2/2 points")
                score += 2

        except FileNotFoundError as e:
            print("File not found:", str(e).split(":")[-1].strip())

        except Exception as e:
            print("An unexpected error occurred:", str(e).split(":")[-1].strip())

    # 7 AI
    try:
        # Execute the module2 script, capturing stdout and stderr
        os.system(f"{command} {module2} > output 2> errors")

        # Check for errors by reading the errors file
        with open("errors", "r") as f:
            errors = f.read().strip()
        assert errors == "", "Error log is not empty."
        print("AI runs without errors +4/4 points")
        score += 4

    except AssertionError:
        _, exc_value, _ = sys.exc_info()
        print("AI runs with errors +0/4 points")
        print(exc_value)
        print("AI output is incorrect +0/4 points")

    else:
        try:
            with open("output", "r") as f:
                output = f.read().strip()

            # Validate output based on expected patterns
            assert re.search(
                r"\bis a winner!|It is a tie!", output
            ), "Expected AI victory message not found."
            print("AI output is correct +4/4 points")
            score += 4

        except AssertionError:
            _, exc_value, _ = sys.exc_info()
            print("AI output is incorrect +0/4 points")
            print(exc_value)

    # 8 Minimax

    try:
        # Execute the Minimax module, capturing stdout and stderr
        os.system(f"{command} {module3} > output 2> errors")

        # Check for errors by reading the errors file
        with open("errors", "r") as f:
            errors = f.read().strip()
        assert len(errors) == 0, "Error log is not empty."
        print("Minimax runs without errors +4/4 points")
        score += 4

    except AssertionError:
        _, exc_value, _ = sys.exc_info()  # Captures the exception value
        print("Minimax runs with errors +0/4 points")
        print(exc_value)  # Prints just the error message from the exception
        print("Minimax output is incorrect +0/8 points")

    else:
        try:
            with open("output", "r") as f:
                output = f.read().strip()
            # Validate output based on expected patterns
            assert (
                re.findall(r"It is a tie!", output) != []
            ), "Expected at least one tie message."
            assert (
                re.findall(r"\bis a winner!", output) == []
            ), "No winner message expected."
            print("Minimax output is correct +8/8 points")
            score += 8

        except AssertionError:
            _, exc_value, _ = sys.exc_info()  # Captures the exception value
            print("Minimax output is incorrect +0/8 points")
            print(exc_value)  # Prints just the error message from the exception

    # 9 SmartAI
    try:
        # Execute the SmartAI module, capturing stdout and stderr
        os.system(f"{command} {module4} > output 2> errors")

        with open("errors", "r") as f:
            errors = f.read().strip()  # Strip whitespace to ensure empty means empty
        assert errors == "", "Error log is not empty."
        print("SmartAI runs without errors +1/1 points")
        extra_credit += 1

    except AssertionError:
        _, exc_value, _ = sys.exc_info()  # Captures the exception value
        print("SmartAI runs with errors +0/1 points")
        print(exc_value)  # Prints just the error message from the exception
        print("SmartAI output is incorrect +0/4 points")

    else:
        try:
            # Open and process the output file to check assertions
            with open("output", "r") as f:
                output = f.read().strip()  # Consider leading/trailing whitespace

            # Check if there are no winners and at least one tie statement
            assert not re.search(
                r"\bis a winner!", output
            ), "Unexpected winner message found."
            assert re.search(r"It is a tie!", output), "Expected tie message not found."
            print("SmartAI output is correct +4/4 points")
            extra_credit += 4

        except AssertionError:
            _, exc_value, _ = sys.exc_info()  # Captures the exception value
            print("SmartAI output is incorrect +0/4 points")
            print(exc_value)  # Prints just the error message from the exception

    # output results
    print(f"Total score: {score}/{total} points")
    print(f"Extra credit: {extra_credit}/{5} points")
    score += extra_credit
    with open("tmp", "w") as f:
        f.write(str(score))
